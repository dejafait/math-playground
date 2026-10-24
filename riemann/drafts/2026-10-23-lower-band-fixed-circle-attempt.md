# Lower-band fixed-circle attempt — work record

Approved target and prior assessment:
`literature/2026-10-23-lower-band-relative-mellin-coverage.md`.
Main gap: initial low-index signs and global mixed positivity. Test only
L454's full arithmetic comparison on 7/8<=m/r<=31/32, retaining the
pinned external premise; no theta-sector or sign assembly is attempted.

First discriminating calculation: at sigma*=15/16, put d=b-1>0 for
any fixed real logarithm center b+it. Euler-bounded inner radii have
R0<d, and outer interpolation radii have R2<d+1/8. A disk containing
the target and its radius-rho Cauchy circle needs R1>=d+1/16+rho.
Then R1^2>R0 R2, since (d+1/16)^2-d(d+1/8)=1/256.
Consequently theta=log(R1/R0)/log(R2/R0)>1/2. This concerns
this fixed concentric-disk certificate, not actual zeta derivatives
or all possible Littlewood methods. Need check exact domains and
record an explicit uniform upper bound before finalizing.

Planned explicit test: use L452's center 2+it and radii in units
1/256: R0=255, R1=273, R2=284, R3=286; reserve rho=1/256.
Compare 273^3 with 255*284^2. If theta<2/3, obtain normalized
logarithm and derivative O((log t)^(2/3)) on the entire changed
strip. This misses o(sqrt(r)); never insert a growing envelope into
L330's small-p hypothesis. Recheck full fixed-window complement,
unbounded tails through shifted height zero, both residues and
non-Euler B lower bound using that weaker exponent. The attempt
will stop if this first certificate fails, even if these tails pass.

Continuation test: only a genuine o(sqrt(r)) complete-domain bound
would justify freezing and then a separately assessed sector target.
An exponent obstruction parks the fixed-circle implementation for
the closed band. Any new mechanism or new target needs separate
coverage; original L323/L327 and fixed-r failures remain unchanged.
At this saved stage unfinished: exact exponent arithmetic, full relative
tail bookkeeping, canonical proof and checkpoint. No further conclusion
was claimed at that stage.

Completed in this invocation: the canonical calculation is L456. Seven
exact rational checks pass in
`scripts/lower-band/fixed-circle-threshold-certificate.json`.
The explicit full-band exponent is <2/3 but >1/2; every fixed real
center has the same strict >1/2 obstruction at the lower endpoint.
All noncentral relative terms tend to zero, but the central magnitude
certificate does not establish little-o variation. Outcome NEGATIVE,
REPRODUCTION; no actual sum sign or RH consequence. The sole current
action and routing are in PROGRESS.md; the changed mechanism remains
REVIEW_REQUIRED, with no new saddle mathematics approved here.
