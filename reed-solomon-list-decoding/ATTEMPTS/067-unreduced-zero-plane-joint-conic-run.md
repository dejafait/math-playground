# One unreduced joint zero-plane numerical run — inconclusive

WHY IT FAILS: The one capped full-domain affine-LMI proposal reaches
10000 iterations with cone distance about 0.97148346, against required
exact distance zero. Its one rational reconstruction via L084's P+N*h
satisfies all 28 selected equalities but violates domain row 26,
22 moment signs and 28 remaining original modes. Full model and exact
failed residuals are in
`scripts/finite-support/zero-plane-joint-feasibility-results.json`;
independent original/raw reconstruction is in
`scripts/finite-support/zero-plane-joint-feasibility-verification.json`.
The [working record](../drafts/2026-10-18-zero-plane-joint-feasibility-working.md)
specifies the original affine blocks, checked zero-direction congruences,
scalings, single-run cap and preserved pre-solve repairs. This is neither
an infeasibility certificate nor a feasible point; the full-plane target
remains open. Stop this numerical prescription without a second solve or
point scan. A fixed exact face reduction suggested by the tight modes
requires its own source assessment and discriminating test. L084 and all
earlier point/weight results remain intact; their pending reviews and
independent global/RS gaps are unchanged.
