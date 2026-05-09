#!/usr/bin/env python3
"""Stop the /ideate timer server. Cross-platform cleanup for server.py."""
import os
import json
import signal

HERE = os.path.dirname(os.path.abspath(__file__))
RUNTIME_FILE = os.path.join(HERE, ".runtime.json")


def main():
    if not os.path.exists(RUNTIME_FILE):
        return
    try:
        with open(RUNTIME_FILE) as f:
            info = json.load(f)
        pid = info.get("pid")
        if pid:
            if os.name == "nt":
                os.system(f"taskkill /PID {pid} /F >NUL 2>&1")
            else:
                try:
                    os.kill(pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
    finally:
        try:
            os.remove(RUNTIME_FILE)
        except OSError:
            pass


if __name__ == "__main__":
    main()
