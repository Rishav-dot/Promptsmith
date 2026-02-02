from __future__ import annotations

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PromptTemplate(BaseModel):
	id: str
	template: str
	version: int = 1
	created_at: Optional[str] = None
	metadata: Optional[dict] = None

	def dict_store(self):
		return {
			"id": self.id,
			"template": self.template,
			"version": self.version,
			"created_at": self.created_at or datetime.utcnow().isoformat() + "Z",
			"metadata": self.metadata or {},
		}

