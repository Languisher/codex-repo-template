# Architecture

Fill this document with the host project's actual architecture. Keep it short
enough for Codex and maintainers to use during everyday changes.

## System Summary

- Product purpose: `<one sentence>`
- Primary runtime: `<language/framework>`
- Package manager: `<tool>`
- Main entrypoints: `<commands or files>`

## Module Boundaries

- Domain logic: `<path>`
- Application services: `<path>`
- API/UI layer: `<path>`
- I/O adapters: `<path>`
- Shared utilities: `<path>`

## Dependency Rules

- `<layer>` may depend on `<layer>`.
- `<layer>` must not depend on `<layer>`.
- Public interfaces are defined in `<path>`.
- Schema or wire-format changes require `<migration/review process>`.

## High-Risk Areas

- `<auth/billing/data/model/deployment area>`
- Required regression tests: `<test path or command>`
