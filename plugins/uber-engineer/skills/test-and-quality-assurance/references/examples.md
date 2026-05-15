# Test And Quality Assurance — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/qa test-strategy --feature=checkout
```

```
/qa flake-report
```

```
/qa contract-test consumer=web provider=api
```

The `/uber` router will dispatch to `/qa` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Add tests for the checkout flow."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Layer the strategy: unit tests on pure functions (cart math, tax rules), component tests on the form (validation, error display), contract test against the orders API (Pact), one Playwright E2E covering the happy path against a per-PR ephemeral env, visual regression on the order summary card only — total suite under 90 seconds."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `frontend-development` skill — for adjacent work that's better handled there.
- `backend-development` skill — for adjacent work that's better handled there.
- `api-development` skill — for adjacent work that's better handled there.
- `mobile-development` skill — for adjacent work that's better handled there.
