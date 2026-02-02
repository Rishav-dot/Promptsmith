from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Optional


DB_PATH = Path("data") / "prompts.db"


def ensure_db() -> None:
	DB_PATH.parent.mkdir(parents=True, exist_ok=True)
	conn = sqlite3.connect(DB_PATH)
	cur = conn.cursor()
	cur.execute(
		"""
	CREATE TABLE IF NOT EXISTS prompts (
		id TEXT PRIMARY KEY,
		template TEXT NOT NULL,
		version INTEGER NOT NULL,
		created_at TEXT NOT NULL,
		metadata TEXT
	)
	"""
	)
	conn.commit()
	conn.close()


def get_conn() -> sqlite3.Connection:
	ensure_db()
	return sqlite3.connect(DB_PATH)

