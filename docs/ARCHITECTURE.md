# Architecture

## Single mega-plugin, three platforms

The uber-engineer plugin is structured as **one** Claude Code plugin that contains 17 discipline
skills, rather than 17 separate plugins. Why:

- A single install gives the user every discipline.
- The discipline-router agent can hand off between disciplines without re-loading plugins.
- Cross-cutting work (full-stack, devops affecting backend, etc.) doesn't fragment.

## Cowork compatibility

Cowork uses the same Claude Code plugin format. The `plugins/uber-engineer/` directory works as-is.

## Codex mirror

`codex-mirror/uber-engineer/` mirrors the plugin in Codex's `.codex-plugin/` format. Skills are
identical (same SKILL.md, same references). Codex uses `AGENTS.md` instead of Claude Code's hooks
for durable project guidance — see `codex-mirror/uber-engineer/AGENTS.md`.

## Component map

| Component | Path | Purpose |
|-----------|------|---------|
| Plugin manifest | `.claude-plugin/plugin.json` | Plugin metadata, component pointers |
| Marketplace | `.claude-plugin/marketplace.json` (repo root) | GitHub marketplace registration |
| Skills | `skills/<discipline>/SKILL.md` + references + scripts | One per discipline (17 total) |
| Agents | `agents/*.md` | discipline-router, build-validator, code-reviewer, ship-auditor |
| Commands | `commands/*.md` | `/uber` (router) + `/uber:<short>` per discipline |
| Hooks | `hooks/hooks.json` | PostToolUse validation, PreToolUse safety, Stop reminders |
| MCP | `.mcp.json` | Supabase, GitHub, Cloudflare, Stripe, PostHog, Context7, Playwright, Chrome DevTools, Firecrawl |
| Scripts | `scripts/*.py` | Hook implementations |

## Skill anatomy

Each skill follows the Agent Skills specification:

```yaml
---
name: <discipline-slug>
description: <front-loaded triggers + non-triggers>
---
```

Body sections (required):

1. When to use this skill
2. When NOT to use this skill
3. Workflow (intake → inspect → source-check → produce → verify → hand back)
4. Artifacts this skill produces
5. Anti-patterns this skill pushes back against
6. Verification required before claiming done
7. Suggested commands
8. References (load on demand)
9. Definition of done

## Routing model

```
user request
   │
   ▼
discipline-router agent
   │
   ├──► PRIMARY discipline ──► skill ──► artifacts
   │
   ├──► SECONDARY disciplines ──► skills ──► artifacts
   │
   ▼
build-validator agent (proves loading/error/empty/populated)
   │
   ▼
ship-auditor agent (proves rendered visible output)
   │
   ▼
hand back to user
```

## Hook lifecycle

- `PostToolUse(Write|Edit on skills/**)` → run that skill's `validate_skill.py`.
- `PostToolUse(Write|Edit any)` → reminder of four-state rule.
- `PreToolUse(Bash with rm -rf|DROP TABLE|git push -f)` → block, require explicit confirm.
- `Stop` → ship-auditor reminder.

## Source discipline

Hard-coded into every skill: official platform docs > Agent Skills spec > official repos > official
discipline docs > community examples (labeled non-authoritative).
