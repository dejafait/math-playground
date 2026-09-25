# Riccati pole cancellation — 2026-09-25

## Gap, target, and discriminating test

The unresolved small-characteristic input is a controlled description of
the polynomial candidates of a general differential interpolant. L008
handles a first-order linear equation, including its fixed evaluation
zeros. This step tests the first nonlinear extension
aP'+bP^2+cP+d=0 with a,b nonzero in odd characteristic. The intermediate
target is an exact condition on the constant-field parameter after
reciprocating the difference from a polynomial solution. A bounded
description could count one nonlinear branch without paying for all
derivative fibers. Coverage of higher-order or other nonlinear
interpolants, and the sharp finite-code boundary, remain separate gaps.

The relevant proofs, recent history, and failed polynomial-in-q transfer
contain no classification of these Riccati polynomial solutions. The
[prize statement](https://proximityprize.org/) was rechecked on this date;
its base-field threshold and existence proviso agree with the frozen
model. The incomplete comparison with the July ABF26 PDF is retained.

Continue if the rational parameter has an explicit polynomiality test
that produces a useful bound independent of q. Test both finite poles
and infinity, since a rational parametrization alone does not control
the polynomial subfamily. If unrestricted cancellation leaves a
field-sized family or a degree-dependent exponential count, record that
limitation and do not call it the polynomial cover needed by C006a.
Compare any obtained count B with epsilon* q for the given field.

## Saved reasoning before the full check

Fix a polynomial solution P_0 and put C_0=2bP_0+c. A nonzero
U=P-P_0 obeys aU'+C_0 U+bU^2=0. Its reciprocal V=1/U therefore
obeys aV'-C_0 V=b. Given a second solution, V_1 is a rational
particular solution; differences from V_1 solve the associated
homogeneous equation. L008's rational-constants argument identifies
ratios of nonzero homogeneous solutions with elements of F(X^p).

Thus a nontrivial rational family has V=V_1+G H with H in F(X^p).
The condition that 1/V is polynomial is exactly that the numerator
of V in lowest terms is a nonzero constant; the degree cutoff must
also be imposed. This observation alone is not a family-counting
bound. The outstanding test is whether cancellation can be encoded
by divisors of a fixed polynomial, or otherwise bounded, without
discarding inseparable factors or ignoring the pole at infinity.

## Saved divisor reduction and obstruction candidate

If the rational homogeneous equation has a nonzero solution, clearing
its denominator by a pth power gives a polynomial one. Let g be its
minimal monic generator from L008, put D=P_1-P_0, phi=Dg, and W=D^2g.
Then a phi'=-bW, so phi' is nonzero. Write H=M/N in reduced form
with M,N in F[X^p]. The denominator before reduction is
T=N+phi M, and U=DN/T. Since gcd(T,M)=1, polynomiality implies
T divides W. Conversely T divides W implies U=D-(W/T)M is polynomial.
After making T monic, differentiation forces M=T'/phi' and
N=T-phi M. Thus each divisor gives at most one candidate, subject to
M,N being derivative constants, being coprime, N nonzero, and the
original degree cutoff. These conditions and exceptional cases still
need a full check.

A possible obstruction to polynomial unfiltered counts is
A=X^(p^s)-X and A P'+P^2+P=0. For every F_p-subspace V of F_(p^s),
its vanishing polynomial H_V is linearized, so H_V' is a nonzero
constant and H_V''=0. The polynomial P_V=A H_V'/H_V appears to solve
the equation, with degree p^s-|V|. Distinct V give distinct zero sets.
There are at least p^(floor(s/2) ceil(s/2)) such subspaces. The full
identity, degree comparison, and finite enumeration are not yet checked
at this save point. This would obstruct only a polynomial bound on all
solutions, not the agreement-filtered list or the prize threshold.

## Completed test and assessment

[L009](../lemmas/L009-riccati-divisors-and-unfiltered-counts.md) proves
the full divisor parametrization, including the case of a zero rational
homogeneous kernel, polynomiality at all finite places, and the degree
cutoff at infinity. Distinct admissible monic divisors give distinct
solutions. One divisor is excluded by N=0, so the total count, including
P_0, is at most tau_F(W), bounded by
2^(2(k-1)+(p-1)deg a). This is independent of q but exponential in n
when p is fixed and deg a,k=O(n). Using it in m rows still requires
B^m<=epsilon* q. It does not yield the sought polynomial field condition.

The same lemma proves the obstruction family, with its identities and
subspace count supplied in full. Its number of solutions exceeds every
fixed power of n even when message dimensions and domain sizes have
the pinned form over suitable extensions. Thus the weak divisor bound
cannot be repaired into a polynomial unfiltered count for this whole
class. The example does not give k agreements with one received word,
and extension fields are not a license to alter a specified instance.

The outcome is NEGATIVE, with exploration turns 0/3: the new example
changes the route decision, rather than merely repeating a prior stop.
The discarded proposal is preserved in the
[attempt record](../ATTEMPTS/002-riccati-unfiltered-polynomial-count.md).
The classification remains a useful exact restriction, but a filtered
count is required. Pairwise differences still obey first-order linear
equations, so multiplicities away from zeros of a provide a specific
reason to investigate weighted agreement counting. That bound is not
proved in this step. No complete target candidate appeared.

`python3 scripts/riccati-families/verify.py` passed 17 exhaustive cases
(35,531 polynomials), 4,309 monic-divisor tests, and 56 recovered
rational parameters. It also checked 84 distinct subspace solutions
in F_9 and F_81, including their degrees and values at all subfield
points. The finite output is in `scripts/riccati-families/results.json`.
These checks support the informal proof; they do not establish a list
boundary. Mathlib coverage remains not checked.
