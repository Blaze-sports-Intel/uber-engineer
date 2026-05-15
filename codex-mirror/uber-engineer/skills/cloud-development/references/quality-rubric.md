# Cloud Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Deploy to staging matches prod config except for secrets and region. | pass / fail / n/a |
| 2 | IAM review passes — no wildcards, no unused permissions. | pass / fail / n/a |
| 3 | Cold start P99 within budget on the smallest config. | pass / fail / n/a |
| 4 | Budget alert wired and tested with a synthetic spike. | pass / fail / n/a |
| 5 | Failover rehearsed against a region-down simulation. | pass / fail / n/a |

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
