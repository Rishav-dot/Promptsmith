from __future__ import annotations

from app.models.requirements import Requirements


def collect_info(data: dict) -> Requirements:
	"""Collect and normalize requirement data into a Requirements model dict.

	For this minimal implementation we assume data is already structured.
	"""
	return Requirements(**data)

