# API Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Returning 200 with errors in the body.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Versioning by accident — silent breaking changes that ship without a major bump.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Pagination with `page=N&size=M` over data that mutates between requests.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Webhook receivers that don't verify the signature.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.

### Error messages that leak stack traces or internal hostnames.

**Fix:** Identify the specific instance, propose the minimal correction, and link to the official-doc evidence justifying the change.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
