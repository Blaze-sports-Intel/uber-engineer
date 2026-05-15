# Security Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Threat model reviewed before launch by a second engineer. | pass / fail / n/a |
| 2 | SAST + SCA gates pass with no unresolved highs. | pass / fail / n/a |
| 3 | Pen test or red-team exercise scheduled before significant launches. | pass / fail / n/a |
| 4 | Tabletop incident exercise run at least once per quarter. | pass / fail / n/a |
| 5 | Secret rotation rehearsed end-to-end. | pass / fail / n/a |

## Definition of done

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Threat model reviewed before launch by a second engineer.
- SAST + SCA gates pass with no unresolved highs.
- Pen test or red-team exercise scheduled before significant launches.
- Tabletop incident exercise run at least once per quarter.
- Secret rotation rehearsed end-to-end.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
