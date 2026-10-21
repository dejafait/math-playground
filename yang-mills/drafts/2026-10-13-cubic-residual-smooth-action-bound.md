# Smooth-action branch — bounded attempt

The prior EXPLORE assessment is
`literature/2026-10-12-cubic-residual-action-cubic-scale.md`, for the
unchanged complete cubic residual/action response. The main gap is the
ultraviolet-uniform interacting reflected comparison, then continuum
and infrared construction. Intermediate target: bound L158's complete
V_i by O(N^3), retaining the exact Sigma A B_h K B_(L ell)^T R order.
A bound could support a subsequent signed-limit calculation; it does
not settle vanishing. Continue if the actual smooth action column
controls the full prefix sandwich; abandon a norm shortcut that still
exceeds cubic scale. E,E and all retained cubic coefficients remain.

Unfinished reasoning saved before the longer proof: insert Sigma's
square roots on either side of A, after restricting B_h to a compact
cutoff equal to one on A's input support. The residual form has norm
O(N), and the cutoff gradient-weighted B_h K^(1/2) has HS norm
O(N^(3/2)). The remaining factor is K^(1/2) B_q^T R Sigma^(1/2),
q=L ell. Its direct part is O(N^(1/2)). For its prefix part use
K<=Y=M tensor G and D_0^T q=0: S^T M_q D_0 is an off-diagonal
skew nearest-neighbor transport. Smooth multiplication is bounded in
the mixed energy of Y^-1. Axial and transverse transport sandwiches
are respectively O(N^3) and O(N^(7/2)); multiplying by q=O(N^-3)
gives O(N^(1/2)). These estimates still require full boundary and
coefficient-product justification; this paragraph is not a result.

Inputs being checked: L018, L026, L028, L150, L156, L157, L158.
No external theorem or changed literature target is proposed. Prior
failures ATTEMPTS/009, /011 and /036 remain in force within their scope.

Completed: [L159](../lemmas/L159-cubic-residual-smooth-action-branch-cubic-bound.md)
proves |V_i|<=C_i N^3 for both actual probes. The ordered trace factors
have norms O(N), O(N^(3/2)) and O(N^(1/2)); the last estimate uses
the complete co-closed action column, K<=M tensor G and bounded smooth
multiplication in the mixed lower-anchored/transverse-Dirichlet energy.
The upper action face is retained through the exact transport-diagonal
cancellation. Fourteen rational identities have error zero, and all
six finite energy inequalities pass. The full certificate is
`scripts/combined-ward-response/cubic-smooth-action-bound-certificate.json`.
These are finite checks; the uniform bounds are analytic. The result
closes cubic boundedness of the mixed sector, without determining its
scaled limit or controlling E,E. Continue the unchanged approved target.
