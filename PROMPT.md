# One research step

Read GOAL.md and follow its research, storage, and validation rules. Read PROGRESS.md for the current state and Next action. Use PROOF.md for the argument and root DAG.md to locate only the lemmas needed for this step.

Inspect existing changes and any unfinished work before starting. Recover an interrupted step without discarding earlier work or repeating a completed result. Execute the current Next action as one coherent research step. If it is too large, complete a meaningful, precisely scoped part and leave the remainder explicit. A rigorously identified obstruction or corrected proof gap is useful progress; do not manufacture a theorem or claim certainty to satisfy the loop.

Store mathematics, graph changes, failed attempts, and a brief dated decision according to GOAL.md. Record the CLI/model used when known in the history entry. Update PROOF.md only when the overall argument changes. Keep PROGRESS.md short, with the current result or unfinished checkpoint and exactly one concrete Next action.

Checkpoint during substantial work: save draft reasoning under an appropriate subfolder and record where to resume before starting another lengthy calculation. Do not rely on being able to save after quota exhaustion. Keep unfinished claims explicitly unproved; do not promote draft claims to proved DAG inputs.

Run python3 scripts/docs/check_structure.py and any mathematical or computational verification required for this step. Repair issues introduced by this step. Never set STATUS: PROVED unless every criterion in GOAL.md is met.

Then return a short account of the result, validation, and next action. Return after this step; the external loop will invoke this same prompt again. Do not start another agent loop, ask the user to continue, change subscriptions, buy credits, use API keys, or alter the loop scripts, their retry state, or this prompt. Do not write Lean. Work only in this repository. Do not commit, reset, or discard existing changes.
