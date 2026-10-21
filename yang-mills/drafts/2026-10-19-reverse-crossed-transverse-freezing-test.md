# Ordered transverse freezing test — 2026-10-19

Approved target: the unchanged complete reverse remainder in
`drafts/literature/2026-10-19-reverse-crossed-quantitative-remainder.md`.
This is saved unfinished reasoning, not an established estimate.

Main gap: interacting reflected error <=c_box/2 and the continuum/infrared
construction. Intermediate target: bound L246(2)'s equal-level bulk
trace minus a comparison frozen in transverse position but retaining
finite-mesh raw exterior values and heat coefficients. Downstream use:
combine with L245 after independently matching raw continuum/heat data.
Independent component rates and all interacting gaps remain.

Plan and discriminating test: after an exact finite axial sum, bound
its endpoint deficit, then use squared Fourier-derivative commutators
on the literal transverse words. Continue if the complete heat-summed
bound is <=O(N^(5/2)log(eN)^2). Abandon a factorwise estimate whose
actual mass losses exceed that threshold. No separate first absolute
moment, projection-commutator operator gain, transpose transfer or
varying-mass substitution in a fixed-mass limit is allowed.

Candidate orders, suppressing fixed finite stencils: cycle the last
exterior scalar to the front. The first word has A=D R_epsilon D*,
then exterior v_k, an order-zero H=Z_j T G_h D_mu* C_mu*, displacement
u, and a bounded convolution containing the sole Q_delta. The second
word has A=Z_m R_epsilon D*, then the same H and displacement, ending
in C_mu D*. Collect v_k and u to the left, retaining [A,M_v],
[H,M_u] and [A,M_u]. Expected three-dimensional symbol bounds:
A(first) bounded with uniformly bounded L2 first derivative;
A(second) has uniformly bounded L2 norm and derivative O(epsilon^-1/4);
H is bounded with uniformly bounded L2 first derivative in h.
These would give O(a N^3 epsilon^-1/4), after the prefactor a and
all t, for the scalar-placement errors. Raw finite-stencil errors
must be bounded separately, preserving the middle energy order.

Known scope and failures: L245 freezes by definition, L246 changes
only axial level, and L244 compares boundaries. None proves this
transverse placement estimate. L228's common-scalar squared-moment
method supports the test, but its different trace bound is not
transferred. Preserve ATTEMPTS/028--032 and L094's obstruction.
Input proofs being checked: L105 L107 L228 L242 L244 L245 L246,
with L104 raw symbols as needed. No new source review is required
within the saved assessment's exact target and techniques.

Completed: [L247](../lemmas/L247-reverse-crossed-transverse-freezing-rate.md)
proves the raw-data freezing comparison with error
C_i[N^2 epsilon^(-1/2)+N^3 epsilon^(-1) exp(-cN sqrt(epsilon))],
uniformly in h,delta. At the existing schedule this is O(N^(5/2)).
The scalar-placement part itself is <=C_i N^2 epsilon^(-1/4);
bounded-offset raw stencil replacements give the larger allowance.
Both exact word orders and the endpoint deficit are written out in
the canonical proof. No mathematical script or new source review was
needed. This is partial REPRODUCTION progress with separate audit
pending; full raw continuum/heat matching remains unproved.
