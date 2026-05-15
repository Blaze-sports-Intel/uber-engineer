# Installation

Three install paths, depending on platform.

## 1. Claude Code (CLI plugin)

### Quick install

```bash
git clone https://github.com/Blaze-sports-Intel/uber-engineer.git ~/.claude/marketplaces/uber-engineer
```

Inside Claude Code:

```
/plugin marketplace add ~/.claude/marketplaces/uber-engineer
/plugin install uber-engineer@uber-engineer-marketplace
```

### Verify

```
/uber audit
```

You should see the routing agent dispatch a discipline plan.

### Env vars

Add these to your shell profile or `.env` to enable the MCP servers:

```bash
export SUPABASE_ACCESS_TOKEN=...
export SUPABASE_PROJECT_REF=...
export GITHUB_PERSONAL_ACCESS_TOKEN=...
export CLOUDFLARE_API_TOKEN=...
export CLOUDFLARE_ACCOUNT_ID=...
export STRIPE_SECRET_KEY=...
export POSTHOG_API_KEY=...
export POSTHOG_HOST=https://us.posthog.com
export FIRECRAWL_API_KEY=...
```

Each MCP server fails closed if its env var is missing — the plugin keeps working without it.

## 2. Cowork (desktop)

The plugin directory `plugins/uber-engineer/` is Cowork-compatible.

```bash
# Clone, then symlink into Cowork's plugins dir
git clone https://github.com/Blaze-sports-Intel/uber-engineer.git
ln -s "$(pwd)/uber-engineer/plugins/uber-engineer" \
  "$HOME/Library/Application Support/Cowork/plugins/uber-engineer"
```

Restart Cowork. The plugin will load on next session start.

> **Verification status:** the symlink approach is documented but not yet confirmed by official
> Cowork plugin docs. Verify on first launch and report observed behavior so this section can be
> updated with the actual install path.

## 3. Codex (OpenAI CLI)

**Important:** `codex-cli` 0.120+ has no `plugin install` subcommand (verified
2026-05-15 via `codex --help`). Codex integration is via `AGENTS.md` + symlinked skills + the
`codex mcp add` flow:

```bash
git clone https://github.com/Blaze-sports-Intel/uber-engineer.git
cd uber-engineer/codex-mirror/uber-engineer

# Wire Codex skill discovery + AGENTS.md
mkdir -p ~/.codex/skills ~/.codex/plugins
ln -sfn "$(pwd)" ~/.codex/plugins/uber-engineer
ln -sfn "$(pwd)/skills/"* ~/.codex/skills/
cp AGENTS.md ~/.codex/AGENTS.md   # or merge with an existing one
```

Wire the MCP servers Codex should call (each requires its env vars set first):

```bash
codex mcp add github     -- npx -y @modelcontextprotocol/server-github
codex mcp add cloudflare -- npx -y @cloudflare/mcp-server-cloudflare
codex mcp add supabase   -- npx -y @supabase/mcp-server-supabase@latest
codex mcp add stripe     -- npx -y @stripe/mcp
codex mcp add posthog    -- npx -y @posthog/mcp
codex mcp add context7   -- npx -y @upstash/context7-mcp
codex mcp add playwright -- npx -y @playwright/mcp@latest
codex mcp add chrome     -- npx -y chrome-devtools-mcp@latest
codex mcp add firecrawl  -- npx -y firecrawl-mcp
```

The Codex variant uses `.codex-plugin/plugin.json` and `AGENTS.md` for durable repo guidance.
The 17 skills are mirrored verbatim — same SKILL.md content, same references.

## Uninstall

### Claude Code
```
/plugin uninstall uber-engineer
```

### Cowork
```bash
rm "$HOME/Library/Application Support/Cowork/plugins/uber-engineer"
```

### Codex
```bash
rm -f ~/.codex/plugins/uber-engineer
for skill in ~/.codex/skills/*/; do
  if [ "$(readlink "$skill")" = *uber-engineer* ]; then rm -f "$skill"; fi
done
# AGENTS.md was copied (not symlinked) — edit or remove uber-engineer sections manually
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Skills don't trigger | Description didn't match | Re-read the skill's `When to use` section, use a trigger word |
| MCP server fails | Env var missing | Check `.env` or shell profile |
| Hook blocks safe command | False positive on destructive guard | Add `# uber-engineer:allow` comment to the command |
| Validation fails on PR | Skill scaffold drift | Run `python3 scripts/validate_all.py` locally |
