# Database Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/db design-schema --feature=billing
```

```
/db migration-review supabase/migrations/0042_orders.sql
```

```
/db query-plan 'select * from orders where ...'
```

The `/uber` router will dispatch to `/db` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Add an `archived_at` column to the orders table."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Write a reversible migration: ALTER TABLE … ADD COLUMN archived_at TIMESTAMPTZ NULL with no default (avoids rewrite on Postgres), partial index `WHERE archived_at IS NULL`, EXPLAIN ANALYZE on the affected queries before and after, lock duration estimate against a prod-like snapshot, and a `down` that drops the column safely."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `backend-development` skill — for adjacent work that's better handled there.
- `data-science-development` skill — for adjacent work that's better handled there.
- `security-development` skill — for adjacent work that's better handled there.
