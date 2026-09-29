# Endpoint fourth moment via rational-grid bounds — 2026-09-27

The approved target was M_N(N^(-1/8))=o(1), using the sufficient
complete weighted fourth-moment estimate o(N^(-1/2)) at dilation 1.
The [prior assessment](../drafts/literature/2026-09-26-current-target.md)
had decision EXPLORE. The missing deterministic sampling bound could
give a vanishing discrete relative mean through L350–L351, while
exceptional indices, the pointwise endpoint margin and lower Laguerre
signs would remain unresolved.

The tested implementation imports Guth–Maynard Lemma 11.6, retains
the actual maximum weights, groups every ratio collision, and transfers
unweighted grid bounds by the largest coefficient on each rectangle.
Unequal scales are handled by a finite Cauchy–Schwarz identity. The
stopping test is the resulting full normalized budget, with all tails
included. This differs from L344–L345's fixed-order derivative bounds
and L347–L348's earlier divergent coefficient mass.

Result: **NEGATIVE; RESEARCH; REPRODUCTION**.
[L352](../lemmas/L352-endpoint-fourth-moment-grid-budget-obstruction.md)
proves a weight tail O(N^(-4)) beyond
exp(32 sqrt(N) log N), exact minimal sample energy, and a budget
tending to one for this implementation. The full proof also covers
unequal numerator/denominator scales and arbitrary sample partitions
combined by the L⁴ triangle inequality. The actual fourth moment
is neither bounded below nor refuted by this result.

## WHY IT FAILS

The imported height-dependent term exceeds the trivial grid budget
uniformly throughout the range carrying almost all the weight, even
with minimal additive energy and with its additional T^ε loss
formally removed. Taking the maximum coefficient on each rectangle
therefore gains nothing over |C_N|≤1. Its normalized off-diagonal
cost tends to one, while o(N^(-1/2)) is required. The canonical
proof is L352; this is a failure of the specified upper-bound
certificate rather than evidence that the desired moment is large.

Stop this implementation. A distinct possibility is to estimate the
sampled Mellin–Euler expressions jointly while retaining their signed,
moving coefficients; it needs a separate literature review. The
earlier absolute Abel and fixed-order derivative failures must be
compared in that review. No global research ban, sign extension,
or RH candidate follows.

The [saved work](../drafts/2026-09-27-weighted-fourth-grid-budget.md)
preserves the intermediate reasoning. Finite formal-frequency checks
validate the collision and four-sample identities and toy energy counts;
the asymptotic tail and scale comparisons are proved analytically.
This is a local specialization of an imported theorem and elementary
inequalities, with no claim of progress beyond known mathematics.
