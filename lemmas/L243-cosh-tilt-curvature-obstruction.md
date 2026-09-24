# Lemma 243: curvature obstruction for the cosh-tilted theta variance test

**Hypotheses.** Use K and its smooth even extension from L048, and p_x, a_x, b_x from L242 on u≥0. Put W(u)=−log K(u), c=W″(0), and V_x(u)=−log p_x(u). Spatial derivatives below are with respect to u, not x.

**Conclusion.** The constant c is finite and c>(68/125)π>0. For x≥0,

V_x″(u)=W″(u)−x sech²(√x u).

For every x>c, V_x″ is negative on a nonempty interval of positive p_x measure next to zero. Thus positive curvature of this tilted potential cannot hold uniformly in x. At x=0 curvature is positive everywhere, but the proposed pointwise comparison

(a_0′(u))²/V_0″(u) ≤ −b_0(u)

fails throughout a sufficiently small interval 0<u<δ. Indeed the ratio of its left side to its right side is 6/(u²W″(u)), which tends to infinity.

These statements obstruct a positive-curvature inverse-curvature variance estimate followed by pointwise domination. They do not refute an integrated variance inequality or any other integration-by-parts method.

**Proof.** L048 gives smoothness, positivity, and W″(u)>(68/125)πe^{2|u|}; in particular c is finite and strictly positive. Normalization contributes only a constant in u, so

V_x(u)=W(u)−log cosh(√x u)+log F(x).

Two spatial derivatives give the formula, including x=0 by continuity. At zero this is c−x. For fixed x>c continuity gives δ>0 with V_x″<0 on [0,δ). Since p_x is strictly positive there, the interval (0,δ) has positive probability. This is an interior failure, not just an endpoint defect.

At x=0, L242 gives a_0=u²/2 and b_0=−u⁴/6. Hence the proposed inverse-curvature integrand is u²/W″(u), whereas the target is u⁴/6. Their ratio on u>0 is exactly 6/(u²W″(u)). Smoothness gives W″(u)→c>0, proving divergence and strict failure on a small positive interval. All quantities in this comparison are integrable at x=0: 1/W″ is bounded by 125/(68π), and the theta density has all polynomial moments by L242. Thus this failure concerns strength of a proposed comparison, not divergent expectations. ∎

For clarity, the screened mechanism would first establish Var_x(a_x)≤E_x[(a_x′)²/V_x″] using a positive-curvature variance argument, then dominate that expectation by −E_x[b_x] pointwise. No such variance theorem is needed or asserted for the nonconvex densities here. The necessary first-sign threshold remains Var_x(a_x)≤−E_x[b_x]; the local failures above do not determine the sign of the difference of those integrated quantities. Even that threshold would not give a positive Stieltjes measure or every mixed reciprocal-node form.

**Mathlib.** Not checked: coverage of the full statement and supporting differentiation results was not checked. No matching theorem is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
