# Security Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Rolling your own crypto.

**Fix:** Replace with a vetted library: libsodium / NaCl for symmetric, age for file encryption, JOSE libraries for tokens, the platform's HSM/KMS for keys. Document why the library was chosen and link to its security audit.

### Authn/authz in the UI but not the API.

**Fix:** Move every authorization check to the server-side handler. UI hides routes for UX, server enforces. Add contract tests that hit the endpoint without a valid token + with a token that lacks the scope, and assert 401/403.

### Long-lived static credentials.

**Fix:** Replace with short-lived tokens issued via OAuth client-credentials, AWS STS, GCP Workload Identity, or equivalent. Set a TTL ≤ 1 hour. Rotate the issuing key on a schedule.

### Logging request/response bodies indiscriminately.

**Fix:** Add a redaction layer that strips known sensitive fields (card, PII, secrets) by name before write. Log shape + sizes, not values. For debugging, sample 1% of requests with explicit consent + retention.

### Treating dependency updates as someone else's problem.

**Fix:** Wire Dependabot / Renovate / Snyk to open PRs on every CVE that affects you. Set a one-week SLA on highs and four-week SLA on mediums. Add a quarterly dependency-health review.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
