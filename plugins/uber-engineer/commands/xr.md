---
description: AR/VR Development — invoke the ar-vr-development skill with focused intent.
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

# /uber:xr

Invoke the **ar-vr-development** skill for a AR/VR Development task.

## Usage

```
/uber:xr $ARGUMENTS
```

Common patterns:

- `/uber:xr frame-budget --hz=90`
- `/uber:xr spatial-ux scene-anchors`
- `/uber:xr comfort-settings`

## What this command does

1. Loads the `ar-vr-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

AR, VR, XR, spatial, Vision Pro, visionOS, Quest, Meta Horizon, ARKit, ARCore, WebXR, OpenXR, Unity XR, Unreal XR, RealityKit, RealityComposer, hand tracking, eye tracking, passthrough, motion sickness.
