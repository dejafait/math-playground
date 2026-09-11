# Lemma 92: spacing-sensitive height-budget selection

**Hypotheses.** Let 0<x_1<x_2<⋯, with Σ_n x_n^{-2}<∞, and
0<b_1<b_2<⋯→H<∞. Set a_n=x_n/sqrt(n) and
S={n≥1: a_j≥a_n for all j≥n}. For a nonempty block
B_N=S∩[N,2N), put M_N=|B_N| and A_N=min_{n∈B_N}a_n.
When M_N≥2 let d_N be the minimum distance between distinct indices
in B_N; when M_N=1 set d_N=N. Write H_m=Σ_{q=1}^m1/q,
with H_0=0 (these harmonic numbers are distinct from the height H).
Define

T_N=N(1+H_{M_N−1}/d_N)/(M_N A_N²),
D_N=b_{4N}−b_N,
Q_n=Σ_{j=n+1}^{2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²].

**Conclusion.** Every nonempty block satisfies

(1/M_N)Σ_{n∈B_N}Q_n≤32 T_N D_N.                    (1)

There is a common unbounded subsequence in S on which Q_n and the
full upward contribution for the paired product of Lemma 84 tend to
zero if either of the following holds:

- T_N has a bounded subsequence over unbounded nonempty blocks;
- Σ_{k: B_{2^k}≠∅}1/T_{2^k}=∞.

In particular, the first condition holds if along such blocks
N/(M_N A_N²) is bounded and d_N≥c(1+log M_N) for a fixed c>0.

## Proof

Fix a block and abbreviate M=M_N, A=A_N and d=d_N. The suffix
separation estimate used in Lemma 90 gives, for n∈B_N and n<j≤2n,

x_j−x_n≥A(j−n)/(4sqrt(N)).

Put Δ_r=b_{r+1}−b_r>0. Dropping the squared height difference from
the denominator and expanding the finite height increments gives

Σ_{n∈B_N}Q_n
 ≤16N A^{-2} Σ_{r=N}^{4N−1} Δ_r C_r,

where

C_r=Σ_{n∈B_N, n≤r} Σ_{1≤k≤n, r<n+k} k^{-2}.

Empty inner sums are zero. For n≤r set ℓ=r−n+1≥1. Extending the
inner sum to all integers k≥ℓ and using a decreasing integral yields

Σ_{k=ℓ}^∞k^{-2}≤ℓ^{-2}+∫_ℓ^∞t^{-2}dt≤2/ℓ.

List the eligible n in decreasing order as n_0>n_1>⋯>n_{p−1}.
For M≥2, spacing implies r−n_q+1≥1+qd. Consequently

C_r≤2Σ_{q=0}^{p−1}1/(1+qd)
 ≤2(1+H_{M−1}/d).

If p=0 the bound is immediate; if M=1 it follows from C_r≤2,
so the stated convention also covers singleton blocks. Summing Δ_r
telescopes to D_N, and dividing by M proves (1). All rearrangements
before the elementary numerical-series bound are finite.

For the first criterion, D_N≤H−b_N→0, so (1) makes the selected
block averages tend to zero. Pass to block starts at least doubling
and choose a minimizing index in each block to obtain an increasing
subsequence with Q_n→0.

For the second criterion use the height-budget identity proved in
Lemma 91: Σ_{k≥0}D_{2^k}≤2(H−b_1)<∞. If T_{2^k}D_{2^k} were
bounded below by some ε>0 on all sufficiently large nonempty dyadic
blocks, then D_{2^k}≥ε/T_{2^k} there, contradicting that finite sum.
Thus their products have liminf zero. Choose increasing k_l with
T_{2^{k_l}}D_{2^{k_l}}<1/l and minimize Q in each block. Disjoint
ordered dyadic blocks and (1) give the required increasing subsequence.

Lemma 84 supplies the paired product and, for n∈S, the estimate

0≤E_f(x_n+i b_n)≤2Q_n+32HΣ_{j>2n}x_j^{-2}
                         +2HΣ_{j>n}x_j^{-2}.

Both tails vanish, proving the common-subsequence conclusion. Finally,
H_{M−1}≤1+log M for M≥1, so the stated spacing condition bounds
1+H_{M−1}/d by 1+1/c and proves the particular criterion. ∎

## Qualifications

This is a scoped sufficient condition for the remaining near-sum
problem, not a universal resolution or a counterexample. The old ratio
R_N=N(2+log M_N)/(M_N A_N²) ignores spacing. For blocks with
M_N→∞ and d_N growing at least as fast as log M_N, the new factor
1+H_{M_N−1}/d_N stays bounded while 2+log M_N diverges. Thus the
new estimate removes a loss for separated suffix indices. This
comparison is algebraic; no construction realizing all the residual
regime's conditions is asserted here. In particular, divergent suffix
weights, zero lower density, R_N→∞ and summable dyadic 1/R_N do
not by themselves verify either new criterion.

A single close pair makes d_N small even when most indices are far
apart. The estimate need not capture that finer geometry. The problem
remains open when T_N→∞ over nonempty blocks and the dyadic inverse
T_N sum converges. No theta-specific statement or RH conclusion follows.

## Verification and formalization obligations

Check the separation estimate, the equivalence r<n+k to k≥r−n+1,
the finite increment range, the numerical tail integral, backwards
spacing including empty and singleton sets, and telescoping. The
height-budget overlap and divergence argument require nonnegative
sums and deletion of finite prefixes only. Audit ordered minimizing
subsequences and both reciprocal-square tails. This analytic result
requires no numerical certificate. Lemma 90 supplies the separation
argument, Lemma 91 the dyadic budget, and Lemma 84 the product and tails.
