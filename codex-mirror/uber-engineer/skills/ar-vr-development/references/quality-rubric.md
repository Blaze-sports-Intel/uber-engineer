# AR/VR Development — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | Tested on a physical headset, not just simulator. | pass / fail / n/a |
| 2 | Frame rate stays at platform target for 5+ minutes. | pass / fail / n/a |
| 3 | Comfort options available in settings and exposed early. | pass / fail / n/a |
| 4 | Privacy disclosures complete: camera, hand, eye, room data. | pass / fail / n/a |
| 5 | Store review checklist signed off. | pass / fail / n/a |

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
