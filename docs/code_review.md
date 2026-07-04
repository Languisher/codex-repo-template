# Code Review

Use this checklist when reviewing code changes.

## Correctness

- Does the implementation satisfy the requested behavior?
- Are edge cases, error paths, and compatibility requirements covered?
- Are public APIs, schemas, migrations, auth, or data formats changed
  intentionally?

## Tests

- Are tests updated for behavior changes?
- Does a bug fix include regression coverage when practical?
- Are flaky, slow, or environment-dependent tests documented?

## Maintainability

- Does the change follow existing project patterns?
- Is new abstraction justified by real duplication or complexity?
- Are docs updated for changed commands, configuration, or workflows?

## Security

- No secrets, credentials, private URLs, or sensitive local paths are committed.
- Logs avoid sensitive payloads and secret values.
- Auth, authorization, billing, and data-deletion behavior receive extra review.
