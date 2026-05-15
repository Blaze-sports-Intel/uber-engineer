# Web Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Lighthouse on the top 5 routes meets budget. | pass / fail / n/a |
| 2 | Sitemap + robots + canonical correct on production. | pass / fail / n/a |
| 3 | Preview URL renders the change before merge. | pass / fail / n/a |
| 4 | Web-vitals dashboard wired and showing data. | pass / fail / n/a |
| 5 | Error reporting catches a synthetic exception. | pass / fail / n/a |

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
