# Blockchain Development — Examples

Concrete invocations and a before/after pattern.

## Slash command invocations

```
/blockchain contract-review src/Vault.sol
```

```
/blockchain fork-test --block=latest
```

```
/blockchain wallet-flow approve-spend
```

The `/uber` router will dispatch to `/blockchain` after reading the request. You can
also call the discipline command directly when you already know the discipline.

## Before / after pattern

**Before:** A vague request that hides the real work.

> "Add a Vault contract with deposit and withdraw."

**After:** The skill rewrites the request as a measurable, discipline-correct task.

> "Write the contract with CEI ordering, ReentrancyGuard, AccessControl roles for pause/upgrade, EIP-712 typed-data signatures for off-chain auth, then a Foundry suite with 95% coverage including fork tests against a pinned block, Slither + Mythril clean, simulation preview wired into the wallet UX so users see exactly what they're signing."

## Skill chaining

This skill works well chained with:

- `discipline-router` agent — when the request crosses disciplines.
- `build-validator` agent — before claiming verification.
- `code-reviewer` agent — before merging changes.
- `ship-auditor` agent — before declaring the ship complete.
- `security-development` skill — for adjacent work that's better handled there.
- `frontend-development` skill — for adjacent work that's better handled there.
- `test-and-quality-assurance` skill — for adjacent work that's better handled there.
