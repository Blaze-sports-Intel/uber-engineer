# Devops And Infrastructure — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/devops pipeline-review .github/workflows/deploy.yml
```

```
/devops rollout-plan --strategy=canary --service=api
```

```
/devops runbook --incident=db-failover
```

The `/uber` router will dispatch to `/devops` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Set up CI for the new service."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Define a pipeline that runs lint + typecheck + unit tests in parallel under 5 minutes, blocks merge on red, builds a container image with the commit SHA tagged, deploys to staging on main, and gates prod deploy on a manual approval — with a Terraform plan output as a PR comment for any infra change."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `cloud-development` skill — for adjacent work that's better handled there.
- `backend-development` skill — for adjacent work that's better handled there.
- `security-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
