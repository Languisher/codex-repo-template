# Testing

Fill this document with the project's test strategy and naming conventions.

## Test Layers

- Unit tests: `<path and command>`
- Integration tests: `<path and command>`
- End-to-end tests: `<path and command>`
- Evaluations: `<path and command, if applicable>`

## Naming

- Test files: `<pattern>`
- Test cases: `<pattern>`
- Fixtures: `<path>`

## Rules

- Behavior changes should include tests.
- Bug fixes should include regression coverage when practical.
- Prefer narrow affected tests during iteration.
- Run `./scripts/verify.sh` before final handoff when configured.

## Commands

```bash
./scripts/test.sh
./scripts/test_affected.sh
./scripts/verify.sh
```
