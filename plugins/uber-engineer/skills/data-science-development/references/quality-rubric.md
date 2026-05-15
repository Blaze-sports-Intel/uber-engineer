# Data Science Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Notebook re-runs end-to-end on a different machine. | pass / fail / n/a |
| 2 | Statistical assumptions documented and checked. | pass / fail / n/a |
| 3 | Dashboard owner + refresh wired into platform. | pass / fail / n/a |
| 4 | Findings reviewed by a second analyst before publishing. | pass / fail / n/a |

## Definition of done

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Notebook re-runs end-to-end on a different machine.
- Statistical assumptions documented and checked.
- Dashboard owner + refresh wired into platform.
- Findings reviewed by a second analyst before publishing.
- Decision memo names the action and the confidence level.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
