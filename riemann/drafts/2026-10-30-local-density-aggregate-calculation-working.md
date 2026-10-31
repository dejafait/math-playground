# Local-density aggregate calculation — working checkpoint

Invocation-start gate: SPECIALIZE in
drafts/literature/2026-10-30-local-density-aggregate-kernel-coverage.md.
One known-tool calculation only; no source arithmetic is reproved.
Existing work and the earlier source/failure records are preserved.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
the original L471 mass restricted to d_j>=delta, using L483's exact
kernel and L485's count-only L2 moment. A controlled larger sector
could reduce the unestimated part of the negative-mass majorant;
smaller displacements, full negative mass and all-height signs remain.

Calculation checkpoint, completed in canonical L486: freeze T,delta,
put U=3T, ell=log U and r_b=2^b delta<1/2. In the finite band
r_b<=d_j<min(2r_b,1/2), k_(d_j)<=r_b^(-2) and its support lies
inside |t-gamma_j|<=2r_b. Select the one right-side zeta zero per
pair, preserving multiplicity, with strict cutoff
sigma_b=1/2+r_b-1/ell. Because delta>=1/log T, this cutoff is
in [1/2,1); it includes equality d_j=r_b, at a fixed exponential
cost only. Dominate the band by the source count in
[t-2r_b,t+3r_b), using H_b=5r_b ell at base U. All starts lie
in [0,U] and 1<=H_b<=U^(1/4) eventually, uniformly over bands.

L485 then gives band kernel L2 norm at most
5 sqrt(C_485 U) ell r_b^(-1) exp(1/8) exp(-r_b ell/8).
Finite L2 triangle and sum_b 2^(-b)<=2 give the total at most
10 exp(1/8) sqrt(C_485 U) ell delta^(-1) exp(-delta ell/8).
The continuous fourth moment yields the uniform bound
B_delta/(T(log T)^3)<=C delta^(-1)exp(-delta log T/8).
No shell supremum, spacing, general-weight (19), selected-amplitude
norm or external half-plane premise enters.

Discriminating comparison: delta=8 log log T/log T makes this
upper bound O(1/log log T), improving C483a's sufficient sector.
For delta=log log T/log T, its scale factor is
(log T)^(7/8)/log log T, tending to infinity, although
delta log T tends to infinity. This is failure of this certificate
to prove the all-mesoscopic claim, not a lower bound on actual mass.

Full hypotheses, padding, constants, citations and proof are now in
lemmas/L486-local-density-aggregate-kernel-bound.md. The new audit
assessment is REVIEW_REQUIRED; no same-turn approval or critical
audit is claimed. No creative mechanism is justified yet: a concrete
weighted zero/amplitude input is missing. See PROGRESS.md for routing.
