# Cloud Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/cloud iam-review aws/policies/api.json
```

```
/cloud env-diff staging prod
```

```
/cloud coldstart-budget worker:api
```

The `/uber` router will dispatch to `/cloud` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Move the image upload pipeline off a VM."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Architect on platform primitives: client uploads directly to R2/S3 with a presigned URL (no proxy through compute), event triggers a Worker/Lambda that resizes via a Browser/Image binding, output goes to a CDN-fronted bucket — IAM scoped to the specific bucket prefix, cost forecast at 100x today's volume, cold-start budget under 100ms p95."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `devops-and-infrastructure` skill — for adjacent work that's better handled there.
- `backend-development` skill — for adjacent work that's better handled there.
- `security-development` skill — for adjacent work that's better handled there.
