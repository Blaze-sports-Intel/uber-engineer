---
name: cloud-development
description: Serverless, multi-environment config, observability, and release promotion across major clouds. Use when the user mentions: AWS, Lambda, S3, DynamoDB, EventBridge, GCP, Cloud Run, Firebase, Azure Functions, Cloudflare Workers, D1, KV, R2, Durable Objects, Vercel, Netlify, Fly.io, Render, serverless, edge runtime, cold start. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: on-prem infrastructure work; container orchestration on a private cluster (use devops-and-infrastructure).
---

# Cloud Development

Serverless, multi-environment config, observability, and release promotion across major clouds.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: AWS, Lambda, S3, DynamoDB, EventBridge, GCP, Cloud Run, Firebase, Azure Functions, Cloudflare Workers, D1, KV, R2, Durable Objects, Vercel, Netlify, Fly.io, Render, serverless, edge runtime, cold start.

Use when the user wants any of:

- Pick cloud + runtime based on cold-start tolerance, region needs, and cost shape.
- Apply least-privilege IAM/scopes from the first commit.
- Promote releases dev → staging → prod with config diffs reviewed.
- Set budgets + alerts; don't discover spend in the invoice.
- Design for the edge: short timeouts, idempotent handlers, no in-memory state.
- Use platform primitives (queues, KV, object storage) instead of bolting on a VPS.

## When NOT to use this skill

- on-prem infrastructure work
- container orchestration on a private cluster (use devops-and-infrastructure)

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

- Environment matrix: dev/staging/prod with config diffs.
- IAM policy or equivalent with least-privilege per role.
- Cost forecast + budget alert.
- Edge-runtime constraint checklist (no Node-only APIs, etc.).
- Cold start budget per handler.
- Multi-region failover plan with RPO + RTO.

## Anti-patterns this skill pushes back against

- Wildcard IAM policies ('*' on actions or resources).
- Hardcoded region or env in code instead of config.
- Long-running Lambda/Worker that should have been a Step Function or Workflow.
- Cold start regressions discovered in prod traffic.
- Single-region deploy treated as 'highly available'.

## Verification required before claiming done

- Deploy to staging matches prod config except for secrets and region.
- IAM review passes — no wildcards, no unused permissions.
- Cold start P99 within budget on the smallest config.
- Budget alert wired and tested with a synthetic spike.
- Failover rehearsed against a region-down simulation.

## Suggested commands

- `/uber:cloud iam-review aws/policies/api.json`
- `/uber:cloud env-diff staging prod`
- `/uber:cloud coldstart-budget worker:api`

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
