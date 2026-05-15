# Full Stack Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/fullstack ship-feature 'add saved search to product index'
```

```
/fullstack vertical-slice src/features/checkout
```

```
/fullstack flag-rollout new-onboarding --percent=10
```

The `/uber` router will dispatch to `/fullstack` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Add a saved-search feature."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Slice it: schema migration adds saved_searches table, server action saves + lists, RSC renders the list with empty/error/loading states, type contract shared via Zod, behind a flag for the first 10% of users with a kill switch and a Playwright happy-path test that runs on every PR."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `frontend-development` skill — for adjacent work that's better handled there.
- `backend-development` skill — for adjacent work that's better handled there.
- `database-development` skill — for adjacent work that's better handled there.
- `api-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
