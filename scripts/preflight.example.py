#!/usr/bin/env python3
"""Example preflight checks for a host project.

Copy and adapt this file after the project defines real prerequisites. Do not
print secret values.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


def require_command(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"missing required command: {name}")


def require_path(path: str) -> None:
    if not Path(path).exists():
        raise SystemExit(f"missing required path: {path}")


def require_env(name: str) -> None:
    if not os.environ.get(name):
        raise SystemExit(f"missing required environment variable: {name}")


def main() -> int:
    # Examples only. Replace with project-specific checks.
    # require_command("your-package-manager")
    # require_path("config/example.toml")
    # require_env("REQUIRED_SECRET_NAME")
    print("preflight example has no project-specific checks configured")
    return 0


if __name__ == "__main__":
    sys.exit(main())
