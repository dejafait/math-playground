# Lemma 266: an off-center anchor removes central-value normalization

**Hypotheses.** Let F be a nonzero entire function real on the real axis, let a be real, and write

H(y)=F(a+iy)F(a−iy)=Σ_(n≥0) d_n y^(2n).

Suppose F(a+ib)=0 with 0<b<s<R. Suppose H(s)≥A>0 and |H(y)|≤M on the complex circle |y|=R. Put

p=s²/R², q=b²/R²,
K=ceil(log(2M/[A(1−p)])/log(1/p)).

**Conclusion.** K≥1 and d_n<0 for some 1≤n≤K, regardless of whether F(a)=0 and of its multiplicity there. For actual theta, one may choose s=3/2 and R=3, and set

M=Ξ(3i)²,
A(a)=((a²+4)(a²+1)/(4π² ζ(2)²)) |Γ(1−ia/2)|²>0,
K(a)=ceil(log(8M/[3A(a)])/log 4).

Every hypothetical nonreal zero a+ib of Ξ then forces a negative D_n(Ξ;a) with 1≤n≤K(a). This cutoff depends on the height a, not on the central value, a central derivative, or b. It is not a proof of any of the required signs.

**Proof.** H is even entire with real Taylor coefficients, and d_0=F(a)²≥0. Cauchy's coefficient estimate gives |d_n|≤M/R^(2n). The maximum modulus principle gives M≥H(s)≥A. Thus the logarithm defining K is positive and K≥1. The definition also gives

p^K≤A(1−p)/(2M).

For each real t with 0≤t<R, absolute convergence and the geometric series bound the tail after K by M(t/R)^(2K+2)/(1−t²/R²). In particular the finite sum S_s=Σ_(n=0)^K d_n s^(2n) satisfies

S_s≥A−Mp^(K+1)/(1−p)≥A(1−p/2)≥A/2.

Suppose all d_n for 0≤n≤K are nonnegative. Since 0<b/s<1, termwise comparison of this finite sum yields

S_b=Σ_(n=0)^K d_n b^(2n)≥(b/s)^(2K) S_s≥(b/s)^(2K) A/2.

Compare the absolute tail at b with the last positive bound. Their ratio is at most

[2M/A] p^K q/(1−q) ≤ (1−p)q/(1−q) < p < 1,

where q<p implies q/(1−q)<p/(1−p). Hence H(b)>0, contradicting H(b)=0. A negative coefficient occurs among 0,…,K, and d_0≥0 excludes index zero. No division by F(a) and no real-center deflation has been used.

For theta, L018 supplies reality, entirety, symmetry, and |Im rho|<1/2 for every zero. Conjugation permits b>0. The circle estimate proved in L259, independently of its nonzero-center hypothesis for the witness formula, gives M=Ξ(3i)² from the positive theta representation. At the real anchor y=3/2, reality gives

H(3/2)=|Ξ(a+3i/2)|²=|ξ(2−ia)|².

Indeed Ξ(z)=ξ(1/2+iz), and the functional equation sends −1+ia to 2−ia. Write w=2−ia. The completed-zeta identity is

ξ(w)=(w(w−1)/2) π^(−w/2) Γ(w/2) ζ(w).

L001 gives 1/ζ(w)=Σ μ(n)n^(−w), whose absolute value is at most ζ(2); hence |ζ(w)|≥1/ζ(2). Taking squared moduli proves H(3/2)≥A(a). The Gamma factor is finite and nonzero on Re(w/2)=1 by the standard input recorded in foundations, so A(a)>0 for every real a. Substituting p=1/4 gives K(a). All reciprocal-series use stays in Re w=2; there is no continuation of a positivity assertion into the critical strip. ∎

This is a genuine replacement of L259's central denominator: it gives a finite height-only cutoff even at real zeros and for arbitrarily small nonzero b. It does not contradict finite-level masking examples, whose growth-to-anchor ratios are not bounded by these actual-theta constants. For exclusion of a hypothetical zero at a, the sufficient target is now D_n(Ξ;a)≥0 for every 1≤n≤K(a). The established all-level signs on |a|≤7/2 still leave possible exterior centers uncovered. No statement here proves the required exterior signs or the all-degree mixed positivity.

**Mathlib.** Full statement and supporting Cauchy/tail comparison: not checked. L001 records the supporting reciprocal identity `ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius` and summability theorem `ArithmeticFunction.LSeriesSummable_moebius_iff`, with direct references:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff

These are supporting results, not a match for the full witness bound; their sources were not rechecked in this step. Gamma nonvanishing coverage was not checked.
