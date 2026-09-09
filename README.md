An attempt to prove the Rieman hypothesis using a simple codex local loop.

# Progress log

## 260909w37 first run

- initial prompt ran for 2min
- recurrent prompt ran for 50min then hit 5h limit `¯\_(ツ)_/¯`

### initial prompt

Read GOAL.md and PROGRESS.md. You are running an informal research loop on the Riemann hypothesis. Do not use Lean. Do not use an API key.

Work only in this directory.
- Keep PROOF.md as the single current best write-up.
- After every attempt, append a dated log to PROGRESS.md: what you tried, where it broke, next lemma.
- If an attempt fails, copy it to ATTEMPTS/YYYY-MM-DD-short-name.md with a one-paragraph WHY IT FAILS.
- Prefer small lemmas over a heroic one-page proof.
- Never set STATUS: PROVED unless every success criterion in GOAL.md is met. If you only have a weakening, say so.
- If you are rate-limited, stop cleanly so a supervisor can resume you.

Continue from the “Next action” line in PROGRESS.md.

### recurrent prompt

Do not stop after one lemma. Read GOAL.md and PROGRESS.md. Execute the current “Next action” fully into PROOF.md. Then immediately take the new next action. Repeat until you hit a rate limit or STATUS is PROVED. After each lemma, update PROGRESS.md. Never wait for me.
