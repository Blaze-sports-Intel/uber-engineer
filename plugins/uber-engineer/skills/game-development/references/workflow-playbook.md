# Game Development — Workflow Playbook

This is the long-form companion to `SKILL.md`. Load when you need the detailed step-by-step.

## Phase 1 — Intake (5 minutes)

Ask once, then commit. Do not pile up clarifying questions.

1. What's the surface? (route, file, service, model, contract, schema, scene, etc.)
2. What does "done" look like for this discipline? (See the definition-of-done states in `quality-rubric.md`.)
3. What does the existing code look like? Read before you propose.
4. Is there a deadline or constraint that changes the strategy?

If the user request crosses disciplines, call `discipline-router` first.

## Phase 2 — Source crawl

For any non-trivial technical claim:

1. Call Context7 MCP first for live docs.
2. Check the relevant entries in `official-sources.md`.
3. If a community blog is the only source, label the claim as "non-authoritative".

Never write API syntax from memory for SDKs that change quickly. Always check version.

## Phase 3 — Plan

Write a 5-10 line plan before touching files. Include:

- The exact change and where.
- The verification you'll run.
- The rollback if it goes wrong.

## Phase 4 — Execute

Match the capability to the artifact:

- **Design a deterministic game loop with fixed update + variable render.** → Loop architecture spec: fixed-step physics rate, render interpolation policy, input sampling cadence.
- **Profile and meet a frame budget (16.6ms at 60fps, 8.3ms at 120fps).** → Frame budget breakdown: CPU update, GPU render, IO, GC, plus the profiler capture annotated with hot spots.
- **Build asset pipelines: import → optimize → atlas/pack → ship.** → Asset import preset for each asset type (texture, mesh, audio, animation).
- **Implement input abstraction that supports gamepad, keyboard, touch, and accessibility devices.** → Input remap UI with default + customized bindings.
- **Apply ECS or component patterns appropriate to the engine.** → Component / system architecture diagram with data ownership and update order.
- **Wire save/load with version migration from day one.** → Save-file schema with version number and migration path, plus a build matrix (dev, profile, release) for each target platform.

## Phase 5 — Verify

Every item in `SKILL.md` § "Verification required before claiming done" must pass. Capture evidence —
log line, screenshot, test output, profiler trace, scope reading, signed transaction hash, whatever
counts as proof in this discipline. Don't claim verification you didn't do.

## Phase 6 — Hand back

Tell the user:

- What shipped (in user terms, not file paths).
- What's now true that wasn't before (visible behavior, capacity, posture).
- What still needs attention, with severity.

No "great question," no apology preambles, no transformation arcs.

## Edge cases

- Repo state surprises: stop and ask, don't paper over.
- Conflicting docs: follow the most recent official source, log the conflict.
- Deadline pressure: shrink scope, never shrink verification.
- Cross-discipline scope creep: hand back to `discipline-router`.
