# Smooth-action second-prefix regularization — working record

Approved target: the unchanged complete cubic residual/action cubic-scale
vanishing test in the 2026-10-12 assessment. Main gap: ultraviolet-uniform
interacting reflection comparison, then continuum/infrared construction.
Intermediate test: replace F in L176(2) at fixed left mass epsilon by
F0=Phi (I_axial tensor G) on component 1, and then by F0_delta with
G_delta. Downstream use: a trace with finite transverse ranges after
polynomial approximation, retaining the two explicit axial profiles.
Continue if errors are subcubic or uniformly removable after the mesh
limit; do not infer a limit from another cubic bound.

Exact axial candidates, with D the full pinned gradient and P the lower
prefix on interior vertices: P D=I, P P^T=M, P D D^T=D^T.
With R_D=(L_D+Delta_T)^(-1), F0-F=R_D(D^T tensor G).
Its Hodge-energy square is R_D(L_D tensor G^2)<=I tensor G^2.
This should give fixed-epsilon error C N^2 epsilon^(-1/2), using L175's
supported factor and the massive version of L159's multiplier energy.
Second-mass error has energy square
I tensor (G-G_delta)^2 + M tensor Delta_T(G-G_delta)^2.
The proposed trace bound is C epsilon^(-1/2)
[N^2+N^3 delta^(3/4)]. Verify the full transverse shell sum and retain
all action faces, normal end edges, constant axial mode and heat modes.

Inputs under examination: L026 L156 L159 L175 L176. No fixed-mass signed
limit, coefficient, vanishing or complete compensation is claimed here.
Duplicate/failure check: L175/L176 retain F explicitly; history/207–208
has no second-prefix replacement. ATTEMPTS/037 concerns signed E's global
energy norm, not this sandwiched cross matrix. The ready assessment's
ATTEMPTS/009, /011, /036 restrictions remain. No new literature is needed.

Completed: both candidate bounds above were proved in canonical
[ L177 ](../lemmas/L177-smooth-action-second-prefix-mass-comparison.md).
Its full proof checks the massive multiplier energy, both terms of the
second-prefix energy square, and the complete low/high spectral sums.
Choosing equal fixed masses gives the uniform comparison (5) there.
The fixed-mass signed limit remains unfinished; see PROGRESS.md for the
sole current continuation record. These initial notes are not a separate
proof or an approval of a changed target.
