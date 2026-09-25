# Frobenius agreement filter — 2026-09-25

## Gap, intermediate target, and discriminating test

The all-field fixed-slack gap remains: L006 constructs an interpolant in
every characteristic, but L005's bounded-dimensional cover fails when
the message degree reaches the characteristic. Its explicit obstruction
is Q=Y_1, whose solutions are P(X)=H(X^p). This step tests whether agreement
filtering can control that family even though its dimension grows with n.
It does not propose a cover for arbitrary differential equations.

The required instructions, full overview, DAG, existing changes, L001,
L005, relevant audits, and the failed q-polynomial transfer were read.
No local result yet analyzes the agreement-filtered Frobenius family.
The [prize statement](https://proximityprize.org/) was rechecked on
September 25: the base-field threshold, four rates, and field-existence
proviso are unchanged. The pinned model and incomplete ABF comparison
remain as recorded in foundations/02-pinned-list-model.md.

Target: identify the filtered family with a lower-degree RS list, and
prove an explicit bound independent of q, preferably directly for
simultaneous interleaving. A plausible use is to count candidates inside
Frobenius fibers in a future small-characteristic solution description.
Producing such a description for general Q, accounting for its number
of fibers, meeting epsilon* q for a given field, and finding the sharp
boundary are separate unresolved steps.

The discriminating test is positivity of the pairwise-counting
denominator at A=k+ceil(gamma n) agreements, for each pinned rate and
admissible characteristic. Continue this mechanism in regimes with a
uniform polynomial bound. Where the denominator is nonpositive, record
the exact limitation without interpreting it as a large-list witness.
The already known geometric dimension obstruction alone is not new
negative evidence for agreement filtering.

## Saved working argument

Put h=floor((k-1)/p). Frobenius is injective on a field, so the points
x_i^p are distinct. The map H -> H(X^p) identifies the kernel of the
first Hasse derivative in degree less than k with polynomials of degree
at most h on those new points. Two distinct polynomial tuples in this
family agree in at most h columns. An affine translate of the family
has the same property after translating the center.

For a list of M tuples, choose exactly A agreeing columns per tuple.
If l_i counts their incidences at column i, then sum l_i=MA and
sum l_i(l_i-1)<=M(M-1)h. Cauchy--Schwarz suggests

\[
 M(A^2-nh)\le n(A-h).
\]

Thus a positive denominator should yield the explicit list bound
floor(n(A-h)/(A^2-nh)), with no power of the interleaving width.
The exact finite-n inequality must be kept; the limiting condition is
(R+gamma)^2>R/p. At the pinned power-of-two smooth domains,
characteristic two is excluded by n dividing q-1. Boundary rounding,
the four rate regimes, and the comparison with epsilon* q were pending
at this save point. The completed checks follow below.

## Completed test and scope

[L007](../lemmas/L007-frobenius-fiber-agreement-bound.md) proves the
reduction and count, including all affine translates and arbitrary
interleaving width. At A=k, the sharper integer bound is
ceil(s(p-1)/(p-s))-1 for R=1/s and p>s. The uniform bounds at the four
rates are 3, 15, 26, and 255 for p>=3,5,11,17, respectively. This is a
bound for a fixed derivative fiber, not for the original full code.

For the smaller admissible primes, the limiting sufficient slack is
gamma_c=sqrt(R/p)-R. Retaining h<=((k-1)/p) shows that equality gives
A^2-nh>=n/p and hence M<=pn; a strictly larger slack gives a constant
bound. Below the cutoff, the denominator is eventually negative. This
only stops use of that second-moment inequality in that regime, not
all agreement counting or the research route. At finite n the exact
integer cutoff is floor(sqrt(nh))+1 agreements. For p=3,n=16,k=4 in
F_81, it fails at four agreements but gives M<=7 at five agreements;
these are bounds, not computed exact list sizes.

The exact arithmetic script
`python3 scripts/frobenius-filter/verify.py` passed 252 cutoff checks,
171 strict-bound checks, and 81 equality-slack rounding checks on
n=16,...,4096 at its seven stated odd primes. Its retained output is
`scripts/frobenius-filter/results.json`. The proof is symbolic;
neither codeword enumeration nor a general theorem was inferred from
these finite checks. Mathlib coverage is not checked.

## Threshold comparison and assessment

If J is the bound in L007, this family's contribution is below the
required threshold only when J<=epsilon* q. A union of T such families
would give T J; controlling T for a general differential equation is
not supplied. In particular, the result cannot be substituted for the
large-characteristic cover in C006a. The geometric obstruction itself
remains true: a family can have large algebraic dimension while its
agreement-filtered portion is small in the proved regimes.

This is ADVANCE, with the exploration streak reset to 0/3, because it
establishes a new applicable bound on the specified obstruction and
its precise limitations. The reason for the subsequent direction is
to move from a fixed derivative fiber to a variable-coefficient linear
differential equation, where any common polynomial factor and its
evaluation zeros may change the agreement count. No result for that
extension or complete candidate for the challenge is asserted here.
