# Vandermonde-retaining spectral lift: bounded working record

2026-11-01. The invocation-start EXPLORE assessment is
`literature/2026-11-01-vandermonde-spectral-derivative-hciz-review.md`.
Work is confined to its actual N=2 test, with arbitrary fixed complex
a1,a2, the full tail and analytic C_2. The target is not a positivity
claim. Main gap: L629's complete signed form has no uniform Gamma/2
lower bound; even that would leave pointwise Xi signs unresolved.

Read L623's full Gamma, L624's arithmetic definition and compact
convergence, L629's exact signed prescription, and L631's full-tail
closure and polynomial diagnostic. Reused the supplied source comparison
and checked the multiplicative-insertion stop/history. Existing changes
are preserved. No cross-notebook input or further literature is needed.

Candidate specified before coefficient extraction: let I_4(z,y) be
probability-Haar HCIZ, Delta(y)=product_(i<j)(y_j-y_i),
y_*=(1/2,1/2,-1/2,-1/2), and d=(partial_y1,partial_y2,
-partial_y3,-partial_y4). Apply the full arithmetic constant-coefficient
operator B_2(d/L;a) to Delta(y) I_4(z,y), then apply
partial_y2 partial_y4, evaluate at y_*, and divide by 12. The arithmetic
operator is defined using the Taylor series of L631 (7)-(8), or an
explicit geometric series of translations from that exact rational
formula. This construction does not use the invariant-polynomial radial
theorem; it differentiates the scalar multiplied HCIZ identity itself.

Required test: justify the operator's convergence and confluence on a
common neighborhood, prove the full germ identity rather than fit
parameters, and independently extract constant amplitude and all nine
cross coefficients. In degree four, Delta(y) has degree six and the
two confluence derivatives imply that only arithmetic orders <=8 can
contribute; this must be justified from homogeneous expansion. No
uniform all-N operator estimate or sign is assumed. A mismatch or
unjustified interchange stops this candidate; a pass admits only a
later, separately gated defect test. No result was claimed at this checkpoint.

The specified construction now passes the full germ argument and the exact
finite test. The determinant expansion groups the 24 permutations into six
blocks after the two confluence derivatives. The explicit translation
series from L631's rational amplitude converges normally for sufficiently
small z, including all derivatives used here; the bound is a polynomial
in the tail index times 4^(-j) exp(4|tau|r j). There is no appeal to
Miglioli's invariant-symbol hypothesis or to a weighted-localization rule.

`scripts/full_gram/spectral_lift_n2.py` computes the degree-ten spectral
alternant, then both geometric translation moments and the finite Taylor
operator. The constant amplitude equals one and every degree 0..8 matches
L631, with all 495 multiindices and pair interchange checked. The complete
diagnostic, normalization, geometric moments and five determinant rows
were inspected in `scripts/full_gram/spectral_lift_n2_certificate.json`.
The canonical proof is saved as L632. This is a local HCIZ
specialization and representation test, with no claimed progress beyond
known sources, positive integral, growing-N bound or RH candidate.
