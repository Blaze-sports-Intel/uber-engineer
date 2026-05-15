# Frontend Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Hard-coded colors instead of design tokens.

**Fix:** Replace the hex value with the closest design token. If no token covers the use case, propose one with a name + intent + dark-mode pair, then commit the token alongside the change.

### Div soup — semantic-free markup that screen readers can't parse.

**Fix:** Map each div to the semantic element it should be (header, nav, main, section, article, aside, footer, button, list). Where no semantic exists, add an ARIA role + name. Re-run axe to confirm zero violations.

### UI that only works for mouse users — no keyboard path, no focus indicators.

**Fix:** Add explicit `:focus-visible` styles using a token, ensure tab order matches visual order, and verify every interactive element fires on Enter/Space. Walk the page with the keyboard end-to-end.

### State scattered through unrelated components instead of lifted to the right scope.

**Fix:** Identify the lowest common ancestor of all components that read or write the state. Lift state there. If state is shared across distant subtrees, move to a typed store (Zustand, Jotai, TanStack Store) — never prop-drill through 4+ layers.

### Mobile and low-bandwidth users ignored — desktop-first layouts that break under 375px.

**Fix:** Rewrite media queries mobile-first. Set the base layout for 320–375px width, then add `min-width` breakpoints upward. Verify on a throttled connection (Slow 3G in DevTools).

### useEffect for derived state. Compute it, don't sync it.

**Fix:** Compute the derived value inline during render. If the computation is expensive, wrap with `useMemo`. If it depends on async data, lift it to a query library (TanStack Query, SWR) — never keep a parallel `useState` synced via `useEffect`.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
