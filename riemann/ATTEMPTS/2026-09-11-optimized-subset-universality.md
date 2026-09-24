# Optimized subset criteria are not universal — 2026-09-11

Outcome: [Lemma 98](../lemmas/L098-consecutive-packets-obstruct-optimized-subset-criteria.md)
constructs permitted coordinates where every-block optimized ratios
diverge and their dyadic inverses are summable, even with divergent suffix
weights and zero lower density.

WHY IT FAILS: Selecting fewer points inside a short consecutive packet
reduces crowding but also reduces the averaging denominator. A rank-gap
Cauchy estimate forces their quotient to retain a logarithmic loss for
every subset. Thus optimization cannot make either sufficient criterion
of Lemma 96 universal. This is a failure of these bounds only: actual
coordinate gaps beyond packet endpoints may still give small near sums,
and no counterexample to the unrestricted subsequence assertion follows.
