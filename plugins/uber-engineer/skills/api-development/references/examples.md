# Api Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/api design-resource users
```

```
/api version-bump --from=v1 --to=v2
```

```
/api webhook-contract subscription.created
```

The `/uber` router will dispatch to `/api` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Add a webhook for order events."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Author the webhook contract first: event types, payload schema with examples, signing scheme (HMAC-SHA256 over body + timestamp, 5-minute replay window), retry schedule with exponential backoff, dead-letter behavior at attempt 8, and a verifier code sample in three languages — then implement the sender against the contract."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `backend-development` skill — for adjacent work that's better handled there.
- `security-development` skill — for adjacent work that's better handled there.
- `full-stack-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
