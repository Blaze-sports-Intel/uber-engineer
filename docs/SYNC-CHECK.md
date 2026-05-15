# SYNC-CHECK — uber-engineer v1.0.0 install pre-flight

**Timestamp:** 2026-05-15
**Operator:** AustinHumphrey (HOME=/Users/AustinHumphrey)
**Canonical org owner:** Blaze-sports-Intel
**Canonical repo:** Blaze-sports-Intel/uber-engineer

---

## B1. GitHub sync — PASS

| Check | Result |
|---|---|
| Active login | `ahump20` ✓ |
| Blaze-sports-Intel visible | yes ✓ |
| Membership role | **admin** (active) ✓ |
| Token scopes | `admin:public_key`, `gist`, `read:org`, `repo`, `workflow` ✓ |
| Blaze-sports-Intel/uber-engineer | **does not exist** (clean slate) |
| Blaze-sports-Intel/uber-engineer-plugin | does not exist |
| ahump20/uber-engineer | does not exist |

**Decision:** Publish to `Blaze-sports-Intel/uber-engineer`. No duplicate-repo conflict. No transfer
needed. Phase 5 publish is unblocked.

## B2. Cloudflare sync — PASS

- Wrangler: `/Users/AustinHumphrey/.npm-global/bin/wrangler` v4.72.0 (4.92.0 available; non-blocking)
- Authenticated as `humphrey.austin20@gmail.com` via OAuth
- Account: `Humphrey.austin20@gmail.com's Account` (`a12cb329d84130460eed99b816e4d0d3`)
- Token permissions: account/user/workers/workers_kv/workers_routes/workers_scripts/workers_tail/d1

Phase only verifies — no Cloudflare resources created.

## B3. Supabase sync — WARN_SUPABASE_NOT_SYNCED

- Supabase CLI: **MISSING** (no `/opt/homebrew/bin/supabase`, no `/usr/local/bin/supabase`)
- `SUPABASE_ACCESS_TOKEN` = missing
- `SUPABASE_PROJECT_REF` = missing

**Impact:** Supabase MCP server in `.mcp.json` will fail-closed until env vars land. Plugin install
itself proceeds. Document in `docs/INSTALL.md` that Supabase MCP requires both env vars to operate.

## B4. Xcode sync — PASS

- Xcode active developer dir: `/Applications/Xcode.app/Contents/Developer`
- Xcode 26.5, build 17F42

## B5. App Store Connect — WARN_APP_STORE_CONNECT_NOT_SYNCED_FOR_IOS_PUBLISH

All 5 ASC env vars missing: `APP_STORE_CONNECT_API_KEY_ID`, `APP_STORE_CONNECT_ISSUER_ID`,
`APP_STORE_CONNECT_API_KEY_PATH`, `APPLE_ID`, `APP_SPECIFIC_PASSWORD`.

**Impact:** Does NOT block plugin install or marketplace publish. Blocks any iOS App Store
publishing workflow from inside the plugin (which the v1.0.0 ship does not perform).

## B6. Claude Code — PASS

- `/Users/AustinHumphrey/.local/bin/claude` v2.1.142
- Marketplace root exists at `/Users/AustinHumphrey/.claude/marketplaces/`

## B7. Codex — REVISED INTEGRATION PATH

- `/opt/homebrew/bin/codex` codex-cli 0.120.0
- Available subcommands: `exec`, `review`, `login`, `logout`, `mcp`, `mcp-server`, `app-server`,
  `app`, `completion`, `sandbox`, `debug`, `apply`, `resume`, `fork`, `cloud`, `exec-server`,
  `features`, `help`

**Critical observation:** **`codex` has NO `plugin` subcommand.**

The install doc at `~/Downloads/UBER-ENGINEER-INSTALL.md` line 41 (`codex plugin install .`) is
incorrect — that command does not exist in codex-cli 0.120.0. Codex integration is via:
1. `~/.codex/config.toml` for global config.
2. `AGENTS.md` at the project root or `~/.codex/AGENTS.md` globally.
3. `codex mcp add` to wire MCP servers Codex can call.
4. Skills under `~/.codex/skills/` or per-project `.codex/skills/`.

