#!/usr/bin/env python3
"""Example preflight checks for projects embedding the Codex overlay.

Copy this file into the host project's own scripts area, then replace the
placeholder checks with project-specific requirements. Keep secret values out of
stdout and logs.
"""

from __future__ import annotations

import os
import socket
import sys
from pathlib import Path


def check_path(label: str, value: str | None, *, must_be_dir: bool = False) -> str | None:
    if not value:
        return f"{label} is not set"

    path = Path(value).expanduser()
    if not path.exists():
        return f"{label} does not exist: {path}"
    if must_be_dir and not path.is_dir():
        return f"{label} is not a directory: {path}"
    return None


def check_port_available(label: str, value: str | None) -> str | None:
    if not value:
        return None

    try:
        port = int(value)
    except ValueError:
        return f"{label} must be an integer port"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind(("127.0.0.1", port))
        except OSError:
            return f"{label} is already in use: {port}"
    return None


def main() -> int:
    checks = [
        check_path("MODEL_PATH", os.environ.get("MODEL_PATH"), must_be_dir=True),
        check_path("DATASET_PATH", os.environ.get("DATASET_PATH")),
        check_path("CACHE_DIR", os.environ.get("CACHE_DIR"), must_be_dir=True),
        check_port_available("SERVICE_PORT", os.environ.get("SERVICE_PORT")),
    ]

    failures = [failure for failure in checks if failure]
    if failures:
        print("Preflight failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Preflight passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
