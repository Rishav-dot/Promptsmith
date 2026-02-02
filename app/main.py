from __future__ import annotations

from app.graph.states.info import collect_info
from app.graph.states.validate import validate
from app.graph.states.generate import generate_prompt
from app.graph.states.evaluate import evaluate_prompt
from app.graph.states.refine import refine_prompt
from app.storage.repository import PromptRepository
from app.utils.helpers import now_iso


def run_pipeline(data: dict):
    print("[1] Collecting info")
    req = collect_info(data)

    print("[2] Validating requirements")
    v = validate(req.dict())
    if not v.get("valid"):
        print("Validation failed:", v.get("errors"))
        return

    print("[3] Generating prompt")
    prompt = generate_prompt(req)
    print("Generated prompt id:", prompt.id)

    print("[4] Evaluating prompt")
    eval_res = evaluate_prompt(prompt.template)
    print("Evaluation score:", eval_res.score)

    if eval_res.score < 0.6:
        print("[5] Refining prompt")
        prompt = refine_prompt(prompt, eval_res)

    print("[6] Saving prompt to repository")
    repo = PromptRepository()
    repo.save(prompt)
    print("Saved prompt", prompt.id, "version", prompt.version, "at", prompt.created_at)


if __name__ == "__main__":
    sample = {
        "objective": "Create a JSON-output prompt for RAG QA",
        "role": "System",
        "inputs": {"context": "documents", "question": "user question"},
        "constraints": "No hallucinations. Strict JSON output.",
        "output_format": "JSON",
        "metadata": {"created_by": "dev"},
    }
    print("Running PromptSmith minimal demo at", now_iso())
    run_pipeline(sample)
