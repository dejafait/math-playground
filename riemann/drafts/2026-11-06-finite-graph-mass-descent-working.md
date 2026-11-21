# Finite graph mass descent — preserved working checkpoint

Completed later in this same attempt as L878, whose canonical proof
is `lemmas/L878-supported-radial-descent-beats-every-coordinate-torus.md`.
The notes below preserve the intermediate reasoning; they are not a
second proof or an independent verification. Conceptual audit is pending.

Approved target: the exact TARGET in
`literature/2026-11-06-finite-graph-mass-descent-period-test.md`.
This is one research attempt, using L847 and L868. Main gap:
L030–L032/C032a actual-Xi all-degree mixed positivity. The proposed
intermediate gain is a universal period bound stronger than L868(11),
not the sharp threshold or a positivity theorem.

Partial reasoning saved before completion, 6 November 2026:

- Write the physical radii as rho_j=R exp(x_j) and the normalized
  torus mass as b(rho). Compact Laurent extraction gives coefficients
  (-2,0), (0,-2) equal to -C a_0^2, and (4,-2), (-2,4) equal to
  -C a_0 a_4. Each Fourier coefficient is bounded by b. Thus
  b>=C a_0^2 max(rho_1^-2,rho_2^-2) and
  b>=C a_0 a_4 max(rho_1^4/rho_2^2,rho_2^4/rho_1^2), the latter
  at least C a_0 a_4 max(rho_1^2,rho_2^2). This should make every
  sublevel compact and establish attainment by continuity.
- No coordinate torus can have constant phase on an open angular
  rectangle: reflect its holomorphic Laurent function in the two
  fixed circles, apply the one-variable identity theorem successively,
  then compare the nonzero (4,-2) coefficient with the missing
  (-4,2) coefficient. This needs to be written with the radius factors
  and both identity-theorem steps explicit.
- At u=x_*+t v the full derivative is -i div(f v), f=F(Phi_x*).
  Where f is nonzero, its modulus derivative is
  |f| v dot grad(arg f). A supported v=-chi grad(arg f) should give
  a strictly negative mass derivative. Verify the support, finite
  descent, full Jacobian and unchanged zeros; formal differentiation
  alone is insufficient.
- L868's upper-only domination and C1 Stokes on the compact graph
  homotopy should give K>=-B for every original admissible triple.
  No stronger regularity, growth or zero-removal assumption is allowed.

No theorem is certified by this working note. The remaining tasks are
the detailed phase and finite-descent proofs and exact Stokes signs.
Stop if these fail or only an arbitrary-radius comparison survives.
