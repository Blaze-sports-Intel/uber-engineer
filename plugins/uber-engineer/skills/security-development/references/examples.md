# Security Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/security threat-model --surface=payments
```

```
/security sast-triage
```

```
/security secret-rotation --provider=stripe
```

The `/uber` router will dispatch to `/security` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Make the new payments flow secure."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Run STRIDE on the payments surface (assets: card data, payout accounts; actors: customer, merchant, attacker; threats: spoofing → strong auth, tampering → signed requests, repudiation → audit log, info disclosure → field-level encryption, DoS → rate limit, elevation → least-privilege scopes), wire SAST + secret scan + dependency audit into CI with a one-week SLA on highs, and tabletop the breach-response runbook before launch."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `backend-development` skill — for adjacent work that's better handled there.
- `api-development` skill — for adjacent work that's better handled there.
- `cloud-development` skill — for adjacent work that's better handled there.
- `devops-and-infrastructure` skill — for adjacent work that's better handled there.
