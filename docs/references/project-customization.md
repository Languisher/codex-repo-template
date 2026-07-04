# Project Customization Reference

Use this checklist when adapting the template to a real repository.

## Required

- Replace placeholders in `AGENTS.md`.
- Fill `docs/architecture.md`, `docs/development.md`, and `docs/testing.md`.
- Implement all scripts under `scripts/`.
- Add real tests under `tests/`.
- Decide which skills are relevant and remove unused ones.

## Optional

- Add nested `AGENTS.md` or `AGENTS.override.md` files for services or
  packages with local rules.
- Add `evals/` for model, data, recommendation, search, or agentic workflows.
- Add `.codex/hooks.json` hooks only when they are supported and useful.
- Add project-type skill templates under `.agents/skill-templates/`.
