from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from codex_repo_template.config import DEFAULT_CONFIG_PATH, ConfigError, load_settings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codex-hello",
        description="Print the configured hello-world message.",
    )
    parser.add_argument(
        "--config",
        default=DEFAULT_CONFIG_PATH,
        type=Path,
        help="Path to a TOML config file.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        settings = load_settings(args.config)
    except ConfigError as exc:
        parser.error(str(exc))

    print(settings.message)
    return 0
