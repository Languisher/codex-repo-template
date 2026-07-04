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

## Steps

1. Inspect the relevant files.
2. Make the smallest implementation change.
3. Update tests.
4. Update docs if behavior, commands, configuration, or public APIs changed.
5. Run validation.
6. Summarize changes and risks.

## Validation

```bash
uv sync --locked
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## Done When

- The requested behavior is implemented.
- Relevant tests pass.
- Lint and format checks pass or failures are documented.
- The final response lists changed files, validation, and remaining risks.
