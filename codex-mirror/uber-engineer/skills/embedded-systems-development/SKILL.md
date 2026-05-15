---
name: embedded-systems-development
description: C/C++/Rust on microcontrollers, RTOS, memory limits, hardware abstraction, and cross-compiling. Use when the user mentions: embedded, microcontroller, MCU, Arduino, ESP32, STM32, Raspberry Pi Pico, RP2040, RTOS, FreeRTOS, Zephyr, bare metal, firmware, HAL, DMA, interrupt, ISR, cross-compile, linker script, no_std. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: Linux server work (use backend-development or devops); general C/C++ programming on desktop.
---

# Embedded Systems Development

C/C++/Rust on microcontrollers, RTOS, memory limits, hardware abstraction, and cross-compiling.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: embedded, microcontroller, MCU, Arduino, ESP32, STM32, Raspberry Pi Pico, RP2040, RTOS, FreeRTOS, Zephyr, bare metal, firmware, HAL, DMA, interrupt, ISR, cross-compile, linker script, no_std.

Use when the user wants any of:

- Pick the right MCU + RTOS + toolchain for the constraints.
- Layout memory: flash, RAM, stack, heap (or no heap).
- Write ISRs that respect latency budgets and don't allocate.
- Configure DMA and peripherals through HAL or registers.
- Cross-compile, flash, and debug over SWD/JTAG.
- Handle power: sleep modes, wake sources, battery budget.

## When NOT to use this skill

- Linux server work (use backend-development or devops)
- general C/C++ programming on desktop

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

- BOM with MCU + peripherals + estimated cost.
- Memory map: text/data/bss/stack/heap allocations.
- Interrupt latency budget per ISR.
- Power budget per mode (active/idle/sleep/deep sleep).
- Bootloader + OTA update plan.
- Hardware-in-the-loop test rig spec.

## Anti-patterns this skill pushes back against

- malloc/new on a memory-constrained MCU.
- Heavy work inside ISRs.
- Blocking sleeps in cooperative schedulers.
- Toolchain versions undocumented; build only works on one machine.
- OTA without rollback to the last-known-good image.

## Verification required before claiming done

- Builds reproducibly from a clean clone with pinned toolchain.
- Flashed image runs on hardware, not just emulator.
- Worst-case stack usage measured, not estimated.
- OTA path rehearsed including rollback.
- Power measurement matches budget within tolerance.

## Suggested commands

- `/uber:embedded memory-map firmware.elf`
- `/uber:embedded isr-budget --target=20us`
- `/uber:embedded ota-plan --hw=esp32s3`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user can see the correct output of this work. Build success, deploy success, and 200
responses do not equal done. Every data surface explicitly handles loading, error, empty, and
populated states. Verification actually happened — no claim of "verified" without evidence.
