# Mixed seventh-power conditional reducible-character audit assessment

TARGET: Critically audit Chocian's Section 6.2 reducible-character reduction to traces ±2 at q=(29,sqrt(5)-11), conditional on its stated determinant, finite-flatness and conductor hypotheses.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact conditional-family searches and primary-reference follow-up in 2026-10-04-mixed-seventh-trace-family-coverage.md. This component was inspected as part of the saved review; no archive or original-descent source is needed for the conditional character question.
SOURCE_EVIDENCE: Chocian arXiv:2609.26996v1 Section 6.2, equations (36)–(37) and the q=29 character paragraph, https://arxiv.org/html/2609.26996v1 ; Raynaud Theorem 3.4.3 and Corollary 3.4.4, printed p. 270, https://www.numdam.org/article/BSMF_1974__102__241_0.pdf ; Milne CFT v4.03 Chapter V Theorems 1.7, 3.5 and 5.3 and Proposition 5.2, https://www.jmilne.org/math/CourseNotes/CFT.pdf ; PVT arXiv:2512.17845v1 Theorem 2.1(3)–(4) and the ray-group statement in the proof of Corollary 7.7, https://arxiv.org/html/2512.17845v1 . These statements were actually read.
COMPARISON: The closest source claims exactly this conditional restriction. Raynaud and global reciprocity provide the general inputs, not the full field-specific conclusion by themselves. Independent reproduction is justified as a bounded correctness check of an unverified candidate's essential character branch; no novelty is sought.
GAP: Check the passage from finite-flat scalar inertia to the level-two digit list, the exclusion of mixed digits by a global unit, the consequent conductor restriction and the Frobenius class at the specified prime. Keep every assumption conditional rather than asserting that all original solutions meet it.
REASON: This is an independently testable component of the saved exhaustion target, with adequate read source coverage. It can establish or refute the proposed reducible-sector trace restriction without the blocked modular archive, four-parameter reduction or original descent.
SCOPE: One conditional proof audit over F=Q(sqrt(5)) for a continuous reducible two-dimensional residual representation over an algebraic closure of F_7, determinant chi_7, finite flat at the prime over 7, unramified outside 3,5,7, and Artin-conductor exponents at most 3 at primes above 3 and 5. Preserve the weight-two normalization. Use REPRODUCTION classification; no full candidate exclusion or irreducible-sector coverage is approved.
COVERED_TARGET: Critically audit Chocian's Section 6.2 reducible-character reduction to traces ±2 at q=(29,sqrt(5)-11), conditional on its stated determinant, finite-flatness and conductor hypotheses.

## Relevance and discriminating test

The main gap is uniform residual-signature emptiness. The proposed intermediate result would cover every reducible representation under the stated hypotheses by the two linear factors T-2 and T-5 used in L016. That could close the character portion of the conditional comparison family; it would leave all irreducible packets, the original representation applicability, the four curve parameters and the pure-field/global argument unresolved.

The pass criterion is a complete conditional argument preserving both possible real-place signs and all locally allowed finite-flat inertia characters. It must justify the global restriction, not assume it or use p>13 irreducibility at p=7. A missing inertia type, unsupported conductor step or additional Frobenius trace would stop reliance on this branch and identify the exact failed interface. Merely recomputing L016's resultants does not meet the test.

The notebook has not proved this conditional statement. The prior unrestricted congruence and repeated-cube failures do not duplicate it: this concerns a globally defined character with conductor and finite-flat hypotheses, not arbitrary independently chosen local points.

## Read inputs and claims to audit, not new results

The precise closest claim is [Chocian, arXiv:2609.26996v1, Section 6.2](https://arxiv.org/html/2609.26996v1#S6.SS2). The source writes the reducible semisimplification as psi plus psi^(-1)chi_7. It first bounds the character conductor at 3 and 5, then uses a unit to rule out the two mixed finite-flat digit types at the inert prime over 7. After a possible interchange of the two characters, it claims that psi has conductor dividing 3(sqrt(5)). Both real places remain in the ray modulus.

The source specifies epsilon=(1+sqrt(5))/2, the unit epsilon^8=13+21epsilon, and the totally positive generator 6-epsilon of the specified prime over 29. Its congruences, local reciprocity evaluation, claimed order-two ray class and consequent traces ±2 are inputs to be checked, not established notebook results. A proof of the required Frobenius order bound may suffice without reproducing a whole ray-class implementation, but must explain why it covers every eligible character.

[Raynaud, *Schémas en groupes de type (p,...,p)*](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf#page=31), Bull. Soc. Math. France 102 (1974), Theorem 3.4.3 and Corollary 3.4.4, printed p. 270, is imported only for the general finite-flat fundamental-character digit restriction. Its strictly henselian base and absolute ramification index must be handled explicitly when applying it over the completion of F. Frobenius invariance of a scalar local character must justify the claimed level bound; no two-element inertia list is assumed at the outset.

[Milne, *Class Field Theory*, v4.03, 6 August 2020](https://www.jmilne.org/math/CourseNotes/CFT.pdf), Chapter V, supplies the standard ray-class exact sequence (Theorem 1.7, p. 150), ideal reciprocity (Theorem 3.5, p. 158), local-global compatibility (Proposition 5.2, p. 178), and the product formula on principal ideles (Theorem 5.3, pp. 178–179). These general theorems may be cited rather than reproved. A local reciprocity convention change must not change the trace conclusion.

[PVT, arXiv:2512.17845v1](https://arxiv.org/html/2512.17845v1), Theorem 2.1(3)–(4), gives supporting residual ramification and finiteness inputs in its own Diophantine scope. The proof of Corollary 7.7 states the narrow ray group C_4 x C_2 for the indicated modulus; that statement is supporting coverage, whereas Corollary 7.7's large-exponent irreducibility conclusion is not used. The general conditional audit assumes the local hypotheses explicitly and does not claim to reconstruct the original solution-to-representation bridge.

No essential source for this narrowly conditional audit is unread. The V4 modular matrices and original Dahmen–Siksek local descent are unnecessary for its statement. They remain parked and cannot be inferred from a successful character audit. No mathematical calculation or new proof was carried out while screening this target.

## Mathlib

Coverage of the exact conditional trace restriction and supporting finite-flat, class-field and conductor results: **not checked**. The named primary inputs are precise citations, not matching Mathlib declarations or formal verification. A successful audit would be a reproduction of the source claim, not evidence of a new signature exclusion.
