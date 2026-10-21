# 2026-10-05 — Radial action local-loop test

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md` for the remaining full
coefficient. Preserve the unfinished radial and forest calculations.
The bounded intermediate target is L023's fourth-chaos sum
W_i = sum_p alpha_(i,p) beta_p. Its O(a^-1) bound does not exclude a
logarithm. A uniform O(1) bound would remove this selected action
summand as an unsuppressed logarithmic source; a surviving divergent
diagonal would instead force its inclusion in a cancellation group.
Neither outcome controls the full coefficient or the interacting
reflected error <= c_box/2. L021 concerns a different flow occurrence;
L022's obstruction prevents transferring general nonlinear jets.

## Reasoning saved before completion

Write K=C_u d, P=d Delta_1^-1 d*, and M=M_3+M_6. For a unit plaquette
e_p, set A_p=Delta_1^-1 d* e_p. Then d A_p=P e_p and
d*d A_p=d* e_p. Hence the residual diagonal simplifies exactly to
beta_p=(d C_u P)_(pp)-(P M P)_(pp). The second term is bounded by ||M||.
The first uses only a fixed number of nearby entries of P.

Freeze u at the plaquette center. The row error is O(1), because the
one derivative contributes a^-1 while smooth coefficient differences
are O(a). On the infinite lattice, constant-u d C_u is odd under
inversion about the plaquette center and P is even, so their product
has zero diagonal. It remains to bound the relative/infinite projection
difference by O(a) or better in the fixed interior support.

A short-time split at t_a=delta*a/128 appears sufficient. Write
P=d integral_0^t exp(-s Delta_1) ds d* + P exp(-t Delta_2).
The two tails have entry size O(a^4/t^2)=O(a^2). In the short integral,
uniformize the component Laplacians with jump rate 8/a^2. Interior
matrix powers agree until at least delta/(4a) steps; at this time the
Poisson mean is at most delta/(16a). The remaining tail is exponentially
small in 1/a, even after the two derivatives and time integration.
This would give a local projection difference O(a^2), and a constant-u
boundary correction O(a). The infinite lattice is only a comparison
kernel, not a replacement boundary condition.

## Completed bounded attempt

L024 supplies the full proof. The exact identity for beta_p is valid
because A_p is co-closed and L A_p=d* e_p. The short-time comparison
uses substochastic component-Laplacian uniformization; paths of fewer
than floor(delta/(4a)) steps agree, while their Poisson tail is
exponentially small. Both projection heat tails are O(a^2), with the
relative bound retaining all boundary modes. This proves the required
local projection-entry estimate O(a^2). Centered average/difference
parity gives the exact frozen-row cancellation; coefficient freezing
costs O(1). Therefore sup_p |beta_p| is O(1), and L023's trace bound
sums it against either actual flowed probe. The radial S4 contribution
is O(1), with its quadratic Wick class still o(1).

The pre-existing exact stencil script passed all 24 checks. Complete
inspection of its /checks certificate found zero parity defects in
every plane/displacement case. The certificate verifies stencil parity,
not the analytic boundary proof. No coefficient for the full Gamma or
finite radial matching value is claimed. The main reflected-error
threshold <= c_box/2 and other continuum/mass gaps are unchanged.

Continuation within the same assessed full-response target uses L011's
nonradial action S4-S_(4,rad), L023's radial definition, and L019's
forest-change cancellation constraints. Its contraction must retain
the exact forest covariance unless linear-curvature invariance is
proved; L022's obstruction rules out assuming general transfer. A
fixed-mesh contraction formula with all internal loops retained is a
discriminating first deliverable before any cutoff-growth claim.
