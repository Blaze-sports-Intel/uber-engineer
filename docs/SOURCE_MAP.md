# Source Map

Every claim in this plugin is grounded in official documentation. Community blogs and Stack Overflow
answers are non-authoritative.

## Platform docs

| Source | URL | Used for |
|--------|-----|----------|
| Anthropic Claude Code plugins | https://code.claude.com/docs/en/plugins | Plugin structure, manifest, components |
| Anthropic Claude Code skills | https://code.claude.com/docs/en/skills | SKILL.md format, triggering, references |
| Anthropic Claude Code hooks | https://docs.anthropic.com/en/docs/claude-code/hooks-guide | Hook events, matchers, safety |
| Anthropic Claude Code subagents | https://docs.anthropic.com/en/docs/claude-code/sub-agents | Agent definition, tools, model |
| Anthropic skills repo | https://github.com/anthropics/skills | Reference skill examples |
| Anthropic plugins official | https://github.com/anthropics/claude-plugins-official | Plugin examples |
| Agent Skills spec | https://agentskills.io/specification | Portable SKILL.md standard |
| MCP specification | https://modelcontextprotocol.io | MCP server config |
| OpenAI Codex plugins | https://developers.openai.com/codex/plugins | Codex plugin structure |
| OpenAI Codex skills | https://developers.openai.com/codex/skills | Codex skill format |
| OpenAI Codex AGENTS.md | https://developers.openai.com/codex/guides/agents-md | Durable project guidance |

## Per-discipline docs

See each skill's `references/official-sources.md` for the authoritative docs used in that skill.

## Source hierarchy (enforced in every skill)

1. Anthropic for Claude Code, OpenAI for Codex.
2. Agent Skills specification.
3. Official repos by Anthropic / OpenAI.
4. Official framework / language / tool docs.
5. Community examples — labeled non-authoritative.

## Update policy

When official docs change in ways that affect this plugin:

1. Update the relevant skill's `references/official-sources.md`.
2. Update the skill body if the change affects workflow or verification.
3. Add a CHANGELOG entry.
4. Tag a new version.
