---
description: AI/ML Development — invoke the ai-ml-development skill with focused intent.
argument-hint: <action> [target] [flags]
allowed-tools:
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Bash
  - Task
---

# /uber:ai

Invoke the **ai-ml-development** skill for a AI/ML Development task.

## Usage

```
/uber:ai $ARGUMENTS
```

Common patterns:

- `/uber:ai eval-suite features/summarize`
- `/uber:ai rag-design --corpus=docs/`
- `/uber:ai rollback-model --service=summarizer`

## What this command does

1. Loads the `ai-ml-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

ML, machine learning, AI, model training, fine-tuning, PyTorch, TensorFlow, JAX, scikit-learn, Hugging Face, LangChain, LlamaIndex, evals, RAG, vector database, embeddings, MLflow, Weights & Biases, prompt engineering, Anthropic API, OpenAI API.
