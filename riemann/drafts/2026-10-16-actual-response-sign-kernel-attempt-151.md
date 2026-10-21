# Prescribed-response conditional feasibility — step 151 working record

Approved target: Test whether L416's full moment list permits joint-sign avoidance when the height marginal is uniform on [H,2H] and all response coordinates and jets equal their actual values at that height.

The unchanged step-150 SPECIALIZE assessment is reused. Main gap: actual
negative-Bcal clipping and L413's regulator-scale/full-error margin toward
global mixed positivity. The intermediate test preserves the prescribed
response graph and uniform base measure, changing only the conditional
critical triple. Its plausible use is to distinguish information supplied
by this coupling from the selected-list obstructions L414--L416.

Read the supplied overview/DAG and assessment, L414's construction and
exact conversion audit, L415's calibration, L416's complete construction
and audit, L410's constants, L389's Hardy identification, and the relevant
L369/L409 statements. The scoped failure records explicitly exclude this
new marginal. Step-138's inspected weak-duality coverage is reused; no
source theorem constructs prescribed moments here. Existing work is
preserved. No external source retrieval or mathematical script is needed
for this algebraic test.

Checkpoint before completing the attempt: use at each actual height the
two actions X_act(t) and -X_act(t), with measurable probabilities. Exact
conversion makes Bcal odd and Delta even. Thus all six second moments,
Delta's first mean, all 23 quartics and all three absolute envelopes are
unchanged pointwise. On Delta>0 the sign is forced to make Bcal>=0;
on Delta<=0 it remains adjustable. The unresolved requirements are the
first Bcal and signed cubic means. Work out their simultaneous attainable
bounds with their distinct tolerances; do not assume clipped information
from the existing uncut moments.

Continue this implementation only if those two moments can be attained
with uniform errors, or a separating gap can be proved. An unevaluated
signed/absolute integral is not a certificate. Failure of this two-action
ansatz cannot separate all allowable conditional critical triples. Do not
alter height mass, response amplitude, actual response derivatives or
curvature to make the construction work.

Completed one bounded attempt. The exact calculation is canonical in
[L417](../lemmas/L417-same-height-sign-kernel-reduction.md). It reduces
this two-action ansatz to the simultaneous first/cubic pair and gives
attained scalar extrema with the required error scales. Those extrema
contain unevaluated sign-restricted absolute integrals; no feasible pair
or robust separating gap has been established. Exact conditional radial
preservation of both second and fourth moments only returns the same
two-action kernel. This is EXPLORATION / REPRODUCTION, not a new zeta
input or a completed feasibility obstruction. No mathematical script was
run, and no new source coverage was approved.

For the same already covered target, the next implementation should allow
critical magnitudes and directions to change at each fixed response,
preserving the moments only after integration. Test a conditional
rare/bulk mixture with fiber masses summing to one, rather than assuming
the clipped integrals in L417. It must supply fixed bounds, exact enough
odd second moments, the negative first Bcal mean and the positive cubic
coefficient together. None of those calibration obligations is solved
by this note. L417 is not a separator for that larger class. The main
argument in PROOF.md is unchanged.
