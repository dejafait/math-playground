# Right circulation with the generic mixed residual norm

WHY IT FAILS: [L064, proof section 5](../lemmas/L064-mixed-pinned-endpoint-regrouping.md)
uses the right circulation and full fractional axial spectral sum before
estimating the actual paired K_1 path/path contraction. Although K_1
has an N-independent operator norm, the full right forest-lift
covariance trace is O(N^5), and the generic whitened residual norm is
O(N). The resulting absolute trace bound is still O(N^(7/2)), versus
the required O(N²). The actual alternating right path map retains
transverse gradients wherever its interior path coefficients are
nonzero; its exact local stencil is recorded canonically in L064(19).
This does not show that the complete composed contraction or signed
heat sum is nonzero, nor refute a sharper cancellation. Park this
combination of spectral gain and generic residual estimates. The next
mechanism must use the residual's component structure, not repeat
the localization or absolute-norm closures in ATTEMPTS/018–020.
