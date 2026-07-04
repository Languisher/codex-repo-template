# Execution Plans

Use execution plans for broad, risky, or multi-step Codex tasks in the host
project. Small edits do not need a plan if the goal, files, preflight, and
validation path are obvious.

## Folders

- `active/`: plans for work currently in progress.
- `completed/`: completed plans worth preserving for later reference.
- `templates/`: reusable plan shapes.

## Workflow

1. Copy `templates/overlay-plan.md` into `active/`.
2. Fill in host-specific goal, context, constraints, preflight, validation,
   risks, and done condition.
3. Keep the checklist current while work proceeds.
4. Move the plan to `completed/` when the work is done and the summary is still
   useful.

Plans describe intent; host tests, checks, or manual verification validate
behavior.

## Optional Project-Type Skills

Project-type skill templates can live under `.agents/skill-templates/`. They
are not active by default. Copy a template into a host project's
`.agents/skills/` directory only when the host project intentionally adopts its
conventions.
