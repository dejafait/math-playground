# Lemma 191: exact displacement interval and Möbius sum

**Hypotheses.** Use L190's profile T_N(v), L188's exact interval J,
and L186's real coefficient H_m(r). In particular u,v are integers in
[N²,4N²], rho=N^(−1/2)>0, and 0<|r|≤R. Write
M=[a−−rho,a++rho]∩Z; all its integers are positive under the inherited
sufficiently large N hypothesis. All sums below are finite.

For m∈M and u,v in the indicated range define integer endpoints

b=max(ceil(−R), ceil(a−²−m²), ceil(−2m rho+rho²),
      ceil(uN²−m²), uv−m²),
t=min(floor(R), floor(a+²−m²), floor(2m rho+rho²),
      floor(4uN²−m²), u(v+1)−m²−1).                         (1)

Empty intervals b>t contribute zero. Let mu be the Möbius function: mu(1)=1,
mu(d)=0 if a prime square divides d, and mu(d)=(−1)^j for a product
of j distinct primes. Put

alpha_m=(sqrt(2πm)/N)G_m,
beta_m=−(sqrt(2πm)/N)(2π/m)C_m,

so that H_m(r)=alpha_m+beta_m r. For each positive divisor d of u put
l_d=ceil(b/d), j_d=floor(t/d). If l_d>j_d put n_d=s_d=0;
otherwise put

n_d=j_d−l_d+1−1_{l_d≤0≤j_d},
s_d=(l_d+j_d)(j_d−l_d+1)/2.                          (2)

**Conclusion.** The exact profile is

T_N(v)=Σ_u P(u)/u Σ_(m∈M, gcd(m,u)=1)
                 Σ_(d|u) mu(d)[alpha_m n_d+beta_m d s_d].       (3)

In particular the inner expression is exactly

Σ_(b≤r≤t, r≠0, gcd(r,u)=1) H_m(r).                            (4)

Both coprimality restrictions and every original floor and outer cutoff
are retained. Formula (3) is an identity, not a decay estimate for T_N
or Z_N. Signed-profile decay remains **unproved**.

**Proof.**

Start with the finite sum defining T_N(v) in L190 and fix u,m.
Membership m∈J_(u,r) in L188 is equivalent, for positive m, to
m∈M and the three closed conditions

a−²≤m²+r≤a+²,
uN²≤m²+r≤4uN²,
−2m rho+rho²≤r≤2m rho+rho².

The square-root equivalences are valid by the inherited positivity of
the radicands. The last condition is exactly
|r−rho²|≤2m rho. The floor cell adds
uv≤m²+r<u(v+1). Intersect these conditions with −R≤r≤R.
All lower bounds are closed. Because u,v,m are integers, the strict
upper bound r<u(v+1)−m² is equivalent to
r≤u(v+1)−m²−1. Taking the integer endpoints gives precisely (1).
We retain r≠0 and gcd(r,u)=1, separately from gcd(m,u)=1.
Thus reversing the finite m,r summation gives (4) inside (3).
This argument also covers an empty intersection and v=4N², where
the closed support bound may force m²+r=4uN².

For any positive integer w, prime factorization gives
Σ_(d|w) mu(d)=Π_(p|w)(1−1), equal to 1 for w=1 and 0 otherwise.
For nonzero r apply this identity to w=gcd(|r|,u), obtaining

1_{gcd(r,u)=1}=Σ_(d|u, d|r) mu(d).

Insert it into (4) and exchange the finite sums. The change r=dk,
with d>0, gives l_d≤k≤j_d and k≠0. The affine formula for H
from L186 then evaluates this sum as alpha_m n_d+beta_m d s_d.
Indeed (2) counts all integers in the closed interval except zero,
and s_d is their sum: removing zero has no effect on the arithmetic
progression formula. That formula follows by pairing each k with
l_d+j_d−k, so it holds also for negative or mixed-sign endpoints.
For b>t, l_d>j_d for every d, and both sides vanish. This proves (3).
No integral approximation, distribution assertion or infinite interchange
has been used. ∎

## Qualification, verification

The zero exclusion is explicit even though u>1 eventually makes its
Möbius-weighted count cancel. In particular the formula is also correct
for u=1. One cannot replace n_d by interval length divided by d while
claiming this exact identity. Bounds or cancellation for the resulting
endpoint errors, m sum and signed pair weights have not been established
here; neither zero-mode negligibility nor RH follows.

`python3 scripts/heat/check_mobius_displacement_interval.py` compares
original inequalities with the integer interval and the Möbius evaluation
using rational parameters and signed affine test weights. It exercises
empty intervals, negative displacements, strict floor endpoints, closed
support endpoints and zero removal. These finite tests check algebra only.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
