# Cubic tied-modulus test — source-scope nomination

TARGET: Test whether P(z)=1+z+z^2+z^3 satisfies D_(r,k)>=0 for all integers r>=1 and k>=1 while having a nonreal zero.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed all-fixed-shifts source comparison in 2026-11-06-all-fixed-shifts-zero-detection-scope.md; exact polynomial strings and solid/contiguous-minor claims were searched locally, and nonnegative contiguous-minor counterexamples were searched externally. No matching cubic certificate was established; no novelty claim.
SOURCE_EVIDENCE: Alexandersson, EJC19(4) (2012), P22, arXiv:1208.5607v1 Theorem6 p.5 and Section3.2 pp.11–12, https://arxiv.org/html/1208.5607v1, reread with its elementary-coefficient normalization and complete formula proof. Fomin–Zelevinsky math/9912128v1 Lemma7/Theorem9 p.5 was inspected only to rule out an unsupported weak-sign import.
COMPARISON: The finite distinct-root formula is exact for complex elementary variables, allowing tied moduli and rational phases; it supplies the method but not this polynomial's signs. No infinite-product limit, repeated-root formula, oscillation theorem or actual-Xi sign estimate is needed for this one test.
GAP: Verify the proposed {1,i,-i} coefficient match, evaluate the complete formulas for shifts1/2 at every rank, and handle shifts3 and k>3 directly from the zero-extended coefficient matrix. Retain zero residue classes. No calculation or sign conclusion has yet been made.
REASON: A finite product is within the original universal class; a certified example would independently refute that exact weak-sign detector despite the inaccessible infinite asymptotics source. This is a bounded known-method specialization. The newly written assessment receives separate source-scope approval next turn before mathematics.
SCOPE: Only the displayed cubic, ordinary coefficients a_0=a_1=a_2=a_3=1 and a_n=0 otherwise, D_(r,k)=det[a_(k+j-i)]_(0<=i,j<r), all r>=1 and k>=1; no PF-infinity, strict-positivity, higher-finite-PF, infinite-degree or Xi realization assertion.

The main gap is still L030–L032/C032a actual-Xi all-degree mixed
positivity. This test concerns whether separate eventually nonnegative
rays could even serve as an abstract detector. It neither establishes
nor assumes those signs for Xi. L837/L838 are contrasts, not mathematical
premises; the normalizations in L832/L776 fix the contextual notation.
No cross-notebook result is needed.

Use Alexandersson's Theorem6 by citation, without reproof. For its source
notation, deleting the first c columns and taking a leading r-square
produces a_(c+j-i); source c is our shift, source k our rank. The
specialization must verify s_0=1 and distinct variables. Equal moduli
do not violate distinctness. Check every term, possible cancellation
and all ranks rather than invoking Theorem4's misprinted general tuple
conditions or sampling. Shifts at/above degree require direct matrix
checks; no extension of the stated subset formula is assumed.

Continue only with a full symbolic rank description and exhaustive
shift cases together with a checked nonreal zero. If any ray has
negative terms arbitrarily far out, this ansatz fails the original
eventual premise; preserve that failure and do not claim a counterexample.
If only finite-rank failures occur, distinguish the weaker eventual
question from the stronger all-rank test in TARGET. A successful test
would refute only the proposed abstract implication. Multiplicities,
infinite products and stricter or actual-Xi hypotheses would not have
been positively characterized. Keep RH IN_PROGRESS in either case.

Full matching Mathlib coverage is unchecked. The source comparison
supports REPRODUCTION, not a creative or potentially-new classification.
No mathematical derivation, script or lemma accompanies this nomination.
