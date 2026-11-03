"""Deterministic, network-free regeneration from reviewed five-model annotations."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile

MODELS = ["google/gemini-3.8-flash", "anthropic/claude-haiku-5.5", "openai/gpt-5.6-luna", "deepseek/deepseek-v4.1-flash", "qwen/qwen3.8-flash"]
LABELS = ("Supported", "Not supported", "Uncertain")
ANNOTATOR = "aggregate:five-model-semantic-consensus-v1"


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def threshold(value):
    if type(value) is not int or not 1 <= value <= 5:
        raise ValueError("min_agreeing_models must be an integer from 1 through 5")
    return value


def text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be nonempty text")
    return value


def unique_index(rows, key, name):
    if not isinstance(rows, list):
        raise ValueError(f"{name} must be a list")
    result = {}
    for row in rows:
        identity = text(row[key], key)
        if identity in result:
            raise ValueError(f"duplicate {name} {identity}")
        result[identity] = row
    return result


def validate_scope(scope, expected_count=88):
    entries = unique_index(scope["entries"], "review_id", "requirements")
    if len(entries) != expected_count:
        raise ValueError(f"expected {expected_count} requirements, got {len(entries)}")
    identities = set()
    for entry in entries.values():
        family = entry["source_family"]
        if not isinstance(family, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", family) or family == "trigger_scope":
            raise ValueError("unsafe or obsolete source family")
        identity = (family, text(entry["annotation_id"], "annotation_id"))
        if identity in identities:
            raise ValueError("duplicate family/annotation identity")
        identities.add(identity)
        text(entry["requirement"], "requirement")
        if not entry.get("propositions"):
            raise ValueError("missing proposition definitions")
        readings = unique_index(entry["readings"], "reading_id", "readings")
        if not readings:
            raise ValueError("missing proposed readings")
        for reading in readings.values():
            text(reading["plain"], "reading plain text")
    return entries


def validate_stage(scope, data, stage):
    if set(data) != {"entries"}:
        raise ValueError("unexpected stage response fields")
    entries = unique_index(data["entries"], "review_id", f"stage {stage} entries")
    if set(entries) != set(scope):
        raise ValueError(f"stage {stage} does not cover scope exactly")
    for review_id, row in entries.items():
        expected_fields = {"review_id", "comments", "interpretations"} if stage == 1 else {"review_id", "comments", "supports", "additional_interpretations"}
        if set(row) != expected_fields:
            raise ValueError("unexpected annotation entry fields")
        if not isinstance(row.get("comments"), str):
            raise ValueError("missing comments field")
        field = "interpretations" if stage == 1 else "additional_interpretations"
        if not isinstance(row.get(field), list):
            raise ValueError(f"{field} must be a list")
        if stage == 1 and not row[field]:
            raise ValueError("Stage 1 requires at least one interpretation")
        for interpretation in row[field]:
            text(interpretation, field)
        if stage == 2:
            supports = row.get("supports")
            expected = {r["reading_id"] for r in scope[review_id]["readings"]}
            if not isinstance(supports, dict) or set(supports) != expected or any(label not in LABELS for label in supports.values()):
                raise ValueError("incomplete or invalid reading assessment")
    return entries


def load_models(run, scope):
    result = {}
    scope_hash = hashlib.sha256(json.dumps(read_json(run / "scope.json"), sort_keys=True).encode()).hexdigest()
    for model in MODELS:
        folder = run / model.replace("/", "_")
        stages = []
        for stage in (1, 2):
            path = folder / f"stage{stage}.validated.json"
            receipt = read_json(folder / f"stage{stage}.success.json")
            if receipt.get("model") != model or type(receipt.get("stage")) is not int or receipt["stage"] != stage or receipt.get("scope_sha256") != scope_hash:
                raise ValueError(f"successful Stage {stage} receipt identity/scope mismatch: {model}")
            if receipt.get("validated_sha256") != digest(path):
                raise ValueError(f"successful Stage {stage} hash mismatch: {model}")
            stages.append(validate_stage(scope, read_json(path), stage))
        result[model] = stages
    return result


def validate_groups(grouping, scope, models):
    reviewers = grouping.get("reviewed_by")
    if not isinstance(reviewers, list) or len(set(reviewers)) < 2 or any(not isinstance(r, str) or not r.strip() for r in reviewers):
        raise ValueError("grouping needs coordinator and subagent reviewer identities")
    groups = unique_index(grouping["groups"], "group_id", "semantic groups")
    seen = set()
    result = {rid: [] for rid in scope}
    for group in groups.values():
        rid = group["review_id"]
        if rid not in scope:
            raise ValueError("group references unknown requirement")
        text(group["canonical"], "canonical description")
        text(group["explanation"], "group explanation")
        if not isinstance(group["members"], list) or not group["members"]:
            raise ValueError("semantic group has no members")
        voters = set()
        for member in group["members"]:
            model, index = member["model"], member["interpretation_index"]
            if model not in models or type(index) is not int or index < 0:
                raise ValueError("invalid group membership")
            originals = models[model][0][rid]["interpretations"]
            if index >= len(originals) or member["text"] != originals[index]:
                raise ValueError("membership does not match original interpretation")
            key = (model, rid, index)
            if key in seen:
                raise ValueError("interpretation belongs to multiple groups")
            seen.add(key)
            voters.add(model)
        result[rid].append({**group, "models": sorted(voters), "model_count": len(voters)})
    expected = {(model, rid, i) for model, stages in models.items() for rid, row in stages[0].items() for i in range(len(row["interpretations"]))}
    if seen != expected:
        raise ValueError("grouping must cover every original Stage 1 interpretation exactly once")
    return result


def decide(counts, minimum):
    highest = max(counts.values())
    winners = [label for label, count in counts.items() if count == highest]
    return winners[0] if highest >= minimum and len(winners) == 1 else "unresolved"


def build(scope, models, groups, minimum):
    families = {entry["source_family"]: ([], []) for entry in scope.values()}
    votes, exclusions, additions = [], [], []
    for rid, entry in scope.items():
        retained = [g for g in groups[rid] if g["model_count"] >= minimum]
        assessments, reading_votes = {}, []
        for reading in entry["readings"]:
            reading_id = reading["reading_id"]
            responses = {model: models[model][1][rid]["supports"][reading_id] for model in MODELS}
            counts = {label: sum(v == label for v in responses.values()) for label in LABELS}
            label = decide(counts, minimum)
            assessments[reading_id] = label
            reading_votes.append({"reading_id": reading_id, "counts": counts, "label": label, "responses": responses})
        reasons = []
        if not retained:
            reasons.append("no Stage 1 semantic group reaches threshold")
        for reading_id, label in assessments.items():
            if label not in ("Supported", "Not supported"):
                reasons.append(f"{reading_id}: {label}")
        audit = {"review_id": rid, "source_family": entry["source_family"], "annotation_id": entry["annotation_id"], "groups": [{**g, "retained": g in retained} for g in groups[rid]], "readings": reading_votes, "eligible": not reasons, "exclusion_reasons": reasons}
        votes.append(audit)
        if reasons:
            exclusions.append({k: audit[k] for k in ("review_id", "source_family", "annotation_id", "exclusion_reasons")})
        for model in MODELS:
            additions.append({"review_id": rid, "model": model, "additional_interpretations": models[model][1][rid]["additional_interpretations"], "comments": models[model][1][rid]["comments"], "stage1_comments": models[model][0][rid]["comments"], "counts_as_stage1_vote": False})
        if reasons:
            continue
        common = {key: entry[key] for key in ("annotation_id", "requirement", "propositions")}
        if entry.get("scenario"):
            common["scenario"] = entry["scenario"]
        common.update(annotator_id=ANNOTATOR)
        comment = "Model-generated annotations; aggregate semantic consensus. See vote_summary.jsonl for provenance."
        opens, readings = families[entry["source_family"]]
        opens.append({**common, "interpretations": [g["canonical"] for g in retained], "comments": comment})
        readings.append({**common, "readings": entry["readings"], "supports": assessments, "additional_interpretations": [], "comments": comment})
    return families, votes, exclusions, additions


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path, rows):
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def regenerate(run, output, min_agreeing_models=None, expected_count=88):
    run, output = Path(run), Path(output)
    config = read_json(run / "config.json")
    if config["expected_models"] != MODELS:
        raise ValueError("expected_models must contain the fixed five exact model IDs in configured order")
    minimum = threshold(config["min_agreeing_models"] if min_agreeing_models is None else min_agreeing_models)
    scope = validate_scope(read_json(run / "scope.json"), expected_count)
    models = load_models(run, scope)
    groups = validate_groups(read_json(run / "grouping.json"), scope, models)
    families, votes, exclusions, additions = build(scope, models, groups, minimum)
    # Never replace source data or a directory that was not created by this tool.
    if output.resolve() == run.resolve() or run.resolve().is_relative_to(output.resolve()):
        raise ValueError("output cannot contain run inputs")
    if output.is_symlink():
        raise ValueError("output cannot be a symlink")
    if output.exists():
        old = read_json(output / "metadata.json")
        if old.get("generator") != ANNOTATOR or set(p.name for p in output.iterdir()) != set(old["generated_files"]):
            raise ValueError("refusing to replace an unrelated output directory")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".aggregate-", dir=output.parent))
    try:
        for family, (opens, readings) in sorted(families.items()):
            if {r["annotation_id"] for r in opens} != {r["annotation_id"] for r in readings}:
                raise ValueError("paired output IDs differ")
            write_jsonl(temporary / f"{family}_open_interpretations.jsonl", opens)
            write_jsonl(temporary / f"{family}_reading_assessment.jsonl", readings)
        write_jsonl(temporary / "vote_summary.jsonl", votes)
        write_jsonl(temporary / "exclusions.jsonl", exclusions)
        write_jsonl(temporary / "stage2_additional_interpretations.jsonl", additions)
        provenance = {str(p.relative_to(run)): digest(p) for p in sorted(run.glob("*/stage*.validated.json"))}
        provenance.update({name: digest(run / name) for name in ("config.json", "scope.json", "grouping.json")})
        metadata = {"generator": ANNOTATOR, "model_generated": True, "expected_models": MODELS, "min_agreeing_models": minimum, "population": 5, "requirements": len(scope), "eligible_requirements": sum(v["eligible"] for v in votes), "input_sha256": provenance, "generated_files": sorted([p.name for p in temporary.iterdir()] + ["metadata.json"])}
        write_json(temporary / "metadata.json", metadata)
        if output.exists():
            for path in output.iterdir():
                path.unlink()
            output.rmdir()
        temporary.rename(output)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--min-agreeing-models", type=int)
    args = parser.parse_args()
    try:
        result = regenerate(args.run, args.output, args.min_agreeing_models)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"regeneration blocked: {exc}\n")
    print(f"Regenerated {result['eligible_requirements']}/{result['requirements']} eligible requirements at threshold {result['min_agreeing_models']}.")


if __name__ == "__main__":
    main()
