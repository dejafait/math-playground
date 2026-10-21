# Straight-forest local loop: bounded working step

The approved target remains the complete remaining order-g^2 response
for L010's two probes, using the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. The main local gap is
the unestimated cutoff behavior of L011's complete coefficient; the
interacting reflected-error threshold c_box/2 and the continuum and
infrared construction remain independent gaps.

This step tests L025's unflowed C_p in the direction-1 straight forest
of L003, rooted at the lower face with the upper axial link omitted.
The intermediate target is a mesh-uniform bound or a two-sided growth
estimate on compactly supported plaquettes. Its downstream use is to
decide whether absolute loop bounds can control the nonradial action
or whether tensor/path and cross-group cancellations are essential.
Continue absolute estimates if the loop is O(1); abandon that particular
bound if an interior diagonal grows with N. Such growth is not a growth
theorem for the selected contraction or the full response.

L025 supplies the actual ordered tensor and both pairing classes;
L018 supplies the exact retracted Hodge Gaussian; L003 supplies the
relative tensor-product spectrum. L017 fixes the path convention.
L019 retains cross-group cancellations. The prior isolated-Haar and
curvature-transfer failures have been checked; neither tests this raw
local covariance bound. No extra general renormalization theorem is
needed, and the ready assessment is reused without external browsing.

Working calculation, to be checked before canonicalization: for a
transverse edge at axial level j with adjacent interior endpoints,
R_F z has the component z_mu minus the transverse difference of the
first j axial links. Hodge components are independent. The axial row
has squared norm 2j, and the ordinary Hodge Laplacian has eigenvalues
at most 16, suggesting Var >= j/8. Factoring that row through the
transverse incidence should give an upper bound j on the path part.
A four-dimensional spectral shell sum should bound the direct-link
variance by 8. Check all normalizations, endpoint restrictions, the
spectral shell count, and an independent finite covariance computation.

Do not infer a value for K:C_p, a probe contraction, the logarithm,
forest-invariant partial groups, or a bounded full remainder from
these raw covariance estimates. No flow damping acts on this loop.

Unfinished reasoning was saved before the finite checks. Completed:
[L026](../lemmas/L026-straight-forest-local-link-loop-growth.md) proves
j/8 <= Var_F(x_mu) <= j+8 and j/8 <= ||C_p|| <= 4(j+9), hence
Theta(a^(-1)) raw loop growth on compact interior plaquettes.
The variance decomposition, spectral shell bound, and pinned path
were checked analytically. Independent dense incidence computations
check 162 interior transverse edges and 216 interior plaquettes at
N=4; the complete seven-check summary in the certificate was inspected.
No failure was found. Small-mesh geometric checks do not assert
admission of the supported Ward generator.

Outcome NEGATIVE, local REPRODUCTION: the proposed O(1) raw matrix
bound fails. This is new local route evidence, without an originality
claim or a complete response estimate. The stopped absolute bound
is recorded in ATTEMPTS/011-uniform-straight-forest-link-loop.md.

Continue in the unchanged approved target by testing the growing
path directions inside L025's quadratic Wick coefficient 6 K:C_p,
retaining its no-internal-pair class and all other L011 terms.
Essential inputs are L026, L025, L018, L011 and L019. The specific
unresolved questions are whether that ordered tensor removes the
O(N) directions, how its remaining coefficients contract with both
probes, and how the other jets cancel any surviving power terms.
L022's independent flow obstruction and L024's radial bound remain.
Do not assume forest independence of this partial group, heat damping
of C_p, a bounded full remainder, or a zero full logarithm. A tensor
cancellation would authorize estimates of the surviving contractions;
a surviving power coefficient would require grouping with other
jets, rather than declaring growth of the complete response.
