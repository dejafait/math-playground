# One focused informal research step

Read GOAL.md, PROGRESS.md, the whole PROOF.md overview, and the global DAG before choosing work. Inspect existing changes and preserve unfinished work.

Apply GOAL.md’s relevance and stopping rules. Identify the precise main RH bottleneck, the threshold or statement needed, and how the proposed result would contribute to a final proof or rigorous disproof. Check existing results for redundancy and previously failed approaches. If that connection is absent, do a strategic audit instead of inventing another lemma. After two consecutive unproductive turns on a route, audit or park it unless a concrete new mechanism justifies continuing.

Perform exactly one coherent informal research or review step. Prefer closing a central gap, repairing an essential proof, reusing or consolidating existing results, or ruling out a route in a way that changes the research decision. New lemmas are justified only by a concrete downstream use, not by novelty, difficulty, or lemma count. Compare every achieved bound against the actual required bound. Do not silently treat a weaker estimate or another equivalent criterion as a solution.

Store full informal proofs or precise named citations in the existing lemma format. Keep a Mathlib reference section with coverage stated as present, absent from the sources checked, or not checked. Preserve relevant theorem names and direct links, distinguishing supporting results from a match for the full statement. Library lookup is optional, not a completion gate. Preserve identifiers and qualifications. Keep DAG.md ID-only: one `ID: inputs` row per lemma/corollary, no Mermaid, names, or per-lemma paths. Update it only for genuine mathematical inputs, and update PROOF.md when the overall argument changes. Do not delete inactive branches or duplicate them as a second graph/index.

Save unfinished reasoning before lengthy work or quota exhaustion. Record the result, its effect on the main gap, and the reason for the next direction in a brief dated history entry. Keep PROGRESS.md the sole compact current checkpoint: bottleneck, route decision, and exactly one concrete Next action. A strategic review may finish with no new lemma.

If a complete informal proof or disproof appears, record an UNVERIFIED CANDIDATE and its essential argument, dependencies, weakest steps, and review questions. Keep STATUS: IN_PROGRESS while correctness is unresolved. Do not call a potentially hallucinated argument verified. The next ordinary turn critically reviews the candidate informally rather than expanding peripheral branches. Apply all GOAL.md success criteria before claiming a verified result.

Run `python3 scripts/docs/check_structure.py` and only the mathematical/computational checks needed for this informal step. Report what changed toward the main goal, what remains missing, and the next action.

Return after this one step. The external loop owns repetition, quota waits, and retries. Do not start an inner agent loop, ask the user to continue, use API keys, buy credits, or modify the launchers, retry state, or this prompt during ordinary loop turns. Work only in this repository. Do not commit, reset, or discard existing changes.
