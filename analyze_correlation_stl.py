import json, re, sys
from multiprocessing import Pool
from collections import Counter
from math import log
from pathlib import Path

import pandas as pd
from scipy import stats

from stl import ParseError, parse, strip_intervals, to_str
import stl_equiv
from stl_equiv import semantically_equivalent

UNCLEAR = {2, 4, 10, 14, 19, 22, 23, 25, 28, 30, 31, 33, 37, 39, 40, 47, 48, 55, 57, 
           58, 60, 69, 74, 76, 77, 78, 82, 83, 85, 86, 88, 91, 94, 97, 108, 110, 113, 
           116, 117, 118, 120, 122, 124, 125, 133, 134, 136, 141, 142, 143, 151, 153, 
           157, 173, 174, 177, 185, 186, 188, 191, 194, 196, 198 } 

BAD_GOLD = {1, 12, 29, 34, 64, 68, 87, 92, 105, 121, 127, 146, 154, 164, 166, 167, 179} # ids whose gold formula are incorrect; these items are dropped from every metric


def formula_of(sample):
    f = sample if isinstance(sample, str) else (sample.get("corrected_formula") or sample["formula"])
    f = re.sub(r"^\s*(?:(?:FINAL|STL)\s*:\s*)+", "", f, flags=re.I)  # Qwen's "FINAL: STL:" prefixes
    return f.replace("¬", "!").replace("∧", "&&").replace("∨", "||").replace("→", "->").strip()


# Pair verdicts: CACHE is loaded from disk (read-only in workers), NEW collects this process's additions.
CACHE, NEW = {}, {}
CACHE_VERSION = f"z3;timeout_ms={stl_equiv.TIMEOUT_MS};v1"
TOUCHED = set()  # pair keys looked up while processing the current item


def equivalent(a, b):
    """True / False, or None if Z3 could not decide (or a formula is unparseable).
    None is never equal to True, so undecided pairs end up in separate clusters."""
    key = (a, b) if a <= b else (b, a)
    TOUCHED.add(key)
    if key in CACHE:
        return CACHE[key]
    if key not in NEW:
        NEW[key] = semantically_equivalent(a, b)[0]
    return NEW[key]


def load_cache(path):
    if path.exists():
        blob = json.load(open(path, encoding="utf-8"))
        if blob["version"] == CACHE_VERSION:
            CACHE.update({(a, b): v for a, b, v in blob["pairs"]})


def save_cache(path):
    pairs = [[a, b, v] for (a, b), v in {**CACHE, **NEW}.items()]
    json.dump({"version": CACHE_VERSION, "pairs": pairs}, open(path, "w", encoding="utf-8"))


def parses(f):
    try:
        parse(f)
        return True
    except ParseError:
        return False


NOT_EXPRESSIBLE = -1  # one shared class for every unparseable sample


def structural(f):
    try:
        return to_str(strip_intervals(parse(f)))
    except ParseError:
        return f


def cluster(formulas, strip=False):
    """Class label per sample: semantic-equivalence class id, or NOT_EXPRESSIBLE if unparseable.
    strip=True ignores interval bounds."""
    if strip:
        formulas = [structural(f) for f in formulas]
    reps, labels = [], []
    for f in formulas:
        if not parses(f):
            labels.append(NOT_EXPRESSIBLE)
            continue
        for i, r in enumerate(reps):
            if equivalent(f, r):
                labels.append(i); break
        else:
            reps.append(f); labels.append(len(reps) - 1)
    return labels, reps


def vote_correct(labels, reps, gold):
    """Is the semantic-majority answer among `labels` equivalent to gold?
    Unparseable samples don't vote; ties go to the class that appeared first."""
    votes = Counter(l for l in labels if l != NOT_EXPRESSIBLE)
    if not votes:
        return False
    best = max(votes.items(), key=lambda kv: (kv[1], -kv[0]))[0]
    return equivalent(reps[best], gold) is True


def norm_entropy(counts):
    n = sum(counts)
    return -sum(c / n * log(c / n) for c in counts if c) / log(n) if n > 1 else 0.0


