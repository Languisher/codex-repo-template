# AGENTS.md

## Project Summary

This is a Python project managed with `uv`. All runtime, development, test, and
tooling commands must go through `uv`.

Required standards:

- Environment and dependency management: `uv`.
- Logging: `stdlogkit` only.
- Tests: `pytest`, unless this project documents a different runner.
- Formatting/linting: `ruff`, unless this project documents a different tool.
- Type checking: `mypy` or `pyright`, according to project configuration.

## Repository Map

- `src/`: production Python package code.
- `tests/`: unit and integration tests.
- `docs/architecture.md`: architecture and module boundaries.
- `docs/development.md`: setup and local development workflow.
- `docs/testing.md`: test strategy and naming rules.
- `scripts/`: canonical project commands.
- `.agents/skills/`: Codex workflows for recurring tasks.

## Non-Negotiable Rules

- Use `uv` for all Python environment, dependency, script, and tool execution.
- Do not use `pip`, `pipenv`, `poetry`, `conda`, or raw global Python commands
  unless the user explicitly asks for an exception.
- Do not add dependencies by editing dependency files manually when `uv add` or
  `uv remove` can make the change.
- All application logging must use `stdlogkit`.
- Do not use `print()` for application logs.
- Do not use Python's `logging` module directly in production code.
- Do not introduce alternate logging libraries such as `loguru`, `structlog`,
  or custom logger wrappers unless the user explicitly approves a migration.
- Do not commit secrets, credentials, private keys, local `.env` files, or
  machine-specific paths.
- Preserve public APIs, schemas, migrations, auth, and data formats unless the
  task explicitly asks for changes.

## uv Rules

Use these command forms by default:

```bash
uv sync
uv run python -m pytest
uv run ruff check .
uv run ruff format .
uv run mypy .
uv add <package>
uv add --dev <package>
uv remove <package>
```

Project scripts should also call `uv run`, for example:

```bash
uv run python -m pytest "$@"
```

When changing dependencies:

1. prefer existing dependencies and the standard library first;
2. use `uv add` or `uv remove`;
3. commit both `pyproject.toml` and `uv.lock` changes when present;
4. explain whether the dependency is runtime, development, optional, or test
   only.

## stdlogkit Logging Rules

All production logging must be implemented through `stdlogkit`.

Required behavior:

- Create loggers through the project's established `stdlogkit` helper or
  directly through `stdlogkit` if no helper exists.
- Use structured fields for operational context instead of interpolated message
  strings where `stdlogkit` supports it.
- Never log secrets, tokens, passwords, private URLs, full request bodies,
  credentials, private prompts, or sensitive model outputs.
- Keep logs actionable: include stable identifiers, state transitions, failure
  causes, and retry context when useful.
- Tests may assert log behavior through `stdlogkit` test utilities or project
  fixtures when available.

Before adding logging, inspect existing `stdlogkit` usage in the repository and
match that pattern.

## Standard Commands

Setup:

```bash
uv sync
```

Run app:

```bash
uv run <app-command>
```

Lint:

```bash
uv run ruff check .
```

Format:

```bash
uv run ruff format .
```

Type check:

```bash
uv run mypy .
```

Test:

```bash
uv run python -m pytest
```

Final verification:

```bash
./scripts/verify.sh
```

If this project documents different concrete commands in scripts or docs, use
the project commands, but keep the `uv` requirement.

## Architecture Rules

- Read `docs/architecture.md` before changing module boundaries.
- Keep domain logic separate from I/O adapters and framework handlers.
- API, CLI, worker, and UI entrypoints may call application services; domain
  modules should not import framework-specific modules.
- Prefer typed dataclasses, Pydantic models, or explicit protocols according to
  existing project conventions.
- Do not introduce global mutable state unless it is already the documented
  project pattern.

## Testing Rules

- Any behavior change must add or update tests.
- Bug fixes should include a regression test that fails before the fix.
- Use `uv run python -m pytest <path>` for narrow tests.
- Run `./scripts/verify.sh` before final response when configured.
- If validation cannot run, report the exact command and reason.

## Codex Skill Routing

Use these skills when the task matches:

- `$python-uv-project`: for Python implementation, dependency, tooling, and
  logging work.
- `$repo-plan`: before multi-file, ambiguous, risky, or architecture-sensitive
  work.
- `$repo-feature`: when adding or changing product behavior.
- `$repo-debug`: when reproducing and fixing bugs or failing tests.
- `$repo-review`: when reviewing diffs or pull requests.
- `$repo-release`: when preparing release notes or version bumps.

## Done Means

A task is done only when:

- code follows existing Python project patterns;
- all logging uses `stdlogkit`;
- all Python commands use `uv`;
- dependencies are updated through `uv` when changed;
- relevant tests/docs are updated;
- validation passes, or failures are documented with exact causes.
