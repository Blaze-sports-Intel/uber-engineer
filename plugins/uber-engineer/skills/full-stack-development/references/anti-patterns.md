# Full Stack Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Frontend types drifting from backend reality — duplicated, hand-maintained interfaces.

**Fix:** Pick one source of truth (Zod schema, OpenAPI spec, GraphQL SDL, tRPC router) and generate the rest. Add a CI gate that regenerates types on every PR and fails if the diff isn't committed.

### API surface designed around UI screens instead of domain operations.

**Fix:** Refactor endpoints to model domain operations (createOrder, refundLine, cancelSubscription). UI composes these — never the other way around. Screens that need 5 endpoints stay 5 endpoints.

### Auth checked in the UI but not on the server.

**Fix:** Move every authorization check to the server-side handler. UI hides routes for UX, but the server enforces. Add a contract test that hits the endpoint without a valid token and asserts 401/403.

### Shipping a feature without an empty state, error state, or loading state.

**Fix:** Add the missing states explicitly. Loading is a skeleton that matches the shape. Empty explains why. Error names what failed and whether it's transient. Never ship a `?:` that renders `null`.

### Big-bang migrations with no rollback path.

**Fix:** Split into dual-write phase (write old + new), backfill phase (catch up old data), dual-read phase (verify new matches old), cut-over phase (read from new), cleanup phase (drop old). Every phase is reversible; only the final cleanup is one-way.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
