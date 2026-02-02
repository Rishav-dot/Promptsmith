from __future__ import annotations

from pydantic import BaseModel
from typing import List, Optional


class EvaluationResult(BaseModel):
	score: float
	issues: List[str] = []
	recommendations: Optional[List[str]] = None

