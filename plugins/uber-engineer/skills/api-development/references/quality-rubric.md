# Api Development — Quality Rubric

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

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Spec lints clean (Spectral / vacuum) with zero errors.
- Backward-compat check against previous minor passes.
- Webhook receiver rejects unsigned + replayed payloads.
- Generated SDK compiles and round-trips a request.
- Public docs site renders the spec without warnings.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
