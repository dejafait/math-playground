# Riemann hypothesis research

This repository focuses exclusively on the Riemann hypothesis. [GOAL.md](GOAL.md) defines the research standards and [PROMPT.md](PROMPT.md) defines one step. The [Riemann notebook](riemann/GOAL.md) retains its checkpoints, proof overview, canonical DAG, lemmas, sources and mathematical evidence.

The other nine notebooks were removed after their complete tracked progress was committed at `40a7e3f9`. Their files remain recoverable from Git history.

Install Python 3.9+ and the [Codex CLI](https://developers.openai.com/codex/cli), then run `codex login` using ChatGPT. Do not configure API keys or custom paid providers. Keep paid extra usage and automatic top-ups disabled in your account; the wrapper cannot inspect account-side billing settings.

On a fresh clone, restore the saved large-certificate bytes before running mathematical scripts:

```bash
make -f scripts/maintenance/Makefile evidence
```

These are lossless versioned archives with exact compressed and expanded checksums, not newly generated numerical results. The shared documentation checker also performs this restoration. Changed local evidence is never overwritten. Some historical full proof/execution streams remain locally generated artifacts; their compact certificates and source bindings are versioned in the [recovered evidence inventory](scripts/maintenance/recovered-evidence-inventory.json).

```bash
bash loop-codex.sh
```

The loop visits enabled notebooks in the order in [the registry](scripts/loop/problems.json), one fresh session and coherent step each. Only Riemann is registered; every research invocation continues its checkpoint. New research targets first require a saved literature assessment; missing or blocked evidence restricts the next turn to source review. Recaps distinguish known imports, reproductions and potentially new results. Each session runs from its problem directory; mathematical reproduction commands are relative to that directory. Shared loop and validation scripts stay at the root.

The scheduler persists its position and keeps trying enabled, unresolved problems without a research retry limit. Exhausted approaches and process failures queue recovery; repeated failures require a different next target instead of permanently halting the problem. Quota cooldowns apply globally and survive restart. Resolved and disabled notebooks are skipped. If none remain eligible, the loop prints their individual reasons and exits. Ctrl+C stops the active process and preserves files. The computer and terminal session must remain running for automatic retries.

```bash
bash loop-codex.sh --dry-run
bash loop-codex.sh --check
bash loop-codex.sh --once
bash loop-codex.sh --problem riemann --once
bash loop-codex.sh --status
bash loop-codex.sh --recover-research
bash loop-codex.sh --resume-research riemann
```

`--resume-research ID` renews only that notebook's research budget, then runs the normal rotation; add `--problem ID` to focus exclusively on it. `--timeout SECONDS` applies the same maximum duration to each invocation (default: two hours). `--verbose` streams CLI output.

Runtime state and per-problem logs live under `scripts/loop-codex/` and are ignored by Git. Legacy research halts automatically become queued recovery turns while preserving their reasons, counters and quota waits. `--status` shows scheduling reasons without running research; `--recover-research` migrates saved stops and exits without a model call. Research decisions stay inside each notebook's `history/`. Stop the loop before manually editing notebooks or infrastructure.

```bash
python3 -B scripts/docs/check_structure.py
python3 -B scripts/docs/check_structure.py --problem riemann
python3 -B -m unittest discover -s scripts/loop -p 'test_*.py' -q
python3 -B -m unittest discover -s scripts/docs -p 'test_*.py' -q
```

[Runner implementation details](scripts/loop/README.md). Structural checks do not establish mathematical correctness.
