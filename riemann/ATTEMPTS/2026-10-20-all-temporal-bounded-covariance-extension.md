# All-temporal extension of the finite covariance repair

Step 273 gives an informative negative result for the exact approved
target; the separate step-275 critical audit validates it. The canonical proof is
[L444](../lemmas/L444-all-temporal-occupation-excludes-bounded-covariance-repair.md).

WHY IT FAILS: With L443's x-second density, rare components, mean and
cutoff fixed, a compact temporal test localized where the intermediate
calibration is negative detects a positive fast-response-phase defect
of order sqrt(log H). The complete Poisson term costs at most
O((log H)^(3/8)log log H), and the high, translation, constant
calibration and old repair terms are lower order. Every additional
zero-11 field satisfying all temporal identities therefore needs an
xy correction norm at least c sqrt(log H). This excludes the required
uniform O(1) bound regardless of recentering or other matrix entries.
It preserves the old finite identities and does not exclude growing
fields, different rare directions, changed x-second densities or
other laws. Those would be different targets requiring review.
