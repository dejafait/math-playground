# Corollary 465a: unconditional common-height Xi tail

## Hypotheses

Let Ξ be the actual entire completion used in L464 and L465, with
their common convention

    Ξ(t+iy)Ξ(t−iy)=Σ_(p≥0) D_p(Ξ;t)y^(2p).

Fix c_0>1/2. All logarithms are natural, t is real and positive,
and p is a nonnegative integer. Use the unconditional conclusions
of L464 and L465 with their stated uniformity. No additional
zero-free half-plane, simplicity or central nonvanishing is assumed.

## Conclusion

There exists T(c_0)≥2 such that for every real t≥T(c_0) and every
integer p satisfying 2p≥c_0 log(t/(2π)), we have D_p(Ξ;t)>0.
Equivalently, all p≥ceil((c_0/2)log(t/(2π))) are covered, with no
upper order cutoff. Central zeros of any multiplicity are allowed.

This reproduces bramble_trace, *Generalized Laguerre positivity at
growing orders*, [paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
displayed v4, 24 October 2026 07:18 UTC, Theorem 1a (4a), using
the first paragraph of Section 4.4 with A=2. The assembly is written
out to check common onset and integer endpoints from audited inputs,
not to claim a result beyond that source. No numerical onset,
endpoint c_0=1/2, arbitrary-order Hardy theorem, initial-sign theorem,
global mixed positivity or RH resolution follows.

## Proof

Fix c_0 first. L465 supplies T_A(c_0) such that, simultaneously
over all permitted integer orders and every t≥T_A(c_0),

    D_p(Ξ;t)>0 when c_0 ell≤2p≤ell³,
    ell=log(t/(2π)).

Its onset depends only on c_0 after its arc angle is fixed; it is
not a separate onset for each p. L464 supplies one absolute C>0
such that, simultaneously over every t≥2 and integer p,

    D_p(Ξ;t)>0 when p≥C L²,  L=log(t+2).

Set

    A=log(2π+2),  E=max(1,A,8C,sqrt(c_0)),
    T(c_0)=max(2,T_A(c_0),2π exp(E)).

This is a finite existential choice; C and T_A have not been
numerically evaluated. For all t≥T(c_0), t≥2π and ell≥E, hence

    L−ell=log(2π(1+2/t))≤log(2π+2)=A≤ell,
    C L²≤4C ell²≤ell³/2.                         (1)

Also ell²≥c_0, so the analytic interval's lower endpoint is no
larger than its upper endpoint. These conditions hold at every
height above this same T(c_0).

Let p be any allowed integer. If 2p≤ell³, its lower bound and
L465 give the sign. If 2p>ell³, then p>ell³/2≥C L² by (1),
so L464 gives the sign, with no upper restriction on p.

For the integer endpoints, put m=ceil(c_0 ell/2) and
k=floor(ell³/2). Every integer m≤p≤k belongs to the analytic
case, including either real endpoint whenever it is an integer.
Every integer p≥k+1 satisfies p>ell³/2 and belongs to the
product case. If the first integer interval is empty, every
allowed p belongs to the second case. There is therefore no
rounding gap. Equality 2p=ell³ is covered by L465's inclusive
upper endpoint. L464 also allows equality p=C L².

Both inputs concern precisely the same coefficient. In L465,
n=2p and the Xi formula is the coefficient of y^(2p), with its
positive factor b(t)² retained. In L464, x=y² makes coefficient
p in x equal coefficient 2p in y, multiplied by a positive C_t.
Thus there is no factorial, sign or Xi-normalization conversion.
L465 does not divide by Ξ(t), and L464 keeps its scalar positive
at central zeros, retaining near zero factors in a monic polynomial.
Neither nonvanishing nor simplicity at the center is required. ∎

This uses the two input audits rather than assuming the whole
manuscript correct. Their analytic and product proofs are not
repeated. Signs below ceil(c_0 ell/2), effective bounded-height
overlap and all-degree mixed positivity remain unresolved.

## Mathlib

Full matching coverage and supporting formalizations have not been
checked. Availability is unknown; no absence claim or formal
verification is made. This informal assembly uses L464 and L465
and elementary logarithmic comparison and floor/ceiling properties.
