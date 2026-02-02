from __future__ import annotations

from typing import Dict

from app.utils.validators import validate_requirements


def validate(data: Dict) -> Dict:
	"""Run validation and return validation result dict."""
	return validate_requirements(data)

