"""Pilot ambiguity classifier from sampled NL->LTL translations. UNTESTED sketch.

Inputs
  folder/raw_samples_<model>.json   (your self_consistency.py output, one per model)
  labels.csv                        columns: id,label   (1 = ambiguous/unclear, 0 = clear)
Usage: python classifier_pilot.py [folder] [labels.csv]

Requires: spot (conda-forge), pandas, numpy, scikit-learn
With ~36 items this is a feasibility check, NOT evidence. Do not tune on it and report it.
"""
import json, sys
from collections import Counter
from math import log
from pathlib import Path

import numpy as np
import pandas as pd
import spot
from ltl_eval import clean, cluster, parse
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mutual_info_score, roc_auc_score, average_precision_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

TAU = 0.10  # a class is "substantial" if it holds >= TAU of parsed samples


def norm_entropy(counts):
    n = sum(counts)
    return -sum(c / n * log(c / n) for c in counts if c) / log(n) if n > 1 else 0.0


def item_features(samples_by_model):
    """samples_by_model: {model: [formula strings]}. Uses only the samples, never the gold."""
    flat = [(m, s) for m, ss in samples_by_model.items() for s in ss]
    labels, _ = cluster([s for _, s in flat])
    models = [m for (m, _), l in zip(flat, labels) if l is not None]
    cls = [l for l in labels if l is not None]
    n = len(cls)
    if n == 0:
        return None
    counts = Counter(cls)
    shares = sorted((c / n for c in counts.values()), reverse=True)
    support = {c: len({m for m, l in zip(models, cls) if l == c}) for c in counts}
    per_model = []
    for m in samples_by_model:
        mc = {l for mm, l in zip(models, cls) if mm == m}
        per_model.append(len(mc))
    return dict(
        n_classes=len(counts),
        n_big=sum(s >= TAU for s in shares),
        entropy=norm_entropy(list(counts.values())),
        top2_share=shares[1] if len(shares) > 1 else 0.0,
        shared_mass=sum(c for k, c in counts.items() if support[k] >= 2) / n,
        model_mi=mutual_info_score(models, cls),   # high = classes are model-specific
        within_model_classes=float(np.mean(per_model)),
        unparsed_frac=1 - n / len(flat),
    )


def load(folder):
    items = {}
    for path in sorted(Path(folder).glob("raw_samples_*.json")):
        model = path.stem.replace("raw_samples_", "")
        for k, item in json.load(open(path, encoding="utf-8")).items():
            d = items.setdefault(k, {"nl": item["nl"], "gold": item["ltl"], "by_model": {}})
            d["by_model"][model] = [clean(s) for s in item["samples"]]
    return items


def build_table(items, labels):
    rows = []
    for k, d in items.items():
        f = item_features(d["by_model"])
        if f is None or k not in labels:
            continue
        gold = parse(d["gold"])
        rows.append(dict(
            id=k, label=labels[k], **f,
            nl_words=len(d["nl"].split()),                      # complexity controls
            gold_len=len(d["gold"].replace(" ", "")),
            gold_props=len(spot.atomic_prop_collect(gold)) if gold else np.nan,
        ))
    return pd.DataFrame(rows)


FEATURE_SETS = {
    "class_count": ["n_classes"],
    "entropy": ["entropy"],
    "dominance": ["top2_share", "n_big"],
    "complexity_only": ["nl_words", "gold_len"],
    "cross_model": ["shared_mass", "model_mi"],
    "small_combo": ["entropy", "top2_share", "shared_mass"],
    "small_combo+complexity": ["entropy", "top2_share", "shared_mass", "nl_words", "gold_len"],
}


def cv_scores(df, cols, repeats=50, seed=0, permute=False):
    cols = [c for c in cols if df[c].nunique() > 1]
    if not cols:
        return None
    X, y = df[cols].fillna(0).values, df["label"].values
    rng = np.random.default_rng(seed)
    model = make_pipeline(StandardScaler(), LogisticRegression(C=0.5, class_weight="balanced"))
    folds = min(5, int(y.sum()), int((1 - y).sum()))
    probas, aucs = [], []
    for r in range(repeats):
        yy = rng.permutation(y) if permute else y
        p = cross_val_predict(model, X, yy, method="predict_proba",
                              cv=StratifiedKFold(folds, shuffle=True, random_state=r))[:, 1]
        probas.append(p)
        aucs.append(roc_auc_score(yy, p))
    mean_p = np.mean(probas, axis=0)
    # bootstrap over items for a CI on the averaged out-of-fold scores
    boots = []
    for _ in range(1000):
        idx = rng.integers(0, len(y), len(y))
        if len(set(y[idx])) == 2:
            boots.append(roc_auc_score(y[idx], mean_p[idx]))
    return np.mean(aucs), np.std(aucs), np.percentile(boots, [2.5, 97.5]), average_precision_score(y, mean_p)


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "raw_samples"
    labels = pd.read_csv(sys.argv[2] if len(sys.argv) > 2 else "labels.csv", dtype={"id": str}).set_index("id")["label"].to_dict()
    df = build_table(load(folder), labels)
    df.to_csv("pilot_features.csv", index=False)
    print(f"{len(df)} items, {int(df.label.sum())} positive. unparsed samples: mean {df.unparsed_frac.mean():.3f}\n")
    print(f"{'feature set':26s} AUROC(mean±sd over CV repeats)  95% CI (item bootstrap)  AUPRC")
    for name, cols in FEATURE_SETS.items():
        res = cv_scores(df, cols)
        if res is None:
            print(f"{name:26s} skipped (no varying features; need >1 model for cross-model features)")
            continue
        m, s, ci, ap = res
        print(f"{name:26s} {m:.3f} ± {s:.3f}              [{ci[0]:.2f}, {ci[1]:.2f}]            {ap:.3f}")
    m, s, ci, ap = cv_scores(df, FEATURE_SETS["small_combo"], permute=True)
    print(f"{'(shuffled labels, sanity)':26s} {m:.3f} ± {s:.3f}   <- should sit near 0.5")
    show = df.sort_values("n_classes", ascending=False)[["id", "label", "n_classes", "entropy", "top2_share", "unparsed_frac"]]
    print("\nPer-item diversity (check that high-diversity NEGATIVES are not just hard sentences):")
    print(show.round(2).to_string(index=False))
    base = (df.n_classes > 1)
    print(f"\nentropy>0 rule: flags {base.mean():.0%} of items; precision {df.label[base].mean():.2f}, "
          f"recall {base[df.label == 1].mean():.2f}")
