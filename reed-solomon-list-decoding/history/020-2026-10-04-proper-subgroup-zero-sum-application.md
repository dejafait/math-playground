# 2026-10-04 — Zero-sum count on a proper smooth subgroup

Completed one mathematical step on the saved SPECIALIZE-ready count
application. Reused its exact COVERED_TARGET and existing source statements;
no additional literature work was undertaken. Preserved prior lemmas,
scripts, results, inactive branches and all pre-existing working changes.

[C012a](../lemmas/C012a-proper-subgroup-zero-sum-certificate.md) applies
Zhu-Wan's Theorem 1.1 to the proper subgroup of order 1024 in F_65537,
inside F_{65537^28}. The imported unordered zero-sum estimate, with an
elementary coarse error bound, gives more than 2^322 candidates at the
explicit center (x^(k+1),0,...,0) for each prize rate and every m>=1.
The actual ambient threshold lies between 2^320 and 2^321. Therefore
the unsafe index is n-k-1 and t_star<=n-k-2 at all four rates. This
extends the local certificate from a full nonzero subfield domain to a
proper smooth subgroup. It does not determine an exact subgroup count
or the boundary below that index.

The proposed continuation test succeeds; the cited error estimate is not
vacuous in this chosen instance. Counts retain source size Q=65537, while
the threshold retains ambient size q=65537^28. The full-nonzero-field
exact formula was not used. The primality/order certificate and a uniform
count comparison are written out, with exact integer/rational corroboration
in `scripts/coefficient-fibers/verify_subgroup_threshold.py` and its
[saved output](../scripts/coefficient-fibers/subgroup-threshold-results.json).
The rational square-root error check is separate from the coarse proof.

Outcome: ADVANCE, a relevant local applicability input; STEP_KIND:
RESEARCH; classification: REPRODUCTION. The construction and subset-count
theorem are known; no progress beyond the checked literature is claimed.
Exploration turns used: 0/3 after this advance. No complete candidate
appeared, and STATUS remains IN_PROGRESS. General upper bounds, the sharp
boundary, nonlinear cover gaps and the parked ABF26 comparison remain open.

The next direction increases agreements to k+2 on this same instance,
with two fixed coefficients below the monic leading term. That could
constrain the boundary one more grid point inward, but its joint-fiber
coverage is outside the saved assessment. The
[new pending assessment](../drafts/literature/2026-10-04-two-leading-coefficient-fibers.md)
is REVIEW_REQUIRED: the next turn must compare known results before
calculations. No two-coefficient derivation or computation was made here.

Added only C012a's genuine direct uses of L001 and L012 to the ID-only
DAG and updated the short overview. Exact-arithmetic verification and
`PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed: 14 nodes, 12 edges, compact overviews and valid links. Unique
step fields, prior ready coverage and the exact new target/assessment
match passed; `git diff --check -- .` passed. The checkpoint has 14
lines and the overview 99. Structural checks do not establish proof
correctness; the new graph inputs were reviewed against their actual
uses in the proof.
