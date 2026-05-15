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

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Staging matches prod config except for secrets and region.
- IAM review passes — no wildcards, no unused permissions.
- Cold start P99 within budget on the smallest config.
- Budget alert wired and tested with a synthetic spike.
- Failover rehearsed against a region-down simulation.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
