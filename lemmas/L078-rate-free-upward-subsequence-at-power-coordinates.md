# Lemma 78: rate-free upward subsequence at power coordinates

**Hypotheses.** Let x_n=n^{2/3}, n≥1, and let 0<b_1<b_2<⋯ tend to a finite H. Put w_n=x_n+i b_n and

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

**Conclusion.** For the full upward contribution over zeros counted with multiplicity,

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²,

one has

(1/N)Σ_{n=N}^{2N−1} E_f(w_n) → 0,

and hence liminf_n E_f(w_n)=0. No rate of convergence of b_n to H is assumed.

## Proof

The coordinates satisfy Σ x_n^{-2}=Σ n^{-4/3}<∞. Lemma 74 therefore supplies the entire product, its exact simple zero set, and the decomposition E_f(w_n)=U_n+V_n, where

U_n=2Σ_{j>n}(b_j−b_n)/[(j^{2/3}−n^{2/3})²+(b_j−b_n)²],

0≤V_n≤2HΣ_{j>n}j^{-4/3}.

For each fixed n the U_n series is finite: once j>4n the horizontal distance is at least q j^{2/3}, where q=1−2^{-2/3}>0, so the tail is dominated by 2Hq^{-2}Σ j^{-4/3}. Only finitely many other terms occur.

Fix an integer N≥1 and split U_n, for N≤n<2N, into A_n with n<j≤4N and B_n with j>4N. All sums below are nonnegative.

### Finite block: count each height increment

The derivative of t^{2/3} is decreasing. For n<j≤4N the mean value theorem gives

j^{2/3}−n^{2/3} ≥ (2/3)(4N)^{-1/3}(j−n).

Dropping the vertical square in the denominator thus gives, with C_0=(9/2)4^{2/3},

A_n≤C_0 N^{2/3} Σ_{j=n+1}^{4N}(b_j−b_n)/(j−n)².       (1)

Write Δ_r=b_{r+1}−b_r>0 and expand b_j−b_n=Σ_{r=n}^{j−1}Δ_r. These are finite sums, so summing (1) over N≤n<2N and rearranging is legitimate. For any fixed N≤r<4N and any separation k=j−n, the pairs crossing r satisfy n≤r<n+k, so n belongs to the k integers r−k+1,…,r. The additional block restrictions only reduce their number. Also k≤4N. Consequently the coefficient of Δ_r in the double sum is at most

Σ_{k=1}^{4N} k/k² ≤ 1+log(4N).

Since Σ_{r=N}^{4N−1}Δ_r=b_{4N}−b_N≤H, we obtain

(1/N)Σ_{n=N}^{2N−1} A_n
 ≤ C_0 H N^{-1/3}(1+log(4N)).                         (2)

### Infinite tail and reflection

If j>4N and n<2N, then n/j<1/2 and j^{2/3}−n^{2/3}≥q j^{2/3}. The decreasing-function integral bound gives

B_n≤2Hq^{-2}Σ_{j>4N}j^{-4/3}
 ≤6Hq^{-2}(4N)^{-1/3}.                              (3)

Similarly, for n≥N,

V_n≤2HΣ_{j>n}j^{-4/3}≤6H n^{-1/3}≤6H N^{-1/3}.       (4)

The tail estimates follow first for finite sums and then by monotone limits. Combining (2)–(4) yields the explicit bound

0≤(1/N)Σ_{n=N}^{2N−1} E_f(w_n)
 ≤H N^{-1/3}[C_0(1+log(4N))+6q^{-2}4^{-1/3}+6].      (5)

Its right side tends to zero. In each dyadic block N=2^m choose an index attaining the smallest E_f(w_n). Its value is at most the block average, and the chosen indices tend to infinity. This proves the lower-limit assertion. ∎

## Qualifications

This resolves the concrete height-rate question left after Lemma 77. Monotonicity is used in the nonnegative increment expansion, and the explicit coordinate geometry is used both in (1) and (3). The result does not assert convergence along every index or for arbitrary coordinates satisfying reciprocal-square summability. It makes no assertion about quadratic-penalty maximizers, theta zeros, signed zero velocities, or RH.

## Verification and formalization obligations

The proof is analytic; no numerical certificate is required. Check the decreasing derivative bound, the at-most-k pairs crossing a fixed increment, the finite rearrangement, the telescoping height sum, both integral tails, and log(N)/N^{1/3}→0. Formalization also needs Lemma 74's product and zero set, the exact higher-zero enumeration, and finite-block minimum selection. No varying-index limit is interchanged with an uncontrolled infinite sum.
