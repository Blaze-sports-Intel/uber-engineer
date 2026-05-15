# AR/VR Development — Examples

Concrete invocations and before/after patterns.

## Slash command invocations

```
/uber:xr frame-budget --hz=90
```

```
/uber:xr spatial-ux scene-anchors
```

```
/uber:xr comfort-settings
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
