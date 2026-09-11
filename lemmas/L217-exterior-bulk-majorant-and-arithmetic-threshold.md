# Lemma 217: exterior bulk majorant and arithmetic threshold

**Hypotheses.** Use the exact nonnegative ordered weight W, ratio r,
and fixed scales of L213, with the original cutoff R=C_R N^(3/2)
for fixed C_R>0 and h comparable to N^(3/2). All factors are integers
in [N,2N]; m lies in M_in and satisfies gcd(m,ab)=1. Put
s=sqrt(2)N, D_*=N^(7/4)/log N, B_*=N^(15/8)/log N,
and H_*=N^(3/4)/log N. For sufficiently large real N define the
ordered-pair set S_N by

N²+D_*<cd<4N²-D_*, |cd-2N²|>B_*,
|c-s|>H_*, |d-s|>H_*.

Write f_cd=max(r(c/N)r(d/N),0) and define

G_N=sum_(S_N) f_cd,
A_cd=N²/(Rh) sum_(a,b,m) W(a,b,c,d,m),
E_rem^+=sum_(S_N) sum_(a,b,m) W(a,b,c,d,m) f_cd.

Every inner sum retains the exact displacement lengths and coprimality.

**Conclusion.** There are fixed positive constants c,C such that

cN²<=G_N<=CN²,  0<=A_cd<=C.                              (1)

Thus the geometric majorant (Rh/N²)G_N is of order Rh, exceeding
Nh by a factor of order N^(1/2). This is not a lower bound on E_rem^+.
The exact normalized identity is

E_rem^+/(Nh)=(R/N³) sum_(S_N) A_cd f_cd.                  (2)

In particular E_rem^+=O(Nh), respectively o(Nh), is equivalent to
sum_(S_N) A_cd f_cd=O(N^(3/2)), respectively o(N^(3/2)).
Equivalently its f-weighted mean

(sum_(S_N) A_cd f_cd)/G_N

must be O(N^(-1/2)), respectively o(N^(-1/2)). Neither of these
arithmetic mean bounds is proved here.

**Proof.**

Consider the integer box 8N/5<=c,d<=17N/10. Its products obey

(64/25)N²<=cd<=(289/100)N².

The distance from the lower product endpoint N² is at least
(39/25)N², from the upper endpoint 4N² at least (111/100)N²,
and from 2N² at least (14/25)N². Both factor distances from s
are at least (8/5-sqrt(2))N, a fixed positive multiple of N.
Since D_*/N², B_*/N², and H_*/N tend to zero, this entire
box lies in S_N eventually, with all strict inequalities satisfied.
It also lies outside any fixed central strip of width K N^(3/2).

By L195, on [8/5,17/10] the ratio is negative and its absolute
value is at least

r0=tanh((3/2)log((8/5)/sqrt(2)))>0.

Indeed log and tanh are increasing. Consequently f_cd>=r0²
on the box. A closed interval of length N/10 contains at least
N/10-1 integers, which is at least N/20 for N>=20. The box
therefore has at least N²/400 ordered pairs. This proves
G_N>=r0² N²/400. Conversely |r|<=1 by L195 and the full
factor square contains at most (N+1)² pairs, proving the upper bound.

The uniform fixed-pair estimate in L213 is

sum_(a,b,m) W(a,b,c,d,m)<=C Rh/N².

It bounds the exact sum on the left without changing its definition;
in particular its cell lengths and gcd restriction are retained.
Multiplication by N²/(Rh) gives the bound on A_cd in (1).
Multiplying the two-sided bounds for G_N by Rh/N² proves the
claimed size of the geometric majorant. The ratio Rh/(Nh)=R/N
is C_R N^(1/2), so it is not O(1).

Finally substitute the definition of A_cd in the finite sum for
E_rem^+ and divide by Nh to obtain (2). Since R=C_R N^(3/2),
the claimed big-O and little-o equivalences follow immediately.
Dividing by the two-sided estimate G_N comparable to N² proves
the weighted-mean versions. No mean value for actual cells or
coprimality has been assumed.

## Qualifications, verification, and formalization

This identifies a limitation of summing the uniform fixed-pair bound
and using only the remaining factor geometry. It does not show that
the actual mass is of order Rh, that an Nh bound is false, or that
L212's negative mass is canceled. A possible improved bound must use
additional information about the exact weights A_cd. Even O(Nh)
without an adequate constant would not decide the signed comparison.
The total signed sum and RH remain unresolved.

Verification is analytic: a fixed rational box satisfies every moving
exclusion, the real-N integer count and ratio lower bound are uniform,
and (2) is an exact finite identity. The two-sided cutoff scale is
explicit and is needed for the stated equivalent exponents. Direct
inputs are L195's ratio formula and L213's fixed-pair estimate; other
localizations and L212 are comparisons only. Formalization requires
the eventual box inclusions, integer counts, monotonicity, and finite
normalization with uniform constants. No numerical evidence is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
