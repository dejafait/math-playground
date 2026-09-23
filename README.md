# Riemann hypothesis research notebook

An informal RH research notebook; RH remains unproved. [GOAL.md](GOAL.md) defines the rules, [PROOF.md](PROOF.md) summarizes the argument, [DAG.md](DAG.md) lists dependencies by lemma ID, and [PROGRESS.md](PROGRESS.md) records where to resume. The Codex loop reads [PROMPT.md](PROMPT.md). Each turn must justify its connection to the main RH gap, check for redundant work, and reassess stalled routes; producing more lemmas is not the objective.

Install Python 3.9+ and the Codex CLI, then sign in with your subscription account:

| CLI | Installation guide | Sign in once |
| --- | --- | --- |
| OpenAI Codex | [Codex CLI](https://developers.openai.com/codex/cli) | `codex login` (ChatGPT) |

Keep paid extra usage and automatic credit top-ups disabled in your account. Do not configure API keys or custom paid providers. The scripts check local authentication settings; they cannot inspect or disable account-side billing options. Existing extra-credit balances may be consumed by the service after included usage runs out.

Start the Codex loop. Each invocation makes one focused informal research or strategic-review step, with an explicit connection to the main RH gap. A complete informal argument is first recorded as an unverified candidate for critical review. The loop repeats until stopped, a failure safeguard triggers, or the notebook reaches its reviewed success criteria:

```bash
bash loop-codex.sh
```

Ctrl+C stops the active process and loop. Logs and persistent retry state live in the `scripts/loop-codex/` folder and are ignored by Git; research decisions remain in `history/`. File locks prevent simultaneous loop runs from editing the notebook.

Quotas trigger a wait until an unambiguous reported reset time plus a buffer, or increasing retries capped at hourly when no reset time is available. Restarting preserves the wait. Authentication/configuration failures stop with an explanation. Repeated unclassified failures or runs without recorded progress also stop for inspection. The computer and terminal session must remain running for automatic retries.

Use `bash loop-codex.sh --check` for a local setup check, `--dry-run` to inspect the command, `--once` for one step, or `--verbose` to stream CLI events. [Runner details and tests](scripts/loop/README.md).
