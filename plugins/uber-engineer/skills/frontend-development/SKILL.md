---
name: frontend-development
description: "Component-level UI: design systems, accessibility, responsive layout, component-tier performance, state architecture inside the component tree. Use when the user mentions: frontend, UI, user interface, component, React, Vue, Svelte, Angular, design system, accessibility, WCAG, ARIA, responsive, Core Web Vitals at the component level, LCP, INP, CLS, Storybook, Tailwind, shadcn/ui, hydration, bundle size, props, hooks, signals, computed, derived state. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: page-level / route-level / SEO / rendering-mode / deploy work in Next.js, Remix, SvelteKit, Astro, or Nuxt — those are web-development territory; backend API design without a UI surface; pure database schema work; infrastructure or deploy automation; iOS/Android native UI (use mobile-development)."
---

# Frontend Development

UI implementation, design systems, accessibility, responsive layout, and frontend performance.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: frontend, UI, user interface, component, React, Vue, Svelte, Angular, design system, accessibility, WCAG, ARIA, responsive, Core Web Vitals at the component level, LCP, INP, CLS, Storybook, Tailwind, shadcn/ui, hydration, bundle size.

Note on meta-framework names (Next.js, Remix, SvelteKit, Astro, Nuxt): these route to **web-development** because they own routing, rendering modes, SEO, and deploy. Component-tier work *inside* those frameworks still routes here.

Use when the user wants any of:

- Generate and refactor components without breaking design-system contracts.
- Audit accessibility against WCAG 2.2 AA: keyboard nav, focus order, labels, color contrast, reduced motion.
- Optimize Core Web Vitals — LCP, INP, CLS — with real measurement, not assumptions.
- Build responsive layouts with explicit mobile/tablet/desktop acceptance criteria.
- Author Storybook stories, MSW fixtures, and visual regression baselines.
- Separate UI state, server state, form state, and URL state with predictable patterns.

## When NOT to use this skill

- page-level / route-level / SEO / rendering-mode / deploy work in Next.js, Remix, SvelteKit, Astro, or Nuxt (use web-development — that skill owns the meta-framework layer)
- backend API design without a UI surface
- pure database schema work
- infrastructure or deploy automation
- iOS/Android native UI (use mobile-development)

## Workflow

1. **Intake.** Read the user intent. Identify which capability above applies. If the request crosses
   into another discipline (e.g. UI + DB), call the `discipline-router` agent before splitting work.
2. **Inspect.** Look at the actual repo state with Read/Grep/Glob before proposing changes. Do not
   assume what code exists from project name alone.
3. **Source-check.** For non-obvious technical claims, ground the answer in the official sources
   listed in `references/official-sources.md`. Use the Context7 MCP for live doc lookups instead of
   relying on training-data memory for fast-moving APIs.
4. **Produce.** Generate the appropriate artifact from the list below.
5. **Verify.** Run every verification layer below before claiming done. Build success is not done.
   200 responses are not done. A real user seeing correct output is done.
6. **Hand back.** Report what shipped, what the visitor sees, what changed. No file paths, function
   names, or engineering jargon unprompted.

## Artifacts this skill produces

- Component checklist (props, states, a11y, tokens, tests).
- Accessibility review report mapped to WCAG SCs.
- Performance budget with measured baseline and target.
- Responsive QA matrix (320/768/1024/1440 minimum).
- Storybook story template with controls and a11y addon.
- Visual regression plan with diff thresholds.

## Anti-patterns this skill pushes back against

- Hard-coded colors instead of design tokens.
- Div soup — semantic-free markup that screen readers can't parse.
- UI that only works for mouse users — no keyboard path, no focus indicators.
- State scattered through unrelated components instead of lifted to the right scope.
- Mobile and low-bandwidth users ignored — desktop-first layouts that break under 375px.
- useEffect for derived state. Compute it, don't sync it.

## Verification required before claiming done

- Unit and component tests pass (Vitest/Jest + RTL).
- axe-core scan returns zero violations on changed surfaces.
- Lighthouse or web-vitals report meets the budget (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1).
- Visual regression diff approved or unchanged.
- Cross-browser smoke pass: Chrome, Safari, Firefox.
- Manual keyboard-only walkthrough of the new path.

## Suggested commands

- `/frontend audit-a11y src/components/Checkout`
- `/frontend perf-budget --route=/products --target=lcp:2500ms`
- `/frontend storybook-gen src/components/Button.tsx`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below must all hold:

- Loading state renders without layout shift.
- Empty state explains why there's no data, not just a blank screen.
- Error state shows what failed and whether it's transient.
- Populated state matches the design and meets the perf budget.

Verification actually happened — no claim of "verified" without evidence.
