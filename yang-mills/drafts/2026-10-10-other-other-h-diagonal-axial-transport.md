# H diagonal: axial summation before the resolvent estimate

The unchanged approved target is the complete other/other cubic limit
and comparison with -12 gamma D_i. The immediate test is the H diagonal
in L091(4), using L090(4) rather than the stopped reverse-prefix norm
shortcut in L094 and ATTEMPTS/028. Existing L091–L094 do not control
this diagonal at cubic scale. The ready literature assessment is reused;
no new source theorem or separate forest invariance is assumed.

Unfinished reasoning saved before proof completion: put
A_k=Pcal Omega_k Qcal. The diagonal is the heat sum of
Tr(K_g A_k V_h A_l^T). L090 gives the generator insertion
(Qcal G0 K_h+K_h G0^T Qcal)/2. Split G0 by its displacement
components. Its u_1 part appears to be a^(-1) U T_1, with
U_s=diag_(nu=2,3,4)(C_nu^T M_(u_1(s)) C_nu), where T_1 is the
actual pinned centered axial difference. Both residual orientations
must be retained and combined using the symmetric full heat sum.

Candidate estimate: cycle T_1 onto the right of
A_l^T K_g A_k U. Its (s,t) block contains min(s,t), with two
O(a) alternating factors. An axial difference of this block is O(a^2)
because Delta min is bounded, the exterior differences are O(a^2),
and U has O(a) differences. Compact displacement support is needed
at both ends. Each axial block of K_h is positive semidefinite,
and its summed trace should be bounded by
(N-1) Tr_(ker P)(Delta_T^-1)=O(N^4).
This would give O(a N^4)=O(N^3) after the generator's 1/a factor.
This is a proposed actual finite-trace estimate, not a proved bound
for the transverse-displacement remainder or the full H diagonal.

Continue if the exact endpoint/clover formula and every block estimate
justify this cubic bound; abandon this gain if it requires moving a
transverse multiplier through a projection or resolvent, deleting an
axial endpoint, or replacing min(s,t) by a local covariance. Essential
inputs: L009 L018 L026 L028 L085 L086 L088 L089 L090 L091 L093.
L084 L079 L080 L082 fix the reference and arithmetic qualifications.
R_R, the transverse H remainder, and the limits of the bounded terms
remain independent obligations. No complete limit or compensation is
assumed; all other response jets and the construction gaps remain.


Completed: [L095](../lemmas/L095-other-other-h-diagonal-axial-transport-bound.md)
proves the actual axial-displacement part of the H diagonal is O(N^3),
with both generator orientations combined, full min(s,t), every pinned
row and all heat modes retained. Its curvature subtraction is also
O(N^3), not subleading. No script or numerical certificate was needed.
This is local ADVANCE / REPRODUCTION, with no novelty claim beyond
checked sources and no scaled-limit assertion.

Continuation under the unchanged ready complete-group assessment:
test R_H,tr in L095(3), the actual rho=2,3,4 displacement part of the
H diagonal, for an O(N^3) signed trace bound. Keep its two generator
orientations and the full transverse projection, resolvent and variable
coefficients. The axial product-difference gain does not control a
transverse derivative of P; a signed transverse summation with its
actual coefficient commutators is the concrete next mechanism to test.
Continue if all these terms reach the cubic threshold or a discriminating
obstruction changes the route; a frozen cancellation without a finite
remainder or the old generic O(N^4) bound does not pass this test.
R_R still requires independent or joint signed control, and every bounded
trace, including R_H,ax and R_H,Q, still needs its scaled limit.

Essential continuation IDs: L009 L018 L026 L028 L048 L085 L086 L087
L088 L089 L090 L091 L092 L093 L094 L095; L065/L066 constrain residual
block extensions, and L084 L079 L080 L082 fix the reference and its
saved-table/IEEE qualifications. No separate invariance, differentiated
base-law zero, finite limit, compensation or complete solution is assumed.
The independent construction gaps recorded above remain. The assessment
and its exact complete-group target are unchanged; no new ready target
is self-approved here.
