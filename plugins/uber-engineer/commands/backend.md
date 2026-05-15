---
description: Backend Development — invoke the backend-development skill with focused intent.
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

# /uber:backend

Invoke the **backend-development** skill for a Backend Development task.

## Usage

```
/uber:backend $ARGUMENTS
```

Common patterns:

- `/uber:backend design-endpoint POST /v1/orders`
- `/uber:backend auth-flow oauth2-pkce`
- `/uber:backend ratelimit /v1/checkout --tier=premium`

## What this command does

1. Loads the `backend-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

backend, API, REST, GraphQL, server, Node.js, Python, Go, Java, Spring Boot, Express, Fastify, FastAPI, Django, Rails, authentication, authorization, JWT, OAuth, rate limiting, idempotency, caching, queue, background job.
