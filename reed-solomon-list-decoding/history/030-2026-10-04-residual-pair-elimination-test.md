# 2026-10-04 — Residual-pair elimination test

Completed one mathematical step on the exact saved correlated-cubic
target, reusing its ready EXPLORE assessment without further browsing.
Existing unfinished changes and all earlier failures were preserved.

[L018](../lemmas/L018-residual-pair-elimination-and-root-count-limitation.md)
eliminates residual pairs from J_3-J_2/Q and resolves the near-diagonal
classes. Its marked-root quadratic gives a precise negative result:
the root-count upper allowance necessarily misses the sufficient energy
threshold by more than 6.14e14. This is a statement about the allowance,
not actual energy or an unsafe list. Signed counts for larger symmetric differences remain
unestimated, so the energy route is parked as required by the bounded
test's stopping criterion. L017's existing upper cap and the full-code
rate bounds are unchanged.

The work reproduces standard finite-field and energy tools, rather than
claiming progress beyond the inspected literature. No full candidate
appeared. STEP_OUTCOME is NEGATIVE; ACTUAL_TASK_TYPE is proof_attempt.
Exploration turns used remain 0/3 after this informative negative result.

Exact rational comparisons and independent residual-pair enumeration
on order-6/F_13 and order-8/F_17 domains passed; results are saved in
scripts/coefficient-fibers/residual-pair-elimination-results.json. The
documentation checker passed with 20 nodes and 20 edges.

The materially different direction proposed is a pole-at-zero received
word with sum/product root constraints. Its own
[assessment](../drafts/literature/2026-10-04-pole-at-zero-sum-product.md)
is REVIEW_REQUIRED: polynomial-center coverage does not authorize this
changed hypothesis. No calculation or proof on that new target was
performed. A bounded primary-source comparison is recommended at
standard/medium, before any mathematical construction is attempted.
