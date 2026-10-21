# Step 143: adding the first Bcal mean

The approved target is the exact TARGET in
`literature/2026-10-15-compatible-jet-first-linear-mean.md` (SPECIALIZE,
saved before invocation). The main gap is actual clipping and the
regulator margin toward global mixed positivity. This test asks whether
L369's known first mean defeats the L414 selected-law obstruction.
Continue on a complete law or robust separator; abandon an implementation
requiring unknown higher moments or actual joint-law information.

Checkpoint before full write-up: retain L414's rare component verbatim.
Write p_H for its mass, M_H for its Delta integral and J_H for its Bcal
integral. The audited formulas give p_H=O(ell^-4), M_H=O(1),
J_H=O(ell^-2). Set b0=zeta(3)/(4pi)>0, w_H=1-p_H and
Z_H=(b0+J_H)/(c w_H). At the replacement bulk atom use a=1,h=0,
x=0,y=Y_H,z=Z_H and the exact model response. Then Bcal=-c Z_H,
Delta=c^2 Z_H^2-c^2(1-4r_H)Y_H^2. Choose

    Y_H^2=[Z_H^2+(a_* ell+M_H)/(c^2 w_H)]/(1-4r_H).

This makes both first means exact; Delta<0 and Bcal<0 at the bulk
atom eventually. Its cubic contribution is O(ell), permitted by the
specified o(ell^2) tolerance, while quartic contributions are O(ell^2)
or smaller. No exact cubic equality is required by the enlarged target.
Remaining work is the complete simultaneous bounds and canonical proof.

The L410/L412/L413 failure records and L414's separate audit were checked.
None proves infeasibility after adding this mean. The prior source review
already covers the conditional atomic theorem; no fresh source retrieval,
new zeta theorem or mathematical script is needed.

Completed: the full simultaneous verification is canonical in
[L415](../lemmas/L415-compatible-jet-first-mean-joint-sign-obstruction.md).
The construction succeeds; the enlarged moment-only implication is stopped,
pending separate critical audit. Both first means are exact, and the cubic
change is O(ell), not an error at quartic scale used for a lower moment.
All 23 quartic coordinates, both absolute envelopes and fixed pointwise
bounds have been checked. The new audit proposal remains REVIEW_REQUIRED;
it was not approved or performed in this mathematical turn.
