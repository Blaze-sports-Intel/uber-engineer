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

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Frame budget met on min-spec hardware over a 5-minute gameplay slice.
- Asset bundle size within target platform limits.
- Save/load roundtrips between schema versions N-1 and N.
- Input works on gamepad, keyboard, and touch with rebinding.
- Build succeeds on every target platform in CI.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
