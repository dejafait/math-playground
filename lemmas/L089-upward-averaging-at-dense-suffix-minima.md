# Lemma 89: upward averaging at dense suffix minima

**Hypotheses.** Let 0<x_1<x_2<⋯ with Σ_n x_n^{-2}<∞, and let
0<b_1<b_2<⋯ tend to H<∞. Set a_n=x_n/sqrt(n) and
S={n≥1: a_j≥a_n for every j≥n}. Suppose there are δ>0 and N_0
such that, for every integer N≥N_0,

M_N=|S∩[N,2N)|≥δ N.

**Conclusion.** Define the actual near sum by

Q_n=Σ_{j=n+1}^{2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²].

Then M_N^{-1}Σ_{n∈S∩[N,2N)} Q_n→0. In particular there is an
unbounded subsequence of S on which Q_n→0 and the full upward
contribution E_f(x_n+i b_n) of the paired product in Lemma 84 tends
to zero. No rate condition on the height increments is imposed.

## Proof

Lemma 84 supplies the product, convergence of its upward sums, and the
far and reflected estimates used below. For sufficiently large N put
B_N=S∩[N,2N), t_N=min B_N, and A_N=a_{t_N}>0.
The suffix property implies a_n≥A_N for every n∈B_N.

First we show (log N)/A_N²→0. Put m=ceil(sqrt(N)) and
p=floor(N/2). For every integer m≤j≤p, density supplies an index
r∈S∩[j,2j). In particular r<2j≤N≤t_N. Since r∈S,
a_r≤a_{t_N}=A_N. Coordinate monotonicity therefore gives

x_j²≤x_r²=r a_r²≤2j A_N².

Consequently, with R(m)=Σ_{j≥m}x_j^{-2},

R(m)≥(1/(2A_N²))Σ_{j=m}^p 1/j
    ≥(1/(2A_N²))log((p+1)/m).

The harmonic lower bound follows by integration on each [j,j+1].
The logarithm divided by log N tends to 1/2. Thus

0≤(log N)/A_N²≤[2 log N/log((p+1)/m)]R(m)→0.       (1)

All denominators are positive for sufficiently large N. Summability
makes R(m) tend to zero, while the bracket tends to 4.

For n∈B_N and n<j≤2n<4N, the suffix inequality gives

x_j−x_n≥a_n(sqrt(j)−sqrt(n))
       ≥A_N(j−n)/(4sqrt(N)).

Indeed sqrt(j)+sqrt(n)<(2+sqrt(2))sqrt(N)<4sqrt(N).
Discarding the nonnegative vertical square from each denominator yields

Q_n≤16N A_N^{-2}Σ_{j=n+1}^{2n}(b_j−b_n)/(j−n)².    (2)

Write Δ_r=b_{r+1}−b_r>0 and expand b_j−b_n=Σ_{r=n}^{j−1}Δ_r.
These are finite sums. For a fixed r and a fixed separation k=j−n,
the condition n≤r<n+k allows at most k integer choices of n, even
before restricting to B_N and j≤2n. Every eligible k is at most 4N.
Hence the coefficient of Δ_r in the double sum on the right of (2),
summed over n∈B_N, is at most

Σ_{k=1}^{4N} k/k²≤1+log(4N).

All eligible r lie in [N,4N). Their increments sum to at most
b_{4N}−b_N≤H. Dividing (2) by M_N≥δ N proves

0≤M_N^{-1}Σ_{n∈B_N}Q_n
 ≤(16H/δ)(1+log(4N))/A_N²→0                      (3)

by (1). In each block N=2^k choose a minimizing index n_k∈B_N.
These indices are strictly increasing, and (3) implies Q_{n_k}→0.
Lemma 84 gives, for every n∈S,

0≤E_f(x_n+i b_n)≤2Q_n+32HΣ_{j>2n}x_j^{-2}
                         +2HΣ_{j>n}x_j^{-2}.

Both tails vanish. This proves the full upward assertion along n_k. ∎

## Qualifications

The density assumption is additional and the proof does not settle
arbitrary irregular suffix sets. It covers cases outside the summable
suffix-weight hypothesis: x_n=n has S equal to all positive integers
and Σ_{n∈S}n/x_n²=∞. The proof also permits a_n to oscillate away from
S; it never assumes global monotonicity of a_n. No assertion about
pointwise convergence, signed motion, theta-specific zeros, or RH follows.

## Verification and formalization obligations

This is an analytic proof; no numerical certificate is required. Check
the density application at each integer j, ordering r<t_N, direction
of the suffix inequality, harmonic lower bound and floor/ceiling limit,
finite crossing count, the normalization by M_N, and the disjoint dyadic
selection. Lemma 84 is the sole direct lemma input, supplying the product
and full-tail estimates. The finite crossing argument is proved here.
