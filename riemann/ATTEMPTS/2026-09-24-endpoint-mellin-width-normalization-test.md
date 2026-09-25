# Endpoint Mellin-width normalization test — 2026-09-24

Gap and intermediate target: L302–L303 leave the endpoint arithmetic
margin at r=2n, a=a_n unsigned. L347–L348 show that the normalization
at distance 1/r from the zeta pole has order-r nonconstant grouped
coefficient mass, even after scalar first-order subtraction. Test
whether replacing the denominator by |ζ(1+1/sqrt(r)+ia)|² makes the
full reduced-ratio coefficient mass O(1). This would remove that
necessary obstruction to a weighted sampling argument. Sampling
control, exceptional prescribed heights and the other low Laguerre
signs would remain unresolved. Continue if the mass is uniformly
bounded; abandon this normalization repair if a character or a
coefficient lower bound still makes it diverge. Bounded mass alone
is not the small relative error needed for positivity.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md and
the global DAG, and inspected the tracked and untracked changes.
L332's expansion has an ℓ² bound at distance 1/r; L348's subtraction
does not change that denominator. L338–L339 shift a Mellin contour
for restricted phase assignments, not a full grouped ℓ¹ bound.
L344–L347's direct, dual and joint sampling failures remain evidence;
none supplies the proposed ratio bound. This changes the whole
normalization after the failed norm and subtraction repairs. The
September 21 admission condition is superseded by GOAL.md. All
previous work and identifiers are preserved.

Unfinished reasoning saved before completing the proof: set
δ=1/sqrt(r), σ=1+δ and c=1/2+δ. The prime-p local factor of
ζ(σ+iv+ia)/ζ(σ+ia) has coefficient absolute sum
1+|exp(−iv log p)−1|/(p^σ−1). Its product is bounded by
exp(|v| Σ_p log(p)/(p^σ−1)), with the sum O(1/δ).
At |v| of order 1/sqrt(r), the Mellin absolute Gaussian and this
linear exponential should have a bounded integral. On the far
contour the uniform crude Euler-product bound must replace the
linear exponential; otherwise its integral would diverge. Exact
regrouping, the moving-contour kernel estimates and this tail bound
still need checking. Trivial and Liouville character values should
stay of constant order; they may prevent a uniformly small norm.

Zero consecutive unresolved exploration turns preceded this test.
No endpoint sign or RH candidate is asserted at this saved stage.

Continuation saved — 2026-09-25: the proposed local-factor norm is
exact, and the logarithmic Euler derivative at σ=1+δ is
Σ_p log(p)/(p^σ−1)=1/δ+O(1), using the analytic factor
δζ(1+δ) near its fixed pole. Thus two normalized Euler factors
cost at most exp(C|v|sqrt(r)), which is integrable against the
kernel bound C sqrt(r)exp(−rv²/4) on |v|≤c. For |v|>c use
the uniform product bound (ζ(σ)²/ζ(2σ))²=O(r²) instead;
the remaining kernel integral is O(sqrt(r)2^(−r/4)).
This suggests a full grouped ℓ¹ bound independent of r, with
the coefficient integration and all ratio collisions still to
be written out. The trivial character gives relative error
tending to 3, while the Liouville character tends to −5/4.
Neither is a test at the prescribed a_n. A uniform scalar estimate
f_r(t)=1+t/sqrt(r)+O(t²/r), where
f_r(t)=exp(t/2+t/sqrt(r))(1−t/(2r))_+^r, should make the
constant grouped coefficient O(1/r) and the squared coefficient
norm O(1/r). These observations remain unfinished at this entry.

Completed assessment — 2026-09-25: ADVANCE.
[L349](../lemmas/L349-endpoint-mellin-width-coefficient-bound.md)
proves the proposed O(1) bound on the full absolute grouped
coefficient mass. Exact local Euler-factor norms control the
central Mellin contour; the crude uniform product bound makes
its far tail exponentially small. Integrating coefficients in
ℓ¹ justifies every equal-ratio grouping. This is a new relevant
input, not a repetition of a stop review. The old proof based on
diverging mass does not apply to these new coefficients.

The limitations are quantitative. The nonconstant mass still has
liminf at least 3; the trivial and Liouville evaluations of the
relative error tend to 3 and −5/4, respectively. Thus the O(1)
target is attained but a uniform absolute error below 1 is not.
The new long-height mean square is C_w/r+O(r^(-3/2)), C_w>0,
worse than L332's order r^(-2); its height limit is taken first.
There is no estimate at a_n. A relative error at most a fixed
η<1 there would give a margin at least (1−η)/(1+sqrt(r))²,
which exceeds the actual required (1+r)²exp(−r/256). Neither
the bounded norm nor the continuous mean supplies that condition.

Continue this normalization through a bounded test of the moving
coefficient vectors. The reason is that a bounded individual
coefficient mass does not bound their accumulated variation, and
L347's sampling certificate uses both. A bounded moving-vector
budget would leave the normalized weighted sampling-operator norm
as a separate unproved input; even a vanishing discrete average
would still leave exceptional indices and the other low Laguerre
signs unresolved. No sign/exclusion range changes and no RH
candidate is recorded. The concrete continuation action is only
in PROGRESS.md. Consecutive unresolved exploration turns remain zero.

Analytic review checked the same-v paired factors, the exact
Euler-factor series, the local pole logarithmic derivative, both
contour tails, Tonelli in coefficient ℓ¹, the uniform scalar
remainder, all ratio collisions, and the order of height and r
limits. The sole new algebra check is
`python3 scripts/laguerre/check_endpoint_mellin_width.py`: twelve
exact local Euler identities and 1,024 formal linear divisor
identities with constant cancellations pass. It does not certify
the analytic estimates or sampled values. Full Mathlib coverage
is not checked; inherited supporting names and links are retained.
The earlier unfinished reasoning and all previous work are preserved.
