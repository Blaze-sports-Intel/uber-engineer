---
description: Security Development — invoke the security-development skill with focused intent.
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

# /uber:security

Invoke the **security-development** skill for a Security Development task.

## Usage

```
/uber:security $ARGUMENTS
```

Common patterns:

- `/uber:security threat-model --surface=payments`
- `/uber:security sast-triage`
- `/uber:security secret-rotation --provider=stripe`

## What this command does

1. Loads the `security-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

security, threat model, STRIDE, OWASP, CVE, SAST, DAST, dependency audit, supply chain, SBOM, Snyk, Dependabot, secrets scanning, SOC 2, ISO 27001, GDPR, PII, encryption, TLS, key management, incident response.
