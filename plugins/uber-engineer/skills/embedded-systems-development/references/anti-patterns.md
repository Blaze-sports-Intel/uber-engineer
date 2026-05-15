# Embedded Systems Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### malloc/new on a memory-constrained MCU.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Heavy work inside ISRs.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Blocking sleeps in cooperative schedulers.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Toolchain versions undocumented; build only works on one machine.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### OTA without rollback to the last-known-good image.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
