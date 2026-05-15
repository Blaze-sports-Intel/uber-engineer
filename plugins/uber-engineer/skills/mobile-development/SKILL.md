---
name: mobile-development
description: "Apple-platform-first mobile engineering — iOS / iPadOS / macOS / visionOS / watchOS / tvOS — plus Android (Kotlin + Compose) and cross-platform (React Native + Expo, Flutter). Use when the user mentions: iOS, iPadOS, macOS, visionOS, watchOS, tvOS, Swift, SwiftUI, UIKit, AppKit, Xcode, Xcode Cloud, Distribution Preparation, TestFlight, App Store Connect, App Store, ASC API, App Clip, WidgetKit, StoreKit, Sign in with Apple, ASWebAuthenticationSession, Mac Catalyst, Liquid Glass, iOS 26, App Intents, OSLog, MetricKit, Swift Concurrency, MainActor, Sendable, actor isolation, Universal Links, Associated Domains, APNs, BGAppRefreshTask, BGProcessingTask, mobile app, native app, Android, Kotlin, Jetpack Compose, Material 3, Play Console, Google Play, FCM, React Native, Expo, EAS, Flutter, Dart, deep link, push notification, offline-first. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: web-only responsive work (use frontend-development); backend-only API design (use api-development); pure 3D scene work that isn't a shipped app (use game-development or ar-vr-development)."
---

# Mobile Development

Apple-platform-first mobile engineering — iOS, iPadOS, macOS, visionOS, watchOS, tvOS — with
explicit coverage of Android (Kotlin + Jetpack Compose) and cross-platform runtimes
(React Native + Expo, Flutter). The weight here is Apple because that's where the platform
gravity, signing surface, review queue, and shipping discipline are heaviest. Android and
cross-platform get their own clearly bounded sections.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words by sub-domain:

**Apple platforms** — iOS, iPadOS, macOS, visionOS, watchOS, tvOS, Swift, SwiftUI, UIKit, AppKit,
Xcode, Xcode Cloud, Distribution Preparation, TestFlight, App Store Connect, ASC API, App Clip,
WidgetKit, StoreKit 2, Sign in with Apple, ASWebAuthenticationSession, Mac Catalyst, Liquid Glass,
iOS 26, App Intents, OSLog, MetricKit, Swift Concurrency, MainActor, Sendable, actor isolation,
Universal Links, Associated Domains, APNs, BGAppRefreshTask, BGProcessingTask, Keychain, SharePlay.

**Android** — Android, Kotlin, Jetpack Compose, Material 3, Play Console, Google Play,
Firebase Cloud Messaging (FCM), Gradle variants, ProGuard / R8, App Bundle, Play Internal Testing,
WorkManager, Hilt, KSP.

**Cross-platform** — React Native, Expo, EAS Build / EAS Update, Hermes, Flutter, Dart,
Skia rendering, Kotlin Multiplatform, shared modules.

Use this skill when the user wants any of:

### Apple-platform work

- Choose between SwiftUI, UIKit, and SwiftUI-on-UIKit-host bridging for a given surface.
- Apply iOS 26 Liquid Glass surface treatment without breaking legibility for body text.
- Adopt Swift 6 strict concurrency: `@MainActor` boundaries, `Sendable` conformance, actor isolation.
- Build with App Intents, Widgets, Live Activities, App Clips, or Shortcuts as system entry points.
- Wire ASWebAuthenticationSession callback URLs through Universal Links + Associated Domains.
- Manage Xcode Cloud workflows: distinguish CI-only from Distribution + TestFlight upload workflows.
- Walk the Apple shipping ladder: dev → simulator → device → TestFlight → review → App Store.
- Recover from App Store Review rejection with a reviewer-notes preamble that names the cause
  and the fix.
- Wire OSLog with structured subsystems and categories so production logs are filterable.
- Ship Mac shells (SwiftUI on macOS or Mac Catalyst) that share the iOS view layer cleanly.

### Android work

- Build Compose-first surfaces with Material 3 dynamic color, edge-to-edge, and predictive back.
- Configure Gradle build variants for staging vs prod with no URL leakage.
- Wire WorkManager for background sync, FCM for push, and the platform refresh callback.
- Ship through Play Internal Testing → Closed Testing → Production with Play Console release notes.

### Cross-platform work

- Decide between native (Swift / Kotlin), React Native + Expo, and Flutter based on team,
  surface, and shipping cadence — and document why.
- Configure EAS Build for iOS + Android with channel-based OTA updates that don't break shipped users.
- Bridge native modules cleanly when the runtime hits its limit instead of forcing JS workarounds.

## When NOT to use this skill

- Web-only responsive work — use `frontend-development`.
- Backend-only API design or service architecture — use `api-development` or `backend-development`.
- Pure 3D scene work that isn't a shipped app — use `game-development` or `ar-vr-development`.
- Server-side push delivery infrastructure (APNs token signing service, FCM relay) — that's
  `backend-development`. The mobile side of push (registration, refresh callback, deep link
  routing on receipt) is in scope here.

## Workflow

