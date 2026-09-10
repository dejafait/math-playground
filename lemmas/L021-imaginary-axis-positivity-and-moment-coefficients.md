# Lemma 21: imaginary-axis positivity and moment coefficients

**Hypotheses.** K is the kernel in Lemma 19. Define M_{2n}=∫_0^∞u^{2n}K(u)du for integers n≥0.

**Conclusion.** Every M_{2n} is finite and strictly positive,

Ξ(z)=Σ_{n≥0}(-1)^n M_{2n}z^{2n}/(2n)!,

with convergence on C, and Ξ(iy)>0 for every real y. Also M_{2n+2}²≤M_{2n}M_{2n+4} for every integer n≥0.

**Proof.** Finiteness follows from Lemma 19, and positivity follows because K(u)>0 on u>0. On |z|≤R, the sum of the absolute values of the cosine-series terms is at most cosh(Ru)≤e^{Ru}. The integrable majorant K(u)e^{Ru} permits exchanging the series and integral in Lemma 20 by dominated convergence (or absolute Fubini). Substitution z=iy gives Ξ(iy)=∫_0^∞K(u)cosh(yu)du>0. Finally apply Cauchy–Schwarz in the measure K(u)du to u^n and u^{n+2}. Their scalar product is M_{2n+2} and their squared norms are M_{2n} and M_{2n+4}. ∎
