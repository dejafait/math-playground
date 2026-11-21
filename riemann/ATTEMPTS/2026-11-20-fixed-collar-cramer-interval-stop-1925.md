# Fixed-collar Cramer interval stop1925

WHY IT FAILS: The one natural polynomial interval evaluation on the
prescribed d=4 collar B=[-1/4,1/4]x[3/4,5/4] gives a Gram-determinant
interval strictly inside[-0.004383,0.006650] containing0. Consequently
neither affine orientation admits the required division in this
implementation, so neither a residual-range exclusion nor a Krawczyk
inclusion was evaluated. The exact Gram matrix is positive definite;
this is enclosure loss, not nonmatching, a negative determinant or an
RH obstruction. Full failed bounds, unchanged input provenance and
independent arithmetic/symbolic replay are in
`scripts/heat/two-site-actual-collar-1925.json` and
`scripts/heat/two-site-actual-collar-check-1925.json`; conventions and
unfinished continuation reasoning are in
`drafts/one-point-theta/2026-11-20-fixed-collar-working-1925.md`.
The full finite specialization and enclosure proof are canonical in
C028u; no counterexample is claimed. Preserve C028t's audited point rank.
A source-assessed positive kernel-update representation would be a
specific new implementation idea; no site/radius sweep is authorized.
