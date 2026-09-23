# Lemma 136: undeformed logarithmic Jensen ratio

**Hypotheses.** Let F be the theta heat deformation of L058. Set H=1/2, r=1+sqrt(17)/2, t=x+1/2 and c_x=t+3i/2 for real x. Write

M(x)=max_{|z−c_x|≤2r}|F(0,z)|.

**Conclusion.** There are constants C≥1 and B>0, independent of x, such that

M(x)/|F(0,c_x)|≤C(2+|x|)^(r+1),

0≤log(M(x)/|F(0,c_x)|)≤B log(2+|x|).

Consequently the full zero count of F(0,·) in Re z∈[x,x+1), including multiplicities, is at most (B/log 2)log(2+|x|). This establishes L135's ratio condition for the singleton parameter set λ=0. It asserts no estimate uniform on a nontrivial heat-parameter interval and no RH conclusion.

**Proof.**

By L058 and L018, F(0,z)=Ξ(z)=ξ(1/2+iz), and all its zeros lie in |Im z|<1/2. The centers are therefore nonzero. Reflection gives

F(0,t+3i/2)=ξ(−1+it)=ξ(2−it).

By L001, |ζ(2−it)|≥1/ζ(2), while its defining absolutely convergent series gives |ζ(2−it)|≤ζ(2). Apply the completion formula in L018 and the vertical-strip Stirling bounds stated in foundations/notation-and-inputs.md. For |t|≥1, positive constants a,A give

a |t|^(5/2)e^(−π|t|/4) ≤ |F(0,c_x)| ≤ A |t|^(5/2)e^(−π|t|/4).       (1)

Here the polynomial prefactor |s(s−1)| contributes power 2 and Γ(s/2), at Re s=2, contributes power 1/2. Factors π^(−Re s/2)/2 are fixed. A compact range, if needed to extend the asymptotic inequalities down to |t|=1, is covered by nonvanishing and continuity.

We next supply a deliberately coarse polynomial bound for ζ, sufficient for the disk numerator. For Re s>1, absolute summation of n^(−s)=s∫_n^∞u^(−s−1)du gives

ζ(s)=s∫_1^∞floor(u)u^(−s−1)du
     =s/(s−1)−s∫_1^∞{u}u^(−s−1)du.                         (2)

The last integral is holomorphic on Re s>0: on compact subsets its integrand and every derivative are dominated by constants times u^(−1−ε)(1+log u)^k. Meromorphic continuation and the identity theorem extend (2) to that half-plane away from 1. For 1/2≤σ≤S and |v|≥1 this yields

|ζ(σ+iv)|≤|s|/|s−1|+|s|/σ≤C_S(1+|v|).                    (3)

Thus no unproved bound inside the critical strip is used.

For z=u+iy in the radius-2r disk, |u−t|≤2r and |y|≤3/2+2r. Replace s=1/2+iz by 1−s whenever Re s<1/2; reflection preserves ξ. The resulting argument w=σ+iv satisfies

1/2≤σ=1/2+|y|≤S:=2+2r,   |v|=|u|.

Take |t|≥4r+4. Then |v|≥1, |v| is between |t|/2 and 3|t|/2, and ||v|−|t||≤2r. Uniform Stirling, (3), and the completion formula give

|ξ(w)|≤C_S |v|^(σ/2+5/2)e^(−π|v|/4)
       ≤C' |t|^(S/2+5/2)e^(−π|t|/4).

The first exponent is the sum 2+(σ/2−1/2)+1. The second inequality uses the bounded difference of |v| and |t| for the exponential and compactness of the range of polynomial exponents. All constants are uniform on the entire translated disk, so its maximum obeys the same bound. Dividing by (1) leaves exponent S/2=r+1.

For |t|≤4r+4, all disks belong to one compact set. Their maxima are bounded by continuity, and the nonzero center values have a positive minimum. Increasing C therefore proves the first conclusion for all x, using comparability of 2+|t| and 2+|x|. Since the disk contains its center the logarithm is nonnegative; absorb log C into B log(2+|x|). L135 applies with L=0 and H=1/2, giving the full local count. ∎

## Limits of the heat extension

The identity with a gamma factor times ζ, the reciprocal-series lower bound on Re s=2, and the cancellation of their exponential decay are established here only for λ=0. Reflection in z persists for real heat slices, but supplies no such factorization or reciprocal series for λ≠0. Joint continuity from L058 controls bounded x windows and does not make these estimates uniform as |x| tends to infinity. A common zero strip for a heat interval is also not proved here.

In fact (1) proves that L135's stronger lower bound using its constant U fails at λ=0 for every fixed finite exponent: |F(0,c_x)|(2+|x|)^b tends to zero for every real b. This does not contradict the relative ratio just proved; both numerator and denominator decay exponentially. It rules out that stronger shortcut even for the undeformed function.

## Verification

Analytic verification checks the center reflection, full classical strip localization, absolute summation and holomorphic continuation in (2), uniformity in σ of Stirling, the disk shifts, all polynomial exponents, and the compact-center minimum. No numerical experiment or computational certificate is required.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
