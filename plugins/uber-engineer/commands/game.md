---
description: Game Development — invoke the game-development skill with focused intent.
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

# /uber:game

Invoke the **game-development** skill for a Game Development task.

## Usage

```
/uber:game $ARGUMENTS
```

Common patterns:

- `/uber:game profile-frame`
- `/uber:game asset-pipeline --type=texture`
- `/uber:game save-migration v3 -> v4`

## What this command does

1. Loads the `game-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

game, Unity, Unreal, Godot, Phaser, Three.js, React Three Fiber, Bevy, ECS, frame budget, draw call, asset pipeline, shader, physics, input system, save system, sprite, GLTF, GLB.
