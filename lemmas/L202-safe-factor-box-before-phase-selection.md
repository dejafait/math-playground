# Lemma 202: safe factor box before phase selection

**Hypotheses.** Use the actual last-block endpoints of L181 and the
candidate and cutoffs of L201. Thus, writing V=2N² and L=N^(3/2),

a+=V-1/4,  a−=V-h/(2π)-1/4.

Here N tends to infinity through real values, h is comparable to L,
and K>0 is fixed. Choose H0>0 such that h/(2πL)>=H0 for all
sufficiently large N. Fix

0<t<=min(K/4,H0/8,1),  J_N=[V-2tL,V-tL].

Let F_N be the ordered integer quadruples (a,b,c,d) with

a,c in [11N/10,6N/5],  ab,cd in J_N.

Take any positive integer W<=min(R,L), whenever such W exists.
For the full-core scale additionally require W>=wL for fixed w>0;
this requires the inherited R to permit that choice.

**Conclusion.** All factors of F_N lie in [N,2N] for sufficiently
large N, and

c_t N³ <= #F_N <= C_t N³.                                (1)

Every tuple satisfies |cd-V|<=K L, |ab-cd|<=tL, and the
opposite-side restriction with delta=1/10. At
m0=floor(sqrt(abcd))+1, every safe-m condition (2)-(4) of L201
holds, uniformly over F_N and the indicated W.

In particular put u=ab, v=cd, s=u+v, k=u-v, and
Q=s/2-k²/(4s)-k⁴/(16s³). The remaining sufficient selection is

F_N^phase={tuple in F_N: frac(Q) in [5/8,7/8]}.            (2)

Every tuple of (2) has an occupied full-core window. A lower bound
#F_N^phase>=c N³ would establish the geometric occupancy target
without coprimality or totient restrictions. Such a bound is **unproved**.
Equation (1) alone gives no lower bound for (2).

**Proof.**

For each integer a in [11N/10,6N/5], its allowed b interval is
[(V-2tL)/a,(V-tL)/a], of length tL/a. Uniformly in a, its
endpoints divided by N lie, for sufficiently large N, between
8/5 and 19/10: their limiting range is [5/3,20/11], strictly
inside that larger interval. Thus every allowed b is in [N,2N].
The same statements hold for c,d. In particular
c/N<=6/5<sqrt(2)-1/10 and d/N>=8/5>sqrt(2)+1/10.
These strict numerical inequalities follow by squaring positive numbers.

There are at least N/20 possible integers a for large N. A closed
real interval of length q contains at least q-1 integers. Since

 tL/a >= (5t/6)sqrt(N),

each a admits at least (5t/12)sqrt(N) integers b for sufficiently
large N. Hence the ordered pair count P_N is at least (t/48)L.
Conversely there are at most N/10+2 possible a, and at most
t sqrt(N)+1 choices of b per a. This gives P_N<=C_t L.
The restrictions on (a,b) and (c,d) are identical and independent,
so #F_N=P_N², proving (1) without replacing integers by a density.
Both products lie in J_N, giving the two claimed strip bounds.

Set x=sqrt(uv). Because u,v belong to the same positive interval
J_N, x also belongs to J_N. Since 0<m0-x<=1,

V-2tL < m0 <= V-tL+1.

The actual stationary endpoints give

m0-a− >= (H0-2t)L+1/4 >=6tL+1/4,
a+-m0 >= tL-5/4 >= tL/2

for sufficiently large N. All of a−,a+,m0 are comparable to N²
(the upper bound for h/L is used here). Multiplying these positive
distances by m0+a− and m0+a+ shows that both
m0²-a−² and a+²-m0² are bounded below by a positive constant
times tLN². They exceed W<=L for large N. This proves (2) of L201.

Next, m0²=uv+O(N²), uniformly, since m0-x is at most one.
Here v=2N²+O_t(L) and u=2N²+O_t(L), so

m0²-uN²=u(v-N²)+O(N²)=2N⁴+O_t(N^(7/2)),
4uN²-m0²=u(4N²-v)+O(N²)=4N⁴+O_t(N^(7/2)).

Both exceed L for large N. This proves (3) of L201. Finally
rho=N^(-1/2) and m0=2N²+O_t(L) yield

2m0 rho-rho²=4L+O_t(N)>L>=W

for large N, proving (4). These estimates concern the exact candidate,
not the real root substituted for an integer.

Apply L201 with epsilon=1/16, for which its phase interval is
[5/8,7/8]. The product-difference bound above gives its required
sector, W<=L gives its upper scale bound, and the safe-m conditions
have just been proved. Thus (2) implies the full-core floor-cell
conditions as well. This proves the sufficient selection assertion.

## Qualifications and verification

This completes only the safe-support portion of the requested count.
It proves that these geometric cutoffs leave order N³ actual ordered
tuples available, not that a fixed proportion pass the phase test.
The narrower box is sufficient, not necessary: failure to obtain a
phase lower bound here would not refute occupancy elsewhere. No
coprimality density, totient threshold, signed-mass conclusion, or RH
claim follows. PROOF.md's overall argument is unchanged.

`python3 scripts/heat/check_safe_factor_box.py` tests integer pair
counts and the exact safe-m and selected full-core inequalities on
finite rational endpoint examples within the proof's scale bounds.
It is an algebra and boundary check, not an asymptotic distribution
test. The proof of (1) is the integer interval estimate above.
Formalization requires integer interval counts, square-root monotonicity,
uniform endpoint margins, and L201's sufficient phase implication.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
