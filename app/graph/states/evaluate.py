from __future__ import annotations

from app.llm.client import MockLLMClient
from app.models.evaluation import EvaluationResult


def evaluate_prompt(prompt_text: str) -> EvaluationResult:
	client = MockLLMClient()
	# In this mock evaluation we give a basic score based on length and simple checks
	resp = client.generate("EVALUATE: " + prompt_text)
	score = min(1.0, max(0.0, len(prompt_text) / 300.0))
	issues = []
	if "hallucinat" in prompt_text.lower():
		issues.append("mentions hallucination rules")
	return EvaluationResult(score=score, issues=issues, recommendations=[resp])

