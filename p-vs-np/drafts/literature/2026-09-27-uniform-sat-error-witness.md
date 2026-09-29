# Uniform SAT error witnesses: completed source comparison

TARGET: Review whether Bogdanov–Talwar–Wan's uniform SAT counterexample finder meets the prescribed input length and S^1_2 provability conditions in Pich–Santhanam's arXiv:2312.08163v1 Corollary 2 with zero advice.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched the original title, exact-length witnessing, dreambreakers, bounded arithmetic and provability; followed author-hosted primary versions and compared the statements and proof portions listed below. No strengthening meeting the full zero-advice hypothesis was located.
SOURCE_EVIDENCE: https://andrejb.net/pubs/quasicrypto-ics.pdf, 10 November 2009, Theorem 1, p. 3, and Lemma 1, procedure D and proof, pp. 7–9; https://www.cs.columbia.edu/~atw12/papers/quasicrypto-ics-submit.pdf, Theorem 1, p. 2, and final procedure/proof, pp. 6–7; https://arxiv.org/pdf/2312.08163v1, w definition and Corollary 2, pp. 3–5; https://eccc.weizmann.ac.il/report/2023/199/download, p. 7. These statements and indicated arguments were read.
COMPARISON: The original deterministic finder does return length n on successful input 1^n, but guarantees success only infinitely often for each fixed algorithm under P≠NP. Corollary 2 needs a pointwise conditional witness at every sufficiently large length for every allowed description, with S^1_2 provability for ordinary EF. This direct import fails.
GAP: No all-large-length conditional witness, common threshold over the allowed descriptions, or S^1_2 proof of W_(n0)^(k,0)(f) is supplied; no impossibility or unprovability of such a strengthening is established either.
REASON: Complete the comparison and stop the direct dreambreaker-to-EF import. Preserve the unresolved uniform transfer and evaluate a different source of certification; do not reprove the known finder or turn its infinitely-often conclusion into the required bound.

## Gap, target and discriminating test

The exact saved target above is preserved. The main gap is still a polynomial-time SAT algorithm or an unconditional exclusion of all such algorithms. This comparison tests a possible source of the witnessing premise in a conditional EF transfer. Keep the arXiv version's Corollary 2, zero advice, fixed clock exponent k, description bound log n, and all sufficiently large input lengths. In particular, the proposed f receives the represented algorithm, not an already supplied error and its satisfying assignment.

The continuation test was an inspected theorem supplying the pointwise conditional behaviour in w_n^(k,0)(f), and the stated S^1_2 proof if ordinary EF is used. A procedure that only succeeds infinitely often, depends on a pre-assumed separation, or has only external correctness cannot be imported as satisfying that whole premise. The test fails for the original finder theorem. This is a statement comparison, not a proof that no modification could work.

A successful match would supply a relevant transfer input, while a superpolynomial EF/ER lower bound would remain missing. The saved PV-sound-decider existence question also remains unresolved; Corollary 2 is a different sufficient mechanism, not a proved equivalence to that question. Neither the witness nor any new proof-length bound is obtained here. L013's polynomial cost in the length of a supplied soundness refutation still does not bound that refutation's length.

## Discovery and inspected versions

Queries on 2026-09-27 included:

- `Bogdanov Talwar Wan Hard instances for satisfiability and quasi-one-way functions pdf`
- `"2312.08163" "Bogdanov" "Corollary 2"`
- `"SAT" "counterexample" "Bogdanov" "length"`
- `"Bogdanov" "Talwar" "Wan" "bounded arithmetic"`
- `"Bogdanov" "Talwar" "Wan" "provable"`
- `"SAT" "witnessing" "uniform" "Pich" "length"`
- `"Hard instances for satisfiability" "length" "infinitely"`
- `"dreambreaker" SAT witnessing`
- `"Gutfreund" "Shaltiel" "Ta-Shma" "bounded arithmetic"`
- `"witnessing" "S^1_2" "SAT"`

The original paper was located through the authors' publication pages, then read at the direct author-hosted URLs in SOURCE_EVIDENCE. The 18-page manuscript is dated 10 November 2009; the corresponding ICS 2010 publication is not dated by the search engine's crawl timestamp. The undated 11-page author submission was used only to cross-check the theorem and final procedure. The arXiv version has 29 pages; the dated ECCC presentation has 35 and different numbering. The [source note](../../foundations/08-uniform-sat-error-witnesses.md) retains precise named statements in the notebook's standard format.

Read from the longer original: §2.1 and Theorem 1, p. 3; the method description, p. 6; §3.1–3.2 and Lemma 1, pp. 7–9; final D and proof of Theorem 1, p. 9. Section 3.3's aggregation argument was also inspected: it invokes infinitely-often success for fixed machines and supplies no proof of the required W statement. The randomized theorem and quasi-one-way-function results are unnecessary for this deterministic comparison.

