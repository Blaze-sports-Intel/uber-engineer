---
description: Blockchain Development — invoke the blockchain-development skill with focused intent.
argument-hint: <action> [target] [flags]
allowed-tools:
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Bash
  - Task
---

# /uber:blockchain

Invoke the **blockchain-development** skill for a Blockchain Development task.

## Usage

```
/uber:blockchain $ARGUMENTS
```

Common patterns:

- `/uber:blockchain contract-review src/Vault.sol`
- `/uber:blockchain fork-test --block=latest`
- `/uber:blockchain wallet-flow approve-spend`

## What this command does

1. Loads the `blockchain-development` skill.
2. Passes `$ARGUMENTS` as the user intent.
3. Runs the skill's intake → inspect → source-check → produce → verify → hand back workflow.
4. If the request crosses disciplines, dispatches the `discipline-router` agent first.
5. Before claiming done, dispatches the `build-validator` agent for verification.

## Trigger words

blockchain, Ethereum, Solidity, Foundry, Hardhat, Rust smart contracts, Solana, Anchor, wallet, ERC-20, ERC-721, NFT, DeFi, EVM, subgraph, indexer, RPC, MEV, wagmi, viem, ethers.js.
