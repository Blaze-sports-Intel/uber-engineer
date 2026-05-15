# Game Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Per-frame allocations causing GC stalls in managed engines.

**Fix:** Pool the allocations: pre-allocate the worst-case count at scene load, reuse instances. Replace LINQ / list-comprehensions in hot paths with explicit loops. Profile with the GC monitor to confirm zero allocations per frame.

### Uncompressed textures shipped to release.

**Fix:** Set the import preset for each texture to use the platform-appropriate compression (BCn on PC, ASTC on mobile, ETC2 fallback). Add a CI check that scans the build for any uncompressed texture larger than 256x256.

### Hardcoded keys without rebinding support.

**Fix:** Route all input through an action map (Unity Input System actions, Unreal InputAction, Godot InputMap). Add a settings UI that lists actions with their current binding and accepts user remap.

### Save files with no version field — first migration breaks every player.

**Fix:** Add `schema_version: int` to the save header now, even at v1. Write a migration framework that loads the version, runs migrations in order, and writes the latest version on save. Test by loading a v1 save in a build with v2 schema.

### Physics tick coupled to render rate, making gameplay frame-rate-dependent.

**Fix:** Decouple: physics runs at a fixed step (e.g., 50Hz), render interpolates between the last two physics states. Test by running the game at 30fps, 60fps, and 144fps — gameplay should produce the same outcome.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
