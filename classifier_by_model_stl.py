"""Run the ambiguity classifier separately for each model.

Usage: python classifier_by_model.py [folder] [labels.csv] [-v]
  folder (default raw_samples_stl) holds raw_samples_<model>.json, one file per model.
Writes folder/features_<model>.csv per model and folder/results_by_model.csv; prints a model x feature-set AUROC table.
Cross-model features (shared_mass, model_mi) are constant within one model and are dropped automatically.
"""
import logging
import sys
from pathlib import Path

import pandas as pd

from classifier_stl import FEATURE_SETS, build_table, cv_scores, load

logger = logging.getLogger("classifier_by_model")


def run_model(path, labels, folder):
    """List of result rows (one per feature set + a shuffled-label sanity row) for one model file."""
    model = path.stem.replace("raw_samples_", "")
    df = build_table(load(folder, pattern=path.name), labels)
    df.to_csv(folder / f"features_{model}.csv", index=False)
    pos, neg = int(df.label.sum()), int((1 - df.label).sum())
    logger.info("%s: %d items (%d positive, %d negative), unparsed mean %.3f",
                model, len(df), pos, neg, df.unparsed_frac.mean())
    if min(pos, neg) < 2:
        logger.warning("%s: skipped, need at least 2 items per class", model)
        return []
    rows = []
    runs = [(name, cols, False) for name, cols in FEATURE_SETS.items()]
    runs.append(("(shuffled labels, sanity)", FEATURE_SETS["small_combo"], True))
    for name, cols, permute in runs:
        res = cv_scores(df, cols, permute=permute)
        if res is None:
            logger.info("%s: %s skipped (no varying features)", model, name)
            continue
        m, sd, ci, ap = res
        rows.append(dict(model=model, feature_set=name, n_items=len(df), n_pos=pos,
                         auroc=m, auroc_sd=sd, ci_lo=ci[0], ci_hi=ci[1], auprc=ap))
    return rows


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG if "-v" in sys.argv else logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
    args = [a for a in sys.argv[1:] if a != "-v"]
    folder = Path(args[0] if args else "raw_samples_stl")
    labels = pd.read_csv(args[1] if len(args) > 1 else "labels.csv", dtype={"id": str}).set_index("id")["label"].to_dict()
    paths = sorted(folder.glob("raw_samples_*.json"))
    if not paths:
        sys.exit(f"no raw_samples_*.json in {folder}")
    rows = []
    for i, path in enumerate(paths, 1):
        logger.info("model %d/%d: %s", i, len(paths), path.name)
        rows += run_model(path, labels, folder)
    res = pd.DataFrame(rows)
    res.to_csv(folder / "results_by_model.csv", index=False)
    table = res.pivot(index="feature_set", columns="model", values="auroc").reindex(res.feature_set.unique())
    print("\nAUROC by model (CV mean; see results_by_model.csv for sd, CI, AUPRC)\n")
    print(table.round(3).to_string())