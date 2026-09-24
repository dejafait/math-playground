# Codex portfolio loop

The root launcher locates the repository from any calling directory. `runner.py` reads the ordered `problems.json` registry; `portfolio.py` validates it, migrates legacy RH counters and selects the next eligible notebook. `codex.py` retains the subscription authentication checks and command construction. `events.py` classifies failures without interpreting tool output as quota errors.

Each invocation starts a fresh session in the selected notebook directory. The literal root PROMPT.md is reread on every turn, prefixed with the active problem and shared instruction paths. Research artifacts and reproduction paths are local to that notebook; the shared documentation checker accepts `--problem ID`. The configured default model is retained. No API key or paid fallback is selected. Existing sandbox policies remain effective; instructions also restrict edits to the active notebook.

## Scheduling and persistence

One completed attempt advances the round-robin cursor. Successful, stalled and timed-out/unclassified attempts count as turns; quota, transient transport and interrupted invocations retain the current slot for retry. Each notebook records elapsed invocation seconds and turn count. Equal turns do not imply equal token consumption; token accounting is not inferred from wall time.

One ignored `scripts/loop-codex/state.json` atomically stores the next problem, global retry/authentication outcome, and a `problems` map of independent research counters. Legacy root research fields move into the `riemann` entry on first launch; global cooldowns and existing logs remain intact. No notebook's research halt is reset by switching to another. `--resume-research ID` explicitly renews only that problem's research budget.

After two STALLED reports, three invalid/stale reports, or three EXPLORATION turns without ADVANCE or NEGATIVE, that notebook is halted. Validation failure also halts the affected notebook. Other eligible notebooks continue. Resolved notebooks (`PROVED` or `DISPROVED`) are skipped; these labels require critical review under GOAL.md and are not mathematical verification by the runner. If no eligible notebook remains, the loop exits. Disabled entries remain on disk but are not scheduled.

Quota cooldowns apply to the entire account. Fallback waits are 5, 15, 30, then 60 minutes; explicit resets plus a 60-second buffer take precedence when later. Transport failures back off from 30 seconds to 15 minutes. Authentication/configuration failures stop the launcher. Three unclassified failures in one notebook halt that notebook, even when other notebooks make progress. Restarting, selecting a problem, or resuming research never bypasses a quota wait.

`process.lock` prevents duplicate launcher runs and `workspace.lock` protects notebook edits. Both are kernel locks released on process exit. Stop the loop before manual edits. Ctrl+C/SIGTERM stops the process group, retaining partial files and the current slot. A two-hour default timeout bounds each invocation; `--timeout` overrides it.

Each notebook has rotating stdout/stderr logs under `scripts/loop-codex/ID/` (2 MiB per stream, two backups). Codex session retention is separate. Logs are operational diagnostics, not research history. They can contain notebook text. `--dry-run` makes no model call and creates no runtime state; `--check` checks local login/configuration without inference. `--once` still honors saved cooldowns.

## Verification

```bash
python3 -B -m unittest discover -s scripts/loop -p 'test_*.py' -q
python3 -B -m unittest discover -s scripts/docs -p 'test_*.py' -q
python3 -B scripts/docs/check_structure.py
bash loop-codex.sh --dry-run
```

Tests use temporary notebooks and fake Codex processes; they spend no model allowance. The process-termination regression uses `ps`, which may require running outside a restrictive sandbox.
