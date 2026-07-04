---
name: repo-plan
description: Plan broad, ambiguous, risky, multi-file, migration, or architecture-sensitive work before implementation.
---

# Repository Planning

Use this skill before implementation when the task is broad, ambiguous,
multi-step, risky, or likely to change architecture, data, public APIs, auth,
deployment, or user-visible workflows.

## Workflow

1. Read `AGENTS.md` and the relevant docs under `docs/`.
2. Inspect existing code, scripts, tests, configs, schemas, and usage before
   proposing changes.
3. Identify constraints, dependencies, migration needs, compatibility concerns,
   and validation commands.
4. Break the work into small steps with a clear done condition for each step.
5. Call out assumptions and risks before editing.
6. After implementation, update the plan status and run relevant validation.

## Output Shape

For substantial work, maintain a short checklist with:

- goal;
- constraints;
- files or areas to inspect;
- implementation steps;
- validation commands;
- risks or rollback notes.
