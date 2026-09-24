# Lemma 233: the signed Fourier term in the first associated kernel

**Hypotheses.** Let k be a real, continuous, even function on R such that for every B>0 there is C_B with |k(u)|≤C_B exp(−B|u|). Use the convention

F(x)=∫_R k(u)e^(ixu)du,
A(t)=∫_R s²k(s+t)k(s−t)ds,
C_f(h)=∫_R f(v+h)f(v)dv,
g(u)=u k(u).

**Conclusion.** For every real x,

A(t)=C_g(2t)+t²C_k(2t),
Â(2x)=[F'(x)²−F(x)F''(x)]/4.

The first summand has Fourier transform F'(x)²/2 at frequency 2x, whereas the second has transform −(F(x)²)''/8. Thus the positive pointwise weight t² does not preserve the nonnegative autocorrelation spectrum.

For the actual theta kernel k(u)=K(|u|), L019–L020 give F(x)=2Ξ(x), hence

Â(2x)=Ξ'(x)²−Ξ(x)Ξ''(x).

Positive definiteness of A requires this expression to be nonnegative at every real x. Positivity of k alone does not establish even this first associated-kernel requirement: the positive smooth kernel

k(u)=g_0(u)+(g_0(u−2)+g_0(u+2))/4,  g_0(u)=π^(−1/2)e^(−u²),

has Â(π)<0. This is a comparison kernel, not the actual theta kernel and not a counterexample to RH.

**Proof.** The decay assumption gives every absolute moment. For any fixed t the defining integrals converge. On compact t intervals their integrands are bounded by a constant times s² exp(−2B|s|), so A is continuous. Under u=s+t, v=s−t the absolute Jacobian is 1/2. Consequently

∫_R |A(t)|dt ≤ (1/8)∫∫ (u+v)²|k(u)k(v)|du dv <∞.

The same calculation with any polynomial in t proves the weighted absolute integrability used below. Dominated differentiation gives F'=∫iu k(u)e^(ixu)du and F''=−∫u²k(u)e^(ixu)du. Evenness makes F and its derivatives real on the real axis.

Since s²=(s+t)(s−t)+t² and k(s−t)=k(t−s), the substitution v=s−t directly gives A=C_g(2t)+t²C_k(2t). Fubini with the preceding absolute moment bounds gives

Â(2x)=(1/8)∫∫(u+v)²k(u)k(v)e^(ix(u−v))du dv.

The u² and v² terms each contribute −FF''. The 2uv term contributes 2F'²: indeed ∫u k(u)e^(ixu)du=−iF', and its complex conjugate is iF'. This proves the asserted factor 1/4.

Independently, the substitution h=2t gives the transform of C_g(2t) as |∫g(u)e^(ixu)du|²/2=F'²/2. The transform of C_k(2t) is F²/2. Differentiating twice with respect to the frequency 2x shows that multiplication by t² gives −(F²)''/8. This also checks the signed decomposition and scaling.

Here positive definiteness means Σ a_j conjugate(a_l) A(t_j−t_l)≥0 for every finite set of real t_j and complex a_j. For continuous A it implies the same inequality integrated against a bounded continuous density on a compact interval, by Riemann sums. Taking density e^(iξt) on [−R,R] therefore gives

0≤∫_[−R,R]∫_[−R,R] A(t−s)e^(iξ(t−s))dt ds
  =∫_[−2R,2R] (2R−|h|)A(h)e^(iξh)dh.

Divide by 2R and use dominated convergence with A integrable. It follows that Â(ξ)≥0. Thus a negative Fourier value rules out positive definiteness, without an unstated spectral representation theorem.

For actual theta, L019 gives the required decay and continuity of the even extension, and L020 identifies its Fourier transform. No differentiability across zero is needed here.

For the comparison example the elementary Gaussian integral and a real shift give F(x)=G(x)q(x), where G(x)=e^(−x²/4) and q(x)=1+(1/2)cos(2x). A direct product differentiation yields

F'²−FF''=G²[(q'²−q q'')+q²/2],

because G'²−GG''=G²/2. At x=π/2, q=1/2, q'=0, q''=2. Therefore F'²−FF''=−(7/8)e^(−π²/8), and

Â(π)=−(7/32)e^(−π²/8)<0.

All hypotheses hold for the finite positive Gaussian mixture. This finishes the proof. ∎

The exact threshold isolated here is F'²−FF''≥0 for every real argument, not just where F vanishes (where it is automatically nonnegative). Even establishing it for actual theta would leave higher associated kernels and the all-degree mixed-positivity gap unresolved. No bound for those forms is obtained.

**Mathlib.** Not checked for the full statement or supporting Fourier, Gaussian-integral, and positive-definiteness results. No matching theorem is claimed. General documentation: https://leanprover-community.github.io/mathlib4_docs/
