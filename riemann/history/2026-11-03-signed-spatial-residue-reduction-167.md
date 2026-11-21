# 3 November 2026 — signed spatial residue reduction, step 167

Completed one proof attempt under the unchanged ready spatial-growth
EXPLORE scope. [L710](../lemmas/L710-signed-spatial-residue-and-centered-bump-reduction.md)
isolates the actual crossed residue, with the centered real-frequency
bump transform left explicit, and pays the remaining terms uniformly
on a fixed spatial patch near the relevant outer point. Its residue
coefficient exceeds exp(n/5000); no such lower bound is asserted for
the residue itself. All 13 exact auxiliary checks pass in
`scripts/one-sided-hankel/spatial-residue-rates-167.json`.

This is a local mathematical input, not a B_sp decision or certified
progress beyond the sources checked. L710 and its L709 input remain
unaudited. Both the bump-transform lower bound and a full unit-spatial
maximum upper bound are missing. The new formula refines the ready
mechanism without reopening the pole-free contour, interpolation,
absolute-envelope or two-arc completion failures.

The overview now records the residue reduction. Its shortened L709
summary still refers to the unchanged canonical bounds
S_(n,1)>=exp(n/50) and relative finite tail O(exp(-n/500)) near i/2.
Only L710's direct mathematical inputs were added to the DAG.

Continue the same approved B_sp target using L710's explicit pair of
remaining thresholds. New essential source use requires review;
coefficient growth alone is not a reason to repeat this attempt.
Full reasoning and unfinished comparisons are preserved in
`drafts/2026-11-03-spatial-residue-growth-working-167.md`.
