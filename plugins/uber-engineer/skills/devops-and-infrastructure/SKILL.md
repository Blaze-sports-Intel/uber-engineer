---
name: devops-and-infrastructure
description: "CI/CD, infrastructure as code, observability, rollback, and incident hygiene. Use when the user mentions: DevOps, CI/CD, GitHub Actions, GitLab CI, Jenkins, Terraform, Pulumi, Ansible, Kubernetes, K8s, Helm, Docker, container, deploy, rollback, blue-green, canary, observability, Prometheus, Grafana, OpenTelemetry, incident, runbook. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: application code changes without deploy implications (use the relevant dev discipline); vendor billing/admin work."
---

# DevOps & Infrastructure

CI/CD, infrastructure as code, observability, rollback, and incident hygiene.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: DevOps, CI/CD, GitHub Actions, GitLab CI, Jenkins, Terraform, Pulumi, Ansible, Kubernetes, K8s, Helm, Docker, container, deploy, rollback, blue-green, canary, observability, Prometheus, Grafana, OpenTelemetry, incident, runbook.

Use when the user wants any of:

- Design CI pipelines that fail fast and cheap.
- Write IaC that is idempotent, reviewable, and reversible.
- Pick a rollout strategy: rolling, blue/green, canary — with measurable health gates.
- Wire OpenTelemetry traces + Prometheus metrics + structured logs.
- Author runbooks that on-call can execute at 3am.
- Use feature flags as deploy/release decoupling, not just experimentation.

## When NOT to use this skill

- application code changes without deploy implications (use the relevant dev discipline)
- vendor billing/admin work

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

- CI pipeline YAML with explicit gates and timing.
- Terraform/Pulumi module with inputs, outputs, and example usage.
- Deployment plan including health checks and rollback trigger.
- Incident runbook with detection → triage → mitigation → postmortem template.
- SLO definitions tied to user-visible behavior, not raw uptime.
- Secrets management strategy with rotation cadence.

## Anti-patterns this skill pushes back against

- Snowflake servers — manual SSH changes that drift from IaC.
- Long-lived branches and merge queues that hide integration cost.
- Logs without trace IDs — debugging by grep across nodes.
- Health checks that return 200 while the app is broken.
- Single deploy step with no rollback path.
- Secrets in CI logs because someone echoed an env var.

## Verification required before claiming done

- IaC plan reviewed — `terraform plan` or `pulumi preview` matches intent.
- Pipeline runs from a clean clone in CI.
- Rollback rehearsed against staging.
- Trace shows up in observability tool for a real request.
- Alert rule fires on injected fault.
- Secrets never appear in logs or build output.

## Suggested commands

- `/devops pipeline-review .github/workflows/deploy.yml`
- `/devops rollout-plan --strategy=canary --service=api`
- `/devops runbook --incident=db-failover`

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

- CI runs from a clean clone with no manual setup.
- IaC plan reviewed and matches intent.
- Rollout strategy rehearsed against staging including rollback.
- Observability shows the change: trace, metric, log all align.
- On-call runbook updated for the new failure modes.

Verification actually happened — no claim of "verified" without evidence.
