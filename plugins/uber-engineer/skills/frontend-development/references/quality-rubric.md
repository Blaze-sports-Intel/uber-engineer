# Frontend Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Unit and component tests pass (Vitest/Jest + RTL). | pass / fail / n/a |
| 2 | axe-core scan returns zero violations on changed surfaces. | pass / fail / n/a |
| 3 | Lighthouse or web-vitals report meets the budget (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1). | pass / fail / n/a |
| 4 | Visual regression diff approved or unchanged. | pass / fail / n/a |
| 5 | Cross-browser smoke pass: Chrome, Safari, Firefox. | pass / fail / n/a |
| 6 | Manual keyboard-only walkthrough of the new path. | pass / fail / n/a |

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
