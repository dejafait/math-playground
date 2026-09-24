# Lemma 244: strict inverse-curvature slack for the exponential theta tilt

**Hypotheses.** Let K be the smooth positive even theta kernel of L048, W=−log K, and

Z(r)=∫_R K(u)e^{ru}du,   p_r(u)=K(u)e^{ru}/Z(r),

m(r)=E_r[U],   v(r)=Var_r(U),   A(r)=E_r[1/W″(U)].

Use F and G from L242. All parameters r below are real; formulas with r in a denominator concern r>0.

**Conclusion.** The tilt preserves positive potential curvature W″. The functions above are finite and continuous, m′(r)=v(r), and

G′(r²)=[r v(r)−m(r)]/(4r³).

There is ε>0 such that A(r)>m(r)/r for 0<r<ε. More precisely, with σ²=v(0)>0,

A(0)>σ²,   lim_{r→0}m(r)/r=σ².

Thus an inverse-curvature upper bound v(r)≤A(r) cannot establish the required threshold v(r)≤m(r)/r by comparing these right sides for every r>0. The conclusion does not determine the sign of G′.

**Proof.** By L019 and evenness, K times any polynomial times e^{R|u|} is integrable for every fixed R. Differentiation of Z under the integral on compact parameter intervals is therefore valid to every fixed order. Positivity gives Z>0; quotient differentiation gives m=(log Z)′ and m′=v. Evenness gives m(0)=0. L048 gives W″(u)>a e^{2|u|}, where a=68π/125>0. Hence 1/W″≤1/a, and dominated convergence gives continuity and finiteness of A. The tilted negative log density is W(u)−ru+log Z(r), proving the curvature assertion. Also Z(r)=2F(r²), so G(r²)=m(r)/(2r); differentiation gives the stated formula for G′.

We prove strictness at zero directly, including the integrations at infinity. Write p=p_0, and define

h(u)=p(u)^(−1)∫_u^∞ t p(t)dt.

The zero mean of p shows that h is even. It is smooth and positive: for u≥0 its defining integral is positive, and for u<0 this follows by evenness. Differentiation gives

(hp)′=−up,   h′−W′h=−u.

Here are sufficient tail bounds for every following integration. From L048 and W′(0)=0,

W′(u)≥(a/2)(e^{2u}−1) for u≥0.

Convexity gives p(u+t)/p(u)≤e^{−W′(u)t} for u>0,t≥0. Integrating (u+t) against this bound yields

0<h(u)≤u/W′(u)+1/W′(u)².

In particular h(u)=O((1+u)e^{−2u}). The defining differential equation also gives |h′(u)|≤u+W′(u)h(u)≤2u+1/W′(u) for u≥1.

We also have W′(u)=O(e^{2u}) and W″(u)=O(e^{2u}) as u→∞. For completeness these follow directly from the actual series in L019: put b=πe^{2u} and factor out its n=1 term to write

K(u)=4b(2b−3)e^{u/2}e^{−b}(1+R(u)),

R(u)=Σ_{n≥2} n²(2n²b−3)/(2b−3) e^{−(n²−1)b}.

For j≤2, termwise u differentiation bounds |R^(j)(u)| by C_j b^j e^{−3b} for b≥π. Indeed derivatives of the rational coefficients are bounded by constants times fixed powers of n, and derivatives of the exponential add at most b^j times fixed powers of n. Factor e^{−3b} from each term and bound the remaining sums by Σ_{n≥2} C n^M e^{−π(n²−4)}<∞. The same domination justifies differentiating the series. The first two logarithmic derivatives of the displayed n=1 factor are O(b), and those of log(1+R) have the asserted exponentially small bounds. This proves the required upper bounds. Evenness handles the other tail.

These estimates and the superexponential decay of p imply that uhp and W′h²p vanish at both infinities, and that all integrands in the following identities are absolutely integrable. Integrating (hp)′=−up against u yields

E_0[h]=E_0[U²]=σ².

Squaring h′−W′h=−u, integrating, and integrating its cross term gives

σ²=E_0[(h′)²]+E_0[W″h²].

Explicitly, the cross term is −∫W′(h²)′p=∫(W″−(W′)²)h²p, with the vanishing boundary term just verified; this cancels the square of W′. Put B=E_0[W″h²]>0. In fact B<σ². Otherwise E_0[(h′)²]=0; continuity and p>0 force h′ identically zero. Then h is a positive constant and the differential equation gives W′(u)=u/h, so W″ is constant. This contradicts W″(u)>a e^{2|u|}.

Cauchy–Schwarz, applied to h√W″ and 1/√W″, now gives

σ⁴=(E_0[h])²≤B A(0)<σ² A(0).

Since σ²>0, this proves A(0)>σ². Finally m′(0)=σ² and m(0)=0 give m(r)/r→σ². The continuous difference A(r)−m(r)/r, extended at zero, is strictly positive there; it stays positive for all sufficiently small positive r. ∎

The proof establishes strict slack without assuming an external variance theorem. The screened inverse-curvature estimate is only an upper-bound mechanism: exceeding its target does not show that the true variance exceeds that target. In particular no first-sign failure, positive Stieltjes measure, all-degree positivity, or RH resolution follows.

**Mathlib.** Not checked: coverage of the full strict-slack statement and supporting integration-by-parts and Cauchy–Schwarz results was not checked. No matching theorem is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
