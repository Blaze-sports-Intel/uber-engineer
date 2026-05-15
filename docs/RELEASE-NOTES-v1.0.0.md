# Release notes — uber-engineer v1.0.0

**Date:** 2026-05-15
**Repo:** https://github.com/Blaze-sports-Intel/uber-engineer
**Commit:** `b3f1030` (initial release)
**Tracker PR for v2.0.0:** https://github.com/Blaze-sports-Intel/uber-engineer/pull/1

---

## What shipped

A full cross-platform engineering plugin marketplace covering 17 software development disciplines:

- **Skills (17):** frontend, backend, full-stack, mobile, game, devops-and-infrastructure, api,
  database, embedded-systems, cloud, ai-ml, blockchain, test-and-quality-assurance, security,
  ar-vr, data-science, web. Each with `SKILL.md` (front-loaded triggers, non-trigger boundaries,
  workflow, artifacts, anti-patterns, verification, definition of done) plus 5 references
  (`official-sources`, `workflow-playbook`, `quality-rubric`, `anti-patterns`, `examples`) and
  a `validate_skill.py` script.
- **Agents (4):** `discipline-router`, `build-validator`, `code-reviewer`, `ship-auditor`.
- **Slash commands (18):** `/uber` router + one per discipline.
- **Hooks (8):** `PostToolUse` validators per skill, `PreToolUse` destructive-action guards
  (`rm -rf`, `DROP TABLE`, `git push --force`), `Stop` ship-auditor reminder.
- **MCP servers (9):** Supabase, GitHub, Cloudflare, Stripe, PostHog, Context7, Playwright,
  Chrome DevTools, Firecrawl — wired with `${VAR}` env substitution, fail-closed when keys missing.
- **Codex mirror:** `codex-mirror/uber-engineer/` with `.codex-plugin/plugin.json` + `AGENTS.md`.
- **Marketplace:** `.claude-plugin/marketplace.json` for GitHub-based distribution.
- **CI:** `.github/workflows/validate.yml` runs `validate_all.py` on every PR. First push went
  green in 11 seconds.

---

## Pre-flight (Phase 0 + Phase 0B sync check)

See `docs/SYNC-CHECK.md` for full detail. Headline outcomes:

- **GitHub:** active login `ahump20`, **admin** on `Blaze-sports-Intel`, all three candidate
  repos clean (no duplicates). Publish path unblocked.
- **Cloudflare:** Wrangler 4.72.0 authenticated.
- **Xcode:** 26.5 active.
- **Codex:** `codex-cli` 0.120.0 — **discovered no `plugin install` subcommand exists**; install
  doc rewritten to reflect actual integration path.
- **Cowork:** plugin dir present, no prior symlink.
- **MCP env:** `GITHUB_PERSONAL_ACCESS_TOKEN` and `STRIPE_SECRET_KEY` set; other 7 servers
  fail-closed by design until env keys land.

Carried-forward warnings:
- `WARN_SUPABASE_NOT_SYNCED` — CLI missing, env vars missing, MCP fails closed.
- `WARN_APP_STORE_CONNECT_NOT_SYNCED_FOR_IOS_PUBLISH` — ASC env vars missing; doesn't affect
  v1.0.0 ship.
- `WARN_CODEX_PLUGIN_SUBCOMMAND_DOES_NOT_EXIST` — install doc carries the corrected path.
- `WARN_MCP_ENV_PARTIAL` — 7/9 MCP servers fail closed until env keys exported.

---

## Install confirmations

### Claude Code
- Symlink: `~/.claude/marketplaces/uber-engineer -> ~/uber-engineer`
- Marketplace JSON parses, plugin name `uber-engineer`, owner URL `https://github.com/Blaze-sports-Intel`.
- Verify by running these inside Claude Code:
  ```
  /plugin marketplace add ~/.claude/marketplaces/uber-engineer
  /plugin install uber-engineer@uber-engineer-marketplace
  /uber audit
  ```

### Cowork
- Symlink: `~/Library/Application Support/Cowork/plugins/uber-engineer -> ~/uber-engineer/plugins/uber-engineer`
- Plugin manifest reads through symlink: 17 skills, 4 agents, 18 commands.
- **Action required:** restart Cowork and report observed behavior. The symlink approach is
  documented but not yet confirmed by official Cowork plugin docs. Update `docs/INSTALL.md`
  Cowork section with whatever Cowork actually shows on next launch.

