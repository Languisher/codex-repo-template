---
name: repo-review
description: Review a diff, pull request, branch, or uncommitted changes for bugs, regressions, missing tests, and maintainability risks.
---

# Repository Review

Use this skill when the user asks for a review.

## Review Priority

Prioritize findings in this order:

1. correctness bugs and regressions;
2. security, privacy, auth, data loss, and migration risks;
3. missing tests for changed behavior;
4. compatibility or API contract breaks;
5. maintainability issues that are likely to cause future defects.

## Workflow

1. Inspect the diff and relevant surrounding code.
2. Cross-check tests and docs against changed behavior.
3. Verify risky claims against executable commands when practical.
4. Lead with findings, ordered by severity, with file and line references.
5. If there are no findings, say so and mention residual test gaps.

## Output Shape

Use this order:

1. findings;
2. open questions or assumptions;
3. brief change summary only as supporting context.
