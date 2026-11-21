# Inverse-phase Taylor multiplier — working step 85

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
The exact target is its original-D joint small-circle resolvent bound
for L666's full independent displacement cube. The main gap remains
actual-Xi all-degree mixed positivity. A successful bound could feed
L683's unaudited transfer; H/support, realization and signs are separate.

The one bounded test is the proposed degree J=floor(sqrt(n)) Taylor
polynomial at v=0 of 1/W_(x+v)(-1), evaluated at all original nodes.
Continue if its full signed response is uniformly at least 1/2 and
its coefficient observation cost is exp(o(n)); explicitly charge the
outer nodes. Abandon this fixed-angle filter if either condition fails,
without concluding anything about the joint maximum V.

The supplied source comparison is reused unchanged. L687 was read in
full: its zero-removal stop does not apply to a filter retaining every
node. L666's exact factor formula and geometry, L661's audited envelope,
and L686's finite replacement and single-anchor limitations were checked.
No new external theorem or separate literature review is needed.

Initial algebra to check: with A_j=1/(d-t_j), b_j=t_j/(U-d*t_j),
the exact extension is W(v)=product_j(1+b_j*v)/(1-A_j*v).
Consequently 1/W(-w)=product_j(1+A_j*w)/(1-b_j*w) has nonnegative
Taylor coefficients. This suggests a subexponential coefficient cost
at degree sqrt(n), but it does not control the signed response or its
outer contribution. Independent shifts can alter that contribution.
All such claims were unfinished at the initial checkpoint.

The bounded test now has a proposed exact obstruction, being written
out for verification. Write 1/W(-w)=sum c_k*w^k with c_k>=0. Adding an
unused numerator factor gives c_(k-1)/c_k<=5k/(2n) for k<=sqrt(n).
At y=n^(-1/4)+O(1/n), the last Taylor term therefore dominates, and
|W(iy)*p_J(iy)| is eventually at least exp((1/8)*sqrt(n)*log n).
Its phase changes by kappa+o(1) between adjacent nodes, where L664's
9/5<g<11/5 gives kappa=(27/10)g strictly between 243/50 and 297/50.
A fixed window of 129 nodes contains a phase within 3/4 of pi/2.
Shifting that node and its conjugate by opposite s, |s|<=1/32, then
changes the real signed sum in both directions by a diverging amount.

The essential outer accounting is the complete undisplaced sum:
L664's audited rectangle, at offset 1/4, applies to the holomorphic
polynomial multiplier with its full exp(o(n)) contour bound. The first
lower-edge frequency vanishes exactly and the remaining error tends
to zero exponentially. Thus the full baseline is 1+o(1), not an
uncontrolled sum of individual moduli. Intermediate value then yields
an exact zero with only two shifted nodes. This is a fixed-angle
certificate obstruction, fully compatible with L686's joint-norm
lower bound for sparse shifts. No full-cube norm countersequence is
claimed. The complete argument and qualifications are now canonical in
[L688](../lemmas/L688-inverse-phase-taylor-fixed-angle-cancellation.md).
The coefficient cost passes, but the proposed uniform signed-response
test fails exactly for every sufficiently large admissible n. This
ends this one fixed-angle attempt; no angular-arc bound was derived.
