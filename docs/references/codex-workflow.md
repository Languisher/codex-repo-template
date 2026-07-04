# Codex Overlay Reference

This overlay keeps reusable Codex workflow guidance in files that can be copied
into an existing project without imposing runtime code, dependencies, tests, or
CI.

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

## Local Mapping

- Durable repository guidance lives in `AGENTS.md`.
- Project-scoped Codex defaults live in `.codex/config.toml`.
- Reusable overlay maintenance guidance lives in
  `.agents/skills/codex-overlay-maintenance/SKILL.md`.
- Optional project-type skill templates live in `.agents/skill-templates/` and
  become active only after a host project copies them into `.agents/skills/`.
- Larger tasks can use `docs/exec-plans/templates/overlay-plan.md`.
- Optional preflight examples live in `scripts/preflight.example.py`.

## Optional Templates

- Python projects that intentionally standardize on `uv`, `stdlogkit`, and TOML
  configuration can copy
  `.agents/skill-templates/python-uv-project/SKILL.md` into their own
  `.agents/skills/` directory and use
  `docs/references/python-uv-project.md` as supporting guidance.

## Prompt Shape

Good Codex prompts for a host project include:

- Goal: the behavior, bug fix, investigation, or documentation outcome.
- Context: relevant files, errors, model paths, service names, logs, or previous
  attempts.
- Constraints: host package manager, lockfile, test commands, deployment rules,
  performance boundaries, security requirements, and resource limits.
- Preflight: resources that must exist before running commands.
- Done when: exact validation commands and expected output.

## Automation Notes

Use `codex exec` for scripted Codex runs only when the prompt, sandbox, and
approval behavior are explicit. Do not expose API keys or private model access
credentials to repository-controlled commands in the same job.
