# Local versus HPC testing for learning exercises

Established 2026-10-22. Read before selecting or running exercise tests.
Adapted from `/home/ajkerr1/development/lecospy/.agents/local_hpc_testing_protocol.md`.
This version applies to this learning repository; it does not configure access
or authorize jobs on the work HPC system.

## Scope

Use local execution to learn and check software design with small fixtures.
Use HPC for meaningful ML execution, real datasets, geospatial integration,
and performance experiments. Classify checks by what they execute, including
transitive dependencies, rather than their names or use of synthetic data.

Do not import LECOSPy's datasets, credentials, container paths, accounts,
partitions, or production job settings into exercises. The applicable cluster
and its approved environment must be established before preparing runnable jobs.

## Local checks

Local checks must remain lightweight individually and in aggregate. There is
no fixed test-count limit. Suitable examples include:

- Syntax, import, type, lint, configuration, and serialization checks that do
  not initialize expensive services, load models, or perform remote calls.
- Unit tests for object invariants, protocols, composition, dependency
  injection, state transitions, and error handling using small in-memory data.
- Small NumPy calculations that do not invoke GDAL or become training workloads.
- Fake model, dataset, storage, scheduler, and agent-tool implementations.
- Mocked subprocess, Slurm, container, retry, and parallel-dispatch tests that
  do not launch real jobs or workers for performance measurement.
- Bounded inspection of returned logs, summaries, and a few metadata records;
  not dataset discovery or full-manifest validation.

Agent exercises default to fake model/tool responses for repeatable local
checks. A live model or external tool integration is a separate check: state
its purpose, request/action bounds, and expected side effects before execution.
Such an integration is not automatically an HPC job.

## HPC-only checks

Use the appropriate Slurm allocation and approved container/environment for:

- Actual model training, fine-tuning, meaningful inference/evaluation runs,
  GPU execution, dataset preparation, and computationally substantial workflows.
- Real-data discovery, full-manifest checks, and dataset-wide diagnostics.
- Any direct GDAL execution, including `osgeo`, GDAL-backed Rasterio, synthetic
  raster fixtures, metadata opens, reprojection, and vector export.
- Real raster processing, including headers, masks, pixels, checksums, and writes.
- Performance measurements: timing comparisons, profiling, throughput, memory
  scaling, multiprocessing/worker comparisons, I/O contention, and cache behavior,
  including those using synthetic data. Normal test-runner elapsed times are
  not benchmark results.

Do not run these on a cluster login node. If a dependency's behavior is unclear,
inspect it before local execution or leave the check pending for HPC.

## Bound each HPC exercise

Before running, record explicit limits appropriate to the learning objective:

- Dataset subset, maximum records/files/windows, and permitted input location.
- Training steps/epochs or inference batches; no open-ended parameter searches.
- CPU count, memory, GPU count if needed, worker count, and wall-time limit.
- Output location and expected artifact size; avoid unnecessary raw-data copies.
- Retry limit and stop conditions for invalid input, failed setup, or exhausted
  resources. Do not automatically scale up resources or resubmit indefinitely.

No universal numeric limits are assumed: choose and record them for the exercise
and the cluster allocation. Prefer the smallest run that answers the question.
Preserve partial results and explicit failures when practical.

## Validation and handoff

1. Select local-safe checks explicitly. Run a broad suite only after confirming
   that every selected test respects these boundaries.
2. Report what local checks establish and which integrations remain untested.
3. Prepare the bounded HPC job using verified cluster details. Job preparation
   does not count as execution; submission must be within the user's authorized
   scope and workplace rules.
4. Record code revision or patch, configuration, dataset subset identity,
   dependency/container version, random seed where relevant, requested resources,
   job ID, and exit status. Keep secrets and workplace data out of this repository.
5. Review compact logs, test summaries, and artifact checksums when appropriate.
   Do not request raw dataset folders as routine evidence.
6. Mark an HPC check complete only after reviewing its returned evidence. If HPC
   is unavailable, keep it pending and continue with independent local work.

Passing fakes does not establish model quality, scheduler/container behavior,
GDAL correctness, or production throughput. An exercise may demonstrate a sound
interface locally while its real integration remains pending.
