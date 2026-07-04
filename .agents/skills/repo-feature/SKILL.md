---
name: repo-feature
description: Add or modify product behavior with focused implementation, tests, docs, and verification.
---

# Repository Feature Work

Use this skill when adding, removing, or changing product behavior.

## Workflow

1. Read `AGENTS.md`, `docs/architecture.md`, and `docs/testing.md`.
2. Inspect current behavior, call sites, tests, fixtures, and relevant docs.
3. Define the smallest behavior change that satisfies the request.
4. Implement using existing project patterns.
5. Add or update tests for new behavior and important edge cases.
6. Update docs when commands, configuration, APIs, or workflows change.
7. Run narrow affected tests, then `./scripts/verify.sh` when configured.

## Guardrails

- Do not introduce dependencies unless approved.
- Do not change public contracts accidentally.
- Preserve existing behavior unless the task explicitly asks for a change.
- Prefer explicit errors and typed/structured data over implicit behavior.
