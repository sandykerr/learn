# Exercise 1: Refactor an experiment runner

Practice responsibility boundaries, composition, and testable interfaces in
Python. The starter works but mixes configuration, data selection, fake model
construction, evaluation, and artifact writing. Your task is to improve its
design while preserving observable behavior. There is no prescribed class
hierarchy or reference solution.

This is a local design exercise: tiny in-memory fixtures, a deterministic fake
model, temporary JSON files, and Python's standard library. No training, external
services, GPU, HPC job, or dependency installation is required. Python 3.10+
is sufficient.

## Start in pi

From the repository root:

```bash
bash scripts/start-coding-exercise.sh
```

The launcher loads both question extensions and exercise-specific tutor
instructions. It disables automatic skill discovery to avoid the global teaching
skill's multiple-choice-only grading rules, and explicitly loads the repository
documentation skill. It uses your configured pi model; select the working GPT 6
option with `/model` if needed. It does not change your saved model settings.

Pi should read the exercise, ask you to inspect the runner, and wait for your
assessment. Edit `runner.py` in your usual editor. Tell pi when you are ready
for feedback. Ask for a small hint whenever needed; the tutor should not rewrite
your implementation without an explicit request.

## Run and test

From the repository root, run the behavioral tests:

```bash
python3 -m unittest discover -s exercises/experiment_runner -p 'test_runner.py' -v
```

For one manual run, choose a disposable output directory:

```bash
python3 exercises/experiment_runner/runner.py --output-dir /tmp/learn-experiment-demo --run-name demo
```

The demo writes `/tmp/learn-experiment-demo/demo.json` and prints the report.
Repeating that command overwrites that demo report. Tests use their own temporary
directories and do not need the manual demo.

## Behavior to preserve

Keep `run_experiment(config, output_dir)` and the CLI working while changing
internals freely. You may add modules beside `runner.py`.

| Input | Contract |
|---|---|
| `run_name` | Required nonempty string containing only ASCII letters, digits, `_`, or `-`. |
| `dataset` | `tiny` by default, or `shifted`. |
| `scale` | Finite integer or float, default `1.0`; booleans are rejected. |
| Other configuration keys | Ignored; the caller's configuration is not mutated. |

`tiny` has inputs `[1, 2, 3, 4]` and targets `[2, 4, 6, 8]`.
`shifted` has inputs `[-2, 0, 2]` and targets `[-4, 0, 4]`.
The fake model multiplies each input by `scale`; no fitting takes place.

Return a report with exactly `run_name`, `dataset`, `scale`, `count`,
`predictions`, and `mae` (mean absolute error against the targets). Write the
same data as JSON to `<output_dir>/<run_name>.json`, creating parent directories
and replacing a report with that name. Reject invalid configuration with
`ValueError` before creating or modifying output files. Filesystem failures may
propagate; transactional storage is outside this first exercise.
Scales that overflow float conversion, predictions, or the error calculation
are also rejected before writing a report.

## Learning sequence

1. Read the starter and tests. Explain the behavior and likely change points.
2. Propose a small refactor and explain its tradeoffs before implementing it.
3. Refactor, preserving behavior and keeping tests passing. Add tests for any
   contract gaps you identify; do not weaken existing assertions to get a pass.
4. Explain your design. Pi will review responsibility boundaries, testability,
   error handling, and the cost of your abstractions.
5. Take on a new requirement introduced by the tutor, then compare designs.
6. Complete a related small task independently and explain your decisions.

Passing tests establishes behavior for covered cases, not design mastery or ML
quality. There is no requirement to use an ABC, a protocol, or any named pattern;
justify whichever approach you choose.

## Save and resume

Ask pi to record a checkpoint before stopping. It should update
`docs/daily_journals/learning/YYYY-MM-DD.md` with observations, hints used,
test results, current stage, and next action while preserving your own notes.
It must not mark this exercise complete just because the starter passes tests.

To resume the last pi session in this repository:

```bash
bash scripts/start-coding-exercise.sh --continue
```

If that resumes a different conversation, use `--resume` to select the exercise
session or start fresh and ask pi to read the latest learning checkpoint.
Session resumption and journal editing still need validation in a real lesson.

See [learning topics](../../docs/learning-topics.md) for the broader direction
and [local/HPC boundaries](../../docs/local-hpc-testing-protocol.md) before
extending this exercise to actual ML execution.
