# Api Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Returning 200 with errors in the body.

**Fix:** Use the correct HTTP status code (4xx for client errors, 5xx for server). Adopt RFC 7807 problem details so clients can branch on `type`, not parse error strings.

### Versioning by accident — silent breaking changes that ship without a major bump.

**Fix:** Run a backward-compatibility check (oasdiff, GraphQL Inspector) on every PR. Block merge on any breaking change without an explicit version bump. Document deprecation policy: 6 months minimum before removal.

### Pagination with `page=N&size=M` over data that mutates between requests.

**Fix:** Switch to cursor-based pagination using a stable, opaque cursor token derived from the last record's sort key. Document the cursor format as opaque so clients don't construct it.

### Webhook receivers that don't verify the signature.

**Fix:** Add HMAC verification at the receiver: hash body + timestamp with the shared secret, constant-time compare. Reject signatures older than 5 minutes (replay defense). Document the verification step in the SDK README.

### Error messages that leak stack traces or internal hostnames.

**Fix:** Wrap server errors in a sanitized response: machine-readable `type`, human `title`, optional `detail` that's been stripped of internals, and a `request_id` for correlation. Stack traces go to internal logs only.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
