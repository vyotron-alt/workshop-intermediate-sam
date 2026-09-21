"""Skill 2 — CLI: tiny argparse tool students can extend."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from hello import greet


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="greet-cli", description="Shared basics CLI demo")
    p.add_argument("name", nargs="?", default="Intermediate")
    args = p.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
