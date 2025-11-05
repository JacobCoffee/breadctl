"""Tests for individual modules."""

from breadctl import bake, deliver, inventory


def test_bake_module_runs() -> None:
    """Test bake module can be imported and run."""
    # Just verify it doesn't crash
    bake.run()


def test_deliver_module_runs() -> None:
    """Test deliver module can be imported and run."""
    deliver.run()


def test_inventory_module_runs() -> None:
    """Test inventory module can be imported and run."""
    inventory.run()
