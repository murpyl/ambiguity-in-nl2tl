"""Run with python -m unittest test_check_candidates -v."""

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import check_candidates as checker


SOURCE = Path(__file__).with_name("joint_versus_separate_eventuality_candidates.jsonl")


class CheckerTests(unittest.TestCase):
    def setUp(self):
        self.item = checker.load_candidates(SOURCE)[0]

    def test_invalid_formula_and_undefined_atom_never_reach_solver(self):
        for formula in ("F(", "F missing"):
            with self.subTest(formula=formula):
                item = {**self.item, "reading_a_ltl": formula}
                solver = Mock()
                self.assertEqual(checker.screen(item, solver)["solver_status"], "error")
                solver.assert_not_called()

    def test_solver_errors_are_not_eligible(self):
        for solver in (Mock(return_value=(None, "parse error")),
                       Mock(side_effect=RuntimeError("solver failure"))):
            self.assertEqual(checker.screen(self.item, solver)["solver_status"], "error")

    def test_exports_are_blinded_and_open_stage_has_no_readings(self):
        item = {**self.item, "future_private_metadata": "secret"}
        open_form, assessment = checker.annotation_forms(item, "item_0001")
        common = {"annotation_id", "scenario", "propositions", "requirement", "annotator_id"}
        self.assertEqual(set(open_form), common | {"interpretations", "comments"})
        self.assertEqual(set(assessment), common | {
            "reading_a", "reading_b", "supports_a", "supports_b",
            "additional_interpretations", "comments"})

    def test_duplicate_ids_and_bad_json_abort_input(self):
        for text in (json.dumps(self.item) + "\n" + json.dumps(self.item), "{broken"):
            with tempfile.TemporaryDirectory() as folder:
                path = Path(folder) / "input.jsonl"
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    checker.load_candidates(path)

    def test_pipeline_filters_and_preserves_source(self):
        originals = [copy.deepcopy(self.item) for _ in range(3)]
        for index, item in enumerate(originals):
            item["candidate_id"] = str(index)
        with tempfile.TemporaryDirectory() as folder:
            path, output = Path(folder) / "input.jsonl", Path(folder) / "out"
            checker.write_jsonl(path, originals)
            before = path.read_bytes()
            solver = Mock(side_effect=[(True, None), (False, "trace"), (None, "error")])
            with patch.object(checker, "load_solver", return_value=(solver, "test")):
                self.assertEqual(checker.run(path, output), 1)
            report = checker.load_candidates(output / "input_solver_report.jsonl")
            self.assertEqual([x["solver_status"] for x in report],
                             ["equivalent", "inequivalent", "error"])
            eligible = checker.load_candidates(output / "input_eligible.jsonl")
            self.assertEqual([x["candidate_id"] for x in eligible], ["1"])
            self.assertEqual(eligible[0]["human_validation_status"], "not_assessed")
            self.assertEqual(path.read_bytes(), before)
            with patch.object(checker, "load_solver", return_value=(solver, "test")):
                with self.assertRaises(FileExistsError):
                    checker.run(path, output)


class SpotIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.solver = staticmethod(checker.load_solver()[0])
        except RuntimeError as exc:
            raise unittest.SkipTest(str(exc))

    def test_actual_equivalence_and_distinguishing_trace(self):
        equivalent, witness = self.solver("F(a | b)", "(F a) | (F b)")
        self.assertTrue(equivalent)
        self.assertIsNone(witness)
        equivalent, witness = self.solver("F(a & b)", "(F a) & (F b)")
        self.assertFalse(equivalent)
        self.assertTrue(witness)

    def test_generated_candidates(self):
        for item in checker.load_candidates(SOURCE):
            with self.subTest(candidate_id=item["candidate_id"]):
                self.assertEqual(checker.screen(item, self.solver)["solver_status"],
                                 "inequivalent")


if __name__ == "__main__":
    unittest.main()
