#!/usr/bin/env bash
# uber-engineer one-liner installer for Claude Code
set -euo pipefail

REPO_URL="https://github.com/Blaze-sports-Intel/uber-engineer.git"
MARKETPLACE_DIR="${HOME}/.claude/marketplaces/uber-engineer"

echo "→ Cloning uber-engineer marketplace into ${MARKETPLACE_DIR}..."
if [ -d "${MARKETPLACE_DIR}" ]; then
  cd "${MARKETPLACE_DIR}" && git pull
else
  mkdir -p "$(dirname "${MARKETPLACE_DIR}")"
  git clone "${REPO_URL}" "${MARKETPLACE_DIR}"
fi

cat <<EOF

→ Done. Inside Claude Code, run:

    /plugin marketplace add ${MARKETPLACE_DIR}
    /plugin install uber-engineer@uber-engineer-marketplace

→ Then verify:

    /uber audit

→ For Cowork:

    ln -s "${MARKETPLACE_DIR}/plugins/uber-engineer" \\
      "\$HOME/Library/Application Support/Cowork/plugins/uber-engineer"

→ For Codex (codex-cli has no plugin subcommand — use AGENTS.md + MCP wiring):

    mkdir -p "\$HOME/.codex/skills" "\$HOME/.codex/plugins"
    ln -sfn "${MARKETPLACE_DIR}/codex-mirror/uber-engineer" "\$HOME/.codex/plugins/uber-engineer"
    ln -sfn "${MARKETPLACE_DIR}/codex-mirror/uber-engineer/skills/"* "\$HOME/.codex/skills/"
    cp "${MARKETPLACE_DIR}/codex-mirror/uber-engineer/AGENTS.md" "\$HOME/.codex/AGENTS.md"

EOF
