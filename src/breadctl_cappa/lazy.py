"""Lazy imports CLI entry point - uses PEP 810 lazy imports."""

from dataclasses import dataclass

import cappa

# PEP 810 lazy imports - modules only loaded when used
lazy import breadctl_cappa.bake as bake
lazy import breadctl_cappa.deliver as deliver
lazy import breadctl_cappa.inventory as inventory


@cappa.command(name="bake", invoke=lambda: bake.run())
@dataclass
class BakeCommand:
    """🥖 Bake fresh loaves with heavy stdlib imports."""


@cappa.command(name="deliver", invoke=lambda: deliver.run())
@dataclass
class DeliverCommand:
    """🚚 Deliver bread to customers using httpx."""


@cappa.command(name="inventory", invoke=lambda: inventory.run())
@dataclass
class InventoryCommand:
    """📦 Show current inventory using sqlite3."""


@dataclass
class BreadctlLazy:
    """🍞 breadctl-lazy - Manage bread operations.

    This is the LAZY version using PEP 810 lazy imports.
    Modules are only loaded when their commands are invoked.
    """

    command: cappa.Subcommands[BakeCommand | DeliverCommand | InventoryCommand]


def cli() -> None:
    """Entry point for the lazy CLI."""
    cappa.invoke(BreadctlLazy)


if __name__ == "__main__":
    cli()