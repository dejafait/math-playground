# Lemma 224: paired endpoint sum by square-root cells

**Hypotheses.** Use the exact functions of L220 and the interior box
and scales of L221. Fix integers a,c,d in that box, put v=cd, and
write J=[j0,j1]. Retain the rounded A_m,B_m throughout. Define

D(a,c,d)=sum_(m in J, gcd(a,m)=1) Delta_m(1),
T_a=sum_(m in J, gcd(a,m)=1) F_m.

**Conclusion.** Uniformly for sufficiently large N,

-T_a <= D(a,c,d) <= C(h/N+1),
|D(a,c,d)| <= C(h/N+1).                                  (1)

In particular L223's paired Bernoulli endpoint sum satisfies

-T <= S <= C N²h,   |S| <= C N²h.                         (2)

These estimates improve the O(N³h) upper bound there, but do not
establish S=o(T). They concern only the unit progression term.

**Proof.**

Keep L223's four endpoints paired by using its exact identity

D(a,c,d)=Z_a-T_a,
Z_a=sum_(m in J, gcd(a,m)=1) sum_(b integer) f_m(b).        (3)

All terms in Z_a and T_a are nonnegative. By L220, f_m(b)<=2
and f_m(b)=0 outside [N,2N]. Positive f_m(b) implies, directly
from its exact overlap definition and -R<=A_m<B_m<=R,

avb-R < m² < a(v+1)b+R-1.                               (4)

For fixed b define the open square-root cell

C_b=(sqrt(avb-R), sqrt(a(v+1)b+R-1)).                    (5)

Its radicands are positive for sufficiently large N. A cell that
contains a contributing m in J has both endpoints 2N²+O(h+1):
indeed m=2N²+O(h), and the difference of the squared endpoints
is ab+2R-1=O(N²); their square roots are comparable to N²,
so the cell has bounded length and each endpoint is O(1) from m.
Consequently its length is

|C_b|=(ab+2R-1)/(sqrt(a(v+1)b+R-1)+sqrt(avb-R))
      <= ((12/5)N²+2R)/(4N²+O(h+1))=3/5+o(1).

This is uniform in b in [N,2N], a in [11N/10,6N/5], and
c,d in the stipulated box, for cells containing such m. In particular
|C_b|<3/4 eventually, so each b contributes at most one integer m.
This assertion does not assume anything about gcd(a,m).

Equation (4) also places every contributing integer b in

((j0²-R+1)/(a(v+1)), (j1²+R)/(av)).                      (6)

The length of this interval is exactly

(j1²-j0²)/(av) + j0²/(av(v+1))
                    + R/(av) + (R-1)/(a(v+1)).

Here j1-j0=O(h), j1+j0=O(N²), a comparable to N, and v
comparable to N². Its length is therefore O(h/N+1/N).
There are at most this length plus one integers in it. Since each
b contributes at most one m and f_m(b)<=2, dropping gcd only
in this nonnegative upper bound gives

0<=Z_a<=C(h/N+1).                                      (7)

L223's exact area formula gives 0<=F_m<=C/N uniformly.
There are O(h+1) integers in J, so 0<=T_a<=C(h+1)/N.
Combining this with (3) and (7) proves (1), including its one-sided
lower bound without changing any rounded endpoints or gcd selection.
The weighted sum of D(a,c,d) with weights phi(a)/a is precisely S;
the analogous sum of T_a is T. There are O(N³) triples and weights
are at most one. Since h comparable to N^(3/2), summing (1) proves
(2). Only finite sums and elementary interval counts are used.

## Limitation and remaining arithmetic question

The available lower bound T>=cN²h/log N and upper bound T<=CN²h
from L223 do not turn (2) into a vanishing relative error. Even a
logarithm-free lower bound for T would leave an O(1), not little-o,
relative estimate. No lower bound on |S| is asserted.

The short-cell count pays an error of order one for each candidate b;
there are O(h/N) such b per triple, the same scale as its real mass.
The exact problem remaining in (3) is a weighted count of whether
C_b contains an integer in J coprime to a, with weight f_m(b).
Replacing that count by interval length or assuming uniform fractional
parts is not justified here. The paired estimate needs no separate
bounds on the four Bernoulli terms. Other divisor terms, the signed
comparison, and RH remain unresolved.

## Verification

Verification is analytic: derive (4) from strict positive overlap,
rationalize (5), use ab<=12N²/5, subtract the endpoints in (6),
and apply the length-plus-one count. The existing exact rational test
`python3 scripts/heat/check_unit_progression.py` verifies the paired
identity used in (3); it does not test asymptotic distribution.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
