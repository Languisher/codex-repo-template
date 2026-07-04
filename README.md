# Codex Project Template

This repository is a starting template for projects that should work well with
Codex. It separates context into durable rules, task-specific skills, and
executable verification.

## Use This Template

1. Copy the files into a new or existing repository.
2. Replace placeholders in `AGENTS.md` and `docs/`.
3. Implement the real commands in `scripts/`.
4. Keep reusable task workflows in `.agents/skills/`.
5. Treat `./scripts/verify.sh` as the final done check.

## Context Layers

- `AGENTS.md`: always-loaded project contract.
- `.agents/skills/`: workflows Codex loads only for matching tasks.
- `scripts/`, `tests/`, `evals/`: executable checks that turn requirements into
  feedback.

The template is intentionally language-neutral. Add package manager, runtime,
test runner, and CI details only after the host project chooses them.

## Included Variants

- `templates/python-uv-agents/AGENTS.md`: Python project instructions that
  require `uv` for environment management and `stdlogkit` for production
  logging.
- `.agents/skill-templates/python-uv-project/SKILL.md`: matching Codex skill
  template for Python implementation work.
- `docs/references/python-uv-project.md`: supporting reference with suggested
  script bodies and project conventions.
