# AR/VR Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/xr frame-budget --hz=90
```

```
/xr spatial-ux scene-anchors
```

```
/xr comfort-settings
```

The `/uber` router will dispatch to `/xr` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Add a hand-tracked menu to the visionOS app."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Anchor the menu to a comfort-zone position 0.6m in front of the user, design the gaze + pinch interaction with a 250ms dwell, fall back to controller pinch when hand tracking is lost, hold 90Hz over a 5-minute gameplay slice on a real Vision Pro, and surface privacy disclosures for hand + room data on first launch."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `game-development` skill — for adjacent work that's better handled there.
- `mobile-development` skill — for adjacent work that's better handled there.
- `frontend-development` skill — for adjacent work that's better handled there.
