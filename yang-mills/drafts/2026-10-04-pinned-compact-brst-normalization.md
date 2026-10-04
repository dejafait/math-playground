# Boundary-pinned compact BRST normalization — applicability calculation

The completed target is the unchanged TARGET in
drafts/literature/2026-10-04-compact-brst-gauge-fixing-normalization.md.
Its SPECIALIZE coverage is reused; no additional source search is needed.

The proposed intermediate input is a nonzero global normalization that
could extend L014 to Wilson links. The discriminating test is whether the
boundary-pinned domains satisfy Testa's presentation of Neuberger's
vanishing theorem. A passing applicability check stops this particular
global completion. It gives no ultraviolet estimate: the required matched
reflected-error bound remains <= c_box/2.

Applicability calculation, saved before final documentation and finalized
in lemmas/L015-boundary-pinned-compact-brst-normalization-vanishes.md:

- At fixed even N >= 2, the interior vertices number v = (N-1)^4 >= 1.
  The site gauge group is SU(2)^v. Only links contained in the geometric
  boundary are fixed. A space-time boundary introduces no boundary into
  this product of compact group manifolds.
- Use U^h_xy = h_x^(-1) U_xy h_y and a real orthonormal anti-Hermitian
  basis t^a. With c_x = c_x^a t^a, the odd left derivation is
  sU_xy = -c_x U_xy + U_xy c_y, sc_x = -c_x^2,
  s bar c_x = i b_x and sb_x = 0. All site variables are zero at boundary
  vertices. These constraints and fixed boundary links are preserved.
  Direct calculation gives s^2 U_xy = -(sc_x+c_x^2)U_xy
  + U_xy(sc_y+c_y^2) = 0, and s^2 c_x = 0.
- For V(U) = -(1/2) sum_e Re Tr U_e, let R_x^a differentiate U^h
  in h_x = exp(t t^a), and set f_x^a = R_x^a V. Then
  f_x^a = (1/2) Re Tr[t^a(sum_out U - sum_in U)].
  All derivatives are globally smooth and bounded on the compact link
  manifold. Set M_xy^{ab} = R_y^b f_x^a; then sf = Mc.
- For alpha > 0, Psi = -sum_x,a bar c_x^a(f_x^a+i alpha b_x^a/2)
  gives sPsi = alpha |b|^2/2 - i(b,f) + (bar c,Mc).
  Each Berezin coefficient is a bounded smooth link coefficient times
  a polynomial in b and exp(-alpha |b|^2/2+i(b,f)). The bosonic
  integrals and all derivatives needed by the cited theorem converge.
- The site vector fields are sums of left/right invariant Haar fields.
  The ghost divergence vanishes because the structure constants are
  totally antisymmetric; s bar c is independent of bar c and sb = 0.
  The restricted functional therefore has exactly the invariant
  integration domains used in Testa, hep-lat/9803025v1, section 2,
  printed pp. 1–2, (1)–(9).

Apply the cited theorem rather than rederive its deformation argument:
the gauge-fixed Wilson denominator and every gauge-invariant numerator
are zero at positive width. The same application to Haar integration over
the site gauge group gives a zero orbit factor. Thus no ratio defines a
normalized Wilson expectation through this prescription. An alpha -> 0
limit of this zero family provides no nonzero normalization; no separate
singular delta-function prescription is evaluated.

The completed result is NEGATIVE / RESEARCH / REPRODUCTION. The source
result is known; only the pinned-cube hypothesis verification is performed
here. The canonical stopped-attempt record is
ATTEMPTS/008-standard-global-pinned-brst-completion.md. No candidate
mass-gap proof appears, and previous free and forest work is preserved.
An induced ordinary Ward formulation on the forest quotient is proposed
for separate screening; no part of it is derived in this step.

The direct algebra was also checked with exact rational unit quaternions
and a six-generator exterior algebra: full ghost nilpotence and zero
ghost divergence, twelve endpoint choices for s^2 U and the Landau
incoming/outgoing signs pass. Relative-link enumeration at N=2 and N=4
confirms (N-1)^4 interior vertices, 4N(N-1)^3 variable links and pinned
endpoints. These are supporting checks; the normalization conclusion
comes from the cited theorem and its all-mesh applicability proof.
