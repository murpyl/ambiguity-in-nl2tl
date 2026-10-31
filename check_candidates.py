"""Screen candidate JSONL with Spot; export blinded English annotation forms."""

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
                candidate_id = item.get("candidate_id")
                if not isinstance(candidate_id, str) or not candidate_id.strip():
                    raise ValueError("candidate_id must be a nonempty string")
                if candidate_id in seen:
                    raise ValueError(f"duplicate candidate_id: {candidate_id}")
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
    for field in ("scenario", "ambiguous_text", "reading_a_plain", "reading_b_plain",
                  "reading_a_ltl", "reading_b_ltl"):
        if not isinstance(item.get(field), str) or not item[field].strip():
            raise ValueError(f"{field} must be a nonempty string")
    propositions = item.get("propositions")
    if not isinstance(propositions, dict) or not propositions:
        raise ValueError("propositions must be a nonempty object")
    if any(not isinstance(value, str) or not value.strip()
           for value in propositions.values()):
        raise ValueError("proposition definitions must be nonempty strings")
    for field in ("reading_a_ltl", "reading_b_ltl"):
        undefined = atoms(parse(item[field])) - propositions.keys()
        if undefined:
            raise ValueError(f"{field}: undefined propositions: {sorted(undefined)}")


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
        same, detail = equivalent(item["reading_a_ltl"], item["reading_b_ltl"])
        if same is True:
            status = "equivalent"
        elif same is False:
            status = "inequivalent"
        else:
            status = "error"
    except (ValueError, RuntimeError) as exc:
        status, detail = "error", str(exc)
    result["solver_status"] = status
    result["solver_detail"] = detail
    return result


def annotation_forms(item, annotation_id):
    # Explicit allowlist: never copy generator confidence, rationales, controls,
    # formulas, family labels, IDs, or proposed/solver witnesses into these forms.
    common = {
        "annotation_id": annotation_id,
        "scenario": item["scenario"],
        "propositions": item["propositions"],
        "requirement": item["ambiguous_text"],
        "annotator_id": None,
    }
    open_form = {**common, "interpretations": [], "comments": ""}
    assessment = {
        **common,
        "reading_a": item["reading_a_plain"],
        "reading_b": item["reading_b_plain"],
        "supports_a": None,
        "supports_b": None,
        "additional_interpretations": [],
        "comments": "",
    }
    return open_form, assessment


def write_jsonl(path, items):
    with path.open("w", encoding="utf-8", newline="\n") as output:
        for item in items:
            output.write(json.dumps(item, ensure_ascii=False) + "\n")


def run(input_path, output_dir):
    input_path = Path(input_path)
    items = load_candidates(input_path)
    equivalent, version = load_solver()
    output_dir = Path(output_dir)
    # A fresh directory prevents stale or accidentally overwritten study exports.
    output_dir.mkdir(parents=True, exist_ok=False)
    report, eligible, open_forms, assessments = [], [], [], []
    for item in items:
        result = screen(item, equivalent)
        result["spot_version"] = version
        if result["solver_status"] == "inequivalent":
            annotation_id = f"item_{len(eligible) + 1:04d}"
            result["annotation_id"] = annotation_id
            eligible.append(result)
            open_form, assessment = annotation_forms(result, annotation_id)
            open_forms.append(open_form)
            assessments.append(assessment)
        report.append(result)
    for name, records in (("solver_report", report), ("eligible", eligible),
                          ("open_interpretations", open_forms),
                          ("reading_assessment", assessments)):
        write_jsonl(output_dir / f"{input_path.stem}_{name}.jsonl", records)
    counts = Counter(item["solver_status"] for item in report)
    print(f"Spot {version}: {len(items)} checked; "
          f"{counts['inequivalent']} eligible for annotation; "
          f"{counts['equivalent']} equivalent (rejected); {counts['error']} errors")
    print(f"Outputs: {output_dir.resolve()}")
    return 1 if counts["error"] else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="candidate JSONL file")
    parser.add_argument("--out-dir", required=True, type=Path,
                        help="new directory for reports and annotation templates")
    args = parser.parse_args()
    try:
        return run(args.input, args.out_dir)
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
