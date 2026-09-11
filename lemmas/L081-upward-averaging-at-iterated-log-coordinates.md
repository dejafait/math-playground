# Lemma 81: upward averaging at iterated-log coordinates

**Hypotheses.** Fix β>1/2 and, for n≥1, put

x_n=sqrt(n log(n+1))(log(log(n+e)))^β.

All logarithms are natural. Let 0<b_1<b_2<⋯ tend to H<∞, put w_n=x_n+i b_n, and define

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

**Conclusion.** This is a nonzero even real entire function with exactly the simple zeros ±w_n, ±conjugate(w_n). Define the full upward contribution, counting all zeros with multiplicity, by

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|².

Write L(t)=sqrt(log(t+1))(log(log(t+e)))^β, q=1−1/sqrt(2), and T(M)=(log(log M))^{1−2β}/(2β−1) for M≥3. For every integer N≥3,

0≤(1/N)Σ_{n=N}^{2N−1}E_f(w_n)
 ≤32H(1+log(4N))/L(N)²+2Hq^{-2}T(4N)+2HT(N).       (1)

In particular the averages tend to zero, with bound O_β(H(log(log N))^{1−2β}), and liminf_n E_f(w_n)=0. No height-tail rate is assumed.

## Proof

The multiplier L(t) is positive and increasing for t>0: both logarithmic factors are positive and increasing there, and β>0. Thus x(t)=sqrt(t)L(t) is strictly increasing and unbounded. For t≥3, log(t+1)≥log t and log(log(t+e))≥log(log t)>0. The function

g(t)=1/(t log t (log(log t))^{2β})

is positive and decreasing on [3,∞), since every denominator factor is positive and increasing. Therefore for integer M≥3,

Σ_{j>M}x_j^{-2}≤Σ_{j>M}g(j)≤∫_M^∞g(t)dt=T(M).       (2)

The integral follows by substituting u=log(log t), and converges because 2β>1. The first three terms are finite, so reciprocal squares are summable. Lemma 74 supplies the product and exact simple zero set.

The higher zeros relative to w_n are precisely w_j and −conjugate(w_j) for j>n. Hence E_f(w_n)=U_n+V_n, where

U_n=2Σ_{j>n}(b_j−b_n)/((x_j−x_n)²+(b_j−b_n)²),

V_n=2Σ_{j>n}(b_j−b_n)/((x_j+x_n)²+(b_j−b_n)²).

For j>2n, increasing L gives x_n/x_j≤sqrt(n/j)<1/sqrt(2), so x_j−x_n≥q x_j. Equation (2) then proves convergence of both series for each n; only finitely many terms precede that bound.

Fix N≥3 and N≤n<2N. Split U_n into A_n with n<j≤4N and B_n with j>4N. For the finite part, increasing L gives

x_j−x_n=L(j)(sqrt(j)−sqrt(n))+sqrt(n)(L(j)−L(n))
 ≥L(N)(j−n)/(sqrt(j)+sqrt(n))
 ≥L(N)(j−n)/(4sqrt(N)).

Dropping the vertical square yields

A_n≤32N L(N)^{-2}Σ_{j=n+1}^{4N}(b_j−b_n)/(j−n)².

Use the finite increment-crossing argument of Lemma 78: write Δ_r=b_{r+1}−b_r>0 and b_j−b_n=Σ_{r=n}^{j−1}Δ_r. For fixed r and k=j−n, at most k possible n satisfy n≤r<n+k. Since k≤4N, each Δ_r has coefficient at most Σ_{k=1}^{4N}1/k≤1+log(4N). The involved increments telescope to b_{4N}−b_N≤H. All these sums are finite, and consequently

(1/N)Σ_{n=N}^{2N−1}A_n≤32H L(N)^{-2}(1+log(4N)).

For j>4N and n<2N, the ratio estimate gives x_j−x_n≥q x_j. Thus, uniformly in the block,

B_n≤2Hq^{-2}Σ_{j>4N}x_j^{-2}≤2Hq^{-2}T(4N).

Also x_j+x_n≥x_j and n≥N imply

V_n≤2HΣ_{j>n}x_j^{-2}≤2HT(N).

These inequalities hold for finite partial sums and pass to their increasing limits. Together they prove (1), controlling the entire infinite contribution.

The first term in (1) is O_β(H(log(log N))^{-2β}), since (1+log(4N))/log(N+1) stays bounded and log(log(N+e))/log(log N) tends to one. The remaining terms are O_β(H(log(log N))^{1−2β}). All tend to zero. In each dyadic block choose an index minimizing the finite nonnegative E_f value. These indices tend to infinity and their values are bounded by the vanishing averages, proving the lower-limit conclusion. ∎

## Qualifications

This answers the stated iterated-log-coordinate question for every fixed β>1/2. Constants are not uniform as β decreases to 1/2. The assertion concerns this explicit geometry, not arbitrary summable coordinates, pointwise convergence, selected penalty maximizers, theta zeros, signed velocities, or RH. Lemma 80 motivates the question but is not a mathematical input.

## Verification and formalization obligations

The proof is analytic and needs no numerical certificate. Check positivity and monotonicity of L and g, the integral substitution and lower endpoint, the exact higher-zero enumeration, the finite horizontal gap bound, the at-most-k increment crossing count, telescoping, the uniform infinite-tail bounds, and the fixed-β limits. Formalization also requires Lemma 74's product and zero set, finite rearrangement, passage to nonnegative series limits, and dyadic minimum selection.
