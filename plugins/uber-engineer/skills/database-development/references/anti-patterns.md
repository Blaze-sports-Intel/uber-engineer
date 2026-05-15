# Database Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### ALTER TABLE on a big table during peak without `CONCURRENTLY`.

**Fix:** Use Postgres's `ALTER TABLE … ADD COLUMN` without DEFAULT (no rewrite), `CREATE INDEX CONCURRENTLY`, and `VALIDATE CONSTRAINT NOT VALID` patterns. On MySQL use `ALGORITHM=INPLACE, LOCK=NONE` where supported. Schedule destructive changes for low-traffic windows.

### SELECT * in production code paths.

**Fix:** List the columns explicitly. SELECT * forces wider scans, breaks when the schema adds columns, and ships unintended data. The ORM equivalents (Prisma `select`, Sequelize `attributes`) are mandatory in hot paths.

### Soft-delete columns without a partial index.

**Fix:** Add a partial index on the active rows: `CREATE INDEX … ON table (key_columns) WHERE deleted_at IS NULL`. Otherwise the index covers tombstones and the query plan stays slow.

### Foreign keys without indexes on the referencing column.

**Fix:** Add an index on every FK column. Without it, deletes on the parent table take a sequential scan of the child — the #3 cause of mysterious latency spikes during cleanup jobs.

### Migrations that work locally but lock prod for minutes.

**Fix:** Test on a snapshot of prod (anonymized if needed). Use `pg_locks` or equivalent to measure lock duration. For locks > 100ms on a hot table, use a multi-step strategy (add nullable, backfill in batches, add NOT NULL constraint).

### Backups never tested with a restore.

**Fix:** Schedule a quarterly restore rehearsal: pull the latest backup, restore to a sandbox, run a sanity query, document RTO. A backup that hasn't been restored isn't a backup.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
