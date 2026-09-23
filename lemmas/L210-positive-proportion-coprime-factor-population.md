# Lemma 210: positive-proportion coprime factor population

**Hypotheses.** Use L202's box F_N, with its fixed t>0 and inherited
geometric hypotheses, and L205's selected set S_D and integer
m0=floor(sqrt(abcd))+1. Fix z=65536 and let D be the product of
all primes at most z. Put c_D=(3/64)phi(D)/D.

**Conclusion.** For all sufficiently large real N (with threshold
allowed to depend on the fixed parameters and D),

#{tuple in S_D: gcd(m0,ab)=1} >= (c_D/2)#F_N
                              > (3/65536)#F_N.          (1)

In particular this is a positive proportion of F_N and is bounded
below by a positive constant times N³. These tuples retain L205's
phase selection and occupied full-core window under the inherited
restrictions on W. No totient threshold is asserted.

**Proof.**

First compare the constants without a prime-distribution theorem.
The usual finite totient product (by inclusion-exclusion over prime
divisors) gives

phi(D)/D = (1/2) product_(3<=p<=65536, p prime) (1-1/p).

Every odd prime in this product is among 3,5,...,65535. Inserting
the remaining odd integers multiplies by numbers in (0,1), so

phi(D)/D >= (1/2) product_(j=1)^32767 2j/(2j+1).

For j>=1, all quantities below are positive and

(2j/(2j+1))² >= (2j-1)/(2j+1),

because 4j² >= (2j-1)(2j+1)=4j²-1. Multiplication and telescoping
therefore give

phi(D)/D >= 1/(2 sqrt(65535)) > 1/512,
c_D/2 > 3/65536.                                      (2)

On the other hand, enlarging the prime sum to an integer sum and
using that x^(-2) decreases on the positive real axis gives

2 sum_(p>z) p^(-2)
 <= 2 sum_(n=z+1)^infinity n^(-2)
 <= 2 integral_z^infinity x^(-2) dx
 = 2/65536 < 3/65536 < c_D/2.                         (3)

All products here are finite; their huge but fixed size poses no
uniformity requirement on N.

Let T_z count tuples of S_D having a common prime p>z of m0 and
ab, as in L205. For N large enough that N^(1/4)>=z, every such
prime is either in (z,N^(1/4)] or above N^(1/4). Apply L207 with
Y=z to the first event, and L209 with Q=N^(1/4) and epsilon=1/12
to the second. A union bound (allowing overlap between the events)
yields

T_z/#F_N <= 2 sum_(p>z) p^(-2) + E_N,

where E_N is a nonnegative upper error tending to zero. Explicitly
it can be taken at most a fixed constant times

N^(-1/24)(log N)² + N^(-1/4) + N^(-1/6)
 + N^(-5/12)log N + N^(-11/12).

Take N sufficiently large that E_N<=1/65536, as well as large
enough for L205's fixed-D population bound. Equations (2)-(3) give

T_z/#F_N <= 3/65536 < c_D/2.

L205 excludes every prime at most z from m0 on S_D. By prime
factorization the tuples of S_D failing gcd(m0,ab)=1 are therefore
exactly those counted by T_z. Consequently

#{tuple in S_D: gcd(m0,ab)=1}
 = #S_D-T_z >= c_D #F_N-T_z >= (c_D/2)#F_N.

This proves (1), using (2) for its strict numerical lower bound.
L202 supplies #F_N bounded below by a positive constant times N³.
The geometric conclusions follow by taking a subset of L205's set;
no independence between phase selection and divisibility was used.

## Qualifications and verification

The choice of z and D is fixed before taking N to infinity. The
proof does not claim an effective useful size for the eventual
threshold in N. A lower bound for phi(ab)/(ab) on a positive
proportion of these tuples still needs proof. In particular this
lemma alone does not establish the negative-strip mass criterion,
a signed-mass lower bound, or RH.

Verification is analytic: the direction of the finite product
comparison, its telescoping square bound, the integer-series integral
bound, the exact common-prime partition, and the vanishing errors
were checked. A rational arithmetic check of the constants uses
`python3 scripts/heat/check_coprime_population_constants.py`.
This script tests only the arithmetic inequalities, not asymptotic
distribution.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
