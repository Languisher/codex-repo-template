# AGENTS.md

## Project Purpose

This repository is a Codex-ready project template. It organizes project context
into three layers:

1. durable instructions in `AGENTS.md`;
2. task-specific workflows in `.agents/skills/`;
3. executable feedback in `scripts/`, `tests/`, and optional `evals/`.

After copying this template into a real project, replace placeholders with the
project's actual runtime, commands, architecture, and completion criteria.

## Repository Map

- `AGENTS.md`: repository-level Codex instructions that should always apply.
- `.codex/config.toml`: project-scoped Codex defaults, loaded after trust.
- `.codex/hooks.json`: optional lifecycle hook placeholders.
- `.codex/rules/default.rules`: optional command-safety notes.
- `.agents/skills/`: reusable Codex workflows for recurring tasks.
- `docs/architecture.md`: system boundaries and module ownership.
- `docs/development.md`: setup, run, and local development notes.
- `docs/testing.md`: test strategy, naming, fixtures, and verification rules.
- `docs/code_review.md`: code-review criteria and release-risk checks.
- `docs/decisions/`: architecture decision records.
- `docs/workflows/`: longer workflow references.
- `scripts/`: canonical project commands used by Codex and humans.
- `tests/`: project tests, once the host project adds implementation code.
- `evals/`: optional behavioral evaluations for complex product or model work.

## Non-Negotiable Rules

- Do not commit secrets, tokens, passwords, credentials, private keys, private
  model URLs, or generated local environment files.
- Do not introduce new production dependencies without explicit approval.
- Do not change public APIs, database schemas, wire formats, migrations, auth,
  authorization, billing, or irreversible data behavior unless the task
  explicitly asks for it.
- Prefer modifying existing modules over creating parallel implementations.
- Preserve backward compatibility unless the task includes a migration plan.
- Use structured parsers and project-native APIs instead of fragile string
  manipulation where practical.

## Standard Commands

Fill these scripts with the real project commands before relying on them:

- Setup: `./scripts/bootstrap.sh`
- Run app: `./scripts/dev.sh`
- Lint: `./scripts/lint.sh`
- Type check: `./scripts/typecheck.sh`
- Test: `./scripts/test.sh`
- Affected tests: `./scripts/test_affected.sh`
- Final verification: `./scripts/verify.sh`

`./scripts/verify.sh` is the canonical done check. It should run the same
quality gates a pull request must pass.

## Architecture Rules

- Read `docs/architecture.md` before changing module boundaries.
- Keep domain logic, I/O adapters, API/UI layers, and shared utilities in their
  documented locations once the host project defines them.
- Do not create new architectural layers, service boundaries, dependency
  managers, configuration systems, or CI workflows unless requested.
- Shared utilities should have at least two real call sites before extraction,
  unless the existing project convention says otherwise.
- When an interface is unclear, inspect definitions, schemas, parsers, and
  existing usage before editing.

## Testing Rules

- Any behavior change must include or update tests when practical.
- Bug fixes should include a regression test that fails before the fix.
- Prefer narrow affected tests while iterating.
- Run `./scripts/verify.sh` before declaring completion, unless the user
  explicitly asks not to or the project has not configured verification yet.
- If validation cannot run, report the exact command skipped and why.

## Codex Skill Routing

Use these repository skills when the task matches:

- `$repo-plan`: before multi-file, ambiguous, risky, or architecture-sensitive
  work.
- `$repo-feature`: when adding or changing product behavior.
- `$repo-debug`: when reproducing and fixing a bug, failing test, runtime
  error, or CI failure.
- `$repo-review`: when reviewing a diff, PR, branch, or uncommitted changes.
- `$repo-release`: when preparing release notes, changelog entries, or version
  bumps.

At the start of a non-trivial task, identify whether a skill applies. If a
skill applies, read and follow it before editing.

## Work Process

For non-trivial changes:

1. Restate the goal, constraints, and done condition.
2. Inspect relevant files before editing.
3. Make the smallest coherent change.
4. Add or update tests and docs when behavior, commands, configuration, or
   public APIs change.
5. Run the narrowest useful validation first.
6. Run `./scripts/verify.sh` before final response when configured.
7. Review the diff for accidental API changes, dead code, and regressions.

## Done Means

A task is complete only when:

- the requested behavior or artifact is implemented;
- relevant tests or docs are added or updated;
- validation passes, or failures are documented with exact causes;
- touched files are summarized;
- remaining risks are called out plainly.
