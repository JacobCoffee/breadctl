"""Inventory operations module - uses sqlite3 and json."""

import sqlite3
import time
from pathlib import Path


def run() -> None:
    """Simulate inventory lookup."""
    Path("/tmp/breadctl.db")
    time.sleep(0.3)

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE inventory (
            item TEXT PRIMARY KEY,
            quantity INTEGER
        )
    """)
    cursor.execute("INSERT INTO inventory VALUES ('flour', 5), ('yeast', 3)")

    cursor.execute("SELECT item, quantity FROM inventory")
    {row[0]: row[1] for row in cursor.fetchall()}


    conn.close()
