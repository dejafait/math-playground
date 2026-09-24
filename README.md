# Mathematical research portfolio

Ten independent mathematical notebooks share one Codex research loop. [GOAL.md](GOAL.md) defines common standards and [PROMPT.md](PROMPT.md) defines one research step. Each notebook has its own goal, progress checkpoint, proof overview, canonical DAG, lemmas, foundations, drafts, attempts, history and mathematical scripts.

| Notebook | Target |
| --- | --- |
| [riemann](riemann/GOAL.md) | Riemann hypothesis; existing research preserved |
| [p-vs-np](p-vs-np/GOAL.md) | P versus NP |
| [hodge](hodge/GOAL.md) | Rational Hodge conjecture |
| [birch-swinnerton-dyer](birch-swinnerton-dyer/GOAL.md) | Birch and Swinnerton-Dyer conjecture |
| [yang-mills](yang-mills/GOAL.md) | Yang–Mills existence and mass gap |
| [beal](beal/GOAL.md) | Beal conjecture |
| [collatz](collatz/GOAL.md) | Collatz conjecture |
| [iut-challenge](iut-challenge/GOAL.md) | Demonstrate an inherent flaw in IUT theory |
| [reed-solomon-mca](reed-solomon-mca/GOAL.md) | Grand mutual-correlated-agreement challenge |
| [reed-solomon-list-decoding](reed-solomon-list-decoding/GOAL.md) | Grand list-decoding challenge |

The two Reed–Solomon problems share a prize pool, not a fixed individual reward. IUT is a theory-verification challenge. Prize eligibility and mathematical correctness are separate; no notebook claims a resolution merely by entering this portfolio.

Install Python 3.9+ and the [Codex CLI](https://developers.openai.com/codex/cli), then run `codex login` using ChatGPT. Do not configure API keys or custom paid providers. Keep paid extra usage and automatic top-ups disabled in your account; the wrapper cannot inspect account-side billing settings.

```bash
bash loop-codex.sh
```

The loop visits enabled notebooks in the order in [the registry](scripts/loop/problems.json), one fresh session and coherent step each. Ten active notebooks receive equal turns, not guaranteed equal tokens or time. Each session runs from its problem directory; mathematical reproduction commands are relative to that directory. Shared loop and validation scripts stay at the root.

The scheduler persists its position. Research halts apply to one notebook; quota cooldowns apply globally and survive restart. Resolved, disabled and halted notebooks are skipped. If none remain eligible, the loop exits. Ctrl+C stops the active process and preserves files. The computer and terminal session must remain running for automatic retries.

```bash
bash loop-codex.sh --dry-run
bash loop-codex.sh --check
bash loop-codex.sh --once
bash loop-codex.sh --problem beal --once
bash loop-codex.sh --resume-research riemann
```

`--resume-research ID` renews only that notebook's research budget, then runs the normal rotation; add `--problem ID` to focus exclusively on it. `--timeout SECONDS` applies the same maximum duration to each invocation (default: two hours). `--verbose` streams CLI output.

Runtime state and per-problem logs live under `scripts/loop-codex/` and are ignored by Git. Legacy RH counters are migrated automatically on first launch without resetting a research halt or quota wait. Research decisions stay inside each notebook's `history/`. Stop the loop before manually editing notebooks or infrastructure.

```bash
python3 -B scripts/docs/check_structure.py
python3 -B scripts/docs/check_structure.py --problem riemann
python3 -B -m unittest discover -s scripts/loop -p 'test_*.py' -q
python3 -B -m unittest discover -s scripts/docs -p 'test_*.py' -q
```

[Runner implementation details](scripts/loop/README.md). Structural checks do not establish mathematical correctness.
