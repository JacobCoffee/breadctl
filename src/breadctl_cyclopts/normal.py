"""Normal (non-lazy) CLI entry point - imports all modules at startup."""

from cyclopts import App

from breadctl import bake as bake_mod
from breadctl import deliver as deliver_mod
from breadctl import inventory as inventory_mod

app = App(
    name="breadctl",
    help="🍞 breadctl - Manage bread operations.\n\nThis is the NORMAL version that imports all modules at startup.",
)


@app.command
def bake() -> None:
    """🥖 Bake fresh loaves with heavy stdlib imports."""
    bake_mod.run()


@app.command
def deliver() -> None:
    """🚚 Deliver bread to customers using httpx."""
    deliver_mod.run()


@app.command
def inventory() -> None:
    """📦 Show current inventory using sqlite3."""
    inventory_mod.run()


def cli() -> None:
    """Entry point for the normal CLI."""
    app()


if __name__ == "__main__":
    cli()
