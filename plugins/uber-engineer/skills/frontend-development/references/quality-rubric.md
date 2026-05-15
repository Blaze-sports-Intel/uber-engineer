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

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Loading state renders without layout shift.
- Empty state explains why there's no data, not just a blank screen.
- Error state shows what failed and whether it's transient.
- Populated state matches the design and meets the perf budget.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
