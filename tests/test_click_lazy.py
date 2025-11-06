"""Tests for click lazy imports CLI."""

from click.testing import CliRunner

from breadctl_click.lazy import breadctl_lazy


def test_help_command() -> None:
    """Test --help works."""
    runner = CliRunner()
    result = runner.invoke(breadctl_lazy, ["--help"])
    assert result.exit_code == 0
    assert "breadctl-lazy" in result.output


def test_bake_command() -> None:
    """Test bake command works with lazy import."""
    runner = CliRunner()
    result = runner.invoke(breadctl_lazy, ["bake"])
    assert result.exit_code == 0


def test_deliver_command() -> None:
    """Test deliver command works with lazy import."""
    runner = CliRunner()
    result = runner.invoke(breadctl_lazy, ["deliver"])
    assert result.exit_code == 0


def test_inventory_command() -> None:
    """Test inventory command works with lazy import."""
    runner = CliRunner()
    result = runner.invoke(breadctl_lazy, ["inventory"])
    assert result.exit_code == 0
