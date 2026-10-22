---
name: learn-repo-workflow
description: Coordinate work in this learning repository through user-approved agent setups. Use for requested repository development, documentation, investigation, and validation tasks.
---

# Main repository workflow

Pi hosts tutoring sessions; Codex develops and maintains this repository. This
is the main coordination skill for repository work. It must be explicitly loaded
or referenced by the agent's project instructions; a root `SKILL.md` alone does
not guarantee automatic discovery in every client.

## Propose before acting

For each new task requested by the user, make the first response a concise
proposal for the agent setup. Do this before task-specific tool calls, file
edits, commands, or spawning agents.

The proposal must state:

- The intended outcome and scope.
- Whether the main agent will work alone or use one to three subagents.
- Each agent's responsibility and why that division is useful.
- How the main agent will integrate and verify the result.

For a small task, a single sentence explaining that the main agent alone will
make and check the change is sufficient. Do not delegate merely to fill slots.

**Wait for the user's approval, modification, or rejection before executing.**
This checkpoint is an explicit user preference, including for main-agent-only
work. When asking, identify this skill and its approval requirement. Silence is
not approval. If the user modifies the setup, follow their approved revision;
if they reject it, do not start the proposed work.

An approval message continues the existing task; it does not trigger another
proposal-and-approval loop. After approval, complete the authorized task,
including normal validation and documentation, without repeatedly asking for
permission. Seek a revised approval if scope or the agreed agent setup materially
changes. A status question or clarification during work does not by itself
replace the task or reset its approval.

## Use up to three subagents when applicable

Use at most three concurrent subagents in total, in addition to the main agent,
subject to the tools available in the session. Count any nested delegation
toward that limit and keep it within the approved setup. If delegation is not
available, disclose that in the proposal and offer main-agent-only execution.

Delegate bounded, separable work where parallel investigation, implementation,
or independent review improves the outcome. Give each subagent its objective,
context, expected output, validation responsibility, and file ownership when
editing. Avoid concurrent edits to the same files.

The main agent owns integration, resolving conflicting findings, reviewing
changes, and reporting evidence and limitations. Delegation does not expand the
authorized scope or grant permission to publish, push, or submit HPC jobs.

## Related repository guidance

- Follow [the documentation skill](skills/repo-documentation/SKILL.md) for
  concise documents and daily journal updates, preserving manual user edits.
- Read [the local/HPC protocol](docs/local-hpc-testing-protocol.md) before
  selecting or running tests.
- Keep [the implementation plan](docs/implementation-plan.md) accurate as
  milestones change. Distinguish completed setup from unverified learner outcomes.
