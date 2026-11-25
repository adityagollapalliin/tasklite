from tasklite.cli import main


def test_add_then_list(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("TASKLITE_FILE", str(tmp_path / "tasks.json"))
    assert main(["add", "Buy milk", "--due", "2026-12-01"]) == 0
    assert main(["list"]) == 0
    out = capsys.readouterr().out
    assert "[ ] 1. Buy milk (due 2026-12-01)" in out
