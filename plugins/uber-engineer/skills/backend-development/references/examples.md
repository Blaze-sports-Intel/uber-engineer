# Backend Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/backend design-endpoint POST /v1/orders
```

```
/backend auth-flow oauth2-pkce
```

```
/backend ratelimit /v1/checkout --tier=premium
```

The `/uber` router will dispatch to `/backend` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Add an endpoint for refunds."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Define POST /v1/refunds with idempotency-key header, structured error catalog (refund_already_processed, payment_not_found, expired), p95 latency budget under 250ms, end-to-end auth check on the server (not just the UI), and a runbook for the failure modes — then write the contract test before the handler."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `api-development` skill — for adjacent work that's better handled there.
- `database-development` skill — for adjacent work that's better handled there.
- `cloud-development` skill — for adjacent work that's better handled there.
- `security-development` skill — for adjacent work that's better handled there.
