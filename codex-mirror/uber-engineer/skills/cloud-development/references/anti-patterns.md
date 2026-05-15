# Cloud Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Wildcard IAM policies ('*' on actions or resources).

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Hardcoded region or env in code instead of config.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Long-running Lambda/Worker that should have been a Step Function or Workflow.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Cold start regressions discovered in prod traffic.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Single-region deploy treated as 'highly available'.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
