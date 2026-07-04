from codex_repo_template.cli import main


def test_cli_prints_hello_world(capsys):
    exit_code = main([])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "hello world\n"
    assert captured.err == ""
