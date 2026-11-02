# Joint angular moment test — inconclusive finite search

The joint projection remains reduced to its first-M spatial moments by
[L651](../lemmas/L651-joint-polynomial-dual-uniform-gram-bound.md).
The new finite calculations and their full limitations are in
[the working record](../drafts/2026-11-02-joint-angular-moments-working.md)
and the three `scripts/one-sided-hankel/joint-angular-*.json` diagnostics.
No new lemma or certified rate is asserted.

WHY IT FAILS: Centered and shifted Chebyshev screens and a bounded
unit-residue pole-location descent did not produce a uniform estimate
or an admissible asymptotic countersequence. The largest sampled loss
rate after descent was about 0.048013, below the permitted 1/16, but
finite samples cannot decide the inequality's unknown constant and
onset. Both descents reached their iteration caps with large gradients;
rounding and quadrature were not enclosed. Thus neither a global
minimum nor even convergence is claimed. This stops this screen batch,
not the joint projection or RH. The refined continuation tests a
P-dependent reflected-weight polynomial remainder with its entire norm;
the earlier untruncated-reflection, exact-recovery and polewise stops
remain preserved with their own qualifications.
