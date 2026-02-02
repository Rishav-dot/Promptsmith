from __future__ import annotations

from app.llm.client import MockLLMClient
from app.models.prompt import PromptTemplate
from app.utils.helpers import now_iso


def refine_prompt(prompt: PromptTemplate, evaluation) -> PromptTemplate:
	client = MockLLMClient()
	# Simple refinement: append evaluation recommendations to the template
	recs = evaluation.recommendations or []
	refined_text = prompt.template + "\n\n# Refinement:\n" + "\n".join(recs)
	return PromptTemplate(id=prompt.id, template=refined_text, version=prompt.version + 1, created_at=now_iso())

