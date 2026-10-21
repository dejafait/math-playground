# 2026-10-20 — Ordered gradient-base joint-kernel freezing attempt

Approved target: the unchanged gradient-base remainder TARGET in
`literature/2026-10-20-gradient-base-crossed-quantitative-remainder.md`.
This is a mathematical attempt, with the prior EXPLORE coverage reused.
Main gap: the interacting reflected bound <=c_box/2 and the independent
continuum/infrared construction. The intermediate comparison is L252(2)
against exactly L104(6); it could complete this component's contribution
to quantitative L011 assembly without resolving those independent gaps.

Inputs read: L103, L104, L249, L250, L251, L252 and the preserved stops
ATTEMPTS/028,029,032. L251 and L252 remain unaudited imports.
Existing work and the ready assessment are unchanged.

Checkpoint before the main calculation: write W_mu=-C_mu* M_u S_mu,
where S_mu is the centered difference, and expand zeta over its raw
plane/path rows as M_f B. Cycle only to M_u. Each resulting scalar
word contains J=C_mu D_(p,mu)*, P=B T, and one of the two terms of
X=sum_j(T_j* M_hj-M_hj T_j). Both J and P vanish to first order at
zero frequency. Commuting M_f only through the fixed-range J has an
explicit O(a) coefficient error. The principal words then have the
form Tr(M_(uf) A M_hj B), with derivative counts (3,1) or (2,2)
on the two massive inverse kernels. The error words have counts
(2,1) or (1,2), with only bounded extra shifts.

Test: prove a mass-uniform joint first kernel moment by Plancherel,
placing the squared spatial weight on the kernel with at least two
differences. Freeze h only inside the closed two-kernel diagonal.
Retain its clamped Lipschitz extension and its complete upper primitive.
If a needed one-factor absolute moment or an uncontrolled small-mass
constant occurs, do not claim the comparison. Keep all local midpoint
offsets, the full heat matrix, the physical lower weight, and the
exact L104 symbols when matching the frozen density. No new source
review or mathematical script is needed for this bounded test.

Unfinished at this checkpoint: the precise local commutator expansion,
uniform Fourier bounds, all normalization/heat sums and the comparison
of the frozen massive density to L104(6).

## Completed disposition

The test succeeds in L253, where the full proof is canonical. The
weighted squared moment belongs to the kernel carrying at least two
differences, and its partner has a uniform unweighted l2 norm. The
local commutator retains orders (2,1) and (1,2), sufficient for its
unweighted product. Global Lipschitz control of the clamped h then
gives O(N^2) freezing, including midpoint and uniform quadrature errors.
The full-torus frozen mass discrepancy is O(N^3 epsilon).

At the existing epsilon=N^(-2/3) schedule the latter is O(N^(7/3));
L252's conditional O(N^(5/2)) original-pair comparison dominates.
L253 therefore reaches the requested component threshold, subject to
separate audit of the new proof and L251/L252. The main construction
gaps remain. A new audit continuation is registered REVIEW_REQUIRED;
no second target was mathematically attempted or approved here.
