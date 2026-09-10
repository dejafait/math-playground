# Shared loop implementation

The four root launchers locate the repository regardless of the caller's directory and invoke `runner.py`. `providers.py` adapts each CLI; `events.py` classifies structured failures and explicit retry times. Prompt text is read afresh from root PROMPT.md every iteration and is never duplicated here. Codex, Claude, and Gemini receive it on stdin; Grok reads it directly through `--prompt-file PROMPT.md`. No adapter evaluates prompt text as shell code.

## Operation

Each run is a fresh CLI session which resumes from the notebook files. The selected model follows the provider's normal configured default; no model or paid fallback is selected by the wrapper. All four CLIs must be current enough to support the flags shown by `--dry-run`. The loop uses subscription/browser authentication. For Claude, use a version supporting `--permission-prompts none`; the loop deliberately does not use `--bare`, which bypasses subscription login.

Codex uses workspace-write with approvals set to never. Claude accepts edits and explicitly allows research read/write tools, Python, search, and read-only Git inspection; other requests are denied without waiting for input. Gemini uses its sandbox, automatic edits, and limited shell-tool approvals; configure a working sandbox backend before launch. Grok auto-approves tools inside its workspace sandbox. Existing vendor policies may further restrict execution; the loop does not disable those policies. CLI sandboxes differ, so these are not claims of identical filesystem isolation.

Local checks reject known API credentials and custom-provider settings. Codex checks ChatGPT login and forces the OpenAI provider and ChatGPT authentication. Claude checks first-party claude.ai login with a Pro or Max subscription. Gemini checks Google-login settings and rejects credential assignments in discovered .env files. Grok rejects API-key/custom-model overrides; its docs have no auth-status command, so `--check` cannot confirm cached Grok login or subscription entitlement. Run `grok login` first. None of these checks verifies a remote subscription's remaining quota, additional credit balance, or auto-top-up settings. Disable extra usage in the provider account to keep spending capped.

Runtime data is stored in `scripts/loop-<vendor>/`: `state.json` (outcome and next retry), `process.lock`, and stdout/stderr logs. Each stream rotates at 2 MiB with two backups (roughly 12 MiB total per provider). Provider-native session files remain governed by the vendor's retention settings. Logs can contain notebook text; they are not research records and are ignored by Git. Never edit retry state to bypass a provider limit.

The shared `workspace.lock` is a kernel file lock, released automatically on process exit; its file remains intentionally. Different provider loops may wait concurrently but only one edits at a time. Do not use this to launch an interactive editor/agent against the same files concurrently. Stop loops before manually editing the notebook or runner.

Quota fallback waits are 5, 15, 30, then 60 minutes. Temporary transport failures back off from 30 seconds to 15 minutes. Explicit reset timestamps or retry-after durations take precedence when later, with a 60-second buffer. Ambiguous human-readable dates use fallback waits. Structured error events are inspected separately from tool results, so a proof discussing rate limits does not cause a spurious pause. Unknown failures retry three times, then stop. Three successful exits without a changed progress/history checkpoint also stop. Completed steps must pass the documentation checker. These checks establish neither mathematical validity nor that changed text is useful progress.

`--timeout SECONDS` bounds one CLI invocation (default two hours), then retains partial work for a fresh invocation. Ctrl+C/SIGTERM interrupts the process group and escalates termination if necessary. A saved checkpoint can survive an interruption; the current in-memory thought cannot be guaranteed. `--once` still honors persisted quota waiting. `--check` performs local CLI status/configuration reads but no model inference; `--dry-run` calls no vendor CLI and creates no runtime files.

## Verification

```bash
python3 -B -m unittest discover -s scripts/loop -p 'test_*.py' -v
python3 scripts/docs/check_structure.py
```

Tests use temporary notebooks and fake CLI executables. They do not spend subscription allowance. Live inference was not part of implementation validation; Gemini and Grok were not installed on the development machine.

## Adapter references

- [Codex non-interactive execution](https://learn.chatgpt.com/docs/non-interactive-mode)
- [Claude programmatic execution and permissions](https://code.claude.com/docs/en/headless)
- [Gemini headless output](https://geminicli.com/docs/cli/headless/) and [cached-login authentication](https://geminicli.com/docs/get-started/authentication/)
- [Grok scripting](https://docs.x.ai/build/cli/headless-scripting), [settings](https://docs.x.ai/build/settings/reference), and [subscription credits](https://docs.x.ai/grok/faq)

- [Grok native streaming event schema and prompt-file flag](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/14-headless-mode.md)
