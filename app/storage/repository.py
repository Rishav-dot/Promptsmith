from __future__ import annotations

import json
from typing import Optional

from app.models.prompt import PromptTemplate
from app.storage.db import get_conn


class PromptRepository:
	def __init__(self) -> None:
		pass

	def save(self, prompt: PromptTemplate) -> None:
		conn = get_conn()
		cur = conn.cursor()
		data = prompt.dict_store()
		cur.execute(
			"INSERT OR REPLACE INTO prompts (id, template, version, created_at, metadata) VALUES (?, ?, ?, ?, ?)",
			(
				data["id"],
				data["template"],
				data["version"],
				data["created_at"],
				json.dumps(data.get("metadata", {})),
			),
		)
		conn.commit()
		conn.close()

	def get(self, id: str) -> Optional[PromptTemplate]:
		conn = get_conn()
		cur = conn.cursor()
		cur.execute("SELECT id, template, version, created_at, metadata FROM prompts WHERE id = ?", (id,))
		row = cur.fetchone()
		conn.close()
		if not row:
			return None
		metadata = {}
		try:
			metadata = json.loads(row[4]) if row[4] else {}
		except Exception:
			metadata = {}
		return PromptTemplate(id=row[0], template=row[1], version=row[2], created_at=row[3], metadata=metadata)

