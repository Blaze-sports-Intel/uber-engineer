# AI/ML Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Evaluating on the training set.

**Fix:** Hold out a test set before any training. Never look at the test set during iteration. For LLMs, also hold out a 'red team' set the model has never seen and rerun before every release.

### Vibes-based prompt engineering with no eval suite.

**Fix:** Define the suite before the prompt: 30+ cases with expected outputs (or rubrics for open-ended). Run the suite on every prompt change. Block prompt PRs without an eval delta.

### Shipping an LLM feature without a deterministic fallback for outages.

**Fix:** Add a fallback path for when the LLM is unreachable: cached prior answer, simpler heuristic, or a graceful 'try again' UI. Test by simulating a provider outage in CI.

### Storing API keys in notebooks.

**Fix:** Move keys to environment variables sourced from a secret manager. Use `python-dotenv` for local dev with a `.env` (gitignored) and `.env.example` (committed) pattern. Add a pre-commit hook that scans for key shapes (sk-, sk-ant-).

### Comparing model versions on different evals.

**Fix:** Pin the eval suite version. When the suite changes, re-run all candidate models on the new version before comparing. Tag each eval run with the suite hash so historical comparisons stay valid.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
