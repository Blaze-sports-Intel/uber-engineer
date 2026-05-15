# Mobile Development — Examples

Concrete invocations and a before/after pattern grounded in the Apple Build Evidence Loop.

## Slash command invocations

```
/mobile ship-ios rc-2026-05-14
```

```
/mobile asc-submit 1.4.0
```

```
/mobile concurrency-audit Sources/Standings
```

```
/mobile a11y-audit ios Sources/GameDetail
```

```
/mobile a11y-audit android app/src/main/java/com/app/gamedetail
```

```
/mobile push-matrix game-final-alerts
```

```
/mobile mac-shell home-tab
```

The `/uber` router will dispatch to `/mobile` after reading the request. You can also call the
discipline command directly when you already know the discipline.

## Before / after — vague mobile request

**Before:** A vague request that hides the real work.

> "Build a saved-items list for the iOS app."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Pick SwiftUI for this surface (single-platform shipping today, Mac shell to follow). Local
> SQLite (via SwiftData) is the source of truth; server is eventual. MainActor on the view model;
> Sendable on the model; actor isolation for the cache. VoiceOver labels with dynamic type
> support. Universal Links for the share-to-app deep link. OSLog subsystem
> `com.app.savedItems`, categories `cache`, `sync`, `ui`. Verification ladder: clean local
> `xcodebuild build` → install on physical iPhone → cellular + low battery test → Xcode Cloud
> distribute green → TestFlight install list verified. No App Store submission until rollback
> plan documented (which TestFlight build to restore)."

## Before / after — App Store rejection recovery

**Before:** Generic resubmission notes.

> "Fixed the issue, please re-review."

**After:** Reviewer notes preamble that names cause and fix.

> "Reviewer notes — preamble. Build 114 addresses the rejection of build 88 cited under
> Guideline 2.1 (sign-in failure). Cause: the auth callback URL was registered as a URL Scheme
> but not as a Universal Link, so the callback never fired on devices with the app installed.
> Fix in this build: Universal Link entry added to the Associated Domains entitlement, the
> `apple-app-site-association` file is hosted at the canonical path, and the callback handler
> writes the credential to Keychain on success. Tested on a clean install on iPhone 15 Pro and
> iPhone SE 3rd gen. Demo credential: <redacted, in App Review Info>. Walk-through: tap Sign In,
> complete OAuth in the system sheet, verify the home tab loads with the user's saved items."

## Before / after — Xcode Cloud "Action Required" misread

**Before:** Treating the status as a manual gate.

> "Xcode Cloud says action required. Waiting for Austin to approve in App Store Connect."

**After:** Read the build output and act.

> "`conclusion: action_required` is Xcode Cloud's signal for compile errors, not a manual
> approval gate. Build output summary: 3 errors. Top error:
> `'try' expression at top level not allowed`. Source file changed in commit
> `<sha>`. Reverting that hunk and re-running the workflow."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses into backend, devops, or design surfaces.
- `build-validator` agent — before claiming verification on a tagged RC.
- `code-reviewer` agent — before merging mobile PRs.
- `ship-auditor` agent — before declaring an App Store or Play release complete.
- `api-development` skill — for the wire contract the app speaks against.
- `backend-development` skill — for APNs / FCM relay infrastructure.
- `security-development` skill — for Keychain, Sign in with Apple, biometric flows.
- `test-and-quality-assurance` skill — for snapshot tests, UI tests, and pre-launch report
  triage.
