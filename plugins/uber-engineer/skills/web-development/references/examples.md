# Web Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/web route-table
```

```
/web seo-audit --url=https://example.com
```

```
/web vitals-budget --route=/
```

The `/uber` router will dispatch to `/web` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Make the marketing site faster."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Audit the route table: marketing pages should be SSG with a 30-day stale-while-revalidate, blog posts should be ISR keyed on content updates, the app shell stays SPA. Set per-route LCP and INP budgets, wire web-vitals + RUM at the framework boundary, and gate every PR on a Lighthouse run against the top 5 routes."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `frontend-development` skill — for adjacent work that's better handled there.
- `backend-development` skill — for adjacent work that's better handled there.
- `cloud-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
