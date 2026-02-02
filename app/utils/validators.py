from __future__ import annotations

from typing import Dict, List

from pydantic import ValidationError

from app.models.requirements import Requirements


def validate_requirements(data: Dict) -> Dict:
	"""Validate a requirements dict against the Requirements model.

	Returns a dict: {"valid": bool, "errors": List[str], "model": Requirements|None}
	"""
	errors: List[str] = []
	model = None
	try:
		model = Requirements(**data)
	except ValidationError as exc:
		for e in exc.errors():
			loc = ".".join(str(x) for x in e.get("loc", []))
			msg = e.get("msg", "invalid")
			errors.append(f"{loc}: {msg}")

	# additional rule-based checks
	if model:
		if not model.objective or len(model.objective.strip()) < 5:
			errors.append("objective: must be at least 5 characters")
		if not model.output_format:
			errors.append("output_format: required")

	return {"valid": len(errors) == 0, "errors": errors, "model": model}

