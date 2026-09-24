# Lemma 259: an explicit theta circle bound for Laguerre detection

**Hypotheses.** Let Ξ be the completion in L018. Suppose Ξ(a+ib)=0 with a,b real, b≠0, and Ξ(a)≠0. Define D_n as the coefficients of Ξ(a+iy)Ξ(a−iy). For R>|b| put

U(R)=∫_0^∞ K(u)cosh(Ru)du=Ξ(iR)>0,
q=b²/R²,
N_R=ceil(log(U(R)²/[|Ξ(a)|²(1−q)])/log(1/q)).

**Conclusion.** There is an integer 1≤n≤N_R such that

D_n(Ξ;a)b^(2n)≤−|Ξ(a)|²(1−q)/N_R<0.

In particular the unconditional strip localization permits R=1, giving the explicit constant

C=U(1)=(3/8)π^(−3/4)Γ(3/4)ζ(3/2)

and the index

N_1=ceil(log(C²/[|Ξ(a)|²(1−b²)])/log(1/b²)).

The circle majorant C² is independent of a. The index still depends on the central value |Ξ(a)|; no height-only bound or exterior positivity is asserted.

**Proof.** L019 and L020 give positivity of K, convergence against every exponential, and the entire cosine representation. For real x,v and u≥0,

|cos((x+iv)u)|²=cos²(xu)+sinh²(vu)≤cosh²(vu).

Thus, for |Im z|≤R,

|Ξ(z)|≤∫_0^∞ K(u)|cos(zu)|du≤U(R).

Every integral is absolutely convergent by L019; the identity U(R)=Ξ(iR) follows directly from L020. Positivity of K makes U(R)>0. If y is complex and |y|=R, both a+iy and a−iy have imaginary part of magnitude |Re y|≤R. Consequently

|Ξ(a+iy)Ξ(a−iy)|≤U(R)².

Apply L258 with m=0, c=|Ξ(a)|², and M=U(R)². Its hypotheses of entirety and reality follow from L018, and its conclusion gives the asserted index and negative margin. In particular N_R≥1. Notice that the bound is on a complex y-circle, not merely on real y.

L018 places every zero of Ξ in |Im z|<1/2, so R=1 is valid. Reflection gives Ξ(i)=ξ(−1/2)=ξ(3/2). Substitution into the completed-zeta formula in L018 yields the displayed C. Γ(3/4) has its convergent positive Euler integral and ζ(3/2) its absolutely convergent positive Dirichlet series, so C is a finite explicit positive constant without any zero assumption. Substitution of R=1 gives N_1. ∎

For a fixed nonzero b, the formula for N_1 diverges as |Ξ(a)| tends to zero. The theta majorization gives an upper bound on |Ξ(a)|, whereas an upper bound on N_1 requires a positive lower bound on that value. Neither positivity of K nor taking absolute values provides one: the real cosine integral is oscillatory. The recorded compact zero-free rectangle does not address possible centers |a|>4. Even a stronger decay upper bound such as L239 cannot be reversed into the needed lower bound. This observation does not assert that values at hypothetical nonreal-zero centers actually approach zero.

The precise sufficient sign target is D_n(Ξ;a)≥0 for every 1≤n≤N_1 at each such center with Ξ(a)≠0. The known compact all-level signs do not reach these centers. If Ξ(a)=0, this formula is inapplicable: L258 instead uses the first nonzero derivative after deflation, whose lower bound is also not supplied here. Thus this explicit specialization completes the circle-estimate task but supplies neither the missing sign proof nor control of small central values.

**Mathlib.** Not checked for the full statement or supporting complex-cosine inequality, integral majorization, Gamma formula, and Cauchy estimate. No matching or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
