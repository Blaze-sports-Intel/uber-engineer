---
name: web-development
description: "Meta-framework layer: routing, rendering modes (SSR/SSG/ISR/RSC), SEO, structured data, page-level perf budgets, deploy, observability, and edge config. Use when the user mentions: web app, website, page, route, SSR, SSG, ISR, RSC, SPA, Next.js, Remix, Astro, SvelteKit, Nuxt, app router, pages router, middleware, generateMetadata, generateStaticParams, SEO, structured data, sitemap, robots.txt, OpenGraph, Twitter Cards, JSON-LD, Lighthouse on the page, Vercel, Cloudflare Pages, Netlify, deploy preview. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: component-tier work inside the framework (use frontend-development — that skill owns the component layer; this skill owns the page/route/deploy layer); isolated backend service work (use backend-development); public API contract design (use api-development)."
---

# Web Development

End-to-end web app delivery: routing, rendering modes, SEO, perf, deploy, and observability.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: web app, website, page, route, SSR, SSG, ISR, RSC, SPA, Next.js, Remix, Astro, SvelteKit, Nuxt, app router, pages router, middleware, generateMetadata, generateStaticParams, SEO, structured data, sitemap, robots.txt, OpenGraph, Twitter Cards, JSON-LD, Lighthouse on the page, Vercel, Cloudflare Pages, Netlify, deploy preview.

Note on component work: anything inside `components/` or below the page boundary routes to **frontend-development**. This skill stays at the page, route, and deploy layer.

Use when the user wants any of:

- Pick the right rendering mode per route, not per app.
- Wire routing, layouts, error boundaries, and not-found at the framework boundary.
- Configure SEO: titles, descriptions, canonical, OpenGraph, Twitter Cards, JSON-LD.
- Optimize Core Web Vitals at the page level with measured budgets.
- Deploy with preview URLs per PR and cache invalidation on release.
- Add web-vitals + RUM + error reporting at the framework boundary.

## When NOT to use this skill

- component-tier work inside the meta-framework (use frontend-development — this skill owns the page/route/deploy layer; that skill owns the component layer)
- isolated backend service work (use backend-development)
- public API contract design (use api-development)

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

- `/web route-table`
- `/web seo-audit --url=https://example.com`
- `/web vitals-budget --route=/`

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

- Lighthouse on the top 5 routes meets budget.
- Sitemap + robots + canonical correct on production.
- Preview URL renders the change before merge.
- Web-vitals dashboard wired and showing data.
- Error reporting catches a synthetic exception.

Verification actually happened — no claim of "verified" without evidence.
