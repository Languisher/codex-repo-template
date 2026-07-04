# 0001: Use Three Codex Context Layers

## Status

Accepted

## Context

Codex works best when durable instructions, task-specific procedures, and
executable validation are separated.

## Decision

This template uses:

- `AGENTS.md` for always-loaded repository rules;
- `.agents/skills/` for reusable task workflows;
- `scripts/`, `tests/`, and optional `evals/` for executable feedback.

## Consequences

- Repository instructions stay shorter and easier to maintain.
- Skills can be loaded only when relevant.
- Completion criteria can be verified by commands instead of prose alone.
