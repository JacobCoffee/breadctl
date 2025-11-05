"""Lazy imports CLI entry point - uses PEP 810 lazy imports."""

import rich_click as click

from breadctl import util

lazy import breadctl.bake as bake
lazy import breadctl.deliver as deliver
lazy import breadctl.inventory as inventory

click.rich_click.USE_RICH_MARKUP = util.click.rich_click.USE_RICH_MARKUP
click.rich_click.SHOW_ARGUMENTS = util.click.rich_click.SHOW_ARGUMENTS
click.rich_click.MAX_WIDTH = util.click.rich_click.MAX_WIDTH


@click.group()
def cli() -> None:
    """[bold green]🍞 breadctl-lazy[/] - Manage bread operations.

    This is the LAZY version using PEP 810 lazy imports.
    Modules are only loaded when their commands are invoked.
    """


@cli.command(name="bake")
def bake_cmd() -> None:
    """🥖 Bake fresh loaves using pandas and matplotlib."""
    bake.run()


@cli.command(name="deliver")
def deliver_cmd() -> None:
    """🚚 Deliver bread to customers using httpx."""
    deliver.run()


@cli.command(name="inventory")
def inventory_cmd() -> None:
    """📦 Show current inventory using sqlite3."""
    inventory.run()


if __name__ == "__main__":
    cli()
