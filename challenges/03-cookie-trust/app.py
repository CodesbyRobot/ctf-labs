#!/usr/bin/env python3
"""Local-only CTF service demonstrating unsafe trust in a client cookie."""

from __future__ import annotations

import html
import os
import secrets
from http import HTTPStatus
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

HOST = "127.0.0.1"
PORT = int(os.environ.get("CTF_PORT", "8000"))
FLAG = os.environ.get("CTF_FLAG", f"flag{{cookie_trust_{secrets.token_hex(6)}}}")


class ChallengeHandler(BaseHTTPRequestHandler):
    server_version = "CTFLabs/1.0"

    def _role(self) -> str:
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get("Cookie", ""))
        except Exception:
            return "guest"
        value = cookie.get("role")
        return value.value if value else "guest"

    def _send_html(self, body: str, *, status: HTTPStatus = HTTPStatus.OK, set_guest: bool = False) -> None:
        payload = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        if set_guest:
            self.send_header("Set-Cookie", "role=guest; Path=/; SameSite=Strict")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        path = urlparse(self.path).path
        role = self._role()

        if path == "/":
            self._send_html(
                """<!doctype html>
<html><body>
<h1>Cookie Trust</h1>
<p>You are signed in as <strong>guest</strong>.</p>
<p>The flag is available only at <a href=\"/admin\">/admin</a>.</p>
</body></html>""",
                set_guest="role=" not in self.headers.get("Cookie", ""),
            )
            return

        if path == "/admin":
            if role == "admin":
                self._send_html(
                    f"<h1>Training admin</h1><p id='flag'>{html.escape(FLAG)}</p>"
                )
            else:
                self._send_html(
                    "<h1>Forbidden</h1><p>Admin role required.</p>",
                    status=HTTPStatus.FORBIDDEN,
                )
            return

        self._send_html("<h1>Not found</h1>", status=HTTPStatus.NOT_FOUND)

    def log_message(self, format: str, *args: object) -> None:
        print(f"[local] {self.client_address[0]} - {format % args}")


def main() -> None:
    server = HTTPServer((HOST, PORT), ChallengeHandler)
    print(f"Cookie Trust is running at http://{HOST}:{PORT}")
    print("This service is intentionally vulnerable and bound to loopback only.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
