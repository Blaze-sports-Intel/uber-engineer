# Devops And Infrastructure — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Snowflake servers — manual SSH changes that drift from IaC.

**Fix:** Detect drift with `terraform plan` or `pulumi preview` on a schedule. Treat any unexpected diff as an incident. Replace SSH access with break-glass-only audited sessions; permanent changes go through code review.

### Long-lived branches and merge queues that hide integration cost.

**Fix:** Switch to trunk-based development with feature flags. Cap branch age at 24 hours. Use a merge queue (GitHub merge queue, Mergify) that re-runs CI after every merge to catch interaction bugs.

### Logs without trace IDs — debugging by grep across nodes.

**Fix:** Add a request-scoped trace identifier (W3C trace-context, OpenTelemetry trace_id) to every log line. Propagate across HTTP/gRPC/queue boundaries. Use a log aggregator that supports trace-link queries.

### Health checks that return 200 while the app is broken.

**Fix:** Differentiate liveness (process is up) from readiness (can serve traffic) from startup (warming). Readiness should test downstream dependencies on a sample. Add a synthetic that exercises the actual user path, not just /health.

### Single deploy step with no rollback path.

**Fix:** Split into deploy + activate. Deploy stages the new version (canary, blue-green slot, or new revision). Activate flips traffic. Rollback is a one-step traffic flip back, not a redeploy.

### Secrets in CI logs because someone echoed an env var.

**Fix:** Mark secrets as masked in the CI platform (GitHub Actions `add-mask`, GitLab `masked`). Use a secret scanner (TruffleHog, gitleaks) on every commit. Rotate any secret that ever appeared in a log.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
