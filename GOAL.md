# Goal

Develop complete, checkable informal resolutions of the problems listed in scripts/loop/problems.json. Each problem has its own GOAL.md specifying its exact target. These shared standards apply to every notebook.

## Success criteria

STATUS in PROGRESS.md may become PROVED or DISPROVED only if ALL of the following hold:

1. There is a single main argument summarized in PROOF.md, with full proofs in lemmas/ and standard inputs in foundations/, that starts from standard, named theorems (no original “well-known facts” that are actually target-equivalent).
2. Every lemma is stated with hypotheses, conclusion, and a proof or a precise citation (book + theorem number, or a standard named theorem).
3. The argument does not assume the conclusion, does not hide an equivalent form of the target as a lemma, and does not rely on numerical evidence, “it is plausible”, or an unstated interchange of limits.
4. A dedicated section named “Known traps checked” lists the usual collapse points and explains why this write-up is not one of them.
5. The claimed resolution has been critically reviewed against its exact hypotheses, every essential dependency, and the known traps. A complete-looking but unverified argument is a candidate, not a verified resolution.

If the argument only proves a weakening, STATUS stays IN_PROGRESS and the weakening is recorded under “Partial results”.

## Relevance and stopping rules

Optimize for closing the main target gap, not for growing the lemma count. At the start of every turn, read the whole PROOF.md overview and inspect the local DAG before loading detailed proofs. Identify the precise unresolved claim separating the current argument from resolving the exact local target.

Before undertaking a calculation or adding a lemma, identify the gap it addresses, explain why the step could help, and state the result or threshold sought and what finding would justify continuing or abandoning it. A plausible downstream use is required; a complete route to the target need not already be proved. Explicitly name remaining unresolved steps. Useful intermediate lemmas are allowed even when other independent gaps remain.

Check existing theorems, duplicates, and failed approaches first. Preserve existing identifiers and evidence. Novelty and lemma count alone do not justify work. Compare achieved bounds with the required threshold without presenting a weakening or equivalent criterion as a solution.

Stopping rules apply to individual approaches, not to research as a whole. After two unproductive turns on an approach, reassess it and either test a materially different mechanism, choose another gap, or begin bounded discovery. Reopening requires a specific new idea and a discriminating test, not an already-established completion mechanism. Historical admission conditions, do not override this policy; their mathematical obstructions remain relevant evidence.

When no technical continuation is justified, actively discover candidates rather than wait for the user to supply one. Allow at most three exploration turns without a mathematical advance or informative negative result. Identify up to three distinct approaches to a named gap, compare them with recorded failures, and test the best concrete intermediate target. By the third turn, record the evidence and a continuation or stop decision. Changing route names or repeating audits does not renew the budget. Exploration may fail and need not produce a lemma.

At the end of every completed turn, replace these fields in PROGRESS.md:

- `STEP_ID: <unique identifier>`: a fresh identifier for this completed step, including reviews that repeat a stop decision.
- `STEP_OUTCOME: ADVANCE|NEGATIVE|EXPLORATION|STALLED`: choose exactly one value. ADVANCE establishes a relevant mathematical input or repairs a real mathematical error; NEGATIVE supplies new evidence that changes a research decision; EXPLORATION performs a new bounded search or test without either result; STALLED supplies no new evidence or actionable test.
- `STEP_EVIDENCE: <brief result and relative artifact path>`: identify what was learned and where it is recorded. Rephrasing a checkpoint, repeating an obstruction, or merely appending history is not an advance or informative negative result.

Keep the bottleneck, route decision, exploration turns used, and exactly one concrete Next action in the compact checkpoint. Record the detailed evidence in history. The runner halts only the affected problem after two consecutive STALLED turns, three invalid/unchanged step reports, or three exploration turns without an ADVANCE or NEGATIVE. A third exploration turn must finish its assessment before returning. A research stop persists across launches until an explicit `--resume-research <problem>`; ordinary research turns must not reset it. This does not relax quota waits. These outcome labels are self-reports, not mathematical verification.

## Research and candidate review

The near-term milestone is a complete informal candidate argument with every essential mathematical step written out. Record it as an UNVERIFIED CANDIDATE in PROGRESS.md, keep STATUS: IN_PROGRESS while its correctness is unresolved, and state its weakest steps and a concrete critical-review action. An anticipated possibility of hallucination is a reason to label and review the candidate honestly, never permission to invent steps or conceal gaps.

