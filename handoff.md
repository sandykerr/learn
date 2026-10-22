# Pi tutoring system: handoff

Last updated: 2026-10-15.

## Intent

The user wants a personal learning system based on `amosblomqvist/learn`, including practical coding skills. The agreed direction is **pi for tutoring in a WSL terminal, and Codex for developing and maintaining this repository**. The user explicitly accepted this division after discussing the existing pi quiz UI.

This replaces the earlier proposal to host tutoring and a custom quiz interface in Codex. Preserve the original pi implementation as a reference and adapt its teaching workflow as needed. Review relevant Alvarmethod skills for useful elements; their final location and integration with pi remain undecided.

The current checkout is `/home/ajkerr1/development/learn`. Fork ownership and remotes have not been verified. No components have been ported or runtime setup validated during this follow-up.

The implementation roadmap is [docs/implementation-plan.md](docs/implementation-plan.md). It contains numbered steps, sub-steps, completion criteria, and the user's requested status labels: `[Complete]`, `[Planned]`, `[In-Progress]`, `[Deferred]`, and `[Skipped]`. Keep it updated as work proceeds.

## Setup verification update — 2026-10-22

- Origin is `git@github.com:sandykerr/learn.git`; branch `main`, HEAD `7cfd894`. Fork relationship and remote access have not been independently checked.
- Linux Node v24.22.0 and npm 12.2.0 resolve through nvm; WSL2 confirmed.
- The user installed pi 1.4.0 via `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`.
- A direct check with the installed pi extension loader loaded `extensions/quiz.ts` and `extensions/ask-user-question.ts`, registering both tools with no errors or warnings. The loader includes aliases for their older `@mariozechner` imports. This does not yet validate interactive rendering or grading.
- The user has a Codex/ChatGPT Pro subscription and is new to pi. Installed pi offers OpenAI → Sign in with ChatGPT; the next user action is interactive `/login openai`. Account access is not yet verified.
- Step 2 of the plan is [In-Progress]. License verification remains unresolved; no upstream license was found locally, and an attempted Alvarmethod LICENSE fetch failed.
- Historical statements below about unverified installation or Node resolution are superseded by this update. No tutoring session has been completed.

## Environment and setup findings

- Current checkout: `/home/ajkerr1/development/learn`.
- User: `ajkerr1`; Ubuntu on WSL2, confirmed through `/proc/version`.
- Codex can read this checkout and run Linux shell commands.
- Initially, `npm` and `npx` resolved to `/mnt/c/Program Files/nodejs/`, and Linux `node` was missing. Running the skill installer launched `CMD.EXE`, which rejected the WSL UNC working-directory path.
- We recommended installing Linux Node through nvm inside WSL and retrying the installer. The user subsequently reported that installation succeeded. We verified the resulting skill files, but did not recheck Node resolution afterward.

The successful command reported by the user was:

```bash
npx skills add vasanthsreeram/Alvarmethod -g -y -a codex
```

All five skills were verified in the user's home directory, each with a `SKILL.md`:

```text
/home/ajkerr1/.agents/skills/teach/
/home/ajkerr1/.agents/skills/probe/
/home/ajkerr1/.agents/skills/learn-profile/
/home/ajkerr1/.agents/skills/learn-visual/
/home/ajkerr1/.agents/skills/learn-verify/
```

All five appeared in both the original and follow-up Codex sessions' available skills. They are globally installed, not project-local copies. A new agent should inspect its own available tools and skills rather than assume this session's capabilities persist.

## Original repo

Upstream: <https://github.com/amosblomqvist/learn>

This is a pi configuration, intended to be cloned into a learning project's `.pi` directory. It is not a Codex plugin.

Relevant files:

- `skills/teach/SKILL.md`: original teaching philosophy and probe → plan → teach process.
- `skills/visualize/SKILL.md`: teaching visualization instructions.
- `extensions/ask-user-question.ts`: implements `ask_user_question` using `pi.registerTool` (registration near line 569).
- `extensions/quiz.ts`: implements the graded `quiz` tool using `pi.registerTool` (registration near line 877).
- `extensions/md-log.ts`: session/Markdown logging integration.
- `extensions/visual-tools/`: Mermaid and SVG tools for pi subagents.
- `agents/`: researcher, SVG maker, and Mermaid maker definitions.

There is no separate `probe` skill in this repo; that skill comes from Alvarmethod.

The pi quiz implementation supports graded choices, feedback, an “I don't know” choice, and optional learner notes. The question and quiz extensions coordinate popups through a shared UI lock. These are pi runtime/UI integrations; having their TypeScript files in a Codex workspace does not make their tools callable by Codex.

`extensions/visual-tools/package.json` includes:

- `@mermaid-js/mermaid-cli` as a dependency.
- A pi development dependency pointing to the original author's machine:
  `file:/Users/amos/.nvm/versions/node/v24.14.0/lib/node_modules/@earendil-works/pi-coding-agent`.

That absolute path would need fixing if installing the original visual tooling here. It is not a dependency of the globally installed Alvarmethod Markdown skills. Avoid treating an npm install in the original extension directory as a fix for Codex's missing quiz tool.

## Alvarmethod adaptation

Project: <https://github.com/vasanthsreeram/Alvarmethod>

