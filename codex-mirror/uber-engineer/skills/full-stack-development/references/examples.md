# Full-Stack Development — Examples

Concrete invocations and before/after patterns.

## Slash command invocations

```
/uber:fullstack ship-feature 'add saved search to product index'
```

```
/uber:fullstack vertical-slice src/features/checkout
```

```
/uber:fullstack flag-rollout new-onboarding --percent=10
```


## Before / after pattern

**Before:** A developer asks for a generic improvement.

> "Make this faster."

**After:** Skill rewrites the request as a measurable task.

> "Profile the route, identify the top three contributors to LCP, propose changes, measure again,
> hold a budget of LCP ≤ 2.5s on 3G mid-tier hardware."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- The other 16 skills in this plugin when scope expands.
