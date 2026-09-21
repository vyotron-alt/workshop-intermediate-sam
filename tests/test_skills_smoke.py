"""Cheap cross-skill smoke (no LLM)."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _run(rel: str) -> None:
    r = subprocess.run([sys.executable, str(ROOT / rel)], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, f"{rel} failed: {r.stderr or r.stdout}"


def test_skill_checks_1_to_7():
    for rel in (
        "skills/git_pr/check.py",
        "skills/cli/check.py",
        "skills/read_code/check.py",
        "skills/http_api/check.py",
        "skills/db_lite/check.py",
        "skills/deploy/check.py",
    ):
        _run(rel)
