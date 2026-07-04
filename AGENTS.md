# AGENTS.md

## Overlay Purpose

This repository is a Codex Overlay Template for embedding Codex operating
guidance into an existing host project.

It is not a Python package, application scaffold, dependency template, test
suite, or CI template. The host project owns its runtime code, package manager,
lockfiles, virtual environments, tests, CI, deployment, model files, datasets,
and service configuration.

## Overlay Map

- `AGENTS.md`: durable Codex guidance for the host project.
- `.codex/config.toml`: project-scoped Codex defaults, active after the host
  project is trusted.
- `.agents/skills/codex-overlay-maintenance/SKILL.md`: maintenance workflow for
  this overlay.
- `.agents/skill-templates/`: optional project-type skill templates that can be
  copied into a host project's `.agents/skills/` directory.
- `docs/exec-plans/`: execution-plan conventions and reusable templates.
- `docs/references/`: stable references for Codex workflows and sources.
- `scripts/preflight.example.py`: optional starting point for host-owned
  preflight checks.

Do not add overlay-owned `pyproject.toml`, `uv.lock`, `.python-version`,
virtual environments, application source code, tests, app configs, model
configs, or host CI files.

Project-type templates under `.agents/skill-templates/` are opt-in examples.
They may describe concrete conventions such as a package manager, logging
library, or config format, but those conventions apply only after a host project
copies and enables the template as its own skill.

If `docs/exec-plans/active/` contains task files, inspect them before
continuing partially completed work.

## Host Project First

Before changing a host project, discover and follow its existing conventions:

1. inspect its repository guidance files, docs, package metadata, lockfiles,
   scripts, CI, and test configuration;
2. identify the package manager, environment setup command, test runner,
   formatter, linter, and build system from host files;
3. inspect the relevant source definitions, schemas, parsers, and existing
   usage before changing interfaces;
4. use host commands exactly as documented instead of substituting overlay
   preferences.

If the host project provides more specific instructions in a nested
`AGENTS.md`, follow the more specific instructions for files under that scope.

## Preflight

Before running application, training, inference, service, migration, or other
expensive commands, perform a command-specific preflight check:

1. confirm required host tools and dependencies are available;
2. confirm required config files and local paths exist;
3. confirm required external resources are available before use;
4. confirm secrets or credentials are present without printing their values;
5. confirm ports, GPUs, databases, caches, queues, or services needed by the
   command are ready;
6. stop and report missing prerequisites before running expensive, stateful, or
   destructive commands.

For model-serving or vLLM-style projects, preflight should usually check model
paths, tokenizer/config/weight files, GPU/CUDA visibility, dataset paths, cache
directories, service ports, and host dependency state.

Use `scripts/preflight.example.py` only as a starting point. The host project
should copy, adapt, or replace it with checks that match its own runtime.

## Codex Workflow

For each non-trivial task:

1. read the relevant host-project files before editing;
2. perform the preflight checks needed before running host commands;
3. restate the goal, constraints, and done condition when the task is broad;
4. make the smallest change that satisfies the request;
5. update host tests or docs when behavior, commands, configuration, or public
   APIs change;
6. run the narrowest useful host validation first;
7. summarize changed files, validation, and remaining risks.

Use `docs/exec-plans/templates/overlay-plan.md` for broad, risky, or multi-step
tasks that need an explicit plan.

## No Guessing Policy

Do not guess interfaces.

Before using or modifying a function, class, CLI flag, config key, module path,
schema, model artifact, service endpoint, or external library API:

1. search for existing usage in the host repository;
2. inspect the definition, parser, schema, or configuration;
3. inspect relevant host docs or references;
4. only then make the change.

If the interface cannot be confirmed, report the uncertainty instead of
inventing behavior.

## Coding Rules

Prefer small, focused changes.

Reuse existing host interfaces before creating new ones.

Preserve host architecture boundaries. If the boundaries are unclear, inspect
docs and existing module organization before editing. Do not invent new layers,
services, dependency managers, configuration formats, or CI workflows unless the
user explicitly asks for them.

When fixing a bug, first identify the failing path or broken invariant, then
make the smallest change that addresses it.

When changing behavior, update or add host-project tests when practical.

## Validation

Use the host project's validation commands. Do not assume a specific language,
package manager, test runner, linter, formatter, or CI provider.

Run the narrowest relevant validation first, then broader host validation when
practical.

Do not claim validation was performed unless the command was actually run.

If validation fails, report the exact command, failure summary, likely cause,
and next minimal fix.

## Dependencies

Do not add dependencies casually.

Before adding a dependency, check whether the host standard library, existing
dependencies, or existing project utilities are sufficient.

If a dependency is necessary, explain why it is needed, whether it is runtime,
development, optional, model-serving, or infrastructure-only, and update the
host dependency files and docs together.

## Documentation

Update host documentation when behavior, commands, configuration, deployment,
model resources, or public APIs change.

Documentation should be concise and operational.

Avoid documenting unstable implementation details unless they are necessary for
maintenance.

## Security and Privacy

Never commit secrets, tokens, passwords, private keys, private model access
URLs, machine-specific credentials, or sensitive local paths.

Do not log secrets or full private payloads.

Redact sensitive environment variables, URLs, credentials, prompts, datasets,
and model outputs in logs and reports.

## Completion Criteria

A task is complete only when:

1. relevant host files were inspected;
2. the change is minimal and consistent with host architecture;
3. required preflight checks were run or skipped with a stated reason;
4. appropriate host validation was run, or the reason for not running it is
   stated;
5. the final response summarizes what changed, which files were touched, what
   validation ran, and any remaining risks.
