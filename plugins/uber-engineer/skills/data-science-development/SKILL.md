---
name: data-science-development
description: "Reproducible analysis, dataset hygiene, statistical rigor, dashboarding, and shipping insights. Use when the user mentions: data analysis, data science, notebook, Jupyter, pandas, Polars, DuckDB, Spark, dbt, Airflow, Dagster, Prefect, Streamlit, Plotly, Tableau, Looker, hypothesis test, A/B test, cohort analysis. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: model training (use ai-ml-development); production data pipeline ops (use devops-and-infrastructure or backend-development)."
---

# Data Science Development

Reproducible analysis, dataset hygiene, statistical rigor, dashboarding, and shipping insights.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: data analysis, data science, notebook, Jupyter, pandas, Polars, DuckDB, Spark, dbt, Airflow, Dagster, Prefect, Streamlit, Plotly, Tableau, Looker, hypothesis test, A/B test, cohort analysis.

Use when the user wants any of:

- Frame the question before pulling data — avoid garden-pathing.
- Reproduce analyses from raw inputs with pinned environment.
- Apply correct statistics: power, effect size, multiple comparisons.
- Build dashboards with explicit owners and refresh cadence.
- Translate findings into recommendations with confidence ranges, not point estimates.
- Use dbt or equivalent to keep transforms versioned and testable.

## When NOT to use this skill

- model training (use ai-ml-development)
- production data pipeline ops (use devops-and-infrastructure or backend-development)

## Workflow

1. **Intake.** Read the user intent. Identify which capability above applies. If the request crosses
   into another discipline (e.g. UI + DB), call the `discipline-router` agent before splitting work.
2. **Inspect.** Look at the actual repo state with Read/Grep/Glob before proposing changes. Do not
   assume what code exists from project name alone.
3. **Source-check.** For non-obvious technical claims, ground the answer in the official sources
   listed in `references/official-sources.md`. Use the Context7 MCP for live doc lookups instead of
   relying on training-data memory for fast-moving APIs.
4. **Produce.** Generate the appropriate artifact from the list below.
5. **Verify.** Run every verification layer below before claiming done. Build success is not done.
   200 responses are not done. A real user seeing correct output is done.
6. **Hand back.** Report what shipped, what the visitor sees, what changed. No file paths, function
   names, or engineering jargon unprompted.

## Artifacts this skill produces

- Analysis plan: question, data, method, stop criteria.
- Notebook + Python/SQL with seed + env pin.
- Statistical methodology note.
- Dashboard with owner, refresh, and SLO.
- Decision memo: finding, confidence, recommended action.
- Data dictionary for the columns touched.

## Anti-patterns this skill pushes back against

- P-hacking via post-hoc test selection.
- Dashboards nobody owns; metrics drift silently.
- Pulling production data into a local CSV.
- Visualizations that hide uncertainty.
- Findings presented without a 'so what'.

## Verification required before claiming done

- Notebook re-runs end-to-end on a different machine.
- Statistical assumptions documented and checked.
- Dashboard owner + refresh wired into platform.
- Findings reviewed by a second analyst before publishing.

## Suggested commands

- `/uber:data analysis-plan --question='did onboarding v2 lift d7?'`
- `/uber:data dashboard-audit --area=revenue`
- `/uber:data ab-test power-analysis`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user can see the correct output of this work. Build success, deploy success, and 200
responses do not equal done. Every data surface explicitly handles loading, error, empty, and
populated states. Verification actually happened — no claim of "verified" without evidence.
