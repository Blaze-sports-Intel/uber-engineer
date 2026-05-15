# uber-engineer

> Production-grade engineering plugin for **Claude Code**, **Cowork**, and **Codex**. 17 discipline
> skills, 4 specialized agents, MCP wiring for the modern web stack, and a deterministic
> "definition of done" workflow.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](CHANGELOG.md)
[![Disciplines](https://img.shields.io/badge/disciplines-17-orange.svg)](#disciplines)
[![Skills](https://img.shields.io/badge/skills-17-purple.svg)](plugins/uber-engineer/skills/)
[![Agents](https://img.shields.io/badge/agents-4-teal.svg)](plugins/uber-engineer/agents/)

## Why this exists

Most plugins ship one capability. Real engineering work crosses disciplines: a feature touches UI,
API, database, tests, and deploy. This plugin gives an agent the right vocabulary, official-doc
references, anti-pattern catalog, and verification rubric for every layer in one installable unit.

The doctrine: **build success ≠ done. 200 OK ≠ done. A real user seeing correct output = done.**

## Install

### Claude Code

```bash
# Clone the marketplace
git clone https://github.com/Blaze-sports-Intel/uber-engineer.git ~/.claude/marketplaces/uber-engineer

# Inside Claude Code
/plugin marketplace add ~/.claude/marketplaces/uber-engineer
/plugin install uber-engineer@uber-engineer-marketplace
```

Or one-liner:

```bash
curl -fsSL https://raw.githubusercontent.com/Blaze-sports-Intel/uber-engineer/main/install.sh | bash
```

### Cowork (desktop)

The same `plugins/uber-engineer/` directory is Cowork-compatible. Drop it into your Cowork plugins
directory or install via the Cowork plugin loader UI.

### Codex (OpenAI CLI)

`codex-cli` 0.120+ has no `plugin install` subcommand. Codex integration uses `AGENTS.md` plus
symlinked skills and the `codex mcp add` flow:

```bash
git clone https://github.com/Blaze-sports-Intel/uber-engineer.git
cd uber-engineer/codex-mirror/uber-engineer
mkdir -p ~/.codex/skills ~/.codex/plugins
ln -sfn "$(pwd)" ~/.codex/plugins/uber-engineer
ln -sfn "$(pwd)/skills/"* ~/.codex/skills/
cp AGENTS.md ~/.codex/AGENTS.md   # or merge with an existing one
```

Wire the MCP servers Codex should call (env vars must be set first):

```bash
codex mcp add github -- npx -y @modelcontextprotocol/server-github
codex mcp add cloudflare -- npx -y @cloudflare/mcp-server-cloudflare
# ...repeat for each MCP server you want Codex to reach
```

## Disciplines

| # | Skill | Command | What it covers |
|---|-------|---------|----------------|
| 01 | `frontend-development` | `/uber:frontend` | UI implementation, design systems, accessibility, responsive layout, and frontend performance. |
| 02 | `backend-development` | `/uber:backend` | Service architecture, API contracts, auth, data persistence, and operational hygiene. |
| 03 | `full-stack-development` | `/uber:fullstack` | End-to-end feature delivery across frontend, backend, API, database, and deploy. |
| 04 | `mobile-development` | `/uber:mobile` | Native iOS, native Android, and cross-platform mobile with build, test, store, and offline constraints. |
| 05 | `game-development` | `/uber:game` | Engine architecture, gameplay systems, performance budgets, and asset pipelines. |
| 06 | `devops-and-infrastructure` | `/uber:devops` | CI/CD, infrastructure as code, observability, rollback, and incident hygiene. |
| 07 | `api-development` | `/uber:api` | API contracts, versioning, backward compatibility, error schemas, and developer experience. |
| 08 | `database-development` | `/uber:db` | Schema design, migration safety, indexing, query review, and read-only-by-default access. |
| 09 | `embedded-systems-development` | `/uber:embedded` | C/C++/Rust on microcontrollers, RTOS, memory limits, hardware abstraction, and cross-compiling. |
| 10 | `cloud-development` | `/uber:cloud` | Serverless, multi-environment config, observability, and release promotion across major clouds. |
| 11 | `ai-ml-development` | `/uber:ai` | Experiment workflows, datasets, evals, model packaging, serving, and rollback for AI/ML systems. |
| 12 | `blockchain-development` | `/uber:blockchain` | Smart contracts, wallet UX, indexers, security review, and on-chain integration. |
| 13 | `test-and-quality-assurance` | `/uber:qa` | Test strategy, contract tests, E2E, visual regression, performance, and accessibility verification. |
| 14 | `security-development` | `/uber:security` | Threat modeling, secure-by-default code, dependency hygiene, secrets management, and incident response. |
| 15 | `ar-vr-development` | `/uber:xr` | Spatial UX, perf budgets, motion comfort, anchors, hand/eye input, and platform-specific deploy. |
| 16 | `data-science-development` | `/uber:data` | Reproducible analysis, dataset hygiene, statistical rigor, dashboarding, and shipping insights. |
| 17 | `web-development` | `/uber:web` | End-to-end web app delivery: routing, rendering modes, SEO, perf, deploy, and observability. |

## Agents

- **`discipline-router`** — routes cross-cutting requests to the right discipline(s).
- **`build-validator`** — proves the four-state rule (loading/error/empty/populated) before "done".
- **`code-reviewer`** — multi-pass review (correctness → security → perf → maintainability).
- **`ship-auditor`** — final gate: rendered output, not 200 OK.

## MCP servers wired

Supabase · GitHub · Cloudflare · Stripe · PostHog · Context7 · Playwright · Chrome DevTools · Firecrawl.

Set the matching env vars in your shell or platform secrets store. See
[`docs/INSTALL.md`](docs/INSTALL.md) for the full list.

## Hooks

- **PostToolUse** — validates skill scaffolds after edit.
- **PreToolUse** — blocks `rm -rf`, `DROP TABLE`, `git push --force` without explicit confirm.
- **Stop** — reminds the agent that 200 OK is not visible-correct output.

## Layout

```
uber-engineer/
├── .claude-plugin/
│   └── marketplace.json        # Marketplace index (Anthropic format)
├── plugins/
│   └── uber-engineer/          # Single mega-plugin
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── skills/             # 17 disciplines
│       ├── agents/             # 4 agents
│       ├── commands/           # 18 slash commands (/uber + 17 specialized)
│       ├── hooks/hooks.json
│       ├── scripts/            # Top-level guards used by hooks
│       └── .mcp.json
├── codex-mirror/               # Codex variant of the same plugin
│   └── uber-engineer/
│       ├── .codex-plugin/plugin.json
│       ├── skills/
│       ├── hooks/hooks.json
│       ├── .mcp.json
│       └── AGENTS.md
├── docs/
│   ├── INSTALL.md
│   ├── ARCHITECTURE.md
│   └── SOURCE_MAP.md
├── .github/workflows/validate.yml
├── install.sh
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Skill structure (per discipline)

Each of the 17 skills follows the same scaffold:

```
skills/<discipline>/
├── SKILL.md                    # Frontmatter + when-to-use + workflow + verification
├── references/
│   ├── official-sources.md     # Authoritative docs only — no community blogs
│   ├── workflow-playbook.md    # Long-form intake → verify → hand-back
│   ├── anti-patterns.md        # Catalog with named fixes
│   ├── quality-rubric.md       # Pass/fail matrix
│   └── examples.md             # Concrete invocations
└── scripts/
    └── validate_skill.py       # CI gate + post-write hook
```

## Source discipline

This plugin grounds every claim in:

1. Anthropic Claude Code docs ([code.claude.com/docs](https://code.claude.com/docs))
2. OpenAI Codex docs ([developers.openai.com/codex](https://developers.openai.com/codex))
3. Agent Skills spec ([agentskills.io/specification](https://agentskills.io/specification))
4. MCP spec ([modelcontextprotocol.io](https://modelcontextprotocol.io))
5. Per-discipline official docs (see each skill's `references/official-sources.md`)

Community blogs and Stack Overflow answers are non-authoritative and labeled as such.

## Contributing

PRs welcome. The validation gate runs on every PR — see
[`.github/workflows/validate.yml`](.github/workflows/validate.yml).

## License

MIT — see [LICENSE](LICENSE).

## Author

**Blaze Sports Intel** · [github.com/Blaze-sports-Intel](https://github.com/Blaze-sports-Intel)
Maintainer: Austin Humphrey · [github.com/ahump20](https://github.com/ahump20) · humphrey.austin20@gmail.com
