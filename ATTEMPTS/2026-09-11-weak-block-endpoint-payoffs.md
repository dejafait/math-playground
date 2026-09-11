# Endpoint-only payoffs for weakly separated blocks — 2026-09-11

Tested extending the separated-block construction by keeping its
nondecreasing unbounded component constant on each block and adding a
bounded nondecreasing correction, under b_j≤2a_j and a_(j+1)≥b_j+2.
The precise obstruction is proved in [Lemma 116](../lemmas/L116-weak-blocks-obstruct-endpoint-only-payoffs.md).

WHY IT FAILS: With dyadic blocks and summable large masses at their left
endpoints, the distance-two transition from a preceding block endpoint
bounds each interblock payoff increase by a summable reciprocal mass.
An unbounded payoff must therefore accumulate infinite increase inside
blocks. A bounded correction cannot supply that increase. The same
example admits a payoff by the lacunary-mass theorem, so this failure
concerns only the endpoint-only construction, not payoff existence or RH.
