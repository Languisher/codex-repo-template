from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[2] / "configs" / "default.toml"


class ConfigError(ValueError):
    """Raised when the TOML configuration is missing or invalid."""


@dataclass(frozen=True)
class Settings:
    message: str


def load_settings(config_path: Path = DEFAULT_CONFIG_PATH) -> Settings:
    try:
        raw_config = config_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ConfigError(f"Config file not found: {config_path}") from exc

    try:
        data = tomllib.loads(raw_config)
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"Config file is not valid TOML: {config_path}") from exc

    hello_config = data.get("hello")
    if not isinstance(hello_config, dict):
        raise ConfigError(f"{config_path} must define a [hello] table")

    message = hello_config.get("message")
    if not isinstance(message, str) or not message:
        raise ConfigError(f"{config_path} must define a non-empty hello.message")

    return Settings(message=message)
