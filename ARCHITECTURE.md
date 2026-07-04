# Architecture

## Purpose

This repository is a minimal Codex development template. The runtime behavior is
intentionally small: read a TOML config value and print `hello world`.

The surrounding structure exists to make Codex work repeatably: clear
instructions, narrow architecture boundaries, tests, linting, and documented
validation commands.

## Components

- `src/codex_repo_template/cli.py`: command-line interface and stdout behavior.
- `src/codex_repo_template/config.py`: TOML loading and validation.
- `configs/default.toml`: user-editable config example.
- `tests/`: executable behavior and template contract checks.
- `.codex/config.toml`: repo-scoped Codex defaults for trusted workspaces.
- `.agents/skills/hello-world-maintenance/SKILL.md`: repo-local Codex workflow
  for changing and validating this template.

## Runtime Flow

1. `codex-hello` starts in `cli.py`.
2. The CLI resolves the config path.
3. `config.py` parses TOML and validates `[hello].message`.
4. The CLI prints the validated message to stdout.

## Boundaries

- CLI output is intentional user-facing output, so `print()` is acceptable.
- Production logging is not needed for this hello-world application. If logging
  is added later, add and document `stdlogkit`, inspect its interface, and
  update tests and docs.
- Configuration remains TOML-only.
- The standard library is enough for runtime behavior; avoid runtime
  dependencies unless they solve a real requirement.
- The default config path is optimized for a source checkout. If this becomes a
  distributable package, move default config loading to package data or
  `importlib.resources`.

## Extending To Larger Projects

When this template is adapted beyond a hello-world CLI, add project-specific
architecture facts before asking Codex to make broad changes:

- module ownership and public API boundaries;
- data model and migration rules;
- error handling and logging policy;
- external service contracts and retry behavior;
- performance, security, and privacy constraints;
- required runtime resources for preflight checks.

## Change Rules

- Keep the hello-world path easy to inspect.
- Add tests before or with behavior changes.
- Update `README.md`, `AGENTS.md`, and config examples when commands,
  conventions, or configuration behavior changes.
- Do not add services, background jobs, databases, or network calls to this
  template unless explicitly requested.
