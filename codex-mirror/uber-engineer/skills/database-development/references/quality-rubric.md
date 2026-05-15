# Database Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Migration up + down both pass on a prod-like snapshot. | pass / fail / n/a |
| 2 | EXPLAIN ANALYZE shows expected index usage. | pass / fail / n/a |
| 3 | RLS tests cover allow + deny paths. | pass / fail / n/a |
| 4 | Restore from latest backup completes in under target RTO. | pass / fail / n/a |
| 5 | Slow query log clean after the change. | pass / fail / n/a |

## Definition of done

- A real user sees the correct output of this work.
- Loading, error, empty, populated states all render correctly.
- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but production behavior is wrong.
- Build is green but the visible surface is empty/broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
