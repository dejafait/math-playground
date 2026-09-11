# Lemma 85: obstruction to height-normalized suffix minima

**Hypotheses.** For n≥1 set

x_n=sqrt(n) log(n+2),   b_n=1−1/log(n+2),   H=1,
h_n=H−b_n.

For any positive sequence q define its selected indices by

S(q)={n≥1: x_j/q_j≥x_n/q_n for every j≥n}.

**Conclusion.** The coordinates are strictly increasing and satisfy
Σ x_n^{-2}<∞; the heights are positive, strictly increasing, and tend
to H. Nevertheless:

1. h_n n²/x_n²→∞, so this quantity cannot tend to zero on any
   unbounded set of indices.
2. For the positive, strictly increasing normalization q_n=n sqrt(h_n),
   one has S(q)=∅.
3. More generally S(q)=∅ for every positive normalization satisfying
   q_n≥c n sqrt(h_n) eventually, for any fixed c>0. No monotonicity
   hypothesis on this more general q is needed.

## Proof

Both sqrt(n) and log(n+2) are positive and strictly increasing, so their
product is strictly increasing. For n≥2,

x_n^{-2}=1/[n log²(n+2)]≤1/[n log² n].

The latter series converges by the integral test: its positive
integrand is decreasing on [2,∞), and substitution u=log t gives
∫_2^∞ dt/[t log² t]=1/log 2. The first term is finite.
Since log 3>1, the heights are positive. Strict growth and convergence
to 1 follow directly from growth and divergence of log(n+2).

Exact substitution gives

h_n n²/x_n²=n/log³(n+2).

This tends to infinity. For completeness, put t=log(n+2), so n=e^t−2;
the exponential series gives e^t≥t⁴/24 for t>0, whence
(e^t−2)/t³≥t/24−2/t³→∞. The same limit holds along every unbounded
set of indices, proving the first assertion.

For q_n=n/sqrt(log(n+2)), positivity is immediate. The logarithmic
derivative of its real-variable extension on [1,∞) is

1/t − 1/[2(t+2)log(t+2)] > 0,

because 2(t+2)log(t+2)>t. Thus q is strictly increasing. Moreover

x_n/q_n=log^(3/2)(n+2)/sqrt(n)→0

by the preceding divergence. A positive sequence tending to zero has
no index at which a minimum over the entire suffix is attained:
for each n its value is positive, and some later value is less than
half that value. Applying this fact to x_n/q_n proves S(q)=∅.

Finally, under the more general eventual lower bound,

0<x_n/q_n≤c^{-1}log^(3/2)(n+2)/sqrt(n)→0.

Finitely many indices preceding the lower bound do not affect this
limit. The same positive-sequence argument excludes every index,
including those finitely many initial indices. This proves assertion 3. ∎

## Qualifications and consequence for the selection argument

The normalization n sqrt(h_n) is suggested by the exact identity
h_n n²/x_n²=(n sqrt(h_n)/x_n)². The hypotheses for the unrestricted
monotone quartet question therefore do not ensure suffix-minimum
attainment for this normalization, or any normalization eventually
bounded below by its positive constant multiple. The example also
shows that changing the selected indices alone cannot force the
sufficient height-tail condition of Lemma 84: that condition fails
along every unbounded set in this example.

These are obstructions to a specified proof method, not a counterexample
to full upward liminf zero. A divergent upper bound says nothing about
divergence of the quantity it bounds. Normalizations outside the stated
class, estimates retaining b_j−b_n in place of h_n, and other selection
arguments remain open here. In particular this lemma does not assert
that every height-dependent normalization fails. No product property,
theta assertion, or RH conclusion is used or proved.

## Verification and formalization obligations

This is an analytic counterexample requiring no numerical certificate.
Verify the integral comparison, the exponential lower bound, positivity
of the derivative, and the quantifiers excluding every suffix minimum.
The mention of Lemma 84 explains the obstructed method; its result is
not an input to this proof. All assertions above follow from the explicit
sequences and elementary calculus.
