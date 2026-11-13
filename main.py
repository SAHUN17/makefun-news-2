"""Publishes the 13 November 2026 news image entry.png to /output/entry.png."""

import os
import shutil

ENTRY_NAME = "entry.png"
OUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def copy_entry() -> str:
    """Copy the entry image into OUT_DIR and return the destination path."""
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY_NAME)
    dest = os.path.join(OUT_DIR, ENTRY_NAME)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(src, dest)
    return dest


def main() -> None:
    print(copy_entry())


if __name__ == "__main__":
    main()
