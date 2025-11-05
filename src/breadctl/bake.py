"""Baking operations module - uses heavy imports (pandas, matplotlib)."""

import time

import matplotlib.pyplot as plt
import pandas as pd


def run() -> None:
    """Simulate baking process using heavy imports."""
    time.sleep(0.5)
    df = pd.DataFrame({"loaves": [1, 2, 3], "temp": [350, 360, 370]})
    plt.plot(df["loaves"], df["temp"])
    print(f"🥖 Baked {len(df)} loaves successfully!")
    print(f"   Temperature range: {df['temp'].min()}°F - {df['temp'].max()}°F")
