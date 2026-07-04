---
name: python-uv-project
description: Optional template for Python host projects that standardize on uv for dependency management, stdlogkit for application logging, and TOML for runtime configuration.
---

# Python uv Project

Use this skill only after a host project has copied it into
`.agents/skills/` and intentionally adopted these Python conventions. Do not
apply these rules to non-Python projects or Python projects that document a
different package manager, logging library, or configuration format.

## Project Conventions

- Manage Python dependencies and lockfiles with `uv`.
- Use the host project's documented `uv` commands for setup, dependency
  changes, test execution, formatting, linting, and lockfile updates.
- Do not edit generated lockfiles manually.
- Use `stdlogkit` for application logs.
- Do not use `print()` for durable application logging. `print()` is acceptable
  only for short-lived local debugging, tests that assert stdout, or CLI output
  that is intentionally part of the user interface.
- Store runtime configuration in TOML files unless the host project documents a
  narrower convention.
- Before adding or changing a TOML key, inspect the config loader, schema,
  defaults, environment overrides, documentation, and existing references.
- Expose durable project scripts and developer workflows through `Makefile`
  targets. Use `uv` behind those targets instead of asking users to memorize
  long raw commands.

## Discovery

Before editing Python code or configuration:

1. Inspect the nearest `AGENTS.md` files and host documentation.
2. Inspect `pyproject.toml`, `uv.lock`, tool configuration, and documented
   setup commands.
3. Search for existing `stdlogkit` usage before adding or changing logging.
4. Search for TOML config loading, schema definitions, default files, and
   environment override behavior before changing configuration.
5. Inspect `Makefile` targets before adding or changing scripts, commands,
   docs, or validation instructions.
6. Inspect tests that cover the target module, config path, or CLI behavior.

## Dependency Changes

- Prefer the standard library and existing project utilities before adding a
  dependency.
- If a new dependency is necessary, update it through the host project's
  documented `uv` workflow.
- Explain whether the dependency is runtime, development, optional,
  infrastructure-only, or test-only.
- Update docs or examples when the dependency affects setup, runtime behavior,
  deployment, or public APIs.

## Logging Changes

- Reuse the project's existing `stdlogkit` logger creation pattern.
- Use structured fields for values that operators need to filter or aggregate.
- Do not log secrets, private payloads, full prompts, private URLs, tokens, or
  credentials.
- Keep user-facing CLI output separate from application logs when the project
  has both.
- Update tests when logging behavior is part of the documented contract.

## TOML Configuration Changes

- Reuse the existing config loader and schema instead of parsing TOML ad hoc.
- Keep config keys stable and documented when they are user-facing.
- Add defaults deliberately; do not silently change behavior for existing
  deployments.
- Validate type, missing-key, and invalid-value behavior near the loader or
  schema layer.
- Update example TOML files and operational docs when adding user-facing
  configuration.

## Makefile Script Entrypoints

- Route durable project scripts through `Makefile` targets.
- Prefer `make <target>` in documentation, execution plans, validation steps,
  and user-facing instructions when a target exists.
- When adding a durable script, CLI task, service command, migration, local job,
  test shortcut, lint command, format command, typecheck command, or preflight
  command, add or update the corresponding `Makefile` target.
- Keep targets thin. They should call the host project's documented `uv`
  commands or existing scripts, not duplicate application logic.
- Before editing `Makefile`, inspect existing target names, phony declarations,
  variable conventions, help output, and parameter patterns.
- Do not bypass an existing `Makefile` target with raw `uv run`, `python`, or
  shell commands in docs or plans unless the target is missing or unsuitable;
  if it is missing and the command is durable, add the target.
- Keep one-off investigative commands out of `Makefile` unless they become a
  repeated project workflow.

## Preflight

Before running setup, tests, application commands, migrations, jobs, services,
or other expensive commands:

- Confirm `uv` is available.
- Confirm `Makefile` exists before relying on `make` targets.
- Confirm required project files exist, usually `pyproject.toml` and any
  required TOML config files.
- Confirm the environment or virtual environment expected by the host project is
  ready.
- Confirm required credentials are present without printing values.
- Confirm required ports, databases, caches, queues, model paths, datasets, or
  external services are available before commands that need them.
- Stop and report missing prerequisites before running expensive, stateful, or
  destructive commands.

## Validation

- Run the narrowest relevant host validation first.
- Prefer module-level or focused test commands before full-suite checks.
- Use the host project's documented `make` targets for validation when they
  exist; otherwise use the documented `uv` commands exactly.
- Do not claim formatting, linting, tests, or lockfile checks passed unless the
  command actually ran.
- If validation fails, report the command, failure summary, likely cause, and
  next minimal fix.

## Completion

A task using this skill is complete only when:

- relevant Python, config, and documentation files were inspected;
- dependency, logging, and TOML conventions were followed or documented as not
  applicable;
- durable scripts and workflow commands were exposed through `Makefile` targets
  or documented as not applicable;
- required preflight checks were run or skipped with a stated reason;
- relevant validation ran or the reason for not running it is stated;
- the final response lists changed files, validation, and remaining risks.
