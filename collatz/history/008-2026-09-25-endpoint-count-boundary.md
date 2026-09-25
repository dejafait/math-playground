# 2026-09-25 — Endpoint count and its surviving boundary term

Step `collatz-2026-09-25-008-endpoint-count-boundary` concluded NEGATIVE.
The [saved test](../drafts/2026-09-25-endpoint-count-boundary.md) records
the gap, intermediate target and threshold. The primary
[source](https://mathprize.net/posts/collatz-conjecture/) was rechecked;
its exact universal target agrees with the existing foundations. Existing
unfinished work and inactive branches were preserved.

[L008](../lemmas/L008-endpoint-count-and-boundary.md) proves exact
disjoint endpoint classes and their density, retaining the finite-interval
error. At the proposed cutoff the density contribution shrinks, but the
error bound grows and prevents the estimate from reaching a count below
one. An explicit endpoint with density contribution 135/512<1 refutes
dropping that error. The
[attempt record](../ATTEMPTS/007-density-only-endpoint-count.md) stops
only the density-only inference; the true count might still vanish under
a sharper argument controlling its offsets.

There is no new exclusion of infinite aperiodic itineraries, no universal
eventual-descent bound, and no complete candidate. The count also includes
some histories starting above the chosen starting cutoff. Inverse
arithmetic remains potentially useful, while growth and compensation
remain untreated together; this motivates examining its extension to a
contracting block. Consecutive exploration turns without an advance or
informative negative remain zero.

Validation: `python3 scripts/endpoint-count/check_count.py` passed complete
periods at depths 1–4 against 183,960 direct forward starts, all integer
cutoffs in those periods, 2,046 representatives through depth 10, and
174,251 disjointness comparisons. The
[output](../scripts/endpoint-count/result.json) records exact rational
evaluation of the boundary witness. These finite checks supplement the
proof, not an infinite-depth conclusion. Mathematical review checked
positivity, complete residue coverage, disjointness, density normalization,
the error term, and both shifted endpoint formulas. The sole new DAG row
uses L007 as the direct mathematical input. Mathlib coverage is not checked.

Documentation validation command:
`python3 ../scripts/docs/check_structure.py --problem collatz`.
Structural checks do not establish mathematical correctness.
