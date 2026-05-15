---
name: database-development
description: Schema design, migration safety, indexing, query review, and read-only-by-default access. Use when the user mentions: database, schema, migration, Postgres, MySQL, SQLite, MongoDB, Redis, Supabase, CockroachDB, PlanetScale, DynamoDB, index, query plan, EXPLAIN, RLS, row-level security, RBAC, partition, sharding. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: application-layer caching strategy without persistence change (use backend-development); data analysis / visualization (use data-science-development).
---

# Database Development

Schema design, migration safety, indexing, query review, and read-only-by-default access.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: database, schema, migration, Postgres, MySQL, SQLite, MongoDB, Redis, Supabase, CockroachDB, PlanetScale, DynamoDB, index, query plan, EXPLAIN, RLS, row-level security, RBAC, partition, sharding.

Use when the user wants any of:

- Design normalized schemas, then denormalize deliberately for read patterns.
- Write migrations that are reversible, online, and lock-aware.
- Read query plans and add the right index, not 'add an index everywhere'.
- Apply row-level security or equivalent at the database, not just the app.
- Plan partitioning and archival before tables get hot.
- Default to read-only DB access; require explicit approval for writes.

## When NOT to use this skill

- application-layer caching strategy without persistence change (use backend-development)
- data analysis / visualization (use data-science-development)

## Workflow

1. **Intake.** Read the user intent. Identify which capability above applies. If the request crosses
   into another discipline (e.g. UI + DB), call the `discipline-router` agent before splitting work.
2. **Inspect.** Look at the actual repo state with Read/Grep/Glob before proposing changes. Do not
   assume what code exists from project name alone.
3. **Source-check.** For non-obvious technical claims, ground the answer in the official sources
   listed in `references/official-sources.md`. Use the Context7 MCP for live doc lookups instead of
   relying on training-data memory for fast-moving APIs.
4. **Produce.** Generate the appropriate artifact from the list below.
5. **Verify.** Run every verification layer below before claiming done. Build success is not done.
   200 responses are not done. A real user seeing correct output is done.
6. **Hand back.** Report what shipped, what the visitor sees, what changed. No file paths, function
   names, or engineering jargon unprompted.

## Artifacts this skill produces

- Schema diagram (ERD) + dbml/Prisma/SQL source.
- Migration file: up, down, lock impact estimate, online strategy.
- Index plan: query → index → expected plan.
- RLS policy set with positive + negative test cases.
- Backup, restore, and PITR rehearsal log.
- Slow query report with proposed fixes.

## Anti-patterns this skill pushes back against

- ALTER TABLE on a big table during peak without `CONCURRENTLY`.
- SELECT * in production code paths.
- Soft-delete columns without a partial index.
- Foreign keys without indexes on the referencing column.
- Migrations that work locally but lock prod for minutes.
- Backups never tested with a restore.

## Verification required before claiming done

- Migration up + down both pass on a prod-like snapshot.
- EXPLAIN ANALYZE shows expected index usage.
- RLS tests cover allow + deny paths.
- Restore from latest backup completes in under target RTO.
- Slow query log clean after the change.

## Suggested commands

- `/uber:db design-schema --feature=billing`
- `/uber:db migration-review supabase/migrations/0042_orders.sql`
- `/uber:db query-plan 'select * from orders where ...'`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user can see the correct output of this work. Build success, deploy success, and 200
responses do not equal done. Every data surface explicitly handles loading, error, empty, and
populated states. Verification actually happened — no claim of "verified" without evidence.
