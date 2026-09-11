# Lemma 198: negative-strip lower-bound counting criterion

**Hypotheses.** Use the actual profiles and exact central-strip mass
Y_mid^- of L195 and L197, with fixed K>0 and all their inherited
scales and cutoffs. In particular h is comparable to N^(3/2).
All asymptotic statements concern sufficiently large N in this setup.
For eta,delta>0 let C_N(eta,delta) count ordered integer tuples
(a,b,c,d,m) satisfying all of the following:

- a,b,c,d are in [N,2N], u=ab, v=cd, and |v-2N²|<=K N^(3/2).
- m belongs to M_in and gcd(m,u)=1.
- The exact L191 cell length ell(u,v,m) is at least eta N^(3/2).
- phi(u)/u is at least eta.
- One of c/N,d/N is at most sqrt(2)-delta and the other is at
  least sqrt(2)+delta.

**Conclusion.** The following two statements are equivalent:

(i) There is c0>0 such that Y_mid^- >= c0 Nh for all sufficiently
large N.

(ii) There are fixed eta,delta,c1>0 such that
C_N(eta,delta) >= c1 N³ for all sufficiently large N.

Furthermore C_N(eta,delta)=O_K(N³). Neither (i) nor (ii) is proved
for the actual arithmetic tuples. This equivalence gives a precise
remaining counting problem for the sharpness test, not a lower bound.

**Proof.**

Let E_N consist of the same strip tuples with ell>0, before imposing
the totient and distance thresholds. Keep gcd(m,u)=1. The proof of
L197 shows that the contributing u products occupy an interval of
length O_K(N^(3/2)), that each fixed u,v permits O(1) integers m,
and that each of the u and v intervals contains O_K(N^(3/2))
ordered factor pairs. These statements are counts without profile
weights. Consequently

                         #E_N <= C_E N³.                 (1)

Using a Cartesian product here is only an upper bound. No reverse
count or coprimality density is asserted.

For a tuple in E_N put

f=phi(u)/u, g=ell/N^(3/2),
D=max(-r(c/N)r(d/N),0),
B=p(a/N)p(b/N)p(c/N)p(d/N) alpha_m N²/u.

The explicit positive smooth profiles in L178 and p=(b+d)/2 give
positive uniform lower and upper bounds for p on [1,2]. L194 gives
these bounds for alpha_m on M_in. Since N²<=u<=4N², there are
constants B_min,B_max>0 with B_min<=B<=B_max. Moreover
0<f<=1, 0<g<=G for a fixed G>0, and 0<=D<=1, since ell<=2R
and |r|<=1. The exact ordered identity of L195 becomes

                 Y_mid^- = N^(-1/2) Σ_(E_N) B f g D.     (2)

All floor lengths and the coprimality restriction remain in this
identity. In particular ell is a length, not an integer point count.

Suppose (i) holds. The comparison h>=c_h N^(3/2) gives
Σ BfgD >= A N³ with A=c0 c_h>0. For a threshold tau in (0,1),
call a tuple bad if f<tau or g<tau or D<tau. On any bad tuple,
f g D <= tau max(1,G). By (1), its total contribution is at most
B_max C_E tau max(1,G) N³. Choose a fixed tau small enough that
this is at most A N³/2. The remaining tuples, with all three
f,g,D>=tau, have total weight at least A N³/2. Each weight
BfgD is at most B_max G, so there are at least
A N³/(2 B_max G) such tuples.

For each remaining tuple D>=tau forces opposite signs of the two
ratios and |r(c/N)|,|r(d/N)|>=tau, since each ratio has modulus at
most one. L195 gives

r(x)=-tanh((3/2)log(x/sqrt(2))),
|r'(x)|=(3/(2x)) sech²((3/2)log(x/sqrt(2)))<=3/2.

Since r(sqrt(2))=0, the mean value theorem implies
|x-sqrt(2)|>=2tau/3 whenever |r(x)|>=tau. Thus these tuples
are counted by C_N(tau,2tau/3), proving (ii).

Conversely suppose (ii) holds. Its positive count implies that the
two permitted closed factor intervals are nonempty. On their union
r is continuous and has no zero. Its absolute value therefore has
a positive minimum r_delta. The opposite-side condition gives
D>=r_delta². On every counted tuple f,g>=eta, so (2) yields

Y_mid^- >= N^(-1/2) B_min eta² r_delta² C_N(eta,delta)
         >= B_min eta² r_delta² c1 N^(5/2).

Using h<=C_h N^(3/2) proves (i). Finally the count in (ii) is a
subset of E_N, which proves its O_K(N³) upper bound. ∎

## Qualifications and verification

This proves that a matching lower bound, if true, can be witnessed
by opposite-side pairs a fixed distance from sqrt(2), with cell lengths
and totient ratios both bounded below at their natural scales.
One cannot infer the requisite count from separate factor-pair counts:
(1) is an upper bound and does not control their simultaneous selection
by the exact m cells and gcd(m,u)=1. This selection remains unproved.
The criterion concerns the negative ordered mass only; exterior signed
mass might cancel it, so it supplies no lower bound for |Y_N| or RH.

Verification is analytic: the exact scaling in (2), uniform compact
profile bounds, finite small-factor deletion, the derivative estimate,
and both conversions between Nh and N^(5/2). Formalization would
require these finite weighted inequalities, integer tuple counts, the
mean value theorem and positive minima on the indicated compact sets.
No numerical inference or additional external theorem is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
