# Codex Workflow Reference

This reference explains how the repository template maps Codex context into
maintainable files.

## Context Layers

- Durable instructions: `AGENTS.md`.
- Conditional workflows: `.agents/skills/*/SKILL.md`.
- Executable feedback: `scripts/`, `tests/`, and optional `evals/`.

## Prompt Shape

Good project prompts usually include:

- goal: the requested behavior, fix, artifact, or investigation;
- context: relevant files, errors, logs, prior attempts, and constraints;
- validation: commands that should pass before completion;
- done condition: exact expected result.

## Verification

Use these commands after filling project-specific content:

```bash
codex --ask-for-approval never "Summarize the current instructions."
codex --cd . --ask-for-approval never "Show which instruction files are active."
```

If instructions are not loaded, check the current directory, empty files,
`AGENTS.override.md`, `project_doc_max_bytes`, and `CODEX_HOME`.
