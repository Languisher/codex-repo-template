---
name: repo-debug
description: Reproduce, isolate, and fix bugs, failing tests, runtime errors, or CI failures with regression coverage.
---

# Repository Debugging

Use this skill for bugs, failing tests, runtime errors, flaky behavior, or CI
failures.

## Workflow

1. Capture the symptom, exact command, error, input, and expected behavior.
2. Reproduce the failure locally with the narrowest command possible.
3. Inspect the failing path, recent changes, logs, tests, and relevant
   definitions.
4. Identify the broken invariant or missing case before editing.
5. Add or update a regression test when practical.
6. Make the smallest fix that addresses the root cause.
7. Rerun the failing command, then broader validation if configured.

## Reporting

Final responses for debugging work should include:

- root cause;
- files changed;
- validation commands and results;
- any remaining risk or unverified environment dependency.
