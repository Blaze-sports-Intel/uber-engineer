# Mobile Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Builds and launches on a physical iOS device + physical Android device. | pass / fail / n/a |
| 2 | TestFlight build passes Apple's automated checks. | pass / fail / n/a |
| 3 | VoiceOver and TalkBack pass for changed flows. | pass / fail / n/a |
| 4 | Offline mode: app loads cached data, queues writes, syncs on reconnect. | pass / fail / n/a |
| 5 | Crash-free session rate ≥ 99.5% in the last release. | pass / fail / n/a |

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
