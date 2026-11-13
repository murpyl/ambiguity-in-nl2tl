"""Train and evaluate ambiguity classifiers on cached NL-to-LTL translations."""

import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, balanced_accuracy_score, roc_auc_score
from sklearn.model_selection import LeaveOneGroupOut, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from classifier import FEATURE_SETS, item_features
from ltl_eval import clean


POOLED_FEATURES = {
    name: columns for name, columns in FEATURE_SETS.items()
    if "complexity" not in name
}
POOLED_FEATURES["length_only"] = ["nl_words"]
POOLED_FEATURES["small_combo+length"] = [*POOLED_FEATURES["small_combo"], "nl_words"]
SINGLE_FEATURES = {
    "class_count": FEATURE_SETS["class_count"],
    "small_combo": ["entropy", "top2_share", "n_big"],
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_features(folder):
    dataset = read_json(folder / "dataset.json")
    config = read_json(folder / "config.json")
    models, draws = config["models"], config["samples"]
    samples = {}
    for model in models:
        tag = model.replace("/", "_")
        path = folder / f"raw_samples_{tag}.json"
        cache = read_json(path)
        if cache.keys() != dataset.keys():
            raise ValueError(f"{path}: statement IDs differ from dataset.json")
        samples[model] = {}
        for key, item in cache.items():
            if any(item[field] != dataset[key][field]
                   for field in ("nl", "propositions", "kind", "pair_id", "family_id")):
                raise ValueError(f"{path}: statement metadata differs for {key}")
            if item["model"] != model or len(item["samples"]) != draws:
                raise ValueError(f"{path}: expected {draws} samples from {model} for {key}")
            samples[model][key] = [clean(sample) for sample in item["samples"]]

    rows = []
    for key, item in dataset.items():
        label = {"clear": 0, "ambiguous": 1}[item["kind"]]
        by_model = {model: samples[model][key] for model in models}
        pooled = item_features(by_model)
        for scope, features in [("pooled", pooled), *(
            (model, item_features({model: formulas})) for model, formulas in by_model.items()
        )]:
            if features is None:
                raise ValueError(f"No parseable translations for {key} in {scope}")
            rows.append({
                "id": key, "pair_id": item["pair_id"], "family_id": item["family_id"],
                "label": label, "scope": scope, "nl_words": len(item["nl"].split()), **features,
            })
    return pd.DataFrame(rows), models, draws


def estimator():
    return make_pipeline(StandardScaler(), LogisticRegression(C=0.5, class_weight="balanced"))


def evaluate(features):
    results, predictions = [], []
    for scope, rows in features.groupby("scope", sort=False):
        y = rows["label"]
        groups = rows["family_id"]
        folds = list(LeaveOneGroupOut().split(rows, y, groups))
        if any(y.iloc[train].nunique() < 2 or y.iloc[test].nunique() < 2 for train, test in folds):
            raise ValueError("Each held-out family and its training split need both classes")
        feature_sets = POOLED_FEATURES if scope == "pooled" else SINGLE_FEATURES
        for name, columns in feature_sets.items():
            score = cross_val_predict(
                estimator(), rows[columns], y, cv=folds, method="predict_proba",
            )[:, 1]
            family_auc = [roc_auc_score(y.iloc[test], score[test]) for _, test in folds]
            results.append({
                "scope": scope, "feature_set": name,
                "auroc": roc_auc_score(y, score),
                "mean_family_auroc": sum(family_auc) / len(family_auc),
                "average_precision": average_precision_score(y, score),
                "balanced_accuracy": balanced_accuracy_score(y, score >= 0.5),
            })
            predictions.append(rows[["id", "pair_id", "family_id", "label", "scope"]].assign(
                feature_set=name, ambiguity_score=score,
            ))
    return pd.DataFrame(results), pd.concat(predictions, ignore_index=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", nargs="?", type=Path, default=Path("retained_translations"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or args.folder / "classifier"
    features, models, draws = build_features(args.folder)
    scores, predictions = evaluate(features)

    pooled = features[features["scope"] == "pooled"]
    columns = POOLED_FEATURES["small_combo"]
    fitted = estimator().fit(pooled[columns], pooled["label"])
    output.mkdir(parents=True, exist_ok=True)
    features.to_csv(output / "features.csv", index=False)
    scores.to_csv(output / "scores.csv", index=False)
    predictions.to_csv(output / "predictions.csv", index=False)
    joblib.dump({
        "estimator": fitted, "feature_columns": columns, "translation_models": models,
        "samples_per_model": draws,
    }, output / "classifier.joblib")
    print(f"{len(pooled)} statements, {pooled.label.sum()} ambiguous, "
          f"{pooled.family_id.nunique()} held-out families, {draws} draws per model")
    print(f"Average precision baseline: {pooled.label.mean():.3f}")
    print(scores.round(3).to_string(index=False))
    print(f"Saved features, held-out scores, predictions and fitted classifier to {output}")


if __name__ == "__main__":
    main()
