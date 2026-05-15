# Backend Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Contract tests pass against the OpenAPI spec. | pass / fail / n/a |
| 2 | Auth flow exercised end-to-end with valid + invalid tokens. | pass / fail / n/a |
| 3 | Load test hits target RPS at p95 latency budget. | pass / fail / n/a |
| 4 | Logs/metrics/traces visible in observability stack. | pass / fail / n/a |
| 5 | Idempotency keys verified on retry. | pass / fail / n/a |
| 6 | Security scan (SAST + dependency audit) clean. | pass / fail / n/a |

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
