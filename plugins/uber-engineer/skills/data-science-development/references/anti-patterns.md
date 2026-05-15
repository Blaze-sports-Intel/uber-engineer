# Data Science Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### P-hacking via post-hoc test selection.

**Fix:** Pre-register the test, the metrics, and the analysis plan before pulling data. If you decide to look at additional metrics, apply a multiple-comparisons correction (Bonferroni, Benjamini-Hochberg). Document any deviation from the plan and why.

### Dashboards nobody owns; metrics drift silently.

**Fix:** Add an owner field to every dashboard at creation. Quarterly dashboard review: confirm owner, confirm refresh, retire dashboards no one looks at. Add a freshness check that alerts if a dashboard hasn't loaded in 30 days.

### Pulling production data into a local CSV.

**Fix:** Use a sanctioned data warehouse with read-only access. If the analysis truly needs raw rows, use an audited query interface (e.g., Snowflake, BigQuery) — never a CSV on a laptop. Apply row-level security to PII tables.

### Visualizations that hide uncertainty.

**Fix:** Show CIs, error bars, or shaded ranges on every chart of an estimated quantity. For point estimates, accompany with a sample size + the noise floor. Never show a single bar without context for what 'normal variation' looks like.

### Findings presented without a 'so what'.

**Fix:** End every analysis with a recommended action, a confidence level, and what would change the recommendation. If you can't write the action, the analysis isn't done — go back to framing.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
