# Actual-G real-zero interval attempt — working checkpoint

2026-11-06. Gate-approved target and sources: unchanged SPECIALIZE
assessment `drafts/literature/2026-11-06-actual-g-real-zero-interval-stationarity.md`.
This is one theorem-specialization attempt (REPRODUCTION), not a new
general variational theorem. Main gap: L030–L032/C032a mixed positivity.

Read L018 in full, L775's radius proof and L844 through its exact density
(1)–(4). Checked the three relevant recorded stops and recent actual-G
claims for duplicates. Preserve the original collar and complement stops.

Provisional reasoning to finish checking: Conrey's Theorem 1 and L018
give infinitely many distinct positive real Xi zeros. Isolation permits
ordering them as gamma_n and choosing I_j=[gamma_(2j-1),gamma_(2j)].
These consecutive-zero intervals are separated. Under z_j=-4t_j^2,
L844 (4) is real, has constant nonzero sign in the product interior and
vanishes on every boundary face. Its denominators have exponent
k+r-1=2(r-1), with no zero denominators on this compact positive box.
The sign-adjusted continuous function therefore attains a positive
interior maximum. Apply coordinate Fermat, then the holomorphic chain
rule d/dt_j=-8t_j partial_z_j and partial_zeta_j=i z_j partial_z_j.
Need finish checking the exact constant, phase and coordinate lift before
recording the canonical proof. No Hessian, contour or sign claim follows.

Continue if all these applicability checks hold for every finite r>=2;
abandon this construction if any fails. No numerical script is needed.

Completed: all checks pass in the canonical proof
`lemmas/L845-actual-g-real-zero-interval-stationary-points.md`.
The exact restriction has constant
R_k^(r(r-1))/(8^r 4^(r(r-1)) G(R_k)^r), with the overall sign
(-1)^(r(r-1)/2). The argument uses a sign-adjusted real maximum,
not differentiation of a modulus. The nonzero coordinate multipliers
are -8t_j and i z_j. This is local reproduction of the approved inputs,
pending independent audit, with no contour or sign consequence.
