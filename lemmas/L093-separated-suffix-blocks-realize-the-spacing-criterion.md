# Lemma 93: separated suffix blocks realize the spacing criterion

**Hypotheses and construction.** For integers k≥1 put
U_k=2^(4k²), d_k=2^(2k²), and define the set of positive integers

P={1} ∪ ⋃_{k≥1}{U_k+j d_k: 0≤j<d_k}.

Set x_s=s^(3/4) for s∈P. For every integer n strictly between
consecutive members s<t of P set

x_n=sqrt(n) t^(1/4)(1+(t−n)/(4t)).                       (1)

Let a_n=x_n/sqrt(n), S={n: a_j≥a_n for all j≥n}, and use the
block quantities M_N,A_N,R_N,T_N of Lemmas 91–92. In particular,
B_N=S∩[N,2N), A_N=min_{n∈B_N}a_n, and these ratios are defined
only for nonempty blocks. The minimum spacing convention for a
singleton is that of Lemma 92.

**Conclusion.** The coordinates increase strictly and satisfy
Σ_n x_n^(-2)<∞. They have all the following properties:

- S=P and Σ_{n∈S}n/x_n²=∞;
- liminf_{N→∞}M_N/N=0, allowing empty blocks in this density;
- R_N→∞ as N→∞ over all nonempty integer blocks;
- Σ_{k≥0: B_(2^k)≠∅}1/R_(2^k)<∞;
- T_(U_k)≤2 for every k≥1.

Consequently, for every positive strictly increasing bounded height
sequence, Lemma 92 gives a common unbounded subsequence of suffix
indices on which the actual near sum and full paired-product upward
contribution tend to zero.

## Proof

The set P is unbounded, contains 1, and its clusters are disjoint:
U_(k+1)/U_k=2^(8k+4)>4. Thus (1) and the prescribed values define
every positive integer coordinate uniquely.

For consecutive s<t in P, extend the right side of (1) to a real
function g on [s,t]. Direct differentiation gives

g'(v)=t^(1/4)(5t−3v)/(8t sqrt(v))>0.

Moreover g(t)=t^(3/4)=x_t and

g(s)=sqrt(s)t^(1/4)(1+(t−s)/(4t))>s^(3/4)=x_s.

Hence all coordinates in this interval increase strictly, including
both boundaries. If there is no interior integer, x_s<x_t directly.
The whole sequence is therefore strictly increasing. For an interior
index n<t, formula (1) gives x_n≥sqrt(n)t^(1/4)≥n^(3/4), and the
same bound is equality at prescribed indices. Comparison with the
convergent p-series Σn^(-3/2) proves reciprocal-square summability.

On each gap interior, a_n=t^(1/4)(1+(t−n)/(4t)) exceeds
a_t=t^(1/4), so no such n is in S. At any s∈P, every later
prescribed value a_t=t^(1/4) exceeds a_s. Every later gap value
exceeds its right endpoint's normalized value, which also exceeds
a_s. Thus s∈S and S=P exactly.

In the kth cluster there are d_k=sqrt(U_k) indices, all below 2U_k.
Each has n/x_n²=1/sqrt(n)≥1/sqrt(2U_k). Its total suffix weight
is therefore at least 1/sqrt(2). Disjoint clusters prove divergence.
The block [2U_k,4U_k) contains no suffix index, since the kth
cluster ends below 2U_k and U_(k+1)>4U_k. These empty blocks
prove the asserted zero lower density.

We next treat all integer blocks, not just aligned ones. For N≥2,
a block [N,2N) cannot intersect two clusters. Indeed, if it met a
cluster based at U and a later one based at V, it would have
N<2U and V<2N, hence V<4U, contrary to the cluster ratios.
If the block is nonempty and meets the cluster based at U, then
U<2N and therefore

1≤M_N≤sqrt(U)<sqrt(2N),       A_N²<sqrt(2N).

The function f(m)=(2+log m)/m decreases on [1,∞), since
f'(m)=−(1+log m)/m²<0. It follows that

R_N = (N/A_N²) f(M_N)
    ≥ sqrt(N/2) f(sqrt(2N))
    = (2+(1/2)log(2N))/2 →∞.                            (2)

Weak inequalities suffice here even though some bounds are strict.
This proves the required limit over every nonempty block.

Each cluster lies entirely in the single half-open dyadic block
[U_k,2U_k), since U_k is a power of two. The only other nonempty
dyadic block is [1,2). At N=U_k the exact values are

M_N=d_k,    A_N²=sqrt(U_k)=d_k,    minimum spacing=d_k.

Consequently

R_(U_k)=2+log d_k=2+2k² log 2,
T_(U_k)=1+H_(d_k−1)/d_k≤2,

where the last bound uses H_(d_k−1)≤d_k−1. At N=1, R_1=2.
The dyadic reciprocal-ratio sum is thus exactly

1/2+Σ_{k≥1}1/(2+2k² log 2)<∞,

by comparison with Σk^(-2). This proves every geometric assertion.
The coordinate and bounded-T hypotheses of Lemma 92 now hold for
any heights in the statement, giving its common-subsequence conclusion. ∎

## Qualifications

This realizes a new sufficient condition inside the preceding residual
regime. It is an example of vanishing along a subsequence, not an
obstruction to vanishing. The generic near-sum problem remains open
when neither spacing criterion applies. Nothing here identifies these
coordinates with theta zeros or changes the unresolved RH argument.

## Verification and formalization obligations

Audit the partition by consecutive prescribed indices, the derivative
and both boundaries, the exact suffix set, the p-series comparisons,
and the distinction between arbitrary integer blocks and aligned dyadic
blocks. Equation (2) requires both the upper bound on A_N² and the
monotonicity of f. Check the half-open endpoints, the singleton block
[1,2), and the finite harmonic bound. This analytic construction needs
no numerical certificate. Lemmas 91 and 92 supply the ratio definitions;
Lemma 92 alone supplies the final upward-subsequence theorem.
