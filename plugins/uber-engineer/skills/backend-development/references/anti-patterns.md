# Backend Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Returning 200 on errors with `{ "error": ... }` in the body.

**Fix:** Use the correct status code (4xx for client errors, 5xx for server). Adopt RFC 7807 problem details for the error body so clients can branch on `type`, not parse strings.

### Stuffing business logic into controllers; thin controllers, thick services.

**Fix:** Move logic into a service module that the controller calls. Controllers do parsing, auth check, response shaping. Anything that could be unit-tested without HTTP belongs in the service.

### N+1 queries hidden behind ORMs.

**Fix:** Profile with the ORM's query log on. Add an eager-load directive (Prisma `include`, ActiveRecord `includes`, SQLAlchemy `joinedload`, Hibernate `JOIN FETCH`) or rewrite as a single SQL with a join. Add a query-count assertion in the test for the hot path.

### Secrets in code, env files committed, or shared via Slack.

**Fix:** Move secrets to the platform secret store (AWS Secrets Manager, Doppler, 1Password, Vault). Rotate the leaked value immediately. Add `.env*` to `.gitignore` and commit a `.env.example` with placeholder names only.

### Logging request bodies that contain PII or credentials.

**Fix:** Add a redaction layer (pino-redact, structlog filter, Spring Cloud Sleuth scrubber) that strips known sensitive fields by name before write. Log the request shape, not the values.

### Long-running synchronous work where a queue belongs.

**Fix:** Split the work: handler enqueues a job + returns 202 with a status URL. Worker consumes the queue with retry and dead-letter. Status endpoint reports progress.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
