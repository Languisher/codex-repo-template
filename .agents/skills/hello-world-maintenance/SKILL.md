---
name: hello-world-maintenance
description: Maintain this Codex-ready Python hello-world template; use when changing CLI behavior, TOML config, tests, docs, or repository Codex workflow files.
---

# Hello World Maintenance

Use this skill to maintain the template's code, tests, documentation, CI, and
Codex workflow files.

## Maintenance Workflow

1. Read `AGENTS.md`, `README.md`, `ARCHITECTURE.md`, and `pyproject.toml`.
2. Inspect the specific files under `src/`, `tests/`, `configs/`, or `docs/`
   that are relevant to the requested change.
3. Before running application code, perform the smallest useful preflight check:
   confirm `uv` is available, dependencies are synced when needed, required
   config files exist, and task-specific external resources are present.
4. Keep runtime behavior focused on printing `hello world` unless the user asks
   for a different behavior.
5. Keep configuration TOML-only.
6. Use `uv` for all Python commands.
7. Update tests and documentation when behavior, commands, configuration, or
   public APIs change.
8. Validate with the narrowest useful command first, then run the full standard
   checks before completion when practical:
   - `uv sync --locked`
   - `uv run pytest`
   - `uv run ruff check .`
   - `uv run ruff format --check .`

Do not add runtime dependencies unless the standard library is insufficient and
the dependency is documented in `pyproject.toml`, `README.md`, and the final
work summary.

## Change Routing

- CLI flags, argument parsing, stdout, and stderr behavior belong in
  `src/codex_repo_template/cli.py`.
- TOML reading, validation, and config defaults belong in
  `src/codex_repo_template/config.py`.
- Module execution behavior belongs in `src/codex_repo_template/__main__.py`.
- User-editable example config belongs in `configs/default.toml`.
- Template contract expectations belong in `tests/test_template_contract.py`.
- Codex workflow rules belong in `AGENTS.md`, `README.md`, `docs/`, and this
  skill.
- CI validation belongs in `.github/workflows/ci.yml`.

## Preflight Checklist

Use only the checks relevant to the task:

- `command -v uv`
- `uv sync --locked`
- confirm `configs/default.toml` exists before running the default CLI path
- confirm task-specific files, configs, or external resources exist before use
- for larger descendants of this template, add checks for model paths, datasets,
  credentials, ports, GPUs, databases, and local caches

Stop and report missing prerequisites before running expensive, stateful, or
destructive commands.

## Validation Matrix

- CLI behavior change: `uv run pytest tests/test_cli.py`
- Config behavior change: `uv run pytest tests/test_config.py`
- Template workflow or required-file change:
  `uv run pytest tests/test_template_contract.py`
- Docs-only workflow change: run the matching contract test when a contract
  exists; otherwise report that no executable validation applies
- Before completion when practical:
  `uv sync --locked`, `uv run pytest`, `uv run ruff check .`,
  `uv run ruff format --check .`

## Common Failure Playbook

- Missing `docs/exec-plans/templates/hello-world-plan.md`: restore the template
  and keep the contract test updated.
- `--config` failures: inspect `build_parser()` and `load_settings()` before
  changing behavior.
- Invalid TOML behavior: update config validation and tests together.
- Module entrypoint failures: inspect `src/codex_repo_template/__main__.py` and
  verify `uv run python -m codex_repo_template`.
- CI drift: keep `.github/workflows/ci.yml`, README validation commands, and
  contract tests aligned.

## Release Checklist

Before tagging or publishing a descendant template:

- run the full validation matrix;
- confirm no secrets or machine-specific paths are present;
- confirm README setup commands still match `pyproject.toml`;
- confirm CI uses locked dependency sync;
- document any remaining risks in the release notes or final summary.
