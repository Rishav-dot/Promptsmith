from __future__ import annotations

from typing import Optional


class MockLLMClient:
	"""A deterministic mock LLM client for local development and testing.

	It returns predictable responses so the project can be run without external APIs.
	"""

	def __init__(self, model: str = "mock-1") -> None:
		self.model = model

	def generate(self, prompt: str, system: Optional[str] = None) -> str:
		# Very simple deterministic "generation" for testing
		header = f"[model={self.model}] "
		if system:
			header += f"(system) "
		return header + prompt.strip().replace("\n", " ")