### Codex
- Plugin symlink: `~/.codex/plugins/uber-engineer -> ~/uber-engineer/codex-mirror/uber-engineer`
- 17 skill symlinks under `~/.codex/skills/`
- AGENTS.md merged into `~/.codex/AGENTS.md` (existing /write skill content preserved at
  `~/.codex/AGENTS.md.before-uber-engineer-*` backup).
- MCP wiring not yet executed — run `codex mcp add ...` per `docs/INSTALL.md` Codex section
  when env vars for the relevant servers are exported.

### GitHub marketplace
- Repo: https://github.com/Blaze-sports-Intel/uber-engineer (public, owner `Blaze-sports-Intel`).
- Created: 2026-05-15T12:48:55Z.
- Default branch: `main`.
- First push validate workflow: **success in 11 seconds**.
- CodeQL also auto-triggered on first push.
- Clean test install verified: cloned fresh from `https://github.com/Blaze-sports-Intel/uber-engineer.git`
  into `/tmp/uber-engineer-test/`, ran bundled `validate_all.py`, all 17 skill scaffolds passed.
- Install path for any user, anywhere:
  ```
  /plugin marketplace add Blaze-sports-Intel/uber-engineer
  /plugin install uber-engineer@uber-engineer-marketplace
  ```

---

## What v1.0.0 doesn't ship (deferred to v2.0.0)

The verbatim per-discipline build prompts at `~/Downloads/plugin_skill_prompt_pack/` call for
additional artifacts per skill that v1.0.0 doesn't include:

- `evals/trigger-evals.json` (30+ should-trigger / should-not-trigger prompts)
- `evals/golden-tasks.json` (10+ realistic tasks with rubrics)
- `evals/rubric.json`
- `agents/<discipline>-architect.md` and `agents/<discipline>-reviewer.md` per skill
- `docs/source-map.md` per skill
- `scripts/run_trigger_evals.py` and `scripts/generate_report.py` per skill
- `assets/checklist-template.md` per skill

These ship as PRs against `v2.0.0-deepening` branch. Tracker: PR #1.

---

## Visitor-visible outcome

This is dev tooling, so there's no public-facing surface. The actual visitor-visible outcome:

- `/uber audit` produces a routing decision for any engineering request across 17 disciplines.
- `/plugin marketplace add Blaze-sports-Intel/uber-engineer` resolves from any machine with
  authenticated `gh`.
- The 5 hooks fire correctly: skill validators on file write, destructive-action guards on
  bash, ship-auditor reminder on stop.
- The 9 MCP servers either operate (when env vars set) or fail closed with a clear message.

---

## Files changed since unzip

5 manifest/doc rewrites for canonical destination + new docs:

| File | Change |
|---|---|
| `plugins/uber-engineer/.claude-plugin/plugin.json` | `homepage` + `repository` → BSI URL; keyword `ahump20` → `blaze-sports-intel` |
| `.claude-plugin/marketplace.json` | `owner.url` → BSI |
| `README.md` | Clone URLs + Codex install block + maintainer line |
| `docs/INSTALL.md` | Clone URLs + Codex section rewritten with actual `codex mcp add` flow |
| `install.sh` | `REPO_URL` + Codex section |
| `docs/SYNC-CHECK.md` | **NEW** — full Phase 0 + 0B pre-flight report |
| `docs/RELEASE-NOTES-v1.0.0.md` | **NEW** — this file |
| `DEEPENING.md` | **NEW** — v2.0.0 tracker on `v2.0.0-deepening` branch |
| `.gitignore` | **NEW** — blocks .DS_Store, .env, secrets |

Plus `~/Downloads/UBER-ENGINEER-INSTALL.md` updated to reflect canonical
`Blaze-sports-Intel/uber-engineer` destination.

---

## Stop conditions that did NOT fire

- No `BLOCK_` tokens during sync check.
- `validate_all.py` passed pre-publish (17/17) and post-publish on fresh clone (17/17).
- `gh repo create` succeeded under `ahump20` admin permission.
- Cowork symlink created cleanly, manifest reachable.
- All 5 manifest JSON parses verified.

---

## Next moves

1. **Austin verifies Cowork on next launch** and reports what shows up; update
   `docs/INSTALL.md` Cowork section with observed behavior.
2. **Export MCP env keys** as needs surface (Cloudflare, Supabase, PostHog, Firecrawl) — each
   server fails closed until its keys land, so partial enablement is fine.
3. **Pick first discipline to deepen** — default priority is `full-stack-development` per
   `DEEPENING.md`. Open a branch off `v2.0.0-deepening`, run the verbatim prompt for that
   discipline, file a PR.
