# First-order differential families — 2026-09-25

## Gap, target, and discriminating test

The small-characteristic gap is a useful description of candidates of a
general interpolating differential equation. L007 controls a fixed
derivative fiber, but gives no bound on how many fibers are needed.
The present bounded step tests the simplest extension: polynomial
solutions of a(X)P'+b(X)P=c(X), with a nonzero. The proposed intermediate
target is an exact affine description P_0+g(X)H(X^p), followed by an
agreement bound that accounts for evaluation zeros of g. Such a result
could count a first-order branch without summing over derivative fibers;
coverage of a general nonlinear or higher-order interpolant would still
be unresolved.

L007 proves only the case a=1, b=0. The prior geometric obstruction is
real, and the failed polynomial-in-q transfer supplies no help here.
The existing proofs and failure record contain no general first-order
classification. The [prize page](https://proximityprize.org/) was rechecked on this date: the target
remains epsilon* times the base-field size with only the stated existence
proviso. The pinned source qualifications are retained.

Continue this mechanism if the polynomial kernel has one generator over
F[X^p] and the resulting shortened-code count has a positive explicit
denominator in a useful parameter range. Test loss at zeros of g, rather
than applying L007 to all n coordinates unchanged. A classification
failure, or a sharp example showing that zeros erase the useful range,
would change the subsequent direction. A one-family bound must still be
compared with epsilon* q; it will not locate the original sharp boundary.

## Saved reasoning before the full check

For two nonzero homogeneous solutions U and g, (U/g)'=0 in F(X).
A reduced fraction with derivative zero has numerator and denominator
in F[X^p], by coprimality and the degree drop under differentiation.
Choose a monic homogeneous solution g of minimal degree. It cannot have
a nonconstant factor in F[X^p], since division by that factor preserves
the equation and decreases degree. A reduced constant-field denominator
must divide g, so must be constant. This suggests that the full kernel
is g F[X^p], including an exact degree cutoff after translation.

If d=deg g, e evaluation points are zeros of g, and z of those columns
match the received word, the remaining N=n-e columns should give a
degree-at-most-h RS list with h=floor((k-1-d)/p) and A-z required
agreements. The anticipated denominator is (A-z)^2-(n-e)h. Its uniform
behavior in e and d, the exceptional singleton/empty cases, and useful
extremal examples have not yet been checked at this save point.

## Completed test and assessment

[L008](../lemmas/L008-first-order-differential-families.md) proves the
classification, including empty and singleton fibers. It also proves
rad(g)|a and deg g<=(p-1)deg a. Dividing by g is permitted only after
deleting its evaluation zeros; the reduced agreement requirement is
A-z, rather than A. L007 then gives the exact stated Johnson bound.
If a has no evaluation zeros, the old bound survives or improves.

For arbitrary a, the square identity in L008 gives one uniform sufficient
slack Gamma_p(R)=(1-R)(1-sqrt(1-1/p))/2. At that cutoff the retained
degree rounding makes the denominator at least (n-e)/p, giving M<=pn;
strictly larger slack gives a constant bound. At the common cutoff
Gamma_3(R), the same proof gives M<=3n uniformly over odd characteristic,
so q>=3 epsilon*^(-1)n suffices for one family. This establishes a useful
range without pretending it covers every positive slack or optimizing
each rate. At n=32,k=16,p=3,d=e=12, the denominator at A=k is -4,
so the same inequality supplies no bound there.

The loss of the old constant is real, not just a weak denominator:
the lemma constructs exactly n-k+1 candidates at A=k in a first-order
family with k-1 fixed zero columns. Its n=16,k=8 realization over F_81
has nine candidates, exceeding the fixed derivative-fiber bound of
three. This also supplies the actual full-code lower bound
B_m((n-k)/n)>=n-k+1. Hence epsilon* q>=n-k+1 is necessary for safety
at that radius; it does not approach L001's sufficient binomial bound
closely enough to locate the boundary.

The main test succeeds, so this is ADVANCE with exploration turns 0/3.
The family bound still needs comparison with epsilon* q, and summing
over T families still costs T. There is no controlled cover for a
general interpolant and no complete target candidate. The first
nonlinear first-order equation is the relevant subsequent direction:
reciprocal differences from a particular Riccati solution lead to a
rational linear equation, where pole cancellation must be understood.
This is a reason to test that extension, not an asserted reduction to
polynomial families of the kind just proved.

`python3 scripts/first-order-families/verify.py` passed 5,432 finite
kernel checks, five exhaustive affine-fiber checks, 120 shortened-list
checks over F_9 (including m=2), and 11,430 exact rational-slack checks.
It also constructs the smooth F_81 example and enumerates its 81 scalar
family members, finding exactly nine candidates. The output is retained
in `scripts/first-order-families/results.json`. These tests support the
symbolic proof; they do not enumerate the full prize instance or replace
that proof. Mathlib coverage remains not checked.
