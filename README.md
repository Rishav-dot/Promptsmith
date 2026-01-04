# PromptSmith 🧠✍️  
**A State-Driven Prompt Engineering System using LangGraph**

## Overview

PromptSmith is a **state-driven prompt engineering platform** that helps users design **high-quality, reusable prompts** by:

1. Collecting structured requirements
2. Validating them using deterministic rules
3. Generating professional prompt templates
4. Evaluating prompt quality using an LLM-based critic
5. Iteratively refining prompts
6. Maintaining version history for reproducibility

Unlike typical prompt generators, PromptSmith uses a **LangGraph-powered state machine** to control how and when prompts are generated.

---

## Motivation

Prompt quality often suffers because:
- Objectives are unclear
- Constraints are missing
- Inputs are poorly defined
- Changes overwrite previous prompts

This project addresses these issues by treating prompt creation as a **controlled, versioned workflow** rather than a one-shot generation.

---

## Key Features

- 🧩 **State-driven workflow** using LangGraph
- 📋 **Structured requirement extraction** via tool calling
- ✅ **Rule-based validation** before generation
- 🏗️ **Enforced prompt templates** (role, objective, inputs, constraints, output format)
- 📊 **Prompt quality evaluation agent**
- 🔁 **Iterative refinement loop**
- 🗂️ **Prompt versioning & history**
- 💾 **Persistent storage** (SQLite / JSON)

---

## System Architecture

User
↓
Requirement Collection (LLM)
↓
Validation (Rule-based)
↓
Prompt Generation (LLM)
↓
Prompt Evaluation (LLM)
↓
Prompt Refinement (LLM)
↓
Versioned Storage


The system transitions between states **dynamically**, based on validation and evaluation outcomes.

---

## Tech Stack

- Python 3.10+
- LangGraph
- LangChain
- OpenAI API
- Pydantic v2
- SQLite (for prompt versioning)
- Streamlit / CLI (UI layer)

---

## Project Structure

app/
├── graph/ # LangGraph workflow and states
├── models/ # Pydantic models
├── llm/ # LLM wrappers and system prompts
├── storage/ # Prompt version persistence
├── utils/ # Validation and helper utilities


---

## Current Status

🚧 **Work in Progress**

Planned development timeline:
- [x] Project architecture & design
- [ ] Requirement gathering state
- [ ] Validation logic
- [ ] Prompt generation
- [ ] Evaluation agent
- [ ] Prompt refinement
- [ ] Versioning & persistence
- [ ] UI & documentation

---

## How to Run (will be updated)

```bash
pip install -r requirements.txt
python app/main.py
```
```markdown
---

## Example Use Case

A user wants to create a prompt for:

- RAG-based question answering
- Strict no-hallucination constraints
- JSON output format
- Clearly defined input variables

PromptSmith will:

- Collect missing or unclear requirements
- Reject vague or incomplete inputs
- Generate a structured, reusable prompt
- Evaluate prompt quality using an LLM-based critic
- Refine the prompt if required
- Store prompt versions for reproducibility

---

## Why This Project Matters

This project demonstrates:

- LLM orchestration using LangGraph
- State machine–driven system design
- Structured prompt engineering
- Validation-first AI workflows
- Versioned prompt lifecycle management

It reflects **real-world LLM system architecture**, not just prompt writing.

---

## Future Improvements

- FastAPI backend for API access
- Multi-user support
- Prompt testing against sample inputs
- Prompt diffing and comparison UI
- Authentication and role-based access
Author

Built by Rishav Datta
Machine Learning & AI Systems Enthusiast


---

# C. How you should update this README daily

### Each day:
- Tick checkboxes
- Add small screenshots / examples
- Update “Current Status”
- Add design notes in `docs/`

This tells reviewers:
> *“This person builds iteratively like a real engineer.”*

---

# D. Final Advice (Important)

❌ Don’t wait to finish before pushing  
✅ Push **small, meaningful commits daily**

Commit messages like:
add validation state for requirements
implement prompt evaluation agent
add prompt versioning with sqlite


These are **gold for interviews**.

---

If you want, next I can:
- Generate `requirements.txt`
- Write `state_graph.py` skeleton
- Design validation rules precisely
- Help you plan **Day 1 commits**

Just tell me what you want next 🚀
