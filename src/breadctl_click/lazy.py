"""Lazy imports CLI entry point - uses inline imports for deferred loading."""

import rich_click as click


@click.group()
def breadctl_lazy():
    """🍞 breadctl-lazy - Manage bread operations.

    This is the LAZY version using deferred imports.
    Modules are only loaded when their commands are invoked.
    """


@breadctl_lazy.command(name="bake")
def bake_cmd():
    """🥖 Bake fresh loaves with heavy stdlib imports."""
    from breadctl import bake

    bake.run()


@breadctl_lazy.command(name="deliver")
def deliver_cmd():
    """🚚 Deliver bread to customers using httpx."""
    from breadctl import deliver

    deliver.run()


@breadctl_lazy.command(name="inventory")
def inventory_cmd():
    """📦 Show current inventory using sqlite3."""
    from breadctl import inventory

    inventory.run()


def cli() -> None:
    """Entry point for the lazy CLI."""
    breadctl_lazy()


if __name__ == "__main__":
    cli()
