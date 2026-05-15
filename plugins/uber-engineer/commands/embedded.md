---
description: Embedded Systems Development — invoke the embedded-systems-development skill with focused intent.
argument-hint: <action> [target] [flags]
allowed-tools:
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Bash
  - Task
---

# /uber:embedded

Invoke the **embedded-systems-development** skill for a Embedded Systems Development task.

## Usage

```
/uber:embedded $ARGUMENTS
```

Common patterns:

- `/uber:embedded memory-map firmware.elf`
- `/uber:embedded isr-budget --target=20us`
- `/uber:embedded ota-plan --hw=esp32s3`

## What this command does

1. Loads the `embedded-systems-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

embedded, microcontroller, MCU, Arduino, ESP32, STM32, Raspberry Pi Pico, RP2040, RTOS, FreeRTOS, Zephyr, bare metal, firmware, HAL, DMA, interrupt, ISR, cross-compile, linker script, no_std.
