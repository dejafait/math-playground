# Goal

Develop a complete, checkable informal argument proving or disproving the Riemann hypothesis:

Every non-trivial zero of the Riemann zeta function ζ(s) has real part 1/2.

## Success criteria

STATUS in PROGRESS.md may become PROVED only if ALL of the following hold:

1. There is a single main argument summarized in PROOF.md, with full proofs in lemmas/ and standard inputs in foundations/, that starts from standard, named theorems (no original “well-known facts” that are actually RH-equivalent).
2. Every lemma is stated with hypotheses, conclusion, and a proof or a precise citation (book + theorem number, or a standard named theorem).
3. The argument does not assume the conclusion, does not hide an equivalent form of RH as a lemma, and does not rely on numerical evidence, “it is plausible”, or an unstated interchange of limits.
4. A dedicated section named “Known traps checked” lists the usual collapse points and explains why this write-up is not one of them.
5. The claimed resolution has been critically reviewed against its exact hypotheses, every essential dependency, and the known traps. A complete-looking but unverified argument is a candidate, not a verified resolution. Lean formalization is not a current requirement or an automatic next step.

If the argument only proves a weakening, STATUS stays IN_PROGRESS and the weakening is recorded under “Partial results”.

## Relevance and stopping rules

Optimize for closing the main RH gap, not for growing the lemma count. At the start of every turn, read the whole PROOF.md overview and inspect the global DAG before loading detailed proofs. Identify the precise unresolved claim separating the current argument from proving RH or producing a rigorously established off-line nontrivial zero.

Before undertaking a calculation or adding a lemma, state in PROGRESS.md: the bottleneck it addresses, the result or quantitative threshold needed, and how that result would be used in the main argument. A chain of dependencies alone is not evidence of relevance. If that connection is missing, audit or consolidate the route instead of extending it.

Check for an existing theorem, stronger lemma, duplicate argument, or already-disproved strategy first. Prefer reusing a result or improving an existing exposition over assigning a new identifier to a routine consequence or another special case. Preserve identifiers and evidence; do not delete historical lemmas just because they are inactive. Keep route classifications in prose, not a second graph or node index.

Each turn must either reduce a specific gap, establish a necessary input with a stated downstream use, repair a real error, or rule out an approach in a way that changes the research decision. Extra equivalent criteria, counterexamples to already-refuted shortcuts, cosmetic improvements, and estimates that still miss the needed scale are not by themselves progress toward RH.

Compare achieved bounds with the required threshold explicitly. After two consecutive turns on a route fail to reduce its bottleneck or produce evidence that changes the route decision, make the next turn a strategic audit, not another technical extension. Continue that route only with a concrete new mechanism; otherwise park it and choose a better justified route. Record negative results honestly rather than manufacturing lemmas to keep the loop busy.

Before ending each turn, explain what changed in the global argument and what remains missing. Keep a short bottleneck and route decision in PROGRESS.md and the detailed rationale in history. Periodically audit whether apparently central branches are actually used by a plausible final argument. Novelty, difficulty, formalizability, and lemma count are not substitutes for relevance.

## Informal research; formalization paused

All ordinary loop turns now focus on informal mathematics or strategic review under the relevance rules above. This supersedes the former Lean catch-up-first policy everywhere, including stale checkpoints, archived history, and lemma-specific formalization obligations. Missing, partial, conditional, or failed Lean proofs do not block research.

Do not write, repair, compile, or extend Lean proofs; do not run Lake, fetch Lean caches, upgrade toolchains, or spend a turn inventorying the formalization backlog. Preserve existing Lean sources, embedded proofs, validation evidence, and unfinished work for possible later use. Existing formalization notes are archival obligations, not current tasks. Resume formalization only on explicit user instruction, not automatically when an informal candidate appears.

The near-term milestone is a complete informal candidate argument with every essential mathematical step written out. Record it as an UNVERIFIED CANDIDATE in PROGRESS.md, keep STATUS: IN_PROGRESS while its correctness is unresolved, and state its weakest steps and a concrete critical-review action. An anticipated possibility of hallucination is a reason to label and review the candidate honestly, never permission to invent steps or conceal gaps. Do not require a Lean proof before recording this milestone. The user can later choose to formalize the essential dependency chain; peripheral lemmas need not all be formalized.

