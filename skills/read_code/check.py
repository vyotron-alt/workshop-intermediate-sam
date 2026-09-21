"""Skill 3 — Read code: import + docstring / symbol checks."""
from __future__ import annotations
import inspect
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from hello import greet


def main() -> int:
    assert callable(greet)
    src = inspect.getsource(greet)
    assert "Hello" in src
    assert greet("Sam") == "Hello, Sam"
    print("skill-3 read-code checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
