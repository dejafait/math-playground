# Lemma 55: the combined generic conditions admit nonreal zeros

**Hypotheses.** Let 0<a≤1/100, c_a=cosh(a/10), and

h_a(u)=[c_a g(u)+(g(u-a)+g(u+a))/2]/(c_a+1),  g(u)=exp(-cosh(2u)).

Let F_a be the Fourier transform of h_a.

**Conclusion.** Every F_a has all of the following properties: entire order at most 1; evenness and reality on R; a smooth strictly positive even kernel with superexponential decay and (log h_a)''<-cosh(2u)/4; strictly alternating nonzero even Taylor coefficients; positive values on the imaginary axis; and every zero in |Re z|>4, |Im z|<1/2. Nonetheless it has nonreal zeros at (2k+1)π/a±i/10 for every integer k.

In addition, there exists a_*∈(0,1/100] such that u↦log h_a(√u) is strictly concave on (0,∞) for every 0<a≤a_*. This additional assertion is not claimed for the whole original parameter interval.

For these same 0<a≤a_*, every admissible weight f(z)=Cz^{2r}∏_j(1−z²/b_j²), where r≥0 is integral, b_j>0, Σ_j b_j⁻²<∞ and A=(−1)^r C>0, satisfies the full weighted adjacent-moment inequalities. Specifically, for every real λ and integer m≥1, put

B_m=∫₀∞t^{2m}e^{λt²}f(it)h_a(t)dt.

Then B_m²>((2m−1)/(2m+1))B_{m−1}B_{m+1}. The product may be empty, finite or infinite. The parameter a is chosen independently of m, λ and f. These inequalities therefore do not force real Fourier zeros, even together with the other stated conditions.

**Proof.** The proof of Lemma 50 is uniform when 0<a≤1/100: the bounds e^{2a}<2 and sinh(2a)<1/40 only improve as a decreases. The three normalized weights here have maximum ratio 2c_a<4<18, so the identical curvature proof applies. Lemma 51 supplies the entire order. Positivity and evenness of the kernel give imaginary-axis positivity and nonzero alternating even coefficients by the same dominated cosine expansion as Lemma 21, applied to 2h_a on [0,∞).

The shift formula gives F_a(z)=[c_a+cos(az)]G(z)/(c_a+1). As in Lemma 52, every prefactor zero is exactly (2k+1)π/a±i/10. Its real part has absolute value ≥100π>4 and its imaginary part has absolute value 1/10. Lemma 54 places every zero of G on the real axis with absolute value >4. Products of entire functions have precisely the union of their zero sets, with added multiplicities, so these two lists locate all F_a zeros. All the stated properties hold simultaneously, but the displayed prefactor zeros are nonreal.

For the additional assertion extend the formula to a=0, where h_0=g, and put ℓ_a(t)=log h_a(t). The function h_a(t) is jointly smooth and positive for real (a,t), with a positive minimum on [0,1/100]×[0,17]. Thus its fourth logarithmic derivative is jointly continuous there and converges uniformly as a→0 to ℓ_0''''(t)=−16cosh(2t)≤−16. Uniform continuity supplies a_*∈(0,1/100] such that ℓ_a''''(t)≤−8 for 0≤a≤a_* and 0≤t≤17.

Evenness gives ℓ_a'''(0)=ℓ_a'(0)=0. Therefore ℓ_a'''(t)≤−8t on [0,17]. Put D_a(t)=tℓ_a''(t)−ℓ_a'(t). Since D_a(0)=0 and D_a'(t)=tℓ_a'''(t), integration gives

D_a(t)≤−8t³/3<0 for 0<t≤17.

For t≥17 the global curvature bound already proved gives ℓ_a''(t)<−cosh(2t)/4. Differentiation of the positive mixture gives −ℓ_a'(t)=Σ_s w_s 2sinh(2(t+s)), with s∈{−a,0,a} and positive weights summing to one. Monotonicity and the addition formula give

−ℓ_a'(t)≤2sinh(2(t+a))≤2e^{2a}cosh(2t)<4cosh(2t).

Consequently D_a(t)<(4−t/4)cosh(2t)≤−cosh(2t)/4<0 for t≥17. This tail estimate is uniform for 0<a≤1/100. Finally, with t=√u,

(d²/du²)log h_a(√u)=D_a(t)/(4t³)<0.

The compact estimate controls the endpoint t→0 and the tail estimate controls all unbounded t. No pointwise convergence on an unbounded interval is promoted to uniform convergence. The explicit nonreal Fourier zeros persist for every such positive a.

To prove the weighted assertion directly, fix any allowed a, λ and f. Set P(u)=∏_j(1+u/b_j²), S=Σ_j b_j⁻², ψ(u)=log h_a(√u), and

w(u)=A u^r exp(λu)P(u)h_a(√u),  u>0.

The product is positive, P(u)≤exp(Su), and its logarithm can be differentiated twice locally uniformly on (0,∞). Indeed the first derivative series is bounded by S and the second by Σ_j b_j⁻⁴≤S². Hence, with V=−log w,

V''(u)=r/u²+Σ_j(b_j²+u)⁻²−ψ''(u)>0.

This includes empty products and every real λ; linear exponential weights contribute zero curvature. Near zero, w(u)=A h_a(0)u^r(1+O(u)), while V'(u)=−r/u+O(1). Smoothness of h_a(√u) at zero follows from its even analytic defining formula. For t=√u≥1, the finite mixture bounds give

h_a(t)≤exp(−cosh(2(t−a))),  |ψ'(u)|≤sinh(2(t+a))/t.

Thus w and its derivative, multiplied by any fixed real power of u, are integrable at infinity: exp((|λ|+S)u) and the derivative factor O(exp(2√u)) are dominated by exp(−cosh(2(√u−a))). These estimates also justify every boundary limit and integral below. They are needed only for each fixed weight, not uniformly over all weights.

Put I_s=∫₀∞u^{s−1}w(u)du. For p=m−1/2>0 the three integrals I_p, I_{p+1}, I_{p+2} are finite and positive. Both u^p w(u) and u^{p+1}w(u) vanish at zero and infinity. Integration of their derivatives, with w'=−V'w, yields

∫₀∞u^p V'(u)w(u)du=p I_p,
∫₀∞u^{p+1} V'(u)w(u)du=(p+1)I_{p+1}.

All integrals are absolutely convergent, including at zero since p+r>0. Let U have probability density u^p w(u)/I_{p+1}. For an independent copy U', strict increase of V' gives

2 Cov(U,V'(U))=E[(U−U')(V'(U)−V'(U'))]>0.

Strictness holds because the density is positive on (0,∞), and all expectations exist by the estimates above. Substituting the two integration identities gives

(p+1)−p I_p I_{p+2}/I_{p+1}²>0.

Finally u=t² gives B_j=I_{j+1/2}/2, so this is exactly the claimed inequality. This argument treats the infinite product directly and does not infer a strict limiting inequality from strict finite inequalities. The same a works for all weights because its only restriction is the already established ψ''<0. ∎

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
