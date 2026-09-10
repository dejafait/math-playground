# Riemann hypothesis research notebook

An informal, checkable research notebook; RH remains unproved. [GOAL.md](GOAL.md) defines the rules, [PROOF.md](PROOF.md) summarizes the argument, [DAG.md](DAG.md) links the lemmas, and [PROGRESS.md](PROGRESS.md) records where to resume. Every provider reads the same [PROMPT.md](PROMPT.md).

Install Python 3.9+ and your chosen CLI, then sign in with your subscription account:

| CLI | Installation guide | Sign in once |
| --- | --- | --- |
| OpenAI Codex | [Codex CLI](https://developers.openai.com/codex/cli) | `codex login` (ChatGPT) |
| Anthropic Claude Code | [Claude Code](https://code.claude.com/docs/en/setup) | `claude auth login` (Claude subscription) |
| Google Gemini CLI | [Gemini CLI](https://geminicli.com/docs/get-started/installation/) | `gemini`, then choose **Sign in with Google** |
| xAI Grok Build | [Grok Build](https://docs.x.ai/build/overview) | `grok login` (subscribed account) |

Keep paid extra usage and automatic credit top-ups disabled in your account. Do not configure API keys or custom paid providers. The scripts check local authentication settings; they cannot inspect or disable account-side billing options. Existing extra-credit balances may be consumed by the service after included usage runs out.

Start any one of these commands; the loop continues until you stop it or the notebook reaches `STATUS: PROVED`:

```bash
bash loop-codex.sh
bash loop-claude.sh
bash loop-gemini.sh
bash loop-grok.sh
```

Each command is an alternative. Ctrl+C stops the active process and loop. Logs and persistent retry state live in the matching `scripts/loop-<vendor>/` folder and are ignored by Git; research decisions remain in `history/`. A shared lock prevents simultaneous notebook edits, while a provider waiting for quota releases the notebook for another provider.

Quotas trigger a wait until an unambiguous reported reset time plus a buffer, or increasing retries capped at hourly when no reset time is available. Restarting preserves the wait. Authentication/configuration failures stop with an explanation. Repeated unclassified failures or runs without recorded progress also stop for inspection. The computer and terminal session must remain running for automatic retries.

Use `bash loop-codex.sh --check` for a local setup check, `--dry-run` to inspect the command, `--once` for one step, or `--verbose` to stream CLI events; the same options work for all four launchers. [Runner details and tests](scripts/loop/README.md).
