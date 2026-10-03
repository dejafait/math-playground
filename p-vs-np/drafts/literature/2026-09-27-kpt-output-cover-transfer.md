# Conditional two-round transfer from supplied output covers

TARGET: Test whether supplied polynomial lists of complete second-round outputs and polynomial EF proofs of their coverage on first-round solver counterexamples yield EF polynomial boundedness from a supplied two-round KPT strategy and SAT∈P, without canonical-selector soundness proofs.
CHECKED: 2026-10-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Dedicated 2026-10-03 searches for finite-range KPT-to-EF transfer, antichecker coverage and two-round witnessing, followed by inspection of the closest transfer proof and a related interactive-protocol theorem; queries and reading scope are recorded below. Reuse the earlier parallel-witnessing and substitution assessments.
SOURCE_EVIDENCE: Pich–Santhanam, https://arxiv.org/pdf/2312.08163v1, Theorem 7, proof and following KPT discussion, pp. 19–20, read for this exact target; author-hosted https://users.ox.ac.uk/~coml0742/papers/eopt.pdf, same section and numbering, also inspected. Arteche–Khaniki–Pich–Santhanam, https://drops.dagstuhl.de/storage/00lipics/lipics-vol297-icalp2024/LIPIcs.ICALP.2024.12/LIPIcs.ICALP.2024.12.pdf, Definition 17, Lemma 18, Theorem 19 and Corollary 20, pp. 12:16–12:17, inspected for scope. Previously read Cook–Thapen, Ježil–Tsintsilidas and Pudlák/Jeřábek inputs are reused by the citations below.
COMPARISON: Adaptive/parallel witnessing and circuit substitution supply supporting operations; Pich–Santhanam retains a provable generator and certification data. The related interactive theorem uses implicit EF, hardness axioms and counting-circuit assumptions. None is a full match for this conditional ordinary-EF transfer from supplied complete-output covers.
GAP: Determine whether the explicitly supplied covers and proofs suffice with one polynomial bound on total EF proof length, preserving all certification and second-round universal variables; do not infer existence of these premises from KPT or SAT∈P.
REASON: Complete the saved conditional target's own theorem-level review as required by recovery, retaining its exact text and EXPLORE decision. The remaining applicability inference needs a later mathematical attempt; no transfer, new bound or originality claim is made in this literature turn.
SCOPE: A supplied two-round solver-or-antichecker strategy at a comparison exponent compatible with the hypothetical SAT algorithm; supplied polynomial EF strategy and evaluator-identification proofs; complete output lists and coverage proofs with one polynomial total binary-length bound, independent of both the first free assignment and the second-round universal challenges.

## Assumptions and success threshold screened

Use the full scope and proposed coverage implication in the [completed review](2026-09-27-kpt-polynomial-output-cover.md). Fix a strategy with two rounds and polynomial EF proofs of its universal disjunction. Choose the comparison exponent k large enough for the hypothetical SAT algorithm's circuits, and assume the supplied strategy is available at that k; a strategy for one arbitrary prescribed k does not suffice by itself. Retain polynomial proofs identifying the assignment verifier with a fixed CNF, using the checked evaluator of L013 or an explicitly justified alternative.

For each length and fixed first formula F, allow a supplied list of complete output tuples and a supplied coverage proof with a single polynomial bound, uniform over F. The tuples may depend on F and on the fixed earlier comparison/certification data, but not on the first free assignment or the second-round universal challenges. Count the full binary list and proof, not just the number of solver circuits. Keep all format and pairing conditions; extra listed tuples need not be silently treated as valid outputs. Nonuniform existence of these supplied data is distinct from efficient generation.

The question is whether these premises yield polynomial EF proofs of all tautologies. A later proof must charge the total case-split overhead and every concrete evaluation, preserve the formula-conclusion requirement for CF-to-EF conversion, and use the actual verifier identification. No proof of SAT-selector correctness or of unsatisfiability may be inserted without a justified bound. The unsatisfiable-F case, where the coverage implication can be vacuous semantically, is a required check rather than a granted proof.

Continue if the inference works without an additional unproved proof-length premise. Otherwise isolate the missing premise or bound and stop this direct cover transfer. Even success leaves cover existence/proofs, the existential arithmetic premise, general-round applicability, and a superpolynomial EF lower bound open. No canonical-recovery reproof or general witnessing compiler is authorized by this assessment.

This ready assessment was saved during a literature-only turn. No part of the proposed transfer is proved here. The [source note](../../foundations/11-kpt-output-covers.md) distinguishes the imported components and full-statement gap; no essential selected source remains unread. Novelty of a future result is not certified by this bounded search.

## Dedicated target review, 2026-10-03

The 2026-09-27 assessment inherited its search evidence from the preceding cover-discovery review. The supervisor now requires a separate review of this saved sufficiency target. Its TARGET is preserved verbatim. This addition supplies that review and retains the original assumptions and continuation test; it does not execute the test. The complete-output mechanism already differs from the stopped canonical recovery in ATTEMPTS/013, so that failure is neither renamed nor reopened.

