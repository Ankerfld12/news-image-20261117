#!/usr/bin/env python3
"""Deliver the finished poster for the news-image-20261117 entry.

This repository ships its poster as a completed asset, assets/entry.png.
The judging harness runs this program offline and afterwards reads a
single file, /output/entry.png. Everything below exists to move the
bundled poster to that exact spot, byte for byte, and nothing more.
"""

import shutil
import sys
from pathlib import Path

# The poster sits in the assets folder next to this file.
POSTER_PATH = Path(__file__).resolve().parent / "assets" / "entry.png"

# Where the harness looks once the program has finished.
OUTPUT_FOLDER = Path("/output")
OUTPUT_PATH = OUTPUT_FOLDER / "entry.png"


def place_poster() -> Path:
    """Copy the bundled poster into /output and return the result path."""
    if not POSTER_PATH.is_file():
        raise FileNotFoundError(f"poster asset not found: {POSTER_PATH}")
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
    # copyfile moves the raw bytes only (no metadata, no re-encoding),
    # so the delivered file stays identical to the bundled asset.
    shutil.copyfile(POSTER_PATH, OUTPUT_PATH)
    return OUTPUT_PATH


def main() -> int:
    result = place_poster()
    print(f"poster delivered to {result} ({result.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
