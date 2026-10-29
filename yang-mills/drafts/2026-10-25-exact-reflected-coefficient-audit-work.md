# L279 critical audit — work record

Approved target and prior SPECIALIZE coverage:
`literature/2026-10-25-exact-reflected-coefficient-critical-audit.md`.
This turn audits the saved coefficient; it does not derive a changed
coefficient or attempt a mesh estimate. Essential inputs: L279, L003
section 1, L011 sections 1–2, and the already inspected Kirwin v2
Theorem 2.1, Lemma 2.3 and section 3.2.

Main gap: continuum Yang–Mills with a nonzero physical sector and finite
positive infinite-volume mass for every compact simple group. The
intermediate target is an independently checked fixed-mesh coefficient,
usable for later growth diagnostics. Acceptance requires exact jets,
both means, all density/action terms, quadratic-only curvature transfer,
and an uncentered joint-moment error o_a(g^6). Stop acceptance for an
omitted term, unsupported remainder or nonlinear Hodge substitution.

Preliminary check: the ordered matrix formula gives the required
degree-two normalization; the candidate density coefficient has the
correct negative sign. The remaining audit will check the quotient
premises, the connected subtractions and the division by g^4. Existing
unfinished notebook changes are preserved. The saved production test
is supporting algebraic evidence, not an independent proof.

Completed: the independent audit is canonical in
[L279 section 5](../lemmas/L279-fixed-mesh-exact-reflected-coefficient.md).
It accepts the saved formula without a changed hypothesis or coefficient.
The quotient premises, ordered jets, all seven connected terms, precise
Laplace orders and product-of-means error pass. No higher jet is moved
to the Hodge law. The existing exact rational check was inspected and
rerun: both coefficients 47/80, actual difference 0, required 0, no
failed checks. Its full certificate remains at
`../scripts/exact-reflected-coefficient/cumulant-certificate.json`.
No new mathematical script or lemma was needed.

For next-target routing only, the saved 2026-09-27 locality assessment
was inspected: it concerns L011's different Ward/flow pair and supplies
no approved growth estimate for L279. The new logarithmic-growth test
is registered as REVIEW_REQUIRED, with no calculation or approval in
this turn. Earlier scalar-only and bulk-only import failures remain
relevant limitations, not a global ban on the exact-pair diagnostic.