For a proposed disproof, require an actual nontrivial off-line zero with a rigorous certificate; a counterexample to a proposed RH proof strategy is not a disproof of RH. Do not change STATUS to PROVED for an unreviewed candidate or merely because no gap was noticed. If a disproof is rigorously established, record that outcome explicitly rather than calling RH proved.

## Lemma documentation

Keep the common section order: Hypotheses, Conclusion, Proof, Mathlib, Lean proof status, Lean proof command, Lean proof code. The mathematical proof is informal and must be rigorous. Retain existing formalization sections as evidence, without redoing their work. For new lemmas, mark formalization “Paused; not required in the current research phase”, and commands/code “Not available”. Mathlib lookup is optional and should be done only when it materially helps the informal argument; otherwise say it has not been checked. Do not spend turns filling placeholder sections or searching for library coverage merely for consistency.

If an informal statement with existing Lean evidence changes, note that the evidence applies to the former statement and is not validation of the revision. Preserve the source without repairing it during this phase. No broad rewrite of existing lemma files is required merely to announce this pause.

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
- Root `DAG.md` is the ONLY canonical node-and-edge source. Keep its minimal header and single plain-text block, with one `ID: inputs` row per lemma/corollary, in numerical order (corollaries after their numbered lemma). List only the IDs of direct mathematical inputs, separated by spaces; an empty right side means no lemma inputs. Resolve an ID by the unique `lemmas/ID-*.md` filename. Never add Mermaid, titles, file paths, click directives, redundant edge lists, or narrative commentary to the rows. Do not create dependency lists, dependency metadata, backlinks, other graphs, or a second node index anywhere else. Plain-text lemma citations within mathematical prose are allowed; lemma files must not link to other lemma files. Distinguish input uses from contrasts, historical motivation, and unproved conditions. Never introduce a cycle or use the missing RH-equivalent positivity as an established premise.
- Keep `PROOF.md` a short narrative assembly, unresolved gap, partial-results overview, known-traps check, and link to formalization obligations. Do not append full lemmas, a graph, a per-lemma catalog, history, or next actions. Shared starting definitions and theorems live in `foundations/`; new lemma-specific formalization obligations stay beside the proof.
- Keep `PROGRESS.md` the sole current status and next-action record. Replace its current state after each attempt; never append a historical log or repeat proofs, validation summaries, or project rules. Aim for at most 40 lines, and at most 100 lines for PROOF.md.
- After each attempt, append a brief dated decision entry under `history/`: what changed, where the approach failed if applicable, and the reason for the next direction. Link to the mathematical result instead of restating its proof. Start a new numbered session/part file before a history file exceeds about 100 lines, even on the same day.
- If an attempt dies, preserve its outcome and a one-paragraph WHY IT FAILS under `ATTEMPTS/`. Link to the canonical counterexample proof instead of copying its derivation. Historical files are not active task instructions.
- After editing documentation, run `python3 scripts/docs/check_structure.py`. Review new or changed dependencies mathematically: structural validation cannot prove that the graph captures every mathematical input or that a proof is correct.
- Never create additional root files unless explicitly requested by the user. `DAG.md`, `PROMPT.md`, and the four `loop-<vendor>.sh` launchers are user-authorized root files. Place scripts and outputs under `scripts/<topic>/`; other material belongs in an appropriate subfolder.
- Never set STATUS: PROVED unless every success criterion above is met. A wrong RH proof is worse than no proof.
- Do not use an API key. Lean formalization is paused; pursue informal research or strategic review only unless the user explicitly resumes formalization. Work only in this directory. If rate-limited, stop cleanly with PROGRESS.md ready for resumption.

- `PROMPT.md` is the sole runnable research prompt for every provider. README contains launch instructions only. Each CLI invocation completes one coherent step; the external launcher owns repetition, quota waiting, and retries. Checkpoint before lengthy work because a quota interruption may prevent final updates.
