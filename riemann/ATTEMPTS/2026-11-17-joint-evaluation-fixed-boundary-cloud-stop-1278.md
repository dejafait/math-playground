# Joint evaluations: fixed boundary clouds stopped1278

17 November2026. The approved simultaneous-evaluation attempt produced
the exact range kernel and tested z_j=i*tau+epsilon*w_j for fixed real
tau and finitely many fixed distinct right-half-plane w_j. The full
proof, including boundary common zeros and singular finite systems,
is in [C032g](../lemmas/C032g-joint-evaluation-kernel-and-fixed-boundary-cloud-stop.md).
Its new result is pending independent audit. The required discriminator
was incompatibility or minimum preimage norms tending to infinity;
the actual minimum squared norms tend to zero at rate O(epsilon).

WHY IT FAILS: Distinct ordinary evaluations away from common zeros
have independent exponential representers and hence a solvable finite
system. At a boundary common zero, theta evenness and conjugation force
F and F' to vanish together at the shifted point; R then has the same
vanishing order as both coefficients. After factoring these orders,
the joint Gram matrix is a fixed positive Cauchy matrix with its explicit
epsilon scale. The minimum norm therefore decreases rather than
diverges. This defeats the specified finite boundary-cloud mechanism,
not the full RKHS criterion or the actual membership equation.

Park this family. Reopening requires a materially different controlled
input, such as an actual interior common-zero obstruction or quantitative
estimates for growing/degenerating clouds; neither is established or
approved here. No norm cap may be invented. A separate conceptual audit
of this negative result is nominated; no further membership search is
scheduled on the basis of the reformulation alone. Preserve stops1272,
1273 and1276. Source metric, the C032f reduction audit, universal range
inclusion, delta, all-degree signing and the actual-Xi bridge stay open.

Audit update1280, 17 November2026: the independent conceptual audit in
C032g accepts this fixed-family stop. It checks every finite boundary
common-zero multiplicity, singular compatibility and the complete
complex kernel convention, and records an explicit perturbation
threshold and O(epsilon^2) squared-norm remainder bound. The conclusion
is unchanged: O(epsilon) tends to zero, whereas nonmembership by this
test required incompatibility or divergence. There is no growing-cloud
or global-membership claim. Park this family after the audit; no further
source approval or replay of this same stop is nominated. The separate
C032f bounded-core/range equivalence remains an independent correctness
gap, not a new witness test or a decision on delta.
