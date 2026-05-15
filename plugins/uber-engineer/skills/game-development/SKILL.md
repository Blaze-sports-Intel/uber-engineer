---
name: game-development
description: "Engine architecture, gameplay systems, performance budgets, and asset pipelines. Use when the user mentions: game, Unity, Unreal, Godot, Phaser, Three.js, React Three Fiber, Bevy, ECS, frame budget, draw call, asset pipeline, shader, physics, input system, save system, sprite, GLTF, GLB. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: pure data-viz that isn't a game (use frontend-development or data-science-development); video editing pipelines without runtime simulation."
---

# Game Development

Engine architecture, gameplay systems, performance budgets, and asset pipelines.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: game, Unity, Unreal, Godot, Phaser, Three.js, React Three Fiber, Bevy, ECS, frame budget, draw call, asset pipeline, shader, physics, input system, save system, sprite, GLTF, GLB.

Use when the user wants any of:

- Design a deterministic game loop with fixed update + variable render.
- Profile and meet a frame budget (16.6ms at 60fps, 8.3ms at 120fps).
- Build asset pipelines: import → optimize → atlas/pack → ship.
- Implement input abstraction that supports gamepad, keyboard, touch, and accessibility devices.
- Apply ECS or component patterns appropriate to the engine.
- Wire save/load with version migration from day one.

## When NOT to use this skill

- pure data-viz that isn't a game (use frontend-development or data-science-development)
- video editing pipelines without runtime simulation

## Workflow

1. **Intake.** Read the user intent. Identify which capability above applies. If the request crosses
   into another discipline (e.g. UI + DB), call the `discipline-router` agent before splitting work.
2. **Inspect.** Look at the actual repo state with Read/Grep/Glob before proposing changes. Do not
   assume what code exists from project name alone.
3. **Source-check.** For non-obvious technical claims, ground the answer in the official sources
   listed in `references/official-sources.md`. Use the Context7 MCP for live doc lookups instead of
   relying on training-data memory for fast-moving APIs.
4. **Produce.** Generate the appropriate artifact from the list below.
5. **Verify.** Run every verification layer below before claiming done. Build success is not done.
   200 responses are not done. A real user seeing correct output is done.
6. **Hand back.** Report what shipped, what the visitor sees, what changed. No file paths, function
   names, or engineering jargon unprompted.

## Artifacts this skill produces

- Frame budget breakdown: CPU update, GPU render, IO, gc.
- Asset import preset for each asset type.
- Input remap UI with default + customized bindings.
- Save-file schema with version number and migration path.
- Profiler capture annotated with hot spots.
- Build matrix: dev, profile, release for each target platform.

## Anti-patterns this skill pushes back against

- Per-frame allocations causing GC stalls in managed engines.
- Uncompressed textures shipped to release.
- Hardcoded keys without rebinding support.
- Save files with no version field — first migration breaks every player.
- Physics tick coupled to render rate, making gameplay frame-rate-dependent.

## Verification required before claiming done

- Frame time meets budget on min-spec hardware.
- Asset bundle size within target.
- Save/load roundtrips cleanly between versions N-1 and N.
- Input works on gamepad, keyboard, touch.
- Build succeeds on every target platform in CI.

## Suggested commands

- `/game profile-frame`
- `/game asset-pipeline --type=texture`
- `/game save-migration v3 -> v4`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below must all hold:

- Frame budget met on min-spec hardware over a 5-minute gameplay slice.
- Asset bundle size within target platform limits.
- Save/load roundtrips between schema versions N-1 and N.
- Input works on gamepad, keyboard, and touch with rebinding.
- Build succeeds on every target platform in CI.

Verification actually happened — no claim of "verified" without evidence.
