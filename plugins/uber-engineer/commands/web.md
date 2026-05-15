---
description: Web Development — invoke the web-development skill with focused intent.
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

# /uber:web

Invoke the **web-development** skill for a Web Development task.

## Usage

```
/uber:web $ARGUMENTS
```

Common patterns:

- `/uber:web route-table`
- `/uber:web seo-audit --url=https://example.com`
- `/uber:web vitals-budget --route=/`

## What this command does

1. Loads the `web-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

web app, website, SSR, SSG, ISR, RSC, SPA, Next.js, Remix, Astro, SvelteKit, Nuxt, SEO, structured data, sitemap, robots.txt, OpenGraph, Lighthouse, Vercel, Cloudflare Pages.
