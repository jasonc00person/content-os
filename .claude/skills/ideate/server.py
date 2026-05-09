#!/usr/bin/env python3
"""Tiny HTTP server for /ideate timer. Serves this skill folder on a free port.
Writes pid + port + start timestamp to .runtime.json so the orchestrator can find them.
Cross-platform: macOS, Linux, Windows."""
import http.server
import socketserver
import socket
import os
import sys
import json
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RUNTIME_FILE = os.path.join(HERE, ".runtime.json")
PREFERRED_PORT = 8765
FALLBACK_RANGE = range(8766, 8800)


def find_free_port():
    for port in [PREFERRED_PORT, *FALLBACK_RANGE]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("no free port found in 8765-8800")


def main():
    os.chdir(HERE)
    port = find_free_port()
    with open(RUNTIME_FILE, "w") as f:
        json.dump({"pid": os.getpid(), "port": port, "start": int(time.time())}, f)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
