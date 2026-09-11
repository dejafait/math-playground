# Lemma 146: functional equation returns the original series

**Hypotheses.** Let J(τ,A) and D be as in L145, with τ>0 and A>0. Put

g(v)=exp(−v²/4)/(2sqrt(π)),
χ(z)=2(2π)^(z−1)sin(πz/2)Γ(1−z),
Q=τ/(2π),
X(τ)=Q^(3/2)exp(iτ(1−log Q)+iπ/4).

For comparison with the center expansion, use t≥π, τ=t−π/2, N=sqrt(t/(2π)), A=Q/N, and C,B,S from L140, L144 and L138. All positive real powers use real logarithms.

**Conclusion.** The exact representation

J(τ,A)=Σ_(n≥1) n^(−2+iτ) ∫_R g(v)χ(−1+i(τ+v))exp(iv log(An))dv                 (1)

has an absolutely summable family of absolutely convergent integrals. Uniformly for A>0 as τ→∞,

J(τ,A)=X(τ) Σ_(n≥1) n^(−2+iτ)exp(−log²(nA/Q))+O(sqrt(τ)).                   (2)

On the specified t scale, X=1/B and the series in (2) is exactly S/C. Consequently

CBJ=S+O(t^(−1)),   CBD=S+O(t^(−1)).                                        (3)

Thus this use of the functional equation and leading Stirling approximation returns the earlier oscillatory series, with an additive error. It supplies no lower bound for the center value.

**Proof.**

The functional equation on z=−1+iy gives

ζ(−1+iy)=χ(−1+iy)Σ_(n≥1)n^(−2+iy).

The series converges absolutely for every real y. The sine bound and complex Stirling formula in the foundations give

|χ(−1+iy)|≤K(1+|y|)^(3/2)                                                   (4)

for all real y: for |y|≥1 the gamma exponential decay cancels the sine exponential growth; continuity handles the compact interval. In particular, the sum of the absolute integrals in (1) is at most

Kζ(2)∫_R g(v)(1+|τ+v|)^(3/2)dv<∞.

Since A^(iv) and n^(iv) have modulus one, this bound is independent of A. Fubini applied to the integral defining J in L145 proves (1).

We record the phase as well as the modulus of the Stirling approximation. For positive y→∞,

Γ(2−iy)=sqrt(2π)y^(3/2)exp(−πy/2)
         ·exp(i(−y log y+y−3π/4))(1+O(1/y)),
sin(π(−1+iy)/2)=−cosh(πy/2)=−½exp(πy/2)(1+O(exp(−πy))).

The gamma identity follows directly from logarithmic complex Stirling with the principal logarithm in the right half-plane. In particular Log(2−iy)=log y−iπ/2+2i/y+O(y^(−2)); its constant real contribution cancels the −2 in the Stirling exponent. Combining these formulas with 2(2π)^(−2+iy) gives

χ(−1+iy)=(y/(2π))^(3/2)
          ·exp(i[y(1−log(y/(2π)))+π/4])(1+O(1/y)).                         (5)

The minus sign from the sine is included in the phase π/4.

Let h=τ^(1/4). For |v|≤h and sufficiently large τ, Taylor expansion of the explicit phase p(y)=y(1−log(y/(2π))) gives

p(τ+v)−p(τ)=−v log Q+O(v²/τ),

because p'(τ)=−log Q and p''(y)=−1/y. The amplitude ratio is 1+O(|v|/τ). The remainder in (5) is uniformly O(1/τ) on this interval. Since v²/τ tends uniformly to zero there, exponentiation yields

χ(−1+i(τ+v))=X(τ)exp(−iv log Q)(1+O((1+v²)/τ)).                            (6)

This uses Taylor expansion of the explicit leading expression, not differentiation of an unspecified Stirling remainder.

Replacing χ by the leading expression in (6) in the sum of local integrals costs at most

(K|X|/τ)ζ(2)∫_R g(v)(1+v²)dv=O(sqrt(τ)).                                  (7)

For the omitted tails, (4) and 1+|τ+v|≤(1+τ)(1+|v|) bound the absolute original tail by

Kζ(2)(1+τ)^(3/2)∫_(|v|>h) g(v)(1+|v|)^(3/2)dv.

This is O(τ^(3/2)exp(−c sqrt(τ))) for some c>0, hence o(sqrt(τ)). For example, absorb the polynomial into exp(v²/8) and bound the remaining Gaussian tail by a constant times exp(−h²/16). The replacement tail has the same bound without the polynomial, since its phase has modulus one. All estimates are uniform in A and n after summing n^(−2). We may therefore replace and extend the local integrals to R with the total error (7).

Gaussian Fourier integration now gives

∫_R g(v)exp(iv log(An/Q))dv=exp(−log²(An/Q)).

The resulting series is absolutely convergent, bounded in absolute mass by ζ(2). This proves (2) without any conditionally convergent interchange.

On A=Q/N, expansion of the square in the definition of S in L138 gives

S=exp(π²/16+iπ log(N)/2)
  ·Σ_(n≥1)n^(−2+i(t−π/2))exp(−log²(n/N))
 =C Σ_(n≥1)n^(−2+iτ)exp(−log²(nA/Q)).

From the explicit B in L144, Q^(−1)sqrt(2π/τ)=Q^(−3/2), and its phase is the negative of the phase in X. Hence BX=1 exactly. Since |C|=exp(π²/16) and |B|=Q^(−3/2), multiplication of (2) by CB gives the first identity in (3). L145 gives D=J+R with |R|=sqrt(π)A²exp(1−τ²/4). On this scale |CBR| is exponentially small, proving the second identity.

L144 already gives the stronger comparison S=CBD+O(t^(−3/2)). Thus (3) is a coarser return to the same series, rather than a new cancellation estimate. Positive Gaussian weights do not remove its phases n^(iτ). Neither (1) nor the upper error bounds imply a lower bound for its modulus. ∎

## Qualifications and verification

No assertion is made that sharper analysis of (1) is impossible. The conclusion concerns this justified leading approximation. The center lower bound, a common heat-interval strip, and RH remain unproved.

Analytic verification checks the absolute Fubini majorant, gamma and sine phase signs, uniform local expansion, both Gaussian tails, Fourier normalization, exact equality BX=1, and the scaled error. No numerical certificate is needed. Formalization would require these explicit identities, Stirling remainder bounds, Taylor estimates, and dominated interchanges. No lower bound is an input.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
