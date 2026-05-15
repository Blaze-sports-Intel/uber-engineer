# Full-Stack Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Type check passes across the whole monorepo. | pass / fail / n/a |
| 2 | Contract tests align frontend expectations with backend reality. | pass / fail / n/a |
| 3 | Playwright/Cypress E2E covers the happy path + one failure path. | pass / fail / n/a |
| 4 | Feature flag toggles cleanly without redeploy. | pass / fail / n/a |
| 5 | Empty/loading/error/populated all render correctly. | pass / fail / n/a |

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
