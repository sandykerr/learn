"""A working but deliberately tangled runner for a software-design exercise.

Everything uses tiny fixtures and arithmetic: no training, model downloads,
external services, or HPC jobs. Refactor this module while keeping its public
behavior intact. There is deliberately no reference solution here.
"""

import argparse
import json
import math
from pathlib import Path
import re


def run_experiment(config: dict, output_dir: str | Path) -> dict:
    """Validate a run, predict on a tiny fixture, and save its JSON report."""
    # Configuration, fixture selection, model behavior, metrics, and persistence
    # live together here. The exercise is to reconsider those responsibilities.
    run_name = config.get("run_name")
    if not isinstance(run_name, str) or not re.fullmatch(
        r"[A-Za-z0-9_-]+", run_name
    ):
        raise ValueError("run_name must contain only letters, digits, '_' or '-'")

    dataset = config.get("dataset", "tiny")
    if dataset not in ("tiny", "shifted"):
        raise ValueError("dataset must be 'tiny' or 'shifted'")

    scale = config.get("scale", 1.0)
    if isinstance(scale, bool) or not isinstance(scale, (int, float)):
        raise ValueError("scale must be a finite number")
    try:
        scale = float(scale)
    except OverflowError as error:
        raise ValueError("scale must be a finite number") from error
    if not math.isfinite(scale):
        raise ValueError("scale must be a finite number")

    if dataset == "tiny":
        inputs = [1, 2, 3, 4]
        targets = [2, 4, 6, 8]
    else:
        inputs = [-2, 0, 2]
        targets = [-4, 0, 4]

    # This arithmetic stands in for a model backend; it does not train anything.
    predictions = []
    for value in inputs:
        predictions.append(value * scale)

    errors = []
    for index in range(len(targets)):
        errors.append(abs(predictions[index] - targets[index]))
    mae = sum(errors) / len(errors)
    if not all(math.isfinite(value) for value in predictions) or not math.isfinite(mae):
        raise ValueError("scale produces non-finite predictions or error")

    report = {
        "run_name": run_name,
        "dataset": dataset,
        "scale": scale,
        "count": len(inputs),
        "predictions": predictions,
        "mae": mae,
    }

    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    report_path = directory / f"{run_name}.json"
    with report_path.open("w", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2, allow_nan=False)
        stream.write("\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--run-name", default="demo")
    parser.add_argument("--dataset", default="tiny")
    parser.add_argument("--scale", type=float, default=1.0)
    arguments = parser.parse_args()
    config = {
        "run_name": arguments.run_name,
        "dataset": arguments.dataset,
        "scale": arguments.scale,
    }
    try:
        report = run_experiment(config, arguments.output_dir)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
