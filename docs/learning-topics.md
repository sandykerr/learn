# Possible learning topics

## Learner and purpose

The learner has a computer science background, knows Python fairly well, and
runs ML workflows on a work HPC system. The goal is stronger software engineering
judgment for data science, ML, and agentic applications, with emphasis on advanced
object-oriented design where it improves the software.

This is a candidate topic map, not an assessed curriculum or a list of knowledge
gaps. Start with a bounded diagnostic exercise, then choose depth and order from
the learner's work. Python fundamentals need review only when a specific gap
appears. Use pi for tutoring and Codex to maintain the framework.

## Candidate topics

| Topic | Design questions | Possible exercise |
|---|---|---|
| Responsibilities and composition | Which objects own which decisions? When is a function enough? | Split a tangled experiment runner into testable collaborators while preserving behavior. |
| Protocols, ABCs, and substitutability | What contract do callers need? When should an interface be structural or explicit? | Support two model backends and expose an implementation that violates the shared contract. |
| Dependency injection and boundaries | Where should concrete services be constructed? | Inject dataset, model, artifact store, and logging dependencies through one composition entry point. |
| Invariants, ownership, and lifecycle | How can invalid states be prevented? Who owns mutable data and resources? | Model configured, fitted, and closed states; test invalid transitions and aliasing bugs. |
| Python object model | How do attribute lookup, descriptors, MRO, and special methods affect an API? | Diagnose a subtle inheritance bug and compare a composition-based alternative. |
| Configuration and domain types | How do validation, immutability, defaults, and serialization interact? | Replace an unstructured configuration dictionary with validated types and round-trip tests. |
| Pipeline and plugin design | How can steps vary without an inheritance explosion? | Add preprocessing and evaluation strategies, then introduce a new requirement that challenges the abstraction. |
| Testing design contracts | What do unit tests, fakes, integration tests, and property-based tests each establish? | Create behavioral contracts for interchangeable components and identify what mocked tests miss. |
| Reproducibility and artifacts | What must be recorded to reproduce or resume an experiment? | Design run identity, configuration snapshots, checkpoint metadata, and schema migration. |
| HPC execution architecture | How should scientific logic be separated from scheduler and container details? | Design an execution backend, verify command construction with fakes, then prepare one bounded HPC smoke test. |
| Concurrency and resource management | What changes across process boundaries? How are cleanup and cancellation handled? | Refactor a worker API to make serialization and resource ownership explicit; benchmark only on HPC. |
| Failure handling and observability | Which failures are retryable? How can partial results remain useful? | Add bounded retries, structured errors, and resumable output to a pipeline without hiding failures. |
| Agent orchestration and tool contracts | How are model calls, tool actions, state, and control flow separated? | Build a small agent state machine with fake model responses and typed tool results. |
| Agent evaluation and nondeterminism | What is deterministic correctness versus empirical quality? | Test orchestration invariants locally and design a separate bounded live evaluation. |
| Patterns and architectural tradeoffs | When do strategy, adapter, factory, or ports-and-adapters simplify change? | Compare two designs against the same evolving requirements, including the cost of added abstraction. |

## Suggested first exercise

Refactor a small experiment runner that combines loading, model construction,
evaluation, and artifact writing. Use tiny in-memory fixtures and a fake model
so the initial exercise is local-safe and requires no cluster or ML framework.

1. Explain the existing behavior and identify likely change points.
2. Add or inspect behavioral tests, then refactor without changing outcomes.
3. Explain responsibility boundaries and why each abstraction is warranted.
4. Introduce a second backend or artifact destination and assess the changes needed.
5. Compare an alternative design and identify tradeoffs, not a single ideal hierarchy.
6. Complete a related task with less guidance and record demonstrated understanding.

Later, replace a fake with a real backend in a separately bounded HPC exercise.
Follow [the testing protocol](local-hpc-testing-protocol.md); local correctness
must not be presented as evidence of HPC execution or model performance.

## Tutoring and assessment

- Use the existing quiz UI for focused concept checks and code-output predictions.
- Use real files, tests, and code review for implementation and design exercises.
- Preserve the learner's attempts; offer progressively stronger hints before solutions.
- Assess behavior, clarity, changeability, resource ownership, and the explanation
  of tradeoffs. Passing tests alone is insufficient evidence of design understanding.
- Record observed strengths, misconceptions, hints used, and a follow-up objective.

## Decisions still open

Choose the first exercise after the diagnostic, then decide which Python typing
and testing tools it needs. Select a real ML framework and cluster integration
only when a later exercise requires them. Avoid installing a broad training stack
or adopting a pattern catalog before there is a concrete learning need.
