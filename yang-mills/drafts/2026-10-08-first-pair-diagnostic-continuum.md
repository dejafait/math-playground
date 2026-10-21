# Actual exterior diagnostic: continuum-limit attempt

Working step YM-20261008-101-first-pair-diagnostic-continuum.

The unchanged SPECIALIZE assessment is
`drafts/literature/2026-09-26-current-target.md`. The gate-approved
combined-response target is unchanged. This attempt tests an intermediate
input: convergence of the exact D_(i,a) in L070(9), for i=3,6, to an
explicit signed continuum functional. L079 would then identify this
functional as the selected a^-3 coefficient up to 2 gamma. Its evaluation,
the complete response/logarithm and the interacting reflected-error bound
<=c_box/2 remain independent gaps, as do the continuum axioms and mass.

Continue this limit mechanism only if the upper boundary row and actual
prefix converge at each fixed exterior mode and a uniform polynomially
weighted heat majorant controls the entire exterior sum. Abandon it if an
uncontrolled boundary trace or axial-prefix tail prevents either test.
Do not infer a limiting sign from L073's N=24 enclosures, or replace the
actual prefix by the stopped bulk-profile approximation.

Duplicate/failure checks: L070 defines the exact diagnostic; L071 removes
only Psi_24; L072–L073 concern finite tensor evaluation and enclosure;
L079 expressly leaves continuum convergence open. ATTEMPTS/024–025 rule
out uniform bulk-profile replacement and profile-only absolute-norm gain.
This attempt instead retains the exterior mode's entire lower-rooted
prefix and takes its continuum limit on the compact coefficient support.
L008's fixed-mode form convergence and full heat bounds are ready inputs;
general flow/stress renormalization results in the saved assessment are
supporting context, not a theorem evaluating this diagnostic.

Unfinished reasoning saved before writing the proof: for a continuum
relative mode f_k and eigenvalue lambda_k, let A_k=f_k/sqrt(lambda_k).
The ordinary discrete square-root covariance column is exactly
a A_(k,a), where A_(k,a)=f_k/sqrt(lambda_(k,a)) sampled on its staggered
grid. The positive upper curvature should tend to
(d A_k)_(1,mu)(4,y). The interior transverse forest lift should tend to
A_(k,mu)(x)-partial_mu integral_(-4)^(x_1) A_(k,1)(h,y) dh.
For an axial cosine with n>=1 the exact prefix of its physical samples
is sin(n pi s/N)/(2 omega_(n,a)); for n=0 it is sa/sqrt(8).
Thus the constant edge mode and the full physical distance are retained.
Check these factors and the upper sign against L026/L070, prove fixed
mode Riemann convergence, then control all exterior labels before any
conclusion. No limit or sign is assumed at this checkpoint.

Essential continuation inputs: L008, L026, L070, L071 and L079.
Unresolved assumptions: evaluation/sign of the continuum functional,
finer o(N^3) remainder, centered path/path, scaled centering defect,
all nine placements and other action/measure/insertion/flow jets. The
shared quartic must be subtracted once in any complete regrouping.

Completed outcome: [L080](../lemmas/L080-first-pair-diagnostic-continuum-limit.md)
establishes D_(i,a)->D_i for both actual probes, with an explicit
absolutely convergent continuum series. The positive upper curvature
limit uses D_1 R_F=D_1, so no interior-prefix approximation is imposed
on the upper pinned row. The exact prefix formula retains n=0 and
converges to the lower-face integral on the actual coefficient support.
Uniform first-derivative bounds on normalized relative modes give
bounded diagnostic factors; the complete double heat sum is dominated
by C exp[-tau(|k|^2+|l|^2)/16]. L008 supplies the already proved
quadratic-form matching. L071's finite Psi_24 cancellation passes to
the limit without removing the surviving sector.

ADVANCE / RESEARCH / REPRODUCTION records a local specialization.
No continuum value, sign or nonvanishing is established. Through L079,
the selected trace has limit a^3 F^circ->2 gamma D_i, but its finer
remainder and all other response terms remain. No mathematical script
or further literature review was performed.

Continuation: evaluate/enclose L080(2) for i=3,6 with full spectral
tail and all transition weights retained. Reuse L072–L073's finite
tensor/enclosure methods only after justifying their continuum
specialization. Essential inputs for that test are L008, L070, L071,
L072, L073, L079 and L080. Continue to coefficient cancellation if
either signed value is certified nonzero; a zero value would instead
require a quantitative L079 remainder test before any O(N^2) claim.
The unchanged broad combined-response target and assessment remain the
sole Next action and NEXT_REVIEW. Independent limitations above remain.
