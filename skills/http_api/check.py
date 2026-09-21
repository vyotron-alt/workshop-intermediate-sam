"""Skill 5 — HTTP API checks (stdlib urllib)."""
from __future__ import annotations
import json
import sys
import threading
import urllib.request
from http.server import HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from skills.http_api.app import Handler


def main() -> int:
    httpd = HTTPServer(("127.0.0.1", 0), Handler)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=2) as resp:
        data = json.loads(resp.read().decode())
    httpd.shutdown()
    assert data.get("ok") is True
    assert data.get("skill") == 5
    print("skill-5 http-api checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
