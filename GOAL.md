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

Keep the bottleneck, route decision, exploration turns used, and exactly one concrete Next action in the compact checkpoint. Three mathematical EXPLORATION attempts without ADVANCE or NEGATIVE require reassessing the mechanism; literature turns do not spend this calculation budget. Two stalled mathematical attempts or two stalled literature turns trigger recovery. Three invalid reports also trigger recovery. Recovery uses ready coverage for a concrete mathematical attempt; only missing essential source coverage requires literature-only work. A fresh valid metadata repair may clear recovery even when honestly labeled STALLED if its next assessment is ready. Exhausted mathematical routes and persistent source blockers require a different mechanism or independently testable target. Keep the original stop evidence. Ordinary turns must not edit scheduler state. Only the user stops the overall loop; quota waits remain unchanged.

Aim for two mathematical attempts per literature turn per notebook, measured over the last ten accepted turns. After at least four mathematical attempts in that window, aim for one literature turn in five. These are scheduling targets, not proof-success or lemma quotas and not wall-clock guarantees. Mathematical work includes proof attempts, calculations, counterexample searches, theorem applications and obstruction tests. Once coverage is ready, the next turn defaults to mathematics. Further literature work must record LITERATURE_REASON naming a changed hypothesis, essential unread source, or specific new relevant lead. Never repeat browsing merely to fill a quota. Essential missing coverage remains a justified exception; park persistently blocked dependent work and choose independent work.

## Literature reuse before research

Before substantial work on a new intermediate target, search for the exact statement, standard terminology, stronger results and known obstructions. Read primary theorem statements and follow relevant references; a prize page, search snippet, model memory or Mathlib homepage is not a literature assessment. Reuse an adequate assessment while its target and assumptions remain unchanged. Refresh it when the target moves outside its assessed scope, a relevant source changes, or new evidence undermines its comparison; no fixed search quota or repeated browsing every turn is required.

Store each assessment in `drafts/literature/<target>.md`. Use exactly one single-line value for each field: `TARGET` (the exact Next action text), `CHECKED` (YYYY-MM-DD), `DECISION`, `SEARCH_EVIDENCE`, `SOURCE_EVIDENCE`, `COMPARISON`, `GAP`, and `REASON`. Expand details below those fields. Record queries and what was actually read, source version and theorem/page numbers, applicability, strongest relevant known conclusion, remaining difference, and why a citation does not suffice. Explicitly distinguish unread leads from inspected theorems. Never infer novelty from a failed search.

`DECISION` is one of:

- `IMPORT`: the needed result is covered; cite it and give only the necessary applicability argument.
- `SPECIALIZE`: known results cover part of the target; derive only the identified difference. Explain any need for changed hypotheses, effective constants, verification of a suspect claim or an essential implementation.
- `EXPLORE`: a documented bounded search found no adequate match; investigate the stated gap without claiming novelty.
- `SOURCE_BLOCKED`: an essential source or exact target remains inaccessible; resolve access or source scope before dependent research.
- `REVIEW_REQUIRED`: discovery or theorem-level comparison remains incomplete; the next turn is literature-only.

`PROGRESS.md` must include `NEXT_REVIEW`, a notebook-relative assessment path matching its exact `Next action`. Preserve proposed calculations as targets while assessing them. At completion add `STEP_KIND: LITERATURE|RESEARCH`, `STEP_REVIEW` (the assessment for the target at turn start), and `STEP_CLASSIFICATION: KNOWN_IMPORTED|REPRODUCTION|POTENTIALLY_NEW|NOVELTY_UNCHECKED`. These describe the completed step, while NEXT_REVIEW describes future work. Existing historical reports need not be retroactively relabeled.

A research turn requires an IMPORT, SPECIALIZE or EXPLORE assessment saved before invocation. An uncovered target or changed assessment requires a separate literature turn. A literature turn may finish approving its next target; it need not invoke another review. Add optional SCOPE explaining covered hypotheses and techniques, and repeated COVERED_TARGET lines listing exact preapproved subtargets. These permit assessment reuse without edits during research; unlisted targets still require review. IMPORT permits only KNOWN_IMPORTED; SPECIALIZE/EXPLORE permit REPRODUCTION or POTENTIALLY_NEW. POTENTIALLY_NEW means only that the recorded search did not establish coverage, not certified originality. NOVELTY_UNCHECKED is restricted to literature turns. Literature turns may update source notes, assessments, histories and overviews, but may not derive new results or modify lemmas/ or mathematical scripts/. Missing evidence restricts work to literature review rather than waiting for the user.

