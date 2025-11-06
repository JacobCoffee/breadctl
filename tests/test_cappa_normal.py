"""Tests for cappa normal (non-lazy) CLI."""

import cappa

from breadctl_cappa.normal import Breadctl


def test_help_command() -> None:
    """Test --help parsing works."""
    import subprocess

    result = subprocess.run(
        ["uv", "run", "breadctl", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "breadctl" in result.stdout


def test_bake_command_parsing() -> None:
    """Test bake command parses successfully."""
    result = cappa.parse(Breadctl, argv=["bake"])
    assert result.command.__class__.__name__ == "BakeCommand"


def test_deliver_command_parsing() -> None:
    """Test deliver command parses successfully."""
    result = cappa.parse(Breadctl, argv=["deliver"])
    assert result.command.__class__.__name__ == "DeliverCommand"


def test_inventory_command_parsing() -> None:
    """Test inventory command parses successfully."""
    result = cappa.parse(Breadctl, argv=["inventory"])
    assert result.command.__class__.__name__ == "InventoryCommand"
