# Collective weighted three-volume — continuation975

TARGET: Attempt the class-uniform stopped three-particle weighted determinant bound using collective real third-volume growth and Vandermonde weight decay, with coupled H and all initial separations retained.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse completed review975 in 2026-11-14-three-particle-collision-volume-review-974.md, including exact/broader searches and local duplicate/failure checks; no matching full theorem or admissible counterexample was established and no novelty is inferred.
SOURCE_EVIDENCE: TNV https://arxiv.org/html/1706.03822v2#A2 AppendixB(B.1)-(B.5), PDF p22; WKM https://arxiv.org/pdf/2008.10321v2 Sections2.2/2.4-2.5/3.1, Theorem4/Proposition5/full proofs, pp4-9; Hall-Ho https://link.springer.com/article/10.1007/s11005-025-01946-9 Proposition3.1/Remark3.2/full proof; Voit-Woerner https://arxiv.org/pdf/1910.07888v1 (2.1), Theorem2.8/full proof. Review975 records the full comparison; repair976 directly rechecked the first two load-bearing local tools.
COMPARISON: Arbitrary-k real compound growth supports a bounded three-volume attempt on compact survivors, but no inspected source pays its singular weighted exponent. Holomorphic heat-root evolution and real repulsive boundary regularity have different hypotheses. The elementary three-column complex determinant/real-volume comparison requires direct justification.
GAP: Prove |W_t(u)|<=C|Delta(u)|^2 uniformly over the full fixed-data class below or refute it admissibly; failure of a sufficient ambient-volume envelope alone is a narrower method obstruction.
REASON: Literature-only recovery976 supplies missing direct source URLs, rechecks the local variational and compound inputs, and approves the unchanged target for one mathematical attempt. The EXPLORE verdict is reused, not a new mathematical result; neither the inequality nor a counterexample is established.
SCOPE: Exactly the class below, unit flat raw physical time and full fixed-time Jacobian, all separations and first lifetime including outer exit; no restart, metric change, symmetry of H, separation assumption, sign, current, homology or Xi conclusion.

Fix real 0<a<R, finite T_0>0, M_1,M_2>=0 and complex H_0.
On B={z in C^3: |z_j|<R}, H is holomorphic, H(0)=H_0,
||grad H||_2<=M_1 and ||D^2H||_op<=M_2 throughout B in standard
Hermitian norms. H need not be symmetric or separable. Put
Delta(z)=product_(i<j)(z_j-z_i), U=B minus {Delta=0},
S=-2 log Delta+H, F=Delta^2 exp(-H). Log derivatives suffice.
Use dot X=conjugate(grad S(X)), X(0,u)=iu for distinct real
u in (-a,a)^3, first maximal lifetime [0,tau(u)) in U,
J_t=D_uX(t,u) at fixed physical time, J_0=i Id, and
W_t=(-1)^3 F(X(t,u))det_C J_t/i^3 before stopping, zero after
stopping and at initial coincidences. Seek finite
C=C(R,a,M_1,M_2,T_0,Re H_0) common to this entire class, with
|W_t(u)|<=C|Delta(u)|^2 for every 0<=t<=T_0, t<tau(u).

Main gap remains L030-L032/C032a actual-Xi all-degree signed
positivity. This modulus could support later multi-collision cutoff
integration; signs, actual-H bounds, global integration and Xi
transfer remain independent. C466s is the single-divisor comparison
and source convention; C466k fixes the signed form. C466t/u and
stops971/972/974 are contrasts, not theorem inputs.

One coherent attempt: use the cited real variational/third-compound
machinery on compact survivors and test collective singular growth
against the exact weight, retaining the prescribed initial plane and
the complete determinant. Directly justify the elementary three-column
norm comparison with standard Gram/Hadamard identities if needed;
this fixes the metric convention and is supporting known mathematics,
not a reason for a new lemma. Do not reprove the cited variational or
compound theorem. Do not sum independent stopped-pair estimates as
if the pair divisors were independent coordinates.

Continue on a fully justified uniform combined estimate or an
admissible fixed-data counterfamily. Numerical samples, changed initial
surfaces and an unbounded sufficient envelope do not refute the
inequality. If the attempt yields only a method obstruction, preserve
its scope and reassess without inflating it. Separated-pair control
does not meet the target. Save unfinished reasoning before lengthy
work; unique endpoints or regular first-hit surfaces must not be
assumed without need and proof. Changed hypotheses require review.

Nominate proof_attempt/development, deep_research/xhigh: this is a
difficult extension of an existing volume mechanism. A source-assessed
central signed-positivity mechanism is still missing, so creative is
unjustified. A later POTENTIALLY_NEW classification would mean only
that this bounded search established no full match; imported tools
and elementary verification must be distinguished. Mathlib coverage
is unchecked. No cross-notebook input.

## Source-link recovery976 — 14 November 2026

The supervisor required direct source URLs in this ready assessment.
The SOURCE_EVIDENCE field now contains version-specific primary URLs
(or the published DOI page), rather than only a pointer to review975.
Reopened TNV Appendix B, HTML equations (69)-(73), corresponding to
PDF (B.1)-(B.5), and WKM Section3.1, printed pp8-9, continuous-A
assumption, Theorem4 and Proposition5 with their complete proofs.
Real initial variations and conjugation are explicit in TNV. WKM's
compound growth inequality does not require the uniform negative
matrix measure needed for its contraction conclusion. This verifies
source scope only; no singular weighted exponent was evaluated.

The saved full-class target, comparison, stopping test, and original
search/failure evidence are unchanged. Review975's inspected Hall-Ho
and Voit-Woerner comparisons are reused without redundant retrieval.
The optional original calibration source remains parked; the planned
elementary norm verification remains supporting reproduction, not a
new lemma. Mathlib coverage is unchecked. No mathematical derivation,
lemma or mathematical script was made in recovery976. This is a
STALLED process repair, not renewed mathematical evidence or a claimed
counter reset. The unchanged EXPLORE target is ready for research;
subsequent mathematical work must still supply the full uniform bound,
an admissible counterfamily, or an honestly narrower method outcome.
