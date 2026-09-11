# Lemma 74: finite successor windows cannot sustain upward motion

**Hypotheses.** Let 0<x_1<x_2<⋯ tend to infinity and let 0<b_1<b_2<⋯ tend to a finite H>0. Put w_n=x_n+i b_n and suppose Σ_n x_n^{-2}<∞. Consider the paired product

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

For a fixed integer K≥1 define the partial right-hand upward contribution

U_{n,K}=2Σ_{j=n+1}^{n+K}(b_j−b_n)/[(x_j−x_n)²+(b_j−b_n)²],

and the full reflected upward contribution

V_n=2Σ_{j>n}(b_j−b_n)/[(x_j+x_n)²+(b_j−b_n)²].

**Conclusion.** The product is a nonzero even real entire function with exactly the simple zeros ±w_n, ±conjugate(w_n), finite full-zero reciprocal-square sum, and nonattained height supremum H. For every fixed K,

liminf_{n→∞} U_{n,K}=0,    V_n→0,

and consequently liminf_{n→∞}(U_{n,K}+V_n)=0. In particular no counterexample in this restricted monotone quartet class can keep a fixed positive upward lower bound at every sufficiently large w_n using just a fixed number of successive right-hand zeros and all reflected higher zeros.

## Proof

The product convergence and exact zero identification follow by the elementary logarithmic-tail argument used in Lemma 72: on |z|≤R the sum of |z²/w_n²| and its conjugate counterpart is at most 2R²Σ x_n^{-2}; eventually each term is at most 1/2 and |log(1−u)|≤2|u|. Thus the logarithmic tails converge uniformly on compact disks and exponentiate to nonvanishing analytic tails. The finite factors give exactly the listed zeros. They are distinct because x_n are strictly increasing and x_n,b_n are positive. The limit is even and real, takes value 1 at zero, and its full-zero reciprocal-square sum is at most 4Σ x_n^{-2}. The height assertions follow from b_n increasing strictly to H.

Write d_n=x_{n+1}−x_n>0 and Δ_n=b_{n+1}−b_n>0. Every summand in U_{n,K} has horizontal distance at least d_n and height difference at most b_{n+K}−b_n. Hence

0≤U_{n,K}≤2K(b_{n+K}−b_n)/d_n².                 (1)

Suppose its lower limit were positive (including infinite). There would be c>0 and N such that U_{n,K}≥c for every n≥N. By (1),

Σ_{n≥N} d_n² ≤ (2K/c)Σ_{n≥N}(b_{n+K}−b_n)
≤ (2K²/c)Σ_{r≥N}Δ_r
= (2K²/c)(H−b_N)<∞.                            (2)

The middle bound follows by writing each height window as Σ_{r=n}^{n+K−1}Δ_r: each nonnegative increment occurs at most K times. This argument applies to finite partial sums first and then passes to their increasing limit.

Let D=Σ_{n≥N}d_n². For m>N, Cauchy–Schwarz gives

x_m=x_N+Σ_{n=N}^{m−1}d_n ≤ x_N+sqrt((m−N)D),

so x_m²≤2x_N²+2mD≤Cm with C=2x_N²+2D>0. It follows that Σ_{m>N}x_m^{-2}≥C^{-1}Σ_{m>N}m^{-1}=∞, a contradiction. Since U_{n,K} is nonnegative, its lower limit must be zero.

For the reflected terms, b_j−b_n≤H and x_j+x_n≥x_j imply directly

0≤V_n≤2HΣ_{j>n}x_j^{-2}→0.                     (3)

This also proves absolute convergence of V_n. Adding (3) preserves the zero lower limit, proving the conclusions. ∎

## Qualifications

These conclusions concern finite right-hand windows, not the full upward contribution E_f defined in Lemma 67. For each fixed n the latter converges by the reciprocal-square tail estimate there, but no bound uniform in n on the omitted right-hand tail is proved here. Pointwise convergence of that tail does not justify an interchange with n→∞. Even simultaneous control of increasingly long finite windows would not alone control the infinite remainder.

The monotone quartet hypothesis is an additional restriction. Moreover, these zeros need not all occur as quadratic-penalty maximizers. The lemma neither proves existence of favorable penalties for general products nor rules out an obstruction supported on a sparse subset of indices or on an unbounded number of higher zeros. It isolates why a simple endless chain of uniformly strong immediate-successor interactions cannot satisfy the required reciprocal-square summability. No theta-specific result or RH conclusion follows.

## Verification and formalization obligations

The proof is analytic and requires no computational certificate. Verify the finite-window bound, the at-most-K counting of each height increment, the Cauchy–Schwarz consequence of finite squared increments, and divergence of the harmonic series. Formalization would also require compact logarithmic-tail convergence and the simple zero identification, nonnegative infinite sums, and the reciprocal-square tail limit in (3).
