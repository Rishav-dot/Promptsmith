from __future__ import annotations

import uuid
from datetime import datetime


def now_iso() -> str:
	return datetime.utcnow().isoformat() + "Z"


def generate_id(prefix: str = "id") -> str:
	return f"{prefix}_{uuid.uuid4().hex[:8]}"

