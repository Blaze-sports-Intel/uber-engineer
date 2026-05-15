# Embedded Systems Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Builds reproducibly from a clean clone with pinned toolchain. | pass / fail / n/a |
| 2 | Flashed image runs on hardware, not just emulator. | pass / fail / n/a |
| 3 | Worst-case stack usage measured, not estimated. | pass / fail / n/a |
| 4 | OTA path rehearsed including rollback. | pass / fail / n/a |
| 5 | Power measurement matches budget within tolerance. | pass / fail / n/a |

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
