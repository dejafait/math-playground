# Signed inverse-weight interpolation: bounded attempt

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-02-signed-finite-deweighting-cost.md`.
Only its prescribed full binomial cost is being tested. L649/L666
give the definitions/family; L667 is a contrast, not an assumed
obstruction to signed combinations.

Partial reasoning saved before completing the proof: for the unique
degree-at-most-N interpolant F(z_a)=1/w_a, N=M-1, exact finite summation
gives sum_k F_k c_k=M/R. Thus the source coefficient inequality gives
m(-1)>=log(M/R)-log S_N, where
S_N=sum_k binomial(N,k)|F_k|. A successful target cost would have the
claimed normalization. For |z_a|<1, S_N>=|F(z_a)|=1/|w_a|.

At the upper outer node m=2q-1, its ordinate satisfies y>=2/5 for
q>=5, regardless of the displacement. At u=-1 the complete inverse
weight has modulus product_j sqrt((1+A_j^2*y^2)/(1+b_j^2*y^2)),
A_j=1/(d-t_j), b_j=t_j/(U-d*t_j), with A_j>b_j>=0.
For 1/2<=t_j<=3/4, A_j>=4/3, b_j<=48/61. Monotonicity in y^2 then
suggests each squared ratio is at least
(1+64/225)/(1+9216/93025)>7/6. There are at least n/4-1 such factors.
If the arithmetic and count hold, log S_N>=(n/4-1)/14,
which exceeds n/100 by a positive linear margin. This would be a
uniform obstruction to this cost, not an upper bound on the true mean.

Pending checks: exact rational comparison; all factors including j=0;
node admissibility and q threshold; true-degree qualifications in the
Mahler step; continuation scope after the stop. No numerical result,
new source theorem, or claim about RH is used.

Completed: the canonical proof is L668. The exact selected-grid count
is (n+1)/4, improving the provisional count and giving
log S_N>=(n+1)/56 uniformly for q>=5. The rational comparison has
positive cross-multiplication difference 275775. All pending finite
identity, degree, factor and geometry checks are included there.
The outcome is NEGATIVE for this prescribed cost only. A separate
critical audit remains outstanding. No mathematical script was needed.
