# Embedded Systems Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/embedded memory-map firmware.elf
```

```
/embedded isr-budget --target=20us
```

```
/embedded ota-plan --hw=esp32s3
```

The `/uber` router will dispatch to `/embedded` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Wake the device on an external pin and read a sensor."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Configure the GPIO as a wake source, drop into deep sleep with the RTC kept alive, wake → enable peripheral clock → DMA the sensor read → log to flash → re-sleep — all within the 50µs ISR budget and 30µA average current draw measured on the actual board."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `security-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
