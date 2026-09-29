# Canonical SAT witnesses in two-round KPT strategies: source assessment

TARGET: Review whether canonical satisfying assignments computed by a hypothetical polynomial-time SAT decider can remove the earlier-assignment dependence of a two-round KPT solver-or-antichecker strategy in Pich–Santhanam §3 without assuming an EF/PV proof of the decider's soundness.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched original KPT witnessing, canonical SAT witnesses, EF substitution and round elimination; read the original theorem and relevant primary treatments listed below. No full matching canonical-elimination theorem was located in this bounded search.
SOURCE_EVIDENCE: https://www.karlin.mff.cuni.cz/~krajicek/kpt.pdf, Theorem A and first proof, p. 145; https://arxiv.org/pdf/2312.08163v1, §2.2, pp. 11–12, and Theorem 7 with subsequent discussion, pp. 19–20; https://www.dcs.warwick.ac.uk/~igorcarb/documents/papers/CKKO21.pdf, Theorems 2.15–2.16 and 5.1 with the latter proof, printed pp. 18–19 and 46–48; https://arxiv.org/pdf/2602.19934v1, Definition 1.2 and Theorems 1.4, 1.6–1.7, pp. 6–8. The earlier Pudlák/Jeřábek substitution assessment is reused.
COMPARISON: KPT supplies a provable adaptive disjunction with a proof-dependent constant number of rounds, not necessarily two; known circuit substitution supplies polynomial syntactic overhead, not correctness of a canonical SAT selector. The inspected round-elimination theorem retains formal counterexample-existence assumptions and does not supply the requested EF conclusion from external SAT∈P.
GAP: For a supplied two-round strategy, determine whether canonical substitution preserves enough of the universal solver-or-antichecker guarantee for the EF transfer without importing a universal correctness proof for the selector; retain PV1-provable existential existence and an EF lower bound as separate missing inputs.
REASON: The essential original source is now read and the syntactic part is covered. Retain the exact target for one bounded proof-obligation test; abandon the direct canonical repair if recovering the needed universal guarantee merely assumes the missing formal SAT-search correctness. No impossibility or novelty claim follows from the unmatched search.

## Scope and discriminating test

The exact saved target above is unchanged. This completes its source review only: no substitution, new derivation, lemma or mathematical script is produced. The main gap is still an algorithm for SAT in P or an unconditional exclusion of all such algorithms. The proposed intermediate target isolates the earlier-assignment dependence in a conditional proof-complexity transfer; a successful repair could broaden the transfer's applicability without itself supplying the existential arithmetic premise or an EF/ER lower bound.

The required bound is a single polynomial EF proof-length bound as n varies, for the fixed strategy and hypothetical decider, sufficient to retain the transfer's universally quantified solver guarantee. The polynomial evaluation time of a selector and the polynomial cost of substituting it into a supplied proof do **not**, as source statements, supply that additional guarantee. No such EF bound is achieved in this review. Even a successful two-round argument would leave general constant-round applicability unresolved; Theorem 7 also gives only a fixed circuit exponent per k.

The source-level test was whether a theorem already covers the exact hypotheses, or instead identifies a residual obligation that can be tested without postulating the desired soundness proof. The outcome is the latter. The [source note](../../foundations/10-kpt-witness-substitution.md) records the imported results in Hypotheses / Conclusion / Proof / Mathlib format. A later bounded test must keep every other counterexample component, including assignment-certification data, and identify exactly what universal variables remain after the proposed substitution. Stop the direct repair if it only succeeds by assuming the canonical selector's unproved universal SAT-search correctness. A concrete-witness argument that avoids this condition would need its own justification; none is supplied here.

## Search and material actually read

Queries on 2026-09-27 included:

- `Krajicek Pudlak Takeuti bounded arithmetic polynomial hierarchy witnessing theorem 1991 pdf KPT`
- `"Bounded arithmetic and the polynomial hierarchy" pdf Krajicek Pudlak Takeuti 143`
- `"canonical" "witness" "Pich" "Santhanam" Frege`
- `"KPT" "P=NP" witnessing SAT`
- `"canonical" "KPT" witnessing`
- `"SAT" "KPT" "soundness"`
- `"canonical" "satisfying assignment" "bounded arithmetic"`
- `"lexicographically" "witnessing" "PV"`
- `"KPT" "canonical" "SAT"`
- `"KPT" "P=NP" "Frege"`
- `"canonical witnesses" "bounded arithmetic"`

Search snippets and secondary catalogues were used for discovery, not as theorem evidence. The term “canonical” produced unrelated hits as well as relevant leads; their absence of a match is not a novelty test.

