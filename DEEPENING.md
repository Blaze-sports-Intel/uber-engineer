# v2.0.0 — discipline deepening tracker

v1.0.0 ships scaffolds: 17 discipline skills with `SKILL.md` (front-loaded triggers + workflow +
verification), 5 references each, and a `validate_skill.py`. Plus 4 cross-cutting agents,
18 commands, 8 hooks, 9 MCP servers, Codex mirror.

v2.0.0 deepens each discipline with the artifacts the verbatim per-discipline build prompts
(`~/Downloads/plugin_skill_prompt_pack/`) call for but v1.0.0 didn't ship: per-skill eval suites,
golden tasks, source maps, per-discipline architect/reviewer subagents, and full per-skill docs.

**Working model:** one PR per discipline, on demand, ordered by which discipline Austin actually
hits first in real BSI work. No big-bang push.

**Version bump:** root `version` → `2.0.0` only after 17/17 disciplines deepened. Until then,
ship under `v1.x.x` patch tags from main for bug fixes, and let `v2.0.0-deepening` accumulate
the discipline upgrades.

**PR template:** `feat(<discipline>): deepen to v2.0.0 spec`.

---

## Per-discipline deepening checklist

For each discipline below, the following deltas land in one PR:

- [ ] `evals/trigger-evals.json` — 30+ prompts split 15 should-trigger / 15 should-not.
- [ ] `evals/golden-tasks.json` — 10+ realistic tasks with rubrics.
- [ ] `evals/rubric.json` — pass/fail rubric keyed off the existing `references/quality-rubric.md`.
- [ ] `agents/<discipline>-architect.md` — explores repo, gathers context, proposes architecture, no edits.
- [ ] `agents/<discipline>-reviewer.md` — reviews against the skill's `quality-rubric.md` and surfaces gaps.
- [ ] `docs/source-map.md` — every official source crawled, dated, official-vs-community labeled.
- [ ] `scripts/run_trigger_evals.py` — JSON shape validation + short report (no model calls without env keys).
- [ ] `scripts/generate_report.py` — structured report on skill coverage and rubric scoring.
- [ ] `assets/checklist-template.md` — discipline-specific intake checklist.
- [ ] CHANGELOG entry under `[2.0.0-deepening]` for that discipline.

Acceptance: `python3 scripts/validate_all.py` passes after the changes; the new evals JSON parses;
the new architect + reviewer subagents are referenced from the discipline's command (`commands/<x>.md`).

---

## Priority order (default — adjust as real use surfaces different needs)

| # | Discipline | Status | PR | Notes |
|---|-----------|--------|----|-------|
| 1 | `full-stack-development` | pending | — | Highest BSI use frequency: every cross-cut feature lands here. |
| 2 | `frontend-development` | pending | — | Heritage Design System, Next.js 16 static export, BSI surfaces. |
| 3 | `devops-and-infrastructure` | pending | — | Cloudflare Workers/Pages/D1/KV/R2 deploys, every BSI ship. |
| 4 | `mobile-development` | pending | — | iOS Craft skill already loaded; this is the cross-platform layer. |
| 5 | `api-development` | pending | — | Highlightly + ESPN integrations, satellite workers. |
| 6 | `security-development` | pending | — | Stripe-keyed auth, Firebase Auth, X-BSI-Key handling. |
| 7 | `database-development` | pending | — | D1 migrations, Supabase, sabermetric stores. |
| 8 | `cloud-development` | pending | — | Wrangler, multi-env config, observability. |
| 9 | `ai-ml-development` | pending | — | The Read (formerly Savant), wOBA/wRC+/FIP recompute crons. |
| 10 | `web-development` | pending | — | End-to-end visitor surfaces, BSI public site. |
| 11 | `test-and-quality-assurance` | pending | — | Playwright, Vitest, gate scripts. |
| 12 | `game-development` | pending | — | BSI Arcade, Three.js + Phaser games. |
| 13 | `blockchain-development` | pending | — | Lower BSI priority but covered by spec. |
| 14 | `ar-vr-development` | pending | — | Lower BSI priority. |
| 15 | `embedded-systems-development` | pending | — | Lower BSI priority. |
| 16 | `data-science-development` | pending | — | Lower BSI priority (Python notebooks for one-off analysis). |

---

## Reference materials for each deepening PR

Per discipline, the verbatim build prompt lives at:

- Claude Code spec: `~/Downloads/plugin_skill_prompt_pack/prompts/claude-code/<NN>-<slug>.md`
- Codex spec: `~/Downloads/plugin_skill_prompt_pack/prompts/codex/<NN>-<slug>.md`

Both must be consulted when deepening — Claude Code for Anthropic-side specifics, Codex for the
mirror. Cross-platform strategy reference:
`~/Downloads/Cross Platform Plugin and Skill Strategy for Claude Code and Codex.pdf`.

Existing `SKILL.md` body and references stay — deepening adds, doesn't replace.

---

## Memory carryover from v1.0.0 ship

- Phase 0 + Phase 0B sync check is mandatory before any plugin install or marketplace publish.
  See `docs/SYNC-CHECK.md` for the v1.0.0 pre-flight; rerun the same checks before the
  v2.0.0 ship.
- `codex-cli` 0.120+ has no `plugin install` subcommand — Codex integration is via `AGENTS.md`
  + symlinked skills + `codex mcp add`. Documented in `docs/INSTALL.md`.
- Cowork install path is the symlink approach but unconfirmed by official Cowork plugin docs;
  Austin verifies on first launch and updates `docs/INSTALL.md` Cowork section with observed
  behavior.

---

## How to claim a discipline

1. Pick the next discipline in priority order (or whichever Austin hits first).
2. Create a branch: `git checkout -b feat/<discipline>-v2-deepening`.
3. Run the verbatim build prompt for that discipline from `~/Downloads/plugin_skill_prompt_pack/`.
4. Tick the checklist boxes above as artifacts land.
5. Run `python3 scripts/validate_all.py` and the new `run_trigger_evals.py`.
6. Open a PR titled `feat(<discipline>): deepen to v2.0.0 spec` against `v2.0.0-deepening`.
7. Update this tracker with PR link + status.

When 17/17 are checked, `v2.0.0-deepening` merges to `main` as v2.0.0.
