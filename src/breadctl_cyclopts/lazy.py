"""Lazy imports CLI entry point - uses inline imports for deferred loading."""

from cyclopts import App

app = App(
    name="breadctl-lazy",
    help="🍞 breadctl-lazy - Manage bread operations.\n\nThis is the LAZY version using lazy loading.\nModules are only loaded when their commands are invoked.",
)


@app.command
def bake() -> None:
    """🥖 Bake fresh loaves with heavy stdlib imports."""
    from breadctl import bake as bake_mod

    bake_mod.run()


@app.command
def deliver() -> None:
    """🚚 Deliver bread to customers using httpx."""
    from breadctl import deliver as deliver_mod

    deliver_mod.run()


@app.command
def inventory() -> None:
    """📦 Show current inventory using sqlite3."""
    from breadctl import inventory as inventory_mod

    inventory_mod.run()


def cli() -> None:
    """Entry point for the lazy CLI."""
    app()


if __name__ == "__main__":
    cli()
