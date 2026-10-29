# C110a — Descent for the two-peak first-drop family with one intervening even step

## Hypotheses

Let T be the shortcut Collatz map on positive integers:
T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n. Let n>1 be
an integer with actual finite parity word

\[
1^a0\,1^c0^d,\qquad a,c,d\in\mathbb Z_{\ge1},\qquad
j=a+1+c+d.
\]

Bits describe states before application of T. With q_k the number
of ones among the first k bits, retain every first-drop guard

\[
3^{q_k}\ge2^k\quad(0\le k<j),\qquad 3^{a+c}<2^j.
\tag{1}
\]

The middle even run has exactly one step and both odd runs are exact.
The last d even steps are observed; no maximal terminal run is assumed.
These are precisely L110's hypotheses. In particular n is odd. There
is no assumption of closure, a global minimum, a least period, distinct
junction values, or existence of such a word for every trajectory.

## Conclusion

Write y=T^j(n). Then y is not n, and exactly one of the following holds:

- y<n, so descent occurs at j;
- y=n+1, with y even and T^{j+1}(n)=(n+1)/2<n.

Consequently there is an r in {j,j+1} with T^r(n)<n. This is a
restricted family theorem, not universal descent or strict descent at j.
It does not exclude the unit-growth case at j.

## Proof

### The imported cycle theorem

Use John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005),
51–70, DOI 10.4064/aa117-1-3,
[Theorem 3(b), printed p.55](https://www.impan.pl/shop/en/publication/transaction/download/product/82263#page=5).
For the same shortcut map this theorem excludes nontrivial m-cycles
for 1<=m<=68; only m=2 is needed here. The definitions in section 1.2,
printed p.52, count local minima by their positions in a displayed
period p. They permit a nonminimal period and a starting local minimum
that is not a global minimum. The m-fold repetition of the cycle
{1,2} is explicitly the trivial m-cycle. Section 1.1, p.51, calls a
cycle nontrivial if it contains an integer greater than 2.

The m=2 proof case is already included in Lemma 15 and its complete
proof, printed p.62: the Lemma 14 upper bound contradicts the
Corollary 11 lower bound. This is an import of the published theorem,
including its computational basis. In particular section 1.3,
pp.52–53, records the external verified bound X0=301*2^50 used in
those estimates. Those computations are not independently replayed
here, and the source theorem is not reproved. The applicability checks
below are the only specialization required.

### Exact equality would be a nontrivial two-cycle

Suppose y=n and set n_i=T^i(n), for 0<=i<=j. Equality gives an actual
positive integer periodic orbit with displayed period p=j: determinism
of T repeats the entire segment. It does not imply or require that j
is its least period.

At every positive odd state z, T(z)-z=(z+1)/2>0. At every positive
even state z, T(z)=z/2<z. Thus the actual parity word has exactly the
successive monotone runs: a increases, one decrease, c increases,
and d decreases. The first even states are at positions a and a+1+c;
the next odd state after the first peak is at a+1. Since n_j=n is
odd, the last even run has exactly length d, as also stated in L110's
equality case. In particular n_{j-1}=2n>n, while n_1>n.

The two local minima in the displayed period are therefore exactly
at positions

\[
t_0=0,\qquad t_1=a+1,
\]

and the two local maxima are exactly at

\[
s_0=a,\qquad s_1=a+1+c.
\]

All four positions have the required strict order because a,c,d>=1.
Strict monotonicity inside each run leaves no additional local extrema.
These are positional assertions, valid even if the two minima have
the same numerical value. The source's exact chronological parameters
are

\[
(k_0,l_0,k_1,l_1)=(a,1,c,d),\quad
K=a+c,\quad L=1+d,\quad p=K+L=j.
\]

Hence this is an m=2 cycle under the source's definitions, without
rotating to a global minimum or discarding repetitions. Since n is
odd and n>1, n>=3. The cycle contains an integer greater than 2,
so it cannot be the repeated trivial cycle {1,2,1,2}. Theorem 3(b)
now contradicts its existence. This proves y is not n.

### Combining with L110

Every hypothesis of L110 is unchanged, including all proper-prefix
guards and the potentially partial terminal even run. Its endpoint
bound gives y<=n+1. Since y and n are integers and equality has just
been excluded, either y<n or y=n+1. In the second case L110 gives
that y is even and T^{j+1}(n)=(n+1)/2<n, using n>1. These are the
claimed alternatives. No unit-growth nondivisibility theorem is needed.

This closes the equality obstruction for L110's family by known
mathematics. It does not treat a longer middle even run, more peaks,
or absence of a finite coefficient drop. In particular the closed-cycle
theorem was used only after exact equality was assumed; it was not
applied to an open endpoint or to a merely formal divisor solution.

## Mathlib

Full matching coverage of this descent statement and the imported
m=2 exclusion is **not checked**. Supporting iteration, parity and
arithmetic coverage is also **not checked**; no Mathlib theorem is
assumed. Unknown availability is not evidence of absence. The precise
published cycle theorem above, rather than a Mathlib claim, is the
external mathematical input. No originality is claimed for this import.