Online research found this adaptation, which explicitly advertises Codex support. It reimplements the learning method from the same video as portable skills rather than fully porting the original pi extensions and Obsidian workflow.

Its skills cover teaching, diagnostic probing, learner preferences, visual explanations, and verification. Its documented session artifacts live under `.alvar/`, including learner profiles, concept maps, session notes, and visuals.

We reviewed the README and relevant installed skill instructions. We have not validated an end-to-end teaching session or audited the complete project.

## Historical Codex quiz compatibility gap

The user explicitly tested:

> Use the probe skill to ask me one diagnostic question about fractions. First check whether its required quiz tool is available.

We inspected:

```text
~/.agents/skills/probe/SKILL.md
~/.agents/skills/teach/references/quiz-ui.md
```

The probe skill requires a quiz UI. Its reference expects `ask_user_question` for Codex and states:

> No match → say which tool is missing and stop. Do not fall back to pasted multiple choice.

It also explicitly says:

> Do not use `request_user_input` for graded quizzes.

The original test session did not expose `ask_user_question` or the pi `quiz` tool. It exposed differently named user-input tools with their own restrictions. The test therefore stopped before asking a fractions question, as required by the installed skill. No answer was collected or graded.

This established that installation and skill discovery worked, but the advertised quiz workflow did not work unchanged in that Codex session. This gap motivated the discussion; it does not block the newly selected pi tutoring approach. Installing another npm package alone will not register a new Codex tool. Do not silently substitute a preference/approval tool for a graded quiz without checking its supported purpose and behavior.

## Agreed project direction and milestones

1. Verify the checkout, Linux Node setup, pi installation/API compatibility, provider authentication options, and upstream licenses.
2. Establish a reproducible pi launch configuration. This repo represents a `.pi` directory; do not assume launching pi from the checkout root automatically loads its contents.
3. Load the bundled question and quiz extensions together, preserving their shared UI lock.
4. Complete one fractions quiz: present → answer → grade and explain → save progress → resume in a later session.
5. Personalize the teaching instructions, then add coding exercises using real files, tests, review, and progressive hints.
6. Document and validate setup and resumption. Revisit research subagents and visualization after the core milestones work.

First milestone: **a working pi tutoring session in WSL with one interactive fractions quiz and saved progress**.

Second milestone: **a practical coding lesson where the learner writes and runs code, receives feedback, and completes an independent follow-up exercise**.

A Codex-hosted browser/MCP quiz bridge and porting pi UI extensions into Codex are marked `[Skipped]` in the plan because pi is the selected tutoring runtime. Advanced research and visualization are `[Deferred]`. Project direction and planning are `[Complete]`; implementation steps remain `[Planned]`.

## Coding-learning findings

The original `skills/teach/SKILL.md` is subject-independent and supports assessing prerequisites, planning a lesson, explaining concepts, and checking understanding. It can be used for programming concepts.

The bundled quiz is choice-based, not a code editor or automatic coding-exercise grader. Practical coding lessons will need explicit instructions for learner-written files, execution/tests, review, hints before solutions, and follow-up tasks. Do not let the tutor overwrite learner attempts while giving feedback. Passing tests alone should not be treated as proof of understanding.

The first language and coding objective have not been selected. Learner artifact locations, progress schema, and final skill discovery configuration also remain open. The original teaching instructions assume Obsidian rendering and researcher subagents; adapt these assumptions to the tools actually configured rather than treating them as already available.

## Work completed in the follow-up conversation

- Read the handoff, repository README, original teaching skill, and relevant quiz implementation details.
- Checked documentation supporting pi's terminal extension UI; no live pi session was launched.
- Recorded the user's choice of pi for tutoring and Codex for development.
- Created [docs/implementation-plan.md](docs/implementation-plan.md) with the requested status convention.
- Updated this handoff to reflect the agreed direction.

Only documentation has been changed. No skill rewrites, dependency installations by the agent, integration configuration, commits, or pushes have been performed. Linux Node resolution, installed pi version, provider access, end-to-end quiz behavior, and progress persistence remain unverified.

## Suggested first actions in the next conversation

1. Read this handoff, [docs/implementation-plan.md](docs/implementation-plan.md), and any applicable `AGENTS.md` files.
2. Start step 2 of the plan: confirm the fork's remote, working tree, Linux Node setup, pi installation, and available provider authentication method. Do not expose credentials.
3. Check both upstream licenses before copying or redistributing code or skills. Alvarmethod's README claims MIT licensing; inspect its actual license. The original checkout's file search did not find a LICENSE/COPYING file, so do not assume a grant from its public availability.
4. Determine how to load this repository's configuration into pi and verify extension compatibility.
5. Implement and test the smallest complete fractions quiz, including saved progress, updating plan statuses and evidence as work proceeds.

## Useful references

- Original project: <https://github.com/amosblomqvist/learn>
- Alvarmethod: <https://github.com/vasanthsreeram/Alvarmethod>
- Microsoft's Node-on-WSL setup guidance: <https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl>

## Suggested opening prompt

> Read handoff.md and docs/implementation-plan.md. We have chosen pi for tutoring in a WSL terminal and Codex for developing this repo. Start with step 2 of the plan: verify the checkout, environment, pi setup, and licenses. Then work toward one interactive fractions quiz with saved progress, preserving the original implementation as a reference. Update plan statuses as work proceeds.
