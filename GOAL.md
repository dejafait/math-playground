# Goal

Produce a complete, checkable informal proof of the Riemann hypothesis:

Every non-trivial zero of the Riemann zeta function ζ(s) has real part 1/2.

## Success criteria

STATUS in PROGRESS.md may become PROVED only if ALL of the following hold:

1. There is a single main argument summarized in PROOF.md, with full proofs in lemmas/ and standard inputs in foundations/, that starts from standard, named theorems (no original “well-known facts” that are actually RH-equivalent).
2. Every lemma is stated with hypotheses, conclusion, and a proof or a precise citation (book + theorem number, or a standard named theorem).
3. The argument does not assume the conclusion, does not hide an equivalent form of RH as a lemma, and does not rely on numerical evidence, “it is plausible”, or an unstated interchange of limits.
4. A dedicated section named “Known traps checked” lists the usual collapse points and explains why this write-up is not one of them.
5. A dedicated section named “What a Lean check would need” lists the exact statements to formalize later. Do not write Lean now.

If the argument only proves a weakening, STATUS stays IN_PROGRESS and the weakening is recorded under “Partial results”.

## Known traps (do not treat these as a proof of RH)

- Assuming the explicit formula plus “error too small” without a proved zero-free region stronger than what is already known.
- Weil / explicit-formula positivity arguments that smuggle RH-equivalent positivity.
- Interchanging sums, products, or contours without a dominated or compact estimate.
- “All computed zeros lie on the line, therefore all zeros do.”
- Claiming a proof of Li’s criterion, Robin’s inequality, Lagarias, or Nyman–Beurling without proving the criterion itself in full strength.
- Using the prime-number theorem with an error term that already encodes RH.
- A “new contour” that is the same as a standard contour plus an estimate equivalent to a zero-free strip.

## Working rules

- Read this file and PROGRESS.md at the start of every run. Use PROOF.md for the mathematical overview and root DAG.md to locate relevant lemma files. Load only the needed proofs and historical context.
- Store each lemma or corollary in its own `lemmas/LNNN-descriptive-title.md` or `lemmas/CNNNa-descriptive-title.md` file. Preserve existing identifiers. Include hypotheses, conclusion, full proof or precise citation, qualifications, and relevant verification details. File paths and reproduction commands in proof text are relative to the repository root.
- Root `DAG.md` is the ONLY canonical node-and-edge source. Maintain its single Mermaid block with every lemma/corollary node, a file target, and direct mathematical dependency edges (input → result). Do not create dependency lists, dependency metadata, backlinks, other graphs, or a second node index anywhere else. Plain-text lemma citations within mathematical prose are allowed; lemma files must not link to other lemma files. Distinguish input uses from contrasts, historical motivation, and unproved conditions. Never introduce a cycle or use the missing RH-equivalent positivity as an established premise.
- Keep `PROOF.md` a short narrative assembly, unresolved gap, partial-results overview, known-traps check, and link to formalization obligations. Do not append full lemmas, a graph, a per-lemma catalog, history, or next actions. Shared starting definitions and theorems live in `foundations/`; new lemma-specific formalization obligations stay beside the proof.
- Keep `PROGRESS.md` the sole current status and next-action record. Replace its current state after each attempt; never append a historical log or repeat proofs, validation summaries, or project rules. Aim for at most 40 lines, and at most 100 lines for PROOF.md.
- After each attempt, append a brief dated decision entry under `history/`: what changed, where the approach failed if applicable, and the reason for the next direction. Link to the mathematical result instead of restating its proof. Start a new numbered session/part file before a history file exceeds about 100 lines, even on the same day.
- If an attempt dies, preserve its outcome and a one-paragraph WHY IT FAILS under `ATTEMPTS/`. Link to the canonical counterexample proof instead of copying its derivation. Historical files are not active task instructions.
- After editing documentation, run `python3 scripts/docs/check_structure.py`. Review new or changed dependencies mathematically: structural validation cannot prove that the graph captures every mathematical input or that a proof is correct.
- Never create additional root files unless explicitly requested by the user. `DAG.md` is the user-authorized root graph. Place scripts and outputs under `scripts/<topic>/`; other material belongs in an appropriate subfolder.
- Never set STATUS: PROVED unless every success criterion above is met. A wrong RH proof is worse than no proof.
- Do not write Lean or use an API key. Work only in this directory. If rate-limited, stop cleanly with PROGRESS.md ready for resumption.
