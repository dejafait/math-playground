# Split equality fibre — bounded second-order attempt

Approved target/coverage: drafts/literature/2026-10-12-equality-split-local-slice.md (unchanged SPECIALIZE at invocation start).
Main gap: universal primitive rational Hodge realization. Local target: the necessary ASD second-order test at L plus L^{-1}, k^2=-14, h.k=0, for a hypothetical (14,21) kernel of L071/L093.
Continue only if every nonzero quaternionic tangent fails; a compatible tangent stops this necessary exclusion mechanism. No quotient smoothness, nonzero actual differential, generic stability or exact quadratic normal form is assumed.

Work in progress: determinant-one stabilizer should be U(1); diagonal H^1 vanishes, the two Dolbeault off-diagonal spaces H^1(L^{+/-2}) each have dimension 26 by zero-slope endpoint vanishing and surface RR. The real ASD H^1 should therefore have quaternionic dimension 26. The diagonal obstruction has three real components, with no off-diagonal obstruction. Check the Weitzenbock/Kähler identifications and all components, not just the complex Yoneda product.

Candidate compatible tangent: choose orthonormal e_1,e_2 in the +2 complex-weight space and v=e_1+J e_2. The quaternionic span of v appears to have identically zero circle moment map. Need prove this in the actual harmonic representation and identify the necessary curvature obstruction with these three quadratics. A formal compatible tangent is not a germ.

Actual-family bridge to check: in a smooth unitary trivialization, r_u=dot(A)_u-d_A H_u; harmonic projection kills the gauge term. Product hyperholomorphicity gives r_{Ru}=-r_u composed with R. Coefficient harmonic invariance should make the projected derivative quaternionic even at the reducible point. No claim of its nonvanishing is made.

## Completed bounded attempt

The candidate line and actual-family harmonic bridge are proved in
`lemmas/L094-split-equality-quaternionic-tangent-compatibility.md`.
The proof avoids needing an off-diagonal cokernel dimension theorem:
all harmonic tangents are off-diagonal, their curvature square is
purely diagonal, and the coefficient splitting is preserved by the
cokernel projection. The remaining scalar self-dual harmonic space is
exactly the hyperkähler triple, all three components of which vanish
on the explicit line. No higher-order or germ calculation was attempted.

Outcome NEGATIVE / REPRODUCTION: stop this necessary second-order
exclusion test. Independent critical audit is the sole proposed next
action, with a new REVIEW_REQUIRED assessment; no approval is claimed.
