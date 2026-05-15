---
description: API Development — invoke the api-development skill with focused intent.
argument-hint: <action> [target] [flags]
allowed-tools:
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Bash
  - Task
---

# /uber:api

Invoke the **api-development** skill for a API Development task.

## Usage

```
/uber:api $ARGUMENTS
```

Common patterns:

- `/uber:api design-resource users`
- `/uber:api version-bump --from=v1 --to=v2`
- `/uber:api webhook-contract subscription.created`

## What this command does

1. Loads the `api-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

API design, REST, GraphQL, gRPC, OpenAPI, Swagger, API versioning, deprecation, error schema, RFC 7807, problem details, webhook, pagination, rate limit, API key, OAuth scopes, SDK, API gateway.