**Phase 4 install path adjustment (locked):**
- Symlink `~/uber-engineer/codex-mirror/uber-engineer` → `~/.codex/plugins/uber-engineer` (best
  guess for any future Codex plugin support; harmless if Codex ignores it).
- Copy or symlink `~/uber-engineer/codex-mirror/uber-engineer/AGENTS.md` →
  `~/.codex/AGENTS.md` (or merge if one already exists).
- Symlink the skills dir to `~/.codex/skills/uber-engineer/` so Codex skill discovery picks them up.
- Run `codex mcp add` for each of the 9 MCP servers using the `.mcp.json` definitions, gated on
  required env vars being set.

This will be documented as the actual Codex install path in `docs/INSTALL.md` Codex section.

## B8. Cowork — PASS

- `/Users/AustinHumphrey/Library/Application Support/Cowork/plugins/` exists, empty
- No prior `uber-engineer` symlink

## B9. MCP env presence (set/missing only — no secret values printed)

| Variable | Status |
|---|---|
| `SUPABASE_ACCESS_TOKEN` | missing |
| `SUPABASE_PROJECT_REF` | missing |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | **set** |
| `CLOUDFLARE_API_TOKEN` | missing |
| `CLOUDFLARE_ACCOUNT_ID` | missing |
| `STRIPE_SECRET_KEY` | **set** |
| `POSTHOG_API_KEY` | missing |
| `POSTHOG_HOST` | missing |
| `FIRECRAWL_API_KEY` | missing |

**Impact:** GitHub MCP and Stripe MCP can operate immediately. Other 7 MCP servers fail-closed
until env vars land. This is the documented design (`/plugin-dev:mcp-integration` requires
fail-closed env handling).

Note on Cloudflare: `wrangler` is OAuth-authenticated and works, but the MCP server in `.mcp.json`
expects `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`. To use the Cloudflare MCP, generate an
API token at https://dash.cloudflare.com/profile/api-tokens and export both vars.

---

## Blockers (BLOCK_)

**None.** Plugin install + GitHub publish are unblocked.

## Warnings (WARN_)

- `WARN_SUPABASE_NOT_SYNCED` — Supabase CLI missing + env vars missing; MCP fails closed.
- `WARN_APP_STORE_CONNECT_NOT_SYNCED_FOR_IOS_PUBLISH` — ASC env vars missing; iOS publish blocked
  (not relevant to v1.0.0 ship).
- `WARN_CODEX_PLUGIN_SUBCOMMAND_DOES_NOT_EXIST` — install doc needs Codex section rewrite.
- `WARN_MCP_ENV_PARTIAL` — only `GITHUB_PERSONAL_ACCESS_TOKEN` and `STRIPE_SECRET_KEY` are set;
  other 7 MCP servers will fail closed.

## CLI inventory

| Tool | Path | Status |
|---|---|---|
| claude | `/Users/AustinHumphrey/.local/bin/claude` (v2.1.142) | ✓ |
| codex | `/opt/homebrew/bin/codex` (v0.120.0) | ✓ (no plugin subcommand) |
| gh | `/opt/homebrew/bin/gh` | ✓ |
| git | `/usr/bin/git` | ✓ |
| python3 | `/usr/bin/python3` | ✓ |
| wrangler | `/Users/AustinHumphrey/.npm-global/bin/wrangler` (v4.72.0) | ✓ |
| supabase | — | MISSING (WARN) |
| xcodebuild | `/usr/bin/xcodebuild` (Xcode 26.5) | ✓ |
| xcrun | `/usr/bin/xcrun` | ✓ |

## Final canonical decisions

- **GitHub repo:** `Blaze-sports-Intel/uber-engineer` (clean slate, ahump20 has admin)
- **Marketplace name:** `uber-engineer-marketplace`
- **Plugin slug:** `uber-engineer`
- **Codex install path:** symlink + AGENTS.md + `codex mcp add` (NOT `codex plugin install`)
- **Cowork install path:** symlink as proposed (Austin verifies post-restart)

## Exact next allowed phase

**Phase 1 — Stage and rewrite manifests.** All gating conditions met. No BLOCK_ tokens. WARN_
tokens documented and carry forward into `docs/INSTALL.md`.
