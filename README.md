# Codex Repo Template

A minimal Python project designed for Codex-driven development. The application
does one thing: it prints `hello world`.

The repository includes the durable files Codex needs to work predictably:
project guidance, project-scoped Codex configuration, a repo-local skill,
architecture notes, execution-plan conventions, tests, lint config, and a small
TOML-backed CLI.

## Quickstart

```bash
uv sync
uv run codex-hello
```

Expected output:

```text
hello world
```

You can also run the module directly:

```bash
uv run python -m codex_repo_template
```

## Validation

Run the standard checks before considering a change complete:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

The same validation runs in GitHub Actions on pushes to `main` and on pull
requests.

## Codex Workflow

Use this default loop for any change:

1. Read `AGENTS.md`, `README.md`, `ARCHITECTURE.md`, `pyproject.toml`, and the
   relevant files under `src/`, `tests/`, and `docs/`.
2. Run the preflight checks needed before executing application code: required
   tools, synced dependencies, config files, and any task-specific external
   resources.
3. Confirm the goal, constraints, and done condition.
4. Make one focused change.
5. Update tests and docs when behavior, commands, config, or public APIs change.
6. Run the narrowest relevant validation.
7. Report changed files, validation, and remaining risks.

For this hello-world template, preflight usually means confirming `uv` works and
`configs/default.toml` exists before running the CLI. Larger projects should
extend the same step to check resources such as model paths, datasets, service
credentials, ports, GPUs, databases, or local caches.

For larger changes, create an execution plan from
`docs/exec-plans/templates/hello-world-plan.md` and place the active copy under
`docs/exec-plans/active/`.

## Project Layout

```text
.
├── AGENTS.md
├── ARCHITECTURE.md
├── README.md
├── .agents/skills/hello-world-maintenance/SKILL.md
├── .codex/config.toml
├── configs/default.toml
├── docs/
├── pyproject.toml
├── src/codex_repo_template/
└── tests/
```

## Configuration

The editable example config lives at `configs/default.toml`:

```toml
[hello]
message = "hello world"
```

The CLI defaults to that file and accepts a replacement path:

```bash
uv run codex-hello --config configs/default.toml
```

## Sources

This template follows the public Codex guidance for `AGENTS.md`, project
configuration, skills, non-interactive runs, and validation-focused workflows.
The CI workflow follows the official uv guidance for GitHub Actions. See
`docs/references/codex-workflow.md` for the source links used while building
the template.
