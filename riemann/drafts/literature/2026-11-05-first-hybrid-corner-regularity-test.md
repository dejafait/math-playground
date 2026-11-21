# First affected hybrid order — finite regularity nomination

TARGET: Test the structured regularity of the r=6001 hybrid matrix across its full L831 one-coefficient error interval, without assuming any exceptional-minor sign.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step658's hybrid/xi, Toeplitz corner and structured-componentwise searches in 2026-11-05-hybrid-saddle-determinant-stability-scope.md; this is a finite rank-one subcase, not a growing-order claim.
SOURCE_EVIDENCE: Duits DPP2 AppendixA Lemmas66/69 and proofs, printed pp.51–52; Rump 2003 Section9 (9.1)–(9.3), Theorem9.2; Rump 1997 Proposition2.6. Exact source links, hypotheses and inspected cases are in the parent review below.
COMPARISON: Known finite determinant algebra and regularity definitions cover the reduction; a Xi-specific scalar sensitivity bound is unpaid. No source supplies this hybrid margin. This is ordinary specialization, not a new sign mechanism or an originality claim.
GAP: Certify structured distance>1, a singular member of the prescribed interval, or a precise informative obstruction; hybrid reference sign, growing orders and other mixed signs remain independent.
REASON: The first affected order isolates one coefficient without fixed-symbol asymptotics or positive Schur blocks; it tests whether the full pointwise saddle tolerance can support a stable comparison.
SCOPE: Newly written ready nomination requiring separate approval next turn. One finite r=6001 test only. No matrix value, inverse entry, cofactor ratio or sign has been derived or certified here.

The main gap is actual-Xi all-degree mixed positivity. A paid regularity
margin could help later sign transfer, with a reference sign independently
proved. Essential inputs are L018/L021, L776 and L830/L831.

Use B=[b_(6000+q-p)] for 0<=p,q<=6000, with the unchanged b_j:
a_j for j<12000, H_*(j)/(8*4^j Gamma(2j+1)) for j>=12000. Put

    e=(30/T_12000)b_12000,
    T_12000=12000/W_0(24000/pi),
    B(t)=B+t e E_(0,6000),   -1<=t<=1.

Here E_(0,6000) has a single1 at that coordinate. First verify that
this is precisely the uncertain support at the specified order. Lower
coefficients are exact actual coefficients, not rounded replacements
or already certified minors; no coefficient certificate is presumed.

Import [Duits's finite Sylvester identity](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf),
AppendixA Lemma66, printed p.51, and the rank-one case of Lemma69,
p.52. Pay nonsingularity before using B^-1. Otherwise use determinant
multilinearity/cofactors without division by an unproved nonzero value.
Do not reprove Sylvester's identity or add a lemma solely for its algebra.

The requested threshold is d(B,e E_(0,6000))>1 using
[Rump 2003](https://www.tuhh.de/ti3/paper/rump/Ru03g.pdf), Section9
(9.1), journal p.49, with this sparse support and real perturbations.
The test must justify and evaluate the scalar determinant condition
along the entire closed path, including a singular reference, zero
slope and endpoint equality. Pay errors in low coefficient evaluation,
H_*, W and every determinant/cofactor estimate. Keep the full L831
tolerance rather than fitting the actual error or treating it as roundoff.

Useful evidence is a certified margin with actual/required bounds or a
certified real t in the closed interval giving a singular matrix. A
symbolic ratio left unpaid is not an advance. If only an unestimated
exceptional-minor ratio remains, record that obstruction and stop; do not
initiate an unbounded dense calculation, precision sweep or neighboring-r
search. Any later script must save its full certificate and print the
result, actual/required bounds, failures and path. Previews are not proof.

Regularity preserves the reference's unknown sign; it does not give
det B>0. A singular member rejects only this pointwise robust certificate,
since arbitrary sampled-coefficient changes need not satisfy analytic
correlations. A failed sufficient norm bound is inconclusive. No
growing-order claim, assumed exceptional sign or cross-notebook input
is permitted. Matching Mathlib coverage is unchecked.

[The parent assessment](2026-11-05-hybrid-saddle-determinant-stability-scope.md)
contains the full source comparison. No essential source remains blocked
for this finite specialization. After separate approval, route as
calculation, standard/high, REPRODUCTION. A genuinely creative central
sign attempt remains unprepared: no new quantitative reference-sign/
conditioning mechanism has been identified.
