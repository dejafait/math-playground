# Prescribed-response rare/bulk feasibility — step 152 working record

Approved target: Test whether L416's full moment list permits joint-sign avoidance when the height marginal is uniform on [H,2H] and all response coordinates and jets equal their actual values at that height.

Reuse the unchanged step-150 SPECIALIZE assessment. Main gap: actual
negative-Bcal clipping and L413's regulator-scale/full-error margin toward
global mixed positivity. Test a conditional rare/bulk law retaining the
actual height/response. Its downstream use is to distinguish what this
coupling forces from L416's more permissive obstruction.

Startup overview/DAG and assessment were supplied. Targeted reads cover
L414's exact conversion/rare construction and audit, L415's calibration,
L416's second-moment construction and audit record, L417 and its failed
sign-only implementation, L410's constants, L390's complete response
bounds, L406's absolute third moment and L409's cubic statement. The
existing bulk chooses a response coordinate and amplitude, so it cannot
be reused at the prescribed graph. No new literature or mathematical
script is needed for the present conditional algebra.

Checkpoint before completing the attempt: with actual X0(t), let R=|X0|,
M=lambda*(log H)^2 for fixed lambda>0, r=max(M,R), and p=(R/r)^4.
At R>0 choose Y=r*s*X0/R, with the common sign making Delta(Y)Bcal(Y)
nonnegative and Bcal(Y)>=0 when Delta(Y)>0. At R=0 set p=0,Y=0.
The subprobability kernel p delta_Y preserves each homogeneous even
quartic exactly at every height; p<=1 permits a complementary bulk
without changing the height marginal. Its total second-moment trace is
at most E R^4/M^2=O(1). Check pointwise envelopes, absolute moments and
the exact remaining cubic before claiming any feasible full law.

Continue only with a justified cubic calibration and a supported bulk
meeting both first means and all six second moments, including their tiny
odd errors. Abandon the direct L416 lift: response freedom and nonuniform
height are excluded. Unevaluated actual weighted integrals are not a
certificate, and this ansatz is not a separator for all conditional laws.

Completed one bounded attempt. Full identities, bounds and limitations
are canonical in [L418](../lemmas/L418-prescribed-response-capped-rare-component.md).
The cap supplies valid conditional weights and exact quartic preservation;
its rare second trace is O(1). The actual weighted cubic in L418 remains
unevaluated. A complementary bulk with norm O(sqrt(ell)) has only
O(ell^(3/2)) cubic and cannot fill a missing ell^2 coefficient. The zero
completion fails the leading second and first-Delta constraints, and no
full bulk has been constructed. No feasible full law or robust separator
is claimed. Record EXPLORATION / POTENTIALLY_NEW, with no novelty claim
beyond the saved comparison and no mathematical-budget reset.

For the unchanged assessed target, test the independent bulk covariance
and two-first-mean calibration on the actual negative discriminant cone
next. Retain the exact rare contributions and their potentially O(1)
odd moments; do not discard them inside the tiny final errors. The rare
cubic and actual/global/regulator obligations remain separate gaps.
The direct normalized-radius lift is parked in the ATTEMPTS record;
PROOF.md's mathematical assembly does not change.
