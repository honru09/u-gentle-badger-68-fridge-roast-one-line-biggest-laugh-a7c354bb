#!/usr/bin/env python3
"""
Fridge Roast: One Line, Biggest Laugh
Writes one original roast line about a smart fridge to /output/entry.txt.
Standard library only. No network, no randomness, no external reads.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
ROAST = (
    "My smart fridge updated its firmware at 2 a.m. and locked the ice maker "
    "until I accepted the new terms — even my leftovers are on a "
    "subscription now.\n"
)


def write_roast() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(ROAST, encoding="utf-8")
    os.chmod(OUTPUT_FILE, 0o644)


if __name__ == "__main__":
    write_roast()
