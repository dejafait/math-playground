# Lemma 145: Mellin contour and pole-scale audit

**Hypotheses.** Let D(s;A) be the entire series in L144, with A>0. Vertical lines are oriented upwards, and A^w uses the real logarithm of A. For the scale comparison use t≥π, τ=t−π/2 and A=(τ/(2π))/sqrt(t/(2π)), as in L144.

**Conclusion.** For every complex s and real c>1−Re(s),

D(s;A)=sqrt(π)/(2πi) ∫_(c) exp(w²/4) A^w ζ(s+w) dw.          (1)

At s=−1+iτ one has the exact decomposition

D(−1+iτ;A)=R(τ,A)+J(τ,A),                                  (2)
R(τ,A)=sqrt(π) A^(2−iτ) exp((2−iτ)²/4),
J(τ,A)=sqrt(π)/(2π) ∫_R exp(−v²/4) A^(iv) ζ(−1+i(τ+v)) dv.

All displayed integrals converge absolutely. Uniformly for A>0 and τ≥0,

|J(τ,A)|≤C(1+τ)^(3/2).                                    (3)

On the specified t scale,

|R(τ,A)|=sqrt(π) A² exp(1−τ²/4)=o(sqrt(t)).                 (4)

Thus the pole term cannot overcome the O(sqrt(t)) additive error in L144. Estimate (3) is only an upper bound, larger than that threshold, and supplies no lower bound for D or J.

**Proof.**

For real y and any real c the Gaussian Fourier identity gives

sqrt(π)/(2π) ∫_R exp((c+iv)²/4−(c+iv)y) dv
 =exp(c²/4−cy) exp(−(y−c/2)²)=exp(−y²).

The Fourier identity itself follows from the Gaussian integral by differentiating its absolutely convergent Fourier integral and integrating by parts: its derivative is −2b times the integral at frequency b, and its value at b=0 is 2sqrt(π). This proves inversion with no contour shift. Apply it to y=log(k/A) and multiply by k^(−s). The absolute sum of the integrals is bounded by a constant times

A^c exp(c²/4) ∫_R exp(−v²/4) dv · Σ_(k≥1) k^(−Re(s)−c),

which is finite. Fubini and the defining zeta series yield (1).

We next justify shifting (1), choosing c=3, to the imaginary axis for fixed τ and A. The only pole in 0<Re(w)<3 is w=2−iτ. Its residue is exp((2−iτ)²/4) A^(2−iτ), because the residue of ζ at 1 is one by L008.

Here is a polynomial strip bound sufficient to discard horizontal edges, without using any zero hypothesis. For Re(z)>0, z≠1, summation by parts first on Re(z)>1 and then analytic continuation give

ζ(z)=z/(z−1)−z ∫_1^∞ {x} x^(−z−1) dx.

The integral is locally uniformly absolutely convergent on Re(z)>0. Indeed its absolute value is at most 1/Re(z). The identity on Re(z)>1 follows from ζ(z)=z∫_1^∞ floor(x)x^(−z−1)dx. Hence for Re(z) in [1/2,2] and |Im(z)|≥1 we have |ζ(z)|≤C(1+|Im(z)|). For Re(z) in [−1,1/2], apply the functional equation and the same bound at 1−z, whose real part belongs to [1/2,2]. The uniform Stirling estimate in the foundations, with Re(1−z) in [1/2,2], and the elementary sine bound give

|ζ(z)|≤C(1+|Im(z)|)^(5/2)

throughout −1≤Re(z)≤2, |Im(z)|≥1. The exponent is deliberately coarse; it suffices here. On a horizontal edge w=u±iT, 0≤u≤3, the Gaussian modulus is exp((u²−T²)/4), A^u is bounded for fixed A, and the zeta factor has polynomial growth in T for fixed τ. Thus both edges vanish as T→∞, taking T>τ+2. The vertical integrals converge absolutely by the same bounds and continuity on their finite portions, since neither line meets the pole. The residue theorem proves (2), including the positive sign of R. This limiting argument is for each τ,A; it does not assert a uniform horizontal-edge estimate while τ varies with T.

For a sharper estimate on the new vertical line, the functional equation at z=−1+iy reads

ζ(−1+iy)=2(2π)^(−2+iy) sin(π(−1+iy)/2) Γ(2−iy) ζ(2−iy).

The absolutely convergent series bounds |ζ(2−iy)|≤ζ(2). Stirling bounds the gamma modulus by C|y|^(3/2)exp(−π|y|/2) for |y|≥1; the sine modulus is at most exp(π|y|/2). Continuity handles |y|≤1. Consequently

|ζ(−1+iy)|≤C(1+|y|)^(3/2).

Since |A^(iv)|=1 and 1+|τ+v|≤(1+τ)(1+|v|), integration against exp(−v²/4) proves (3), with a constant independent of A and τ. Finally A²=τ²/(2πt) is comparable to t as t→∞ and τ is comparable to t; taking the modulus of R proves (4).

In particular (2) gives |D|≥|R|−|J|, but the available bound makes this estimate vacuous at large t. The alternative inequality |D|≥|J|−|R| would need a new lower bound for |J|. Combining with L144 only yields

F(−1,t+3i/2)/(H(t)C(t)B(t))=J(τ,A)+O(sqrt(t)),

because R is smaller than this error. This is an additive identity, not a nonvanishing assertion. ∎

## Qualifications and verification

The zeta pole is not a main term with a proved relatively small remainder here. No estimate of the oscillatory integral from below, no center lower bound, no common heat-interval strip, and no RH conclusion is proved. The size of the upper bound in (3) does not assert that J actually has that size.

Analytic verification consists of Gaussian normalization, the absolute Fubini majorant, the sole crossed pole and its sign, polynomial strip control of horizontal edges, the fixed-parameter contour limit, the uniform bound on the new line, and the comparison with the L144 error. No numerical certificate is needed.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
