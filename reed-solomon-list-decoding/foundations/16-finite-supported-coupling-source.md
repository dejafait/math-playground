# Finite supported coupling — primary source

## Hypotheses

A and B are finite sets, P and Q probability measures on them, and
R is any subset of A times B. Disjoint tagged copies may be used.
There is no independence assumption or positivity requirement on every
atom, and R need not be an order relation.

## Conclusion

A coupling with these marginals and mass one on R exists exactly when
P(U) <= Q(N_R(U)) for every U subset A, where N_R(U) consists of the
B-neighbors of U in R. Equivalently there are nonnegative weights on
allowed pairs with the prescribed row and column sums.

## Proof

Import Twan Koperberg, *Couplings and Matchings: Combinatorial notes on
Strassen’s theorem*, [arXiv:2202.02092v1](https://arxiv.org/pdf/2202.02092v1),
4 February 2022, Theorem 1, p. 2; Proposition 4, pp. 5–6.
The inspected proof passes through a spanning forest and removes leaves
with their incident mass. Lemma 3, pp. 3–4, splits tight subsets or
transfers weight until a tight subset/removable vertex occurs. No reproof
is needed. The v1 Lemma 3 statement prints w(B)=w(B); use the explicit
equal-side-weight hypothesis of Proposition 4. Theorem 1 has probability
mass one on both sides. No computational efficiency for implicit states
is asserted here.

## Mathlib

Full matching finite supported-coupling theorem: not checked.
Unknown availability is not evidence of absence. This source gives no
RS theorem and no verdict for L030’s specific two-core laws.
