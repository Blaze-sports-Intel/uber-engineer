# Data Science Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/data analysis-plan --question='did onboarding v2 lift d7?'
```

```
/data dashboard-audit --area=revenue
```

```
/data ab-test power-analysis
```

The `/uber` router will dispatch to `/data` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Did the new onboarding lift d7 retention?"

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Frame the question (what counts as d7? which cohort? what's the noise floor?), pull from the canonical data warehouse view (not a one-off CSV), check sample-size power for the effect we'd care about, run the test with an FDR correction across the multiple metrics, and write a decision memo with the effect size + 95% CI and a recommended next action — not just 'p < 0.05'."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `ai-ml-development` skill — for adjacent work that's better handled there.
- `database-development` skill — for adjacent work that's better handled there.
- `backend-development` skill — for adjacent work that's better handled there.
