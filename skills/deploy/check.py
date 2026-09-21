"""Skill 7 — Deploy: require a deploy script and dry-run it."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    script = ROOT / "scripts/deploy_dry_run.sh"
    assert script.is_file(), "scripts/deploy_dry_run.sh missing"
    r = subprocess.run(["bash", str(script)], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr or r.stdout
    assert "DRY_RUN_OK" in r.stdout
    print("skill-7 deploy checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
