# Uniform subendpoint sector attempt

Approved target: Attempt a uniform whole-plane theta-sector reduction to
L454's S_{r,m} on 31/32≤m/r≤63/64 with normalized error
O((1+r)^K exp(−κr)) for fixed K,κ>0.

The startup assessment is the saved SPECIALIZE review
[coverage](literature/2026-10-23-subendpoint-theta-sector-reduction-coverage.md).
Its TARGET matches the supplied Next action exactly. The recovery report's
older mismatch does not require changing or reapproving this supplied
assessment. This invocation performs the authorized mathematical attempt.

Main gap: initial low indices and global mixed positivity. Intermediate
target: the complete theta integral with the exact L454 finite sum and
one uniform exponentially small additive error. Downstream use: compare
with audited L454's conditional subexponential lower margin. Continue
only if every mass, clipped patch, moving boundary and sector has a
fixed positive decay rate. Stop this implementation on any unpaid
complete budget; failure of a budget would not sign the integral.

Saved unfinished reasoning: for α=m/r in the approved band, α≥3/4
and α<1. The full positive weights and their clipping tails are
bounded by the α=3/4 weights in L325, retaining its exp(r/24)
mass and exp(−r/200) tail. Tangent-polynomial derivatives remain
uniform because m/r is bounded. The translated power is
(jk)^(−(1+α)/2)≤(jk)^(−7/8), so L325's moving Gaussian
head/tail bound exp(19r/80) still pays for the a^(−1/2)
normalized complement. On the smaller boundary rectangle t≤53/100,
t^(m−ℓ)≤t^(3r/4−ℓ), for ℓ≤2 and sufficiently large r.
The remaining high-strip estimate needs a uniform negative coefficient
of u+v in its global majorant; 1−α≥1/64 supplies it. Uniform
full-square derivative bounds, reflections and normalization still need
to be written before this becomes a complete result.

Inspected duplicates/failures: L326 is the fixed α=3/4 theorem;
L453 has bounded m−r. Neither states this result. L323's r/4
strip obstruction and L327's fixed-band PSD obstruction remain intact;
the present r/20 reduction retains the signed arithmetic sum.
No new external theorem or external premise is required for the sector
reduction itself. Matching Mathlib coverage is not checked.

Completed attempt: the full proof is canonical in
[L455](../lemmas/L455-subendpoint-uniform-whole-plane-theta-reduction.md).
All complete budgets pass with K=2 and κ=1/200, including a
uniform integrable high-strip majorant and the exact reflected
normalization. The result is a local reproduction/specialization,
pending separate critical audit, not an additional sign theorem.
No mathematical script or numerical certificate was needed: the
load-bearing inequalities and error comparisons are analytic in
the canonical proof. The newly selected audit scope remains
REVIEW_REQUIRED; the original ready assessment is unchanged.