1. **Intake.** Read the user intent. Identify which sub-domain applies (Apple, Android, cross-platform).
   If the request crosses sub-domains (e.g. ship the same feature on iOS and Android), call
   `discipline-router` only if other disciplines are also involved — otherwise stay here and
   produce parallel artifacts.
2. **Inspect.** Read the actual project before proposing. For Apple: check the Xcode project
   structure (which targets, which schemes, which Xcode Cloud workflows exist). For Android: check
   `build.gradle.kts` variants. For cross-platform: check `app.json` / `eas.json` / `pubspec.yaml`.
3. **Source-check.** For non-trivial claims, ground in the official sources listed in
   `references/official-sources.md` — WWDC sessions, Swift Evolution proposals, Xcode release
   notes, ASC API docs, Android Codelabs. Use Context7 MCP for live doc lookups instead of
   training-data memory.
4. **Plan.** Write a 5–10 line plan. Include the exact change, the verification you'll run on a
   physical device, and the rollback path (TestFlight reject + restore previous build, Play
   rollback, EAS channel revert).
5. **Execute.** Match the capability to the artifact (see Phase 4 in `workflow-playbook.md`).
6. **Verify.** Walk the platform-specific shipping ladder. Build success on a Mac is not done.
   Xcode Cloud green is not done. TestFlight upload is not done. A real install on a real device
   showing the right thing is done. See `quality-rubric.md` for the matrix.
7. **Hand back.** Report what shipped, what a real installer of the build sees, what changed.
   Plain English. No file paths, no Swift identifiers, no Xcode UI navigation breadcrumbs unless
   the user specifically asked.

## Apple Build Evidence Loop

The single most important discipline this skill enforces. Apple's tooling has too many places
where "build succeeded" can be a lie. The loop:

1. **Local xcodebuild build clean** — before tagging any release candidate, run a clean build
   locally. PR-level CI doesn't catch post-merge `main` drift.
2. **Confirm Xcode Cloud workflow targeting** — there are typically two workflows: a CI-only
   workflow (no archive, no TestFlight upload) and a "distribute" workflow (Distribution Preparation
   post-action + TestFlight upload action). Tag the branch the *distribute* workflow watches.
3. **Watch the Xcode Cloud run** — `conclusion: action_required` is **not** a manual approval
   gate; it means compile errors. Read `output.summary` Errors count.
4. **Distinguish Archive ≠ Upload ≠ Install.** A build can be archived without being uploaded.
   It can be uploaded without finishing TestFlight processing. It can finish processing without
   appearing on a tester's install list. Don't claim "live on TestFlight" until the install list
   on a real device shows the build.
5. **Build numbers are auto-incremented at archive time** by Xcode Cloud above whatever number
   sits in `pbxproj`. Read the actual TestFlight build number from App Store Connect, not from
   the project file.
6. **Merge release branch back to main same day** any time a `release/*` branch produces a binary
   that's archived to App Store Connect. Skipping this causes the next RC to drift and miss the
   recent fixes.

## Artifacts this skill produces

- **Stack decision record** — chosen runtime (native Swift / native Kotlin / RN+Expo / Flutter),
  why, what would force a re-evaluation, and which native escape hatches are available.
- **Apple shipping ladder checklist** — per-build: clean local build → device install → Xcode
  Cloud distribute run → TestFlight processing complete → install list verification → reviewer
  notes drafted → submit for review → release.
- **App Store Connect submission package** — version metadata, what's-new copy, screenshots
  captured at the right device sizes, reviewer notes with cause-of-fix preamble when a prior
  rejection exists, demo account credentials when login is required.
- **Xcode Cloud workflow spec** — start condition, environment variables, post-actions
  (Distribution Preparation, TestFlight upload), notifications.
- **Concurrency-safe data layer** — explicit MainActor boundaries on UI-touching types, Sendable
  conformance on shared models, actor isolation for caches and stores. Strict concurrency mode on.
- **Liquid Glass surface treatment plan** — where the effect is applied, fallback for older OS,
  legibility check at body text size against worst-case background.
- **Push + deep link matrix** — per notification type: trigger, audience, payload, deep link
  destination, expiration, what happens when the user taps from cold launch vs background.
- **Universal Links + Associated Domains setup** — `apple-app-site-association` file at the
  right path with `applinks` entries that match the app's entitlements.
- **Authentication flow** — Sign in with Apple, ASWebAuthenticationSession callback URL handler,
  Keychain storage with the right access group, token refresh policy.
- **Background work plan** — BGAppRefreshTask vs BGProcessingTask choice, scheduling cadence,
  what happens when the OS denies the request, fallback paths.
- **OSLog wiring** — subsystem and category per major component, log levels mapped to severity,
  Privacy annotations on sensitive values, Console / Instruments query examples.
- **MetricKit wiring** — `MXMetricManager` subscriber, payload aggregation, dashboard surfaces.
- **Mac shell plan** — SwiftUI on macOS or Mac Catalyst, which iOS view layer is shared, which
  AppKit interop points are needed, window management strategy.
