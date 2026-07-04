# Python uv Project Reference

This reference supports the optional
`.agents/skill-templates/python-uv-project/SKILL.md` template. It is not a
global overlay requirement.

## Scope

Use these conventions only in host projects that explicitly adopt the
`python-uv-project` skill template.

The template assumes:

- Python dependencies are managed with `uv`.
- Application logging uses `stdlogkit`.
- Runtime configuration is stored in TOML files.
- Durable scripts and developer workflows are exposed through `Makefile`
  targets.

If a host project documents different conventions, follow the host project.

## uv

- Treat `pyproject.toml` and `uv.lock` as host-owned files.
- Use the host project's documented `uv` commands.
- Do not manually edit `uv.lock`.
- Before adding dependencies, check whether the standard library, existing
  dependencies, or local utilities are sufficient.
- When adding dependencies, document their role: runtime, development, optional,
  infrastructure-only, or test-only.

## stdlogkit

- Search for existing logger setup before adding new logging code.
- Reuse project helpers for logger names, context fields, and formatting.
- Prefer structured context over string interpolation for operational values.
- Never log secrets, private model URLs, tokens, credentials, full private
  payloads, private prompts, or sensitive dataset content.
- Keep deliberate CLI stdout separate from application logs.

## TOML Configuration

- Find the config loader before editing config files.
- Inspect schema, defaults, environment overrides, example files, and docs.
- Reuse the existing parser and validation path.
- Add or rename keys only with a clear compatibility plan.
- Update examples and operational docs when user-facing config changes.

## Makefile Entrypoints

The `Makefile` is the human-facing command surface. `uv` remains the dependency
manager and Python execution backend.

Expose repeated project workflows as stable targets, such as:

- `make setup`
- `make test`
- `make lint`
- `make format`
- `make typecheck`
- `make run`
- `make serve`
- `make migrate`
- `make preflight`

Target names should follow the host project's existing naming conventions. Add
new names only when an existing target cannot reasonably cover the workflow.

Targets should be thin wrappers around documented `uv` commands or existing
scripts. Do not put application logic in `Makefile`.

Use raw `uv run`, `python`, or shell commands directly only for one-off
investigation, bootstrapping a missing target, or cases where the host project
explicitly documents that no target should exist.

## Preflight Examples

Useful checks for Python projects that adopt this template include:

- `uv` exists on `PATH`;
- `Makefile` exists before using `make` targets;
- `pyproject.toml` exists;
- required TOML config files exist;
- required environment variables are present without printing values;
- service ports are free before starting local servers;
- databases, caches, queues, datasets, model paths, or external services needed
  by the command are available.

The exact command remains host-owned.
