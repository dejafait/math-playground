# First-derivative attempt — step 369

Approved target: compute the real first-curvature-derivative restriction
range for three distinct quaternionic lines spanning a two-plane in
L118's opposite image. Reuse the prior SPECIALIZE assessment
`literature/2026-10-18-three-line-curvature-first-derivative.md`.

Main gap: universal primitive Hodge realization. Intermediate use: a
necessary collision condition beyond L123, with actual K3 jets and angles,
F existence, gluing and transport still unknown. Test full range versus
a proper subspace of prescribed admissible first derivatives. Preserve
ATTEMPTS/047/070/071; no metric realization is sought.

Working calculation: RW (2.5) makes the derivative coefficient a tensor
in H* tensor Sym^5 E*, with reality on all six quaternionic factors.
Differentiated vector Gauss with parallel df and normal splitting imposes
T(H;L,L,L,L,L-perp)=0. Restriction/orthogonal extension on E_W should
preserve this module and the full external normal equations.

In L123's metric graph coordinates, for each H component use quintics
A,B,T and F=A+dA[Cy]+K32+K23+dB[Dx]+B. The axis normal equations
fix exactly these (4,1),(1,4) terms. The remaining diagonal problem is
K(x,x)=T0, d1 K(x,x)[u]=U(x;u), with T0=T-A-B-D_C A-D_D B and
U=dT[Hu]-dA[u]-d2A[u,Cx]-dB[Du]. Unlike degree four, the radial
identity permits separate diagonal values P=U(x;x)-2T0 for K32 and
Q=3T0-U(x;x) for K23. Their evaluation maps onto binary quintics.
Any residual d1 derivative has zero radial contraction, hence equals
(u0 x1-u1 x0) times a binary cubic. Adding Delta times a (2,1)
cubic to K32 should realize every such residual without changing the
diagonal value. This predicts an onto 24-to-16 interpolation map,
an eight-complex-dimensional kernel, and real range 36/36 after the
H index and reality. The predicted W solution fibre is real dimension 16.

To verify before claiming: explicit coefficient proof of the residual
factorization and evaluation surjectivity; Bianchi converse via the
two-dimensional alternating identity; full tensor reality and averaging;
normal differentiation and ambient extension; five-tensor source scale
a_i^(5/2)/c^(3/2), c=2lambda. No source values are assigned.

Completed: the full proof is canonical in L124. All predicted dimensions,
the uniform angle statement, real averaging on H* tensor Sym^5 E*,
normal-connection differentiation and source scale are established there.
The exact rational certificate passes every check with no failures.
The order-one restriction mechanism is parked for full range, not for a
source blocker. Separate critical audit remains pending.