- **Android equivalents** — Compose surface plan, Material 3 dynamic color choice, Gradle
  variant config, WorkManager schedule, FCM token refresh handler, Play Console rollout strategy.
- **Cross-platform release plan** — EAS Build profiles per environment, channel-based OTA update
  strategy with canary cohort, native escape-hatch points documented.

## Anti-patterns this skill pushes back against

The catalog with concrete fixes lives in `references/anti-patterns.md`. Highlights:

- "Action Required" in Xcode Cloud read as a manual approval gate. It means compile errors.
- Tagging an RC without running `xcodebuild build` locally first.
- Release branch archived to App Store Connect but never merged back to `main`.
- Claiming "live on TestFlight" before the install list on a real device shows the build.
- Hardcoded API URLs that ship to TestFlight and prod alike instead of varying per scheme.
- Permissions requested on launch instead of in context.
- Push tokens not refreshed; users silently lose notifications after rotation.
- Liquid Glass overlays applied to body text without legibility verification on worst-case
  background.
- ASWebAuthenticationSession callback URL not registered in Associated Domains, so the callback
  never fires.
- @MainActor missing on UI-touching functions; data race surfaces in production logs.
- Force-unwrapping optionals on async data that legitimately can be nil.
- Web layouts copy-pasted into mobile without redesign for thumb reach.
- Treating the simulator as 'tested' — never run on a physical device with real network.
- Compose surfaces ignoring predictive back and edge-to-edge.
- React Native bridge calls in hot paths instead of native module work.
- Flutter pixel-perfect on one platform but never tested on the other.

## Verification required before claiming done

### Apple platforms

- Local `xcodebuild build` clean against the active scheme on the latest Xcode.
- Build installs and launches on a physical device on cellular (LTE + 5G), low battery mode, and
  one device two generations old.
- Xcode Cloud distribute workflow concluded `success`; TestFlight build state `VALID`.
- Build appears in the install list of a real TestFlight tester.
- VoiceOver pass for changed flows; dynamic type at xxxLarge does not clip.
- Light + dark mode parity.
- Privacy nutrition labels reflect any new data collection.
- App Store Connect submission shows green readiness checks before submit.

### Android

- Build installs and launches on a physical device with Play Services and one Android Go device.
- Compose surfaces respect predictive back and edge-to-edge with system bar contrast verified.
- TalkBack pass for changed flows.
- Play Console pre-launch report passes.
- ProGuard / R8 mapping uploaded.

### Cross-platform

- iOS and Android builds both pass their respective device checks above.
- OTA update mechanism tested — issue an update on a canary channel, verify roll forward and
  roll back.

### All platforms

- Crash-free session rate ≥ 99.5% in the most recent comparable release.
- Offline mode: cached data renders, writes queue, sync resumes on reconnect.
- Background: push wakes the app, deep link routes to the correct screen from cold launch.

## Suggested commands

- `/mobile ship-ios <build|tag>` — walk the Apple Build Evidence Loop end to end.
- `/mobile asc-submit <version>` — draft App Store Connect submission with reviewer notes.
- `/mobile concurrency-audit <module>` — Swift 6 actor isolation + Sendable check.
- `/mobile a11y-audit ios <feature>` — VoiceOver + dynamic type + contrast verification.
- `/mobile a11y-audit android <feature>` — TalkBack + Material 3 contrast verification.
- `/mobile push-matrix <feature>` — push + deep link routing plan.
- `/mobile offline-strategy <feature>` — offline-first sync contract.
- `/mobile mac-shell <feature>` — SwiftUI-on-macOS shell from existing iOS view layer.

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs for every sub-domain.
- `references/workflow-playbook.md` — long-form workflow with Phase 4 capability→artifact mapping.
- `references/anti-patterns.md` — anti-pattern catalog with concrete fixes.
- `references/quality-rubric.md` — pass/fail rubric with platform-specific shipping ladders.
- `references/examples.md` — real before/after invocations including rejection-recovery pattern.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references via the shared
  plugin-level validator.

## Definition of done

A real installer of the shipped build experiences the correct outcome of this work on the device
they actually use. Build success on the maintainer's Mac is not done. Xcode Cloud green is not
done. TestFlight upload is not done. The discipline-specific states below all need to hold:

- **Apple shipping ladder** — clean local build, device install, Xcode Cloud distribute green,
  TestFlight processing VALID, install list shows the build on a real tester device, ASC
  readiness checks all green.
- **Android shipping ladder** — device install, pre-launch report green, Play Console rollout to
  Internal Testing tier verified before any Production rollout.
- **Online** — feature works against the staging API for the active scheme/variant.
- **Offline** — cached data renders, writes queue, sync resumes on reconnect.
- **Background** — push wakes the app, deep link routes to the correct screen from cold launch
  and from background.
- **Accessibility** — VoiceOver / TalkBack pass for the new flow; dynamic type at xxxLarge does
  not clip; contrast meets WCAG AA.
- **Concurrency** — strict concurrency mode passes; no data races in the changed code.

Verification actually happened — evidence captured (TestFlight install screenshot, ASC readiness
screenshot, OSLog filter output, MetricKit payload, Play Console pre-launch report).
