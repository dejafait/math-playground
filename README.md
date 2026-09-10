# Riemann hypothesis research notebook

Read [GOAL.md](GOAL.md) for the goal and canonical working rules, [PROGRESS.md](PROGRESS.md) to resume, and [PROOF.md](PROOF.md) for the mathematical overview. Root [DAG.md](DAG.md) contains the sole graph definition and links to all lemma files. Research decisions live in [history/](history/) and failed strategies in [ATTEMPTS/](ATTEMPTS/).

## Initial prompt

Read GOAL.md and PROGRESS.md. Run the informal research loop under the working rules in GOAL.md. Continue from the current Next action in PROGRESS.md. Store full results in individual lemma files and update the sole graph in root DAG.md. Keep the proof overview and current progress short. Record decisions in history/ and failed strategies in ATTEMPTS/, linking to proofs. Do not use Lean or an API key. Work only in this directory. Never claim PROVED unless all success criteria are met.

## Recurrent prompt

Read GOAL.md and PROGRESS.md and follow GOAL.md's current storage and validation rules. Execute the current Next action into the appropriate individual lemma file(s); maintain root DAG.md, replace the current state in PROGRESS.md, and append a brief decision to history/. Update PROOF.md only if the overall argument changes. Run the documentation structure check. Then take the new next action and repeat until rate-limited or STATUS is PROVED. Do not stop after one lemma or wait for me.
