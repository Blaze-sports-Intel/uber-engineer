# Devops And Infrastructure — Quality Rubric

Use this rubric on PR review or before claiming any task done.

## Verification matrix

| # | Check | Result |
|---|-------|--------|
| 1 | IaC plan reviewed — `terraform plan` or `pulumi preview` matches intent. | pass / fail / n/a |
| 2 | Pipeline runs from a clean clone in CI. | pass / fail / n/a |
| 3 | Rollback rehearsed against staging. | pass / fail / n/a |
| 4 | Trace shows up in observability tool for a real request. | pass / fail / n/a |
| 5 | Alert rule fires on injected fault. | pass / fail / n/a |
| 6 | Secrets never appear in logs or build output. | pass / fail / n/a |

## Definition of done

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below all need to
hold:

- CI runs from a clean clone with no manual setup.
- IaC plan reviewed and matches intent.
- Rollout strategy rehearsed against staging including rollback.
- Observability shows the change: trace, metric, log all align.
- On-call runbook updated for the new failure modes.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured.
- Rollback plan exists and someone other than the author could execute it.

## Failure modes that block "done"

- Tests pass but the real-world behavior is wrong.
- Build is green but the visible / measurable surface is broken.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
