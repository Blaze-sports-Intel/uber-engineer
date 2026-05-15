---
name: full-stack-development
description: End-to-end feature delivery across frontend, backend, API, database, and deploy. Use when the user mentions: full-stack, fullstack, end-to-end feature, ship a feature, Next.js full-stack, Remix, SvelteKit, Nuxt, tRPC, T3 stack, Astro, Hono, monorepo, Turborepo, Nx. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: single-layer work that belongs in one discipline; pure infra/deploy without app code.
---

# Full-Stack Development

End-to-end feature delivery across frontend, backend, API, database, and deploy.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: full-stack, fullstack, end-to-end feature, ship a feature, Next.js full-stack, Remix, SvelteKit, Nuxt, tRPC, T3 stack, Astro, Hono, monorepo, Turborepo, Nx.

Use when the user wants any of:

- Slice a feature vertically across UI, API, persistence, and tests in one pass.
- Pick the right framework boundary — server components, server actions, RSC, RPC, REST.
- Manage cross-cutting concerns: auth context, error boundaries, telemetry, caching.
- Coordinate migrations: ship behind a flag, dual-read/dual-write, backfill, cut over, clean up.
- Keep frontend and backend types in sync (Zod, tRPC, OpenAPI codegen, GraphQL codegen).
- Decide between SSR, SSG, ISR, RSC, and SPA per route, not per app.

## When NOT to use this skill

- single-layer work that belongs in one discipline
- pure infra/deploy without app code

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

- Vertical slice PR plan: schema → API → UI → tests → docs.
- Type contract definition shared across layers.
- Feature flag rollout plan with kill switch.
- End-to-end test scenario with happy + error + empty paths.
- Rollback plan that doesn't require code revert.

## Anti-patterns this skill pushes back against

- Frontend types drifting from backend reality — duplicated, hand-maintained interfaces.
- API surface designed around UI screens instead of domain operations.
- Auth checked in the UI but not on the server.
- Shipping a feature without an empty state, error state, or loading state.
- Big-bang migrations with no rollback path.

## Verification required before claiming done

- Type check passes across the whole monorepo.
- Contract tests align frontend expectations with backend reality.
- Playwright/Cypress E2E covers the happy path + one failure path.
- Feature flag toggles cleanly without redeploy.
- Empty/loading/error/populated all render correctly.

## Suggested commands

- `/uber:fullstack ship-feature 'add saved search to product index'`
- `/uber:fullstack vertical-slice src/features/checkout`
- `/uber:fullstack flag-rollout new-onboarding --percent=10`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user can see the correct output of this work. Build success, deploy success, and 200
responses do not equal done. Every data surface explicitly handles loading, error, empty, and
populated states. Verification actually happened — no claim of "verified" without evidence.
