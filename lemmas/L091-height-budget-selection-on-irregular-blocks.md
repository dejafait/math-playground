# Lemma 91: height-budget selection on irregular blocks

**Hypotheses.** Let 0<x_1<x_2<⋯ with Σ_n x_n^{-2}<∞, and let
0<b_1<b_2<⋯ tend to H<∞. Put a_n=x_n/sqrt(n) and
S={n≥1: a_j≥a_n for all j≥n}. For a nonempty block
B_N=S∩[N,2N), set M_N=|B_N|, A_N=min_{n∈B_N}a_n, and

R_N=N(2+log M_N)/(M_N A_N²),   D_N=b_{4N}−b_N.

Define the actual near sum

Q_n=Σ_{j=n+1}^{2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²].

**Conclusion.** For every nonempty block,

(1/M_N)Σ_{n∈B_N}Q_n≤16 R_N D_N.                         (1)

Each of the following additional conditions suffices for Q_n and the
full upward contribution of the paired product of Lemma 84 to tend to
zero on a common unbounded subsequence of S:

- R_N is bounded above along some unbounded sequence of nonempty blocks;
- writing K={k≥0: B_{2^k} is nonempty}, one has
  Σ_{k∈K}1/R_{2^k}=∞.

Neither condition requires a decay rate for the height deficits.

## Proof

The finite crossing-count argument of Lemma 90, before bounding the
sum of height increments by H, gives

Σ_{n∈B_N}Q_n
 ≤16N A_N^{-2}(2+log M_N) Σ_{r=N}^{4N−1}(b_{r+1}−b_r).

Indeed, all contributing increments have n≤r<j≤2n with
N≤n<2N, so they are contained in this displayed range. Enlarging the
range only adds positive increments. The sum telescopes to D_N;
division by M_N proves (1). All sums here are finite.

As N→∞, 0<D_N≤H−b_N→0. Hence the first condition and (1) force
these block averages to zero. Selecting a minimizing index in each
block and passing to blocks whose starting indices at least double
produces a strictly increasing subsequence with Q_n→0.

For the second condition put Δ_r=b_{r+1}−b_r>0. For every integer
r≥1, the condition 2^k≤r<2^{k+2}, k≥0, holds for at most two k.
For example, if 2^m≤r<2^{m+1}, only k=m and k=m−1 are possible,
with a negative k omitted. Thus, first summing over finitely many k
and then taking the increasing limit,

Σ_{k≥0}D_{2^k}≤2Σ_{r≥1}Δ_r=2(H−b_1)<∞.                (2)

Suppose that for some ε>0 and all sufficiently large k∈K we had
R_{2^k}D_{2^k}≥ε. Positivity of R_{2^k} would imply
D_{2^k}≥ε/R_{2^k}, contradicting (2) and the assumed divergence.
Removing finitely many k cannot remove this divergence, since each
R_{2^k} is finite and positive. Therefore there are strictly increasing
k_l∈K with R_{2^{k_l}}D_{2^{k_l}}<1/l. Select a minimizer n_l of
Q_n in B_{2^{k_l}}. These half-open dyadic blocks are disjoint and
ordered, so n_l increases strictly. Equation (1) gives Q_{n_l}→0.

For either selection, Lemma 84 supplies the product, its simple zeros,
and the bound, for n∈S,

0≤E_f(x_n+i b_n)≤2Q_n+32HΣ_{j>2n}x_j^{-2}
                         +2HΣ_{j>n}x_j^{-2}.

The two convergent-series tails tend to zero. This proves the full
upward-contribution assertion on the same subsequence. ∎

## Qualifications

This resolves a scoped part of the regime where all sufficiently large
nonempty blocks have R_N bounded below by a positive constant. In that
regime the first condition covers any bounded-ratio subsequence, and
the second also permits ratios growing so slowly that their reciprocals
have divergent sum over the nonempty dyadic blocks. For example, the
numerical condition R_{2^k}≤C(k+1) on every sufficiently large dyadic
block, when those blocks are all nonempty, implies the second condition
by harmonic divergence. This is a sufficient conditional observation,
not a constructed coordinate example or a universal growth bound.

The remaining regime can have R_N→∞ over all nonempty blocks and
Σ_{k∈K}1/R_{2^k}<∞. The argument proves no result there: a finite
height-increment budget alone does not contradict the lower bounds
D_{2^k}≥ε/R_{2^k} when their right sides are summable. This limitation
is not a counterexample to the actual near-sum assertion. Divergent
suffix weights and zero lower dyadic density are neither required nor
excluded by this lemma. No RH or theta-specific conclusion follows.

## Verification and formalization obligations

This is an analytic proof and needs no numerical certificate. Audit the
finite increment range inherited from Lemma 90, its telescoping sum,
the twofold overlap including dyadic endpoints and k=0, the passage to
nonnegative infinite sums, divergence after deletion of a finite prefix,
and the ordered subsequence selection. Lemma 90 is used for its finite
crossing estimate; Lemma 84 supplies the product and full-tail bounds.
