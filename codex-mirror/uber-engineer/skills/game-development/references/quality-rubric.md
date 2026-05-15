# Game Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Frame time meets budget on min-spec hardware. | pass / fail / n/a |
| 2 | Asset bundle size within target. | pass / fail / n/a |
| 3 | Save/load roundtrips cleanly between versions N-1 and N. | pass / fail / n/a |
| 4 | Input works on gamepad, keyboard, touch. | pass / fail / n/a |
| 5 | Build succeeds on every target platform in CI. | pass / fail / n/a |

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
