# Overlay Execution Plan

## Goal

State the host-project outcome in one sentence.

## Context

- Host project:
- Relevant source files:
- Relevant tests or checks:
- Relevant docs:
- External references:

## Constraints

- Respect the host project's package manager, lockfiles, test runner, formatter,
  CI, runtime services, and deployment conventions.
- Do not introduce overlay-owned dependencies, virtual environments, app code,
  tests, or CI.
- Confirm host-project interfaces before using or modifying them.
- Keep changes scoped to the requested behavior.

## Preflight

- Identify the host project's required tools and environment setup command.
- Identify the command-specific resources needed before execution.
- Verify required config files, model paths, datasets, credentials, ports, GPUs,
  databases, caches, or services before use.
- Do not print secret values while checking credentials.
- Stop and report missing prerequisites before running expensive, stateful, or
  destructive commands.

## Steps

1. Inspect the relevant host-project files and docs.
2. Run the preflight checks needed for the task.
3. Confirm goal, constraints, and done condition for broad changes.
4. Make the smallest implementation or documentation change.
5. Update host-project tests or docs when behavior, commands, configuration, or
   public APIs change.
6. Run the narrowest relevant host-project validation.
7. Summarize changed files, validation, and remaining risks.

## Validation

- Host setup command:
- Narrow test/check command:
- Full validation command:
- Manual verification, if needed:

## Risks

- Runtime resource risks:
- Compatibility risks:
- Security or privacy risks:
- Rollback considerations:

## Done When

- The requested host-project outcome is implemented.
- Required preflight checks pass or missing prerequisites are documented.
- Relevant host-project validation passes or failures are explained.
- The final response lists changed files, validation, and remaining risks.
