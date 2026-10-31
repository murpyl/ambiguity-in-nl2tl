"""NL vagueness/ambiguity vs. semantic diversity of sampled LTL answers.

Semantic equivalence is exact (spot, via ltl_equiv).
Usage: python analyze_correlation.py [folder]   (default: raw_samples)
Reads folder/raw_samples*.json, writes folder/metrics_<name>.csv per file.
"""
import json, sys
from math import log
from pathlib import Path

import pandas as pd
import spot
from scipy import stats

from ltl_eval import clean, cluster as semantic_cluster, parse

UNCLEAR = {12, 15, 21, 24, 27, 28, 29, 30, 32}  # 0-indexed ambiguous + vague


def formula_of(sample):
    return clean(sample)


def parsed(s):
    return parse(s)


def equivalent(a, b):
    """True/False, or None if either side is unparseable."""
    fa, fb = parsed(a), parsed(b)
    return None if fa is None or fb is None else spot.are_equivalent(fa, fb)


NOT_EXPRESSIBLE = -1


def cluster(formulas):
    """Class label per sample: semantic-equivalence class id, or NOT_EXPRESSIBLE if unparseable."""
    labels, _ = semantic_cluster(formulas)
    return [NOT_EXPRESSIBLE if label is None else label for label in labels]


def norm_entropy(counts):
    n = sum(counts)
    return -sum(c / n * log(c / n) for c in counts if c) / log(n) if n > 1 else 0.0


def analyze(path, out_dir):
    data = json.load(open(path, encoding="utf-8"))
    rows = []
    for k, item in data.items():
        fs = [formula_of(s) for s in item["samples"]]
        labels = cluster(fs)
        counts = pd.Series([label for label in labels if label != NOT_EXPRESSIBLE]).value_counts()
        gold = item.get("ltl")
        acc = (sum(equivalent(f, gold) is True for f in fs) / len(fs)) if gold else float("nan")
        rows.append(dict(
            id=k, nl=item["nl"], unclear=int(int(k) in UNCLEAR), n_samples=len(fs),
            n_unparsed=labels.count(NOT_EXPRESSIBLE),
            n_classes=len(counts) if len(counts) else float("nan"),
            norm_entropy=norm_entropy(counts.tolist()) if len(counts) else float("nan"),
            majority_share=counts.iloc[0] / counts.sum() if len(counts) else float("nan"),
            gold_acc=acc,
        ))
    df = pd.DataFrame(rows)
    df.to_csv(out_dir / f"metrics_{path.stem}.csv", index=False)

    print(f"\n=== {path.name} === (unparsed samples: {df.n_unparsed.sum()}/{df.n_samples.sum()})")
    metrics = ["n_classes", "norm_entropy", "majority_share", "n_unparsed"] + (["gold_acc"] if df.gold_acc.notna().all() else [])
    print(df.groupby("unclear")[metrics].agg(["mean", "std", "count"]).round(3).T, "\n")
    for m in metrics:
        d = df.dropna(subset=[m])  # only gold_acc can be NaN
        a, b = d[d.unclear == 1][m], d[d.unclear == 0][m]
        u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        rho, p_rho = stats.spearmanr(d.unclear, d[m])
        print(f"{m:15s} MWU p={p:.3f}  rank-biserial={2 * u / (len(a) * len(b)) - 1:+.2f}  spearman={rho:+.2f} (p={p_rho:.3f})")
    if "gold_acc" in metrics:
        print("spearman(n_classes, gold_acc) =", round(stats.spearmanr(df.n_classes, df.gold_acc)[0], 2))


if __name__ == "__main__":
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else "raw_samples")
    files = sorted(folder.glob("raw_samples*.json"))
    if not files:
        sys.exit(f"no raw_samples*.json in {folder}")
    for f in files:
        analyze(f, folder)
