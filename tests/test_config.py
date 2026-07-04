from pathlib import Path

import pytest

from codex_repo_template.config import ConfigError, load_settings


def test_load_settings_reads_message(tmp_path: Path):
    config_path = tmp_path / "settings.toml"
    config_path.write_text('[hello]\nmessage = "hello world"\n', encoding="utf-8")

    settings = load_settings(config_path)

    assert settings.message == "hello world"


def test_load_settings_rejects_missing_hello_table(tmp_path: Path):
    config_path = tmp_path / "settings.toml"
    config_path.write_text('[other]\nmessage = "hello world"\n', encoding="utf-8")

    with pytest.raises(ConfigError, match=r"\[hello\]"):
        load_settings(config_path)


def test_load_settings_rejects_empty_message(tmp_path: Path):
    config_path = tmp_path / "settings.toml"
    config_path.write_text('[hello]\nmessage = ""\n', encoding="utf-8")

    with pytest.raises(ConfigError, match="hello.message"):
        load_settings(config_path)
