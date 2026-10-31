"""Per-model analysis of the pilot. Imports classifier_pilot.py (same folder). UNTESTED sketch.

Usage: python classifier_by_model.py [folder] [labels.csv]

Prints:
  1. AUROC of each single feature, computed from ONE model's 10 samples only
  2. leave-one-model-out: pooled features without model m (does one model drive the signal?)
  3. per-item class count by model (see which models split on which items)
  4. standardized logistic-regression coefficients (descriptive only, fit on all data)
All AUROCs here use "higher feature = more ambiguous" with no fitting, so there is no CV;
the bootstrap CI is over items.
"""
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from classifier import FEATURE_SETS, build_table, item_features, load

FEATS = ["n_classes", "entropy", "top2_share", "n_big"]  # the ones meaningful for a single model
rng = np.random.default_rng(0)


def auc_ci(y, x, n=1000):
    y, x = np.asarray(y), np.asarray(x, dtype=float)
    if len(set(y)) < 2 or np.ptp(x) == 0:
        return np.nan, (np.nan, np.nan)
    boots = []
    for _ in range(n):
        i = rng.integers(0, len(y), len(y))
        if len(set(y[i])) == 2:
            boots.append(roc_auc_score(y[i], x[i]))
    return roc_auc_score(y, x), tuple(np.percentile(boots, [2.5, 97.5]))


folder = sys.argv[1] if len(sys.argv) > 1 else "raw_samples"
labels = pd.read_csv(sys.argv[2] if len(sys.argv) > 2 else "labels.csv",
                     dtype={"id": str}).set_index("id")["label"].to_dict()
items = load(folder)
models = sorted({m for d in items.values() for m in d["by_model"]})

# 1 + 3: per-model features
rows = []
for k, d in items.items():
    if k not in labels:
        continue
    for m in models:
        f = item_features({m: d["by_model"][m]})
        if f:
            rows.append(dict(id=k, model=m, label=labels[k], **{c: f[c] for c in FEATS}))
pm = pd.DataFrame(rows)

print("== 1. Single-model AUROC (features from that model's samples only) ==")
for m in models:
    s = pm[pm.model == m]
    for c in ["n_classes", "entropy"]:
        a, ci = auc_ci(s.label, s[c])
        print(f"{m:35s} {c:10s} AUROC {a:.2f}  CI [{ci[0]:.2f}, {ci[1]:.2f}]  "
              f"items with >1 class: {(s.n_classes > 1).mean():.0%}")

# 2: leave-one-model-out on pooled class count
print("\n== 2. Leave-one-model-out (pooled n_classes / entropy without model m) ==")
for m in models:
    vals = []
    for k, d in items.items():
        if k not in labels:
            continue
        f = item_features({mm: v for mm, v in d["by_model"].items() if mm != m})
        if f:
            vals.append((k, labels[k], f["n_classes"], f["entropy"]))
    v = pd.DataFrame(vals, columns=["id", "label", "n_classes", "entropy"])
    a, ci = auc_ci(v.label, v.n_classes)
    print(f"without {m:30s} n_classes AUROC {a:.2f}  CI [{ci[0]:.2f}, {ci[1]:.2f}]")

# 3: which models split on which items
print("\n== 3. Class count per model (rows sorted by label, then total) ==")
wide = pm.pivot(index="id", columns="model", values="n_classes")
wide.insert(0, "label", [labels[i] for i in wide.index])
wide["max"] = wide[models].max(axis=1)
print(wide.sort_values(["label", "max"], ascending=False).to_string())

# 4: descriptive coefficients on the pooled table (NOT an evaluation)
print("\n== 4. Standardized coefficients, fit on all 36 items (descriptive only) ==")
df = build_table(items, labels)
for name in ["small_combo", "small_combo+complexity"]:
    cols = FEATURE_SETS[name]
    clf = make_pipeline(StandardScaler(), LogisticRegression(C=0.5, class_weight="balanced"))
    clf.fit(df[cols].fillna(0), df.label)
    coefs = clf[-1].coef_[0]
    print(name, {c: round(float(w), 2) for c, w in zip(cols, coefs)})