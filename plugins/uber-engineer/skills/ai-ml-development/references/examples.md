# AI/ML Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/ai eval-suite features/summarize
```

```
/ai rag-design --corpus=docs/
```

```
/ai rollback-model --service=summarizer
```

The `/uber` router will dispatch to `/ai` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Add a summarization feature."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Build the eval suite first — 30 golden cases (correct summaries), 15 edge cases (empty input, max-length input, mixed languages), 10 adversarial cases (prompt injection attempts) — then choose the approach (RAG vs fine-tune vs prompt) based on which one passes the suite at the lowest cost-per-call."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `data-science-development` skill — for adjacent work that's better handled there.
- `backend-development` skill — for adjacent work that's better handled there.
- `security-development` skill — for adjacent work that's better handled there.
