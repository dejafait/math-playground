# Lemma 82: upward averaging for monotone square-root multipliers

**Hypotheses.** Let (L_n)_{n≥1} be positive and nondecreasing, with

Σ_{n≥1} 1/(n L_n²)<∞.

Set x_n=sqrt(n)L_n. Let 0<b_1<b_2<⋯ tend to H<∞, put w_n=x_n+i b_n, and define

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

**Conclusion.** The product is a nonzero even real entire function with exactly the simple zeros ±w_n, ±conjugate(w_n). Define the full upward contribution over all zeros, counted with multiplicity, by

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|².

Put S(M)=Σ_{j>M}1/(j L_j²) for positive integers M and q=1−1/sqrt(2). For every integer N≥1,

0≤(1/N)Σ_{n=N}^{2N−1}E_f(w_n)
 ≤32H(1+log(4N))/L_N²+2Hq^{-2}S(4N)+2HS(N).       (1)

The right side tends to zero. Consequently the full upward block averages tend to zero and liminf_n E_f(w_n)=0, without a height-tail rate or any further regularity of L_n.

## Proof

Since L_n≥L_1>0 and is nondecreasing, x_n is strictly increasing to infinity. Its reciprocal squares are summable by hypothesis. Lemma 74 supplies the product and its exact simple zero set. The higher zeros relative to w_n are exactly w_j and −conjugate(w_j) for j>n. Thus E_f(w_n)=U_n+V_n, with

U_n=2Σ_{j>n}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],

V_n=2Σ_{j>n}(b_j−b_n)/[(x_j+x_n)²+(b_j−b_n)²].

For j>2n, monotonicity gives x_n/x_j≤sqrt(n/j)<1/sqrt(2), so x_j−x_n≥q x_j. The tail of U_n is therefore dominated by 2Hq^{-2}Σ_{j>2n}x_j^{-2}; its preceding terms are finite. Also V_n≤2HS(n). Both defining series converge.

Fix N and N≤n<2N. Split U_n=A_n+B_n at j=4N, with A_n containing n<j≤4N. For this range,

x_j−x_n=L_j(sqrt(j)−sqrt(n))+sqrt(n)(L_j−L_n)
 ≥L_N(j−n)/(sqrt(j)+sqrt(n))
 ≥L_N(j−n)/(4sqrt(N)).

Dropping the vertical square gives

A_n≤32N L_N^{-2}Σ_{j=n+1}^{4N}(b_j−b_n)/(j−n)².

Apply the finite increment-crossing argument of Lemma 78. Explicitly, write Δ_r=b_{r+1}−b_r>0 and b_j−b_n=Σ_{r=n}^{j−1}Δ_r. For fixed r and separation k=j−n, there are at most k eligible n with n≤r<n+k. Since k≤4N, the coefficient of each Δ_r after summing the last display over n and dividing by N is at most

32L_N^{-2}Σ_{k=1}^{4N}1/k≤32L_N^{-2}(1+log(4N)).

Only N≤r<4N occur, and their increments sum to b_{4N}−b_N≤H. These are finite sums, so their rearrangement is legitimate. This proves the first term in (1).

For j>4N and n<2N, the ratio bound gives x_j−x_n≥q x_j. Uniformly in the block,

B_n≤2Hq^{-2}S(4N),    V_n≤2HS(N).

These estimates hold for finite partial sums and then for their increasing limits, proving (1) for the entire infinite contribution.

It remains to prove that the first term vanishes. For N≥4 set m=floor(sqrt(N)). Since L_j≤L_N for j≤N,

S(m)≥Σ_{j=m+1}^N 1/(j L_j²)
 ≥L_N^{-2}Σ_{j=m+1}^N 1/j
 ≥L_N^{-2}log((N+1)/(m+1)).                         (2)

The last inequality follows by integrating 1/t on each [j,j+1]. The logarithm in (2), divided by log N, tends to 1/2: log(N+1)/log N→1 and log(m+1)/log N→1/2. Thus

0≤(log N)/L_N²≤[log N/log((N+1)/(m+1))]S(m)→0,

because the bracket tends to 2 and the convergent-series tail S(m) tends to zero. As (1+log(4N))/log N→1, the first term of (1) vanishes. Both remaining terms vanish by summability. Finally, in each dyadic block choose an index minimizing the finite nonnegative E_f value. These indices tend to infinity and their values are at most the vanishing block averages. This proves the lower-limit assertion. ∎

## Qualifications

The result covers every multiplier specified in the question, including multipliers with jumps; no interpolation, differentiability, slow variation, or explicit formula is used. The monotonicity of x_n/sqrt(n) is an additional geometric hypothesis beyond increasing x_n and summable reciprocal squares. The proof supplies no common numerical decay rate for all multipliers. It does not prove pointwise vanishing, the unrestricted monotone quartet assertion, a statement about penalty maximizers or signed velocities, any theta-specific conclusion, or RH. Lemma 81 motivates the generalization but is not an input to this proof.

## Verification and formalization obligations

This is an analytic proof and requires no numerical certificate. Check strict coordinate increase, the product hypotheses, enumeration of higher zeros, the horizontal gap constant, finite crossing count and endpoints, telescoping, and bounds for both infinite tails. The new limiting step requires the discrete harmonic lower bound (2), monotonicity in its correct direction, floor-square-root asymptotics, and convergence of a summable nonnegative tail. Formalization also requires compact product convergence from Lemma 74, finite rearrangement, increasing limits of nonnegative partial sums, and dyadic minimum selection.
