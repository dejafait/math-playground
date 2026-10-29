# Moving low cluster: bounded mathematical attempt

2026-10-29, step 548. Work in progress; no result claimed at this checkpoint.

The gate-approved target is exactly: Test whether moving-cluster compression
makes L297's complete one-heat-line low response o(1) at r_N.
Reuse the pre-existing EXPLORE assessment in
[the approved review](literature/2026-10-29-moving-low-cluster-response-test.md).
The main perturbative gap is a controlled complete tail and uniform
interacting comparison; the immediate obstruction is mixed-source and
off-ground low response after L298/L300. Success here removes only this
low-response obstruction, not the high contour, uncut estimate, higher
remainder, continuum axioms or positive mass.

Use L279 L280 L282 L283 L287 L289 L297 L298 L299 L300 and their
upstream premises, with the exact SU(2) relative cube, even N, a=8/N,
counting measure, both reflected 12-bumps, fixed unweighted H and Q,
ambient own-slice jets, full unchanged density, boundary-fixed gauges
and every variable normal endpoint. No source-uniform estimate is an input.

The single test is the full signed scalar
3 partial_s partial_t Tr_H(Wtilde_N(s,t) H_N^lo(s,t)) at zero,
with r_N fixed, retaining all four L297(22) terms. Continue on a controlled
o(1) estimate or a genuinely refined explicit threshold; abandon the
o(1) claim only upon a rigorous complete nonvanishing contribution.
An uncontrolled absolute estimate is unfinished work, not a counterexample.

Initial scoped check: L297 already contains the moving-contour calculus;
L298/L300 control fixed-ground compressions only. ATTEMPTS/047--050
stop distinct earlier mechanisms and are preserved. The supplied source
review covers the finite-matrix tools; no further literature search is
needed for this target. Existing tracked and untracked work is preserved.

The direct route under examination is to combine the signed local
row cancellations with the regularity of the actual zero-source
projector derivatives. Mixed inverse insertions and all relative-boundary
errors must be accounted for before a moving compression bound is claimed.

## Intermediate reasoning saved before the full proof

The more direct object is an energy-form bound for each of the four
zero-source derivatives of Wtilde, rather than pointwise estimates of
projector derivatives. Let Ahat=A/lambda_0. The proposed bound is
||Ahat^(-1/2) Wtilde_alpha Ahat^(-1/2)||
<= C_f(N^-1 + N^-1 sqrt(log(eN)) + N^-2 log(eN)).
This is still to be checked in the canonical proof, not an assumed input.

For the internal-curl plus quartic part, with density at order zero,
L298/L300 already give a summable first spatial moment and direction-row
defect bounded by C_f(N^-1 + d^-2 log(ed)^2). Extend each relative
component to the 2N-periodic lattice by its actual odd vertex/even
midpoint reflections. The norm and total difference energy each acquire
factor 16 in their squares. Subtracting the column component at the row
anchor controls the row difference by C||L^(1/2)v||. A discrete slice
trace estimate controls every weighted boundary layer by
C(N^-1||v||^2 + ||v||||L^(1/2)v||). On fixed H, L=C*C,
so this would give O(N^-1) in the Ahat form norm without ground-field
supremum bounds, a moving frame, or any complex-source Cauchy estimate.

For mixed source order, h_-(x)h_+(x)=0 for the exact two bumps.
The two ordered inverse insertions have kernel factors with exponents
(3+j,4,3+k), j,k in {0,1}. Subtract the common-anchor source product;
the Lipschitz error reduces either the first or middle exponent by one.
The resulting complete convolution is bounded by
C_f N^-1 log(e+r)^2 (1+r)^(-1-j-k). Pairing with the other
internal line gives N^-1 log(e+r)^2 (1+r)^-5, which has a summable
row. Distinct inverse slots, vertex/inverse slots and two vertex slots
must be checked separately; all freeze to the same zero source product.
Quartic slots remain local. No boundary-to-infinite transfer is needed
for this mixed derivative.

The external-curl placements should retain L300(23)'s energy bound for
all labeled source allocations, using L297(10),(13), including both
orders inside G_-+. If all these checks pass, L297(19)'s weighted
low-contour trace estimates give O_f(N^-1/2 log(eN)^(5/2)) for the
entire four-term scalar. High-contour estimates are not part of this test.

## Completed attempt

The full proof is now canonical in
[L301](../lemmas/L301-complete-low-heat-response-energy-form-bound.md).
It verifies the relative extension energies, weighted boundary trace,
all mixed source allocations and the external-curl restoration, then
applies L297's weighted residue estimates to all four trace terms.
The resulting O_f(N^-1/2 log(eN)^(5/2)) bound passes the registered
o(1) test under the upstream premises. No mathematical script was
needed. Separate conceptual audit remains pending; this working note
is preserved as intermediate reasoning, not an alternative proof.
