"""Normal (non-lazy) CLI entry point - imports all modules at startup."""

import rich_click as click

from breadctl import bake, deliver, inventory


@click.group()
def breadctl():
    """🍞 breadctl - Manage bread operations.

    This is the NORMAL version that imports all modules at startup.
    """


@breadctl.command(name="bake")
def bake_cmd():
    """🥖 Bake fresh loaves with heavy stdlib imports."""
    bake.run()


@breadctl.command(name="deliver")
def deliver_cmd():
    """🚚 Deliver bread to customers using httpx."""
    deliver.run()


@breadctl.command(name="inventory")
def inventory_cmd():
    """📦 Show current inventory using sqlite3."""
    inventory.run()


def cli() -> None:
    """Entry point for the normal CLI."""
    breadctl()


if __name__ == "__main__":
    cli()
