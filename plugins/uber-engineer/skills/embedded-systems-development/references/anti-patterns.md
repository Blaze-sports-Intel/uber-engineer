# Embedded Systems Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### malloc/new on a memory-constrained MCU.

**Fix:** Replace dynamic allocation with statically-sized buffers, fixed-capacity pools, or stack allocation with measured high-water marks. Audit with `--no-allow-multiple-definition` and disable the heap entirely on platforms where it's optional.

### Heavy work inside ISRs.

**Fix:** Keep the ISR to: read the peripheral register, set a flag or post to a queue, exit. Do the work in a task context. Measure ISR duration with a GPIO-toggle + scope to confirm under the latency budget.

### Blocking sleeps in cooperative schedulers.

**Fix:** Replace `sleep_ms()` with a timer-based wake or a yield to the scheduler. In bare-metal cooperative loops, structure tasks as state machines that return after each step.

### Toolchain versions undocumented; build only works on one machine.

**Fix:** Pin the toolchain in a manifest (PlatformIO `platform_packages`, Zephyr `west`, esp-idf `idf-version`). Containerize the build (Docker + the pinned toolchain). Add a CI build that flashes a smoke image to a hardware-in-the-loop board.

### OTA without rollback to the last-known-good image.

**Fix:** Implement A/B partition or active/inactive slots. Boot loader marks an image 'pending', the application marks it 'confirmed' after a health check (e.g., successful sensor read). If never confirmed, next boot rolls back. Test the rollback path explicitly.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
