# Lemma 164: sharpness of the restricted triple diagonal

**Hypotheses.** Let N be a positive real number tending to infinity,
I be the integers in [N,2N], and E(N) count ordered pairs of triples
in I³ with equal products. Define

D3(A)=Σ_m (Σ_(r,s,u∈I:rsu=m) A_r A_s A_u)²

for nonnegative real amplitudes. Fix constants 0<c≤K.

**Conclusion.** For all sufficiently large N there are absolute positive
constants c0,C0 such that

c0 N³(log N)^4 ≤ E(N) ≤ C0 N³(1+log N)^4.                 (1)

If c N^(−1/2)≤A_n≤K N^(−1/2) for every n∈I, then

D3(A) ≍_(c,K) (log N)^4.                                (2)

Thus the exponent four in L163 is sharp for its stated class of
amplitudes, already in one fixed proportional window. This assertion
concerns a positive arithmetic diagonal, not a cutoff-weighted average
or the full oscillatory sixth moment.

**Proof.**

Set η=1/10, h=floor(log2(N)/100), and X=N^(1/3). Choose independently
four integers d11,d12,d21,d22 in [-h,h] and complete the matrix by

d13=−d11−d12,       d23=−d21−d22,
d31=−d11−d21,       d32=−d12−d22,
d33=d11+d12+d21+d22.

Every row and column sum is zero, and |dij|≤4h. For each displacement
matrix choose positive integer entries in the real intervals

xij ∈ [Yij,(1+η)Yij],       Yij=X 2^dij.                 (3)

All row and column products belong to [N,(1+η)³N]⊂[N,2N],
and the product of the nine Yij is N³. There are (2h+1)^4 boxes.
They are disjoint: different displacement matrices differ in at least
one integer exponent, and 1+η<2 makes that coordinate's intervals
disjoint. Uniformly over these boxes,

N^α≤Yij≤N^β,       α=1/3−1/25,   β=1/3+1/25.

In particular β−2α=−1/3+3/25<0.

We prove that each box contains at least c1 N³ matrices whose nine
entries are pairwise coprime, with c1>0 independent of the box and N.
This elementary counting step is needed: arbitrary integer matrices
need not give distinct margins.

Fix an integer P>2000, and let q be the product of all primes at most
P. Restrict every entry in (3) to be 1 modulo q. An interval of length
L contains between L/q−1 and L/q+1 such integers. Here each length
Lij=ηYij is at least Lmin=ηN^α. For sufficiently large N, each
coordinate therefore has at least Lij/(2q) choices. Choose the nine
entries independently and uniformly from these restricted sets.

For a prime p>P the Chinese remainder theorem gives at most
Lij/(qp)+1 choices in coordinate ij divisible by p. Consequently its
probability of divisibility is at most

2/p+2q/Lij ≤ 2/p+2q/Lmin.

For two distinct coordinates independence bounds the probability that
both are divisible by p by the square of this last quantity. All entries
are at most U=(1+η)N^β; a shared prime cannot exceed U. By a union bound,
the probability that a given coordinate pair has a common prime is at most

4/(P−1) + (8q/Lmin)(1+log U) + 4q²U/Lmin².              (4)

Indeed enlarge the prime sums to integer sums and use
Σ_(n>P) n^(−2)≤1/(P−1), Σ_(1≤n≤U) 1/n≤1+log U,
and at most U possible integers. Primes at most P divide none of the
chosen entries. There are 36 unordered coordinate pairs. With P fixed
as above, the constant contribution in 36 times (4) is less than 1/4.
The other contributions tend to zero uniformly, since α>0 and β<2α.
For sufficiently large N their sum is also less than 1/4. At least half
of the restricted matrices are therefore pairwise coprime. Their number
in each box is at least

(1/2) ∏_(i,j) (Lij/(2q)) = η^9 N³ / (2(2q)^9).          (5)

No prime distribution estimate is used, and q is fixed before N tends
to infinity.

For a pairwise coprime matrix let ri be its ith row product and sj its
jth column product. Unique prime factorization gives

gcd(ri,sj)=xij.                                         (6)

To verify this even when entries have prime powers, every prime divides
at most one cell. It occurs in both of these margins exactly when that
cell is their intersection, with the same exponent in both. Thus the
ordered six margins recover the whole matrix, and the map is injective
on all selected boxes together. The row and column total products agree.
Multiplying (5) by (2h+1)^4 proves the lower bound in (1).

For the upper bound apply L163 with a=1, b=2, and A_n=N^(−1/2).
Then D3(A)=N^(−3)E(N). For general amplitudes in the stated range,
expanding the finite square gives

c^6 N^(−3)E(N) ≤ D3(A) ≤ K^6 N^(−3)E(N).

This proves (2). ∎

## Scope and verification

The construction proves sharpness of the unweighted positive diagonal
bound. It does not show that the diagonal survives cancellation in a
full time moment or that it is large on the cutoff transition event.
The cutoff-tail target and RH remain unproved.

Verification is analytic for the uniform sieve estimate and asymptotic
count. The exact finite regression
`python3 scripts/heat/check_triple_sharpness.py` checks the displacement
identities and injectivity on small pairwise coprime matrices; it is not
numerical evidence for the asymptotic bound. Formalization would require
finite interval residue counts, the Chinese remainder theorem, finite
union bounds, the two elementary harmonic bounds, and recovery (6).

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
