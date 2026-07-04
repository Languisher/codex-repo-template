---
name: language-neutral-project
description: Template for adding host-specific Codex guidance to a project after its runtime, package manager, and verification commands are known.
---

# Language-Neutral Project Skill

Copy this template into `.agents/skills/` and rename it when a host project
needs a project-specific workflow.

## Fill In

- Runtime and package manager:
- Setup command:
- Development command:
- Lint command:
- Typecheck command:
- Test command:
- Final verification command:
- Architecture docs:
- High-risk areas:

## Workflow

1. Read `AGENTS.md` and relevant host docs.
2. Inspect existing code and tests before editing.
3. Follow host commands exactly as documented.
4. Update tests and docs for behavior changes.
5. Run narrow validation first, then final verification.
