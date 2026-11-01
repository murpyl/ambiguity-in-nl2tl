"""Audit LTL dataset records without modifying them.

Usage: python dataset_checks.py candidates.jsonl [--stage candidates|annotations|calibration|final]

Each record has item_id, family_id, contrast_id, ambiguous_text, propositions
(mapping atom -> English meaning), and readings (list of objects with reading_id,
plain, ltl, clear_rewrite). Later stages add:

annotations: {open: [{annotator_id, interpretations: [str]}],
              assessment: [{annotator_id, supports: {reading_id: bool|"uncertain"},
                            additional_interpretations: [str]}]}
controls: {reading_id: [{annotator_id, selects: bool, excludes_others: bool}]}
calibration: {reading_id: [{model, formula, prompt_id, run_id}]}
split: train|dev|test

The final stage treats each record as one validated ambiguous item plus one
clear control for each endorsed reading. With two readings, 67 records imply
201 evaluated sentences.

The CLI reports issues; human plausibility and rewrite clarity remain human judgments.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime
import json
from pathlib import Path

from ltl import ParseError, parse


def read_jsonl(path):
    records = []
    with Path(path).open(encoding="utf-8-sig") as stream:
        for line_no, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"line {line_no}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"line {line_no}: expected object")
            records.append(value)
    if not records:
        raise ValueError("input has no records")
    return records


def atoms(node):
    if node[0] == "atom":
        return {node[1]}
    return set().union(*(atoms(child) for child in node[1:] if isinstance(child, tuple)))


def require_text(record, field, issues, prefix):
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        issues.append(f"{prefix}: {field} must be nonempty text")
        return None
    return value.strip()


def load_spot():
    try:
        import spot
        if not all(hasattr(spot, key) for key in ("formula", "are_equivalent", "translate", "version")):
            raise ImportError("installed spot is not the LTL Spot library")
        from ltl_equiv import to_spot
        return spot, to_spot
    except ImportError as exc:
        raise RuntimeError(f"Spot LTL bindings required: {exc}") from exc


def check_candidate(record, issues, solver):
    prefix = record.get("item_id", "<missing item_id>")
    for field in ("item_id", "family_id", "contrast_id", "ambiguous_text"):
        require_text(record, field, issues, prefix)
    props = record.get("propositions")
    if not isinstance(props, dict) or not props or any(
        not isinstance(key, str) or not key.isidentifier() or not isinstance(val, str) or not val.strip()
        for key, val in props.items()
    ):
        issues.append(f"{prefix}: propositions must map valid atom names to nonempty meanings")
        props = {}
    readings = record.get("readings")
    if not isinstance(readings, list) or len(readings) < 2:
        issues.append(f"{prefix}: readings must contain at least two entries")
        return {}
    ids, formulas, rewrites = set(), {}, set()
    for index, reading in enumerate(readings):
        location = f"{prefix}/reading[{index}]"
        if not isinstance(reading, dict):
            issues.append(f"{location}: expected object")
            continue
        rid = require_text(reading, "reading_id", issues, location)
        require_text(reading, "plain", issues, location)
        rewrite = require_text(reading, "clear_rewrite", issues, location)
        formula = require_text(reading, "ltl", issues, location)
        if rid in ids:
            issues.append(f"{location}: duplicate reading_id {rid}")
        if rid:
            ids.add(rid)
        if rewrite:
            if rewrite.casefold() == str(record.get("ambiguous_text", "")).casefold():
                issues.append(f"{location}: clear rewrite repeats ambiguous text")
            if rewrite.casefold() in rewrites:
                issues.append(f"{location}: duplicate clear rewrite")
            rewrites.add(rewrite.casefold())
        if formula and rid:
            try:
                used = atoms(parse(formula))
                if used - props.keys():
                    issues.append(f"{location}: undefined atoms {sorted(used - props.keys())}")
                formulas[rid] = solver[1](formula)
            except (ParseError, RuntimeError) as exc:
                issues.append(f"{location}: invalid formula: {exc}")
    classes = []
    if len(formulas) == len(readings):
        spot, _ = solver
        for rid, formula in formulas.items():
            for cls in classes:
                if spot.are_equivalent(formula, formulas[cls[0]]):
                    cls.append(rid)
                    break
            else:
                classes.append([rid])
        if len(classes) < 2:
            issues.append(f"{prefix}: fewer than two inequivalent reading classes")
        if any(len(cls) > 1 for cls in classes):
            issues.append(f"{prefix}: equivalent readings should be merged: {classes}")
        # Check actual satisfiability of every claimed distinction, including
        # pairs that are not class representatives.
        for i, (left_id, left) in enumerate(formulas.items()):
            for right_id, right in list(formulas.items())[i + 1:]:
                if spot.are_equivalent(left, right):
                    continue
                witness = spot.translate(spot.formula.Xor(left, right)).accepting_word()
                if witness is None:
                    issues.append(f"{prefix}: missing solver witness for {left_id}/{right_id}")
    return {"ids": ids, "classes": classes, "formulas": formulas}


def check_annotations(record, result, issues, minimum=3, endorsements=2):
    prefix, ids = record["item_id"], result["ids"]
    data = record.get("annotations")
    if not isinstance(data, dict):
        issues.append(f"{prefix}: missing annotations object")
        return
    people, times = {}, {}
    for stage in ("open", "assessment"):
        responses = data.get(stage)
        if not isinstance(responses, list):
            issues.append(f"{prefix}: annotations.{stage} must be a list")
            return
        seen = set()
        for response in responses:
            if not isinstance(response, dict):
                issues.append(f"{prefix}: invalid {stage} response")
                continue
            annotator = response.get("annotator_id")
            if not isinstance(annotator, str) or not annotator.strip() or annotator in seen:
                issues.append(f"{prefix}: missing or repeated annotator in {stage}")
                continue
            seen.add(annotator)
            submitted = response.get("submitted_at")
            try:
                if not isinstance(submitted, str):
                    raise ValueError("missing timestamp")
                parsed_time = datetime.fromisoformat(submitted.replace("Z", "+00:00"))
                if parsed_time.tzinfo is None:
                    raise ValueError("timestamp lacks timezone")
                times[(stage, annotator)] = parsed_time
            except ValueError:
                issues.append(f"{prefix}: invalid submitted_at in {stage}/{annotator}")
            values = response.get("interpretations" if stage == "open" else "additional_interpretations")
            if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
                issues.append(f"{prefix}: invalid open-ended interpretations in {stage}/{annotator}")
            if stage == "assessment":
                support = response.get("supports")
                if not isinstance(support, dict) or set(support) != ids or any(
                    type(v) is not bool and v != "uncertain" for v in support.values()
                ):
                    issues.append(f"{prefix}: incomplete support choices for {annotator}")
            people[stage] = seen
        if len(seen) < minimum:
            issues.append(f"{prefix}: fewer than {minimum} {stage} annotations")
    if people.get("open") != people.get("assessment"):
        issues.append(f"{prefix}: annotator IDs differ between stages")
    for annotator in people.get("open", set()) & people.get("assessment", set()):
        earlier, later = times.get(("open", annotator)), times.get(("assessment", annotator))
        if earlier is not None and later is not None and earlier >= later:
            issues.append(f"{prefix}: {annotator} completed assessment before open stage")
    counts = Counter()
    for response in data.get("assessment", []):
        if isinstance(response, dict) and isinstance(response.get("supports"), dict):
            counts.update(rid for rid, value in response["supports"].items() if value is True)
            if response.get("additional_interpretations"):
                issues.append(f"{prefix}: added interpretations require expert adjudication")
    supported = sum(any(counts[rid] >= endorsements for rid in cls) for cls in result["classes"])
    if supported < 2:
        issues.append(f"{prefix}: fewer than two endorsed inequivalent classes")
    if record.get("k_observed") != supported:
        issues.append(f"{prefix}: k_observed should be {supported} under the stated rule")


def check_controls(record, result, issues, minimum=2):
    prefix, ids = record["item_id"], result["ids"]
    controls = record.get("controls")
    if not isinstance(controls, dict) or set(controls) != ids:
        issues.append(f"{prefix}: controls need one entry for every reading")
        return
    for rid, reviews in controls.items():
        if not isinstance(reviews, list) or len(reviews) < minimum:
            issues.append(f"{prefix}/{rid}: too few control reviews")
            continue
        seen = set()
        for review in reviews:
            if not isinstance(review, dict) or not isinstance(review.get("annotator_id"), str):
                issues.append(f"{prefix}/{rid}: invalid control review")
                continue
            if review["annotator_id"] in seen:
                issues.append(f"{prefix}/{rid}: repeated control reviewer")
            seen.add(review["annotator_id"])
            if review.get("selects") is not True or review.get("excludes_others") is not True:
                issues.append(f"{prefix}/{rid}: rewrite not independently confirmed clear")


def check_calibration(record, result, issues, solver):
    prefix, ids = record["item_id"], result["ids"]
    data = record.get("calibration")
    if not isinstance(data, dict) or set(data) != ids:
        issues.append(f"{prefix}: calibration missing for one or more readings")
        return
    for rid, responses in data.items():
        if not isinstance(responses, list) or not responses:
            issues.append(f"{prefix}/{rid}: no calibration responses")
            continue
        seen = set()
        evaluation_models = set(record.get("evaluation_models", []))
        for response in responses:
            if not isinstance(response, dict):
                issues.append(f"{prefix}/{rid}: invalid calibration response")
                continue
            for field in ("model", "prompt_id", "run_id"):
                require_text(response, field, issues, f"{prefix}/{rid}")
            key = (response.get("model"), response.get("run_id"))
            if response.get("model") in evaluation_models:
                issues.append(f"{prefix}/{rid}: calibration model is also an evaluation model")
            if key in seen:
                issues.append(f"{prefix}/{rid}: duplicate calibration run")
            seen.add(key)
            formula = response.get("formula")
            if formula is not None:
                try:
                    parsed = result["formulas"].get(rid)
                    actual = solver[1](formula)
                    if parsed is not None:
                        response_score = solver[0].are_equivalent(actual, parsed)
                        if "correct" in response and response["correct"] is not response_score:
                            issues.append(f"{prefix}/{rid}: calibration correctness conflicts with Spot")
                except (ParseError, RuntimeError):
                    if response.get("correct") is True:
                        issues.append(f"{prefix}/{rid}: invalid formula marked correct")


def check_dataset(records, stage):
    solver = load_spot()
    issues, results = [], {}
    item_ids, contrast_splits, family_splits, text_owner, formula_contrasts = set(), defaultdict(set), defaultdict(set), {}, {}
    for record in records:
        item_id = record.get("item_id")
        if item_id in item_ids:
            issues.append(f"duplicate item_id: {item_id}")
        item_ids.add(item_id)
        result = check_candidate(record, issues, solver)
        results[item_id] = result
        if result.get("formulas") and len(result["formulas"]) == len(record.get("readings", [])):
            # Exact structural duplicates are caught here. Human review still
            # decides whether different structures instantiate the same idea.
            signature = tuple(sorted(str(formula) for formula in result["formulas"].values()))
            if signature in formula_contrasts:
                issues.append(f"duplicate formula contrast: {item_id} and {formula_contrasts[signature]}")
            formula_contrasts[signature] = item_id
        text = record.get("ambiguous_text")
        if isinstance(text, str):
            key = text.casefold().strip()
            if key in text_owner:
                issues.append(f"duplicate candidate text: {item_id} and {text_owner[key]}")
            text_owner[key] = item_id
        if stage in ("annotations", "calibration", "final") and result.get("classes"):
            check_annotations(record, result, issues)
        if stage in ("calibration", "final") and result.get("classes"):
            check_controls(record, result, issues)
            check_calibration(record, result, issues, solver)
        if stage == "final":
            split = record.get("split")
            if split not in ("train", "dev", "test"):
                issues.append(f"{item_id}: invalid split")
            else:
                contrast_splits[record.get("contrast_id")].add(split)
                family_splits[record.get("family_id")].add(split)
    if stage == "final":
        for contrast, splits in contrast_splits.items():
            if len(splits) > 1:
                issues.append(f"contrast {contrast} leaks across splits: {sorted(splits)}")
        for family, splits in family_splits.items():
            if len(splits) > 1:
                issues.append(f"family {family} crosses splits: {sorted(splits)}")
        print(f"Final selection contains {len(records)} ambiguous records; clear rows depend on endorsed readings")
    return issues


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("input", type=Path)
    cli.add_argument("--stage", choices=("candidates", "annotations", "calibration", "final"), default="candidates")
    cli.add_argument("--expected-pairs", type=int, help="optional exact contrast-record count; 67 two-reading records give 201 rows")
    args = cli.parse_args()
    try:
        records = read_jsonl(args.input)
        issues = check_dataset(records, args.stage)
        if args.stage == "final" and args.expected_pairs is not None and len(records) != args.expected_pairs:
            issues.append(f"expected {args.expected_pairs} pairs, found {len(records)}")
    except (OSError, ValueError, RuntimeError) as exc:
        cli.exit(2, f"error: {exc}\n")
    for issue in issues:
        print(f"FAIL: {issue}")
    print(f"Checked {len(records)} records at stage {args.stage}: {len(issues)} issue(s)")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
