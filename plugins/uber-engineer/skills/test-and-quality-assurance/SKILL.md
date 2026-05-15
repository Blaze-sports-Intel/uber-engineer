---
name: test-and-quality-assurance
description: "Test strategy, contract tests, E2E, visual regression, performance, and accessibility verification. Use when the user mentions: tests, testing, QA, test strategy, test pyramid, Vitest, Jest, Pytest, JUnit, RSpec, Go test, Playwright, Cypress, WebDriverIO, Detox, Appium, contract test, Pact, visual regression, Percy, Chromatic, Lighthouse CI. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: writing application code that has tests as a side effect (the discipline owns testing decisions); build/CI orchestration without test logic (use devops-and-infrastructure)."
---

# Test & Quality Assurance

Test strategy, contract tests, E2E, visual regression, performance, and accessibility verification.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: tests, testing, QA, test strategy, test pyramid, Vitest, Jest, Pytest, JUnit, RSpec, Go test, Playwright, Cypress, WebDriverIO, Detox, Appium, contract test, Pact, visual regression, Percy, Chromatic, Lighthouse CI.

Use when the user wants any of:

- Design a test pyramid that's mostly unit, then component/contract, then E2E.
- Apply mutation testing where it pays off (Stryker, mutmut).
- Use contract tests to keep client and server in sync.
- Run Playwright/Cypress against ephemeral environments.
- Add visual regression gates on a small, intentional surface — not the whole app.
- Wire flake quarantine + flake budget so flaky tests don't rot the suite.

## When NOT to use this skill

- writing application code that has tests as a side effect (the discipline owns testing decisions)
- build/CI orchestration without test logic (use devops-and-infrastructure)

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

- Test strategy doc: what runs in unit, integration, E2E, and where.
- Contract test pair (consumer + provider) with broker URL.
- E2E happy-path spec with retries-on-known-flake disabled.
- Visual regression baseline + diff threshold.
- Flake report with quarantine queue.
- Coverage report by directory, not by file.

## Anti-patterns this skill pushes back against

- Snapshot tests over the entire DOM.
- E2E tests as the primary defense against regressions.
- Coverage as a target instead of a signal.
- Tests that pass only when run alone.
- Mocking the system under test.

## Verification required before claiming done

- Test suite passes from a clean clone with no manual setup.
- Mutation score above the agreed threshold on critical modules.
- Contract tests pass against the latest provider version.
- Flake rate below the agreed budget over the last N runs.
- Visual regression diffs reviewed, not auto-accepted.

## Suggested commands

- `/qa test-strategy --feature=checkout`
- `/qa flake-report`
- `/qa contract-test consumer=web provider=api`

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

- Suite passes from a clean clone with no manual setup.
- Mutation score above the agreed threshold on critical modules.
- Contract tests pass against the latest provider version.
- Flake rate below the agreed budget over the last N runs.
- Visual regression diffs reviewed, not auto-accepted.

Verification actually happened — no claim of "verified" without evidence.
