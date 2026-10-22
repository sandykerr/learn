# Pi tutoring system implementation plan

## Goal and direction

Use pi in a WSL terminal for tutoring and use Codex to develop and maintain this repository. Preserve the original pi implementation as a reference. Adapt the teaching workflow to personal learning preferences and practical coding exercises.

The first milestone is one working interactive fractions quiz in pi: present a question, collect an answer, show grading and feedback, and save progress. The next milestone is a coding lesson in which the learner edits a real file, runs tests, receives hints, and completes a follow-up exercise.

This plan supersedes the Codex-hosted tutoring direction proposed in `../handoff.md`. The handoff remains historical context. No working pi session or coding exercise has been validated yet.

## Status conventions

- **[Complete]** — Finished, with relevant results verified.
- **[Planned]** — Intended work that has not started.
- **[In-Progress]** — Work currently underway.
- **[Deferred]** — Intentionally postponed; revisit when the stated condition applies.
- **[Skipped]** — Intentionally excluded from this approach, with a reason recorded.

Update sub-step statuses as work proceeds. Mark a parent step [Complete] when its required sub-steps and completion criteria are satisfied; explain any deferred or skipped sub-steps. Record concrete validation evidence alongside completed implementation work.

## 1. [Complete] Establish the project direction

- [Complete] Read the handoff and inspect the original repository's teaching instructions and quiz interface.
- [Complete] Choose pi for the tutoring runtime and terminal UI.
- [Complete] Choose Codex for repository development and maintenance.
- [Complete] Identify coding skills as an intended learning use case.
- [Complete] Record a phased implementation plan in `docs/`.

Evidence: repository inspection and the user's decisions in the planning conversation. These decisions establish direction, not runtime compatibility.

## 2. [In-Progress] Verify the repository, environment, and licenses

- [Planned] Confirm Git remotes, fork ownership, branch, and existing local changes. Establish an identifiable upstream reference before changing original components.
- [Complete] Check Linux `node`, `npm`, and `npx` resolution in WSL and record versions. Verified 2026-10-22: all resolve under `/home/ajkerr1/.nvm/versions/node/v24.22.0/bin`; Node v24.22.0 and npm 12.2.0.
- [Complete] Check whether pi is installed, identify its version, and compare its extension API with the bundled code. Verified pi 1.4.0 after user installation; both bundled tools register through its extension loader with no errors or warnings. Interactive rendering and grading remain to be tested.
- [Planned] Verify an available model provider and authentication method for pi without recording credentials.
- [Planned] Inspect the actual upstream licenses for this repository and Alvarmethod before copying or redistributing material. Record any unresolved permissions and how they affect implementation.
- [Planned] Document the verified setup and remaining prerequisites in `docs/`.

Verification notes (2026-10-22): `origin` is `git@github.com:sandykerr/learn.git`, branch `main`, HEAD `7cfd894`. Only `docs/` and `handoff.md` are untracked; no tracked modifications were reported. WSL2 is confirmed. Pi was initially absent; the user subsequently installed pi 1.4.0 through npm. Its loader supplies compatibility aliases for the older `@mariozechner` imports. A direct loader check registered `quiz` and `ask_user_question` without errors or warnings; no model request or interactive quiz was run. No upstream license file was found locally or in the original repository root listing; fetching Alvarmethod’s LICENSE failed, so its actual license remains unverified. The user selected their existing Codex/ChatGPT Pro subscription. Installed pi offers OpenAI → Sign in with ChatGPT; authentication and account access remain pending.

Completion criteria: the intended checkout is identified, runtime prerequisites are known, and licensing constraints are recorded before dependent copying or distribution work.

## 3. [Planned] Establish a reproducible pi launch configuration

- [Planned] Choose how this checkout is loaded as pi configuration. The repository root currently represents a `.pi` directory; verify discovery rather than assuming pi loads its extensions from any working directory.
- [Planned] Define a separate learner workspace for exercises and progress, and decide which artifacts belong in version control.
- [Planned] Install or configure only the dependencies required for the initial quiz workflow.
- [Planned] Load the bundled `quiz` and `ask_user_question` extensions together so their shared popup lock remains effective.
- [Planned] Verify the teaching skill and both tools appear in the running pi session.
- [Planned] Add project guidance in `AGENTS.md` and document exact launch commands and required setup.
- [Planned] Preserve the original implementation through an upstream reference and clearly document intentional adaptations.

