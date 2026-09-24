# Lemma 253: second associated spectrum and a signed theta remainder

**Hypotheses.** Let k be real, continuous, even, and satisfy |k(u)|≤C_B exp(−B|u|) for every B>0. Set F(x)=∫_R k(u)e^(ixu)du, g(u)=u k(u), h(u)=u²k(u), and C_f(v)=∫_R f(w+v)f(w)dw. Define

A₂(t)=∫_R s⁴k(s+t)k(s−t)ds,
R(t)=2t²C_g(2t)+t⁴C_k(2t).

For the sign conclusion take the actual theta kernel k(u)=K(|u|) of L019.

**Conclusion.** With hats denoting ∫ f(t)e^(iξt)dt,

A₂(t)=C_h(2t)+R(t),
Â₂(2x)=[F F⁗−4F′F‴+3F″²]/16,
R̂(2x)=−(F′²)″/4+(F²)⁗/32.

For actual theta, F=2Ξ and Â₂(2x)=3D₂(Ξ;x), where D₂(J;x)=J″²/4−J′J‴/3+JJ⁗/12. The remainder R̂ has both positive and negative real values. Thus the modular identity does not give a nonnegative spectrum for this particular non-autocorrelation remainder. No negative value of the total Â₂ is asserted.

**Proof.** All polynomially weighted double integrals below converge absolutely by the exponential bounds. Under u=s+t, v=s−t, the Jacobian is 1/2 and s⁴=(u+v)⁴/16. Fubini and differentiation under the integral give

Â₂(2x)=(1/32)∫∫(u+v)⁴k(u)k(v)e^(ix(u−v))du dv
          =(2FF⁗−8F′F‴+6F″²)/32.

Evenness makes all displayed derivatives real. Alternatively, expand s⁴=((s+t)(s−t)+t²)² to obtain A₂=C_h(2t)+2t²C_g(2t)+t⁴C_k(2t). The autocorrelation spectra at frequency 2x are respectively F″²/2, F′²/2, and F²/2. Multiplication by t² corresponds to −(1/4)d²/dx² and multiplication by t⁴ to (1/16)d⁴/dx⁴. This gives the asserted R̂ and checks the coefficients independently. L019–L020 identify F=2Ξ for theta and justify the entire differentiation used here.

We now prove the sign obstruction for actual theta without any numerical Fourier evaluation. The exponential bounds imply that C_k, C_g, C_h and their polynomially weighted versions are continuous, bounded and integrable. For example, for any B, absorbing polynomial weights into the decay gives an integrable bound by a constant times exp(−B(|w+2t|+|w|)); its integral is at most a constant times (1+|t|)exp(−2B|t|). The same argument supplies dominated convergence for continuity. Thus R is continuous, bounded, integrable and even; R(0)=0.

At zero frequency the formula above gives

R̂(0)=[F(0)F⁗(0)−5F″(0)²]/16,

whose sign is not needed. Instead C_g(0)=∫u²k(u)²du>0 by strict positivity of theta in L019. Continuity therefore gives C_g(2t)>0 for sufficiently small |t|. Since C_k(2t)>0 for every t, R(t)>0 for every sufficiently small nonzero t. In particular R is not identically zero.

Suppose R̂ were nonnegative everywhere. For ε>0, the elementary Gaussian integral and Fubini give

∫_R R̂(ξ)e^(−εξ²)dξ
 =√(π/ε)∫_R R(t)e^(−t²/(4ε))dt → 2πR(0)=0

as ε decreases to zero. The limit follows by the Gaussian approximate identity, using boundedness and continuity at zero. Since the left integrands would be nonnegative and increase as ε decreases, monotone convergence forces R̂≡0 (R̂ is continuous). The same calculation centered at any a, with the factor e^(−iaξ), would then give 2πR(a)=0, a contradiction. Applying the identical argument to −R rules out R̂≤0 everywhere. Therefore R̂ takes both signs. This proof does not assume integrability of R̂ or invoke an unqualified Fourier inversion.

For completeness the positive-definiteness implication proved by the interval-density argument in L233 applies to the continuous integrable A₂ as well: positive definiteness requires Â₂≥0. The required actual-theta second-level threshold is therefore D₂(Ξ;x)≥0 for every real x. The signed remainder neither proves nor disproves that threshold: the nonnegative autocorrelation contribution F″²/2 may compensate it. ∎

The comparison required for this decomposition is R̂(2x)≥−F″(x)²/2 at every real x, not R̂≥0. No such global quantitative comparison is obtained. Even establishing it would leave higher levels and the main all-degree mixed-positivity gap unresolved.

**Mathlib.** Not checked for the full statement or supporting Fourier, Gaussian approximate-identity, autocorrelation, and differentiation results. No matching theorem is claimed. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
