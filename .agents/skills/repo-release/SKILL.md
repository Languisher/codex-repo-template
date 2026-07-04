---
name: repo-release
description: Prepare release notes, changelog entries, version bumps, and release validation for a repository.
---

# Repository Release

Use this skill for release notes, changelogs, version bumps, tagging prep, or
release validation.

## Workflow

1. Read `AGENTS.md`, release docs, changelog, package metadata, and CI status
   files when present.
2. Identify included commits or changes since the last release point.
3. Group changes by user impact: added, changed, fixed, deprecated, removed,
   security, migration.
4. Confirm versioning rules before editing version files.
5. Run release validation commands documented by the project.
6. Call out breaking changes, migrations, rollback notes, and known issues.

## Release Notes Template

Use `docs/workflows/release.md` as the local release checklist and adapt output
to the project's changelog style.
