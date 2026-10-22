---
name: repo-documentation
description: Maintain this learning repository's documentation and daily learning/development journals. Use when recording learning activity, documenting repository changes or validation, or organizing project documentation.
---

# Repository documentation

Keep documentation concise, reusable, and easy to navigate. Read existing files
before editing; extend the relevant document rather than creating a competing
source of truth.

## Daily journals

Maintain one Markdown file per active day and journal type:

- `docs/daily_journals/learning/YYYY-MM-DD.md`: learning undertaken that day.
- `docs/daily_journals/development/YYYY-MM-DD.md`: features or behavior added,
  tested, changed, or removed that day.

Use the user's local date (America/New_York unless updated). Update the existing
daily file across sessions. Create an entry when there is relevant activity;
do not generate empty entries for inactive days or invent retrospective events.

Learning journals are shared between the user and agents. Preserve manual notes,
reflections, and edits. Add concise agent observations without rewriting the
user's voice or claiming unobserved understanding. Record topics and exercises,
evidence of progress, open questions, and useful next steps. Distinguish the
learner's self-assessment from observed exercise results. Planning a curriculum
does not establish that its topics were learned.

Development journals summarize meaningful additions, changes, removals, and
validation results. Link relevant files, exercises, or commits when available.
Distinguish tests actually run from planned checks, and user-reported results
from agent-verified results. Include pending checks or limitations when they
affect the interpretation of the day's work. Do not turn the journal into a
command transcript or repeat unchanged status on every update.

Before finishing substantive learning or development work, update the relevant
journal; update both only when both kinds of activity occurred. Keep entries
short and consolidate repetition while preserving user-authored content. If
manual notes conflict with new evidence, add a clearly attributed correction
or question rather than silently replacing them.

## Concise, reusable documents

Keep high-level documents focused on purpose, decisions, current status, and
next steps. Put detailed procedures, examples, and technical evidence in focused
documents and link to them from the overview. Keep reusable instructions in
their canonical document; journals should link to them and record what happened.

Avoid duplicating large explanations across handoffs, plans, topic outlines,
and journals. Update stale high-level statements when work changes them, while
preserving dated history as history. Do not split short coherent documents into
many tiny files solely to make each file shorter.

## Navigation

As files accumulate and their purposes become difficult to scan, add or update
a concise file index or reference sheet, such as `docs/README.md`. Group links
by purpose with a short description. For large journal collections, use a
journal index or monthly reference sheet rather than listing every daily entry
in the top-level overview. Choose indexes based on navigation needs, not an
arbitrary file-count threshold.

When moving or renaming documents, update incoming links and relevant indexes.
Use repository-relative links in saved documentation. Check changed paths and
links before finishing. Keep credentials and private workplace data out of docs.
