# Lemma 295: signed same-sign boundary-strip bound

**Hypotheses.** Use the theta kernel, shifted integrand F and parameters a,n,r,h,τ,Φ_* of L269. Let a tend to positive infinity with h in a fixed compact interval [h₀,h₁] contained in (5,∞). Thus n=r(h−9/2), and r tends to infinity. Define

S₊={s+x≥0, s−x≥0, min(s+x,s−x)≤r/4}.

Let S₋ be its reflection under s↦−s. Boundaries have planar measure zero. Constants and limits below are uniform over the stated h-band and admissible integers n.

**Conclusion.** The exact theta summands are absolutely integrable and integrally summable over S₊ for each parameter value. Their signed integrals satisfy

Σ_(j,k≥1) |∫∫_(S₊) F_jk(s,x) ds dx| = o(exp(Φ_*)/a).

In particular |∫∫_(S₊) F|=o(exp(Φ_*)/a), and the same bound holds on S₋. This controls the small-argument pieces omitted from L288's same-sign sector. It is not itself a global Laguerre positivity theorem.

**Proof.** Put p=2n, H=h−9/2, and C₀=(8π²)². On the positive same-sign quadrant use u=s+x≥0, v=s−x≥0. The absolute Jacobian is 1/2. The exact theta expansion in L269 gives the summand in these coordinates as

T_jk(u,v)=C₀ exp(Φ_*) A_jk(u,v) exp(iφ_j(u)−iφ_k(v)),
φ_j(u)=au−π sin(2τ)j²exp(2u),
A_jk=exp(−9r+h) ((u+v)/(2r))^p j⁴k⁴
 · exp(9(u+v)/2−(h/2)(j²exp(2(u−r))+k²exp(2(v−r))))
 · E_j(u) overline(E_k(v)),
E_j(u)=1−3/(2πj²exp(2u+2iτ)).                         (1)

Indeed the exponential factors from the two kernel arguments have imaginary constants +9τ/2 and −9τ/2, which cancel; 2ax=a(u−v). The saddle identities give 2πexp(2r)cos(2τ)=h and 2πexp(2r)sin(2τ)=a. The series converges absolutely pointwise on this quadrant for every fixed τ<π/4. Integral interchange will follow from an explicit bound below.

The derivative issue at u+v=0 is removed before estimating the series. For ℓ=0,1,2, and w≥0, one has, for sufficiently large r,

|d^ℓ/dw^ℓ (w/(2r))^p| ≤ C exp(H(w−2r)).               (2)

To prove this, put t=w/(2r). For ℓ=0, log t≤t−1 proves the assertion for t>0, and continuity handles zero. For ℓ≥1, the supremum of t^(p−ℓ)exp(−p(t−1)) occurs at t=1−ℓ/p. Thus the optimal multiplier is

(p)_ℓ/(2r)^ℓ · exp(ℓ)(1−ℓ/p)^(p−ℓ),

which is bounded because p/(2r)=H stays in a fixed compact positive interval and p>2 eventually. This also covers w=0 by continuity. Mixed differentiation of the polynomial in (1) uses precisely these three derivatives, so no division by u+v is needed.

Set y=u−r+log j, z=v−r+log k, and define

g_h(t)=exp(h t−(h/2)(exp(2t)−1)),
M_h(t)=(1+exp(2t))g_h(t),
w_jk=(jk)^(4−h).

Both E_j and E'_j are bounded uniformly for u≥0, j≥1. Differentiating the other one-variable factor in (1) introduces 9/2−h exp(2y), or its z counterpart. Therefore (2), the product rule, and h≤h₁ give, for b,d∈{0,1},

|∂_u^b ∂_v^d A_jk(u,v)| ≤ C w_jk M_h(y)M_h(z).       (3)

For completeness, the undifferentiated exponential after applying (2) is exactly bounded by

j⁴k⁴ exp(h(u+v−2r)+h−(h/2)(exp(2y)+exp(2z)))
 = w_jk g_h(y)g_h(z).

This verifies the index power and normalization in (3); the derivative multipliers are absorbed by the two factors 1+exp(2t).

