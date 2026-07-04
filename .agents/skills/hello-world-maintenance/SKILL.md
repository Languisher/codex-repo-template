---
name: hello-world-maintenance
description: Maintain this Codex-ready Python hello-world template; use when changing CLI behavior, TOML config, tests, docs, or repository Codex workflow files.
---

# Hello World Maintenance

Follow this workflow when maintaining the template:

1. Read `AGENTS.md`, `README.md`, `ARCHITECTURE.md`, and `pyproject.toml`.
2. Inspect the specific files under `src/`, `tests/`, `configs/`, or `docs/`
   that are relevant to the requested change.
3. Keep runtime behavior focused on printing `hello world` unless the user asks
   for a different behavior.
4. Keep configuration TOML-only.
5. Use `uv` for all Python commands.
6. Update tests and documentation when behavior, commands, configuration, or
   public APIs change.
7. Validate with the narrowest useful command first, then run the full standard
   checks before completion when practical:
   - `uv run pytest`
   - `uv run ruff check .`
   - `uv run ruff format --check .`

Do not add runtime dependencies unless the standard library is insufficient and
the dependency is documented in `pyproject.toml`, `README.md`, and the final
work summary.
