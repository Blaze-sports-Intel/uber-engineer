# Test & Quality Assurance — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Test suite passes from a clean clone with no manual setup. | pass / fail / n/a |
| 2 | Mutation score above the agreed threshold on critical modules. | pass / fail / n/a |
| 3 | Contract tests pass against the latest provider version. | pass / fail / n/a |
| 4 | Flake rate below the agreed budget over the last N runs. | pass / fail / n/a |
| 5 | Visual regression diffs reviewed, not auto-accepted. | pass / fail / n/a |

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
