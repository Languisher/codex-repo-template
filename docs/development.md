# Development

Fill this document with local setup and development workflow details.

## Prerequisites

- Runtime: `<version>`
- Package manager: `<tool/version>`
- External services: `<database/cache/queue/model/service>`
- Required environment variables: `<names only, no values>`

## Setup

```bash
./scripts/bootstrap.sh
```

## Run

```bash
./scripts/dev.sh
```

## Common Commands

```bash
./scripts/lint.sh
./scripts/typecheck.sh
./scripts/test.sh
./scripts/verify.sh
```

## Troubleshooting

- If dependencies are missing, rerun setup and inspect lockfiles.
- If ports are occupied, stop the conflicting local service or configure a
  documented alternate port.
- If credentials are missing, create a local env file from the documented
  example without committing secrets.
