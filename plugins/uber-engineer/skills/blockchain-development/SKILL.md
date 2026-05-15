---
name: blockchain-development
description: "Smart contracts, wallet UX, indexers, security review, and on-chain integration. Use when the user mentions: blockchain, Ethereum, Solidity, Foundry, Hardhat, Rust smart contracts, Solana, Anchor, wallet, ERC-20, ERC-721, NFT, DeFi, EVM, subgraph, indexer, RPC, MEV, wagmi, viem, ethers.js. Pair with the discipline-router agent for cross-cutting work. Do NOT trigger for: general web3 frontend without contract code (use frontend-development); trading bots without on-chain integration."
---

# Blockchain Development

Smart contracts, wallet UX, indexers, security review, and on-chain integration.

This skill is part of the **uber-engineer** plugin's discipline coverage. Pair with the
`discipline-router` agent when a request crosses disciplines, and the `build-validator` agent
before claiming any work is done.

## When to use this skill

Trigger words: blockchain, Ethereum, Solidity, Foundry, Hardhat, Rust smart contracts, Solana, Anchor, wallet, ERC-20, ERC-721, NFT, DeFi, EVM, subgraph, indexer, RPC, MEV, wagmi, viem, ethers.js.

Use when the user wants any of:

- Author Solidity or Anchor contracts with explicit access control.
- Write deterministic test suites against forked mainnet state.
- Run static analysis (Slither, Mythril) before deploy.
- Design wallet flows that don't ask users to sign opaque blobs.
- Build event indexers for on-chain state into off-chain queries.
- Apply reentrancy, integer overflow, and signature-replay guards by default.

## When NOT to use this skill

- general web3 frontend without contract code (use frontend-development)
- trading bots without on-chain integration

## Workflow

1. **Intake.** Read the user intent. Identify which capability above applies. If the request crosses
   into another discipline (e.g. UI + DB), call the `discipline-router` agent before splitting work.
2. **Inspect.** Look at the actual repo state with Read/Grep/Glob before proposing changes. Do not
   assume what code exists from project name alone.
3. **Source-check.** For non-obvious technical claims, ground the answer in the official sources
   listed in `references/official-sources.md`. Use the Context7 MCP for live doc lookups instead of
   relying on training-data memory for fast-moving APIs.
4. **Produce.** Generate the appropriate artifact from the list below.
5. **Verify.** Run every verification layer below before claiming done. Build success is not done.
   200 responses are not done. A real user seeing correct output is done.
6. **Hand back.** Report what shipped, what the visitor sees, what changed. No file paths, function
   names, or engineering jargon unprompted.

## Artifacts this skill produces

- Contract spec: state, events, access roles, upgrade path.
- Foundry/Hardhat test suite with coverage report.
- Static analysis report with each finding triaged.
- Wallet UX flow: human-readable confirmations + simulation preview.
- Indexer schema mapped to contract events.
- Mainnet deploy checklist with multisig sign-off.

## Anti-patterns this skill pushes back against

- Storing secrets / private keys in repo.
- Upgradeable proxies without storage layout discipline.
- Wallet prompts that ask users to sign raw hex.
- Tests passing on mocks while behavior differs on a fork.
- Treating audit as optional for non-trivial value transfer.

## Verification required before claiming done

- Test coverage on contracts ≥ 95% lines + branches.
- Static analysis reports zero unresolved highs.
- Fork test matches mainnet state assumptions.
- Wallet flow simulation shown to a non-engineer who understands what they're signing.
- Multisig sign-off recorded before mainnet deploy.

## Suggested commands

- `/blockchain contract-review src/Vault.sol`
- `/blockchain fork-test --block=latest`
- `/blockchain wallet-flow approve-spend`

## References (load on demand)

- `references/official-sources.md` — authoritative documentation URLs.
- `references/workflow-playbook.md` — detailed step-by-step playbook.
- `references/anti-patterns.md` — anti-pattern catalog with fixes.
- `references/quality-rubric.md` — pass/fail rubric for review.
- `references/examples.md` — concrete examples, before/after diffs.

## Scripts

- `scripts/validate_skill.py` — sanity-checks SKILL.md frontmatter and references.

## Definition of done

A real user, operator, or downstream system experiences the correct outcome of this work. Build
success and deploy success do not equal done. The discipline-specific states below must all hold:

- Test coverage on contracts ≥ 95% lines + branches.
- Static analysis reports zero unresolved highs.
- Fork test matches mainnet state assumptions.
- Wallet flow simulation shown to a non-engineer who understands what they're signing.
- Multisig sign-off recorded before mainnet deploy.

Verification actually happened — no claim of "verified" without evidence.
