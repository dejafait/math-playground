# Lemma 79: rate-free upward averaging for all summable powers

**Hypotheses.** Fix p>1/2. Let x_n=n^p for integers n≥1, and let 0<b_1<b_2<⋯ tend to H<∞. Put w_n=x_n+i b_n and

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

**Conclusion.** The product is a nonzero even real entire function with exactly the simple zeros ±w_n, ±conjugate(w_n). Define the full upward contribution, over all zeros with multiplicity, by

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|².

With c_p=p min(1,4^{p−1})>0 and q_p=1−2^{−p}>0, for every integer N≥1,

0≤(1/N)Σ_{n=N}^{2N−1}E_f(w_n)
 ≤ H N^{1−2p}[2c_p^{-2}(1+log(4N))
                 + 2q_p^{-2}4^{1−2p}/(2p−1) + 2/(2p−1)].       (1)

In particular these block averages tend to zero and liminf_n E_f(w_n)=0, without any height-tail rate assumption.

## Proof

Since Σ_n x_n^{-2}=Σ_n n^{-2p}<∞, Lemma 74 supplies the stated product and exact simple zero set. The zeros above w_n are precisely w_j and −conjugate(w_j), j>n. Therefore E_f(w_n)=U_n+V_n, with

U_n=2Σ_{j>n}(b_j−b_n)/[(j^p−n^p)²+(b_j−b_n)²],

V_n=2Σ_{j>n}(b_j−b_n)/[(j^p+n^p)²+(b_j−b_n)²].

Both converge for each fixed n: for j>2n, j^p−n^p≥q_p j^p, and the numerators are at most 2H. Thus the tails are dominated by convergent multiples of Σ j^{-2p}; the remaining terms are finite.

Fix N≥1 and N≤n<2N. Split U_n into A_n for n<j≤4N and B_n for j>4N. For t∈[N,4N],

p t^{p−1}≥c_p N^{p−1}.

Indeed the derivative decreases when p<1 and increases when p>1, and it equals 1 when p=1. The mean value theorem gives j^p−n^p≥c_p N^{p−1}(j−n) within the finite block. Dropping the nonnegative vertical square yields

A_n≤2c_p^{-2}N^{2−2p}Σ_{j=n+1}^{4N}(b_j−b_n)/(j−n)².       (2)

Use the finite increment-crossing argument of Lemma 78: put Δ_r=b_{r+1}−b_r>0 and expand b_j−b_n=Σ_{r=n}^{j−1}Δ_r. For clarity, for any fixed r and separation k=j−n, the condition n≤r<j permits at most k choices of n, namely r−k+1 through r. The block restrictions can only reduce that count. All separations are at most 4N, so each Δ_r has coefficient at most Σ_{k=1}^{4N}1/k≤1+log(4N). Rearrangement here is finite. Since the increments involved have N≤r<4N and sum to b_{4N}−b_N≤H, averaging (2) gives

(1/N)Σ_{n=N}^{2N−1}A_n
 ≤2c_p^{-2}H N^{1−2p}(1+log(4N)).                         (3)

For j>4N and n<2N one has n/j<1/2, so j^p−n^p≥q_p j^p. The decreasing-function integral estimate, valid since 2p>1, gives

B_n≤2Hq_p^{-2}Σ_{j>4N}j^{-2p}
 ≤(2Hq_p^{-2}/(2p−1)) · (4N)^{1−2p}.                       (4)

Likewise the reflected contribution satisfies

V_n≤2HΣ_{j>n}j^{-2p}
 ≤[2H/(2p−1)]n^{1−2p}
 ≤[2H/(2p−1)]N^{1−2p}.                                 (5)

These infinite-sum estimates hold first for finite partial sums and then for their monotone limits. Combining (3)–(5) proves (1). With p fixed, 2p−1>0, so N^{1−2p}(1+log(4N))→0. Choose a minimum of E_f(w_n) in each finite block 2^m≤n<2^{m+1}. Its value is bounded by that block average, and these indices tend to infinity. Nonnegativity proves the stated lower limit. ∎

## Qualifications

This extends the explicit exponent in Lemma 78 to all powers satisfying reciprocal-square summability. The constants and convergence are not asserted uniform as p decreases to 1/2. At p=1/2 the summability hypothesis fails (indeed |w_n|²=n+b_n²≤n+H²), so this product argument does not cover that endpoint. Neither pointwise convergence of E_f(w_n) nor the unrestricted monotone-coordinate assertion is established. No conclusion about penalty maximizers, theta zeros, signed velocities, or RH follows.

## Verification and formalization obligations

The proof is analytic and needs no numerical certificate. Check the derivative minimum separately for p<1, p=1, and p>1; the exact higher-zero enumeration; the finite increment expansion and at-most-k crossing count; the telescoping height bound; the decreasing p-series integral estimates and their monotone limits; and log(N)/N^{2p−1}→0. Formalization also requires the product and simple zero statement from Lemma 74 and minimum selection in each finite dyadic block. All infinite remainders have explicit bounds uniform over the averaging block.
