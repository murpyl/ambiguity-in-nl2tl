"""Separate accepted-reading diversity from translation errors in the retained dataset."""

import argparse
import csv
import json
from collections import Counter
from math import isclose, log
from pathlib import Path
from statistics import mean

import pandas as pd
import spot
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import LeaveOneGroupOut, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from ltl_eval import clean, cluster, parse


def entropy(counts):
    total = sum(counts)
    return -sum(count / total * log(count / total) for count in counts if count)


def measure(formulas, golds):
    labels, representatives = cluster(formulas)
    counts = Counter(label for label in labels if label is not None)
    retained, outside = [], []
    for label, (_, representative) in enumerate(representatives):
        matches = sum(spot.are_equivalent(representative, gold) for gold in golds)
        if matches > 1:
            raise ValueError("Gold readings must be semantically distinct")
        (retained if matches else outside).append(counts[label])
    parsed = sum(counts.values())
    scale = log(parsed) if parsed > 1 else 1
    n_retained, n_outside = sum(retained), sum(outside)
    retained_entropy = n_retained / parsed * entropy(retained) / scale if parsed else 0
    outside_entropy = n_outside / parsed * entropy(outside) / scale if parsed else 0
    status_entropy = entropy([n_retained, n_outside]) / scale
    total_entropy = entropy(list(counts.values())) / scale
    assert isclose(total_entropy, retained_entropy + outside_entropy + status_entropy, abs_tol=1e-12)
    return {
        "classes": len(counts), "retained_classes": len(retained), "outside_classes": len(outside),
        "entropy": total_entropy, "retained_entropy": retained_entropy,
        "outside_entropy": outside_entropy, "status_entropy": status_entropy,
        "correct": n_retained, "unparseable": len(formulas) - parsed,
        "error_rate": 1 - n_retained / len(formulas),
    }


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def collect(folder, dataset, annotations):
    models = list(annotations["models"])
    caches, metrics = {}, {}
    for model in models:
        stem = f"raw_samples_{model}"
        caches[model] = read_json(folder / f"{stem}.json")
        with (folder / f"metrics_{stem}.csv").open(newline="", encoding="utf-8") as source:
            metrics[model] = {row["id"]: row for row in csv.DictReader(source)}
        assert caches[model].keys() == metrics[model].keys() == dataset.keys()
    individual, pooled = {}, {}
    for sample_id, item in dataset.items():
        golds = [parse(formula) for formula in item["gold_formulas"]]
        assert all(gold is not None for gold in golds)
        all_draws = []
        for model in models:
            entry = caches[model][sample_id]
            assert all(entry[key] == item[key] for key in ("nl", "kind", "pair_id", "gold_formulas"))
            draws = [clean(draw) for draw in entry["samples"]]
            assert len(draws) == annotations["draws_per_model"]
            row = measure(draws, golds)
            prior = metrics[model][sample_id]
            assert row["classes"] == int(float(prior["n_classes"]))
            assert isclose(row["entropy"], float(prior["norm_entropy"]), abs_tol=1e-12)
            assert row["correct"] / len(draws) == float(prior["gold_acc"])
            assert row["unparseable"] == int(prior["n_unparsed"])
            individual[sample_id, model] = row
            all_draws.extend(draws)
        pooled[sample_id] = measure(all_draws, golds)
    return individual, pooled


def paired_summary(dataset, annotations, individual):
    fields = ("classes", "retained_classes", "outside_classes", "entropy", "error_rate")
    pairs = annotations["pairs"]
    rows = []
    for pair_id, pair in pairs.items():
        ambiguous_id = f"{pair_id}:ambiguous"
        for model in annotations["models"]:
            ambiguous = individual[ambiguous_id, model]
            clear = [individual[sample_id, model] for sample_id in pair["clear_sample_ids"]]
            baseline = annotations["samples"][ambiguous_id]["difficulty_excluding_model"][model]["pair_error_rate"]
            reference_errors = [
                individual[sample_id, reference]["error_rate"]
                for sample_id in pair["clear_sample_ids"]
                for reference in annotations["models"]
                if reference != model
            ]
            assert isclose(baseline, mean(reference_errors), abs_tol=1e-12)
            rows.append({
                "model": model, "pair": pair_id, "family": dataset[ambiguous_id]["family_id"],
                "baseline": baseline, "ambiguous_multireading": ambiguous["retained_classes"] >= 2,
                **{field: ambiguous[field] - mean(item[field] for item in clear) for field in fields},
            })
    frame = pd.DataFrame(rows)
    low = frame[frame.baseline == 0]
    print("\nPAIRED AMBIGUOUS MINUS MEAN CLEAR, BASELINE COMPUTED WITHOUT THE EVALUATED MODEL")
    for label, group in [("all", frame), ("zero reference error", low),
                         ("positive reference error", frame[frame.baseline > 0])]:
        print(label, "model–pairs", len(group), "distinct pairs", group.pair.nunique(),
              "families", group.family.nunique(), group[list(fields)].mean().round(4).to_dict(),
              "ambiguous multireading", int(group.ambiguous_multireading.sum()))
    print(low.groupby("model")[["classes", "retained_classes", "outside_classes", "entropy", "error_rate"]]
          .agg(["size", "mean"]).round(4).to_string())
    by_family = low.groupby("family")[list(fields)].mean()
    print("Zero reference error by family\n" + by_family.round(4).to_string())
    print("Zero reference error, leave-one-family-out class gap range:",
          min(low[low.family != family].classes.mean() for family in by_family.index),
          max(low[low.family != family].classes.mean() for family in by_family.index))


