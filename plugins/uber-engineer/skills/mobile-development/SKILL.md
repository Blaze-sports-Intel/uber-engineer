---
name: mobile-development
description: "Native iOS, native Android, and cross-platform mobile with build, test, store, and offline constraints. Use when the user mentions: iOS, Swift, SwiftUI, Xcode, Android, Kotlin, Jetpack Compose, React Native, Expo, Flutter, Dart, TestFlight, App Store, Play Store, mobile app, Liquid Glass, deep link, push notification, offline-first. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: web-only responsive work (use frontend-development); backend-only API design."
---

# Mobile Development

Native iOS, native Android, and cross-platform mobile with build, test, store, and offline constraints.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: iOS, Swift, SwiftUI, Xcode, Android, Kotlin, Jetpack Compose, React Native, Expo, Flutter, Dart, TestFlight, App Store, Play Store, mobile app, Liquid Glass, deep link, push notification, offline-first.

Use when the user wants any of:

- Choose between native (Swift/Kotlin), Expo/React Native, and Flutter based on team and surface.
- Design offline-first sync that resolves conflicts deterministically.
- Handle background tasks, push, and permissions within OS limits.
- Wire up TestFlight / Play Console internal tracks with structured release notes.
- Apply iOS HIG and Material 3 conventions — not invent custom navigation.
- Manage code signing, provisioning, and OTA updates without breaking shipped users.

## When NOT to use this skill

- web-only responsive work (use frontend-development)
- backend-only API design

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

- Native build configuration (Xcode scheme / Gradle variant) with signing strategy.
- Offline sync contract: source of truth, conflict policy, retry budget.
- Push notification matrix: trigger, audience, deep link, expiration.
- TestFlight / internal track release checklist.
- Accessibility audit: VoiceOver / TalkBack labels, dynamic type, contrast.
- Crash analytics dashboard wiring.

## Anti-patterns this skill pushes back against

- Web layouts copy-pasted into mobile without redesign for thumb reach.
- Permissions requested on launch instead of in context.
- Treating the simulator as 'tested' — never run on a physical device with real network.
- Push tokens not refreshed; users silently lose notifications after token rotation.
- Hardcoded API URLs that ship to TestFlight and prod alike.

## Verification required before claiming done

- Builds and launches on a physical iOS device + physical Android device.
- TestFlight build passes Apple's automated checks.
- VoiceOver and TalkBack pass for changed flows.
- Offline mode: app loads cached data, queues writes, syncs on reconnect.
- Crash-free session rate ≥ 99.5% in the last release.

## Suggested commands

- `/mobile a11y-audit ios Sources/Checkout`
- `/mobile testflight-prep --build=42`
- `/mobile offline-strategy src/features/cart`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below must all hold:

- Builds and launches on a physical iOS device + physical Android device.
- Online: feature works against staging API.
- Offline: cached data renders, writes queue, sync resumes on reconnect.
- Background: push wakes the app, deep link routes to the correct screen.
- Accessibility: VoiceOver + TalkBack pass for the new flow.

Verification actually happened — no claim of "verified" without evidence.
