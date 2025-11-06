"""Tests for click normal (non-lazy) CLI."""

from click.testing import CliRunner

from breadctl_click.normal import breadctl


def test_help_command() -> None:
    """Test --help works."""
    runner = CliRunner()
    result = runner.invoke(breadctl, ["--help"])
    assert result.exit_code == 0
    assert "breadctl" in result.output


def test_bake_command() -> None:
    """Test bake command works."""
    runner = CliRunner()
    result = runner.invoke(breadctl, ["bake"])
    assert result.exit_code == 0


def test_deliver_command() -> None:
    """Test deliver command works."""
    runner = CliRunner()
    result = runner.invoke(breadctl, ["deliver"])
    assert result.exit_code == 0


def test_inventory_command() -> None:
    """Test inventory command works."""
    runner = CliRunner()
    result = runner.invoke(breadctl, ["inventory"])
    assert result.exit_code == 0
