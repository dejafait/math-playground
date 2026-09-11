# Lemma 100: upward averaging for arbitrary prescribed interpolation

**Hypotheses.** Let P be any unbounded subset of the positive integers
containing 1. At s∈P put x_s=s^(3/4); between consecutive s<t in P put

x_n=sqrt(n)t^(1/4)(1+(t−n)/(4t)),  s<n<t.

Let 0<b_1<b_2<⋯ tend to H<∞, put w_n=x_n+i b_n, and define

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²),
E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²,

where ρ ranges over zeros counted with multiplicity.

**Conclusion.** The coordinates strictly increase and have summable
reciprocal squares. The product is a nonzero even real entire function
with exactly the simple zeros ±w_n, ±conjugate(w_n). For every N≥1,
with q=1−2^(−3/4)>0,

0≤(1/N)Σ_{n=N}^{2N−1}E_f(w_n)
 ≤ H N^(−1/2)[64(1+log(4N))+18q^(−2)+4].             (1)

In particular the block averages tend to zero and there exists an
increasing subsequence n_k→∞ along which E_f(w_(n_k))→0, for every
permitted height sequence and every such P. The bound is uniform in P
and in heights with a common bound H. The selected indices need not
belong to P and may depend on the heights.

## Proof

Every nonprescribed integer is between two consecutive elements of P,
so the definition is exhaustive. Its value is at least n^(3/4), because
t>n and the factor in parentheses exceeds 1. Hence Σx_n^(−2)≤Σn^(−3/2)<∞.

We first prove the global separation estimate

x_j−x_n ≥ (j^(3/4)−n^(3/4))/3,  j>n.                 (2)

For consecutive prescribed indices s<t, define on the real interval
[s,t] the interpolant g_t(v)=sqrt(v)t^(1/4)(5/4−v/(4t)). Then

g_t'(v)=t^(1/4)(5t−3v)/(8t sqrt(v))
         ≥ t^(1/4)/(4sqrt(v)) ≥ (1/4)v^(−1/4).

Also g_t(t)=t^(3/4) and g_t(s)≥s^(3/4). For each integer
s≤m<t, the discrete difference x_(m+1)−x_m is at least
∫_m^(m+1)(1/4)v^(−1/4)dv. If t=s+1 this follows directly
from the prescribed power values. If t>s+1, the first difference has
an additional nonnegative jump g_t(s)−x_s, the interior differences
are integrals of g_t', and the last difference ends at g_t(t)=x_t.
These cases exhaust every adjacent pair of integers. Summing from
m=n to j−1 proves (2), and also proves strict increase.

Lemma 74 now supplies the product properties and its reflected bound.
The higher zeros are exactly w_j and −conjugate(w_j) for j>n, so

E_f(w_n)=U_n+V_n,
U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],
0≤V_n≤2HΣ_{j>n}x_j^(−2)≤4H n^(−1/2).                (3)

The last inequality uses the integral of t^(−3/2) on [n,∞).
For fixed n, (2) bounds the sufficiently distant terms of U_n by a
constant times H j^(−3/2); its finite prefix has positive denominators.
Thus the full sums are finite.

For N≤n<2N split U_n=A_n+B_n at j=4N. For n<j≤4N,
(2) and the decreasing derivative of v^(3/4) give

x_j−x_n≥(1/4)(4N)^(−1/4)(j−n).

Discarding the squared height difference in the denominator yields

A_n≤64sqrt(N)Σ_{j=n+1}^{4N}(b_j−b_n)/(j−n)².

Use the finite height-increment crossing argument of Lemma 78:
write Δ_r=b_(r+1)−b_r and expand each numerator as
Σ_{r=n}^{j−1}Δ_r. For a fixed r and separation k=j−n, at most
k pairs cross r, since n≤r<n+k. Consequently its coefficient in
the sum over n is at most Σ_{k=1}^{4N}1/k≤1+log(4N).
Only N≤r<4N occurs and the sum of these Δ_r is b_(4N)−b_N≤H.
All rearrangements are finite. Therefore

(1/N)Σ_{n=N}^{2N−1}A_n≤64H N^(−1/2)(1+log(4N)).       (4)

For j>4N and n<2N, (2) gives x_j−x_n≥q j^(3/4)/3.
Thus, by the same integral bound,

B_n≤18Hq^(−2)Σ_{j>4N}j^(−3/2)
    ≤18Hq^(−2)N^(−1/2).                              (5)

Apply these infinite-tail bounds first to finite partial sums and
then take their nonnegative increasing limits. Combining (3)–(5)
proves (1). Since log(N)/sqrt(N)→0, the averages vanish. Choose a
minimum in each finite block [2^k,2^(k+1)); the selected indices
strictly increase and their contributions are bounded by the block
averages. This proves the subsequence conclusion. ∎

## Qualifications and verification

This resolves the existence question for the specified interpolation
family, with no density assumption on P or height convergence rate.
It does not assert selection inside P, a height-independent common
subsequence, vanishing at every index, or a result for arbitrary
increasing coordinates with summable reciprocal squares. It has no
theta-specific or RH implication.

The proof is analytic and needs no numerical certificate. Verification
checks include every adjacent-pair boundary case, integration and the
factor 1/3, the finite coefficient count and cutoff, both integral
tails, and the factor 2 in the full sum. Formalization would require
these estimates, the product conclusions of Lemma 74, enumeration of
P and its consecutive gaps, and finite-block minimum selection.
