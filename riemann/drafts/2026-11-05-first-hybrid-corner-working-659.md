# First hybrid corner — bounded attempt, step659

RESEARCH / REPRODUCTION under the unchanged invocation-start SPECIALIZE
assessment `literature/2026-11-05-first-hybrid-corner-regularity-test.md`.
This is an unfinished scalar certification, not a new lemma or a
negative Xi minor. No source refresh was needed.

The main gap is actual-Xi all-degree mixed positivity. Regularity of
one hybrid across the full L831 interval could transfer an independently
proved reference sign. Continue only with a certified margin or singular
member; stop at an unestimated exceptional-minor ratio. Reference sign,
growing-order control and other mixed signs are independent gaps.

## Exact support and imported algebra

Use L018/L021/L776's normalization a_j=lambda_j/(8*4^j), with b_j
unchanged from the assessment. At r=6001 put

    B_(p,q)=b_(6000+q-p), 0<=p,q<=6000,
    h=b_12000=H_*(12000)/(8*4^12000 Gamma(24001)),
    e=(30/T_12000)h, T_12000=12000/W_0(24000/pi).

Every index is between0 and12000. The upper equality requires
q-p=6000, hence uniquely p=0,q=6000. All other entries are exact a_j,
not rounded approximations. L831 at the real integer supplies the
strict actual error |a_12000-h|<e. The prescribed test nevertheless
uses the whole closed path B(t)=B+t e E_(0,6000), -1<=t<=1.
Here h,e>0 by the positive real branches and Gamma positivity.

Import finite rank-one determinant algebra from M. Duits,
*Determinantal point processes*, Appendix A Lemmas66/69, printed
pp.51–52, [author PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf).
The parent assessment records the inspected hypotheses and proofs.
Determinant multilinearity/cofactor expansion needs no invertibility.
No general identity is reproved and no lemma is added for this algebra.

Put Delta=det B and C=cofactor_(0,6000)(B). The cofactor sign is
(-1)^(0+6000)=1. Delete row0 and column6000 and set p'=p-1; then

    C=det[a_(5999+q-p')]_(p',q=0)^5999=D_(6000,5999),
    det B(t)=Delta+t e C.

The cofactor involves only indices0,...,11998 and is an actual
exceptional minor. Neither its sign nor its magnitude is supplied
by L830/L831. L776 supplies the definition, not its unpaid Fredholm
norm hypothesis. No inverse of B or determinant sign is assumed.

## Complete scalar test and unpaid quantity

- If Delta=0, t=0 is singular, including when C=0.
- If Delta!=0 and C=0, the determinant is a nonzero constant;
  the whole path is regular and the sparse distance is infinite.
- If Delta C!=0, the sole possible singular parameter is
  t_*=-Delta/(e C). The closed path is regular exactly when
  |Delta|>e|C|. Equality is a singular endpoint; strict reverse
  inequality puts t_* in the interior.

For nonsingular B and C!=0 the structured componentwise distance is
|Delta|/(e|C|). Apply S. M. Rump, *Structured perturbations Part II:
Componentwise distances*, SIAM J. Matrix Anal. Appl.25 (2003),31–56,
Section9 (9.1)–(9.3), journal pp.49–50,
[author PDF](https://www.tuhh.de/ti3/paper/rump/Ru03g.pdf), to this
one-dimensional real support. Its threshold is strictly greater than1.
This is the already assessed definition and finite algebra specialized
to the exact support; it supplies no bound for the determinants.

In the nonzero case the unpaid comparison is precisely

    |Delta|/(h|C|) > 30/T_12000.

Neither determinant has been evaluated or certified, including its
nonvanishing. No actual bound for this ratio, distance, singular
parameter, low coefficients, H_* or W was produced. The singular-base
and zero-slope branches are undecided too. The scalar criterion is
not an advance, a certificate, or verification of regularity.

## Decision and limitations

Stop at the approved unpaid-ratio condition. This is EXPLORATION:
one bounded finite specialization, without a decisive regularity or
instability result and without progress beyond the assessed source
mathematics. L831's pointwise error does not pay the determinant
comparison. No dense determinant calculation, precision sweep,
neighboring-r search or unstructured inverse test was performed.
Reopening needs new quantitative determinant/cofactor input.

Even a singular member would reject only this robust pointwise
certificate; arbitrary coefficient changes need not satisfy actual
analytic correlations. Reference sign and all-degree signs remain
open. Matching Mathlib coverage is unchecked; no absence claim is made.
No canonical lemma, DAG edge or main-argument change is warranted.

An independent continuation is a source question about actual fixed-order
coefficient signs from verified zero height. Step569 records Katkova's
sector theorem and Michalowski's larger verified-height discussion;
L466 records the precise Platt–Trudgian input. No PF_6001 conclusion is
derived here. The separate nomination is REVIEW_REQUIRED, does not pay
the ratio above, and does not prepare a new central creative mechanism.
