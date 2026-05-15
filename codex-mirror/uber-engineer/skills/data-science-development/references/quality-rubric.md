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

- A real user sees the correct output of this work.
- Loading, error, empty, populated states all render correctly.
- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but production behavior is wrong.
- Build is green but the visible surface is empty/broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
