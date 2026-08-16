#!/usr/bin/env python3
"""Create a small PNG with a synthetic CTF flag in a tEXt metadata chunk."""

from __future__ import annotations

import binascii
import struct
import zlib
from pathlib import Path

WIDTH = 64
HEIGHT = 64
FLAG = "flag{metadata_can_talk}"
OUTPUT = Path(__file__).with_name("evidence.png")


def chunk(kind: bytes, data: bytes) -> bytes:
    checksum = binascii.crc32(kind + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", checksum)


def build_png() -> bytes:
    signature = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0)

    rows = bytearray()
    for y in range(HEIGHT):
        rows.append(0)  # No per-row filter.
        for x in range(WIDTH):
            rows.extend(((x * 4) % 256, (y * 4) % 256, ((x + y) * 2) % 256))

    metadata = b"Comment\x00" + FLAG.encode("latin-1")
    return b"".join(
        [
            signature,
            chunk(b"IHDR", ihdr),
            chunk(b"tEXt", metadata),
            chunk(b"IDAT", zlib.compress(bytes(rows), level=9)),
            chunk(b"IEND", b""),
        ]
    )


def main() -> None:
    OUTPUT.write_bytes(build_png())
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
