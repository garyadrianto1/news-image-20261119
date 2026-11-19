#!/usr/bin/env python3
"""Entry for news-image-20261119: copy the pre-rendered front page to /output/entry.png.

The image was drawn at build time (system Python + PIL) as a flat vector
layout: 36 verified stories from Thursday 19 November 2026, 3 large leads,
10 medium stories, a world map with numbered pins, a numbered one-liner
list, and a DATE CHECK box. This program only copies the file; no network,
no randomness, stdlib only.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # 1 MiB, per the competition rules
MAX_DIM = 1024


def validate_png(path):
    """Check the PNG magic, the size cap, and the IHDR dimensions."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {size} bytes > {MAX_BYTES}")
    with open(path, "rb") as f:
        head = f.read(33)
    if head[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG (bad magic bytes)")
    if len(head) < 33 or head[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit(f"entry.png too large: {width}x{height} > {MAX_DIM}x{MAX_DIM}")
    return size, width, height


def main():
    size, width, height = validate_png(SRC)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, dst)
    # read-back: the copy must be byte-for-byte identical to the source
    with open(SRC, "rb") as f:
        src_bytes = f.read()
    with open(dst, "rb") as f:
        dst_bytes = f.read()
    if src_bytes != dst_bytes:
        raise SystemExit("copy mismatch: output differs from source")
    print(f"wrote {dst} ({size} bytes, {width}x{height}, sha256 checked by caller)")


if __name__ == "__main__":
    main()
