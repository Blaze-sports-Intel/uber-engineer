---
description: Data Science Development — invoke the data-science-development skill with focused intent.
argument-hint: <action> [target] [flags]
allowed-tools:
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Bash
  - Task
---

# /uber:data

Invoke the **data-science-development** skill for a Data Science Development task.

## Usage

```
/uber:data $ARGUMENTS
```

Common patterns:

- `/uber:data analysis-plan --question='did onboarding v2 lift d7?'`
- `/uber:data dashboard-audit --area=revenue`
- `/uber:data ab-test power-analysis`

## What this command does

1. Loads the `data-science-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

data analysis, data science, notebook, Jupyter, pandas, Polars, DuckDB, Spark, dbt, Airflow, Dagster, Prefect, Streamlit, Plotly, Tableau, Looker, hypothesis test, A/B test, cohort analysis.
