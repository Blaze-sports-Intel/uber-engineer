# Mobile Development — Quality Rubric

Use this rubric on PR review or before claiming any task done. Walk the platform-specific
shipping ladder for the platforms the change touches.

## Apple-platform shipping ladder

| # | Check | Result |
|---|-------|--------|
| 1 | Local `xcodebuild build` clean against the active scheme on the latest Xcode. | pass / fail |
| 2 | Build installs on a physical device (not just simulator). | pass / fail |
| 3 | Tested on cellular (LTE + 5G) and low battery mode. | pass / fail |
| 4 | Tested on one device two generations old. | pass / fail |
| 5 | Xcode Cloud distribute workflow (the one with Distribution Preparation + TestFlight upload) concluded `success`. | pass / fail |
| 6 | TestFlight build state shows `VALID` (not `processing`, not `invalid`). | pass / fail |
| 7 | Build appears in the install list of a real TestFlight tester (not just in the build list). | pass / fail |
| 8 | VoiceOver pass for changed flows. | pass / fail |
| 9 | Dynamic type at xxxLarge does not clip. | pass / fail |
| 10 | Light + dark mode parity. | pass / fail |
| 11 | Strict concurrency mode passes; no data races in changed code. | pass / fail |
| 12 | Liquid Glass surfaces (if used) verified for legibility against worst-case background. | pass / fail / n/a |
| 13 | OSLog subsystem and category present on changed code paths. | pass / fail |
| 14 | App Store Connect submission shows green readiness checks before submit. | pass / fail / n/a |
| 15 | Reviewer notes draft includes cause-of-fix preamble if a prior rejection exists. | pass / fail / n/a |
| 16 | Release branch merged back to `main` same day after archive (if applicable). | pass / fail / n/a |

## Android shipping ladder

| # | Check | Result |
|---|-------|--------|
| 1 | Gradle build clean for the target variant. | pass / fail |
| 2 | Installs on a physical device with Play Services. | pass / fail |
| 3 | Tested on one Android Go device. | pass / fail |
| 4 | Compose surfaces respect predictive back. | pass / fail |
| 5 | Edge-to-edge enabled with verified system bar contrast. | pass / fail |
| 6 | TalkBack pass for changed flows. | pass / fail |
| 7 | Play Console pre-launch report passes. | pass / fail |
| 8 | ProGuard / R8 mapping uploaded to Play Console. | pass / fail |
| 9 | App Bundle (not raw APK) uploaded. | pass / fail |
| 10 | Release notes drafted in Play Console. | pass / fail |

## Cross-platform shipping ladder

| # | Check | Result |
|---|-------|--------|
| 1 | iOS shipping ladder above passes for the iOS build. | pass / fail |
| 2 | Android shipping ladder above passes for the Android build. | pass / fail |
| 3 | EAS Build URL captured for both platforms. | pass / fail |
| 4 | OTA update tested on a canary channel — roll forward verified. | pass / fail / n/a |
| 5 | OTA update rollback path verified on the canary channel. | pass / fail / n/a |
| 6 | Native escape-hatch points documented for any feature that needed bridging. | pass / fail / n/a |

## Cross-cutting (every platform)

| # | Check | Result |
|---|-------|--------|
| 1 | Crash-free session rate ≥ 99.5% on the most recent comparable release. | pass / fail |
| 2 | Offline mode: cached data renders, writes queue, sync resumes on reconnect. | pass / fail |
| 3 | Background: push wakes the app, deep link routes correctly from cold and background launch. | pass / fail / n/a |
| 4 | Privacy nutrition labels reflect any new data collection. | pass / fail / n/a |
| 5 | API base URL verified to match the active scheme/variant (no environment leakage). | pass / fail |

## Definition of done

A real installer of the shipped build experiences the correct outcome on the device they
actually use. Build success on the maintainer's Mac is not done. Xcode Cloud green is not done.
TestFlight upload is not done. The discipline-specific states below all need to hold:

- **Apple shipping ladder** — every applicable row above is `pass`.
- **Android shipping ladder** — every applicable row above is `pass`.
- **Cross-platform shipping ladder** — every applicable row above is `pass`.
- **Online** — feature works against the staging API for the active scheme/variant.
- **Offline** — cached data renders, writes queue, sync resumes on reconnect.
- **Background** — push wakes the app, deep link routes correctly.
- **Accessibility** — VoiceOver / TalkBack pass; dynamic type at xxxLarge does not clip;
  contrast meets WCAG AA.
- **Concurrency** — strict concurrency mode passes; no data races in the changed code.

Plus the cross-cutting baseline:

- Verification actually happened — evidence captured (screenshots, log filters, MetricKit
  payloads, ASC readiness shots, Play pre-launch report).
- Rollback plan exists and someone other than the author could execute it (which TestFlight
  build to restore, which Play track to roll back to, which EAS channel to revert).

## Failure modes that block "done"

- Tests pass on the simulator but real-world behavior on device is wrong.
- Xcode Cloud is green but the build never made it to a tester's install list.
- The author "checked" without producing evidence.
- A claim of verification that wasn't actually run.
- App Store Review rejected the prior submission and the resubmission doesn't address the cited
  cause.
- Release branch archived but not merged back to `main` same day — the next RC will drift.
