---
description: Frontend Development — invoke the frontend-development skill with focused intent.
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

# /uber:frontend

Invoke the **frontend-development** skill for a Frontend Development task.

## Usage

```
/uber:frontend $ARGUMENTS
```

Common patterns:

- `/uber:frontend audit-a11y src/components/Checkout`
- `/uber:frontend perf-budget --route=/products --target=lcp:2500ms`
- `/uber:frontend storybook-gen src/components/Button.tsx`

## What this command does

1. Loads the `frontend-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

frontend, UI, user interface, React, Next.js, Vue, Svelte, Angular, component, design system, accessibility, WCAG, ARIA, responsive, Core Web Vitals, LCP, INP, CLS, Storybook, Tailwind, shadcn/ui, hydration, bundle size.
