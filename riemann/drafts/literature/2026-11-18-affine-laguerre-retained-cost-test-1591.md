# Affine Laguerre coefficient and retained-cost test1591

TARGET: Test whether affine generalized-Laguerre references with degree-dependent alpha_d>-1, real m_d and nonzero real sigma_d can match the first three subleading coefficients of unchanged P_d and make the fourth/fifth retained Schmeisser cost o(d^2).
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact Laguerre/reference queries, named local stops and primary near-overlap comparison completed in drafts/literature/2026-11-18-growing-reference-source-notes-1591.md; no matching optimized residual theorem was found in this bounded scope. No originality inference.
SOURCE_EVIDENCE: DLMF v1.2.8 Table18.3.1, (18.5.12), (18.9.1)/Table18.9.1 https://dlmf.nist.gov/18.3 https://dlmf.nist.gov/18.5#E12 https://dlmf.nist.gov/18.9 ; Pan-Zeng2020 B81e p1 (1.1)-(1.4) https://www.mat.univie.ac.at/~slc/wpapers/s81panzeng.pdf ; reuse Schmeisser2002 Theorem1/Corollary1 and full relevant proof coverage in C028a/c/source-notes1503. Holland2608.08682v1 Lemma4.3 is inspected contrast, not an input.
COMPARISON: Sources supply exact finite coefficients, positive Gamma-weight orthogonality, norms and recurrence. Their affine normalization and constrained actual residual cost need checking. C028a/c's Gaussian/finite-terminal floors do not settle this bulk-changing family; Holland's large-derivative ascending-coefficient defect does not settle unchanged unshifted reciprocal matching.
GAP: Determine all admissible three-coefficient matches and the retained normalized fourth/fifth cost, including parameter sequences approaching alpha=-1, zero scale or infinity. Neither existence nor a positive floor is assumed.
REASON: One bounded known-method specialization can exclude this proposed majorant or identify a necessary test passed. Import known formulas; derive only affine conventions and the actual coefficient/cost difference. New continuation awaits separate approval next turn.
SCOPE: Each integer d>=5, same parameters alpha_d,m_d,sigma_d for every degree 0<=n<=d; actual coefficients and S_2,S_3 of C028a; no RH, root reality/simplicity, uniform parameter bound or conditioning premise.

Main gap: L030-L032/C032a all-degree positivity. C028b makes H_d=o(d)
an exact downstream criterion. A full Schmeisser upper bound I(P_d)=o(d)
would suffice, whereas the two retained costs alone cannot suffice.

For this test define the prospective monic affine basis by

    q_n(x)=sigma_d^n*(-1)^n*n!*
           L_n^(alpha_d)((x-m_d)/sigma_d),  0<=n<=d.

Use the pushforward under x=m_d+sigma_d*z of the normalized positive
Gamma weight on z>0, with alpha_d>-1. Negative sigma_d is allowed.
The test must check monicity, orthogonality, norms and norm ratios from
the cited formulas; no evaluated affine norm is asserted by this review.
For the unique expansion P_d=sum a_n q_n, define h_n=integral q_n^2 dmu_d.
The proposed equations are a_(d-1)=a_(d-2)=a_(d-3)=0 and the diagnostic is

    B_d=(h_(d-4)*a_(d-4)^2+h_(d-5)*a_(d-5)^2)/h_(d-1).

First solve/check feasibility over the entire stated real parameter
range. Infeasibility for all sufficiently large d stops this family
without calculating the remaining terms. Otherwise test whether a
uniform eventual B_d>=c*d^2, c>0, excludes all feasible sequences, or
exhibit a rigorously specified feasible sequence with B_d/d^2->0.
No numerical parameter sweep or unbounded higher-coefficient search
is needed. If neither result is proved, save the exact unresolved
equations/inequality after this one attempt.

Essential actual inputs are C028a's full unchanged P_d coefficient
contract and strict S_2,S_3 signs. Use L025's convergent logarithm only
if higher actual coefficients are needed; do not assume signs for
S_4,S_5. Any essential numerical coefficient enclosure must retain
its exact inherited evaluator and error contracts, as in C028c, and
receive complete evidence inspection. No numerical result is needed
merely to form the parameter equations. C028c is a failure comparison,
not a theorem covering the new recurrence. No new DAG row exists.

A positive floor stops only this reference-family upper bound, never
lower-bounds actual root heights. A vanishing retained cost warrants
assessment of the omitted sum, not automatic full-cost control or RH.
All degree-dependent boundary cases must be included in an obstruction.
Mathlib coverage is unchecked. This is calculation/standard/high and
REPRODUCTION of a known-method specialization, not a claimed creative
central-gap payment mechanism. The latter remains blocked by the lack
of any independent full-cost upper estimate.
