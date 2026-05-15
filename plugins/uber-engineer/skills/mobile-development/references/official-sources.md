# Official Sources for Mobile Development

Ground every non-obvious technical claim in these sources. Community sources (blogs, Stack
Overflow, Reddit) are non-authoritative and may be used only as implementation inspiration.

## Apple platforms (always check first for Apple work)

### Documentation

- [Apple Developer Documentation](https://developer.apple.com/documentation/) — root.
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) —
  including the iOS 26 Liquid Glass material guidance.
- [Swift Documentation](https://www.swift.org/documentation/) — language reference and the
  concurrency model.
- [Swift Evolution](https://www.swift.org/swift-evolution/) — accepted proposals for the active
  Swift version.
- [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui).
- [App Intents](https://developer.apple.com/documentation/appintents).
- [WidgetKit](https://developer.apple.com/documentation/widgetkit).
- [StoreKit 2](https://developer.apple.com/documentation/storekit).
- [BackgroundTasks](https://developer.apple.com/documentation/backgroundtasks) — BGAppRefreshTask
  and BGProcessingTask.
- [User Notifications](https://developer.apple.com/documentation/usernotifications) — APNs
  registration and handler contract.
- [Universal Links](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)
  + [Associated Domains](https://developer.apple.com/documentation/xcode/configuring-an-associated-domain).
- [Authentication Services](https://developer.apple.com/documentation/authenticationservices) —
  ASWebAuthenticationSession, Sign in with Apple.
- [OSLog + os.signpost](https://developer.apple.com/documentation/os/logging) — structured
  logging with subsystems and categories.
- [MetricKit](https://developer.apple.com/documentation/metrickit) — payload-driven device
  diagnostics.

### Build, distribute, review

- [Xcode Release Notes](https://developer.apple.com/documentation/xcode-release-notes).
- [Xcode Cloud Documentation](https://developer.apple.com/documentation/xcode/xcode-cloud).
- [App Store Connect Documentation](https://developer.apple.com/help/app-store-connect/).
- [App Store Connect API Reference](https://developer.apple.com/documentation/appstoreconnectapi).
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).
- [Privacy and Data Use](https://developer.apple.com/app-store/app-privacy-details/).

### WWDC sessions (treat as authoritative)

- WWDC session videos at <https://developer.apple.com/videos/> — filter by year and topic. Always
  check the most recent year's sessions for any API you're touching.

## Android

- [Android Developer Documentation](https://developer.android.com/).
- [Kotlin Documentation](https://kotlinlang.org/docs/home.html).
- [Jetpack Compose Documentation](https://developer.android.com/jetpack/compose) and
  [Compose samples](https://github.com/android/compose-samples).
- [Material Design 3 Specification](https://m3.material.io/).
- [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager).
- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging).
- [Play Console Help](https://support.google.com/googleplay/android-developer).
- [Google Play Policy Center](https://support.google.com/googleplay/android-developer/topic/9858052).

## Cross-platform

- [React Native Documentation](https://reactnative.dev/docs/getting-started).
- [React Native New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page) —
  TurboModules, Fabric, Codegen.
- [Expo Documentation](https://docs.expo.dev/).
- [EAS Build Documentation](https://docs.expo.dev/build/introduction/).
- [EAS Update Documentation](https://docs.expo.dev/eas-update/introduction/).
- [Flutter Documentation](https://docs.flutter.dev/).
- [Dart Language Tour](https://dart.dev/language).

## Plugin ecosystem (this skill ships inside)

- [Anthropic Claude Code Documentation](https://code.claude.com/docs).
- [Anthropic Skills Repository](https://github.com/anthropics/skills).
- [Anthropic Claude Plugins Official](https://github.com/anthropics/claude-plugins-official).
- [OpenAI Codex Documentation](https://developers.openai.com/codex).
- [Agent Skills Specification](https://agentskills.io/specification).
- [Model Context Protocol Specification](https://modelcontextprotocol.io).

## Source hierarchy

1. WWDC session videos for the active iOS / macOS / visionOS / watchOS / tvOS year.
2. Official Apple documentation for the framework you're using.
3. Apple sample code repositories (when present and dated within the active OS year).
4. Swift Evolution proposals for accepted-and-shipped language features.
5. Android Codelabs and the Compose samples repository for Android.
6. React Native, Expo, and Flutter official docs for cross-platform.
7. Community examples — labeled non-authoritative; cite alongside an official source or skip.

If official docs conflict with anything in this skill, follow the official docs and update this
file with the change. Open a PR with a one-line note in the changelog.
