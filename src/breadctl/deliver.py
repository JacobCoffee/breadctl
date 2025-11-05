"""Delivery operations module - uses httpx."""

import time

import httpx


def run() -> None:
    """Simulate delivery using httpx."""
    time.sleep(0.2)

    response = httpx.Response(
        status_code=200,
        text="Delivered OK",
    )
    print(f"🚚 Delivery status: {response.text}")
    print(f"   HTTP Status: {response.status_code}")
