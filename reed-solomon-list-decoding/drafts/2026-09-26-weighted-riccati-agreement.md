# Weighted Riccati agreement — 2026-09-26

## Gap, target, and discriminating test

Small-characteristic nonlinear interpolants still lack a useful filtered
list estimate or controlled cover. L009 rules out a polynomial count of
all Riccati polynomial solutions; L007–L008 only count particular linear
families. This step tests pairwise differences directly for
aP'+bP^2+cP+d=0, retaining simultaneous column agreement. The intermediate
target is a field-independent bound in terms of the number e of evaluation
zeros of a. A useful bound could control one nonlinear branch without
counting its derivative fibers. A cover of a general interpolant, control
of e for the resulting equations, the sharp finite-code boundary, and the
July ABF26 comparison remain separate unresolved steps.

The overview, DAG, relevant proofs, existing changes, recent history, and
failure records were inspected. No earlier lemma gives this weighted
count. The earlier unfiltered-count failure is preserved. The
[prize page](https://proximityprize.org/) was rechecked on 2026-09-26;
its threshold remains epsilon* times the base-field size, with only the
field-existence proviso. The pinned model and incomplete ABF comparison
remain qualified.

Continue if multiplicity gives a polynomial or constant filtered bound
with an explicit cutoff that improves the ordinary pairwise root bound
when e is controlled. Test its behavior at e=0, e=n, and on L009's raw
subspace family on a smooth domain. If the coefficient-zero cost removes
the improvement, record that regime rather than claiming a general
small-characteristic bound. Compare the resulting J with epsilon* q;
there is no license to enlarge a given field.

## Saved reasoning before the full check

For distinct scalar solutions P,Q, U=P-Q satisfies
aU'+(b(P+Q)+c)U=0. At an evaluation root x of U with a(x) nonzero,
the order of U must be divisible by p: otherwise the derivative term has
strictly smaller order than the other term. Hence a pair of distinct
tuples has at most k-1 common-root multiplicity when charging p for
regular columns and 1 for zeros of a. A differing row witnesses this
bound, so no power depending on the interleaving width is needed.

Choose exactly A agreeing columns per tuple, and write l_i for their
incidences. With w_i=p or 1, inverse-weight Cauchy gives
sum_i w_i l_i^2 >= (M A)^2 / (e+(n-e)/p).
The pair term is at most M(M-1)(k-1). The diagonal term is at most
M W_A, where W_A=p A-(p-1)max(0,A-(n-e)). Thus the proposed bound is

M <= floor(V (W_A-(k-1)) / (p A^2-V(k-1))),
V=n+(p-1)e,

provided its denominator is positive. This calculation still needs the
full edge-case and rounding check. At e=0 it has the derivative-fiber
cutoff; at e=n it becomes the ordinary Johnson count. L009's example
a=X^(p^s)-X on a multiplicative subgroup of order n has
e=gcd(n,p^s-1), which can be far smaller than deg a. This is a concrete
test of whether the previous raw-solution obstruction survives filtering.

## Completed test and assessment

[L010](../lemmas/L010-weighted-riccati-agreement.md) proves the proposed
bound, including all-exceptional and zero-exceptional limits, the helpful
k-1 correction at the limiting slack, and a uniform choice of weight 3
in odd characteristic. Its real positivity cutoff is lower than the ordinary
Johnson cutoff when e<n and k>1, though it does not determine a sharp list
boundary. When eta in L010 is nonnegative it gives M<=pn, so the additional sufficient
field condition for the family is q>=epsilon*^(-1)pn. Containment of an
entire RS list in that family remains unproved.

For p=3, odd s>=3, Q=3^s, and n=2k with k the least power of two at
least Q, the old subspace equation has exactly e=2 exceptional points on
any multiplicative domain of order n in a compatible field. The bound
gives at most four candidates at k agreements, although the unfiltered
scalar set has at least 3^((s^2-1)/4) elements. This is a concrete success
of filtering against the previous obstruction, not an extrapolation
from finite experiments. Safety of this contribution still needs
4<=epsilon* q for the specified field.

The exact checks enumerated 7,290 polynomials and 20,977 center agreement
patterns, including a two-row case. They tested 321 tuple pairs, one
regular root of order p, 45,815 positive-denominator list inequalities,
41,160 all-exceptional specializations, and ten smooth-domain parameter
instances. The proof, not these finite checks, establishes the general
claim; [results](../scripts/weighted-riccati/results.json) retain the
finite evidence. Mathlib coverage remains not checked.

The outcome is ADVANCE, with exploration turns 0/3, because a new
conditional nonlinear filtered bound and an infinite-family application
are established. At e=n the same method gives only the ordinary Johnson
bound. The remaining cost is the weight 1 assigned to every exceptional
column. Two candidates agreeing with the same center share more local
data there than an arbitrary pair of solutions; that is the reason to
investigate center-dependent multiplicities at those points. No bound of
that kind is asserted here, and no complete target candidate appeared.
