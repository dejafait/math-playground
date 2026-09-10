# Provider loop implementation — 2026-09-10

Consolidated the README prompts into root PROMPT.md. Added root loop-codex.sh, loop-claude.sh, loop-gemini.sh, and loop-grok.sh, with shared supervision under scripts/loop/ and matching ignored runtime-output folders. Each invocation performs one coherent research step and checkpoints to the existing notebook; the supervisor owns quota waits and retries.

Implemented persistent cooldowns, rotating logs, shared repository locking, process-group interruption, local subscription-auth checks, and completion validation. Provider billing settings and extra-credit balances must still be managed in the account. Runtime scripts do not purchase credits or switch to API authentication.

Validated with offline fake-CLI tests, including launches from another directory, literal prompt handling, quota/reset parsing, cooldown persistence, graph checks, and Ctrl+C child cleanup. No model inference was used for testing. Codex's local ChatGPT-login check passed; Claude reported no active login in the local check, and Gemini/Grok were not installed. The mathematical next action is unchanged.