def item_row(args):
    """One item's metrics (runs in a worker). Returns (row, new cache entries)."""
    k, item = args
    NEW.clear()
    TOUCHED.clear()
    fs = [formula_of(s) for s in item["samples"]]
    labels, reps = cluster(fs)
    counts = pd.Series(labels).value_counts()
    s_counts = pd.Series(cluster(fs, strip=True)[0]).value_counts()
    gold = item.get("stl") or item.get("ltl")
    acc = (sum(equivalent(f, gold) is True for f in fs) / len(fs)) if gold else float("nan")
    row = dict(
        id=k, nl=item["nl"], unclear=int(int(k) in UNCLEAR), n_samples=len(fs),
        n_unparsed=labels.count(NOT_EXPRESSIBLE),
        n_undecided=sum((CACHE[k] if k in CACHE else NEW[k]) is None for k in TOUCHED),
        n_classes=len(counts),
        norm_entropy=norm_entropy(counts.tolist()),
        majority_share=counts.iloc[0] / len(labels),
        struct_n_classes=len(s_counts),
        struct_norm_entropy=norm_entropy(s_counts.tolist()),
        struct_majority_share=s_counts.iloc[0] / len(labels),
        gold_acc=acc,
        **({f"vote_correct_{n}": vote_correct(labels[:n], reps, gold) for n in range(1, len(fs) + 1)} if gold else {}),
    )
    return row, dict(NEW)


def analyze(path, out_dir):
    data = {k: v for k, v in json.load(open(path, encoding="utf-8")).items() if int(k) not in BAD_GOLD}
    cache_path = out_dir / "equiv_cache.json"
    load_cache(cache_path)
    empty = [k for k, v in data.items() if not v["samples"]]
    if empty:
        print(f"WARNING {path.name}: skipping {len(empty)} items with no samples: {empty}")
    items = [(k, v) for k, v in data.items() if v["samples"]]
    with Pool() as pool:  # workers fork after the cache is loaded
        results = pool.map(item_row, items, chunksize=1)
    rows = [r for r, _ in results]
    for _, new in results:
        NEW.update(new)
    save_cache(cache_path)
    df = pd.DataFrame(rows)
    df.to_csv(out_dir / f"metrics_{path.stem}.csv", index=False)
    report(df, path.name)


def report(df, name):
    print(f"\n=== {name} === (unparsed samples: {df.n_unparsed.sum()}/{df.n_samples.sum()}, "
          f"undecided pairs: {df.n_undecided.sum()})")
    metrics = ["n_classes", "norm_entropy", "majority_share", "struct_n_classes", "struct_norm_entropy", "struct_majority_share", "n_unparsed"] + (["gold_acc"] if df.gold_acc.notna().all() else [])
    print(df.groupby("unclear")[metrics].agg(["mean", "std", "count"]).round(3).T, "\n")
    for m in metrics:
        d = df.dropna(subset=[m])  # only gold_acc can be NaN
        a, b = d[d.unclear == 1][m], d[d.unclear == 0][m]
        u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        rho, p_rho = stats.spearmanr(d.unclear, d[m])
        print(f"{m:22s} MWU p={p:.3f}  rank-biserial={2 * u / (len(a) * len(b)) - 1:+.2f}  spearman={rho:+.2f} (p={p_rho:.3f})")
    vcols = [c for c in df.columns if c.startswith("vote_correct_")]
    if vcols:
        acc_k = df[vcols].astype(float).groupby(df.unclear).mean().T
        acc_k.insert(0, "all", df[vcols].astype(float).mean())
        acc_k.index = [int(c.rsplit("_", 1)[1]) for c in vcols]
        acc_k = acc_k.rename(columns={0: "clear", 1: "unclear"})
        acc_k.index.name = "k_samples"
        print("\nmajority-vote accuracy vs gold using the first k samples:\n", acc_k.round(3))
    if "gold_acc" in metrics:
        print("spearman(n_classes, gold_acc) =", round(stats.spearmanr(df.n_classes, df.gold_acc)[0], 2))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--report"]
    folder = Path(args[0] if args else "raw_samples_stl")
    if "--report" in sys.argv:  # print the summary from saved CSVs; no recomputation
        files = sorted(folder.glob("metrics_*.csv"))
        if not files:
            sys.exit(f"no metrics_*.csv in {folder}")
        for f in files:
            df = pd.read_csv(f)
            df["unclear"] = df.id.isin(UNCLEAR).astype(int)  # reflect the current UNCLEAR set
            report(df, f.name)
    else:
        files = sorted(folder.glob("raw_samples*.json"))
        if not files:
            sys.exit(f"no raw_samples*.json in {folder}")
        for f in files:
            analyze(f, folder)