"""Skill 6 — DB lite: sqlite round-trip (stdlib)."""
from __future__ import annotations
import sqlite3
from pathlib import Path


def main() -> int:
    db = Path("/tmp/workshop-skill6.sqlite")
    if db.exists():
        db.unlink()
    con = sqlite3.connect(db)
    try:
        con.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY, body TEXT NOT NULL)")
        con.execute("INSERT INTO notes (body) VALUES (?)", ("shared-basics",))
        con.commit()
        row = con.execute("SELECT body FROM notes WHERE id = 1").fetchone()
        assert row and row[0] == "shared-basics"
    finally:
        con.close()
        db.unlink(missing_ok=True)
    print("skill-6 db-lite checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
