# Finite penalty audit working note — step416

Approved target: Audit C999e's complete-kernel target-norm certificates and the finite penalty obstruction at n=64,128.

Prior SPECIALIZE review414 is supplied and unchanged. C997c's kernel,
C997s's exact cap/primitive, C999e's full proof and both implementations
have been inspected. Reused source coverage369/410/411/412/415; no source
blocker. The five-term signs, conjugated exponents, moment recurrence,
PSD, cap relaxation and interval-length conversion check symbolically.

Pending: independently validate all stored terms, fifteen products and
all their moments/coefficient intervals, not just terminal aggregation.
Use a separate exact-integer dyadic implementation, with its own
exponential enclosure, and compare every stored interval with an
independently computed enclosure. No generator imports, parameter sweep,
Lanczos, G,h or inverse form. Save complete replay and comparisons to disk.
Accept the strict bounds only if this full check succeeds; preserve any
specific failure without weakening the scope. The primary arithmetic
code's directed contexts, exact negation and reciprocal guards have been
read; its custom exponential still requires this independent test.

The main gap is actual-Xi positivity and forcing, not finite arithmetic.
This audit can close a local verification gap and confirm the finite
experiment should remain parked. It gives neither an E_n upper bound nor
an unbounded-n obstruction. After this bounded audit, choose a different
source-assessed continuation; no tuning of these fixed parameters.

Completed disposition: all independent enclosure comparisons pass (6924
at64, 13580 at128), with complete replay artifacts under target-radau and
canonical proof/audit in C999e. The pending paragraph above records the
pre-computation checkpoint. The finite audit is complete and the fixed
experiment stays parked. A different source-only continuation is nominated
in literature/2026-11-11-real-radius-li-recovery-review-416.md; it is not
approved mathematics and no coefficient-recovery result was derived.
