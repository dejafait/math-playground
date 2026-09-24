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
