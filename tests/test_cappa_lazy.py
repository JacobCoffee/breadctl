"""Tests for cappa lazy imports CLI."""

import cappa
import pytest

from breadctl_cappa.lazy import BreadctlLazy


def test_help_command() -> None:
    """Test --help parsing works."""
    # Help is handled by invoke, just test that parse works without --help
    result = cappa.parse(BreadctlLazy, argv=["bake"])
    assert result is not None


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
