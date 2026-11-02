# Anchor-line uniform Hankel bound — audited synthetic obstruction

The target was the exact C645g symbol at delta=1/4, eta=1/100,
Re(a)=-5/4, with the anchor, positive integer original residues and
M<=n/3. The construction in
[C645l](../lemmas/C645l-anchor-line-chebyshev-hankel-counterfamily.md)
gives ||H_q||<720*n*exp(-3*n/80) along n=3m, m odd >=3. Its proof
and arithmetic are complete. Separate conceptual review on 2 November
2026 confirmed the stated bound without a mathematical correction;
the full audit is recorded in the canonical corollary.

WHY IT FAILS: Common-real-part support still allows a unit-residue
Chebyshev census. Its exact finite-node identity controls the error at
an exponent involving 2m, although there are only m distinct unit
residues. The continuous arcsine average can be deformed to a left
arc with a favorable exact grid-product gain. Together these estimates
control the entire boundary and hence the largest Hankel norm, while
retaining the complex inverse-grid phases. Line support and original
positive residues therefore do not force the proposed bound. No scalar
cancellation or small
singular value substitutes for this full-norm calculation.

The planar stops and C645g's small-census theorem remain intact. This
does not construct actual Xi poles, isolate a Xi layer, supply a useful
independent upper bound or decide signs. The RH gap remains open.
