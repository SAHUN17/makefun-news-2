"""Publish the news-image-01 bounty entry (13 November 2026 news) to /output.

Copies the bundled newspaper-style front page entry.png to the directory given
by ENTRY_OUTPUT_DIR (default: /output).
"""

import os
import shutil
from pathlib import Path

ENTRY_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
PNG_MAGIC = b"\x89PNG"


def resolve_source() -> Path:
    """Return the bundled entry.png sitting next to this file."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def check_source(path: Path) -> None:
    """Raise if *path* is missing, empty, or not a PNG by magic bytes."""
    if not path.exists():
        raise FileNotFoundError(f"entry image not found: {path}")
    if path.stat().st_size == 0:
        raise ValueError(f"entry image is empty: {path}")
    with path.open("rb") as fh:
        magic = fh.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        raise ValueError(f"entry image is not a PNG: {path}")


def publish(out_dir: str) -> Path:
    """Create *out_dir*, copy the source into it, and return the destination."""
    src = resolve_source()
    check_source(src)
    dest_dir = Path(out_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / ENTRY_NAME
    shutil.copyfile(src, dest)
    return dest


def verify(dest: Path) -> None:
    """Raise if *dest* is missing, empty, or not a PNG by magic bytes."""
    if not dest.exists():
        raise FileNotFoundError(f"published entry not found: {dest}")
    if dest.stat().st_size == 0:
        raise ValueError(f"published entry is empty: {dest}")
    with dest.open("rb") as fh:
        magic = fh.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        raise ValueError(f"published entry is not a PNG: {dest}")


def main() -> int:
    """Resolve the output dir, publish, verify, and print the destination."""
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    dest = publish(out_dir)
    verify(dest)
    print(dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
