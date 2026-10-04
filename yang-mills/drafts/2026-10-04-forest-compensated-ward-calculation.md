# Forest-compensated finite Ward calculation

The completed target is the exact TARGET in
drafts/literature/2026-10-04-forest-compensated-ward-identity.md. Its prior
SPECIALIZE assessment is reused without further literature work. Existing
changes, the stopped global BRST prescription and earlier boundary/locality
failures are preserved.

The gap is an explicit nonlinear generator acting on L003's forest slice.
Its proposed use is to retain the removed-link derivatives in L011's
response expansion. The stopping test is preservation of all pinned roots
and forest links, with a fully differentiated reduced-Haar divergence.
Compare it pointwise with L010's full divergence; no zero-divergence
assumption is allowed. The required interacting reflected error remains
<= c_box/2, and no bound toward it is sought from finite gauge reduction.

Working derivation saved before the longer algebra check, now completed
in lemmas/L016-forest-compensated-nonlinear-ward-identity.md:

- Use the allowed convention h.U_xy = h_x U_xy h_y^(-1), with h = 1
  on every boundary vertex. For each rooted-forest path let P_v(U) be
  its ordered link product from root to v, with inverse matrices on
  reversed traversals. Put P_v = 1 on every boundary vertex.
  The quotient map is q_e = P_x U_e P_y^(-1). Its inverse is
  U_e = k_x q_e k_y^(-1), k_v = P_v^(-1), with q_f = 1 on forest links.
- At a slice point, differentiate P_v along V_a and write
  omega_v = D P_v[V_a]. Because the forest links are all identity,
  omega_v is the signed sum of the full X_f along that root path.
  It vanishes on the boundary. For every remaining link,
  Y_e = X_e + omega_x - Ad_(q_e) omega_y gives W q_e = Y_e q_e.
  On a forest edge X_f + omega_x - omega_y = 0.
- The product-Haar gauge/quotient coordinates give an equivariant
  full field the form dot q = W(q), dot k_v = -k_v omega_v(q).
  The orbit component has zero Haar divergence at fixed q.
  This proves div_reduced W = (div_full V_a)|_slice pointwise.
  The statement is checked with all derivative terms retained;
  neither the compensator divergence nor the omitted forest-link
  divergence is separately zero by this argument.
- Gauge invariance gives W S_g = (V_a S_g)|_slice and W O = (V_a O)|_slice.
  The divergence comparison passes: the reduced insertion is exactly
  the old full insertion restricted to the slice, and compact Haar
  integration supplies its centered Ward identity for both existing
  Wilson-flow probes.

The full compensator away from the slice includes adjoint transports,
as specified by L016's rooted recursion. On the slice, differentiating
each path sum gives the remaining-link derivatives of every X_f. The
derivative of the endpoint adjoint transport has a zero contracted
commutator, but the derivatives of omega remain. Their reduced divergence
equals the forest-link part of the original full divergence. This is a
pointwise comparison; neither part is separately zero in general.

The independent check
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/forest-ward/check.py` passes.
It uses exact rational unit quaternions and dual derivatives of the actual
clover rule with one-site interior coefficients at N=4. Two forests test
lower-face and reversed upper-face paths, all pinned roots and tree links,
the full retraction derivative at nontrivial gauge coordinates, action
derivatives, full and reduced divergences, and L010's plaquette regrouping.
The reduced compensator contributions are 322843/709800 and 1304/20475,
exactly the omitted tree-link divergences. Dropping those derivatives
therefore fails this test. The all-mesh proof covers the original u_a and
the two existing Wilson-flow probes; the coefficient samples supply no
Wilson expectation, locality bound or ultraviolet estimate.

Outcome: ADVANCE / RESEARCH / REPRODUCTION. This is local progress in
the approved finite representation, using known tree-gauge and Haar
machinery. No claim beyond the checked literature is made. The exact
identity is complete, so a repeated audit would be redundant. The ready
free-linearization subcase can test its use with the forest Hessian and
the existing Hodge quotient before any further interacting expansion.
Exploration turns used are zero after this relevant input. The reflected
error requirement <= c_box/2 and all construction/mass-gap gaps remain
open; no complete candidate is asserted.