| Primary source/version | Inspected material and exact role |
| --- | --- |
| Krajíček–Pudlák–Takeuti, APAL 52 (1991), 143–153; author-hosted 11-page scan, revised 25 January 1990 | §1 setup, pp. 144–145; Theorem A and its first, Herbrand-based proof, p. 145; following proof discussion, p. 146. Resolved the previously essential unread source. The scan's ∃Πᵇᵢ notation is broader than the quantifier-free case used here. Clean later statements corroborate the dependence and PV1 case. |
| Pich–Santhanam, arXiv:2312.08163v1, submitted 13 December 2023, 29 pages | Re-read §2.2, pp. 11–12, and all of §3, pp. 19–20: formal Theorem 7, proof, displayed adaptive witnesses and their assignment dependence. The source states an obstacle to its direct proof, not a universal impossibility theorem. |
| Carmosino–Kabanets–Kolokolova–Oliveira, *LEARN-Uniform Circuit Lower Bounds and Provability in Bounded Arithmetic*, author manuscript dated 7 July 2021, 65 PDF pages | Theorems 2.15–2.16, printed pp. 18–19; equations (3)–(4), Theorem 5.1 and proof with the dreambreaker discussion, printed pp. 46–48 (PDF pages 48–50). Checks a genuine round-elimination argument and its formal hypotheses. The Search-SAT-EQ description immediately before Definition 4.11, printed p. 45, was also read. |
| Ježil–Tsintsilidas, arXiv:2602.19934v1, 23 February 2026, 38 pages | Definition 1.2, Theorems 1.4, 1.6–1.7 and their surrounding explanations, pp. 6–8. Their general KPT statement corroborates the original. The conditional adaptivity separation's hypotheses and unbounded-round scope do not match this two-round test under SAT∈P; its full proof was not needed or imported. |

Direct links and precise statements are in the source note. The [2026-09-26 reflection assessment](2026-09-26-current-target.md) remains sufficient for Pudlák, arXiv:2007.14835v1, Lemma 2.1, and Jeřábek's 25 November 2003 manuscript, Lemmas 2.4–2.5. It is reused rather than redoing that search. These results justify substitution and proof representation, not arbitrary semantic identifications.

The [official Cook problem statement](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf), §1, pp. 1–2, was reconfirmed: the target is uniform deterministic versus nondeterministic polynomial-time decision. The original KPT paper was accessible through web extraction from both author-hosted copies; a local download failed DNS resolution, which did not block reading the source.

Unread leads include the *Meta-Mathematics of Computational Complexity Theory* search hit, the Buss 1997 *Theoria* article (its author-page retrieval failed), and the general book treatments cited by the inspected papers. None is used as a premise. The original KPT theorem and all essential statements for this bounded comparison were accessible and read. No claim is made to have surveyed every later result or read the entire 65-page CKKO manuscript.

## Applicability and redundancy

1. **A term versus its correctness.** PV1's language includes clocked polynomial-time algorithms. This permits naming a proposed canonical selector under the hypothetical algorithmic assumption. It does not make its intended universal SAT-search specification an axiom. The source note records that specification as a potential missing condition, not as a theorem or an unavoidable premise of every possible transfer.
2. **Substitution versus recovery of the conclusion.** The generic proof-substitution operation is covered and should not be reproved. The unanswered part is whether the resulting two-round argument still yields the universal conclusion needed by the EF transfer. A theorem merely giving efficient search or a substituted disjunction is not a full match.
3. **All prior counterexample data.** The source's later function depends on the earlier formula, satisfying assignment, comparison circuit and assignment-certification data. Replacing just one component does not, by any cited result, erase the others. Keep the pairing relation D and the solver alternative in view; do not discard them to simplify the proposed application.
4. **Round count.** KPT provides some constant c depending on a proof. The two-round case is a deliberately bounded conditional test. Its success would not establish c=2 for the unproved existential statement or a reduction of arbitrary c to two.
5. **Known elimination and known obstructions.** CKKO Theorem 5.1 uses formal counterexample-existence assumptions and permits polynomially changing lengths. It is not a proof of this canonical substitution claim. The 2026 adaptivity theorem assumes a separation rather than SAT∈P and concerns unbounded rounds; using it to stop this repair would exceed its statement.

The [direct-minmax failure](../../ATTEMPTS/012-direct-minmax-to-antichecker-generator.md) already settled existence versus a uniform certified generator. The [dreambreaker failure](../../ATTEMPTS/011-direct-dreambreaker-to-ef-transfer.md) already settled the cited finder's length/description mismatch. Neither is new negative evidence here, and neither is reopened. The new work is resolving the original KPT source gap and distinguishing the covered syntactic operation from the untested proof obligation. L013's supplied-proof overhead still leaves the soundness-proof length missing; L012's parity family still has polynomial ER refutations.

## Decision and limits

**EXPLORE.** No full theorem was found, but this is not a source-access block or a proof that the repair fails. The exact two-round target is retained for a bounded informal applicability test in a later invocation. That test must either justify recovery of the required universal conclusion with the stated resources, identify a strictly narrower sufficient proof obligation, or stop the direct canonical repair on a concrete residual obstruction. Merely repeating that external correctness differs from provability would be STALLED.

This is LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. All mathematical statements supplied are named imports; there is no reproduced proof or result claimed beyond the checked literature. Exploration turns used becomes **1**, with no reset from the source search. The unchanged target has this completed assessment before any later research invocation. PROGRESS.md remains the sole current checkpoint; no second next-action record is created.

## Mathlib

Coverage: **not checked** for the proposed canonical substitution, KPT witnessing, or the supporting arithmetic and CF/EF results. Named theorems and direct links are retained in the source note; supporting results are not represented as a full match.
