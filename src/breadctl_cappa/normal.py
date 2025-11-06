"""Normal (non-lazy) CLI entry point - imports all modules at startup."""

from dataclasses import dataclass

import cappa

from breadctl import bake, deliver, inventory


@cappa.command(name="bake", invoke=bake.run)
@dataclass
class BakeCommand:
    """🥖 Bake fresh loaves with heavy stdlib imports."""


@cappa.command(name="deliver", invoke=deliver.run)
@dataclass
class DeliverCommand:
    """🚚 Deliver bread to customers using httpx."""


@cappa.command(name="inventory", invoke=inventory.run)
@dataclass
class InventoryCommand:
    """📦 Show current inventory using sqlite3."""


@dataclass
class Breadctl:
    """
    🍞 breadctl - Manage bread operations.

    This is the NORMAL version that imports all modules at startup.
    """

    command: cappa.Subcommands[BakeCommand | DeliverCommand | InventoryCommand]


def cli() -> None:
    """Entry point for the normal CLI."""
    cappa.invoke(Breadctl)


if __name__ == "__main__":
    cli()
