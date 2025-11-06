"""Tests for cyclopts normal (non-lazy) CLI."""

import subprocess


def test_help_command() -> None:
    """Test --help works."""
    result = subprocess.run(
        ["uv", "run", "breadctl-cyclopts", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "breadctl" in result.stdout


def test_bake_command() -> None:
    """Test bake command works."""
    result = subprocess.run(
        ["uv", "run", "breadctl-cyclopts", "bake"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0


def test_deliver_command() -> None:
    """Test deliver command works."""
    result = subprocess.run(
        ["uv", "run", "breadctl-cyclopts", "deliver"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0


def test_inventory_command() -> None:
    """Test inventory command works."""
    result = subprocess.run(
        ["uv", "run", "breadctl-cyclopts", "inventory"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
