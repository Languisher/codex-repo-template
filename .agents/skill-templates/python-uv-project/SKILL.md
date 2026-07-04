---
name: python-uv-project
description: Work on Python projects that must use uv for environment and dependency management and stdlogkit for all production logging.
---

# Python uv Project

Use this skill for Python implementation, tests, dependency changes, tooling,
logging, packaging, debugging, and review work in projects standardized on
`uv` and `stdlogkit`.

## Hard Requirements

- Use `uv` for all Python commands.
- Use `uv sync` for environment setup.
- Use `uv run ...` for Python, tests, scripts, linters, formatters, and type
  checkers.
- Use `uv add`, `uv add --dev`, and `uv remove` for dependency changes.
- All production logging must use `stdlogkit`.
- Do not use `print()` for application logging.
- Do not call Python's `logging` module directly in production code.
- Do not introduce `loguru`, `structlog`, custom logger wrappers, or another
  logging framework unless the user explicitly approves a migration.

## First Checks

Before editing:

1. Read `AGENTS.md`.
2. Inspect `pyproject.toml`, `uv.lock`, and existing scripts.
3. Search for existing `stdlogkit` usage and match the local pattern.
4. Inspect tests and fixtures around the changed behavior.
5. Confirm the narrow validation command to run.

Useful searches:

```bash
rg "stdlogkit|from logging|import logging|print\\(" src tests
rg "tool\\.ruff|tool\\.mypy|tool\\.pytest|dependency-groups" pyproject.toml
```

## Command Defaults

Use project scripts when present. Otherwise default to:

```bash
uv sync
uv run ruff check .
uv run ruff format .
uv run mypy .
uv run python -m pytest
```

For narrow tests:

```bash
uv run python -m pytest tests/path/to/test_file.py::test_name
```

## Logging Workflow

When adding or changing logs:

1. Search for the project's existing `stdlogkit` logger setup.
2. Reuse the same logger creation and configuration pattern.
3. Use structured context fields where supported.
4. Avoid secrets, credentials, private URLs, full payloads, and sensitive model
   data.
5. Add tests for important logging behavior only when logs are part of the
   requested contract or regression.

If no project pattern exists, add the smallest local `stdlogkit` usage that is
consistent with the library and keep it close to the calling module. Do not
invent a broad logging abstraction without at least two real call sites.

## Dependency Workflow

When adding a dependency:

1. Check whether the standard library or current dependencies are sufficient.
2. Choose runtime vs development dependency deliberately.
3. Use `uv add <package>` or `uv add --dev <package>`.
4. Confirm `pyproject.toml` and `uv.lock` are updated.
5. Run affected tests.

## Implementation Workflow

1. Inspect relevant source, tests, types, and configuration.
2. Make the smallest coherent change.
3. Keep functions typed according to existing project style.
4. Preserve public interfaces unless explicitly asked to change them.
5. Add or update tests for behavior changes.
6. Run narrow validation first, then broader verification.

## Review Checklist

- No raw `logging` usage in production code.
- No `print()` application logs.
- No non-`uv` Python commands in scripts/docs introduced by the change.
- Dependency changes were made through `uv`.
- Tests cover changed behavior.
- `uv run` validation commands were actually run or skipped with a stated
  reason.
