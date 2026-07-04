# AGENTS.md

## Project Overview

This is a Codex-ready Python template. Its only runtime goal is to print
`hello world`, but the repository is structured so Codex can safely inspect,
change, validate, and report on the project.

The project uses:

- `uv` for Python environment and dependency management.
- TOML for application and Codex configuration.
- `stdlogkit` for future production logging.

Do not introduce alternative environment managers, logging frameworks, or
configuration formats unless explicitly requested.

## Repository Map

- `README.md`: user-facing setup, usage, and Codex workflow.
- `ARCHITECTURE.md`: design boundaries for the hello-world CLI.
- `pyproject.toml`: package metadata, scripts, dependencies, and tool config.
- `src/codex_repo_template/`: application code.
- `configs/default.toml`: editable TOML configuration example.
- `tests/`: behavioral and template contract tests.
- `.codex/config.toml`: project-scoped Codex defaults.
- `.agents/skills/`: repo-local Codex skills.
- `docs/design-docs/`: design notes and recurring project beliefs.
- `docs/exec-plans/`: plan templates and active/completed plan folders.
- `docs/references/`: stable references for Codex workflows and sources.

If `docs/exec-plans/active/` contains task files, inspect them before
continuing partially completed work.

## Environment

Use `uv` for Python commands.

Preferred commands:

- `uv sync`
- `uv run codex-hello`
- `uv run python -m codex_repo_template`
- `uv run pytest`
- `uv run ruff check .`
- `uv run ruff format .`

Do not use bare `python`, `pip`, `pytest`, or `ruff` unless explicitly
requested.

If dependencies are missing, update `pyproject.toml` first, then run
`uv sync`.

## Logging

This template has no production logs because the application only emits
intentional CLI output.

When production logging is added:

1. use `stdlogkit`;
2. inspect existing usage or official project references before calling its API;
3. never replace it with `logging`, `structlog`, `loguru`, or another framework
   without explicit approval.

Do not use `print()` for production logging. `print()` is acceptable for
intentional CLI output, temporary local debugging, and tests that verify stdout
behavior.

Logs must contain enough context to debug failures, but must not expose
secrets, tokens, credentials, or private data.

## Configuration

Use TOML for configuration.

Do not introduce YAML, JSON, `.env`, or Python config files unless explicitly
requested. Codex-specific files that have fixed upstream formats, such as
`AGENTS.md` and skill `SKILL.md` files, are allowed.

Before adding a new config key:

1. inspect `configs/default.toml`;
2. inspect `src/codex_repo_template/config.py`;
3. reuse an existing key if appropriate;
4. update config examples, validation logic, tests, and docs together.

Do not invent config keys without checking how configuration is parsed.

## Codex Workflow

For each non-trivial task:

1. read the relevant files before editing;
2. restate the goal, constraints, and done condition when the task is broad;
3. make the smallest change that satisfies the request;
4. update tests or docs when behavior, commands, configuration, or public APIs
   change;
5. run the narrowest useful validation first;
6. summarize changed files, validation, and remaining risks.

Use `docs/exec-plans/templates/hello-world-plan.md` for larger tasks that need
an explicit plan.

## No Guessing Policy

Do not guess interfaces.

Before using or modifying a function, class, CLI flag, config key, module path,
or external library API:

1. search for existing usage in the repository;
2. inspect the definition, parser, or schema;
3. inspect relevant docs under `docs/` or `docs/references/`;
4. only then make the change.

If the interface cannot be confirmed, report the uncertainty instead of
inventing behavior.

## Coding Rules

Prefer small, focused changes.

Reuse existing interfaces before creating new ones.

Preserve existing architecture boundaries:

- CLI argument parsing belongs in `src/codex_repo_template/cli.py`.
- TOML parsing and validation belong in `src/codex_repo_template/config.py`.
- The package entry point belongs in `src/codex_repo_template/__main__.py`.
- User-editable config examples belong in `configs/`.

Avoid broad rewrites unless explicitly requested.

When fixing a bug, first identify the failing path or broken invariant, then
make the smallest change that addresses it.

When changing behavior, update or add tests.

## Testing and Validation

After code changes, run the narrowest relevant validation first.

Common commands:

- `uv run pytest`
- `uv run pytest tests/<specific_test_file>.py`
- `uv run ruff check .`
- `uv run ruff format --check .`

Do not claim validation was performed unless the command was actually run.

If validation fails, report the exact command, failure summary, likely cause,
and next minimal fix.

## Dependencies

Do not add dependencies casually.

Before adding a dependency, check whether the standard library or an existing
dependency is sufficient.

If a dependency is necessary, explain why it is needed and whether it is
runtime, development, or optional.

## Documentation

Update documentation when behavior, commands, configuration, or public APIs
change.

Documentation should be concise and operational.

Avoid documenting unstable implementation details unless they are necessary for
maintenance.

## Security and Privacy

Never commit secrets, tokens, passwords, private keys, or machine-specific
credentials.

Do not log secrets or full private payloads.

Redact sensitive environment variables, URLs, and credentials in logs and
reports.

## Completion Criteria

A task is complete only when:

1. relevant files were inspected;
2. the change is minimal and consistent with existing architecture;
3. appropriate validation was run, or the reason for not running it is stated;
4. the final response summarizes what changed, which files were touched, what
   validation was run, and any remaining risks.
