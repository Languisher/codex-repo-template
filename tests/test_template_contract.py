from pathlib import Path

REQUIRED_TEMPLATE_FILES = [
    "AGENTS.md",
    "ARCHITECTURE.md",
    "README.md",
    ".codex/config.toml",
    ".agents/skills/hello-world-maintenance/SKILL.md",
    "configs/default.toml",
    "docs/design-docs/core-beliefs.md",
    "docs/design-docs/index.md",
    "docs/exec-plans/README.md",
    "docs/exec-plans/templates/hello-world-plan.md",
    "docs/references/codex-workflow.md",
    "pyproject.toml",
    "src/codex_repo_template/cli.py",
    "src/codex_repo_template/config.py",
]


def test_codex_template_contract_files_exist():
    repo_root = Path(__file__).resolve().parents[1]

    missing_files = [
        relative_path
        for relative_path in REQUIRED_TEMPLATE_FILES
        if not (repo_root / relative_path).is_file()
    ]

    assert missing_files == []
