---
name: ai-ml-development
description: "Experiment workflows, datasets, evals, model packaging, serving, and rollback for AI/ML systems. Use when the user mentions: ML, machine learning, AI, model training, fine-tuning, PyTorch, TensorFlow, JAX, scikit-learn, Hugging Face, LangChain, LlamaIndex, evals, RAG, vector database, embeddings, MLflow, Weights & Biases, prompt engineering, Anthropic API, OpenAI API. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: data analysis without model training (use data-science-development); ML infra rollout work without model changes (use devops-and-infrastructure)."
---

# AI/ML Development

Experiment workflows, datasets, evals, model packaging, serving, and rollback for AI/ML systems.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: ML, machine learning, AI, model training, fine-tuning, PyTorch, TensorFlow, JAX, scikit-learn, Hugging Face, LangChain, LlamaIndex, evals, RAG, vector database, embeddings, MLflow, Weights & Biases, prompt engineering, Anthropic API, OpenAI API.

Use when the user wants any of:

- Run reproducible experiments — pinned data, pinned code, pinned hardware.
- Build eval harnesses that catch regressions before users do.
- Version datasets and models the same way you version code.
- Apply prompt evals for LLM-backed features — golden cases, edge cases, adversarial cases.
- Decide between fine-tune, RAG, tool-use, and prompting for a given problem.
- Wire model serving with retries, circuit breakers, and graceful degradation.

## When NOT to use this skill

- data analysis without model training (use data-science-development)
- ML infra rollout work without model changes (use devops-and-infrastructure)

## Workflow

1. **Intake.** Read the user intent. Identify which capability above applies. If the request crosses
   into another discipline (e.g. UI + DB), call the `discipline-router` agent before splitting work.
2. **Inspect.** Look at the actual repo state with Read/Grep/Glob before proposing changes. Do not
   assume what code exists from project name alone.
3. **Source-check.** For non-obvious technical claims, ground the answer in the official sources
   listed in `references/official-sources.md`. Use the Context7 MCP for live doc lookups instead of
   relying on training-data memory for fast-moving APIs.
4. **Produce.** Generate the appropriate artifact from the list below.
5. **Verify.** Run every verification layer below before claiming done. Build success is not done.
   200 responses are not done. A real user seeing correct output is done.
6. **Hand back.** Report what shipped, what the visitor sees, what changed. No file paths, function
   names, or engineering jargon unprompted.

## Artifacts this skill produces

- Experiment tracker entry: dataset hash, code hash, hyperparams, metric.
- Eval suite with should-pass and should-fail cases per capability.
- Model card: training data, intended use, limitations, fairness notes.
- Inference SLA: P50/P95/P99 latency, cost per call.
- Prompt or fine-tune diff with eval delta.
- Rollback plan that pins the previous model version.

## Anti-patterns this skill pushes back against

- Evaluating on the training set.
- Vibes-based prompt engineering with no eval suite.
- Shipping an LLM feature without a deterministic fallback for outages.
- Storing API keys in notebooks.
- Comparing model versions on different evals.

## Verification required before claiming done

- Eval suite passes against current + previous model version.
- Inference latency within SLA on the target hardware.
- Cost forecast at expected QPS within budget.
- Outputs reviewed for PII leakage and policy violations.
- Rollback rehearsed by switching the version pin.

## Suggested commands

- `/uber:ai eval-suite features/summarize`
- `/uber:ai rag-design --corpus=docs/`
- `/uber:ai rollback-model --service=summarizer`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user can see the correct output of this work. Build success, deploy success, and 200
responses do not equal done. Every data surface explicitly handles loading, error, empty, and
populated states. Verification actually happened — no claim of "verified" without evidence.
