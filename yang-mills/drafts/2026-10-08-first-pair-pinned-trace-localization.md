# Actual first-pair pinned trace localization

Working step YM-20261008-100-first-pair-pinned-trace-localization.

The gate-approved target remains the combined order-g² Ward response in
`drafts/literature/2026-09-26-current-target.md` (SPECIALIZE, reused).
This bounded attempt concerns L078(2), not a different observable.
Main gap: ultraviolet-uniform interacting response and, independently,
the continuum axioms, reflection positivity, infrared limit and finite mass.
Intermediate target: identify the actual N³ circulation/path coefficient
through a controlled local pinned-trace limit with its variable exterior
coefficients retained. Downstream use: determine whether this contribution
requires cancellation before seeking the complete cutoff logarithm.
Continue if the pinned Green compositions have uniform local approximation
errors tending to zero after N^-3 normalization. Abandon this localization
mechanism if its low spectral tail or coefficient-freezing error is not
uniform in axial level and the complete exterior heat sum.

Inputs inspected: L028, L045, L062, L064, L065, L070, L074,
L076, L077 and L078. ATTEMPTS/022–025 exclude automatic frozen
cancellation, right-row shear with generic norms, uniform bulk axial
replacement and profile-only absolute-norm gain. None excludes this
actual variable-coefficient trace test. No general renormalization theorem
is reproved and no additional browsing is needed for the unchanged gate.

Checkpoint of unfinished reasoning: cyclic diagonalization writes the
normalized transverse trace as <C_R^T G delta_v,
G V_s^T D^T Q_v(s) T delta_v>. The second source is a centered
difference of a uniformly bounded finite-support vector, so its Green
image should converge in l², unlike the undifferentiated monopole.
Use the pinned sine spectrum to prove a low-λ l² tail bound O(sqrt(ε))
in squared norm and polynomial approximation above ε. L045 supplies
energy convergence for the first monopole. The coefficient-derivative
error is bounded by O(a sqrt(N)) through ||G delta_v||²=O(N).
No trace limit, sign, diagnostic identification or logarithm is assumed
at this checkpoint. Prove these claims before updating the argument.

Independent unresolved assumptions for continuation: actual diagnostic
continuum convergence/evaluation, centered path/path, scaled exterior
defect, all nine placements and other action/measure/insertion/flow jets;
subtract the shared quartic once. The interacting error <=c_box/2 is open.

Completed outcome: [L079](../lemmas/L079-first-pair-pinned-trace-localization.md)
proves a³ J_(i,N)-2 gamma D_(i,a)->0 for both probes, with the
actual diagnostic and complete heat sum retained. Its new load-bearing
estimates are the squared l² low-spectral tail <=C sqrt(epsilon),
the uniform pinned monopole norm squared <=C N, and the resulting
O(a sqrt(N)) coefficient-derivative error. L045 supplies energy
convergence; fixed-range polynomial approximation proves l² dipole
convergence. The actual pinned trace is then frozen only inside an
l² pairing, including its full variable-coefficient error.

ADVANCE / RESEARCH / REPRODUCTION: a local leading-scale
identification, not an evaluated coefficient or result beyond the
sources checked. No mathematical script or numerical evidence is
used. The unchanged ready SPECIALIZE assessment remains reusable.
The result is qualitative o(N³); no O(N²) rate is obtained.

Continuation under the same gate-approved target: establish the
continuum convergence and value of the exact D_(i,a) in L070(9),
using its actual averaged upper curvature, forest prefix, physical
sa weight, u_(a,1), full relative spectrum and both probes. Essential
inputs are L028, L062, L064, L070 and L079; L071–L073 give
finite-diagnostic structure/evidence, not a continuum-limit theorem.
Do not infer the limiting sign from L073's N=24 enclosure. A nonzero
limit would determine this selected a^-3 coefficient through L079;
a zero limit would require a finer error test before any O(N²) claim.
Centered path/path and all other response terms remain necessary for
cancellation and the logarithm. The shared quartic is subtracted once.

Completion checks: the scoped documentation checker passes (80 nodes,
349 edges). The new DAG row was checked against direct mathematical
uses: compact coefficient/mode bounds, the energy projection, exact
path and incidence conventions, and L078's reduction are retained.
L077 and L073 are contrasts/evidence, not mathematical premises.
Analytic normalization cross-check: the local tensor factor -4 gamma
multiplied by the exact trace prefactor -a²/2 gives +2 gamma a².
After multiplication by a³ this is +2 gamma a^5 sum_s s sum_y
of the actual exterior product, which matches (1) because a^4(sa)=a^5s.
This checks only the sign and scale conversion after localization;
no finite-frequency Riemann sum is identified with a torus integral.