For a proposed disproof, require a rigorous counterexample meeting the local goal. Refuting a strategy is not refuting its target. Use STATUS: DISPROVED for a reviewed disproof, STATUS: PROVED for a reviewed proof, and keep unverified candidates IN_PROGRESS.

## Lemma documentation

Keep the common section order: Hypotheses, Conclusion, Proof, Mathlib. The mathematical proof must be rigorous. Use Mathlib as a mathematical reference: state whether the full result is present, absent from the sources checked, or not checked. Distinguish a full matching theorem from supporting results, and retain relevant theorem names and direct links. Unknown availability is not evidence of absence. Look up coverage when it materially helps the argument; it is not a completion gate.

## Known traps

Check the problem-specific traps in the active notebook’s GOAL.md. Numerical evidence and equivalent reformulations are not resolutions.

## Working rules

- Read the shared GOAL.md, the local GOAL.md, and local PROGRESS.md at the start of every run. Use PROOF.md for the mathematical overview and the active notebook’s DAG.md to locate relevant lemma files. Load only the needed proofs and historical context.
- Store each lemma or corollary in its own `lemmas/LNNN-descriptive-title.md` or `lemmas/CNNNa-descriptive-title.md` file. Preserve existing identifiers. Include hypotheses, conclusion, full proof or precise citation, qualifications, and relevant verification details. File paths and reproduction commands in proof text are relative to the active problem directory.
- The active notebook’s `DAG.md` is the ONLY canonical node-and-edge source. Keep its minimal header and single plain-text block, with one `ID: inputs` row per lemma/corollary, in numerical order (corollaries after their numbered lemma). List only the IDs of direct mathematical inputs, separated by spaces; an empty right side means no lemma inputs. Resolve an ID by the unique `lemmas/ID-*.md` filename. Never add Mermaid, titles, file paths, click directives, redundant edge lists, or narrative commentary to the rows. Do not create dependency lists, dependency metadata, backlinks, other graphs, or a second node index anywhere else. Plain-text lemma citations within mathematical prose are allowed; lemma files must not link to other lemma files. Distinguish input uses from contrasts, historical motivation, and unproved conditions. Never introduce a cycle or use the missing target-equivalent positivity as an established premise.
- Keep `PROOF.md` a short narrative assembly, unresolved gap, partial-results overview, known-traps check. Do not append full lemmas, a graph, a per-lemma catalog, history, or next actions. Shared starting definitions and theorems live in `foundations/`.
- Keep `PROGRESS.md` the sole current status and next-action record. Replace its current state after each attempt; never append a historical log or repeat proofs, validation summaries, or project rules. Aim for at most 40 lines, and at most 100 lines for PROOF.md.
- After each attempt, append a brief dated decision entry under `history/`: what changed, where the approach failed if applicable, and the reason for the next direction. Link to the mathematical result instead of restating its proof. Start a new numbered session/part file before a history file exceeds about 100 lines, even on the same day.
- If an attempt dies, preserve its outcome and a one-paragraph WHY IT FAILS under `ATTEMPTS/`. Link to the canonical counterexample proof instead of copying its derivation. Historical files are not active task instructions.
- After editing documentation, run `python3 ../scripts/docs/check_structure.py --problem <active-problem>`. Review new or changed dependencies mathematically: structural validation cannot prove that the graph captures every mathematical input or that a proof is correct.
- Never create additional root files unless explicitly requested by the user. The shared root files and registered problem directories are user-authorized; research turns create artifacts only inside their active notebook. Place scripts and outputs under `scripts/<topic>/`; other material belongs in an appropriate subfolder.
- Never set STATUS: PROVED or DISPROVED unless every success criterion above is met. A wrong proof is worse than no proof.
- Do not use an API key. Edit only the active problem directory during research turns. Shared instructions and infrastructure are read-only during research turns. If rate-limited, stop cleanly with PROGRESS.md ready for resumption.

- `PROMPT.md` is the sole runnable research prompt for every provider. README contains launch instructions only. Each CLI invocation completes one coherent step; the external launcher owns repetition, quota waiting, and retries. Checkpoint before lengthy work because a quota interruption may prevent final updates.

- Lemma identifiers and DAG edges are local to each notebook. Do not assume a result from another notebook; restate and justify any imported mathematical input locally.
