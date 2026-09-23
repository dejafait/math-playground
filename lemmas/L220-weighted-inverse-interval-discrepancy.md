# Lemma 220: weighted inverse-interval discrepancy

**Hypotheses.** Use the boxes, scales, Q_N and slice q(a,c,d) of
L218–L219, for sufficiently large real N. Put v=cd and K=floor(2N).
For m in M_in set

A_m=max(ceil(-R),ceil(a−²-m²),ceil(-2m rho+rho²)),
B_m=min(floor(R),floor(a+²-m²),floor(2m rho+rho²)),
f_m(x)=max(min(B_m,a(v+1)x-m²-1)-max(A_m,avx-m²),0)/R

on [N,2N], and zero elsewhere. Write F_m=integral_R f_m(x) dx,
and D(m)=sum_(j|m)|mu(j)|. Define

S_K(am)=sum_(1<=k<=K, gcd(k,am)=1) mu(k)/k²,
Delta_m(l)=sum_(b in lZ) f_m(b)-F_m/l.

**Conclusion.** The exact identity q=M+E holds, where

M=(phi(a)/a) sum_(m in M_in, gcd(m,a)=1)
                   (phi(m)/m) S_K(am) F_m,
E=(phi(a)/a) sum_(m in M_in, gcd(m,a)=1)
       sum_(k<=K, gcd(k,am)=1) mu(k)/k
       sum_(j|m) mu(j) Delta_m(jk).                         (1)

Every exact integer length and both arithmetic weights are retained.
Uniformly, 1/4<=S_K(am)<=7/4 and |Delta_m(l)|<=8. Consequently

|E|<=8(phi(a)/a)(1+log K) sum_(m in M_in, gcd(m,a)=1) D(m). (2)

In particular M is nonnegative and comparable to
(phi(a)/a) sum_(m in M_in, gcd(m,a)=1) (phi(m)/m) F_m.
It is O(h/N). Neither an upper bound of order one for M nor a
saving for E on average over a,c,d is proved. Summing (1) gives
an exact discrepancy formulation of the unresolved Q_N=O(N³).

**Proof.**

First the two product-support cutoffs in L191 are redundant on this
fixed box. Here v>=64N²/25>N² and v+1<=289N²/100+1<4N².
At integer b, the lower integer avb-m² dominates ceil(abN²-m²),
and the upper integer a(v+1)b-m²-1 is at most floor(4abN²-m²).
Thus f_m(b) is exactly L219's e_m(b), including all remaining rounded
endpoints. This observation avoids replacing a rounded moving cutoff
by a differentiable approximation. Positive f_m(x) implies x in I_m.

The untruncated expression min(B_m,a(v+1)x-m²-1) minus
max(A_m,avx-m²) is concave: a minimum of affine functions is
concave and a maximum is convex. Its positive part is unimodal
(nondecreasing then nonincreasing on its positive interval).
Clipping to [N,2N] preserves this property with possible endpoint
jumps. Also 0<=f_m<=2 since B_m<=R and A_m>=-R.
Its total variation on the real line is therefore at most 4.
All level sets {x:f_m(x)>t}, 0<=t<2, are intervals, with any
endpoint convention allowed. The number of multiples of l in an
interval differs from its length/l by at most 2. Integrating this
inequality over t (the elementary layer-cake identity) gives
|Delta_m(l)|<=4, and hence the stated conservative bound 8.
This also covers empty support and values at clipping endpoints.

If gcd(a,m)>1 the entire integer contribution is zero. Otherwise,
for an integer b coprime to m, prime factorization gives

phi(ab)/(ab)=(phi(a)/a)
       sum_(k|b, gcd(k,am)=1) mu(k)/k.

Primes dividing a have already supplied their factor; primes dividing
m cannot divide b. Insert 1_{gcd(b,m)=1}=sum_(j|m,j|b)mu(j).
All b under consideration are positive and at most K, so k<=K.
Since gcd(k,m)=1, simultaneous divisibility by j and k is exactly
divisibility by jk. Finite interchange now expresses q as the same
sum as E with Delta_m(jk) replaced by sum_(b in jkZ)f_m(b).
Substitute F_m/(jk)+Delta_m(jk). The identity
sum_(j|m)mu(j)/j=phi(m)/m yields (1).

For the coefficient, the k=1 term is 1, and
sum_(k=2)^infinity 1/k² <= 1/4+integral_2^infinity x^(-2)dx=3/4.
This proves its two uniform bounds without a prime-distribution input.
The triangle inequality and sum_(k<=K)1/k<=1+log K give (2).
Finally F_m<=2|I_m| and L219 bounds the sum of interval lengths
by O(h/N), proving M=O(h/N).

## What this discrepancy reduction does and does not establish

Let M_tot and E_tot be the sums of M and E over the O(N³) triples.
Then Q_N=M_tot+E_tot exactly, with M_tot>=0 and M_tot=O(N^(7/2)).
Because Q_N>=0, the requested upper bound is equivalent to the
one-sided condition E_tot<=-M_tot+O(N³). In particular a small
absolute discrepancy by itself proves the requested bound only if
the main term is also appropriately controlled. No lower bound on
M_tot is asserted: the exact lengths and gcd(a,m) selection matter.

The separate-progression error budget in (2) has no factor 1/N:
it pays an O(1) endpoint error for each m and divisor choice, whereas
the real intervals have length O(1/N). Dropping arithmetic restrictions
gives only O(h(1+log K) max_(m in M_in)D(m)) per slice and
O(N³h(1+log K) max D(m)) in aggregate, worse than L219's bound.
These are limitations of the proved estimate, not lower bounds on
its actual error and not a disproof of the desired saving. Cancellation
between progression errors, or a separate main-term analysis, remains
necessary for this route to advance.

## Verification

The verification is finite algebra and analytic interval counting:
redundant cutoffs, concavity and bounded height, layer-cake counting,
prime-factor identities, and finite summation. The script
`scripts/heat/check_weighted_inverse_discrepancy.py` additionally checks
the weighted divisor identity with rational piecewise-affine lengths.
It is an algebra test, not asymptotic distribution evidence.
No signed-total
estimate or RH conclusion follows.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
