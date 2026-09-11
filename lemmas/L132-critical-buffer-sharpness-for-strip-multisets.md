# Lemma 132: critical buffer sharpness for strip multisets

**Hypotheses.** Fix c>0. Counting functions below count full multisets, with multiplicities, in the disk |z|≤t.

**Conclusion.** There exists a single locally finite multiset Z invariant under conjugation and negation, contained in |Im z|≤1, with no real or imaginary-axis points, such that

N(t)=O(t log t),    Σ_{ρ∈Z}|ρ|^(-2)<∞.

There are simple points w_n=A_n+i/2 in Z, with A_n→∞, for which, on setting d_n=c sqrt(A_n log A_n) and R_n=A_n+d_n,

E_n=2Σ_{ρ∈Z, |Re ρ|>R_n, Im ρ>1/2}
          (Im ρ−1/2)/|w_n−ρ|² → 1/(4c²)>0.

Thus a fixed positive multiple of the critical buffer cannot guarantee vanishing exterior upward interaction in this class. The multiset may depend on c, but it is fixed throughout the limit n→∞.

## Proof

Put A_n=4^n, d_n=c sqrt(A_n log A_n), u_n=A_n+2d_n, and M_n=floor(A_n log A_n). Start at an integer n₀ sufficiently large that 2d_n<A_n/2 for every n≥n₀; this is possible since log A_n/A_n→0. At each of the four points ±u_n±i put multiplicity M_n. At each of ±A_n±i/2 put multiplicity one. Let Z consist of precisely these points for n≥n₀.

The construction gives the stated symmetries and strip bound. Its positive real coordinates lie in [A_n,3A_n/2), so the intervals for different n are disjoint. All target points are simple, there are no points on either axis, and every compact set contains finitely many points counting multiplicity.

If a point from level n has modulus at most t, then A_n≤t. Consequently

N(t)≤4Σ_{n≥n₀, 4^n≤t}(M_n+1)=O(t log t).

For completeness, if k=floor(log t/log 4), then Σ_{n≤k}n4^n≤kΣ_{n≤k}4^n≤(4/3)k4^k, which gives this estimate for large t. Also every point of level n has modulus at least A_n, whence

Σ_{ρ∈Z}|ρ|^(-2)≤4Σ_{n≥n₀}(M_n+1)/A_n²
                  ≤4Σ_{n≥n₀}(n log 4/4^n+16^(-n))<∞.

Only cluster points with height 1 contribute to E_n; targets have height 1/2 and all negative-height points are excluded. Each contributing numerator is 2(1−1/2)=1. All levels j<n lie inside the window, since u_j<3A_j/2≤3A_n/8<R_n. Both cluster points at level n lie outside it, because u_n=A_n+2d_n>R_n. Every level j>n also lies outside it: A_j≥4A_n and R_n<5A_n/4. Therefore

E_n = M_n/[4d_n²+1/4]
      + M_n/[(u_n+A_n)²+1/4]
      + Σ_{j>n} M_j{1/[(u_j−A_n)²+1/4]
                      +1/[(u_j+A_n)²+1/4]}.

This equality involves nonnegative terms. The following estimates also prove finiteness, so no conditional summation is involved. The first term tends to 1/(4c²), since M_n/(A_n log A_n)→1. The second is at most M_n/(4A_n²)=O(log A_n/A_n). For j>n, u_j−A_n≥3A_j/4 and u_j+A_n≥A_j. Thus the last sum is at most

(16/9+1)Σ_{j>n} M_j/A_j²
 ≤(25/9) log 4 Σ_{j>n}j/4^j = O(n/4^n)→0.

The last estimate follows directly by writing j=n+k and summing the convergent geometric series Σ4^(-k) and Σk4^(-k). This proves the exact limit. ∎

## Qualifications and verification

This establishes critical-scale failure for actual positive exterior sums in the abstract multiset class, strengthening the scope comparison with the majorant in L131. It does not assert that such a multiset is a theta heat slice. Large multiplicities are allowed by the question's multiset hypothesis. The target zero is not a highest zero in the larger window: earlier clusters have height 1. No bounded-domain maximum principle is contradicted, and the signed exterior interaction, which includes downward contributions, is not asserted positive. No necessity theorem for theta zeros, strip theorem, or RH conclusion follows.

The proof is elementary and uses no earlier mathematical lemma. Verification checked full multiplicities, the disk counting convention, the strict exterior cutoff, target simplicity, convergence, and the exact limit by explicit geometric bounds. No numerical verification is needed. Formalization would require this locally finite multiset construction, the geometric summation bounds, and the displayed positive-series limit.
