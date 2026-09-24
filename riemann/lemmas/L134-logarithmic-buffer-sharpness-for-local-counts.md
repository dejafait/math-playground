# Lemma 134: logarithmic-buffer sharpness for local counts

**Hypotheses.** Fix c>0. All counts and sums below include full multiplicities; log denotes the natural logarithm.

**Conclusion.** There is a single locally finite multiset Z, invariant under conjugation and negation and contained in |Im z|≤1, with no points on either axis, such that for every real x,

#{ρ∈Z: Re ρ∈[x,x+1)} ≤ 4 log(2+|x|).

Moreover N(t):=#{ρ∈Z: |ρ|≤t}=O(t log t) and Σ_{ρ∈Z}|ρ|^(-2)<∞. There are simple points w_n=A_n+i/2 in Z, with A_n=4^n→∞, for which d_n=c log A_n and R_n=A_n+d_n satisfy

E_n:=2Σ_{ρ∈Z, |Re ρ|>R_n, Im ρ>1/2}
           (Im ρ−1/2)/|w_n−ρ|² → 1/(6c)>0.

Thus a fixed multiple of log A does not guarantee vanishing exterior upward interaction even under this logarithmic local count. Z may depend on c but is fixed throughout the limit.

**Proof.**

Put K_n=floor(d_n), M_n=floor(log A_n), and u_{n,k}=A_n+2d_n+k for 0≤k<K_n. Choose n₀ so large that, for all n≥n₀, A_n≥4, d_n≥2, and 3d_n<A_n/2. At each of the four points ±u_{n,k}±i put multiplicity M_n. At each of ±A_n±i/2 put multiplicity one. These are precisely the points of Z.

All positive real coordinates at level n lie in [A_n,3A_n/2). Successive cluster coordinates at one level are separated by exactly 1. The target coordinate and first cluster coordinate are separated by 2d_n≥4. Coordinates at distinct positive levels are separated by more than 1, since A_{n+1}=4A_n; the same holds on the negative side. The gap across zero is at least 2A_{n₀}. Therefore any two distinct real coordinates of Z are at distance at least 1. A half-open unit interval contains at most one of them, including when their distance is exactly 1.

If [x,x+1) contains a coordinate v at level n, then |x|> |v|−1≥A_n−1 by the triangle inequality and |v−x|<1. Hence log(2+|x|)>log A_n. At a cluster coordinate the full count is 2M_n≤2 log A_n; at a target coordinate it is 2≤2 log A_n. Both imply the asserted bound with constant 4. An empty interval satisfies it trivially. In particular the constant does not depend on c, although n₀ does.

The symmetries, absence of axis points, and simplicity of targets follow from the separated coordinates. Each level contains 4(K_n M_n+1) points counting multiplicities, which is O_c(n²). All its points have modulus at least A_n. This proves local finiteness and

Σ_{ρ∈Z}|ρ|^(-2) ≤4Σ_{n≥n₀}(K_n M_n+1)/16^n<∞.

For t large, only n≤floor(log t/log 4) contribute to N(t). Thus N(t)=O_c((log t)³), which in particular is O_c(t log t).

Only cluster points at height 1 enter E_n, each with numerator 2(1−1/2)=1. For j<n their absolute real coordinates are less than 3A_j/2≤3A_n/8<R_n. At level n both signs of u_{n,k} are strictly exterior since u_{n,k}≥A_n+2d_n>R_n. For j>n they are also exterior since A_j≥4A_n while R_n<7A_n/6. Consequently the nonnegative sum is exactly

E_n=P_n+Q_n+T_n,

P_n=M_n Σ_{k=0}^{K_n−1}[(2d_n+k)²+1/4]^(-1),

Q_n=M_n Σ_{k=0}^{K_n−1}[(2A_n+2d_n+k)²+1/4]^(-1),

T_n=Σ_{j>n} M_j Σ_{k=0}^{K_j−1}
       {[(u_{j,k}−A_n)²+1/4]^(-1)
        +[(u_{j,k}+A_n)²+1/4]^(-1)}.

We have Q_n≤K_n M_n/(4A_n²)=O_c(n²/16^n). For j>n, u_{j,k}−A_n≥3A_j/4 and u_{j,k}+A_n≥A_j, so

T_n≤(25/9)Σ_{j>n} K_j M_j/A_j²
    =O_c(Σ_{j>n}j²/16^j)=O_c(n²/16^n)→0.

The last bound follows by putting j=n+ℓ and using (n+ℓ)²≤n²(1+ℓ)² for n≥1 and convergence of Σ_{ℓ≥1}(1+ℓ)²16^(−ℓ). These estimates prove finiteness as well as convergence of the remainders.

Finally, write d=d_n. Then

P_n=(M_n/d_n) [(1/d)Σ_{k=0}^{floor(d)−1}
                   ((2+k/d)²+1/(4d²))^(-1)].

The functions ((2+t)²+1/(4d²))^(-1) converge uniformly on [0,1] to (2+t)^(-2): their difference in absolute value is at most 1/(64d²). The bracket is a left Riemann sum with mesh 1/d over [0,floor(d)/d]; its omitted final interval has length less than 1/d and bounded integrand. It therefore tends to

∫₀¹(2+t)^(-2)dt=1/2−1/3=1/6.

Since M_n/d_n→1/c, P_n→1/(6c). Together with the two remainder bounds this proves the claim. ∎

## Qualifications and verification

This elementary construction has no earlier lemma as a mathematical input. L133 is a comparison: its sufficient superlogarithmic buffer cannot be replaced by c log A for all multisets satisfying its hypotheses. No necessity assertion for each individual multiset follows. No realization as zeros of a theta heat slice is established, and no statement about signed net interaction or a highest point in the larger window is made. Earlier clusters have greater height than the target. The RH gap is unchanged.

Analytic verification checked arbitrary half-open unit intervals, both signs of real coordinates, full multiplicities, strict cutoffs, target simplicity, reciprocal-square summability, and the exact Riemann-sum normalization with geometric remainder bounds. No numerical certificate is required.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
