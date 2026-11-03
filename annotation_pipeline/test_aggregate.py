"""Offline aggregation regression tests: python -m unittest annotation_pipeline.test_aggregate -v."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from annotation_pipeline import aggregate as a


def fixture(run, count=2):
    scope = {"entries": [{"review_id": f"r{i}", "annotation_id": f"a{i}", "source_family": "trigger_scope_final" if i % 2 else "other", "requirement": "Eventually a.", "propositions": {"a": "alarm"}, "readings": [{"reading_id": "A", "plain": "An alarm occurs."}, {"reading_id": "B", "plain": "An alarm never occurs."}]} for i in range(count)]}
    a.write_json(run / "scope.json", scope)
    a.write_json(run / "config.json", {"expected_models": a.MODELS, "min_agreeing_models": 3})
    groups = []
    for entry in scope["entries"]:
        groups.append({"group_id": entry["review_id"] + "g1", "review_id": entry["review_id"], "canonical": "An alarm eventually occurs.", "explanation": "Same unbounded eventual occurrence meaning.", "members": [{"model": m, "interpretation_index": 0, "text": "An alarm eventually occurs."} for m in a.MODELS]})
    a.write_json(run / "grouping.json", {"reviewed_by": ["coordinator", "auditor"], "groups": groups})
    for model in a.MODELS:
        folder = run / model.replace("/", "_")
        folder.mkdir()
        for stage in (1, 2):
            rows = []
            for entry in scope["entries"]:
                row = {"review_id": entry["review_id"], "comments": "original comment"}
                if stage == 1:
                    row["interpretations"] = ["An alarm eventually occurs."]
                else:
                    row.update(supports={"A": "Supported", "B": "Not supported"}, additional_interpretations=["Stage 2 discovery"])
                rows.append(row)
            path = folder / f"stage{stage}.validated.json"
            a.write_json(path, {"entries": rows})
            a.write_json(folder / f"stage{stage}.success.json", {"model": model, "stage": stage, "scope_sha256": hashlib.sha256(json.dumps(a.read_json(run / "scope.json"), sort_keys=True).encode()).hexdigest(), "validated_sha256": a.digest(path)})
    return scope


class AggregationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.run = Path(self.tmp.name) / "run"
        self.run.mkdir()
        self.output = Path(self.tmp.name) / "final"
        self.scope = fixture(self.run)

    def regenerate(self, minimum=None):
        return a.regenerate(self.run, self.output, minimum, expected_count=2)

    def modify_stage(self, model, stage, modify):
        folder = self.run / model.replace("/", "_")
        path = folder / f"stage{stage}.validated.json"
        data = a.read_json(path)
        modify(data)
        a.write_json(path, data)
        a.write_json(folder / f"stage{stage}.success.json", {"model": model, "stage": stage, "scope_sha256": hashlib.sha256(json.dumps(a.read_json(self.run / "scope.json"), sort_keys=True).encode()).hexdigest(), "validated_sha256": a.digest(path)})

    def test_offline_end_to_end_determinism_and_paired_ids(self):
        with patch("socket.socket", side_effect=AssertionError("network forbidden")):
            result = self.regenerate()
            original = {p.name: p.read_bytes() for p in self.output.iterdir()}
            self.regenerate()
        self.assertEqual(result["eligible_requirements"], 2)
        self.assertEqual(original, {p.name: p.read_bytes() for p in self.output.iterdir()})
        for family in ("other", "trigger_scope_final"):
            opens = [json.loads(x) for x in (self.output / f"{family}_open_interpretations.jsonl").read_text().splitlines()]
            readings = [json.loads(x) for x in (self.output / f"{family}_reading_assessment.jsonl").read_text().splitlines()]
            self.assertEqual([x["annotation_id"] for x in opens], [x["annotation_id"] for x in readings])
            self.assertEqual(opens[0]["annotator_id"], a.ANNOTATOR)
        additions = (self.output / "stage2_additional_interpretations.jsonl").read_text()
        self.assertIn('"counts_as_stage1_vote": false', additions)

    def test_threshold_validation(self):
        for value in (0, 6, True, 2.0, "3"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                a.threshold(value)
        for value in range(1, 6):
            self.assertEqual(a.threshold(value), value)

    def test_tied_labels_are_unresolved_at_lower_threshold(self):
        for counts in ({"Supported": 2, "Not supported": 2, "Uncertain": 1}, {"Supported": 1, "Not supported": 1, "Uncertain": 3}):
            label = a.decide(counts, 1)
            self.assertEqual(label, "unresolved" if counts["Supported"] == 2 else "Uncertain")
        for model in a.MODELS[2:4]:
            self.modify_stage(model, 2, lambda d: d["entries"][0]["supports"].update(A="Not supported"))
        self.modify_stage(a.MODELS[4], 2, lambda d: d["entries"][0]["supports"].update(A="Uncertain"))
        self.assertEqual(self.regenerate(1)["eligible_requirements"], 1)
        audit = json.loads((self.output / "vote_summary.jsonl").read_text().splitlines()[0])
        self.assertEqual(audit["readings"][0]["label"], "unresolved")
        self.assertEqual(audit["readings"][0]["counts"], {"Supported": 2, "Not supported": 2, "Uncertain": 1})

    def test_majority_uncertain_excluded(self):
        for model in a.MODELS[:3]:
            self.modify_stage(model, 2, lambda d: d["entries"][0]["supports"].update(A="Uncertain"))
        self.assertEqual(self.regenerate()["eligible_requirements"], 1)
        self.assertIn("A: Uncertain", (self.output / "exclusions.jsonl").read_text())

    def test_unique_model_group_count_and_threshold(self):
        self.modify_stage(a.MODELS[0], 1, lambda d: d["entries"][0]["interpretations"].append("Same alarm meaning."))
        grouping = a.read_json(self.run / "grouping.json")
        group = grouping["groups"][0]
        group["members"].append({"model": a.MODELS[0], "interpretation_index": 1, "text": "Same alarm meaning."})
        separated = group["members"][3:5]
        group["members"] = group["members"][:3] + group["members"][5:]
        grouping["groups"].append({**group, "group_id": "separate", "canonical": "A different temporal scope.", "explanation": "Synthetic fixture separation.", "members": separated})
        a.write_json(self.run / "grouping.json", grouping)
        self.assertEqual(self.regenerate(3)["eligible_requirements"], 2)
        audit = json.loads((self.output / "vote_summary.jsonl").read_text().splitlines()[0])
        self.assertEqual(audit["groups"][0]["model_count"], 3)
        self.assertEqual(self.regenerate(4)["eligible_requirements"], 1)
        self.assertEqual(a.read_json(self.output / "metadata.json")["min_agreeing_models"], 4)

    def test_grouping_coverage_and_original_integrity(self):
        original = a.read_json(self.run / "grouping.json")
        for mutation in (lambda g: g["groups"][0]["members"].pop(), lambda g: g["groups"][0]["members"][0].update(text="changed"), lambda g: g["groups"][0]["members"].append(g["groups"][0]["members"][0])):
            grouping = copy.deepcopy(original)
            mutation(grouping)
            a.write_json(self.run / "grouping.json", grouping)
            with self.assertRaises(ValueError):
                self.regenerate()
            self.assertFalse(self.output.exists())

    def test_missing_or_invalid_model_never_reduces_population(self):
        folder = self.run / a.MODELS[0].replace("/", "_")
        (folder / "stage2.success.json").unlink()
        with self.assertRaises(FileNotFoundError):
            self.regenerate()
        self.assertFalse(self.output.exists())

    def test_invalid_completeness_and_hash(self):
        self.modify_stage(a.MODELS[0], 2, lambda d: d["entries"][0]["supports"].pop("B"))
        with self.assertRaisesRegex(ValueError, "incomplete"):
            self.regenerate()
        path = self.run / a.MODELS[0].replace("/", "_") / "stage1.validated.json"
        path.write_text(path.read_text() + "\n")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            self.regenerate()

    def test_protect_source_and_unrelated_outputs(self):
        self.output.mkdir()
        (self.output / "keep.txt").write_text("original")
        with self.assertRaises(FileNotFoundError):
            self.regenerate()
        self.assertEqual((self.output / "keep.txt").read_text(), "original")
        for family in ("trigger_scope", "../old", "/tmp", "x/y"):
            scope = copy.deepcopy(self.scope)
            scope["entries"][0]["source_family"] = family
            with self.assertRaises(ValueError):
                a.validate_scope(scope, 2)

    def test_scope_and_receipt_identity_are_bound(self):
        original_scope = a.read_json(self.run / "scope.json")
        changed = copy.deepcopy(original_scope)
        changed["entries"][0]["requirement"] = "A changed requirement."
        a.write_json(self.run / "scope.json", changed)
        with self.assertRaisesRegex(ValueError, "identity/scope mismatch"):
            self.regenerate()
        a.write_json(self.run / "scope.json", original_scope)
        receipt = self.run / a.MODELS[0].replace("/", "_") / "stage1.success.json"
        original = a.read_json(receipt)
        for key, value in (("model", a.MODELS[1]), ("stage", 2), ("stage", True)):
            a.write_json(receipt, {**original, key: value})
            with self.assertRaisesRegex(ValueError, "identity/scope mismatch"):
                self.regenerate()
        self.assertFalse(self.output.exists())

    def test_unexpected_stage_fields_rejected(self):
        self.modify_stage(a.MODELS[0], 1, lambda d: d["entries"][0].update(additional_interpretations=["leaked"]))
        with self.assertRaisesRegex(ValueError, "unexpected annotation"):
            self.regenerate()

    def test_production_requires_88(self):
        with self.assertRaisesRegex(ValueError, "expected 88"):
            a.regenerate(self.run, self.output)

    def test_full_88_fixture(self):
        run = Path(self.tmp.name) / "full"
        run.mkdir()
        fixture(run, 88)
        result = a.regenerate(run, self.output)
        self.assertEqual(result["requirements"], 88)
        self.assertEqual(result["eligible_requirements"], 88)


if __name__ == "__main__":
    unittest.main()
