"""Normal (non-lazy) CLI entry point - imports all modules at startup."""

import rich_click as click

from breadctl import bake, deliver, inventory, util

click.rich_click.USE_RICH_MARKUP = util.click.rich_click.USE_RICH_MARKUP
click.rich_click.SHOW_ARGUMENTS = util.click.rich_click.SHOW_ARGUMENTS
click.rich_click.MAX_WIDTH = util.click.rich_click.MAX_WIDTH


@click.group()
def cli() -> None:
    """[bold blue]🍞 breadctl[/] - Manage bread operations.

    This is the NORMAL version that imports all modules at startup.
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
