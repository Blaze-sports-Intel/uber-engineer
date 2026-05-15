# Frontend Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/frontend audit-a11y src/components/Checkout
```

```
/frontend perf-budget --route=/products --target=lcp:2500ms
```

```
/frontend storybook-gen src/components/Button.tsx
```

The `/uber` router will dispatch to `/frontend` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Make this component faster."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Profile the component's render path, identify what triggers re-renders, isolate the heaviest contributor, and ship a measured fix — keep the budget at LCP ≤ 2.5s and INP ≤ 200ms on a mid-tier device."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `full-stack-development` skill — for adjacent work that's better handled there.
- `web-development` skill — for adjacent work that's better handled there.
- `mobile-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
