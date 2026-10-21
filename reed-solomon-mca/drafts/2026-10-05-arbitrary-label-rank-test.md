# Bounded arbitrary-label alternating rank test

Started October 5, 2026; approved target and coverage are in
[the saved assessment](literature/2026-10-05-cyclic-0125-arbitrary-label-rank.md).
This is one falsification attempt, with at most 4096 distinct bijections.
No sampling result will establish the universal statement.

## Gap, inputs, and test

The pinned model has error between 11/q and 16/q, against allowable
fifteen at q=97^20. The intermediate target is rank 28 for every bijective
labeling of L025's cyclic 0125 family by H. L010 supplies moment-column
independence, L025 supplies the supports and disjoint pair, and L026
supplies the necessary alternating equations and eight cyclic controls.
The ready EXPLORE assessment checks duplicates and recorded failures;
the fixed-label stop is not an arbitrary-label exclusion.

A universal rank certificate would exclude this family over every
extension, using the disjoint pair to exclude dependent directions.
A certified deficient labeling stops that uniform linear criterion.
It does not supply a decomposable alternating vector, full weights,
sixteen distinct finite parameters, or actual admissible L010 locators.
If all tested cases have rank 28, report EXPLORATION and keep universality
open; continuation requires a universal mechanism or a different
discriminating test, rather than another sample batch. Other support
families and ABF26 correspondence remain independent gaps.

## Construction and basis independence

The complete applicability argument, basis-independence proof, and
certificate qualifications are recorded in the arbitrary-label subsection
of [L026](../lemmas/L026-cyclic-0125-affine-support-exclusion.md).
No symmetry reduction of the labeling list is used.

## Reproducible bounded coverage

The generator will first list the eight cyclic generator labelings,
then all single transpositions of each, then explicitly constructed
affine exponent orders, bit orders, block orders, and rotations of
the increasing numerical H order. Duplicate labelings are discarded.
Remaining cases use Python's Random with integer seed 20261005042,
shuffling the increasing numerical H order. The certificate records
the complete labeling list, origin of each case, actual coverage,
all support blocks and selected full-column-rank minors. Its list,
not a claim about random distribution or symmetry, defines coverage.

Stop at the first deficient case and save the complete matrix,
row reduction and a nonzero kernel vector. Independently reconstruct
that case using nullspaces of the actual four-by-eight moment matrices.
For full-rank cases verify the saved maximal minors, and check support
annihilators against independently reconstructed moment nullspaces.
All arithmetic is exact modulo 97. Full certificates stay under
scripts/cyclic-0125/.

## Completed outcome

EXPLORATION. All 4096 tested labelings have rank 28; required rank is 28.
Coverage: 8 cyclic controls, 960 single transpositions, 120 additional
affine exponent orders, 380 additional bit orders, 28 additional block
orders, 32 numerical orders and 2568 seeded shuffles. All 1820 individual
four-element support blocks occur, but this does not cover all simultaneous
sixteen-support arrangements. No deficient case or verification failure
occurred. The independent audit checks every maximal minor and every block,
with 27784 passing checks, including the eight nullspace-basis controls.

Full evidence: `scripts/cyclic-0125/arbitrary-label-rank-result.json` and
`scripts/cyclic-0125/arbitrary-label-rank-audit.json`. Reproduction commands
and rigorous finite-case qualifications are in L026. The sample gives
local exclusions beyond the inspected cyclic-label conclusions; it gives
no universal result, new global bound or certified originality.
Mathlib coverage of the exact enlarged target is not checked.

Close this sample route without another batch. A proposed continuation
uses the common factors of neighboring support quartics to seek a universal
coefficient argument; it needs a separate literature approval before any
proof attempt. This is a change from numerical falsification to a proposed
universal mechanism, not a reset of the mathematical exploration budget.
