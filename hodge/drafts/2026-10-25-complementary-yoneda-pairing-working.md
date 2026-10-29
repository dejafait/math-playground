# Complementary Yoneda pairing — bounded attempt, step 551

Invocation-start gate: SPECIALIZE in
`literature/2026-10-25-adjoint-complementary-yoneda-component.md`.
The target is the actual composite R[j_1u,j_1v], not an arbitrary
quadratic obstruction model. Inputs read: L071, L116, L164, L165;
L116 retains L108/L109/L111/L115. No changes to their hypotheses.

Main gap: primitive Hodge realization, with hypothetical F existence
still independent. Intermediate target: vanishing of this complementary
component on all H=H^0(B,M). Downstream use: constrain the freedom in
L165 for the actual bracket, before any point-obstruction exclusion.
Test: compute Q([j_1u,j_1v],iw) for every w in H^1(B,M); continue only
for justified cancellation/detection, otherwise record the surviving
operation and park. ATTEMPTS/068,/092,/093 remain in force locally.

Work in progress: for closed Dolbeault representatives alpha,beta,gamma
of j_1u,j_1v,iw, their degrees are 1,1,2. The trace integral is
Tr_X(alpha beta gamma + beta alpha gamma). Cyclically moving beta
in the second term past degrees 1+2 gives a minus sign, giving
Tr_X(alpha[beta,gamma]), not zero. The source's intermediate-line
sign discrepancy is avoided by using its final invariant identity
and explicitly checking these degrees. No pure-relative representative
or bracket-compatible splitting is assumed.

The actual derived composite r mu (j tensor j) has source
(M tensor M)[-2] and target M[-1]. It is therefore a global Ext^1
operation, not a sheaf Hom. Its local vanishing cannot by itself
kill the global operation.

Completed: the full calculation, hypotheses, citations and limits are
canonical in L166. No vanishing or nonvanishing was obtained; this is
EXPLORATION, with the cyclicity-only route parked in ATTEMPTS/094.
The new polynomial-lift continuation is REVIEW_REQUIRED and was not
attempted here. This working note preserves the unfinished-stage record.
