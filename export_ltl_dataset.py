"""Export one ambiguous row and one clear row per endorsed LTL reading.

Usage: python export_ltl_dataset.py reviewed.jsonl --out final.jsonl
"""

import argparse
from collections import Counter
import json
from pathlib import Path

from dataset_checks import read_jsonl


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
    args = cli.parse_args()
    records = read_jsonl(args.input)
    rows = rows_for(records)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("x", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Exported {len(rows)} rows from {len(records)} reviewed pairs to {args.out}")


if __name__ == "__main__":
    main()
