# Interior-anchor signed-tail attempt — 2026-10-25

The approved target is the exact TARGET in
[the saved SPECIALIZE assessment](literature/2026-10-25-interior-anchor-signed-tail-barrier.md).
The main gap is still initial signs at unbounded heights. This step tests
whether the fixed-anchor small-tail comparison remains viable below the
anchor-dependent logarithmic threshold; it does not seek signs.

Unfinished reasoning saved before completing the attempt: fix
3/8<eta<1/2, 0<=c<eta/2 and B>=0. Choose
max(3/8,2c)<r<eta and put
delta0=eta-r-2c log(eta/r)>0. Positivity follows by integrating
1-2c/x from r to eta. Use two legitimate, separately parameterized
instances of L461 rather than reverse its stated radii: an auxiliary
anchor alpha in (3/8,r) with outer radius r yields its circle growth
bound after multiplying by its explicit lower model; anchor eta with
an outer radius in (eta,1/2) yields the required positive lower bound.
Their ratio should be at most C T^(r-eta+4 epsilon). With
q=(eta/r)^2>1, Cauchy and the finite geometric sum then suggest a
bound C' T^(-delta0+4 epsilon), uniformly for K<=c log T+B.
Fix epsilon<delta0/4 before all constants and heights. Remaining checks:
the two model exponents, complex shifted heights, central zeros, c=0,
and the exact signed-tail conclusion. Nothing here is an RH candidate.

The existing L322 exterior obstruction and the September 24 ellipse
failure are retained. The narrowly searched later lemmas and audit
notes contain no established extension; the prior audit only nominated
this test. L461's proof and conditional audit, including its full
shifted-height bounds, have been read. No additional external theorem
is being asserted and no source re-search is needed for this ready scope.

Completed in this same bounded attempt: L462 contains the full proof.
Two independently ordered L461 instances give the required model
ratio, and choosing epsilon=delta0/8 leaves decay exponent delta0/2.
The geometric bound is uniform also for K=0 and c=0. The test's
continuation criterion is met; its result stops the small-tail route
below the stated fixed-anchor threshold. No additional target was
attempted. Full reasoning is canonical in L462 rather than this draft.
