"""Skill 1 — Git/PR: repo hygiene checks (no LLM)."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    readme = ROOT / "README.md"
    assert readme.is_file(), "README.md missing"
    text = readme.read_text(encoding="utf-8")
    assert "portal" in text.lower() or "workshop" in text.lower(), "README should mention workshop/portal"
    # Students practice PRs; we only assert the repo has a clear contribution path
    assert (ROOT / ".gitignore").is_file(), ".gitignore missing"
    print("skill-1 git/pr checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
