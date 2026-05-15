# Changelog

All notable changes to uber-engineer are documented here.

## [1.0.0] - 2026-05-15

### Added

- Initial release with 17 discipline skills:
  frontend, backend, full-stack, mobile, game, devops, api, db, embedded, cloud,
  ai-ml, blockchain, qa, security, xr, data, web.
- 4 specialized agents: discipline-router, build-validator, code-reviewer, ship-auditor.
- 18 slash commands: `/uber` (router) + one per discipline.
- 8 lifecycle hooks: skill validation (PostToolUse), destructive action guards (PreToolUse),
  ship-auditor reminder (Stop).
- MCP wiring for Supabase, GitHub, Cloudflare, Stripe, PostHog, Context7, Playwright,
  Chrome DevTools, Firecrawl.
- Codex mirror with `.codex-plugin/` and `AGENTS.md`.
- Marketplace `marketplace.json` for GitHub-based distribution.
- GitHub Actions validation workflow.

### Source discipline

- Every skill grounded in official platform docs first, official discipline docs second.
- Community sources labeled non-authoritative.
- Source map at `docs/SOURCE_MAP.md`.
