# Lemma 95: paired suffix blocks realize exact crowding

**Construction.** For k≥1 let U_k=2^(4k²), d_k=2^(2k²), and set

P={1} ∪ ⋃_{k≥1}{U_k+j d_k+e: 0≤j<d_k, e∈{0,1}}.

For s∈P set x_s=s^(3/4). Between consecutive s<t in P set

x_n=sqrt(n)t^(1/4)(1+(t−n)/(4t)),   s<n<t.               (1)

Use S, B_N, M_N, A_N, C_N, V_N as in Lemma 94, and the
minimum-spacing ratio T_N from Lemma 92. Ratios are defined only
for nonempty blocks; empty blocks are allowed when discussing density.

**Conclusion.** These coordinates strictly increase and have
Σ_n x_n^(-2)<∞. Moreover:

- S=P, and Σ_{n∈S}n/x_n²=∞;
- liminf_{N→∞}M_N/N=0;
- T_N→∞ over all nonempty integer blocks;
- Σ_{m≥0: B_(2^m)≠∅}1/T_(2^m)<∞;
- V_(U_k)≤2 for every k≥1.

Thus, for every positive strictly increasing bounded height sequence,
Lemma 94 gives a common vanishing subsequence for Q_n and the full
paired-product upward contribution, despite failure of both criteria
in Lemma 92.

## Proof

Every cluster lies in [U_k,2U_k): its last point is 2U_k−d_k+1<2U_k,
since d_k≥4. Also U_(k+1)/U_k=2^(8k+4)>4. The prescribed set is
therefore unbounded with disjoint ordered clusters and contains 1.
The interpolation argument of Lemma 93 applies to this set. Explicitly,
the continuous gap function has derivative

t^(1/4)(5t−3v)/(8t sqrt(v))>0,   s≤v≤t.

Its value at s exceeds s^(3/4), and its value at t equals t^(3/4).
For adjacent prescribed indices there is no gap interior and their
values increase directly. This proves strict increase at every index.
Formula (1) gives x_n≥n^(3/4); hence Σx_n^(-2)≤Σn^(-3/2)<∞.
Every gap interior has a_n>a_t=t^(1/4), so is not a suffix minimum.
At a prescribed s, later prescribed normalized values are larger, and
later gap values exceed their right endpoint's normalized value.
Thus S=P exactly.

There are 2d_k points in the kth cluster, each below 2U_k. Its suffix
weight is at least 2d_k/sqrt(2U_k)=sqrt(2). Disjoint clusters prove
divergence. The blocks [2U_k,4U_k) contain no prescribed point, proving
zero lower density.

For N≥2 a block [N,2N) meets at most one cluster: if it met clusters
based at U<V, then N<2U and V<2N, giving V<4U, a contradiction.
On a nonempty block meeting the cluster based at U, we have U<2N and

M_N≤2sqrt(U)<2sqrt(2N),   A_N²<sqrt(2N).                (2)

The intersection with that cluster is a consecutive portion of its
ordered points, which alternate paired gaps 1 and inter-pair gaps d_k−1.
Every three consecutive points include a complete pair. Thus M_N≥3
forces minimum spacing 1. In this case, with M=M_N,

T_N=N(1+H_{M−1})/(M A_N²).

If M≤N^(1/4), this is at least N^(1/4)/sqrt(2). If M>N^(1/4),
(2) gives N/(M A_N²)>1/4, and H_{M−1}≥log M by integrating 1/t
on [1,M]. Therefore T_N>(log N)/16. For M≤2, irrespective of the
spacing convention, T_N≥N/(M A_N²)>sqrt(N/2)/2.
All three lower bounds tend to infinity, proving the limit over every
nonempty integer block, not merely aligned blocks.

The only nonempty dyadic blocks are [1,2) and [U_k,2U_k). For the
latter M=2d_k, A²=d_k, and minimum spacing is 1. Consequently

T_(U_k)=(1+H_{2d_k−1})/2.

Since H_{2d_k−1}≥log(2d_k)≥2k² log 2,
1/T_(U_k)≤1/(k² log 2). Also T_1=1. Comparison with Σk^(-2)
proves summability of all nonempty dyadic inverse T_N.

To bound crowding, split the kth cluster into its two arithmetic grids,
one for each e∈{0,1}. For any eligible integer r, list points of either
grid at most r backwards. Successive distances r−n+1 are at least
1, 1+d_k, 1+2d_k, …, so that grid contributes at most

1+H_{d_k−1}/d_k≤2.

An empty grid contributes zero. Thus C_(U_k)≤4 uniformly over every
r in the defining maximum, and

V_(U_k)=U_k C_(U_k)/(2d_k²)=C_(U_k)/2≤2.

Lemma 94 now applies for every height sequence stated above. ∎

## Qualifications and verification

This realizes the exact-crowding improvement in all the requested
residual conditions. Failure of the earlier sufficient criteria is not
failure of the near-sum assertion. Nothing identifies these coordinates
with theta zeros or proves RH. No claim is made about general coordinates
for which V_N tends to infinity and its dyadic inverses are summable.
The analytic proof needs no numerical certificate. Formalization should
check gap boundaries including adjacent prescribed points, exact suffix
membership, half-open dyadic endpoints, the consecutive-portion argument,
the three uniform lower bounds, and the separate-grid harmonic estimate.
