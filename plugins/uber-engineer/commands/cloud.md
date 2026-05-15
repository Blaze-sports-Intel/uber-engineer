---
description: Cloud Development — invoke the cloud-development skill with focused intent.
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

# /uber:cloud

Invoke the **cloud-development** skill for a Cloud Development task.

## Usage

```
/uber:cloud $ARGUMENTS
```

Common patterns:

- `/uber:cloud iam-review aws/policies/api.json`
- `/uber:cloud env-diff staging prod`
- `/uber:cloud coldstart-budget worker:api`

## What this command does

1. Loads the `cloud-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

AWS, Lambda, S3, DynamoDB, EventBridge, GCP, Cloud Run, Firebase, Azure Functions, Cloudflare Workers, D1, KV, R2, Durable Objects, Vercel, Netlify, Fly.io, Render, serverless, edge runtime, cold start.
