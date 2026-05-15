# Cloud Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Wildcard IAM policies ('*' on actions or resources).

**Fix:** Replace wildcards with the specific actions and ARNs the role actually needs. Use AWS IAM Access Analyzer (or GCP IAM Recommender) to identify unused permissions and prune. Add a CI gate that diffs the policy against a baseline.

### Hardcoded region or env in code instead of config.

**Fix:** Move region and environment to runtime config (env vars, parameter store, platform config). Reference from a single config module — never inline literals in handlers. Test by running the same artifact in two regions.

### Long-running Lambda/Worker that should have been a Step Function or Workflow.

**Fix:** Decompose into steps with explicit state. Use Step Functions, Cloudflare Workflows, Temporal, or Durable Objects. The handler stays under the cold-start budget; long work happens in the orchestrator with retries + observability.

### Cold start regressions discovered in prod traffic.

**Fix:** Add a cold-start budget test in CI: cold-invoke the handler, measure end-to-end latency, fail the build if it exceeds the budget. For latency-sensitive routes, enable provisioned concurrency or smart placement.

### Single-region deploy treated as 'highly available'.

**Fix:** Document the actual SLA. If multi-region is required, deploy to at least two regions with a global load balancer (Route 53, Cloudflare LB), routine failover rehearsal, and a documented RPO/RTO. If single-region is fine, say so explicitly so on-call knows what to expect.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
