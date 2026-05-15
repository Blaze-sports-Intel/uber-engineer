# Mobile Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/mobile a11y-audit ios Sources/Checkout
```

```
/mobile testflight-prep --build=42
```

```
/mobile offline-strategy src/features/cart
```

The `/uber` router will dispatch to `/mobile` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Build a saved-items list for the iOS app."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Pick native SwiftUI (single platform), define the offline-first sync contract (local SQLite is source of truth, server eventual), wire VoiceOver labels with dynamic type support, run on a physical iPhone before claiming done — TestFlight upload only after a clean physical-device pass."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `frontend-development` skill — for adjacent work that's better handled there.
- `api-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
- `security-development` skill — for adjacent work that's better handled there.
