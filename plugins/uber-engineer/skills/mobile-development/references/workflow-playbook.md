# Mobile Development — Workflow Playbook

Long-form companion to `SKILL.md`. Apple-platform-first because the platform surface is heaviest
there; Android and cross-platform sections follow the same shape with different specifics.

## Phase 1 — Intake (5 minutes)

Ask once, then commit. Do not pile up clarifying questions.

1. Which sub-domain — Apple platforms, Android, or cross-platform?
2. Which surface specifically — a SwiftUI view, an App Intent, a Compose screen, an EAS update?
3. What does "done" mean for this discipline? (See `quality-rubric.md` for the platform-specific
   shipping ladders.)
4. What does the existing project look like? Read the Xcode project structure / Gradle variants /
   `eas.json` / `pubspec.yaml` before proposing.
5. Is there a deadline (App Store review window, TestFlight expiry, store-mandated SDK upgrade)?

If the request also touches another discipline (UI + DB, app + worker), call `discipline-router`
first. Sub-domain switches *within* mobile (iOS + Android) stay in this skill.

## Phase 2 — Source crawl

For any non-trivial technical claim:

1. Call Context7 MCP first for live docs.
2. Cross-check the relevant entries in `official-sources.md`:
   - **Apple** — Apple Developer documentation, Human Interface Guidelines, Swift Evolution,
     WWDC session videos, Xcode release notes, App Store Connect API docs.
   - **Android** — Android developer docs, Kotlin docs, Jetpack Compose docs, Material 3 spec,
     Play Console help.
   - **Cross-platform** — React Native docs, Expo / EAS docs, Flutter docs.
3. If a community blog is the only source, label the claim **non-authoritative** and prefer not
   to ship behavior from it without an official confirmation.

Never write SDK syntax from training memory for fast-moving APIs (SwiftUI, App Intents,
Compose, Expo SDK, Flutter packages). Always check the version in the project against the doc
version you're reading.

## Phase 3 — Plan

Write a 5–10 line plan before touching files. Include:

- The exact change and where (which target, which scheme, which variant, which package).
- The verification you'll run on a real device.
- The rollback if it goes wrong (which TestFlight build to restore, which Play track to roll
  back to, which EAS channel to revert).

## Phase 4 — Execute

Match the capability to the artifact. The mappings:

### Apple platforms

- **Choose between SwiftUI, UIKit, and SwiftUI-on-UIKit-host bridging for a given surface.** →
  Surface decision record naming the chosen approach and the bridging boundary if any.
- **Apply iOS 26 Liquid Glass surface treatment without breaking legibility for body text.** →
  Liquid Glass surface plan: where the effect is applied, fallback for older OS, legibility
  verification screenshot at body text size.
- **Adopt Swift 6 strict concurrency.** → Concurrency-safe data layer: MainActor boundaries,
  Sendable conformance, actor isolation, strict concurrency mode enabled in the scheme.
- **Build with App Intents, Widgets, Live Activities, App Clips, or Shortcuts.** → System entry
  point spec naming the intent / widget / activity, its parameters, and the deep link target.
- **Wire ASWebAuthenticationSession callback URLs through Universal Links + Associated Domains.** →
  Auth callback flow: `apple-app-site-association` entry, entitlement, callback handler, Keychain
  write on success, error states.
- **Manage Xcode Cloud workflows.** → Workflow spec distinguishing CI-only from
  Distribute + TestFlight workflow, with start condition, env vars, post-actions, notifications.
- **Walk the Apple shipping ladder.** → Ladder checklist (clean local build → device install →
  Xcode Cloud distribute green → TestFlight VALID → install list verification → ASC readiness
  green → submit for review).
- **Recover from App Store Review rejection.** → Reviewer notes preamble naming the rejection
  cause and the specific fix, plus a sign-in or feature walkthrough if reviewer credentials are
  needed.
- **Wire OSLog with structured subsystems and categories.** → OSLog wiring with subsystem per
  major component, category per concern, Privacy annotations, Console / Instruments query examples.
- **Ship Mac shells (SwiftUI on macOS or Mac Catalyst).** → Mac shell plan documenting which iOS
  view layer is shared, which AppKit interop is needed, window management strategy.

### Android

- **Build Compose-first surfaces with Material 3.** → Compose surface plan with dynamic color,
  edge-to-edge, predictive back, system bar contrast verification.
- **Configure Gradle build variants.** → Variant config with no URL leakage, signing config per
  variant, ProGuard / R8 rules, App Bundle output.
- **Wire WorkManager + FCM.** → Background sync schedule, FCM token refresh handler, deep link
  routing on receipt.
- **Ship through Play tracks.** → Play Console release plan: Internal → Closed → Production with
  rollout percentage, pre-launch report, release notes.

### Cross-platform

- **Decide native vs RN+Expo vs Flutter.** → Stack decision record with the constraints that
  would force a re-evaluation.
- **Configure EAS Build with channel-based OTA updates.** → EAS profile config per environment,
  channel-based update strategy with canary cohort, rollback path.
- **Bridge native modules.** → Native module spec with the JS surface, the iOS implementation,
  the Android implementation, and the failure-mode tests.

## Phase 5 — Verify

Walk the platform-specific shipping ladder in `quality-rubric.md`. Capture evidence:

- Apple — TestFlight install list screenshot, ASC readiness checks screenshot, Xcode Cloud build
  log link, OSLog filter output for the changed code path, MetricKit payload.
- Android — Play Console pre-launch report link, device install screenshot.
- Cross-platform — EAS build URL, OTA update channel verification, both-platform device
  installs.

Do not claim verification you didn't run. "Should work" is not verification.

## Phase 6 — Hand back

Tell the user:

- What shipped (in user terms — "this version is on TestFlight and the install list shows it",
  not "I tagged rc-X.Y.Z and Xcode Cloud workflow N concluded success").
- What's now true that wasn't before (visible behavior, store status, posture).
- What still needs attention with severity (e.g. "ASC readiness has one yellow check on
  encryption export compliance — needs your one-time answer in App Store Connect").

No "great question," no apology preambles, no transformation arcs.

## Edge cases

- **Project state surprises** — uncommitted changes in the iOS workspace, drifted Pods, missing
  Mac signing certificate. Stop and ask, don't paper over.
- **Conflicting docs** — when WWDC session, sample code, and forum post disagree, follow the
  most recent official source (WWDC > sample code > docs > forum).
- **Deadline pressure** — shrink scope, never shrink verification. An RC that wasn't
  device-installed is not a candidate for App Store submission regardless of the deadline.
- **Cross-discipline scope creep** — hand back to `discipline-router`. A push notification
  feature touches mobile (registration, refresh, deep link) AND backend (APNs token signer,
  payload composition, audience targeting) AND devops (APNs key rotation). Don't try to own all
  three.
- **Apple review rejection** — read the rejection in full (not just the headline). Address the
  cited cause first; don't bundle unrelated fixes into the resubmission.
- **Xcode Cloud quota exhausted** — runs cancel pre-start with `null` `cancelReason`. Check the
  ASC quota banner before assuming it's a credentials problem.
