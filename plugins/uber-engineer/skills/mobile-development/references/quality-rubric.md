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

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- Builds and launches on a physical iOS device + physical Android device.
- Online: feature works against staging API.
- Offline: cached data renders, writes queue, sync resumes on reconnect.
- Background: push wakes the app, deep link routes to the correct screen.
- Accessibility: VoiceOver + TalkBack pass for the new flow.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
