"""Tests for normal (non-lazy) CLI."""

from click.testing import CliRunner

from breadctl.normal import cli


def test_help_command() -> None:
    """Test --help displays correctly."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "breadctl" in result.output
    assert "Manage bread operations" in result.output


def test_bake_command() -> None:
    """Test bake command runs successfully."""
    runner = CliRunner()
    result = runner.invoke(cli, ["bake"])
    assert result.exit_code == 0
    assert "Baked" in result.output
    assert "loaves" in result.output


def test_deliver_command() -> None:
    """Test deliver command runs successfully."""
    runner = CliRunner()
    result = runner.invoke(cli, ["deliver"])
    assert result.exit_code == 0
    assert "Delivery status" in result.output


def test_inventory_command() -> None:
    """Test inventory command runs successfully."""
    runner = CliRunner()
    result = runner.invoke(cli, ["inventory"])
    assert result.exit_code == 0
    assert "inventory" in result.output
