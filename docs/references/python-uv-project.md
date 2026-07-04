# Python uv Project Reference

This reference supports Python repositories that standardize on `uv` for
environment management and `stdlogkit` for logging.

## Required Project Policy

- `uv` owns Python environment setup, dependency changes, lockfile updates, and
  command execution.
- `stdlogkit` owns all production logging.
- Raw `print()` is not application logging.
- Direct production use of Python's `logging` module is not allowed.
- Alternate logging libraries require explicit approval.

## Recommended Files

```text
repo-root/
  AGENTS.md
  pyproject.toml
  uv.lock
  src/
  tests/
  scripts/
    bootstrap.sh
    lint.sh
    typecheck.sh
    test.sh
    verify.sh
  docs/
    architecture.md
    development.md
    testing.md
  .agents/
    skills/
      python-uv-project/
        SKILL.md
```

## Script Bodies

Use these as starting points after copying the Python template into a project.

`scripts/bootstrap.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
uv sync
```

`scripts/lint.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
uv run ruff check .
```

`scripts/typecheck.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
uv run mypy .
```

`scripts/test.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
uv run python -m pytest "$@"
```

`scripts/verify.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
./scripts/lint.sh
./scripts/typecheck.sh
./scripts/test.sh
```

## pyproject.toml Guidance

Keep tool configuration in `pyproject.toml` unless the project already uses
dedicated config files.

Typical development dependencies:

- `pytest`
- `ruff`
- `mypy` or `pyright`
- `stdlogkit`

Add them with `uv add --dev` or `uv add`, depending on whether they are needed
at runtime.

## Logging Guidance

Before writing logs:

1. Search for existing `stdlogkit` usage.
2. Reuse the same import and logger setup.
3. Prefer structured fields for request ids, job ids, user-safe identifiers,
   model ids, retry counts, and state transitions.
4. Do not log secrets, credentials, tokens, private URLs, full payloads, private
   prompts, or sensitive model outputs.

Do not create a project-wide logging wrapper until there are multiple concrete
call sites that need it.
