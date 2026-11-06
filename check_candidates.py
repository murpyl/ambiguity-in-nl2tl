"""Screen candidate JSONL with Spot; export solver reports and eligible candidates."""

import argparse
from collections import Counter
import json
from pathlib import Path

from ltl import parse


def load_candidates(path):
    items, seen = [], set()
    with Path(path).open(encoding="utf-8-sig") as source:
        for line_number, line in enumerate(source, 1):
            try:
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ValueError("expected a JSON object")
                candidate_id = item.get("item_id")
                if not isinstance(candidate_id, str) or not candidate_id.strip():
                    raise ValueError("item_id must be a nonempty string")
                if candidate_id in seen:
                    raise ValueError(f"duplicate item_id: {candidate_id}")
            except ValueError as exc:
                raise ValueError(f"{path}:{line_number}: {exc}") from exc
            seen.add(candidate_id)
            items.append(item)
    if not items:
        raise ValueError("input contains no candidates")
    return items


def atoms(node):
    if node[0] == "atom":
        return {node[1]}
    return set().union(*(atoms(child) for child in node[1:]))


def validate_item(item):
    for field in ("item_id", "family_id", "contrast_id", "ambiguous_text"):
        if not isinstance(item.get(field), str) or not item[field].strip():
            raise ValueError(f"{field} must be a nonempty string")
    propositions = item.get("propositions")
    if not isinstance(propositions, dict) or not propositions:
        raise ValueError("propositions must be a nonempty object")
    if any(not isinstance(value, str) or not value.strip()
           for value in propositions.values()):
        raise ValueError("proposition definitions must be nonempty strings")
    readings = item.get("readings")
    if not isinstance(readings, list) or len(readings) < 2:
        raise ValueError("readings must contain at least two objects")
    seen = set()
    for index, reading in enumerate(readings):
        if not isinstance(reading, dict):
            raise ValueError(f"readings[{index}] must be an object")
        for field in ("reading_id", "plain", "ltl", "clear_rewrite"):
            if not isinstance(reading.get(field), str) or not reading[field].strip():
                raise ValueError(f"readings[{index}].{field} must be nonempty text")
        rid = reading["reading_id"]
        if rid in seen:
            raise ValueError(f"duplicate reading_id: {rid}")
        seen.add(rid)
        undefined = atoms(parse(reading["ltl"])) - propositions.keys()
        if undefined:
            raise ValueError(f"{rid}: undefined propositions: {sorted(undefined)}")


def load_solver():
    try:
        import spot
        if not all(hasattr(spot, name) for name in ("formula", "translate", "version")):
            raise ImportError("installed 'spot' module is not the Spot LTL library")
        from ltl_equiv import semantically_equivalent
    except ImportError as exc:
        raise RuntimeError(
            f"Spot LTL Python bindings required: {exc}. "
            "See https://spot.lre.epita.fr/install.html"
        ) from exc
    return semantically_equivalent, spot.version()


def screen(item, equivalent):
    result = dict(item)
    result["human_validation_status"] = "not_assessed"
    try:
        validate_item(item)
        readings = item["readings"]
        classes = [[reading["reading_id"]] for reading in readings]
        pairwise = []
        for i, left in enumerate(readings):
            for right in readings[i + 1:]:
                same, detail = equivalent(left["ltl"], right["ltl"])
                if same is None:
                    raise ValueError(f"undecided pair {left['reading_id']}/{right['reading_id']}: {detail}")
                pairwise.append({
                    "reading_ids": [left["reading_id"], right["reading_id"]],
                    "equivalent": same,
                    "solver_witness": detail if not same else None,
                })
                if same:
                    left_class = next(group for group in classes if left["reading_id"] in group)
                    right_class = next(group for group in classes if right["reading_id"] in group)
                    if left_class is not right_class:
                        left_class.extend(right_class)
                        classes.remove(right_class)
        result["pairwise_checks"] = pairwise
        result["reading_classes"] = classes
        result["k_candidate"] = len(classes)
        status = "inequivalent" if len(classes) >= 2 else "equivalent"
        detail = None
    except (ValueError, RuntimeError) as exc:
        status, detail = "error", str(exc)
    result["solver_status"] = status
    result["solver_detail"] = detail
    return result


def write_jsonl(path, items):
    with path.open("w", encoding="utf-8", newline="\n") as output:
        for item in items:
            output.write(json.dumps(item, ensure_ascii=False) + "\n")


def run(input_path, output_dir):
    input_path = Path(input_path)
    items = load_candidates(input_path)
    equivalent, version = load_solver()
    output_dir = Path(output_dir)
    # A fresh directory prevents stale or accidentally overwritten screening outputs.
    output_dir.mkdir(parents=True, exist_ok=False)
    report, eligible = [], []
    for item in items:
        result = screen(item, equivalent)
        result["spot_version"] = version
        if result["solver_status"] == "inequivalent":
            eligible.append(result)
        report.append(result)
    for name, records in (("solver_report", report), ("eligible", eligible)):
        write_jsonl(output_dir / f"{input_path.stem}_{name}.jsonl", records)
    counts = Counter(item["solver_status"] for item in report)
    print(f"Spot {version}: {len(items)} checked; "
          f"{counts['inequivalent']} solver eligible; "
          f"{counts['equivalent']} equivalent (rejected); {counts['error']} errors")
    print(f"Outputs: {output_dir.resolve()}")
    return 1 if counts["error"] else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="candidate JSONL file")
    parser.add_argument("--out-dir", required=True, type=Path,
                        help="new directory for solver reports and eligible candidates")
    args = parser.parse_args()
    try:
        return run(args.input, args.out_dir)
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
