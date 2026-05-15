---
name: ar-vr-development
description: "Spatial UX, perf budgets, motion comfort, anchors, hand/eye input, and platform-specific deploy. Use when the user mentions: AR, VR, XR, spatial, Vision Pro, visionOS, Quest, Meta Horizon, ARKit, ARCore, WebXR, OpenXR, Unity XR, Unreal XR, RealityKit, RealityComposer, hand tracking, eye tracking, passthrough, motion sickness. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: flat 2D UI work (use frontend-development); mobile non-XR apps (use mobile-development)."
---

# AR/VR Development

Spatial UX, perf budgets, motion comfort, anchors, hand/eye input, and platform-specific deploy.

This skill is one of 17 discipline skills in the **uber-engineer** plugin. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: AR, VR, XR, spatial, Vision Pro, visionOS, Quest, Meta Horizon, ARKit, ARCore, WebXR, OpenXR, Unity XR, Unreal XR, RealityKit, RealityComposer, hand tracking, eye tracking, passthrough, motion sickness.

Use when the user wants any of:

- Apply spatial UX patterns: comfort zones, depth cues, occlusion, anchors.
- Hit headset frame budgets (72/90/120 Hz) without dropping below threshold.
- Choose input modality: hand, controller, gaze + pinch, voice.
- Manage motion comfort: vignettes, snap turn, comfortable locomotion.
- Handle passthrough vs full VR transitions.
- Ship to App Store / Horizon Store with platform-specific assets.

## When NOT to use this skill

- flat 2D UI work (use frontend-development)
- mobile non-XR apps (use mobile-development)

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

- Spatial UX spec: anchor strategy, occlusion, depth zones.
- Frame budget breakdown per platform.
- Input modality matrix.
- Comfort settings: snap turn, vignette, sitting/standing.
- Store listing assets + privacy disclosures.
- Accessibility plan: subtitles, color, contrast, alternate input.

## Anti-patterns this skill pushes back against

- Reading-heavy UI floating in space without anchors.
- Camera-coupled UI that induces sickness.
- Fixed 'forward' assumed; no recenter affordance.
- Hand-only input without controller fallback.
- Ignoring passthrough boundary in mixed reality.

## Verification required before claiming done

- Tested on a physical headset, not just simulator.
- Frame rate stays at platform target for 5+ minutes.
- Comfort options available in settings and exposed early.
- Privacy disclosures complete: camera, hand, eye, room data.
- Store review checklist signed off.

## Suggested commands

- `/uber:xr frame-budget --hz=90`
- `/uber:xr spatial-ux scene-anchors`
- `/uber:xr comfort-settings`

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
