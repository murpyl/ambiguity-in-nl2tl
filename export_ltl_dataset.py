"""Export one ambiguous row and one clear row per endorsed LTL reading.

Usage: python export_ltl_dataset.py reviewed.jsonl --out final.jsonl --expected-pairs 67
Requires real Spot LTL bindings. Never modifies the reviewed input.
"""

import argparse
from collections import Counter
import json
from pathlib import Path

from dataset_checks import check_dataset, read_jsonl


def rows_for(records):
    rows = []
    for record in records:
        endorsements = Counter(
            rid
            for response in record["annotations"]["assessment"]
            for rid, supported in response["supports"].items()
            if supported is True
        )
        readings = [r for r in record["readings"] if endorsements[r["reading_id"]] >= 2]
        shared = {key: record[key] for key in ("family_id", "contrast_id", "propositions", "split")}
        rows.append({**shared, "item_id": record["item_id"] + ":ambiguous",
                     "pair_id": record["item_id"], "kind": "ambiguous",
                     "text": record["ambiguous_text"],
                     "readings": [{"reading_id": r["reading_id"], "ltl": r["ltl"]}
                                  for r in readings]})
        for reading in readings:
            rid = reading["reading_id"]
            rows.append({**shared, "item_id": record["item_id"] + ":clear:" + rid,
                         "pair_id": record["item_id"], "kind": "clear",
                         "text": reading["clear_rewrite"], "reading_id": rid,
                         "ltl": reading["ltl"]})
    return rows


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("input", type=Path)
    cli.add_argument("--out", required=True, type=Path)
    cli.add_argument("--expected-pairs", type=int, default=67)
    args = cli.parse_args()
    if args.input.resolve() == args.out.resolve():
        cli.error("input and output must differ")
    if args.out.exists():
        cli.error("output already exists")
    try:
        records = read_jsonl(args.input)
        issues = check_dataset(records, "final")
    except (OSError, ValueError, RuntimeError) as exc:
        cli.exit(2, f"error: {exc}\n")
    if len(records) != args.expected_pairs:
        issues.append(f"expected {args.expected_pairs} pairs, found {len(records)}")
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        cli.exit(1, f"No export: {len(issues)} validation issue(s)\n")
    rows = rows_for(records)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("x", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Exported {len(rows)} rows from {len(records)} reviewed pairs to {args.out}")


if __name__ == "__main__":
    main()
