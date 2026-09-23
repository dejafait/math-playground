# Codex loop implementation

The root `loop-codex.sh` launcher locates the repository regardless of the caller's directory and invokes `runner.py`. `codex.py` supplies the Codex command and authentication checks; `events.py` classifies structured failures and explicit retry times. Prompt text is read afresh from root PROMPT.md every iteration and passed literally on stdin.

## Operation

Each run is a fresh CLI session which resumes from the notebook files. PROMPT.md now directs informal research or strategic review, with relevance checks against the main RH gap. A candidate argument is recorded honestly and reviewed informally. Existing quota waits and stop safeguards remain in force. The selected model follows the Codex configured default; no model or paid fallback is selected by the wrapper. Codex must support the flags shown by `--dry-run`. The loop uses ChatGPT subscription authentication.

Codex uses workspace-write with approvals set to never. Existing Codex policies may further restrict execution; the loop does not disable those policies.

Local checks reject known Codex API credentials and custom-provider settings. The loop checks ChatGPT login and forces the OpenAI provider and ChatGPT authentication. These checks do not verify remaining subscription quota, additional credit balance, or auto-top-up settings. Disable extra usage in the account to keep spending capped.

Runtime data is stored in `scripts/loop-codex/`: `state.json` (outcome and next retry), `process.lock`, and stdout/stderr logs. Each stream rotates at 2 MiB with two backups (roughly 12 MiB total). Codex session files remain governed by its retention settings. Logs can contain notebook text; they are not research records and are ignored by Git. Never edit retry state to bypass a quota limit.

The `process.lock` prevents duplicate loop runs; `workspace.lock` protects notebook edits. Both are kernel file locks, released automatically on process exit; their files remain intentionally. Stop the loop before manually editing the notebook or runner.

Quota fallback waits are 5, 15, 30, then 60 minutes. Temporary transport failures back off from 30 seconds to 15 minutes. Explicit reset timestamps or retry-after durations take precedence when later, with a 60-second buffer. Ambiguous human-readable dates use fallback waits. Structured error events are inspected separately from tool results, so a proof discussing rate limits does not cause a spurious pause. Unknown failures retry three times, then stop. Three successful exits without a changed progress/history checkpoint also stop. Completed steps must pass the documentation checker. These checks establish neither mathematical validity nor that changed text is useful progress.

`--timeout SECONDS` bounds one CLI invocation (default two hours), then retains partial work for a fresh invocation. Ctrl+C/SIGTERM interrupts the process group and escalates termination if necessary. A saved checkpoint can survive an interruption; the current in-memory thought cannot be guaranteed. `--once` still honors persisted quota waiting. `--check` performs local CLI status/configuration reads but no model inference; `--dry-run` does not call Codex and creates no runtime files.

## Verification

```bash
python3 -B -m unittest discover -s scripts/loop -p 'test_*.py' -v
python3 scripts/docs/check_structure.py
```

Tests use temporary notebooks and a fake Codex executable. They do not spend subscription allowance. Live inference is not part of these checks.

## Reference

- [Codex non-interactive execution](https://learn.chatgpt.com/docs/non-interactive-mode)