def pooled_summary(dataset, annotations, pooled):
    fields = ("classes", "retained_classes", "outside_classes", "entropy", "retained_entropy",
              "outside_entropy", "status_entropy")
    rows = []
    for sample_id, item in dataset.items():
        level = annotations["samples"][sample_id]["translation_difficulty"]["difficulty_level"]
        result = pooled[sample_id]
        assert isclose(result["error_rate"], annotations["samples"][sample_id]["translation_difficulty"]["error_rate"])
        rows.append({"kind": item["kind"], "level": level, **result})
    frame = pd.DataFrame(rows)
    grouped = frame.groupby(["kind", "level"])
    table = grouped[list(fields)].mean().assign(n=grouped.size())
    print("\nPOOLED CLASS AND NORMALIZED ENTROPY COMPONENTS\n" + table.round(4).to_string())


def detection(folder, dataset, annotations):
    features = pd.read_csv(folder / "classifier" / "features.csv")
    frame = features[features.scope == "pooled"].copy()
    assert frame.id.is_unique and set(frame.id) == dataset.keys()
    assert all(row.label == (dataset[row.id]["kind"] == "ambiguous")
               and row.family_id == dataset[row.id]["family_id"] for row in frame.itertuples())
    frame["text"] = frame.id.map(lambda key: dataset[key]["nl"])
    frame["n_props"] = frame.id.map(lambda key: len(dataset[key]["propositions"]))
    frame["pair_error"] = frame.id.map(lambda key: annotations["samples"][key]["pair_difficulty"])
    y = frame.label
    folds = list(LeaveOneGroupOut().split(frame, y, frame.family_id))
    wording = ("wording", TfidfVectorizer(analyzer="char", ngram_range=(3, 5), min_df=2), "text")
    length = ("length", StandardScaler(), ["nl_words", "n_props"])
    diversity = ("diversity", StandardScaler(), ["entropy", "top2_share", "shared_mass"])
    designs = {
        "length + propositions": [length],
        "diversity": [diversity],
        "wording + length + propositions": [wording, length],
        "wording + length + propositions + diversity": [wording, length, diversity],
    }
    print("\nLEAVE-ONE-FAMILY-OUT AMBIGUITY DETECTION")
    for name, columns in designs.items():
        estimator = make_pipeline(ColumnTransformer(columns),
                                  LogisticRegression(C=0.5, class_weight="balanced"))
        score = cross_val_predict(estimator, frame, y, cv=folds, method="predict_proba")[:, 1]
        family_auc = [roc_auc_score(y.iloc[test], score[test]) for _, test in folds]
        frame[name] = score
        print(name, f"AUROC {roc_auc_score(y, score):.3f}, macro-family AUROC {mean(family_auc):.3f}, "
              f"AP {average_precision_score(y, score):.3f}")
    base, combined = list(designs)[-2:]
    for name in (base, combined):
        row = frame[frame.pair_error == 0]
        print("Zero pair error", name, len(row), f"AUROC {roc_auc_score(row.label, row[name]):.3f}")
    family_deltas = pd.Series({
        family: roc_auc_score(group.label, group[combined]) - roc_auc_score(group.label, group[base])
        for family, group in frame.groupby("family_id")
    })
    print("Per-family AUROC change\n" + family_deltas.round(3).to_string())
    clear = frame[frame.label == 0]
    for name, group in [("zero pair error", clear[clear.pair_error == 0]),
                        ("positive pair error", clear[clear.pair_error > 0])]:
        print("Clear false positives at 0.5,", name, len(group),
              {design: int((group[design] >= 0.5).sum()) for design in (base, combined)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, nargs="?", default=Path("retained_translations"))
    folder = parser.parse_args().folder
    dataset = read_json(folder / "dataset.json")
    annotations = read_json(folder / "sample_annotations.json")
    assert dataset.keys() == annotations["samples"].keys()
    individual, pooled = collect(folder, dataset, annotations)
    print(f"Validated {len(individual)} model–statement metrics against the saved Spot results.")
    paired_summary(dataset, annotations, individual)
    pooled_summary(dataset, annotations, pooled)
    detection(folder, dataset, annotations)


if __name__ == "__main__":
    main()
