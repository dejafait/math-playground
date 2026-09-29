# Conditional two-round transfer from supplied output covers

TARGET: Test whether supplied polynomial lists of complete second-round outputs and polynomial EF proofs of their coverage on first-round solver counterexamples yield EF polynomial boundedness from a supplied two-round KPT strategy and SAT∈P, without canonical-selector soundness proofs.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: The exact complete-output cover and its conditional EF use were screened in drafts/literature/2026-09-27-kpt-polynomial-output-cover.md this literature turn; reuse its recorded KPT, finite-list, parallelism and antichecker searches.
SOURCE_EVIDENCE: Cook–Thapen, https://arxiv.org/pdf/cs/0409015v1, Theorem 7, pp. 15–16; Ježil–Tsintsilidas, https://arxiv.org/pdf/2602.19934v1, Definition 1.2 and Theorem 4.11, pp. 6–7 and 24; Pich–Santhanam, https://arxiv.org/pdf/2312.08163v1, §3, pp. 19–20, and https://eccc.weizmann.ac.il/report/2023/199/download/, §4, pp. 25–26; prior Pudlák/Jeřábek substitution assessment reused. Statements and relevant proofs were inspected as specified in the linked review.
COMPARISON: Standard adaptive/parallel witnessing and polynomial proof substitution cover the background operations. They do not provide the proposed complete-output lists, their EF coverage proofs, or the precise conditional two-round transfer; the closest published transfer assumes a provable generator.
GAP: Determine whether the explicitly supplied covers and proofs suffice with one polynomial bound on total EF proof length, preserving all certification and second-round universal variables; do not infer existence of these premises from KPT or SAT∈P.
REASON: This is the concrete conditional applicability test selected by the completed source comparison, not an unscreened new mechanism. Import the supporting results and test only the remaining inference; the search does not certify originality.

## Assumptions and success threshold screened

Use the full scope and proposed coverage implication in the [completed review](2026-09-27-kpt-polynomial-output-cover.md). Fix a strategy with two rounds and polynomial EF proofs of its universal disjunction. Choose the comparison exponent k large enough for the hypothetical SAT algorithm's circuits, and assume the supplied strategy is available at that k; a strategy for one arbitrary prescribed k does not suffice by itself. Retain polynomial proofs identifying the assignment verifier with a fixed CNF, using the checked evaluator of L013 or an explicitly justified alternative.

For each length and fixed first formula F, allow a supplied list of complete output tuples and a supplied coverage proof with a single polynomial bound, uniform over F. The tuples may depend on F and on the fixed earlier comparison/certification data, but not on the first free assignment or the second-round universal challenges. Count the full binary list and proof, not just the number of solver circuits. Keep all format and pairing conditions; extra listed tuples need not be silently treated as valid outputs. Nonuniform existence of these supplied data is distinct from efficient generation.

The question is whether these premises yield polynomial EF proofs of all tautologies. A later proof must charge the total case-split overhead and every concrete evaluation, preserve the formula-conclusion requirement for CF-to-EF conversion, and use the actual verifier identification. No proof of SAT-selector correctness or of unsatisfiability may be inserted without a justified bound. The unsatisfiable-F case, where the coverage implication can be vacuous semantically, is a required check rather than a granted proof.

Continue if the inference works without an additional unproved proof-length premise. Otherwise isolate the missing premise or bound and stop this direct cover transfer. Even success leaves cover existence/proofs, the existential arithmetic premise, general-round applicability, and a superpolynomial EF lower bound open. No canonical-recovery reproof or general witnessing compiler is authorized by this assessment.

This ready assessment was saved during a literature-only turn. No part of the proposed transfer is proved here. The [source note](../../foundations/11-kpt-output-covers.md) distinguishes the imported components and full-statement gap; no essential selected source remains unread. Novelty of a future result is not certified by this bounded search.

## Mathlib

Coverage: **not checked** for the conditional transfer or its supporting witnessing and proof-substitution statements. Direct primary-source links and theorem numbers are retained above; no full match or absence is asserted.
