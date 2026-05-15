# Test And Quality Assurance — Quality Rubric

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

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Suite passes from a clean clone with no manual setup.
- Mutation score above the agreed threshold on critical modules.
- Contract tests pass against the latest provider version.
- Flake rate below the agreed budget over the last N runs.
- Visual regression diffs reviewed, not auto-accepted.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
