---
description: Test & Quality Assurance — invoke the test-and-quality-assurance skill with focused intent.
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

# /uber:qa

Invoke the **test-and-quality-assurance** skill for a Test & Quality Assurance task.

## Usage

```
/uber:qa $ARGUMENTS
```

Common patterns:

- `/uber:qa test-strategy --feature=checkout`
- `/uber:qa flake-report`
- `/uber:qa contract-test consumer=web provider=api`

## What this command does

1. Loads the `test-and-quality-assurance` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

tests, testing, QA, test strategy, test pyramid, Vitest, Jest, Pytest, JUnit, RSpec, Go test, Playwright, Cypress, WebDriverIO, Detox, Appium, contract test, Pact, visual regression, Percy, Chromatic, Lighthouse CI.
