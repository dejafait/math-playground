# Lemma 94: exact crowding height-budget selection

**Hypotheses.** Let 0<x_1<x_2<⋯, Σ_n x_n^(-2)<∞, and
0<b_1<b_2<⋯→H<∞. Put a_n=x_n/sqrt(n) and
S={n≥1: a_j≥a_n for every j≥n}. For every nonempty block
B_N=S∩[N,2N), set M_N=|B_N|, A_N=min_{n∈B_N}a_n, and

C_N=max_{r∈integers, N≤r<4N} Σ_{n∈B_N,n≤r}1/(r−n+1),
V_N=N C_N/(M_N A_N²),   D_N=b_{4N}−b_N,
Q_n=Σ_{j=n+1}^{2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²].

**Conclusion.** Every nonempty block satisfies

(1/M_N)Σ_{n∈B_N}Q_n≤32 V_N D_N.                         (1)

A common unbounded subsequence in S has Q_n→0 and full paired-product
upward contribution E_f(x_n+i b_n)→0 if either V_N has a bounded
subsequence over unbounded nonempty blocks, or
Σ_{k≥0: B_(2^k)≠∅}1/V_(2^k)=∞. The product and E_f are those of
Lemma 84. With the spacing convention and T_N of Lemma 92, V_N≤T_N.

## Proof

Use the finite separation and increment expansion in Lemma 92. Writing
Δ_r=b_{r+1}−b_r, it gives

Σ_{n∈B_N}Q_n≤16N A_N^(-2) Σ_{r=N}^{4N−1}Δ_r
  Σ_{n∈B_N,n≤r} Σ_{1≤k≤n, k≥r−n+1} k^(-2).

For every integer ℓ≥1, the decreasing integral bound gives
Σ_{k=ℓ}^∞k^(-2)≤ℓ^(-2)+1/ℓ≤2/ℓ. Thus the coefficient of
Δ_r is at most 2C_N. Telescoping the increments and dividing by M_N
proves (1). The increment expansion is finite; only a convergent
positive numerical series is used to bound its coefficients.

At r equal to any member of B_N its own summand is 1, so C_N≥1.
It is finite, and V_N is finite and strictly positive. Also
D_N≤H−b_N→0. A bounded-V subsequence therefore has block averages
tending to zero. Select block starts at least doubling and minimize Q_n
in each block to obtain an increasing sequence with Q_n→0.

For the second condition, Lemma 91 gives
Σ_{k≥0}D_(2^k)≤2(H−b_1)<∞. If V_(2^k)D_(2^k)≥ε>0 on all
sufficiently large nonempty dyadic blocks, this implies
D_(2^k)≥ε/V_(2^k) there, a contradiction. Hence select increasing
k_l with V_(2^{k_l})D_(2^{k_l})<1/l and minimize Q_n in these
ordered disjoint blocks. Equation (1) gives the required near-sum limit.

For either selection, Lemma 84 supplies the product and the estimate

0≤E_f(x_n+i b_n)≤2Q_n+32HΣ_{j>2n}x_j^(-2)
                         +2HΣ_{j>n}x_j^(-2),  n∈S.

Both convergent-series tails vanish on the selected sequence.
Finally, listing eligible indices backwards as in Lemma 92 gives
C_N≤1+H_{M_N−1}/d_N, including singleton blocks, where H_m is the
mth harmonic number. This proves V_N≤T_N. ∎

## Qualifications and verification

The crowding quantity is exact as defined; the estimate (1) still uses
upper bounds for the finite reciprocal-square coefficients and coordinate
separation. No optimality is asserted. Neither criterion is proved to
hold for all permitted coordinates. This is not a theta-specific or RH
result. Check the finite increment range, integer tail cutoff, positivity
of V_N, dyadic height budget, subsequence ordering, and full tails.
Formalization would require these same statements and the finite maximum
defining C_N. The proof is analytic and needs no numerical certificate.
