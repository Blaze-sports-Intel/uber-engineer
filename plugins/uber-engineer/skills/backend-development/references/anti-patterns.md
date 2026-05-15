# Backend Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Returning 200 on errors with `{ "error": ... }` in the body.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Stuffing business logic into controllers; thin controllers, thick services.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### N+1 queries hidden behind ORMs.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Secrets in code, env files committed, or shared via Slack.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Logging request bodies that contain PII or credentials.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Long-running synchronous work where a queue belongs.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
