---
description: Route an engineering request across the 17 uber-engineer disciplines.
argument-hint: <natural language request>
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Task
---

# /uber

Top-level entry point. Dispatches to the right discipline based on natural-language intent.

## Usage

```
/uber $ARGUMENTS
```

## What this command does

1. Calls the `discipline-router` agent with `$ARGUMENTS`.
2. Receives a routing plan: PRIMARY discipline + SECONDARY + ordered steps.
3. Dispatches each step to the right per-discipline command.
4. Calls `build-validator` and `ship-auditor` before reporting back.

## Per-discipline commands

| Command | Discipline |
|---------|------------|
| `/uber:frontend` | Frontend Development |
| `/uber:backend` | Backend Development |
| `/uber:fullstack` | Full-Stack Development |
| `/uber:mobile` | Mobile Development |
| `/uber:game` | Game Development |
| `/uber:devops` | DevOps & Infrastructure |
| `/uber:api` | API Development |
| `/uber:db` | Database Development |
| `/uber:embedded` | Embedded Systems Development |
| `/uber:cloud` | Cloud Development |
| `/uber:ai` | AI/ML Development |
| `/uber:blockchain` | Blockchain Development |
| `/uber:qa` | Test & Quality Assurance |
| `/uber:security` | Security Development |
| `/uber:xr` | AR/VR Development |
| `/uber:data` | Data Science Development |
| `/uber:web` | Web Development |

## Examples

```
/uber ship a saved-search feature with UI, API, DB migration, and tests
/uber audit accessibility on the new checkout flow
/uber move our auth from custom JWT to Auth0
```
