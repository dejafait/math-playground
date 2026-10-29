# Scale-adapted band calculation, 29 October 2026

Approved scope: `drafts/literature/2026-10-28-scale-adapted-band-cost-test.md`.
The main gap is L471's full B(T)=o(T(log T)^3), itself only a
sufficient mean first-sign estimate. The intermediate target is the
band h<d_j<=min(2h,1/16), h=u/log T, with the prescribed 6h disks
and h collars. A summable large-u envelope could control that sector;
fixed-u annuli, larger displacements, individual signs and mixed
positivity would remain independent gaps.

Working calculation saved before final documentation: finite factors
give cell cost C h^(-1) S_k^2 M_k rho^(4M_k-4), rho=9/10.
Bounded-strip Stirling gives |P(x+iy)/A(x)|^2 comparable to
(x/(2pi))^(-y). Reflection on y>0 makes the completed continuous
norm cost exp(|y|log T) on BOTH sides. The area integral therefore
suggests E(7u)=integral_0^(7u) exp(v)min(1,1/v)dv, and a normalized
envelope C E(7u)/u^3, comparable to exp(7u)/u^4. The complete
denominator, multiplicity, overlap and uniformity checks belong in
the canonical proof L475. This provisional reasoning is not a
lower bound for the actual band mass.

Continuation/abandonment test: continue this implementation for
dyadically summable decay or a precise additional constraint with a
plausible independent test; otherwise park it. A one-simple-pair
cell has M_k=1 and no residual-factor suppression. Existing L471's
ordinary-moment loss and the parked selected-energy/Dirichlet
routes do not supply the missing compensation.

Completed: L475 contains the full proof and confirms the displayed
envelope, including multiplicities, endpoints, both vertical signs
and a local polynomial single-pair diagnostic. The dyadic test fails;
the implementation is parked. This negative result concerns the
available upper bound only. The separate attempt record and history
give the route decision; PROGRESS.md owns the sole next action.
