---
name: api-development
description: "Public-facing API contract design: paths, versioning, backward compatibility, error schemas, webhook signing, SDK generation, developer experience. Use when the user mentions: API design, REST design, GraphQL schema, gRPC proto, OpenAPI, Swagger, API versioning, deprecation policy, error schema, RFC 7807, problem details, webhook contract, cursor pagination, API key issuance, OAuth scopes, SDK generation, API gateway, public docs. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: implementing the handlers behind the contract (use backend-development — this skill designs the wire; backend-development builds the service); internal-only service-to-service calls without external contract; frontend data fetching strategy without server contract change."
---

# API Development

API contracts, versioning, backward compatibility, error schemas, and developer experience.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: API design, REST, GraphQL, gRPC, OpenAPI, Swagger, API versioning, deprecation, error schema, RFC 7807, problem details, webhook, pagination, rate limit, API key, OAuth scopes, SDK, API gateway.

Use when the user wants any of:

- Design URI paths, verbs, and resources that follow REST or GraphQL conventions.
- Author OpenAPI 3.1 or GraphQL SDL that doubles as the source of truth.
- Apply versioning strategy (URI path, header, GraphQL field deprecation) consistently.
- Design cursor-based pagination, filter, sort, and partial response.
- Author webhook contracts with signatures, retries, and replay safety.
- Generate typed SDKs from the spec, not hand-rolled per client.

## When NOT to use this skill

- implementing the handlers behind the contract (use backend-development — this skill designs the wire; that skill builds the service)
- internal-only service-to-service calls without an external contract
- frontend data fetching strategy without a server contract change

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

- OpenAPI 3.1 spec or GraphQL SDL covering 100% of the surface.
- Error catalog: code, machine-readable type, human message, HTTP status.
- Versioning + deprecation policy doc.
- Webhook signing + retry contract.
- SDK generation config + smoke tests.
- Postman/Bruno collection synced from spec.

## Anti-patterns this skill pushes back against

- Returning 200 with errors in the body.
- Versioning by accident — silent breaking changes that ship without a major bump.
- Pagination with `page=N&size=M` over data that mutates between requests.
- Webhook receivers that don't verify the signature.
- Error messages that leak stack traces or internal hostnames.

## Verification required before claiming done

- OpenAPI lint passes (Spectral or vacuum) with zero errors.
- Backward compatibility check against the previous minor version is clean.
- Webhook receiver rejects unsigned + replayed payloads.
- Generated SDK compiles and round-trips a request.
- Public docs site renders the spec without warnings.

## Suggested commands

- `/api design-resource users`
- `/api version-bump --from=v1 --to=v2`
- `/api webhook-contract subscription.created`

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

- Spec lints clean (Spectral / vacuum) with zero errors.
- Backward-compat check against previous minor passes.
- Webhook receiver rejects unsigned + replayed payloads.
- Generated SDK compiles and round-trips a request.
- Public docs site renders the spec without warnings.

Verification actually happened — no claim of "verified" without evidence.
