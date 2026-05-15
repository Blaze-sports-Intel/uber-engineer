# Changelog

All notable changes to uber-engineer are documented here.

## [1.0.2] - 2026-05-15

### Changed

- **mobile-development skill rebuilt with Apple-platform depth.** Previous version was
  stack-agnostic (iOS or Android, pick one, ship to the store). 1.0.2 reflects the actual
  shape of modern mobile work: Apple platforms (iOS / iPadOS / macOS / visionOS / watchOS / tvOS)
  carry the heaviest weight, with Android (Kotlin + Compose) and cross-platform (RN+Expo,
  Flutter) as explicitly bounded sub-domains.

### Added (mobile-development)

- **Apple Build Evidence Loop** as a first-class section in `SKILL.md`: local `xcodebuild build`
  before tagging, distinguishing CI-only Xcode Cloud workflows from Distribute + TestFlight
  workflows, Archive ≠ Upload ≠ Install, build-number auto-increment behavior, release-branch
  merge-back-after-archive discipline.
- Triggers expanded to include iOS 26 / Liquid Glass, Swift 6 strict concurrency / MainActor /
  Sendable / actor isolation, App Intents, WidgetKit, StoreKit 2, ASWebAuthenticationSession,
  Universal Links / Associated Domains, OSLog, MetricKit, Mac Catalyst, Sign in with Apple,
  BGAppRefreshTask / BGProcessingTask.
- Anti-patterns rewritten with real iOS gotchas plus concrete fixes:
  - "Action Required" in Xcode Cloud ≠ manual approval gate (means compile errors).
  - Tagging an RC without a clean local `xcodebuild build` first.
  - Release branch archived to App Store Connect but never merged back to `main` same day.
  - Claiming "live on TestFlight" before the install list shows the build on a tester device.
  - Liquid Glass overlays without legibility verification at body text size.
  - ASWebAuthenticationSession callback URL not registered in Associated Domains.
  - `@MainActor` missing on UI-touching functions; data race surfaces in production.
- Quality rubric split into three platform-specific shipping ladders (Apple, Android,
  cross-platform) plus cross-cutting checks.
- Examples include rejection-recovery reviewer-notes preamble pattern (cause-of-fix lead) and
  the Xcode Cloud "Action Required" misread.
- Suggested commands tilted to real Apple-platform craft: `/mobile ship-ios`,
  `/mobile asc-submit`, `/mobile concurrency-audit`, `/mobile mac-shell`.
- Official sources reorganized with Apple platforms first (WWDC, Apple Developer Documentation,
  Swift Evolution, Xcode release notes, App Store Connect API, MetricKit) followed by Android
  and cross-platform.

## [1.0.1] - 2026-05-15

### Changed

- Reference packs rebuilt from per-discipline data instead of generator-stamped templates. Every
  discipline now has its own real before/after example, real Phase 4 capability→artifact mapping,
  real anti-pattern fixes, and a discipline-correct definition-of-done state set.
- backend ↔ api boundary sharpened with mutual exclusion clauses.
- frontend ↔ web boundary sharpened with mutual exclusion clauses.
- 17 byte-identical per-skill validators consolidated into a shared
  `scripts/validate_skill.py` plus thin `runpy` wrappers.
- Manifest schema drift fixed: `git-subdir` source on marketplace entry, `author` as object,
  `components` key removed, `hooks.json` rewritten to string-matcher + typed command array
  schema, YAML descriptions quoted to escape colons.

## [1.0.0] - 2026-05-15

### Added

- Initial release with 17 discipline skills:
  frontend, backend, full-stack, mobile, game, devops, api, db, embedded, cloud,
  ai-ml, blockchain, qa, security, xr, data, web.
- 4 specialized agents: discipline-router, build-validator, code-reviewer, ship-auditor.
- 18 slash commands: `/uber` (router) + one per discipline.
- 21 lifecycle hook entries across 3 events: 18 PostToolUse skill validators (one per skill +
  cross-cutting) + 2 PreToolUse destructive-action guards (rm -rf, DROP TABLE / git push --force) +
  1 Stop ship-auditor reminder.
- MCP wiring for 9 platforms: Supabase, GitHub, Cloudflare, Stripe, PostHog, Context7, Playwright,
  Chrome DevTools, Firecrawl.
- Codex mirror with `.codex-plugin/` and `AGENTS.md`.
- Marketplace `marketplace.json` for GitHub-based distribution.
- GitHub Actions validation workflow.

### Source discipline

- Every skill grounded in official platform docs first, official discipline docs second.
- Community sources labeled non-authoritative.
- Source map at `docs/SOURCE_MAP.md`.
