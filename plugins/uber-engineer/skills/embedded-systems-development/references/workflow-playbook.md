# Embedded Systems Development — Workflow Playbook

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

- **Pick the right MCU + RTOS + toolchain for the constraints.** → BOM with MCU + peripherals + estimated cost, plus a stack decision record.
- **Layout memory: flash, RAM, stack, heap (or no heap).** → Memory map: text/data/bss/stack/heap allocations, with worst-case usage measurements.
- **Write ISRs that respect latency budgets and don't allocate.** → Interrupt latency budget per ISR, with measured timings on hardware.
- **Configure DMA and peripherals through HAL or registers.** → Peripheral configuration spec: DMA channels, clock tree, pin muxing, validated against the silicon errata.
- **Cross-compile, flash, and debug over SWD/JTAG.** → Reproducible build script with pinned toolchain version, plus a flashing + debug recipe (OpenOCD config, probe model, target voltage).
- **Handle power: sleep modes, wake sources, battery budget.** → Power budget per mode (active/idle/sleep/deep sleep), plus a bootloader + OTA update plan and the hardware-in-the-loop test rig spec.

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