The concrete source need was the scope of the published transfer proof when its one generated output is replaced by separately supplied, nonuniform complete-output cases. The newly found interactive-protocol paper was checked as a possible stronger match. The [dedicated source note](../2026-10-03-kpt-cover-transfer-source-notes.md) retains precise citations in Hypotheses / Conclusion / Proof / Mathlib format.

Search queries on 2026-10-03 were:

- `"KPT" "finite range" "Frege"`
- `"KPT" "output" "cover" "witnessing"`
- `"Towards P≠NP from Extended Frege lower bounds" existential anticheckers`
- `"extended Frege" "anticheckers" "finite"`
- `"From proof complexity to circuit complexity via interactive protocols"`
- `"KPT witnessing" "polynomial" "case" proof`
- `"KPT" "bounded range" witnessing`
- `"KPT" "finite-range" witnessing`
- `"antichecker" "coverage" Frege`
- `"two-round" "KPT" "Frege"`

The exact-cover queries did not locate a full statement match. Several returned unrelated meanings of KPT; these were discarded. This is a bounded search report, not an absence or novelty theorem.

| Source and material inspected or reused | Applicability to this exact target |
| --- | --- |
| Pich–Santhanam arXiv:2312.08163v1, §3, Theorem 7 with its proof and following displayed KPT strategy, pp. 19–20; the 29-page author copy has the same relevant numbering | Closest ordinary-EF transfer. Retains formal generator correctness, pairing/certification information and earlier replies; its stated conclusion does not import the proposed cover inference. |
| Arteche–Khaniki–Pich–Santhanam, ICALP 2024, article 12, Definition 17, Lemma 18 with its proof, Theorem 19 and Corollary 20 with their short proofs, pp. 12:16–12:17; introduction's Theorem 1, Corollary 2 and proof outline, pp. 12:4–12:6 | Related transfer uses a stronger proof system and different circuit premises. It is a scope comparison, not an input establishing ordinary EF boundedness from SAT∈P. |
| Cook–Thapen Theorem 7 and Ježil–Tsintsilidas Definition 1.2 / Theorem 4.11 | Reuse the sufficient [2026-09-27 primary-source assessment](2026-09-27-kpt-polynomial-output-cover.md) and [source note](../../foundations/11-kpt-output-covers.md). No new parallel-witnessing search or reproof is needed. |
| Pudlák Lemma 2.1 / Fact 1 and Jeřábek Lemmas 2.4–2.5 | Reuse the [reflection assessment](2026-09-26-current-target.md) and [source note](../../foundations/06-reflection-specialization.md). These are supporting syntactic results, with formula-conclusion conversion and evaluator identification still required. |

The [arXiv submission history](https://arxiv.org/abs/2312.08163) lists v1 dated 13 December 2023. The author copy was read as the retrieved 29-page manuscript, not assumed to be a new journal revision. The distinct ECCC layout and its Theorem 10 remain covered by the prior review; its numbering is not substituted here. Secondary search results mentioned a journal publication and range-avoidance papers. Their full texts were not inspected and are not inputs or claimed matches. The ICALP paper omits some underlying formalization proofs; only the displayed scope and the indicated arguments were inspected, and its simulation is not imported. No essential source needed for the selected conditional test is blocked.

Reconfirmed the exact uniform decision target from [Cook's official Clay statement, §1, pp. 1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf), linked by the [Clay problem page](https://www.claymath.org/millennium/p-vs-np/). A fixed-exponent circuit conclusion or a bound for a stronger proof system is not substituted for that target.

The required bound remains one polynomial in the full input length for the total complete-output data, coverage proof and resulting EF proof, uniformly over the fixed formulas under consideration. The background results supply no such cover bound. A later attempt must account for every listed tuple, including extra entries and malformed or miscertified data, and retain every second-round challenge. It must not count only solver descriptions or assume a proof of the hypothetical SAT algorithm's universal correctness. Whether the necessary finite case treatment succeeds is deliberately left unproved.

**Decision: retain EXPLORE.** The same concrete sufficiency test is ready for a later mathematical invocation. Import supporting operations by citation and investigate only this residual inference. Stop the direct transfer if it needs an additional unprovided universal proof or exceeds the polynomial total-length threshold. A successful inference would still leave cover construction and coverage-proof bounds, the existential arithmetic premise, extension beyond two rounds and a superpolynomial ordinary-EF/ER lower bound unresolved.

This completes a process/source-assessment repair, with STEP_OUTCOME STALLED: the route decision and mathematical gap are unchanged. Supporting mathematics is imported, not newly discovered; the full conditional target is still unproved and its originality unestablished. Exploration turns used remains 1; this literature turn spends no calculation turn and resets no counter. The overview and DAG need no change because the overall argument and its mathematical inputs have not changed.

## Mathlib

Coverage: **not checked** for the conditional transfer or its supporting witnessing and proof-substitution statements. Direct primary-source links and theorem numbers are retained above; no full match or absence is asserted.
