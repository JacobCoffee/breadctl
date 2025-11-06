"""Tests for cyclopts lazy imports CLI."""

import subprocess


def test_help_command() -> None:
    """Test --help works."""
    result = subprocess.run(
        ["uv", "run", "breadctl-cyclopts-lazy", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "breadctl-lazy" in result.stdout


def test_bake_command() -> None:
    """Test bake command works with lazy import."""
    result = subprocess.run(
        ["uv", "run", "breadctl-cyclopts-lazy", "bake"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0


def test_deliver_command() -> None:
    """Test deliver command works with lazy import."""
    result = subprocess.run(
        ["uv", "run", "breadctl-cyclopts-lazy", "deliver"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0


def test_inventory_command() -> None:
    """Test inventory command works with lazy import."""
    result = subprocess.run(
        ["uv", "run", "breadctl-cyclopts-lazy", "inventory"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
