# 2026-10-17 — step 189: adaptive exact-integral enclosure

RESEARCH / REPRODUCTION / calculation under the unchanged prior
SPECIALIZE assessment `drafts/literature/2026-10-17-bulk-haar-integral-enclosure.md`.
ADVANCE is limited to a stronger certified local bound: L426's
[step-189 section](../lemmas/L426-covariance-free-bulk-actual-height-phase-average.md)
now gives -223/1000<=I<=138/1000. It does not prove I nonzero.

The capped four-coordinate adaptive test retained the exact mixture,
both selector stages and entire response tail. Its 65536 leaves and
32768 chosen splits pass exact partition replay and aggregation; the
complete certificate is `scripts/discriminant/bulk-haar-adaptive-enclosure-189.json`.
Width falls by about 29.1 percent, passing the predeclared 25 percent
test. The remaining strict-cell width dominates the branch-cell width.

This justifies continuation on the same approved integral with the saved
partition, rather than declaring this adaptive mechanism exhausted.
The uniform-mesh and sampling stops remain recorded. The narrowing is
a known-method specialization, not a new integration theorem or a
sign, clipping, regulator, realization or RH result. PROOF.md and the
DAG are unchanged because no assembly or direct dependency changed.
