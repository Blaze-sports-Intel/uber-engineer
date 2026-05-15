# AI/ML Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Eval suite passes against current + previous model version. | pass / fail / n/a |
| 2 | Inference latency within SLA on the target hardware. | pass / fail / n/a |
| 3 | Cost forecast at expected QPS within budget. | pass / fail / n/a |
| 4 | Outputs reviewed for PII leakage and policy violations. | pass / fail / n/a |
| 5 | Rollback rehearsed by switching the version pin. | pass / fail / n/a |

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
