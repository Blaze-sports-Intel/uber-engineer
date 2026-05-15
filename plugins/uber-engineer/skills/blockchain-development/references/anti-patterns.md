# Blockchain Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Storing secrets / private keys in repo.

**Fix:** Move keys to a hardware wallet (Ledger/Trezor) for deploys, or a secret manager (AWS KMS, Doppler) for service accounts. Never commit a `.env` with a real key. Rotate any key that has ever been in the repo, even briefly.

### Upgradeable proxies without storage layout discipline.

**Fix:** Use OpenZeppelin's upgrades plugin to enforce storage layout compatibility. Add `__gap` storage slots to base contracts. Run the layout check on every upgrade PR. Document each layout change in the contract spec.

### Wallet prompts that ask users to sign raw hex.

**Fix:** Use EIP-712 typed data so wallets show a human-readable structure. Pair with a simulation step (Tenderly, Defender, or in-app wallet preview) that shows the resulting state change before the user signs.

### Tests passing on mocks while behavior differs on a fork.

**Fix:** Add fork tests against a pinned mainnet block for every external integration. Use Foundry's `vm.createSelectFork`. Block deploy if fork tests are absent or stale (older than 30 days).

### Treating audit as optional for non-trivial value transfer.

**Fix:** Set a value threshold (e.g., $1M TVL or any new fund mechanism). Above the threshold, an external audit is mandatory before mainnet. Below, an internal review by a second engineer is mandatory. Document the policy in the repo.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
