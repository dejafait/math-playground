# Adaptive enclosure work note — step 189

The main RH gap remains global mixed positivity. The approved target is
exactly the TARGET in `drafts/literature/2026-10-17-bulk-haar-integral-enclosure.md`:
determine whether L426's fixed I is nonzero, without changing its mixture,
multiplicative response or ordered selector. Reuse that prior SPECIALIZE
assessment and the known inclusion method cited in L426. No new source
review or general integration theorem is needed.

Inputs: L426's exact integral and step-188 enclosure, L423's exact mixture,
L422's audited coefficient tails, L419's ordered rule, L425's exact
complementary gaps and L037's pi enclosure. L424 and audited
L368/L369/L390 explain the prospective trajectory comparison. Existing
step-175 sampling and step-188 uniform-mesh failures remain intact.

One attempt: retain the 32768 initial cells, and repeatedly bisect a
cell with greatest mass times observable width. Compare its four possible
coordinate bisections by the achieved certified width reduction; intersect
each child range with its parent. Keep the exact dyadic masses and full
response tail. Caps: 65536 final leaves, 262144 candidate-child evaluations,
plus reading/verifying the initial certificate. Cache response and selector
intervals; do not use sampled values for proof decisions. A zero-excluding
interval is the main threshold. Width at most 3/4 of step 188's width is
the declared material-narrowing threshold. Otherwise stop this direct
adaptive implementation and reassess a materially different mechanism.

A nonzero I would distinguish L423's complete law from the trajectory
occupation identity on this test. Even success would leave actual
clipping, L413's full-error regulator margin, actual realization and global
mixed positivity unresolved. No sign or realization is assumed.

Completed within both caps. Canonical proof and exact bounds are in
L426's step-189 section; complete data are in
`scripts/discriminant/bulk-haar-adaptive-enclosure-189.json`.
The bound -223/1000<=I<=138/1000 is still inconclusive. The exact width
ratio is below 71/100, so the declared narrowing threshold passes.
The split tree and all 65536 terminal masses/ranges were checked by
complete replay and exact aggregation. This is local progress using
known inclusion methods, with no progress beyond the sources claimed.
Further work on the same integral is justified by this measured narrowing;
it must preserve the full tail and may still fail to exclude zero.
