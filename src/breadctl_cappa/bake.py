"""Baking operations module - simulates heavy imports."""

# Simulate heavy imports by importing multiple stdlib modules
# maybe..?
import collections
import itertools
import time


def run() -> None:
    """Simulate baking process with heavy stdlib imports."""
    time.sleep(0.3)

    # Simulate data processing that would use pandas
    loaves = [1, 2, 3]
    temps = [350, 360, 370]

    # Use some of the heavy imports to prevent them being optimized away
    data = collections.defaultdict(list)
    for loaf, temp in itertools.zip_longest(loaves, temps):
        data["loaves"].append(loaf)
        data["temps"].append(temp)

