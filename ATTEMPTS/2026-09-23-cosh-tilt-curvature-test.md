# Cosh-tilted theta curvature test

Date: 2026-09-23

The main gap remains all-degree actual reciprocal-node mixed positivity. The intermediate target is L242's integrated first-sign bound Var_x(a_x)≤−E_x[b_x] for every x≥0. It is a necessary diagnostic for the proposed positive Stieltjes representation, which would supply mixed positivity; higher derivative signs and the measure itself would remain unresolved even after success. The concrete test was positive curvature of the tilted density followed by domination of the inverse-curvature variance integrand. Continue this mechanism if those hypotheses and the required comparison hold uniformly; abandon it if either has an actual-theta obstruction.

Redundancy screen: L047–L048 establish curvature of the untilted kernel only. L046 explains variance in sums, and L242 rules out the direct double-integrand sign. None computes the curvature after the cosh tilt or compares the proposed inverse-curvature integrand with its required target. The prior stops remain evidence, not global bans.

[L243](../lemmas/L243-cosh-tilt-curvature-obstruction.md) proves two exact obstructions without numerical approximation: the tilt destroys convexity near zero whenever x>W″(0), and even at x=0 the proposed pointwise comparison misses its target by a ratio tending to infinity near zero.

**WHY IT FAILS.** Strict log-concavity of K does not survive arbitrarily large cosh tilts: their positive logarithmic curvature at zero equals x. At zero tilt, positive curvature alone yields a candidate integrand of order u², while the required negative term has order u⁴. These failures stop the specified positive-curvature plus pointwise-comparison proof, but do not disprove the integrated bound; small regions can be outweighed elsewhere. No negative actual mixed form or RH counterexample is obtained.

Decision: stop this mechanism. A distinct representation uses the whole-line exponential tilt K(u)e^{ru}, which preserves the curvature of W. The next diagnostic is whether its mean m(r) and variance satisfy r Var_r(u)≤m(r); this is the same first-sign threshold in a representation without the cosh curvature defect. It is not established here. One bounded test resolved as NEGATIVE; zero consecutive unresolved exploration turns. No candidate.
