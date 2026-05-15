# DevOps & Infrastructure — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Snowflake servers — manual SSH changes that drift from IaC.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Long-lived branches and merge queues that hide integration cost.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Logs without trace IDs — debugging by grep across nodes.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Health checks that return 200 while the app is broken.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Single deploy step with no rollback path.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Secrets in CI logs because someone echoed an env var.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
