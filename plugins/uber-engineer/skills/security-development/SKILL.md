---
name: security-development
description: "Threat modeling, secure-by-default code, dependency hygiene, secrets management, and incident response. Use when the user mentions: security, threat model, STRIDE, OWASP, CVE, SAST, DAST, dependency audit, supply chain, SBOM, Snyk, Dependabot, secrets scanning, SOC 2, ISO 27001, GDPR, PII, encryption, TLS, key management, incident response. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: vendor compliance paperwork without code or config implications; physical security."
---

# Security Development

Threat modeling, secure-by-default code, dependency hygiene, secrets management, and incident response.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: security, threat model, STRIDE, OWASP, CVE, SAST, DAST, dependency audit, supply chain, SBOM, Snyk, Dependabot, secrets scanning, SOC 2, ISO 27001, GDPR, PII, encryption, TLS, key management, incident response.

Use when the user wants any of:

- Run STRIDE threat models against new surfaces.
- Apply OWASP Top 10 + ASVS as a checklist, not a sermon.
- Manage secrets via a vault or platform secret store — never in repo.
- Wire SAST + DAST + SCA into CI with actionable findings, not noise.
- Author incident-response playbooks: detect → contain → eradicate → recover → review.
- Apply least privilege, defense in depth, and explicit deny defaults.

## When NOT to use this skill

- vendor compliance paperwork without code or config implications
- physical security

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

- Threat model doc: assets, actors, surface, attack trees, mitigations.
- SBOM (CycloneDX or SPDX) per release artifact.
- Secret-rotation schedule with owners.
- CI security gates: SAST, DAST, secret scan, dependency audit.
- Incident playbook + on-call rotation.
- Data classification + retention policy.

## Anti-patterns this skill pushes back against

- Rolling your own crypto.
- Authn/authz in the UI but not the API.
- Long-lived static credentials.
- Logging request/response bodies indiscriminately.
- Treating dependency updates as someone else's problem.

## Verification required before claiming done

- Threat model reviewed before launch by a second engineer.
- SAST + SCA gates pass with no unresolved highs.
- Pen test or red-team exercise scheduled before significant launches.
- Tabletop incident exercise run at least once per quarter.
- Secret rotation rehearsed end-to-end.

## Suggested commands

- `/security threat-model --surface=payments`
- `/security sast-triage`
- `/security secret-rotation --provider=stripe`

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

- Threat model reviewed before launch by a second engineer.
- SAST + SCA gates pass with no unresolved highs.
- Pen test or red-team exercise scheduled before significant launches.
- Tabletop incident exercise run at least once per quarter.
- Secret rotation rehearsed end-to-end.

Verification actually happened — no claim of "verified" without evidence.
