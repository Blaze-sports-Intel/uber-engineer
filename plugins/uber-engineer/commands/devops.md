---
description: DevOps & Infrastructure — invoke the devops-and-infrastructure skill with focused intent.
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

# /uber:devops

Invoke the **devops-and-infrastructure** skill for a DevOps & Infrastructure task.

## Usage

```
/uber:devops $ARGUMENTS
```

Common patterns:

- `/uber:devops pipeline-review .github/workflows/deploy.yml`
- `/uber:devops rollout-plan --strategy=canary --service=api`
- `/uber:devops runbook --incident=db-failover`

## What this command does

1. Loads the `devops-and-infrastructure` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

DevOps, CI/CD, GitHub Actions, GitLab CI, Jenkins, Terraform, Pulumi, Ansible, Kubernetes, K8s, Helm, Docker, container, deploy, rollback, blue-green, canary, observability, Prometheus, Grafana, OpenTelemetry, incident, runbook.
