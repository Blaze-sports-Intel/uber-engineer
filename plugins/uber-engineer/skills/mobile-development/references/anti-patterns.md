# Mobile Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path. Apple-platform anti-patterns
weigh heaviest because that's where the most damage happens silently.

## Apple platforms

### "Action Required" in Xcode Cloud read as a manual approval gate.

**Fix:** `conclusion: action_required` in Xcode Cloud means **compile errors**, not a manual
gate. Read `output.summary` and look for the Errors count. Fix the errors and re-run. Don't sit
in App Store Connect waiting for an Approve button that doesn't exist.

### Tagging an RC without running `xcodebuild build` locally first.

**Fix:** PR-level CI runs against the PR branch. Once merged to `main`, fresh drift can land
that the PR didn't see. Two-minute local `xcodebuild build` before tagging vs ten-minute Xcode
Cloud round-trip plus burned quota — do the local build first, every time.

### Release branch archived to App Store Connect but never merged back to `main`.

**Fix:** The moment a `release/*` branch produces a binary that's archived to ASC, merge it back
to `main` same day, before any other PR lands. Skipping this causes the next RC to drift and
miss the recent fixes — and rejection-recovery cycles compound the drift.

### Claiming "live on TestFlight" before the install list on a real device shows the build.

**Fix:** Three distinct steps live between "archived" and "installable": Archive ≠ Upload ≠
Install. A build can be archived without being uploaded (post-action missing). It can be uploaded
without finishing TestFlight processing. It can finish processing without appearing on a tester's
install list (group not assigned, processing held for export compliance question). Walk all
three. Don't say "live" until the install list shows it.

### TestFlight build numbers read from `pbxproj` instead of from App Store Connect.

**Fix:** Xcode Cloud auto-increments build numbers above whatever number sits in `pbxproj` at
archive time. If the project file says `351`, TestFlight may show `384`. Read the actual
TestFlight build number from ASC (or via the ASC API), not from the project file.

### Hardcoded API URLs that ship to TestFlight and prod alike.

**Fix:** Move the base URL into a build configuration that varies per scheme. Verify TestFlight
builds hit staging, App Store builds hit prod, and no environment leaks across. Add a runtime
log line that reports which environment the active build is talking to, so a tester can confirm.

### Permissions requested on launch instead of in context.

**Fix:** Defer permission prompts until the user attempts the action that requires them. Camera
prompt when they tap the camera icon, location prompt when they open the map. Pre-prompt screen
explains why before the OS dialog. Apple Review will reject blanket on-launch prompts.

### Push tokens not refreshed; users silently lose notifications after rotation.

**Fix:** Implement `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`. Sync the
new token to the backend on app launch and on rotation. Verify by uninstalling + reinstalling
and confirming pushes resume.

### Liquid Glass overlays applied to body text without legibility verification.

**Fix:** Liquid Glass is a backdrop effect; body text on top of it can lose contrast against
worst-case wallpaper or background imagery. Verify legibility at body text size against the worst
plausible background (high-contrast image, dark photo, busy gradient). If contrast fails, add a
solid material layer behind the text or skip the effect for that surface.

### ASWebAuthenticationSession callback URL not registered in Associated Domains.

**Fix:** The callback never fires. Add the `applinks:` entry to the entitlement, host the
`apple-app-site-association` file at `https://<domain>/.well-known/apple-app-site-association`
with the right `appID` and path patterns, and verify with `swcutil verify -d <domain>` from a Mac.

### `@MainActor` missing on UI-touching functions; data race surfaces in production.

**Fix:** Enable strict concurrency mode in the scheme. Add `@MainActor` to view models and any
type that touches `@State`, `@Observable`, or UIKit/AppKit. Use `actor` for mutable shared
state. Add `Sendable` conformance to types crossing actor boundaries. The compiler errors are
cheap; the production data race is not.

### Force-unwrapping optionals on async data that legitimately can be nil.

**Fix:** Replace `data!` with `guard let data else { return }` or `if let data`. Async fetches
fail. The optional is the contract. Force-unwrap means the test path didn't include the failure
case.

### Web layouts copy-pasted into the mobile app without redesign for thumb reach.

**Fix:** Move primary actions into the bottom 30% of the screen. Replace hover affordances with
long-press or a visible button. Verify thumb reach at iPhone SE width and Pro Max width.

### Treating the simulator as 'tested' — never run on a physical device with real network.

**Fix:** Add a 'physical device pass' to the release checklist. Test on cellular (LTE + 5G), low
battery mode, and at least one device two generations old. The simulator misses APNs, Keychain
biometrics, real network conditions, and thermal throttling.

### Shipping a v1 with a known sign-in failure and hoping reviewer doesn't hit it.

**Fix:** They will hit it. Lead the reviewer notes with a one-paragraph preamble naming the
known cause, the fix in this build, and the credential to use for testing. Save the rejection
cycle.

## Android

### Compose surface ignoring predictive back and edge-to-edge.

**Fix:** Use `BackHandler` for predictive back. Set `enableEdgeToEdge()` in the Activity. Verify
system bar contrast on light and dark themes. Material 3 surfaces should follow dynamic color
unless brand override is required.

### Gradle variants that leak prod URLs into staging builds.

**Fix:** Define `buildConfigField` per `productFlavor`, not per `buildType`. Verify by greping
the APK with `apkanalyzer dex packages` for hardcoded URLs.

### FCM token refresh handler not implemented.

**Fix:** Override `FirebaseMessagingService.onNewToken`. Sync to backend on launch and on
rotation. Verify by clearing app data and confirming pushes resume.

## Cross-platform (React Native + Expo, Flutter)

### React Native bridge calls in hot paths.

**Fix:** Profile with Flipper or Hermes profiler. Move hot-path work to a native module exposed
via TurboModules. JS-side optimization in a hot loop usually loses to a 50-line native module.

### Flutter pixel-perfect on one platform, never tested on the other.

**Fix:** Run on a physical iOS device AND a physical Android device for every shipped build.
Material widgets render differently than Cupertino widgets; the gold-master screenshot from one
platform is not evidence for the other.

### EAS Update channel mishandled — production users get a staging update.

**Fix:** Channel names match scheme/variant. Verify the update channel in `eas.json` matches the
build profile. Test the OTA mechanism end-to-end on a canary cohort before broad rollout. Have a
rollback channel ready.

### Native escape hatches mocked instead of implemented.

**Fix:** When the cross-platform runtime hits its limit (camera filters, deep linking edge
cases, biometrics), implement the native module properly on both platforms. Mocking the JS
surface and shipping anyway means the feature works in dev and breaks in TestFlight.

## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
