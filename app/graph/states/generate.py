from __future__ import annotations

from app.llm.client import MockLLMClient
from app.llm.prompts import GENERATION_PROMPT_TEMPLATE, SYSTEM_PROMPT
from app.models.prompt import PromptTemplate
from app.utils.helpers import generate_id, now_iso


def generate_prompt(requirements) -> PromptTemplate:
	client = MockLLMClient()
	prompt_text = GENERATION_PROMPT_TEMPLATE.format(
		role=requirements.role or "Assistant",
		objective=requirements.objective,
		inputs=requirements.inputs or {},
		constraints=requirements.constraints or "",
		output_format=requirements.output_format or "text",
	)
	resp = client.generate(prompt_text, system=SYSTEM_PROMPT)
	pt = PromptTemplate(id=generate_id("prompt"), template=resp, version=1, created_at=now_iso())
	return pt

