---
description: Full-Stack Development — invoke the full-stack-development skill with focused intent.
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

# /uber:fullstack

Invoke the **full-stack-development** skill for a Full-Stack Development task.

## Usage

```
/uber:fullstack $ARGUMENTS
```

Common patterns:

- `/uber:fullstack ship-feature 'add saved search to product index'`
- `/uber:fullstack vertical-slice src/features/checkout`
- `/uber:fullstack flag-rollout new-onboarding --percent=10`

## What this command does

1. Loads the `full-stack-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

full-stack, fullstack, end-to-end feature, ship a feature, Next.js full-stack, Remix, SvelteKit, Nuxt, tRPC, T3 stack, Astro, Hono, monorepo, Turborepo, Nx.
