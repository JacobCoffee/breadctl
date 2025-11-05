"""Shared utilities for breadctl CLI."""

import rich_click as click

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.MAX_WIDTH = 100
click.rich_click.STYLE_ERRORS_SUGGESTION = "bold red"
