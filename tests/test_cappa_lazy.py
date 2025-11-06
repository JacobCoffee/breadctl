"""Tests for cappa lazy imports CLI."""

import cappa
import pytest

from breadctl_cappa.lazy import BreadctlLazy

# Skip all tests in this module until PEP 810 is implemented
pytestmark = pytest.mark.skip(reason="PEP 810 lazy import syntax not yet available in Python")


def test_help_command() -> None:
    """Test --help parsing works."""
    cappa.parse(BreadctlLazy, argv=["--help"], exit_on_error=False)
    # Cappa parsing succeeds, help is handled by invoke


def test_bake_command_parsing() -> None:
    """Test bake command parses successfully with lazy import."""
    result = cappa.parse(BreadctlLazy, argv=["bake"])
    assert result.command.__class__.__name__ == "BakeCommand"


def test_deliver_command_parsing() -> None:
    """Test deliver command parses successfully with lazy import."""
    result = cappa.parse(BreadctlLazy, argv=["deliver"])
    assert result.command.__class__.__name__ == "DeliverCommand"


def test_inventory_command_parsing() -> None:
    """Test inventory command parses successfully with lazy import."""
    result = cappa.parse(BreadctlLazy, argv=["inventory"])
    assert result.command.__class__.__name__ == "InventoryCommand"
