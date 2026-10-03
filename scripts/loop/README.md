# Codex portfolio loop

The root launcher locates the repository from any calling directory. `runner.py` reads the ordered `problems.json` registry; `portfolio.py` validates it, migrates legacy RH counters and selects the next eligible notebook. `codex.py` retains the subscription authentication checks and command construction. `events.py` classifies failures without interpreting tool output as quota errors.

Each invocation starts a fresh session in the selected notebook directory. The literal root PROMPT.md is reread on every turn, prefixed with the active problem and shared instruction paths. Research artifacts and reproduction paths are local to that notebook; the shared documentation checker accepts `--problem ID`. The configured default model is retained. No API key or paid fallback is selected. Existing sandbox policies remain effective; instructions also restrict edits to the active notebook.

## Scheduling and persistence

One completed attempt advances the round-robin cursor. Successful, stalled and timed-out/unclassified attempts count as turns; quota, transient transport and interrupted invocations retain the current slot for retry. Each notebook records elapsed invocation seconds and turn count. Equal turns do not imply equal token consumption; token accounting is not inferred from wall time.

One ignored `scripts/loop-codex/state.json` atomically stores the next problem, global retry/authentication outcome, and a `problems` map of independent research counters. Legacy root research fields move into the `riemann` entry on first launch; global cooldowns and existing logs remain intact. The registry's `enabled` flag controls participation; runtime reasons and counters live in this separate state file. `bash loop-codex.sh --status` shows both, without authentication checks, model calls or writes. `--resume-research ID` explicitly renews only that problem's research budget.

Mathematical and literature turns have separate budgets. Three mathematical EXPLORATION attempts, two stalled mathematical attempts, two stalled literature turns, or invalid reports queue recovery. Ready coverage permits mathematics during recovery; source gaps require review. A fresh valid STALLED metadata repair clears recovery when its next assessment is ready. The last ten accepted turn kinds appear in status; guidance targets two mathematical turns per literature turn, falling toward one review in five after four mathematical turns. Ratios guide attempted work, not success or elapsed time. Further literature on ready targets requires LITERATURE_REASON. Persistent blockers require independent targets.
Existing persistent stops automatically migrate to recovery on normal launch. `bash loop-codex.sh --recover-research` performs only this migration and exits, retaining quota waits and counters. Use `--problem ID` to limit migration. There is no permanent automatic research halt. Exhausted routes and repeated recovery failures require a different Next action before counters renew. The prompt also requires a materially different mechanism, not a renamed target; that semantic distinction cannot be proved by a string check. `--resume-research ID` explicitly renews a budget. Disabled entries remain unscheduled. Resolved notebooks (`PROVED` or `DISPROVED`) are skipped unless a rejected turn still needs recovery; these labels require critical review under GOAL.md and are not mathematical verification by the runner. An empty schedule prints the reason for every selected problem.

Quota cooldowns apply to the entire account. Fallback waits are 5, 15, 30, then 60 minutes; explicit resets plus a 60-second buffer take precedence when later. Transport failures back off from 30 seconds to 15 minutes. Authentication/configuration failures pause and retry every five minutes without invoking the model while local checks fail. A user may need to repair login or configuration; the loop remains alive and interruptible. Invalid startup arguments, corrupt state and a conflicting process lock are reported as errors rather than overwritten. Three unclassified failures in one notebook queue recovery, even when other notebooks make progress. Restarting, selecting a problem, or resuming research never bypasses a quota wait.

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

## Literature gate

Before invocation, `literature.py` binds `NEXT_REVIEW` to the exact saved `Next action`. Missing, incomplete, stale-target or source-blocked assessments select a literature-only turn. Ready IMPORT/SPECIALIZE/EXPLORE assessments permit the matching research target. Uncovered directions require a prior review turn; literature turns can approve their next target. Optional SCOPE and repeated COVERED_TARGET fields permit explicit preapproved subtargets; completed work uses STEP_KIND, STEP_CLASSIFICATION and STEP_REVIEW. The full schema and decisions are in ../../GOAL.md.

The launcher explicitly requests `web_search="live"` rather than depending on a user's search default. Managed restrictions and source access failures can still prevent retrieval; record those failures, never infer that a theorem is absent. This does not change shell sandbox or approval settings.

After invocation, the gate validates the completed and next assessments before outcome counters can reset. Literature-only turns cannot change mathematical lemma or script files. Invalid reports queue recovery only for the affected notebook, including reports claiming resolution. Direct source URLs may appear in the assessment body as well as SOURCE_EVIDENCE. Source truth and novelty remain matters for mathematical review; the checks cannot detect fabricated evidence. Existing notebooks migrate through a literature turn without resetting quota state; saved research stops are preserved as recovery reasons.

Use `python3 -B -m unittest discover -s scripts/loop -p 'test_*.py' -q` for an offline scheduling round and gate regressions. These use fake processes, not ten paid research calls. Actual research resumes through the usual launcher, with one review or research step per notebook.
