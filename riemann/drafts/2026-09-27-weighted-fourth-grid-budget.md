# Saved work: weighted endpoint fourth-moment test

The approved target is the exact Next action in
[the prior assessment](literature/2026-09-26-current-target.md).
The gap is deterministic sampling at dilation 1. The sufficient moment
threshold is o(N^(-1/2)); success would imply the concentration condition
in L351, leaving exceptional indices and the endpoint sign margin open.

The shared rules, local overview and DAG, existing changes, L349–L351,
and the relevant L344–L345 obstruction statements were read. The prior
EXPLORE assessment is being reused. Guth–Maynard Lemma 11.6 is imported
by citation; its unweighted proof is not being repeated.

Saved intermediate reasoning before completing the proof:

- Group the positive pair weights as L351's c_N(k,l). This retains every
  ratio collision and expresses the fourth moment as a weighted rational
  grid sum. The exact collision mass is B_N/W_N²=O(1/N).
- The existing d_4 majorant should bound the weight outside k,l≤X_N by
  O(N^(-4)), with X_N the next power of two above
  exp(32 sqrt(N) log N). Use half of the exponent excess for the tail.
- The actual a_n grow by a factor exceeding exp(4). The sample additive
  energy at tolerance 1 should therefore be exactly 2N²−N. The same
  assertion holds for every subset of samples.
- Expand a rectangular unweighted fourth moment in four sample indices.
  Cauchy–Schwarz bounds it by the geometric mean of the two square-grid
  fourth moments. This handles unequal numerator and denominator scales.
- Even with minimal energy, the imported height term exceeds the trivial
  square-grid budget uniformly for grids through X_N. A maximum-coefficient
  transfer would then return the entire retained weight. Every sample
  subset containing two points still has diameter at least c exp(4N),
  so ordinary sample partitioning may not repair this particular bound.

These statements are pending a full written check. The intended stopping
test is the complete resulting certificate, not the actual fourth moment:
if its normalized retained-weight cost tends to one, stop this grid/maximum
transfer. This would not refute the moment target or RH. It would be a
local application and limitation of an imported estimate, with no novelty
claim. The theorem's T^ε factor must not be replaced by N^ε.

Completed check — 2026-09-27: all five intermediate statements are
proved in [L352](../lemmas/L352-endpoint-fourth-moment-grid-budget-obstruction.md).
The complete specified certificate tends to one, including the exact
collision term and the O(N^(-4)) tail. The obstruction also survives
arbitrary sample subsets combined by the L⁴ triangle inequality.
This is an informative NEGATIVE result for that implementation; the
actual fourth moment and sampling condition remain open. The imported
theorem was used by citation, with local specialization recorded as
REPRODUCTION and no claim of mathematical novelty.
