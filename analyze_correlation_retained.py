"""NL vagueness/ambiguity vs. semantic diversity of sampled LTL answers.

Semantic equivalence is exact (spot, via ltl_equiv).
Usage: python analyze_correlation_retained.py [folder]   (default: retained_translations)
Reads folder/raw_samples*.json, writes metrics and paired comparisons per file.
"""
import json, sys
from math import log
from pathlib import Path

import pandas as pd
import spot
from scipy import stats

from ltl_eval import clean, cluster as semantic_cluster, parse


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
        golds = item["gold_formulas"]
        acc = (sum(any(equivalent(f, gold) is True for gold in golds) for f in fs) / len(fs)) if golds and fs else float("nan")
        unclear = int(item["kind"] == "ambiguous")
        rows.append(dict(
            id=k, nl=item["nl"], unclear=unclear,
            pair_id=item.get("pair_id"), family_id=item.get("family_id"),
            kind=item.get("kind"), n_samples=len(fs),
            n_unparsed=labels.count(NOT_EXPRESSIBLE),
            n_classes=len(counts) if len(counts) else float("nan"),
            norm_entropy=norm_entropy(counts.tolist()) if len(counts) else float("nan"),
            majority_share=counts.iloc[0] / counts.sum() if len(counts) else float("nan"),
            gold_acc=acc,
        ))
    df = pd.DataFrame(rows)
    df.to_csv(out_dir / f"metrics_{path.stem}.csv", index=False)

    if df.empty:
        print(f"{path.name}: empty cache")
        return
    config_path = out_dir / "config.json"
    expected = json.loads(config_path.read_text()).get("samples") if config_path.exists() else None
    all_rows = df
    if expected:
        df = df[df.n_samples >= expected]
        print(f"{path.name}: {len(df)}/{len(all_rows)} statements have {expected} samples")
        if df.empty:
            print("No complete statements to analyze.")
            return
    print(f"\n=== {path.name} === (unparsed samples: {df.n_unparsed.sum()}/{df.n_samples.sum()})")
    metrics = ["n_classes", "norm_entropy", "majority_share", "n_unparsed"] + (["gold_acc"] if df.gold_acc.notna().all() else [])
    print(df.groupby("unclear")[metrics].agg(["mean", "std", "count"]).round(3).T, "\n")
    for m in metrics:
        d = df.dropna(subset=[m])  # only gold_acc can be NaN
        a, b = d[d.unclear == 1][m], d[d.unclear == 0][m]
        if a.empty or b.empty:
            print(f"{m}: need samples from both clear and ambiguous statements")
            continue
        u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        rho, p_rho = stats.spearmanr(d.unclear, d[m])
        print(f"{m:15s} MWU p={p:.3f}  rank-biserial={2 * u / (len(a) * len(b)) - 1:+.2f}  spearman={rho:+.2f} (p={p_rho:.3f})")
    if "gold_acc" in metrics:
        print("spearman(n_classes, gold_acc) =", round(stats.spearmanr(df.n_classes, df.gold_acc)[0], 2))
    if df.pair_id.notna().all():
        paired_analysis(all_rows, path, out_dir, metrics, expected)


def paired_analysis(df, path, out_dir, metrics, expected=None):
    # Each ambiguous item is compared with the mean of its own clear rewrites.
    # Require complete, equally sampled pairs so interrupted runs cannot bias comparisons.
    target = expected or df.n_samples.max()
    rows = []
    for pair_id, group in df.groupby("pair_id"):
        ambiguous = group[group.kind == "ambiguous"]
        clear_rows = group[group.kind == "clear"]
        if len(ambiguous) != 1 or clear_rows.empty or target == 0 or (group.n_samples != target).any():
            continue
        row = {"pair_id": pair_id, "family_id": group.family_id.iloc[0],
               "n_clear": len(clear_rows), "n_samples": target}
        for metric in metrics:
            row["ambiguous_" + metric] = ambiguous[metric].iloc[0]
            row["clear_mean_" + metric] = clear_rows[metric].mean()
            row["delta_" + metric] = row["ambiguous_" + metric] - row["clear_mean_" + metric]
        rows.append(row)
    paired = pd.DataFrame(rows)
    paired.to_csv(out_dir / f"paired_{path.stem}.csv", index=False)
    print(f"Paired comparisons: {len(paired)} complete pairs (ambiguous minus mean clear).")
    for metric in metrics:
        if paired.empty:
            break
        deltas = paired["delta_" + metric].dropna()
        if deltas.empty:
            continue
        p = stats.wilcoxon(deltas).pvalue if (deltas != 0).any() else 1.0
        print(f"{metric:15s} mean delta={deltas.mean():+.3f} paired Wilcoxon p={p:.4g}")


if __name__ == "__main__":
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else "retained_translations")
    files = sorted(folder.glob("raw_samples*.json"))
    if not files:
        sys.exit(f"no raw_samples*.json in {folder}")
    for f in files:
        analyze(f, folder)
