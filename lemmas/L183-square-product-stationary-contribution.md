# Lemma 183: square-product stationary contribution

**Hypotheses.** Use the block, bounded real weights w, product weights
W(k), endpoints a±, and coordinates z± of L182. Thus h≍N^(3/2),
a±≍N² and a+−a−=h/(2π). Define the square subset of the stationary
contribution by

A_sq=N^(−2) Σ_(n∈I⁴: n1*n2*n3*n4=m², a−≤m≤a+, m integer)
                    w(n) K_2(log(m²/N⁴)).

Each quadruple is counted once, with its unique positive square root m.
For each m in this range let

G_m=∫_(z−(m²))^(z+(m²)) sin(z²) dz.

**Conclusion.** For every epsilon>0, as N tends to infinity,

Re A_sq=(N²h)^(−1) Σ_(a−≤m≤a+, m integer)
                W(m²) sqrt(2πm) G_m
          + O_epsilon(N^(−2+epsilon)),                         (1)

and even with absolute values on individual quadruple contributions,

N^(−2) Σ_(square stationary quadruples)
           |w(n) K_2(log(m²/N⁴))|
       =O_epsilon(N^(−1+epsilon)).                             (2)

In particular A_sq=o(1), and its combined all-positive/all-negative
contribution −Re A_sq/8 to the mixed moment is o(1).

**Proof.**

We first prove the needed multiplicity bound rather than assuming a
uniform bound on the number of factorizations. Let d_4(k) count ordered
positive integer factorizations of k into four factors. Unique prime
factorization and distribution of each prime exponent among four slots give

d_4(k)=∏_(p^b || k) binomial(b+3,3).

For any eta>0 this is at most C_eta k^eta. Indeed,
binomial(b+3,3)≤4^b for b≥1: assigning b labeled objects to four slots
surjects onto all weak compositions of b. For primes p≥4^(1/eta)
this is at most p^(eta b). There are only finitely many smaller primes;
for each of them the supremum over b≥0 of
binomial(b+3,3)/p^(eta b) is finite, since exponential growth dominates
the cubic polynomial. Multiplying those finitely many suprema proves
the bound, including k=1.

Here m²≤C N⁴. Taking eta=epsilon/4 shows

d_4(m²)≤C_epsilon N^epsilon.

Restriction of the four factors to I cannot increase this count, and
boundedness of w gives |W(m²)|≤C_epsilon N^epsilon. The number of
integers m in the closed interval [a−,a+] is at most h/(2π)+1=O(h).
Consequently the total absolute weight of square stationary quadruples
is O_epsilon(h N^epsilon). This estimate allows nonintegral N and
includes squares at either endpoint.

Apply L182's uniform kernel expansion separately to these quadruples.
Since m is an integer,

exp(i(4πm+π/2))=i,
Re(i F(z−,z+))=∫_(z−)^(z+) sin(z²) dz.

The weights are real, so taking real parts and grouping by m proves
(1). The absolute accumulated kernel error is at most

C N^(−2) h^(−1) * h N^epsilon
       =O_epsilon(N^(−2+epsilon)).

The finite Fresnel integral in L182 is uniformly bounded for all these
endpoints, including a saddle at an endpoint. For completeness, on
[−1,1] use length; on either exterior half-line integrate exp(−iz²)
using its derivative −2iz exp(−iz²), bounding endpoint terms by C
and the remaining integral by C∫_1^infinity z^(−2) dz. Splitting any
finite interval into these three pieces proves a universal bound.
Thus |G_m|≤C as well. Because sqrt(2πm)≍N, each kernel is O(N/h).
Multiplication by the total absolute weight just established gives (2).
Choose, for example, epsilon=1/2 to obtain o(1). Conjugate pairing
has the coefficient −1/8 specified in L182, proving the final assertion. ∎

## Scope, verification

The phase i does not make the real contribution zero: the finite Fresnel
factor is complex, and its real projection is exactly G_m. Nor is the
signed weight W(m²) assumed positive. The bound retains all endpoint
factors and proves negligibility by sparsity, without any arithmetic
cancellation assumption. Perfect-square products therefore do not obstruct
an o(1) stationary bound. No such bound is proved for the nonsquare
products, which may include near-square phases, or for the full mixed
moment. First-moment decay, uniform integrability and RH remain unproved.

Verification is analytic: prime-exponent counting, the elementary divisor
bound with eta=epsilon/4, integer endpoint counting, the exact real
projection, and the two normalized error scales are checked above.
No computational or numerical assertion is needed.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
