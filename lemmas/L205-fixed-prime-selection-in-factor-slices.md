# Lemma 205: fixed-prime selection in factor slices

**Hypotheses.** Use L202's box F_N and L203's slices, with fixed t>0
and real N tending to infinity. Let D>=1 be a fixed integer. Write
x=sqrt(abcd), m0=floor(x)+1, and I=[21/32,27/32]. For each tuple
P4 denotes the value of its own L203 polynomial at its slice index.

**Conclusion.** For sufficiently large N depending on t and D, the set

S_D={tuple in F_N: frac(P4) in I, gcd(m0,D)=1}

has at least c_D #F_N members, where

c_D=(3/64)phi(D)/D>0.                                  (1)

The same proportion holds within every individual slice. Every member
passes L202's phase test and has its occupied full-core window under
L202's restrictions on W. Thus any fixed finite set of primes can be
excluded from m0 while retaining order N³ actual tuples.

For fixed z>=2 take D to be the product of the primes at most z, and
let T_z count the members of S_D for which some prime p>z divides
both m0 and ab. The number of members of S_D with gcd(m0,ab)=1 is
exactly #S_D-T_z. In particular the still **unproved** estimate

T_z <= (c_D/2)#F_N                                     (2)

for some fixed z and all sufficiently large N would give the requested
order N³ coprime population. No estimate (2) is asserted here.

**Proof.**

Put r0=3/32 and q=3/4. Use the periodic triangle

psi(y)=max(1-dist(y,q+Z)/r0,0)

from L204. It has support I modulo one, height one, and mean r0.
On the circle of circumference D define the continuous function

Psi_D(y)=sum over 0<=r<D with gcd(r+1,D)=1
          max(1-dist(y,r+q+D Z)/r0,0).

The supports are disjoint: their centers have circular separation at
least one when there is more than one center, whereas 2r0<1. For D=1
this is just psi. Consequently 0<=Psi_D<=1, and its nonzero values
occur only where frac(y) is in I and gcd(floor(y)+1,D)=1.
Its integral over a period is r0 phi(D); thus its mean is
mu_D=r0 phi(D)/D.

For completeness, in the Fourier convention e(ky/D), its kth
coefficient is

A_k=(r0/D) [sin(pi k r0/D)/(pi k r0/D)]²
       times sum over the selected r of e(-k(r+q)/D),    (3)

with the quotient interpreted as one at k=0. This follows by
integrating each translated triangle, or by the convolution calculation
in L204 after changing the period from one to D. In particular
A_0=mu_D and, for k!=0,

|A_k| <= phi(D) D/(r0 pi² k²).

The Fourier series is absolutely and uniformly convergent, and Fejér's
theorem identifies it with Psi_D, as in L204. For each fixed nonzero
integer k, the third-derivative argument in L204 applies to kP4/D:
its third derivative has magnitude comparable to |k|/(DN) uniformly
on the whole slice. Since D is fixed and n=M+1 is comparable to
sqrt(N), that argument gives

n^(-1) |sum_(j=0)^M e(kP4(j)/D)| = O_(t,D,k)(N^(-1/12)).

To average the Fourier series, first truncate at a fixed H with
sum_(|k|>H)|A_k|<mu_D/4. Then take N sufficiently large that the
finite nonzero-mode contribution is less than mu_D/4, uniformly over
all slices. Therefore the slice average of Psi_D(P4) is at least
mu_D/2=c_D. This uses no uniform assertion for growing D or H.

It remains to check that the selected integer is the exact m0.
The Taylor remainder estimate in L203 gives

|x-P4|=O_t(N^(-1/2)),  |Q-P4|=O_t(N^(-1/2))

uniformly. Take both errors less than 1/32. If Psi_D(P4)>0,
frac(P4) lies in I, at distance at least 5/32 from an integer.
Thus floor(x)=floor(P4), so the gcd condition defining the support
is precisely gcd(m0,D)=1. Also frac(Q) belongs to [5/8,7/8].
Since Psi_D<=1, its slice sum is a lower bound for the number of
members of S_D. In fact the same transfer applies to the endpoints
of I and hence to every member of S_D. Sum over the unique slice
indexing of L203 to obtain (1), and use L202 for the window assertion.

Finally, for the indicated product D, gcd(m0,D)=1 rules out every
prime at most z as a common divisor with ab. The fundamental theorem
of arithmetic says that gcd(m0,ab)>1 is then equivalent to the
existence of a common prime divisor greater than z. This proves the
exact subtraction identity and the conditional consequence of (2).

## Qualifications and verification

This is a fixed-prime selection theorem, not full coprimality. Constants
and the threshold in N may depend on D. One cannot take D to include
all primes up to 2N in the proved fixed-D limit: no such uniform
estimate was supplied, and c_D itself would then vary with N. Separate
phase distribution modulo one does not estimate the joint event
p divides m0 and p divides ab for growing p. The large-prime count
(2), or another argument for full coprimality, remains necessary.
Totient selection and the RH argument are unchanged.

Verification is analytic: the disjoint triangle supports, period-D
Fourier normalization, absolute tail, fixed-frequency derivative bound,
uniform integer-boundary margin, and exact prime-divisor partition.
The existing command `python3 scripts/heat/check_factor_slice_phase.py`
rechecks the rational approximation inequalities used in the transfer;
it is not evidence for a prime-distribution assertion.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
