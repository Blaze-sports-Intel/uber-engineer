---
name: backend-development
description: "Service architecture, API contracts, auth, data persistence, and operational hygiene. Use when the user mentions: backend, API, REST, GraphQL, server, Node.js, Python, Go, Java, Spring Boot, Express, Fastify, FastAPI, Django, Rails, authentication, authorization, JWT, OAuth, rate limiting, idempotency, caching, queue, background job. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: pure frontend UI work (use frontend-development); database schema migration work (use database-development); container orchestration / deploy pipeline (use devops-and-infrastructure)."
---

# Backend Development

Service architecture, API contracts, auth, data persistence, and operational hygiene.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: backend, API, REST, GraphQL, server, Node.js, Python, Go, Java, Spring Boot, Express, Fastify, FastAPI, Django, Rails, authentication, authorization, JWT, OAuth, rate limiting, idempotency, caching, queue, background job.

Use when the user wants any of:

- Design service boundaries and request/response contracts that survive versioning.
- Implement auth flows: session, JWT, OAuth 2.1, OIDC, API keys, RBAC, ABAC.
- Make endpoints idempotent, retry-safe, and observable from day one.
- Apply rate limiting, request validation, and abuse mitigation at the edge.
- Pick the right caching layer — none, in-memory, Redis, CDN — based on read/write profile.
- Wire up structured logging, metrics, and tracing before the service ships.

## When NOT to use this skill

- pure frontend UI work (use frontend-development)
- database schema migration work (use database-development)
- container orchestration / deploy pipeline (use devops-and-infrastructure)

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

- OpenAPI 3.1 spec with examples, error schemas, and security definitions.
- Auth flow diagram showing token issuance, refresh, and revocation.
- Rate-limit policy mapped to endpoint sensitivity.
- Service health-check + readiness probe specification.
- Runbook for the top 3 failure modes.
- Migration plan for breaking API changes.

## Anti-patterns this skill pushes back against

- Returning 200 on errors with `{ "error": ... }` in the body.
- Stuffing business logic into controllers; thin controllers, thick services.
- N+1 queries hidden behind ORMs.
- Secrets in code, env files committed, or shared via Slack.
- Logging request bodies that contain PII or credentials.
- Long-running synchronous work where a queue belongs.

## Verification required before claiming done

- Contract tests pass against the OpenAPI spec.
- Auth flow exercised end-to-end with valid + invalid tokens.
- Load test hits target RPS at p95 latency budget.
- Logs/metrics/traces visible in observability stack.
- Idempotency keys verified on retry.
- Security scan (SAST + dependency audit) clean.

## Suggested commands

- `/uber:backend design-endpoint POST /v1/orders`
- `/uber:backend auth-flow oauth2-pkce`
- `/uber:backend ratelimit /v1/checkout --tier=premium`

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
