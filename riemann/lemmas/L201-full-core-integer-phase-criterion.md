# Lemma 201: full-core integer phase criterion

**Hypotheses.** Use L199's full-core window, with all of its original
cutoffs, positive integer W<=R, u,v in [N²,4N²], and
|v-2N²|<=K N^(3/2) for fixed K. Take N sufficiently large.
For the phase expansion additionally assume |u-v|<=C N^(3/2),
with fixed C. Coprimality and totient restrictions are omitted.

**Conclusion.** Put x=sqrt(uv), g=1-frac(x), and m0=floor(x)+1.
The full-core window is occupied if and only if all of these hold:

W <= 2xg+g² <= u-1-W,                                    (1)
a−²+W <= m0² <= a+²-W,                                  (2)
uN²+W <= m0² <= 4uN²-W,                                 (3)
2m0 rho-rho² >= W,  rho=N^(-1/2).                        (4)

Its sole integer is then m0. This includes square uv: in that case
g=1 and (1) fails for sufficiently large N in the central strip.

Write s=u+v, k=u-v, and

Q=s/2-k²/(4s)-k⁴/(16s³).

If k²/s²<=1/2, there is E with

x=Q-E,  0<=E<=k⁶/s⁵.                                   (5)

In the additional |k|<=C N^(3/2) sector this is O_C(N^(-1)).
For every fixed epsilon in (0,1/4), if W=O(N^(3/2)), then

frac(Q) in [1/2+2epsilon,1-2epsilon]                     (6)

implies (1) for sufficiently large N in this sector. Conditions
(2)-(4) still have to be imposed. In particular (6) and (2)-(4),
with the original ordered factor and opposite-side restrictions,
give a sufficient family for the requested occupancy count. No
lower bound on the population of that family is asserted.

**Proof.**

The untrimmed floor-cell square-root interval has width

sqrt(u(v+1)-1)-sqrt(uv)
  < u/(2sqrt(uv)) = (1/2)sqrt(u/v) < 1,

since v>=3N²/2 and u<=4N² for sufficiently large N. By W>0,
every admissible integer is strictly above x. Thus it must equal
m0, or else the interval would have width greater than one.
Substitute m0=x+g in the floor-cell square inequalities to obtain
(1). The other conditions of L199 are precisely (2)-(4); W<=R
is already assumed. This proves both directions with all cutoffs.
If x is integral, g=1; then 2x+1>u since (1/2)sqrt(u/v)<1,
so the upper bound in (1) fails.

For (5), put z=k²/s². The function f(z)=sqrt(1-z) has
f'(0)=-1/2, f''(0)=-1/4 and
f'''(z)=-(3/8)(1-z)^(-5/2). On [0,1/2] its absolute value
is at most (3/8)2^(5/2)<3. Taylor's theorem with remainder gives

0 <= 1-z/2-z²/8-sqrt(1-z) <= z³/2.

Multiplication by s/2 yields the claimed (slightly looser) bound
E<=k⁶/s⁵. Since s>=2N² and |k|<=C N^(3/2), this is O_C(N^(-1)).

For sufficiently large N, E<epsilon. Under (6), subtracting E
crosses no integer, and therefore

frac(x) in [1/2+epsilon,1-2epsilon],
2epsilon <= g <= 1/2-epsilon.

Here u/v=1+O_C(N^(-1/2)), x is comparable to N², and
u/(2x)=(1/2)sqrt(u/v)=1/2+O_C(N^(-1/2)). Consequently
(2xg+g²)/u is bounded away from both zero and one, uniformly
on this interval for g. Since (W+1)/u=O(N^(-1/2)), (1) follows.
This last argument asserts nothing about (2)-(4).

## Why the quartic term matters

The quadratic approximation s/2-k²/(4s) does not have o(1)
absolute error uniformly on this scale. Take integer N=j²,
u=2N²+N^(3/2), v=2N². Then

k⁴/(16s³) -> 1/1024,

while (5)'s remainder tends to zero. Thus the error of the quadratic
approximation tends to 1/1024. These are an integer-product-scale
example, not a construction of ordered factors in the original
support. They disprove only a uniform quadratic approximation over
the stated integer u,v sector. The exact criterion (1)-(4) applies
without any approximation or assumption on k.

## Qualifications and verification

The remaining task is a lower bound for simultaneous phase selection
and safe-m selection on actual products ab,cd. Separate factor-pair
counts or an O(N^(-1)) phase error do not prove such a bound: one
also needs control of the number near phase boundaries. No
uniform distribution, coprimality density, or RH conclusion is used.
L200's necessary exclusion is consistent with this criterion; it is
not an input to its proof. The additional k-sector is an explicit
restriction, not a deduction here from all original cutoffs.

`python3 scripts/heat/check_full_core_phase.py` checks the exact
candidate equivalence with rational cutoffs and integer square roots,
and (5) by rational squared inequalities. These are finite algebra
checks, not evidence for an asymptotic population estimate.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