Read from the transfer paper: w_n^k(f) and its explanation, p. 3; the zero-advice specialization's underlying universal simulation and description restriction, p. 4; Corollary 2, the definition of W and the subsequent qualification, p. 5. Rechecked the ECCC length warning on p. 7. The original theorem refines that warning: the final D filters its output to length n; the missing guarantee is success at each prescribed erroneous length, not the complete absence of length control.

Additional discovery leads are **not theorem inputs**: Pich's [*Learning algorithms from circuit lower bounds*, November 2020](https://users.ox.ac.uk/~coml0742/papers/satclbt.pdf) was opened for its title, abstract and comparison discussion, but its interactive witnessing theorem was not assessed. The Gutfreund–Shaltiel–Ta-Shma and Atserias primary papers were not read in this turn. No formalization or black-box impossibility result is inferred from these leads. They are not essential to comparing the two explicit statements already inspected. No essential source for the completed comparison remains unread.

The [Clay statement](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf), §1, pp. 1–2, was reconfirmed alongside the [problem page](https://www.claymath.org/millennium/p-vs-np/). The target remains ordinary uniform deterministic versus nondeterministic polynomial time; the site's unsolved label is not a mathematical input.

## Required guarantee versus the available theorem

| Condition | Original finder | Corollary 2 with zero advice |
| --- | --- | --- |
| Output and search model | Canonical search failure comes with a satisfying assignment; final D outputs an n-bit formula when successful. | An n-bit satisfiable formula and assignment must expose failure of the clocked search algorithm at that same length. |
| Length quantifier | Infinitely many successful n for each fixed A. The intermediate Lemma 1 ranges over n^(1/r)<N≤n under an extra premise. | One threshold n0 and success whenever an error exists, for every n>n0 and every description of length ≤log n. |
| Hypothesis | Deterministic Theorem 1 assumes P≠NP. | The w formula has a correctness-or-witness disjunction at the individual length; it is not given an unproved separation as an axiom. |
| Feasibility | Polynomial-time procedure with A and its running-time bound as inputs; intermediate encoding degrees depend on A. | A fixed polynomial-time f for each fixed k; the target clock and description restriction are explicit. No running-time impossibility is inferred just from these different presentations. |
| Formal proof | No S^1_2 proof of the needed W statement occurs in the inspected theorem or proof. | Item 2 requires that proof. Item 1 instead changes the proof system by adding witnessing axioms. |

These are applicability differences, not new lower bounds. Merely setting advice to zero leaves the simultaneous description and length quantifiers in place. A fixed-exponent conclusion n^Ω(k), even with its hypotheses proved, must not be reported as excluding every polynomial exponent. The transfer's formal-provability premise and a suitable EF/ER lower bound remain independent obligations.

## Redundancy and continuation decision

The previous assessment had only a later paper's warning and an unread original. Reading Theorem 1 and its exact-length filter now closes the direct-import test and corrects an overbroad interpretation of that warning. This is new source evidence for a specific stop decision, not a repetition of the generic missing-soundness observation. The known algorithm and transfer are imported as qualified inputs; no result beyond those sources is claimed.

Do not reproduce the finder or use its P≠NP premise to prove P≠NP. Do not assume that padding preserves an arbitrary algorithm's error: L003 and L009 already show why paying for another input length needs a separate argument. The [automatic-transfer failure](../../ATTEMPTS/010-automatic-decider-to-er-simulation.md), L012's easy ER parity family and the missing bound after L013 remain unchanged. The [direct-import stop record](../../ATTEMPTS/011-direct-dreambreaker-to-ef-transfer.md) preserves this more specific failure.

**EXPLORE** records that no full matching witness theorem was found; it does not recommend deriving the missing strengthening from the cited theorem. The direct import is stopped. The alternative identified in the same transfer paper is feasible antichecker generation, using a finite set of test inputs rather than this one-candidate finder. Its informal Theorem 3 and reference to Lipton–Young were read only to select a separate target; the original minmax theorem and formal Theorem 7 have not been assessed. The [new REVIEW_REQUIRED assessment](2026-09-27-feasible-antichecker-generator.md) preserves that separate question, including the solver-or-antichecker alternative and stronger circuit scope. No work on that construction is done here.

The completed step is LITERATURE / NEGATIVE / NOVELTY_UNCHECKED: a newly inspected mismatch changes the route, without claiming a new theorem or novelty of a possible repair. Consecutive exploration turns return from 1 to 0 because of this informative negative; no launcher or research-stop state is changed.

## Mathlib

Coverage: **not checked** for the full comparison or supporting witness results. Corollary 2 is a conditional downstream input; Theorem 1 is a weaker known finder guarantee. Neither is identified as a full match for the missing strengthened witness.
