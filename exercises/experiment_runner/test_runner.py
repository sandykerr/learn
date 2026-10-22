"""Behavioral checks for the refactoring exercise; no design is prescribed.

Run from the repository root:
    python3 -m unittest discover -s exercises/experiment_runner -p test_runner.py -v
"""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from runner import run_experiment


class ExperimentBehaviorTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)

    def assert_report(self, actual, expected):
        self.assertEqual(set(actual), set(expected))
        for field in expected:
            if field == "mae":
                self.assertAlmostEqual(actual[field], expected[field])
            else:
                self.assertEqual(actual[field], expected[field], field)

    def test_defaults_create_parents_and_persist_returned_report(self):
        output = self.root / "nested" / "reports"
        report = run_experiment({"run_name": "baseline-01_v1"}, output)
        expected = {
            "run_name": "baseline-01_v1", "dataset": "tiny", "scale": 1.0,
            "count": 4, "predictions": [1, 2, 3, 4], "mae": 2.5,
        }
        self.assert_report(report, expected)
        persisted = json.loads((output / "baseline-01_v1.json").read_text())
        self.assert_report(persisted, expected)
        self.assertEqual(persisted, report)

    def test_dataset_and_scale_results(self):
        cases = [
            ("tiny", 2, [2, 4, 6, 8], 0.0),
            ("tiny", -1, [-1, -2, -3, -4], 7.5),
            ("tiny", 0.5, [0.5, 1, 1.5, 2], 3.75),
            ("shifted", 1, [-2, 0, 2], 4 / 3),
            ("shifted", 0, [0, 0, 0], 8 / 3),
            ("shifted", 2, [-4, 0, 4], 0.0),
        ]
        for index, (dataset, scale, predictions, mae) in enumerate(cases):
            with self.subTest(dataset=dataset, scale=scale):
                name = f"case_{index}"
                report = run_experiment(
                    {"run_name": name, "dataset": dataset, "scale": scale},
                    str(self.root),
                )
                self.assert_report(report, {
                    "run_name": name, "dataset": dataset, "scale": scale,
                    "count": len(predictions), "predictions": predictions,
                    "mae": mae,
                })
                self.assertEqual(
                    json.loads((self.root / f"{name}.json").read_text()), report,
                )

    def test_input_is_unchanged_and_unknown_fields_are_ignored(self):
        config = {"run_name": "immutable", "notes": {"tags": ["learner"]}}
        original = copy.deepcopy(config)
        report = run_experiment(config, self.root)
        self.assertEqual(config, original)
        self.assertNotIn("notes", report)
        self.assertEqual(set(report), {
            "run_name", "dataset", "scale", "count", "predictions", "mae",
        })

    def test_repeated_runs_overwrite_only_the_named_report(self):
        first = run_experiment({"run_name": "first"}, self.root)
        first_snapshot = copy.deepcopy(first)
        first_bytes = (self.root / "first.json").read_bytes()
        run_experiment({"run_name": "second", "scale": -1}, self.root)
        second = run_experiment(
            {"run_name": "second", "dataset": "shifted", "scale": 2}, self.root,
        )
        self.assertEqual(first, first_snapshot)
        self.assertEqual((self.root / "first.json").read_bytes(), first_bytes)
        self.assertEqual(json.loads((self.root / "second.json").read_text()), second)
        self.assertEqual(second["predictions"], [-4, 0, 4])
        self.assertEqual(second["mae"], 0)
        self.assertEqual({path.name for path in self.root.iterdir()}, {
            "first.json", "second.json",
        })

    def test_invalid_config_does_not_create_output_or_modify_existing_files(self):
        invalid = [{}]
        invalid.extend({"run_name": name} for name in (
            "", " ", "has space", "../escape", "a/b", "a\\b", "a.b", None, 1,
        ))
        invalid.extend({"run_name": "existing", "dataset": dataset} for dataset in (
            "unknown", "", None, 1,
        ))
        invalid.extend({"run_name": "existing", "scale": scale} for scale in (
            True, False, None, "2", [], {}, float("nan"), float("inf"),
            float("-inf"), 10**400, 1e308, -1e308,
        ))
        existing = self.root / "existing_output"
        existing.mkdir()
        sentinel = b"preserve this existing report\n"
        (existing / "existing.json").write_bytes(sentinel)
        for index, config in enumerate(invalid):
            with self.subTest(config=config):
                missing = self.root / f"missing_{index}" / "reports"
                for output in (missing, existing):
                    with self.assertRaises(ValueError):
                        run_experiment(config, output)
                self.assertFalse(missing.parent.exists())
                self.assertEqual((existing / "existing.json").read_bytes(), sentinel)
                self.assertEqual(list(existing.iterdir()), [existing / "existing.json"])

    def test_cli_produces_the_same_report_on_stdout_and_disk(self):
        output = self.root / "cli_output"
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("runner.py")),
             "--output-dir", str(output), "--run-name", "demo",
             "--dataset", "shifted", "--scale", "2"],
            capture_output=True, text=True, timeout=10, check=True,
        )
        report = json.loads(completed.stdout)
        self.assert_report(report, {
            "run_name": "demo", "dataset": "shifted", "scale": 2,
            "count": 3, "predictions": [-4, 0, 4], "mae": 0,
        })
        self.assertEqual(json.loads((output / "demo.json").read_text()), report)


if __name__ == "__main__":
    unittest.main()
