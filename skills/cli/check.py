"""Skill 2 — CLI checks."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    r = subprocess.run(
        [sys.executable, str(ROOT / "skills/cli/greet_cli.py"), "Alex"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0, r.stderr
    assert "Hello, Alex" in r.stdout, r.stdout
    print("skill-2 cli checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
