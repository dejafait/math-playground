# Full-star thinning — bounded attempt checkpoint

The gate-approved target is the exact TARGET in
[the prior SPECIALIZE assessment](literature/2026-10-25-two-core-full-star-thinning.md).
The main gap remains arbitrary-center 67/68 safety. This attempt tests
only deletion from the two specified L030 families while retaining
their identical complete common stars, with left distinguished column 16.

The audited L125 rigidity and formula (8) supply a candidate map from
all left polynomial indices to all right polynomial indices. Its linear
part is multiplication by a nonzero field scalar. The remaining proof
obligations are restriction to nonstar indices in both directions,
distinctness and forbidden intersection for every paired support, then
disjoint-edge counting with both full stars counted separately.

The downstream use is to exclude this full-star-preserving repair of the
full-law construction. Continue if the verified sum bound is below twice
1532496; otherwise abandon this matching as a sufficient obstruction.
Incomplete stars, other left columns, arbitrary marginal laws, global
compatibility and actual RS realization are outside this attempt.

Initial exact arithmetic gives 2552584 nonstar indices per side and
2590122 as the proposed retained-size sum bound. These numbers alone
do not verify the polynomial correspondence or a sharp optimum.

## Completed disposition

The symbolic verification and restricted obstruction are canonical in
L126. The counting certificate is
`scripts/finite-support/full-star-thinning-count.json`.
Separate critical audit is proposed under a REVIEW_REQUIRED assessment;
no sharpness or broader list bound is claimed.
