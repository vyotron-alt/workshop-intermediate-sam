#!/usr/bin/env bash
# Skill 7 — fake deploy (no cloud). Students replace with real steps later.
set -euo pipefail
echo "Packaging workshop artifact…"
test -f hello/__init__.py
test -f pyproject.toml
echo "DRY_RUN_OK"
