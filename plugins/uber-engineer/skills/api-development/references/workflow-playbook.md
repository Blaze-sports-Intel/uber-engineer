# Api Development — Workflow Playbook

This is the long-form companion to `SKILL.md`. Load when you need the detailed step-by-step.

## Phase 1 — Intake (5 minutes)

Ask once, then commit. Do not pile up clarifying questions.

1. What's the surface? (route, file, service, model, contract, schema, scene, etc.)
2. What does "done" look like for this discipline? (See the definition-of-done states in `quality-rubric.md`.)
3. What does the existing code look like? Read before you propose.
4. Is there a deadline or constraint that changes the strategy?

If the user request crosses disciplines, call `discipline-router` first.

## Phase 2 — Source crawl

For any non-trivial technical claim:

1. Call Context7 MCP first for live docs.
2. Check the relevant entries in `official-sources.md`.
3. If a community blog is the only source, label the claim as "non-authoritative".

Never write API syntax from memory for SDKs that change quickly. Always check version.

## Phase 3 — Plan

Write a 5-10 line plan before touching files. Include:

- The exact change and where.
- The verification you'll run.
- The rollback if it goes wrong.

## Phase 4 — Execute

Match the capability to the artifact:

- **Design URI paths, verbs, and resources that follow REST or GraphQL conventions.** → OpenAPI 3.1 spec or GraphQL SDL covering 100% of the surface.
- **Author OpenAPI 3.1 or GraphQL SDL that doubles as the source of truth.** → Spec-as-source pipeline: types, mocks, tests, docs, SDKs all generated from the spec.
- **Apply versioning strategy (URI path, header, GraphQL field deprecation) consistently.** → Versioning + deprecation policy doc.
- **Design cursor-based pagination, filter, sort, and partial response.** → Error catalog: code, machine-readable type, human message, HTTP status — covering pagination edge cases.
- **Author webhook contracts with signatures, retries, and replay safety.** → Webhook signing + retry contract.
- **Generate typed SDKs from the spec, not hand-rolled per client.** → SDK generation config + smoke tests, plus a Postman/Bruno collection synced from the spec.

## Phase 5 — Verify

Every item in `SKILL.md` § "Verification required before claiming done" must pass. Capture evidence —
log line, screenshot, test output, profiler trace, scope reading, signed transaction hash, whatever
counts as proof in this discipline. Don't claim verification you didn't do.

## Phase 6 — Hand back

Tell the user:

- What shipped (in user terms, not file paths).
- What's now true that wasn't before (visible behavior, capacity, posture).
- What still needs attention, with severity.

No "great question," no apology preambles, no transformation arcs.

## Edge cases

- Repo state surprises: stop and ask, don't paper over.
- Conflicting docs: follow the most recent official source, log the conflict.
- Deadline pressure: shrink scope, never shrink verification.
- Cross-discipline scope creep: hand back to `discipline-router`.
