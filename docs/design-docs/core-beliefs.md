# Core Beliefs

## Small Runtime, Strong Workflow

The application should stay intentionally small. The template is valuable
because the Codex development workflow around the application is explicit,
repeatable, and validated.

## Context Before Change

Codex should inspect the relevant files before editing. For this repository,
that usually means `AGENTS.md`, `README.md`, `ARCHITECTURE.md`,
`pyproject.toml`, the target files under `src/`, and the related tests.

## TOML Is The Configuration Boundary

Application configuration lives in TOML. Add new keys only after inspecting
`configs/default.toml` and `src/codex_repo_template/config.py`.

## Validation Is Part Of The Work

A change is not complete until the relevant validation command has run, or the
reason it could not run is documented.

## Preflight Before Execution

Codex should verify the minimal prerequisites before running application code.
For this template, that means `uv`, synced dependencies when needed, and
`configs/default.toml`. Larger projects should add concrete checks for external
resources such as model paths, datasets, credentials, ports, GPUs, databases,
or caches.

## CLI Output Is Intentional

The hello-world behavior is user-facing CLI output, so `print()` is acceptable
in `cli.py`. Future production logs should use `stdlogkit` only after the
dependency has been added, documented, and inspected.
