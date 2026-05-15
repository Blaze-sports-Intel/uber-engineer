# AI/ML Development — Workflow Playbook

This is the long-form companion to `SKILL.md`. Load when you need the detailed step-by-step.

## Phase 1 — Intake (5 minutes)

Ask once, then commit. Do not pile up clarifying questions.

1. What's the surface? (route, file, service, model, etc.)
2. What's the user-visible outcome? Loading + empty + error + populated all need to work.
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

- **Run reproducible experiments — pinned data, pinned code, pinned hardware** → Experiment tracker entry: dataset hash, code hash, hyperparams, metric.
- **Build eval harnesses that catch regressions before users do** → Eval suite with should-pass and should-fail cases per capability.
- **Version datasets and models the same way you version code** → Model card: training data, intended use, limitations, fairness notes.
- **Apply prompt evals for LLM-backed features — golden cases, edge cases, adversarial cases** → Inference SLA: P50/P95/P99 latency, cost per call.
- **Decide between fine-tune, RAG, tool-use, and prompting for a given problem** → Prompt or fine-tune diff with eval delta.
- **Wire model serving with retries, circuit breakers, and graceful degradation** → Rollback plan that pins the previous model version.

## Phase 5 — Verify

Every item in `SKILL.md` § "Verification required before claiming done" must pass. Capture evidence —
log line, screenshot, test output. Don't claim verification you didn't do.

## Phase 6 — Hand back

Tell the user:

- What shipped (in user terms, not file paths).
- What's now visible / changed for the visitor.
- What still needs attention, with severity.

No "great question," no apology preambles, no transformation arcs.

## Edge cases

- Repo state surprises: stop and ask, don't paper over.
- Conflicting docs: follow the most recent official source, log the conflict.
- Deadline pressure: shrink scope, never shrink verification.
- Cross-discipline scope creep: hand back to `discipline-router`.
