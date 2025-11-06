"""Delivery operations module - uses httpx."""

import time

import httpx


def run() -> None:
    """Simulate delivery using httpx."""
    time.sleep(0.2)

    httpx.Response(
        status_code=200,
        text="Delivered OK",
    )
