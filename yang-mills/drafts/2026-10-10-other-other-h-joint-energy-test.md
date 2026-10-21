# Transverse H joint circulation/covariance energy attempt

Saved unfinished reasoning under the unchanged complete other/other
EXPLORE assessment. Main gap: interacting ultraviolet control;
intermediate threshold: an actual O(N^3) bound for L099(2), followed
separately by its a^3 limit and the complete-group comparison.

Start from L088(3). Since P D^T=0, its gh block is exactly

    A_k=P [B_b^T M_f B_q-B_q^T M_f B_b
             +(B_q^T M_b-B_b^T M_q)D] Q.

The exterior-circulation terms M_f are retained. Thus the circulation
pieces of A_l^T K_g A_k place one D on each side of the covariance
after cyclicity, before coefficient commutation. The full generator
has a curvature input; its intervening variable multiplier and all
endpoint filters must still be handled rather than commuted away.

Proposed bulk test: for the infinite transverse/axial grid define
E_j(theta)=D(theta) r_lambda(j) D(theta)^*, with the original forward
incidence D in periodic unshifted phases, lambda=sum |e^(i theta)-1|^2,
r_lambda(j)=exp(-kappa |j|)/(2 sinh kappa),
2 cosh kappa-2=lambda. Test

    sum_j (sum_z |z|^2 ||E_j^vee(z)||_F^2)^(1/2) < infinity.

Unlike L109's separate absolute first moments, this keeps both
circulations with the covariance and uses quadratic sums. The
candidate derivative bound is C(1+|j|sqrt(lambda)) exp(-c|j|sqrt(lambda));
three-dimensional integration would make its L2 norm O((1+|j|)^(-3/2)),
summable over the complete axial line. This calculation is not yet
verified. It would control bulk Lipschitz multiplier commutators in
Hilbert--Schmidt norm. The actual pinned-boundary comparison,
nonlocal P factors, generator order and exterior-circulation errors
are separate unproved obligations, so this test alone cannot establish
an actual cubic bound, limit or compensation.

Continue if this exact energy kernel has the summable quadratic
moment and a valid coefficient-error placement; abandon this placement
if it loses a derivative or merely returns the O(N^4) estimate.
Essential inputs: L009 L028 L085 L088 L091 L095 L099 L108 L109.
L097 L098 L100 L101 L104 L107 retain the other unevaluated limits;
L084 L079 L080 L082 retain the comparison and IEEE qualifications.
No boundary gain, projection commutator gain, cubic limit or coefficient
value is assumed. Preserve ATTEMPTS/028--032.

Completed: L110 now contains the full proof of the joint bulk moment,
its scalar Hilbert--Schmidt commutator consequence and the exact pinned
circulation split with an O(N^3) exterior-circulation remainder. The
initial unverified calculation above is preserved as the attempt
snapshot; the conclusions and qualifications are canonical in L110.
There is no complete R_H,tr cubic bound or limit. The cubic remainder
has not been evaluated and cannot be discarded.

Continuation within the unchanged approved complete-group target:
test the quadratic coefficient-error placement for the actual D,D
core of L110(1). Retain P between the two F coefficients, G_tr in
its exact curvature-input order, min(s,t) and both coefficient levels.
The discriminating subtest is an O(N^3) total trace error for the
actual Lipschitz coefficient differences, including relative pinned
covariance/image terms and staggered shifts, using L110(2)--(3) only
where its bulk hypotheses hold. Continue on a controlled finite-box
estimate; abandon this placement on a demonstrated unsandwiched
derivative loss or a non-summable boundary error. An insufficient
upper bound alone supplies no signed growth. No pinned extension,
uniform operator-norm projection gain, cubic coefficient, compensation
or a^3 limit is assumed.

Essential inputs for that placement are L009 L028 L085 L088 L095
L099 L110; L108 L109 and ATTEMPTS/028--032 retain the shortcut stops.
L091 supplies the complete assembly; L097 L098 L100 L101 L104 L107
retain the other unevaluated limits. L084 L079 L080 L082 retain the
reference coefficient and IEEE qualifications. All independent jets,
finer scales, matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass
remain unresolved. The exact target and saved EXPLORE assessment are
unchanged; no new target is self-approved by this continuation.
