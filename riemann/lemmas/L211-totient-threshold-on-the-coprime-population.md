# Lemma 211: totient threshold on the coprime population

**Hypotheses.** Use L202's box F_N with its fixed t>0 and all
inherited geometric restrictions, and L210's coprime subset of S_D
with z=65536. Set B=2^25 and eta=exp(-B)>0.

**Conclusion.** For all sufficiently large real N, more than
(3/131072)#F_N tuples in that coprime subset satisfy
phi(ab)/(ab)>=eta. In particular their number is bounded below
by a positive constant times N³. They retain the selected phase
and occupied full-core window, with the inherited restrictions on W.

**Proof.**

Let A_N be the ordered integer pairs (a,b) with

a in [11N/10,6N/5], ab in J_N=[2N²-2tN^(3/2),2N²-tN^(3/2)],

and write P_N=#A_N. By L202 all factors belong to [N,2N]
eventually, P_N>=(t/48)N^(3/2), and F_N=A_N times A_N.

Fix a prime p<=2N. There are at most N/p+1 integers divisible
by p in the closed interval [N,2N]. For each fixed a in that
interval, the product restriction places b in an interval of length
tN^(3/2)/a<=t sqrt(N), hence permits at most t sqrt(N)+1 integers.
For a fixed b the same product restriction places a in an interval
of length at most t sqrt(N); intersecting with the prescribed
interval for a only decreases the count. Thus a union bound gives

#{(a,b) in A_N: p divides ab}
 <=2(N/p+1)(t sqrt(N)+1)
 <=4t sqrt(N)(N/p+1)

once t sqrt(N)>=1. Division by the lower bound on P_N yields

P_N^(-1) #{(a,b) in A_N: p divides ab}
 <=192(1/p+1/N).                                      (1)

It is harmless that this upper bound can exceed one. Both factor
orientations were counted; no distribution in short intervals is assumed.

The finite totient product, proved by inclusion-exclusion over prime
divisors, gives for each positive integer n

log(n/phi(n))=sum_(p|n) log(p/(p-1)).

Here phi(1)=1 and an empty sum is zero. The elementary inequality
log(1+x)<=x for x>=0 implies log(p/(p-1))<=1/(p-1)<=2/p.
Every prime divisor of ab divides a or b and is therefore at most
2N. Summing this identity over A_N and applying (1) gives

P_N^(-1) sum_(A_N) log(ab/phi(ab))
 <=384 [sum_(p<=2N) 1/p² + N^(-1) sum_(p<=2N) 1/p]
 <=384 [1+(1+log(2N))/N]
 <=768                                                   (2)

for sufficiently large N. For the second inequality enlarge the
prime sums to integer sums: sum_(n=2)^infinity n^(-2)<=
integral_1^infinity x^(-2)dx=1, and the harmonic sum through
floor(2N) is at most 1+log(2N). All averages and prime sums before
these upper comparisons are finite.

A pair with phi(ab)/(ab)<exp(-B) has log(ab/phi(ab))>B.
Nonnegativity of the logarithm and (2) therefore imply

#{bad pairs in A_N}/P_N <=768/B=3/131072.                 (3)

Each first pair has exactly P_N opposite pairs in F_N. Consequently
the fraction of all tuples whose first pair is bad is at most the
same constant, regardless of how phase and coprimality select tuples.
L210 supplies more than (3/65536)#F_N coprime selected tuples.
Deleting all the bad tuples of F_N leaves more than

(3/65536-3/131072)#F_N=(3/131072)#F_N

coprime selected tuples with the required totient threshold. L202's
cardinality bound gives the claimed order N³ lower bound. Taking a
subset preserves L210's geometric conclusions.

## Qualifications and verification

The threshold eta is extremely small but fixed independently of N.
No useful effective threshold for N is claimed. No independence of
arithmetic and phase selection is assumed. This proves the requested
totient selection; the assembly into the negative-strip mass criterion,
a lower bound for a signed total mass, and RH are not asserted here.

Verification is analytic: both factor orientations, closed-interval
rounding for real N, finite prime-sum interchange, the integral and
harmonic comparisons, Markov deletion and the strict surviving margin.
The exact constant equality is 768/2^25=3/131072. No computational
distribution evidence is required.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
