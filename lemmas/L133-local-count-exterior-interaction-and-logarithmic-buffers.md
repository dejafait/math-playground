# Lemma 133: local-count exterior interaction and logarithmic buffers

**Hypotheses.** Let Z be a locally finite multiset in |Im z|≤H, with H>0, counting full multiplicities. Suppose a constant C>0 satisfies

#{ρ∈Z: Re ρ∈[x,x+1)} ≤ C log(2+|x|)                 (1)

for every real x. For A≥2 and d≥1 put R=A+d and

W(A,d)=(8C/d)[log(3+A+2d)+log 2].

**Conclusion.** For every w=a+ib with |a|≤A and 0<b≤H,

Σ_{|Re ρ|>R}|w−ρ|^(-2) ≤ W(A,d),                  (2)

E_R(w):=2Σ_{|Re ρ|>R, Im ρ>b}(Im ρ−b)/|w−ρ|²
 ≤ 2(H−b)W(A,d),                                   (3)

Σ_{|Re ρ|>R}|Im(2/(w−ρ))| ≤ 4H W(A,d).             (4)

All sums converge absolutely. For arbitrary functions d(A)≥1,

W(A,d(A))→0 ⇔ d(A)/log A→∞.                        (5)

Thus buffers log A times any positive diverging factor suffice for vanishing exterior interaction. For example, d=log A log log A is sufficient and o(A) for large A. Equivalence (5) concerns the displayed majorant, not necessity for an actual multiset. The conclusions are uniform over any family with the same C and H.

If Z is the zero multiset of a real theta heat slice as in L129, w is a zero of multiplicity m, and no zero in |Re z|≤R has height greater than b, its local forward cluster height rate obeys

c(w)≤−m/b−mb/(a²+b²)+2(H−b)W(A,d).                 (6)

## Proof

Write u=Re ρ. Every exterior zero satisfies |u−a|>d. For each k≥0 set t=2^k d. Cover the positive interval [a+t,a+2t) and the negative interval [a−2t,a−t) each by ceil(t) consecutive half-open unit intervals, starting at its left endpoint. These covers include every point of the original intervals, including their left endpoints. The two sequences of original intervals cover all u with |u−a|>d; their choices of boundary convention cause no omission. On each original interval |u−a|≥t.

Every unit interval used has starting point x with |x|≤A+2t+1. By (1) the total count in the two original intervals is at most

2 ceil(t) C log(3+A+2t) ≤ 4Ct log(3+A+2t),

where t≥1. Covers may extend past the original endpoints; counting additional points only increases this bound. Since |w−ρ|²≥(u−a)², summing these nonnegative estimates gives

Σ_{|u|>R}|w−ρ|^(-2)
 ≤ (4C/d) Σ_{k≥0} 2^(−k) log(3+A+2^(k+1)d).

The inequality 3+A+2^(k+1)d≤2^k(3+A+2d) yields

log(3+A+2^(k+1)d)≤log(3+A+2d)+k log 2.

Both Σ 2^(−k) and Σ k 2^(−k) equal 2, so (2) follows, with finite right side. Upward numerators are at most 2(H−b), and absolute imaginary numerators at most 4H. This proves (3), (4), and convergence without any interchange of signed sums.

For (5), W≥8C log A/d, so vanishing implies log A/d→0. Conversely suppose log A/d→0. Where d≤A, use 3+A+2d≤5A for A≥2, giving W≤8C[log(5A)+log 2]/d→0. Where d>A, use 3+A+2d≤5d, giving W≤8C[log(5d)+log 2]/d→0 because d>A→∞. These bounds cover even oscillatory buffer functions. The stated example follows from elementary logarithmic limits. The constants depend only on C and H, proving family uniformity.

For (6), use the quartet extraction and absolutely convergent imaginary-sum argument of L129. They give c(w)≤−m/b−mb/(a²+b²)+E_R(w) under exactly the stated window-maximum hypothesis. Substituting (3) proves the claim, including the multiple-zero interpretation supplied there. ∎

## Qualifications and verification

The local count (1) is an extra hypothesis. No proof here establishes it for theta heat slices, individually or uniformly in time. A common strip bound is likewise still assumed. Unlike the global-count estimate of L131 (a comparison only), this estimate uses the count near the observation point before summing distant shells. No symmetry is required for (2)–(5).

This result neither proves optimality of the logarithmic buffer for actual interactions nor controls the annulus A<|Re ρ|≤A+d. It does not ensure inner attainment of a larger-window height maximum or a uniform time remainder. The overall argument and RH gap remain unchanged.

Verification is analytic: half-open covers, endpoint inclusion, full multiplicities, the two geometric-series constants, nonnegative summation, and the two-case buffer limit were checked. No numerical certificate is needed. Formalization would require the shell-cover counting inequality, summability of the geometric majorant, the arbitrary-function limit equivalence, and substitution into the conditional local height rate.
