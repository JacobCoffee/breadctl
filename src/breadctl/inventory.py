"""Inventory operations module - uses sqlite3 and json."""

import json
import sqlite3
import time
from pathlib import Path


def run() -> None:
    """Simulate inventory lookup."""
    db_path = Path("/tmp/breadctl.db")
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
    items = {row[0]: row[1] for row in cursor.fetchall()}

    print("📦 Current inventory:")
    print(f"   {json.dumps(items, indent=2)}")

    conn.close()
