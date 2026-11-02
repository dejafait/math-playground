# Synthetic three-moment boundary calculation — working checkpoint

2026-11-01. Approved target: Derive C645e's synthetic boundary residual certificate with every grid term and the exact n-dependent polynomial-weight cost.

Reuse the invocation-start SPECIALIZE assessment in
`drafts/literature/2026-11-01-three-moment-contour-transfer.md`.
Only the synthetic closed-disk hypotheses there are in scope.

Main gap: actual-Xi signs at unbounded heights/all-degree mixed positivity.
Intermediate target: express all three C645e moments as contour integrals
of the interpolating residual and evaluate their boundary multiplier costs.
A downstream detector still needs an independent upper bound below the
resulting necessary residual size, together with actual pole census,
multiplicities, interpolation, clearance and uniformity.

Attempt in progress: use H_k=B_n(x)[n(z-x)]^k(F-P)/B_n.
At each grid point first retain the putative residue
B_n(x)[n(it_j-x)]^k(F(it_j)-P(it_j))/B_n'(it_j), then verify
the simple zero of B_n and local interpolation removal. Check all
rational denominators before summing genuine pole residues.
On the circle |B_n|=1. The exact weight supremum is
n^k(R+d)^k. For a potentially sharper evaluated common cost, the
quadratic weight has circle average n^2(R^2+d^2); check that it
dominates the other two average costs for all n>=5.

Continue only if every singularity is accounted for and the common
cost is explicitly evaluated with exact |B_n(x)| retained. An extra
uncontrolled grid/boundary term stops this certificate. These are
unfinished calculations, not established results or Xi claims.

Completed checkpoint: the full calculation is now canonical in
`lemmas/C645f-synthetic-three-moment-boundary-certificate.md`.
It gives E_n>=1/[81R n^2(R^2+d^2)|B_n(x)|] under exactly the
assessed synthetic hypotheses. Every grid term is displayed and removed
locally, and the exact maximum of the three circle-average weight costs
is n^2(R^2+d^2). No mathematical script or numerical evidence is needed.
The result awaits independent audit; no actual-Xi transfer or residual
upper bound has been established. The unfinished notes above are retained
as the pre-calculation checkpoint, not an additional proof source.
