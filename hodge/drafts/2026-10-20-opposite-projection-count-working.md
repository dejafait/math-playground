# Opposite projection/count attempt — working checkpoint

2026-10-20. Approved target: test a general linear projection of L137's
original opposite image to P^4 for a sharper ordered-coincidence bound.
The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-projection-double-point-bound.md`.
Inputs read: audited L120/L121/L137/L139; recorded failures
ATTEMPTS/070,073,078 are preserved. No new source discovery is needed.

Main gap: universal primitive Hodge realization, with conditional F
existence still unresolved. Intermediate target: a finite effective
smooth-source double-point residual retaining all original ordered
pairs. Downstream use: a smaller upper threshold for a later independent
lower-count comparison. Continue only if the geometric hypotheses hold
and the bound improves L139; otherwise park the failed specialization.

Working argument, not yet independently audited: write u:B -> P^N for
L137's original parametrization and l=c_1(u^*O(1)). For N>4, parameterize
centres by W in Gr(N-4,C^(N+1)), of dimension d. Containing a fixed point
has codimension five; meeting a fixed tangent/secant projective line has
codimension at least four. The source tangent-direction base has dimension
three, so a general centre kills no source tangent. Distinct-image ordered
source pairs have dimension four, so their incidence has dimension at most
d and a general parameter has zero-dimensional or empty fibre. Existing
coincidences are finite by L121. For N<=4 use linear inclusion instead.

Unramifiedness makes the diagonal clopen in the auxiliary fibre product.
On a neighborhood of the diagonal the inverse diagonal ideal is exactly
the source diagonal ideal, so its blowup residual is empty near the
exceptional divisor. The entire residual is thus the finite off-diagonal
scheme, with positive lengths dominating the original reduced ordered
pairs. Fulton Theorem 9.3 should then give length = delta^2-10delta+24,
using l^2=delta and K3 tangent Chern numbers. Remaining work in this
attempt: write every incidence and scheme step, verify the coefficient
and all low-N/empty cases, and compare symbolically with K(K+1).

Completed in this attempt: the full incidence, exceptional-neighborhood,
ordered-multiplicity, low-N and coefficient arguments are saved canonically
in L140. The result is P<=(delta-4)(delta-6)<K(K+1). The former pending
list above records the mid-attempt state. A separate critical audit is
registered with REVIEW_REQUIRED; no audit verdict is asserted here.
