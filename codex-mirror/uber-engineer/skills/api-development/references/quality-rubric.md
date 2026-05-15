# API Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | OpenAPI lint passes (Spectral or vacuum) with zero errors. | pass / fail / n/a |
| 2 | Backward compatibility check against the previous minor version is clean. | pass / fail / n/a |
| 3 | Webhook receiver rejects unsigned + replayed payloads. | pass / fail / n/a |
| 4 | Generated SDK compiles and round-trips a request. | pass / fail / n/a |
| 5 | Public docs site renders the spec without warnings. | pass / fail / n/a |

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