Keep the existing outcome labels, but do not report importing or reproducing known mathematics as a new mathematical discovery. Every recap must distinguish local progress from progress beyond the sources checked. An assessment that merely repeats an old decision is STALLED; unanswered searches remain EXPLORATION, not an automatic budget reset. Source import or a documented overlap that changes a route can be useful progress. Existing stopping and quota rules still apply.

The runner checks field completeness, paths, exact target matching, prior assessment availability and classification before accepting an outcome. It rejects lemma/program writes in literature-only turns and queues recovery on violations without accepting the rejected outcome or resetting exploration counters. Counters renew only after a valid recovery report. These are process checks, not semantic validation of sources, proofs or novelty. Preserve all prior work; do not delete superseded derivations.

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

## Adaptive model and effort routing

The supervisor explicitly selects model and effort for each invocation, independently of the CLI default. Accepted checkpoints may recommend NEXT_TASK_TYPE (metadata, source_extraction, literature_comparison, calculation, implementation, proof_attempt, proof_audit), NEXT_MODEL_ROLE (routine, standard, deep_research), NEXT_EFFORT (low, medium, high, xhigh, max), NEXT_ROUTING_REASON, and optional NEXT_ESCALATION. Recommendations bind to the exact Next action; missing or invalid recommendations use task defaults without triggering research recovery. Keep the checkpoint compact.

Routine maps to gpt-6-luna, standard to gpt-6.1-sol, deep_research to gpt-6-astra. Bootstrap defaults are Sol/high for ready mathematical targets and Sol/medium for uncovered targets. Mechanical repairs/extraction can use Luna/low or medium; theorem comparison uses Sol/medium or high; difficult proofs, new mechanisms and critical audits use Astra/high. An unavailable cached model falls back explicitly to an available configured role; unsupported effort is lowered to a supported level. Absent capability data is recorded as unverified, not confirmed access. Model mappings remain explicit until reviewed; new defaults do not silently change them.

Max requires NEXT_ESCALATION naming a concrete unresolved obstruction, after a successful invocation reporting EXPLORATION or NEGATIVE at Astra/high or xhigh. Each invocation performs one bounded step. Max is limited to two of ten attempted invocations, and Astra to four of ten per notebook; the supervisor lowers settings beyond these limits. These are spending proxies, not exact subscription-credit limits. Lower settings may follow the hard reasoning step. Report tokens, elapsed time, requested/actual settings and validated outcomes separately; lemma count and self-reported advances do not establish quality. Subscription allowance is unavailable unless reliably observed; tokens and elapsed time are not exact credit costs. Quota waits, subscription-only authentication and notebook permissions remain unchanged.

## Input scope and economical context

Ordinary research reads only its active notebook plus shared instructions and narrowly required infrastructure. Use notebook-local searches, scoped git inspection and the checker with --problem; never read all problem checkpoints or proof files for orientation. Cross-notebook mathematical use is exceptional: first name the exact result and record CROSS_NOTEBOOK_REASON, then read only that input and justify any import locally. The supervisor audits observable command patterns; this is a behavioral policy, not a filesystem read sandbox or proof of compliance.

Read compact local overview/DAG before targeted proofs. Search specific histories for prior failures and read only relevant sections. Retrieve primary theorem hypotheses and relevant proof cases before larger source extracts. Batch independent small reads, retain sequential dependencies. Keep routine tool output concise; save full calculation certificates on disk with summaries of conclusions, thresholds, failures and paths. Larger reads remain permitted with a mathematical purpose. Do not omit needed hypotheses to meet an output target. Keep proofs canonical and continuation notes compact; preserve fresh sessions.

Completed research is not rejected merely because it selects a new ready continuation. The supervisor defers a newly written/changed next assessment to a separate literature approval turn, preserving the mathematical outcome and recommendation. Unchanged assessments saved before invocation are reusable for matching next targets. A valid stalled process repair can clear recovery without claiming mathematical progress; only genuine exhaustion or persistent source obstruction requires a new mechanism. Prior stops remain recorded.

## Verbatim startup context

The supervisor supplies the shared goal and local GOAL, PROGRESS, PROOF and DAG verbatim once per invocation, plus a bounded optional literature assessment. This satisfies their startup-read requirements; do not reread unchanged supplied content or the runnable prompt. Explicit NOT SUPPLIED markers require targeted disk reads when relevant. No mathematical content is summarized or silently truncated. Read necessary lemma proofs, omitted source evidence and changed passages normally; expand output whenever a hypothesis or load-bearing proof requires it. Use the supervisor's JSON inspector for labeled bounded previews and exact selected values rather than loading whole certificates. Previews never establish correctness. Model/effort choices and proof standards remain unchanged.
