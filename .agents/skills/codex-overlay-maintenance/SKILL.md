---
name: codex-overlay-maintenance
description: Maintain this Codex overlay template for embedding Codex guidance, skills, execution plans, references, and optional preflight checks into an existing host project.
---

# Codex Overlay Maintenance

Use this skill when changing the overlay files that are meant to be copied into
an existing project. The overlay must not impose a Python package, dependency
manager, lockfile, virtual environment, application code, tests, or CI on the
host project.

## Overlay Scope

The overlay owns only these paths:

- `AGENTS.md`
- `.codex/config.toml`
- `.agents/skills/codex-overlay-maintenance/SKILL.md`
- `docs/exec-plans/`
- `docs/references/`
- `scripts/preflight.example.py`

Do not add host-project files such as `pyproject.toml`, `uv.lock`,
`.python-version`, `.github/workflows/`, `src/`, `tests/`, app configs, model
configs, or generated environments.

## Maintenance Workflow

1. Inspect `AGENTS.md`, this skill, and the relevant files under `docs/` or
   `scripts/`.
2. Keep instructions host-neutral. Say "use the host project's command" instead
   of naming `uv`, `pip`, `pytest`, `ruff`, CUDA, vLLM, or any other tool unless
   it is clearly presented as an example.
3. Preserve the distinction between reusable Codex operating rules and
   project-specific facts that must be filled in after the overlay is embedded.
4. Update execution-plan templates when workflow expectations change.
5. Update references when public-source assumptions or links change.
6. Validate with structural checks that do not require a host project.

## Preflight Guidance

The overlay provides `scripts/preflight.example.py` as a starting point only.
Host projects should copy or replace it, then add concrete checks for their own
runtime resources.

For vLLM-style projects, useful host-specific checks usually include:

- model path exists and contains expected config/tokenizer/weight files;
- GPU/CUDA visibility matches the task;
- required environment variables are present without printing secret values;
- dataset and cache paths exist and have the needed permissions;
- service ports are available before starting servers;
- host dependency and lockfile commands pass.

## Validation Matrix

- Overlay structure change: verify only allowed overlay paths are present.
- `AGENTS.md` change: check that host-neutral language is preserved.
- Execution-plan change: check that goal, context, constraints, preflight,
  steps, validation, risks, and done condition are present.
- Preflight example change: run a syntax check with the host's available Python
  only if Python is available; otherwise inspect the script manually and report
  that syntax validation was skipped.

## Common Failure Playbook

- Host-specific command leaked into overlay: rewrite it as a placeholder or
  example and tell the host project to fill in the real command.
- Runtime files added accidentally: remove them from the overlay and document
  that the host owns runtime code, dependencies, tests, and CI.
- Preflight became too generic to help: add examples of resource categories,
  but leave concrete paths and commands to the host project.
- Execution plan became a checklist without validation: add explicit validation
  commands or "to be filled by host project" placeholders.
