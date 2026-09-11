# Lemma 221: real main term exceeds the target scale

**Hypotheses.** Use the exact M_tot, E_tot, Q_N and functions f_m,
F_m of L220 on the fixed factor box of L218. Use the actual
last-block endpoints of L181, namely

a+=2N²−1/4, a−=a+−h/(2π),

with h comparable to N^(3/2), R=C_R N^(3/2), C_R>0 fixed,
and rho=N^(−1/2). All assertions are for sufficiently large real N.

**Conclusion.** There are fixed positive constants c,C such that

c N^(7/2)/(log N)² <= M_tot <= C N^(7/2).                 (1)

In particular M_tot/N³ tends to infinity. If Q_N=O(N³), then

E_tot/M_tot = −1+O((log N)²/sqrt(N)).                     (2)

Thus E_tot=o(M_tot), or E_tot=O(N³), would instead rule out that
proposed bound. No estimate on the actual E_tot or lower bound on
Q_N is asserted.

**Proof.**

Write H=h/(2π), and restrict the integer a,m variables to

A=[11N/10,6N/5], J=[a−+H/4,a+−H/4].

Their real lengths are A0=N/10 and J0=H/2. Retain all integers
c,d in [8N/5,17N/10], and put v=cd. Every m in J belongs to
M_in, and m=2N²+O(N^(3/2)) uniformly. Consequently

m²/(avN) = 4/((a/N)(v/N²))+O(N^(−1/2)).

The limiting expression lies between 4/((6/5)(289/100)) and
4/((11/10)(64/25)), both strictly between 1 and 2. Hence the
point m²/(av) stays a fixed positive multiple of N from both
endpoints N,2N, uniformly over these restrictions.

We first bound the exact integral F_m from below without altering
its rounded cutoffs. Put w=min(R/4,m rho/4), so w is comparable
to N^(3/2). In L220's definitions, each raw lower cutoff is at
most −2w and each raw upper cutoff at least 2w, eventually.
For the R cutoff this follows from R>=4w. For the rho cutoff
it follows from 2m rho>=8w and rho²=o(w). For the stationary
cutoffs it follows from the distance H/4 to each endpoint:
m²−a−² and a+²−m² are bounded below by a positive constant
times N²H, which exceeds w. Taking ceilings and floors therefore
still gives A_m<=−w and B_m>=w for sufficiently large N.

Consider the real interval

X_m=[(m²+w+1)/(a(v+1)), (m²−w)/(av)].

On this interval a(v+1)x−m²−1>=w and avx−m²<=−w.
Thus the exact f_m(x) is at least 2w/R. Its length before any
clipping is

|X_m|=m²/[av(v+1)]−(w+1)/[a(v+1)]−w/(av).

The first term is bounded below by a positive constant times 1/N;
the two subtracted terms are O(N^(−3/2)). Both endpoints differ
from m²/(av) by O(1/N), so the strict interior margin above
ensures X_m is contained in [N,2N]. It is nonempty eventually,
and we have proved uniformly

F_m >= (2w/R)|X_m| >= c1/N.                              (3)

This uses the exact f_m of L220, including its minus one. The
constant c1 may depend on C_R and the scale comparison constants.

Next count pairs (a,m) in A times J with gcd(a,m)=1. Any prime
common to a,m is at most 6N/5. An interval of real length L
contains at most L/p+1 multiples of p and at least L−1 integers.
A union bound therefore bounds the number of noncoprime pairs by

sum_(p<=6N/5) (A0/p+1)(J0/p+1)
 <= (3/4)A0 J0 + (A0+J0)(1+log(6N/5)) + 6N/5.           (4)

Here primes were enlarged to integers: sum_(n>=2)1/n² is at
most 1/4+integral_2^infinity x^(−2)dx=3/4, and the harmonic
sum is at most 1+log(6N/5). All sums preceding these bounds
are finite. The total pair count is at least (A0−1)(J0−1).
Since A0 is comparable to N and J0 to h, subtracting (4) leaves
at least A0 J0/8 coprime pairs eventually. Indeed all the error
terms divided by A0 J0 tend to zero. This proves a lower bound
c2 Nh while retaining exactly the gcd(a,m)=1 selection.

Finally an elementary universal totient bound is sufficient here.
If n has k distinct prime divisors p1<...<pk, then pi>=i+1 and

phi(n)/n = product_(i=1)^k (1−1/pi)
          >= product_(i=1)^k i/(i+1)=1/(k+1).

Since n>=2^k, this is at least 1/(1+log_2 n); it also holds
for n=1. Our a=O(N), m=O(N²) therefore satisfy

(phi(a)/a)(phi(m)/m) >= c3/(log N)².                     (5)

By L220, S_K(am)>=1/4, and every summand of M_tot is
nonnegative. Restrict that sum to the pairs just counted and to
the at least N²/400 ordered c,d pairs in the fixed box. Equations
(3) and (5) give

M_tot >= (1/4)(c3/(log N)²)(c1/N)(c2 Nh)(N²/400),

which proves the lower bound in (1). The upper bound is L220's
existing bound. No independence between totient weights, cell
lengths and the gcd selection was assumed: all lower bounds on
weights and lengths are uniform over the retained pairs.

The exact identity Q_N=M_tot+E_tot from L220 gives
E_tot/M_tot=−1+Q_N/M_tot. Under the explicitly unproved
condition Q_N=O(N³), (1) bounds the last term by
O((log N)²/sqrt(N)), proving (2). Conversely either small-error
condition in the conclusion gives Q_N/M_tot tending to one,
which, by (1), is incompatible with Q_N=O(N³).

## Qualifications, verification, and formalization

This is a real-main-term lower bound, not an integer sampling
asymptotic. The signed progression errors could cancel that main
term; such cancellation is not proved or excluded. The signed
comparison and RH remain unresolved. The logarithmic loss is
sufficient to distinguish the two scales; no sharp asymptotic
constant or positive integer-population proportion is claimed.

Verification is analytic: strict rational box margins, the exact
plateau endpoint subtraction including the minus one, eventual
rounding inequalities, finite prime union counting, the telescoping
totient bound, and the exact signed identity. Formalization would
require these inequalities uniformly in real N and the elementary
limits log(N)/N and (log N)²/sqrt(N). No numerical distribution
evidence or additional nonstandard arithmetic input is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
