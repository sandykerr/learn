#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$repo_root"

if ! command -v pi >/dev/null 2>&1; then
  echo 'pi is not on PATH. Open the WSL shell where pi is installed.' >&2
  exit 127
fi

exec pi \
  --no-extensions \
  --no-skills \
  --no-prompt-templates \
  --no-mcp \
  --extension "$repo_root/extensions/quiz.ts" \
  --extension "$repo_root/extensions/ask-user-question.ts" \
  --skill "$repo_root/skills/repo-documentation/SKILL.md" \
  --append-system-prompt "$repo_root/exercises/experiment_runner/TUTOR.md" \
  "$@" \
  'Begin or resume the experiment_runner lesson using the exercise tutor instructions. Read any relevant learning checkpoint; let me do the analysis and coding.'
