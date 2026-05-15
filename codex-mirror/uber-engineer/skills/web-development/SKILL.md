---
name: web-development
description: End-to-end web app delivery: routing, rendering modes, SEO, perf, deploy, and observability. Use when the user mentions: web app, website, SSR, SSG, ISR, RSC, SPA, Next.js, Remix, Astro, SvelteKit, Nuxt, SEO, structured data, sitemap, robots.txt, OpenGraph, Lighthouse, Vercel, Cloudflare Pages. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: isolated frontend component work (use frontend-development); isolated backend service work (use backend-development).
---

# Web Development

End-to-end web app delivery: routing, rendering modes, SEO, perf, deploy, and observability.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: web app, website, SSR, SSG, ISR, RSC, SPA, Next.js, Remix, Astro, SvelteKit, Nuxt, SEO, structured data, sitemap, robots.txt, OpenGraph, Lighthouse, Vercel, Cloudflare Pages.

Use when the user wants any of:

- Pick the right rendering mode per route, not per app.
- Wire routing, layouts, error boundaries, and not-found at the framework boundary.
- Configure SEO: titles, descriptions, canonical, OpenGraph, Twitter Cards, JSON-LD.
- Optimize Core Web Vitals at the page level with measured budgets.
- Deploy with preview URLs per PR and cache invalidation on release.
- Add web-vitals + RUM + error reporting at the framework boundary.

## When NOT to use this skill

- isolated frontend component work (use frontend-development)
- isolated backend service work (use backend-development)

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

- Route table: path → rendering mode → cache policy → owner.
- SEO config per route.
- Performance budget per route with measured baseline.
- Deploy pipeline with preview + production + rollback.
- Observability dashboard: vitals, errors, traffic.
- Accessibility statement page wired into the app.

## Anti-patterns this skill pushes back against

- Every page SSR'd because someone heard SSR was good.
- Client-side routing without a 404 page.
- Meta tags in components that don't render server-side.
- Cache busting via query string instead of fingerprinted filenames.
- Production deploys without preview URLs.

## Verification required before claiming done

- Lighthouse on the top 5 routes meets budget.
- Sitemap + robots + canonical correct on production.
- Preview URL renders the change before merge.
- Web-vitals dashboard wired and showing data.
- Error reporting catches a synthetic exception.

## Suggested commands

- `/uber:web route-table`
- `/uber:web seo-audit --url=https://example.com`
- `/uber:web vitals-budget --route=/`

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
