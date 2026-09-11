# Lemma 193: density first-moment decay

**Hypotheses.** Use L192's exact integer intervals [b,t], density profile
and signed pairing, with all inherited scales and bounded real pair
profiles. Use L191's alpha_m,beta_m, so beta_m=O(N^(−2)), and
L186's P,Q. Put ell=t−b and J=(t²−b²)/2 on nonempty intervals;
put both equal to zero on empty intervals. Define finite signed sums

Z_G=Σ_(u,v,m∈M: gcd(m,u)=1) P(u)Q(v) phi(u)/u² alpha_m ell,
Z_C=Σ_(u,v,m∈M: gcd(m,u)=1) P(u)Q(v) phi(u)/u² beta_m J.

Thus Zbar_N=Z_G+Z_C exactly. The sign in beta_m is included in Z_C.

**Conclusion.** For every epsilon>0,

|Z_C| ≤ Σ_(u,v,m∈M: gcd(m,u)=1)
           |P(u)Q(v)| phi(u)/u² |beta_m J|
       = O_epsilon(h N^(1/2+epsilon)+N^(1+epsilon)) = o(Nh), (1)

where the final little-o follows by choosing epsilon<1/2. Consequently

Z_N=Z_G+O_epsilon(h N^(1/2+epsilon)+N^(1+epsilon)),          (2)

and Z_N=o(Nh) if and only if Z_G=o(Nh). Decay of Z_G is
**unproved**. Its available absolute estimate here is only
O_epsilon(h N^(3/2+epsilon)).

**Proof.**

All constants can depend on the fixed profiles and inherited scale
constants. Every estimate below uses the original R=O(N^(3/2)),
with R+1 or R+2 in bounds to include integer rounding. Take N
sufficiently large that 2(R+2)<N².

Call m exceptional at a stationary endpoint if

|m²−a−²|≤R+2 or |m²−a+²|≤R+2.

There are O(1) such integers: since a±,m are positive and comparable
to N², each condition implies |m−a±|=O(N^(−1/2)). Outside these
exceptional values each stationary support inequality either excludes
all r in [−R,R], or imposes no restriction there.

Call (u,m) a boundary pair if there exists an integer j such that

|m²−uj|≤R+2.                                                (3)

This includes the global support boundaries j=N² and j=4N² as
well as every floor boundary. Since 2(R+2)<u, there is at most one
such j for a given u,m. If (3) fails, the full displacement window
[−R,R] lies strictly inside one real floor cell. The global support
conditions either exclude it or leave it intact. In particular a
strict upper floor bound, whose integer version subtracts 1, does
not trim any integer in this window.

Consider a nonempty interval for m not exceptional and (u,m) not a
boundary pair. The only remaining cutoffs are the original radius and
nearest-square displacement window. Thus

b=ceil(max(−R,−2m rho+rho²)),
t=floor(min(R,2m rho+rho²)).

Write L=2m rho and delta=rho²=N^(−1). The sum of the two real
endpoints max(−R,−L+delta) and min(R,L+delta) lies between 0
and 2delta: if both active endpoints come from the same interval the
sum is respectively 0 or 2delta, and in the mixed case it lies between
these values. Integer rounding alters the sum by less than 2.
Consequently |b+t|≤2+2delta and

|J|=|(t−b)(t+b)/2|=O(R+1).                                 (4)

This does not assume that Q takes the same value on adjacent cells;
there is just one surviving cell in this case. In all cases the crude
bound |J|≤R(t−b)=O((R+1)²) suffices. L192's argument shows that
at most two cells v have nonempty intervals for each u,m.

We give the weighted counts needed for the exceptional pairs. The pair
formulas in L186 and the divisor estimate in L187 imply, for every
eta>0, |P(u)|,|Q(v)|=O_eta(N^eta), uniformly on their supports,
and Σ_u |P(u)|=O(N²). Arbitrarily small exponents may be chosen
separately and then combined. Therefore the total absolute pair mass
in the at most two cells for any fixed m is O_epsilon(N^(2+epsilon)).

For boundary pairs a better bound holds. Put r=uj−m² in (3).
Then r is integral, |r|≤R+2, and u divides the positive integer
m²+r≍N⁴. For each of O(R+1) choices of r the elementary divisor
bound gives O_epsilon(N^epsilon) choices of u. The uniform divisor
bounds for P and Q, and the at most two relevant cells, give

Σ_(u boundary, v with nonempty interval) |P(u)Q(v)|
       =O_epsilon((R+1)N^epsilon),                          (5)

for each fixed m. This is an upper bound only; repetitions can only
increase its majorant. The integer m²+r is positive for large N,
so the divisor estimate is applicable. No distribution of quadratic
residues is asserted or needed.

Now phi(u)/u≤1, 1/u=O(N^(−2)), and beta_m=O(N^(−2)).
Drop gcd(m,u)=1 only in the nonnegative majorants. Partition the
sum into endpoint-exceptional m, boundary pairs for the remaining m,
and the rest. The three respective bounds are

O_epsilon((R+1)² N^(−2+epsilon)),
O_epsilon(h (R+1)³ N^(−4+epsilon)),
O_epsilon(h (R+1) N^(−2+epsilon)).                           (6)

Indeed the first uses O(1) values of m and full pair mass; the second
uses (5) and the crude J bound; the third uses (4) and full pair mass.
Substituting R=O(N^(3/2)) proves (1). All signed weights and the
coprimality restriction remain in the exact formula; taking absolute
values is used only to establish a bound valid for those weights.

L192 gives Z_N=Zbar_N+O_epsilon(h N^epsilon), absorbed in (2).
Since h≍N^(3/2), division by Nh and epsilon<1/2 proves both the
little-o assertion and the equivalence. Finally alpha_m=O(1),
ell=O(R+1), and full pair mass per m give the stated absolute bound
for Z_G. That estimate does not prove its required decay. ∎

## Qualifications, verification and formalization

The estimate gains from the signed first moment inside each density
integral; it does not bound the integral of |x| on a typical cell by
O(R). It neither averages Q nor assumes that gcd(m,u)=1 is independent
of the endpoints. The remaining interval-mass term, nonzero additive
frequencies, other gcd sectors and RH are unresolved.

`python3 scripts/heat/check_density_first_moment.py` checks the exact
integer-interval classification and the first-moment bound with rational
cutoffs, including negative displacements, singleton and empty intervals,
floor boundaries and support boundaries. Asymptotic bounds (5)–(6) are
proved analytically. Formalization requires the endpoint partition,
rounding estimate, weighted divisor count and finite absolute summation.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
