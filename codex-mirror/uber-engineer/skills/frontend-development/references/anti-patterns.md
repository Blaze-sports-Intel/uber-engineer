# Frontend Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Hard-coded colors instead of design tokens.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Div soup — semantic-free markup that screen readers can't parse.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### UI that only works for mouse users — no keyboard path, no focus indicators.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### State scattered through unrelated components instead of lifted to the right scope.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Mobile and low-bandwidth users ignored — desktop-first layouts that break under 375px.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### useEffect for derived state. Compute it, don't sync it.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
