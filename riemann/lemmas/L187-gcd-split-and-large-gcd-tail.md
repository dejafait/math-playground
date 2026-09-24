# Lemma 187: gcd split and large-gcd tail

**Hypotheses.** Use L186's notation and sufficiently large N, with
rho=N^(−1/2). For g dividing m write t=m/g and define

E_(m,g,s)={ell∈Z: L_m/g≤ell≤U_m/g, ell≠0,
                         ell≡−g t² (mod s)}.

Sum s over positive integers with N²≤gs≤4N² and gcd(t,s)=1.
Pair weights outside their support are zero, as in L186.

**Conclusion.** There is the exact signed identity

B_N=Σ_(m∈M) Σ_(g|m) Σ_s P(gs)
       Σ_(ell∈E_(m,g,s)) Q((g t²+ell)/s) H_m(g ell).       (1)

Every contributing ell satisfies gcd(ell,s)=gcd(g,s). Each inner set
has at most one element. No endpoint is rounded or symmetrized in (1).

Let B_N^(≥G) denote (1) restricted to g≥G, for any real G≥1.
Uniformly in G, for every epsilon>0,

|B_N^(≥G)| ≤ C_epsilon h N^(3/2+epsilon)/G.                (2)

The same bound holds with every summand replaced by its absolute value.
In particular B_N^(≥N^(1/2+delta))/(Nh)=o(1) for each fixed delta>0.
For G=1 this gives only O_epsilon(N^(1/2+epsilon)) after normalization;
it does not prove the cancellation criterion in L186.

**Proof.**

In each term of L186 set g=gcd(m,u), t=m/g, s=u/g. Then
m²+r=uv is equivalent to r=g ell and sv=g t²+ell.
Conversely these substitutions, with gcd(t,s)=1, give exactly the
original gcd and integer v. The bounds on ell are exactly those on r,
and ell≠0 excludes precisely the squares. This is a bijective finite
reindexing, proving (1) without changing signed weights.
The congruence implies gcd(ell,s)=gcd(g t²,s)=gcd(g,s), because t
is a unit modulo s. This necessary gcd equality is not substituted for
the stronger congruence. The ell interval has length (U_m−L_m)/g;
its residue spacing is s, and their ratio is (U_m−L_m)/(gs)<1
by L186. Thus it contains at most one admissible ell, including when
s=1. Empty intervals remain empty.

For the bound, choose R=C N^(3/2) uniformly bounding |r| in L186.
For fixed m,g there are at most 2 floor(R/g)≤2R/g nonzero
multiples r of g. This bound has no additive constant; in particular
there are no terms if g>R. For each such r the positive integer
k=m²+r is O(N⁴). Expanding absolute pair weights by the triangle
inequality bounds their sum over all u,v with uv=k by a fixed constant
times d_4(k), the number of ordered positive four-factor representations.
The elementary fixed-order divisor bound gives d_4(k)=O_eta(k^eta)
for every eta>0. Restricting to the gcd sector can only decrease this
absolute bound. Also H_m(r)=O(1) by L186.

For completeness, the divisor bound follows from
 d_j(k)=product_(p^a||k) binomial(a+j−1,j−1).
For sufficiently large primes the polynomial in a is bounded by p^(eta a)
for every a≥1 (use binomial(a+j−1,j−1)≤j^a); for each of the finitely
many smaller primes the ratio to p^(eta a) is bounded uniformly in a.
Multiplication proves the bound, also for j=2.

The absolute sum for fixed m,g is therefore O_eta(N^(4eta)R/g).
There are O(h) values of m, since h≍N^(3/2) and M has length O(h).
For each m=O(N²),

Σ_(g|m, g≥G) 1/g ≤ d_2(m)/G = O_eta(N^(2eta)/G).

Combining these bounds and choosing eta=epsilon/6 proves (2).
For G=N^(1/2+delta), divide by Nh and choose epsilon<delta.
No cancellation or probabilistic residue distribution has been assumed. ∎

## Scope and verification

This proves a saving for a restricted large-gcd sector, not an improvement
of the full absolute bound. In the g=1 sector the necessary gcd condition
is merely gcd(ell,s)=1; the proof still allows O(N^(3/2)) displacements
for each m. A further gain from the full congruence, or from signed weights,
is not ruled out and remains unproved. No lower bound for the actual
profile-weighted sum is asserted. RH remains unresolved.

`python3 scripts/heat/check_gcd_residue_split.py` tests the exact bijection,
necessary gcd equality, signed sums and closed and empty endpoint cases.
The asymptotic tail bound is proved above, not inferred from these tests.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
