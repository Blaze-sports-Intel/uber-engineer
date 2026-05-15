---
description: Database Development — invoke the database-development skill with focused intent.
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

# /uber:db

Invoke the **database-development** skill for a Database Development task.

## Usage

```
/uber:db $ARGUMENTS
```

Common patterns:

- `/uber:db design-schema --feature=billing`
- `/uber:db migration-review supabase/migrations/0042_orders.sql`
- `/uber:db query-plan 'select * from orders where ...'`

## What this command does

1. Loads the `database-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

database, schema, migration, Postgres, MySQL, SQLite, MongoDB, Redis, Supabase, CockroachDB, PlanetScale, DynamoDB, index, query plan, EXPLAIN, RLS, row-level security, RBAC, partition, sharding.
