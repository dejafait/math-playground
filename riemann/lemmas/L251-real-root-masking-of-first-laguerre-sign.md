# Lemma 251: real-root masking of the first Laguerre sign

**Hypotheses.** Let a=10+i/4 and let P and F=P cos(z/100) be the functions of L029. Put

H(z)=(1−z²/100)F(z),    Q_J(t)=J′(t)²−J(t)J″(t).

All real-axis derivatives below are ordinary derivatives. Define A_H(x)=H(i√x) by its entire power series and G_H=A_H′/A_H for x≥0.

**Conclusion.** Q_F(10)<0, but Q_H(t)>0 for every real t. Nevertheless H has the nonreal zeros ±a, ±conj(a). It is even, real on R, of order at most one, has infinitely many zeros all satisfying |Re z|>4 and |Im z|<1/2, has strictly alternating nonzero even Taylor coefficients, and is positive on the imaginary axis. G_H is strictly completely monotone on [0,∞) and has no positive Stieltjes representation with integrable weight (1+s)^(−1). Thus whole-real-axis first Laguerre positivity, even combined with these localization and scalar-sign properties, does not force real zeros. No positive Fourier-kernel representation for H is asserted.

**Proof.** Away from real zeros, logarithmic differentiation of a real entire function gives

Q_J(t)/J(t)²=−(J′/J)′(t).

A linear root factor at ρ contributes 1/(t−ρ)² to this expression. A conjugate pair at c±ib, with c real and b>0, contributes

2((t−c)²−b²)/((t−c)²+b²)².

The cosine factor contributes 10^(−4)sec²(t/100). These identities follow by differentiating the finite product; no infinite product interchange is needed.

For F at t=10, the pair centered at 10 contributes −2/b²=−32 with b=1/4. The real roots ±5 contribute 1/25+1/225<1. The conjugate pair centered at −10 contributes

2(400−b²)/(400+b²)² < 2/400 < 1.

Finally cos(1/10)≥1−(1/10)²/2>1/2, so the cosine contribution is less than 4/10000<1. Thus Q_F(10)/F(10)²<−29. None of the factors of F vanishes at 10, proving strict negativity.

Multiplication by 1−z²/100 adds real roots at each conjugate pair's real center. For u=t−c≠0, the combined contribution of the real root c and the two nonreal roots c±ib is exactly

1/u² + 2(u²−b²)/(u²+b²)²
 = (3u⁴+b⁴)/(u²(u²+b²)²) > 0.

Apply this separately with c=10 and c=−10. Away from the real roots of H, the remaining contributions from ±5 and from the cosine are also strictly positive. This proves Q_H(t)>0 there. At a real root r, Q_H(r)=H′(r)²>0 because every real root is simple: ±5 and ±10 are distinct, the cosine roots have absolute value at least 50π>10 and are simple, and the nonreal-root factors never vanish on R. This covers every real t without taking a singular logarithmic derivative at a root.

The additional factor has only the roots ±10, so L029 gives the claimed zero localization, nonreal roots and infinitely many zeros. The bound |H(z)|≤C(1+|z|)^8 exp(|z|/100) gives order at most one. If F(z)=Σ_(n≥0)(−1)^n d_n z^(2n) with d_n>0, the new coefficient magnitudes are d_0 and d_n+d_(n−1)/100>0 for n≥1. Also H(iy)=(1+y²/100)F(iy)>0.

On x≥0, A_H(x)=(1+x/100)A_F(x), hence

G_H(x)=1/(x+100)+G_F(x).

L247 proves strict complete monotonicity of G_F. Since (−1)^k (d/dx)^k (x+100)^(−1)=k!/(x+100)^(k+1)>0, the same holds for G_H at every order including right derivatives at zero. Finally its added term is analytic at −a², so G_H retains the residue-one nonreal pole of G_F there. A positive Stieltjes integral with the stated weight would be holomorphic on C\(−∞,0], by the compact domination proved in L247. The identity theorem on this slit domain with the two nonreal poles removed contradicts the retained pole, exactly as in that proof. ∎

The achieved inequality is strict at every real point, not only on compact sets or away from zeros. It remains a first-level test; the required all-degree mixed positivity is not obtained. This is a counterexample to a proposed generic implication, not to RH or to a statement with additional actual-theta hypotheses.

**Mathlib.** Not checked: coverage of the full counterexample and its elementary logarithmic-derivative identities was not checked. No matching or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
