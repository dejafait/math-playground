# Endpoint first-order subtraction test — 2026-09-24

Gap and intermediate target: the endpoint arithmetic value at the
coupled heights is still unsigned. L347 stops the full coefficient-space
sampling norm because the nonconstant coefficient mass is at least
r/4−O(1). Test the exact first correction
Q_r(a)=r^(-1)Σ_(m,n)(mn)^(-1−1/r)U(m,n)exp(ia log(n/m)),
with U from L332, and the grouped coefficients of R_r−Q_r.
An algebraic removal of the order-r mass could make a smaller signed
remainder a useful input to a different sampling argument. The explicit
correction, its remainder at a_n, and the other low Laguerre levels
would still need control. Continue this subtraction if it removes the
order-r obstruction; stop any renewed absolute norm certificate if the
remaining coefficient mass still misses its required threshold.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md and
global DAG, and inspected the existing tracked and untracked work.
L332 gives a coefficientwise expansion with an ℓ² remainder, not an
ℓ¹ expansion. L335 and L347 give the normalized Liouville evaluation.
L344–L347 stop direct, dual and joint absolute sampling certificates;
none subtracts the explicit first term. L330's derivative-magnitude
failure remains relevant to any later bound on Q_r(a_n). The September
21 admission condition is superseded by GOAL.md, with all mathematical
evidence retained. No earlier subtraction calculation was found.

Unfinished reasoning saved before completing the estimates: write
s=1+1/r+ia and L(s)=ζ′(s)/ζ(s). Absolute Dirichlet differentiation
suggests the exact identity
Q_r(a)=[−2 Re L(s)−Re L′(s)/4−(Re L(s))²/2]/r.
For the Liouville character replace ζ by F(s)=ζ(2s)/ζ(s).
Since F(1+w)=A_1 w+A_2 w²+O(w³), its logarithmic derivative has
leading term 1/w. Thus Q_r[λ]=−r/4+O(1), suggesting cancellation
of L347's order-r evaluation. This alone does not bound the remaining
ℓ¹ mass. A refined local Mellin expansion and a different character
may distinguish a real coefficient-mass improvement from cancellation
at only one test point. All convergence, remainders and threshold
comparisons are still to be checked at this saved stage.

Zero consecutive unresolved exploration turns preceded this test;
no RH candidate is asserted. Prior unfinished work is preserved.

Completed assessment — 2026-09-24: NEGATIVE.
[L348](../lemmas/L348-endpoint-first-order-subtraction-obstruction.md)
proves the proposed exact logarithmic-derivative identity. The
subtracted remainder has long-height mean square O(r^(-4)), and its
Liouville evaluation is O(1). However, its value at the trivial
character is 3r/4+O(1), while its constant coefficient is O(r^(-2)).
The remaining nonconstant coefficient mass is therefore at least
3r/4−O(1). The two character tests together give the uniform lower
bound 3r/16−O(1) even after choosing any real scalar multiple of Q_r,
including a scalar depending on r. The refined Liouville constant
suggested in the saved reasoning is unnecessary for this decision.

WHY IT FAILS: the [canonical proof](../lemmas/L348-endpoint-first-order-subtraction-obstruction.md)
shows that the same first-order polynomial reacts differently to
the zeta pole and the Liouville zero. Removing the latter's large
value introduces a large remainder at the former. Scalar damping
cannot cancel both, and removing the constant frequency does not
alter their leading orders. Positive-weight sampling norms then
still cost at least cN² against the required o(N), or at least cN
after normalizing the squared vector-Abel budget. This remains true
with independent interval weights and sample-dependent scalars.
It is a bound on the certificate, not the actual discrete mean.

Stop this first-order subtraction as a repair for absolute sampling.
Its improved continuous mean square does not control the prescribed
samples or the explicit correction there. The endpoint still needs
a positive arithmetic margin dominating (1+r)²exp(−r/256) at
r=2n, a=a_n. A successful discrete mean would itself leave exceptional
indices, other low Laguerre signs and the main mixed-positivity gap
unresolved. All established sign/exclusion ranges are unchanged;
STATUS remains IN_PROGRESS and there is no RH candidate. This new
obstruction resets consecutive unresolved exploration turns to zero.

A different normalization is motivated by the mismatch between the
present pole distance 1/r and the Mellin width 1/sqrt(r). Moving the
denominator to the latter scale changes the whole ratio, rather than
subtracting a polynomial with large pole derivatives. L338–L339 use
a shifted contour for conditional phase estimates; the sources checked
do not bound the full ratio's grouped coefficient mass at that scale.
An O(1) mass bound would remove the present necessary obstruction,
while leaving a new sampling estimate and the prescribed-height margin
unproved. That bound is not established in this step; the sole concrete
continuation action is in PROGRESS.md.

Analytic verification covers absolute differentiated products, exact
ratio grouping, the uniform ℓ² remainder, bounded analytic factors
at the pole and zero, removal of the constant frequency, uniformity
in the damping scalar, and the sampling certificate's quantifiers.
`python3 scripts/laguerre/check_endpoint_first_order.py` passes 1,024
formal divisor-polynomial identities, the conjugate-pair algebra,
two Laurent leading coefficients and the minimax equality point.
These checks do not certify infinite-series estimates or a_n values.
Full Mathlib coverage is not checked; inherited supporting names and
direct links are preserved. All prior changes and unfinished work
remain intact.
