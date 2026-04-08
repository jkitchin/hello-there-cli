"""Tests for the hello-there CLI."""

import subprocess
import sys

from hello_there.cli import main


def test_default_greeting(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["hello-there"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello there, World"


def test_named_greeting(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["hello-there", "--name", "Alice"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello there, Alice"


def test_cli_entry_point():
    result = subprocess.run(
        [sys.executable, "-m", "hello_there.cli"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "hello there, World" in result.stdout


def test_cli_entry_point_with_name():
    result = subprocess.run(
        [sys.executable, "-m", "hello_there.cli", "--name", "Bob"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "hello there, Bob" in result.stdout
