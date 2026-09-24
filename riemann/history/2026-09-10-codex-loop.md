# Codex loop implementation — 2026-09-10

Consolidated the README prompts into root PROMPT.md. Added root loop-codex.sh, with supervision under scripts/loop/ and an ignored runtime-output folder. Each invocation performs one coherent research step and checkpoints to the existing notebook; the supervisor owns quota waits and retries.

Implemented persistent cooldowns, rotating logs, shared repository locking, process-group interruption, local subscription-auth checks, and completion validation. Account billing settings and extra-credit balances must still be managed in the account. Runtime scripts do not purchase credits or switch to API authentication.

Validated with offline fake-CLI tests, including launches from another directory, literal prompt handling, quota/reset parsing, cooldown persistence, graph checks, and Ctrl+C child cleanup. No model inference was used for testing. Codex's local ChatGPT-login check passed. The mathematical next action is unchanged.
