# DevOps & Infrastructure — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | IaC plan reviewed — `terraform plan` or `pulumi preview` matches intent. | pass / fail / n/a |
| 2 | Pipeline runs from a clean clone in CI. | pass / fail / n/a |
| 3 | Rollback rehearsed against staging. | pass / fail / n/a |
| 4 | Trace shows up in observability tool for a real request. | pass / fail / n/a |
| 5 | Alert rule fires on injected fault. | pass / fail / n/a |
| 6 | Secrets never appear in logs or build output. | pass / fail / n/a |

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
