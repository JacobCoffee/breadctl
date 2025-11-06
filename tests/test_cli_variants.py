"""Parametrized tests for all CLI variants."""

import subprocess

import pytest


CLI_VARIANTS = [
    "breadctl",
    "breadctl-lazy",
    "breadctl-click",
    "breadctl-click-lazy",
    "breadctl-cyclopts",
    "breadctl-cyclopts-lazy",
]
COMMANDS = ["bake", "deliver", "inventory"]


@pytest.mark.parametrize("variant", CLI_VARIANTS)
def test_help_command(variant: str) -> None:
    """Test --help works for all variants."""
    result = subprocess.run(
        ["uv", "run", variant, "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "breadctl" in result.stdout.lower()


@pytest.mark.parametrize("variant", CLI_VARIANTS)
@pytest.mark.parametrize("command", COMMANDS)
def test_command_execution(variant: str, command: str) -> None:
    """Test all commands execute successfully for all variants."""
    result = subprocess.run(
        ["uv", "run", variant, command],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
