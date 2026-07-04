# Codex Workflow Reference

This template was built from current public Codex guidance and keeps the
practical parts in the repository so future Codex sessions do not need to
rediscover them.

## Source Links

- Codex best practices:
  https://developers.openai.com/codex/learn/best-practices
- Custom instructions with `AGENTS.md`:
  https://developers.openai.com/codex/guides/agents-md
- Codex config basics:
  https://developers.openai.com/codex/config-basic
- Codex skills:
  https://developers.openai.com/codex/skills
- Codex non-interactive mode:
  https://developers.openai.com/codex/noninteractive
- uv in GitHub Actions:
  https://docs.astral.sh/uv/guides/integration/github/

## Local Mapping

- Durable repository guidance lives in `AGENTS.md`.
- Project-scoped Codex defaults live in `.codex/config.toml`.
- Reusable repo workflow guidance lives in
  `.agents/skills/hello-world-maintenance/SKILL.md`.
- Larger tasks can use `docs/exec-plans/templates/hello-world-plan.md`.
- Standard validation is `uv sync --locked`, `uv run pytest`,
  `uv run ruff check .`, and `uv run ruff format --check .`.
- GitHub Actions runs the standard validation in `.github/workflows/ci.yml`.

## Prompt Shape

Good Codex prompts for this repository include:

- Goal: the behavior or documentation outcome.
- Context: relevant files, errors, or previous attempts.
- Constraints: TOML-only config, `uv`, no unnecessary dependencies, and small
  changes.
- Done when: exact validation commands and expected output.

## Automation Notes

Use `codex exec` for scripted Codex runs only when the prompt, sandbox, and
approval behavior are explicit. Do not expose API keys to repository-controlled
commands in the same job.
