# Test And Quality Assurance — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Snapshot tests over the entire DOM.

**Fix:** Replace whole-DOM snapshots with targeted assertions on the parts of the DOM that matter (specific text, specific structure, specific accessibility properties). Snapshots are for stable outputs you actively review on change.

### E2E tests as the primary defense against regressions.

**Fix:** Push the test pyramid base wider: more unit + integration tests, fewer E2E. Aim for 70% unit, 25% integration/contract, 5% E2E. E2E catches real-browser issues, not business logic bugs.

### Coverage as a target instead of a signal.

**Fix:** Stop reporting overall coverage as a metric. Instead, set per-directory thresholds tied to risk. Block merges when critical paths drop below their threshold. Don't chase 100%.

### Tests that pass only when run alone.

**Fix:** Find the shared state: a global, a singleton, a database row not cleaned up, a port not released. Add `beforeEach` cleanup or use the test runner's isolation primitives (Vitest `--isolate`, Jest `--runInBand`). Run the suite in shuffled order in CI.

### Mocking the system under test.

**Fix:** Mock the boundaries (network, time, filesystem), not the thing you're testing. If the thing under test is hard to test without mocks, the design needs to change — usually pull the side effect out of the unit.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