Uniformly in the compact h-band, M_h has bounded supremum and bounded integral on the whole real line. On t≤0 it is at most C exp(h₀t). On t≥0 it is bounded by C(1+exp(2t))exp(h₁t−(h₀/2)exp(2t)), an integrable function tending to zero at infinity. In particular

Σ_jk ∫₀^∞∫₀^∞ |A_jk(u,v)| du dv
 ≤ C Σ_jk(jk)^(−(h₀−4)) < ∞.                         (4)

Here h₀−4>1 is essential. Tonelli for the majorants followed by absolute Fubini justifies integrating the exact theta series, on the full quadrant and on its boundary strips, for each parameter value.

We next retain the oscillation. The bounded-primitive calculation in L294 applies unchanged to φ_j: after translating y=u−r+log j it is a constant plus a(y−exp(2y)/2). For either phase sign and any interval J,

|∫_J exp(±iφ_j(u))du|≤C a^(−1/2),                   (5)

uniformly in j and the interval endpoints. This estimate includes stationary points at or near zero; it does not assume a nonstationary phase throughout the interval.

Here are the boundary terms explicitly. On R=[0,U]×[0,V], anchor the two primitives at zero. Integrating by parts in both variables bounds the signed integral of A_jk by C/a times

|A_jk(U,V)| + ∫₀^U |∂_u A_jk(u,V)|du
 + ∫₀^V |∂_v A_jk(U,v)|dv
 + ∫₀^U∫₀^V |∂_u∂_v A_jk(u,v)|du dv.                (6)

All lower-edge terms vanish because the anchored primitives vanish there. Define

N_j(U)=M_h(U−r+log j)+∫₀^U M_h(u−r+log j)du

when U is finite, and N_j(∞)=∫₀^∞ M_h(u−r+log j)du. Bound (3) makes (6) at most C w_jk N_j(U)N_k(V). Infinite endpoints follow by a limit: for fixed indices, A_jk and the needed derivatives decay superexponentially at positive infinity in either variable, and (3) supplies integrable domination. Thus their upper-edge terms tend to zero, exactly as expressed by N_j(∞). All N_j(U) are bounded by one uniform constant.

Take L=r/4. The region min(u,v)≤L is the union of R₁=[0,L]×[0,∞) and R₂=[0,∞)×[0,L], with intersection R₀=[0,L]². Inclusion-exclusion and (6) give

|∫_(R₁∪R₂) A_jk exp(iφ_j−iφ_k)|
 ≤ (C/a) w_jk [N_j(L)N_k(∞)+N_j(∞)N_k(L)+N_j(L)N_k(L)].   (7)

For each fixed j, uniformly in h,

N_j(L) ≤ M_h(Y_j)+∫_(−∞)^(Y_j) M_h(t)dt →0,
Y_j=−3r/4+log j →−∞.                                (8)

Indeed the negative-tail majorant above bounds the right side by C exp(h₀Y_j) once Y_j≤0. Thus the bracket in (7) tends uniformly to zero for each fixed pair, while remaining uniformly bounded for every pair. Since w_jk≤(jk)^(−(h₀−4)), the summable majorant yields a summed little-o bound: choose a fixed finite index square to make its complementary weight sum arbitrarily small; on that square use (8). This argument handles growing indices whose stationary points lie inside or near the strips without incorrectly treating them as fixed.

Restoring C₀exp(Φ_*) and the Jacobian 1/2 proves the claimed summed o(exp(Φ_*)/a) estimate. Finally F(−s,x)=F(s,x) by evenness of the theta kernel and the even polynomial s^(2n): the two kernel factors are interchanged. This maps S₊ onto S₋ and proves the second assertion. ∎

The gained 1/a comes from signed primitives, not an absolute-integrand estimate. The proof uses absolute summability only to interchange sums and integrals and dominate the index tails. It does not cover h approaching 5, where that summability deteriorates, nor h≤5. A separate global assembly must still check the principal coefficient and reflection factors against L288 and the mixed-sector estimate.

**Mathlib.** Full statement: not checked. Supporting theta expansions, integration by parts, absolute Fubini/Tonelli and dominated series limits: not checked. No full or supporting library match is claimed. L269 supplies the exact kernel and normalization; L294 supplies the uniform bounded-primitive estimate (5). The derivative bound, rectangular boundary accounting and summable boundary-strip limit are proved here.
