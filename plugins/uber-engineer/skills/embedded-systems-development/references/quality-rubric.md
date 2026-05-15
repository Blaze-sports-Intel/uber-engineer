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

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Builds reproducibly from a clean clone with pinned toolchain.
- Boot: device starts cleanly, peripherals initialize.
- Active: workload runs at expected throughput within latency budget.
- Sleep: average current matches battery-budget target on the actual hardware.
- Fault: watchdog resets, OTA can recover, last-known-good image rolls back.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
