# Lemma 209: large-prime tail by product counting

**Hypotheses.** Use L202's box F_N with fixed t>0 and L205's
selected set S_D, for fixed z>=2 and D the product of primes at most
z. Put m0=floor(sqrt(abcd))+1. For 2<=Q<=2N let V_Q(N) count
members of S_D having a common prime p>Q of m0 and ab.

**Conclusion.** For every fixed epsilon>0, uniformly in Q,

V_Q(N) <= C_(t,epsilon) N^epsilon
             [N^3/Q + N^(5/2) log N + N^2].             (1)

In particular V_(z,1/12) from L208, with Q=N^(5/12), satisfies

V_(z,1/12)(N)/#F_N = O_t(N^(-1/3)+N^(-5/12)log N)
                    = o(1).                           (2)

Also the count U_z of common primes p>N^(1/4) is o(#F_N).
These conclusions do not assert full coprimality or RH.

**Proof.**

We first record an elementary divisor bound with its constants. For
any delta>0 there is C_delta such that the number tau(v) of positive
divisors of an integer v>=1 is at most C_delta v^delta. Indeed write
v as a product of prime powers. For primes q>=2^(1/delta) and
integers alpha>=1, alpha+1<=2^alpha<=q^(delta alpha).
For each of the finitely many smaller primes the supremum of
(alpha+1)/q^(delta alpha), over integers alpha>=0, is finite, since
an exponential dominates a linear function. Multiplying these finite
suprema proves the bound, including v=1. With delta=epsilon/2,
v<=4N^2 therefore gives tau(v)<=C_epsilon N^epsilon.

Fix a prime p<=2N. Let A(p) be the number of allowed first pairs
(a,b) with p dividing ab. We need only an upper bound, not a density:

A(p)<=C_t(N^(3/2)/p+N).                                (3)

To see this for p dividing a, there are O(N/p+1) multiples in the
a interval and O_t(sqrt(N)) allowed b values for each. This is
O_t(N^(3/2)/p+sqrt(N)). For p dividing b, each of O(N) choices
of a has at most O_t(sqrt(N)/p+1) multiples in its b interval.
Adding the two bounds proves (3), even when a tuple is counted twice.
All estimates include interval endpoints and hold for large N,
uniformly throughout p<=2N.

For one such fixed pair put u=ab. By L202 both u and v=cd belong
to J_N=[2N^2-2tN^(3/2),2N^2-tN^(3/2)]. Their geometric mean
belongs to the same interval. Consequently m0 lies in an interval
of length at most tN^(3/2)+1, so the number of possible m0 divisible
by p is at most C_t(N^(3/2)/p+1).

For each possible integer m=m0, the exact rounding condition is

(m-1)^2 <= uv < m^2.                                  (4)

Here m is positive; (4) is equivalent to m-1<=sqrt(uv)<m,
including the case of an integer square root. Hence v lies in the
half-open real interval [(m-1)^2/u,m^2/u), of length (2m-1)/u.
Uniformly u>=N^2 and m<=2N^2+1 for sufficiently large N, so this
length is at most 5. It contains at most 6 integers. Restricting
these integers further to J_N only decreases their number. Each
positive integer v in J_N has at most tau(v) ordered positive
factorizations (c,d): choosing c as a divisor determines d uniquely.
In particular imposing L202's factor restrictions cannot increase
the bound C_epsilon N^epsilon per v.

Thus, for each fixed first pair, the number of opposite pairs with
p dividing m0 is at most

C_(t,epsilon) N^epsilon (N^(3/2)/p+1).                 (5)

This is an upper bound for the full box; no property of the phase
selection or independence of divisibility events has been used.
Multiplying (3) and (5), the joint count for a given p is at most

C_(t,epsilon) N^epsilon
 [N^3/p^2 + N^(5/2)/p + N^(3/2)/p + N].               (6)

Every prime divisor of ab divides a or b, whose sizes are at most
2N. Apply the finite union bound to (6) for Q<p<=2N, and use

sum_(p>Q) p^(-2) <= C/Q,
sum_(p<=2N) 1/p <= 1+log(2N),
#{p<=2N} <= 2N.

These inequalities follow by enlarging the prime sums to integer
sums and comparing with integrals. Absorb the smaller
N^(3/2)log N term into N^(5/2)log N. This proves (1).
Since #F_N is bounded below by c_t N^3, choose epsilon=1/12
and Q=N^(5/12) to obtain (2); the extra N^(-11/12) term is
absorbed into the displayed bound. Choosing instead Q=N^(1/4)
and the same epsilon gives

U_z(N)/#F_N <= C_t[N^(-1/6)+N^(-5/12)log N+N^(-11/12)]
             = o(1).

Constants in these upper bounds do not require uniform distribution
modulo growing primes, and are independent of the selected subset.

## Qualifications and verification

The bounded product interval costs the elementary N^epsilon divisor
loss, but this is harmless above any fixed positive power of N.
This does not control all p>z for fixed z: replacing Q by z in (1)
would leave a growing N^epsilon/z bound. Combining a small-prime
estimate with this tail and the fixed-D population still requires
an explicit comparison of constants; no full coprime population is
claimed here. Totient selection and the main RH gap remain unresolved.

Verification is analytic: the elementary divisor proof, both factor
orientations in (3), the strict upper endpoint in (4), the constant
length of the product interval, and the three prime sums above.
No numerical distribution assertion is used or required. The direct
mathematical inputs are L202 for the box and its cardinality and
L205 for the selected set and candidate integer. L208 only identifies
the notation for the requested tail; its estimates are not used.
Formalization would require unique prime factorization, the divisor
bound proved above, integer interval counts, and finite union bounds.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
