# Lemma 99: common upward subsequence at consecutive packet endpoints

**Hypotheses.** Take the coordinates of Lemma 98, with
U_k=2^(4k²), d_k=2^(2k²), and n_k=U_k+d_k−1 for k≥2.
Let 0<b_1<b_2<⋯ tend to H<∞. Define the paired product f and
full upward contribution E_f as in Lemma 84, and put

Q_n=Σ_{j=n+1}^{2n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²].

**Conclusion.** The fixed endpoint sequence (n_k), independent of the
heights, satisfies Q_(n_k)→0 and E_f(x_(n_k)+i b_(n_k))→0.
More precisely, writing T_k=U_(k+1),

0≤Q_(n_k)≤H/[T_k^(1/4)−n_k^(1/4)]²≤4H/T_k^(1/2).       (1)

Thus the optimized sufficient criteria obstructed in Lemma 98 can
both fail while the actual near and full upward sums vanish along a
common explicit subsequence for every permitted height sequence.

## Proof

Lemma 98 proves strict increase of the coordinates, summability of
reciprocal squares, and that every n_k is a suffix minimum. Therefore
Lemma 84 supplies f, its exact simple zero set, convergence of its
upward sums, and the far and reflected tail estimates.

Fix k≥2 and abbreviate n=n_k and T=T_k. The next prescribed suffix
index after n is T. For n<j<T the defining interpolation gives

x_j/sqrt(j)=T^(1/4)(1+(T−j)/(4T))≥T^(1/4).

For a prescribed index j≥T the same inequality follows from
x_j/sqrt(j)=j^(1/4). For any other j≥T, its gap ends at some
prescribed t>j≥T and the interpolation is at least t^(1/4).
Consequently every integer j>n satisfies

x_j−x_n≥sqrt(j) T^(1/4)−n^(3/4)
        ≥sqrt(n)[T^(1/4)−n^(1/4)].                      (2)

The bracket is positive. In fact n<2U_k and
T/U_k=2^(8k+4), so n/T<2^(−8k−3)<1/16. Hence
n^(1/4)<T^(1/4)/2, giving a bracket at least T^(1/4)/2.

There are exactly n summands in Q_n. Each numerator is at most H,
and discarding its squared height difference from the denominator
and applying (2) gives

Q_n≤n H/{n[T^(1/4)−n^(1/4)]²}.

This proves both bounds in (1). Since T_k→∞, Q_(n_k)→0.
No bound on the rate of convergence of b_n has been used.

For every n=n_k, Lemma 84's decomposition, with the near term kept
exact, gives

0≤E_f(x_n+i b_n)≤2Q_n+32HΣ_{j>2n}x_j^(−2)
                         +2HΣ_{j>n}x_j^(−2).

The two convergent-series tails tend to zero as n_k→∞. Together with
(1) this proves the full-upward limit along the same endpoints. ∎

## Qualifications and verification

The subsequence works for every permitted height sequence; convergence
is even uniform over such sequences with a common upper bound on H.
This is a result for the explicit coordinates of Lemma 98, not for
arbitrary suffix sets or theta zeros. It does not resolve RH or the
unrestricted upward-subsequence assertion.

The proof is analytic and requires no numerical certificate. The
mathematical checks are the exhaustive normalized-coordinate cases,
positivity and size of the gap, the exact count n of near terms, the
factor 2 in the full contribution, and convergent tail passage.
Formalization would need those inequalities, the fixed subsequence
limit, and the product and tail conclusions of Lemma 84.
