# Game Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/game profile-frame
```

```
/game asset-pipeline --type=texture
```

```
/game save-migration v3 -> v4
```

The `/uber` router will dispatch to `/game` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Make the game run smoother."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Capture a frame on min-spec hardware, identify the top three contributors to frame time (likely allocations, draw calls, or texture bandwidth), fix the heaviest one, re-capture — hold 16.6ms at 60fps with no GC stall over 5 minutes of gameplay."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `frontend-development` skill — for adjacent work that's better handled there.
- `ar-vr-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
