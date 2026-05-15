# Blockchain Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Test coverage on contracts ≥ 95% lines + branches. | pass / fail / n/a |
| 2 | Static analysis reports zero unresolved highs. | pass / fail / n/a |
| 3 | Fork test matches mainnet state assumptions. | pass / fail / n/a |
| 4 | Wallet flow simulation shown to a non-engineer who understands what they're signing. | pass / fail / n/a |
| 5 | Multisig sign-off recorded before mainnet deploy. | pass / fail / n/a |

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
