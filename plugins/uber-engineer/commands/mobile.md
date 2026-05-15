---
description: Mobile Development — invoke the mobile-development skill with focused intent.
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

# /uber:mobile

Invoke the **mobile-development** skill for a Mobile Development task.

## Usage

```
/uber:mobile $ARGUMENTS
```

Common patterns:

- `/uber:mobile a11y-audit ios Sources/Checkout`
- `/uber:mobile testflight-prep --build=42`
- `/uber:mobile offline-strategy src/features/cart`

## What this command does

1. Loads the `mobile-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

iOS, Swift, SwiftUI, Xcode, Android, Kotlin, Jetpack Compose, React Native, Expo, Flutter, Dart, TestFlight, App Store, Play Store, mobile app, Liquid Glass, deep link, push notification, offline-first.
