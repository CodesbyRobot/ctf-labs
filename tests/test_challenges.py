from __future__ import annotations

import base64
import binascii
import codecs
import re
import struct
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class ChallengeIntegrityTests(unittest.TestCase):
    def test_encoding_trail_decodes_to_expected_flag(self) -> None:
        artifact = (ROOT / "challenges/01-encoding-trail/artifact.txt").read_text().strip()
        base64_layer = bytes.fromhex(artifact)
        rot13_layer = base64.b64decode(base64_layer).decode("utf-8")
        flag = codecs.decode(rot13_layer, "rot_13")
        self.assertEqual(flag, "flag{encoding_is_not_encryption}")

    def test_log_hunt_uses_reserved_ip_and_contains_flag(self) -> None:
        log_text = (ROOT / "challenges/02-log-hunt/access.log").read_text()
        matching = [line for line in log_text.splitlines() if "/internal/export" in line]
        self.assertEqual(len(matching), 3)
        self.assertTrue(all(line.startswith("203.0.113.77 ") for line in matching))

        request_path = re.search(r'"GET (\S+) HTTP/1\.1"', matching[-1])
        self.assertIsNotNone(request_path)
        note = parse_qs(urlsplit(request_path.group(1)).query)["note"][0]
        self.assertEqual(base64.b64decode(note).decode(), "flag{logs_tell_a_story}")

    def test_cookie_service_is_loopback_only(self) -> None:
        source = (ROOT / "challenges/03-cookie-trust/app.py").read_text()
        self.assertIn('HOST = "127.0.0.1"', source)
        self.assertNotIn('HOST = "0.0.0.0"', source)
        self.assertIn('role == "admin"', source)

    def test_png_has_valid_text_chunk_with_expected_flag(self) -> None:
        data = (ROOT / "challenges/04-png-breadcrumb/evidence.png").read_bytes()
        self.assertTrue(data.startswith(b"\x89PNG\r\n\x1a\n"))

        offset = 8
        text_values: list[bytes] = []
        while offset < len(data):
            length = struct.unpack(">I", data[offset : offset + 4])[0]
            kind = data[offset + 4 : offset + 8]
            payload = data[offset + 8 : offset + 8 + length]
            crc_read = struct.unpack(">I", data[offset + 8 + length : offset + 12 + length])[0]
            crc_expected = binascii.crc32(kind + payload) & 0xFFFFFFFF
            self.assertEqual(crc_read, crc_expected)
            if kind == b"tEXt":
                text_values.append(payload)
            offset += 12 + length
            if kind == b"IEND":
                break

        self.assertIn(b"Comment\x00flag{metadata_can_talk}", text_values)


if __name__ == "__main__":
    unittest.main()