Completion criteria: a documented command starts pi in WSL with the required teaching skill and question tools loaded, without extension errors.

## 4. [Planned] Complete one interactive fractions quiz

- [Planned] Run a small, deterministic fractions question through the existing quiz UI.
- [Planned] Verify that the answer and explanation remain hidden in the learner-facing UI until submission.
- [Planned] Check correct, incorrect, “I don't know,” and cancellation outcomes.
- [Planned] Confirm the tutor receives the selected answer and result and can respond appropriately.
- [Planned] Define a minimal progress record: topic, question, response, result, timestamp, and next learning step. Distinguish cancellation from a knowledge gap.
- [Planned] Save the result in the learner workspace and verify it can be read in a subsequent session.
- [Planned] Record the manual test results and any compatibility fixes.

Completion criteria: the learner completes a real terminal quiz, receives feedback, and can resume from saved progress. This is the first working milestone.

## 5. [Planned] Adapt the teaching workflow to the learner

- [Planned] Review the original teaching approach and relevant Alvarmethod skills, choosing useful elements after the license review.
- [Planned] Select a canonical location for pi teaching instructions and learner artifacts. Check skill discovery and avoid ambiguous duplicate skill names.
- [Planned] Capture learning goals, experience, preferred pace, and desired hint level.
- [Planned] Retain the probe → plan → teach structure while allowing practical exercises to demonstrate understanding.
- [Planned] Remove assumptions specific to the original author's setup, including mandatory Obsidian rendering where inappropriate for a terminal session.
- [Planned] Define how the tutor verifies uncertain claims using tools actually available in the selected configuration.
- [Planned] Validate a short lesson and refine instructions based on the learner's experience.

Completion criteria: pi follows the personalized instructions and uses the chosen progress files consistently across sessions.

## 6. [Planned] Add practical coding exercises

- [Planned] Select the first programming language and a small learning objective with the learner.
- [Planned] Create an exercise workspace with clear instructions, starter files, and a documented run/test command.
- [Planned] Define tutor behavior: let the learner attempt the task, inspect their code, give progressively stronger hints, and reveal a full solution when requested or agreed.
- [Planned] Separate learner work from reference solutions and avoid overwriting an attempt during feedback.
- [Planned] Add meaningful tests for expected behavior and relevant edge cases. Use code review and explanation checks for qualities tests cannot establish.
- [Planned] Incorporate debugging and explaining why a solution works, alongside getting tests to pass.
- [Planned] Save demonstrated skills, misconceptions, hints used, and a suggested next exercise.
- [Planned] Run one complete coding lesson followed by a related task the learner solves independently.

Completion criteria: the learner writes and runs real code, receives evidence-based feedback, and demonstrates transfer on a follow-up task. This is the second working milestone.

## 7. [Planned] Make the workflow reliable and easy to resume

- [Planned] Document installation, provider setup, launch, exercise execution, progress storage, and session resumption.
- [Planned] Document recovery from missing tools, extension failures, interrupted quizzes, and failed test commands.
- [Planned] Validate the documented setup from a fresh learner workspace.
- [Planned] Add targeted regression checks for custom behavior introduced during implementation.
- [Planned] Review which configuration, exercises, and progress artifacts should be shared or kept personal.

Completion criteria: the documented workflow reproduces both milestones and resumes saved learning progress without relying on undocumented session state.

## 8. [Deferred] Add advanced research and visual teaching tools

Revisit after the quiz and coding lesson milestones work reliably and the learner identifies a need.

- [Deferred] Evaluate researcher and visualization subagents, including whether tmux is worth adding.
- [Deferred] Repair machine-specific visual tooling dependencies if those tools are adopted.
- [Deferred] Choose how diagrams and rendered math are viewed alongside terminal tutoring.
- [Deferred] Consider richer curriculum maps and progress summaries based on actual use.

## 9. [Skipped] Build a Codex-hosted quiz interface

- [Skipped] Build a browser/MCP quiz bridge for Codex. The selected tutoring runtime is pi, which already has the intended interface.
- [Skipped] Port pi UI extensions into Codex for the first milestones. Codex is the development environment for this project.

Revisit only if the user later chooses to run tutoring sessions in Codex.
