from __future__ import annotations

from pydantic import BaseModel
from typing import Dict, Optional


class Requirements(BaseModel):
	objective: str
	role: Optional[str] = None
	inputs: Optional[Dict[str, str]] = None
	constraints: Optional[str] = None
	output_format: Optional[str] = None
	metadata: Optional[Dict[str, str]] = None

