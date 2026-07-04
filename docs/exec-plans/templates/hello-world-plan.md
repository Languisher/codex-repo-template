# Hello World Execution Plan

## Goal

State the user-visible outcome in one sentence.

## Context

- Relevant source files:
- Relevant tests:
- Relevant docs:
- External references:

## Constraints

- Keep runtime behavior focused on printing `hello world` unless explicitly
  requested otherwise.
- Use `uv` for Python commands.
- Keep configuration TOML-only.
- Do not add runtime dependencies without documenting why they are necessary.

## Preflight

- Confirm `uv` is available before running Python commands.
- Confirm dependencies are synced when a command depends on the project
  environment.
- Confirm `configs/default.toml` exists before running the default CLI path.
- List any task-specific external resources and verify they exist before use.
- Stop and report missing prerequisites before running expensive, stateful, or
  destructive commands.

For larger projects, extend this section with concrete checks for required
resources such as model paths, datasets, service credentials, ports, GPUs,
databases, or local caches.

## Steps

1. Inspect the relevant files.
2. Run the preflight checks needed for the task.
3. Make the smallest implementation change.
4. Update tests.
5. Update docs if behavior, commands, configuration, or public APIs changed.
6. Run validation.
7. Summarize changes and risks.

## Validation

```bash
uv sync --locked
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## Done When

- The requested behavior is implemented.
- Required preflight checks pass or missing prerequisites are documented.
- Relevant tests pass.
- Lint and format checks pass or failures are documented.
- The final response lists changed files, validation, and remaining risks.
