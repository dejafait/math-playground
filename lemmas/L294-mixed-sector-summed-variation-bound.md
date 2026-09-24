# Lemma 294: signed mixed-sector bound by summed amplitude variation

**Hypotheses.** Use the exact summands T_jk(u,v) and coordinate Jacobian from L292, and the parameters of L269. Let a tend to infinity with h in a fixed compact interval [h₀,h₁] contained in (5,∞). Put H=h−9/2=n/r, p=2n, and γ=2(h₀−9/2)log 2−1/2>0. Let Q_jk be the clipped cores of L293.

**Conclusion.** Uniformly in this range,

(1/2) Σ_(j,k≥1) |∫_(u,v>0) T_jk(u,v) du dv|
 ≤ C exp(Φ_*) exp(−γr)/a = o(exp(Φ_*)/a).

The series can be integrated termwise over this whole sector. Moreover,

(1/2) Σ_(j,k≥1) |∫_((0,∞)²\Q_jk) T_jk(u,v) du dv|
 ≤ C exp(Φ_*) (1+r²)exp(−γr)/a = o(exp(Φ_*)/a).

The opposite mixed sector satisfies the same bounds by conjugation and reflection. This supplies mixed-sector control, not a whole-plane positivity theorem.

**Proof.** All constants below are uniform on the specified compact h-band. We have r~(log a)/2 and p=2Hr tending to infinity. Factor the exact expression of L292 as

T_jk=C₀ exp(−2aτ) exp(9iτ) A_jk(u,v) exp(iφ_j(u)+iφ_k(v)),
A_jk=P(u−v) B_j(u) B_k(v),
P(w)=(w/2)^p,
B_j(u)=j⁴ exp(9u/2−q(u)j²) E_j(u),
q(u)=(h/2)exp(2(u−r)),
φ_j(u)=au−π sin(2τ)j²exp(2u).

Here C₀=(8π²)², and E_j is the exact complex factor in L292. Since u≥0 and j≥1, both E_j and E'_j are uniformly bounded: their nonconstant part has modulus 3/(2πj²exp(2u)), and differentiation multiplies it by −2. Hence

|B_j(u)|+|B'_j(u)|
 ≤ C j⁴ exp(9u/2)(1+q(u)j²)exp(−q(u)j²).                 (1)

We first prove an index-summed envelope. For every q>0,

Σ_(j≥1) j⁴(1+qj²)exp(−qj²) ≤ C q^(−5/2)exp(−q/2).     (2)

For q≤1, the Gaussian fourth and sixth moment sum estimates give respectively O(q^(−5/2)) and O(q·q^(−7/2)); these follow by scaling the integrals and adding the maximum of each unimodal summand. The factor exp(−q/2) is bounded below in this range. For q≥1, factor out exp(−q), and bound the remaining series by C(1+q) using j²−1≥0 and convergence at q=1. The inequality (1+q)exp(−q)≤Cq^(−5/2)exp(−q/2) finishes (2).

Consequently, for c=h₀/4, (1) implies

Σ_j (|B_j(u)|+|B'_j(u)|) ≤ C exp(5r) W(u),
W(u)=exp(−u/2) exp(−c exp(2(u−r))).                     (3)

Next, for ℓ=0,1,2 and all real w, the normalized polynomial satisfies

|d^ℓ/dw^ℓ (w/(2r))^p|
 ≤ C 2^(−p)exp(−p)exp(2H|w|).                         (4)

For ℓ=0 this is log t≤t−1 with t=|w|/r. For ℓ>0 maximize t^(p−ℓ)exp(−pt) at t=(p−ℓ)/p; the ratio of the resulting bound to the right side of (4) is at most

(p(p−1)⋯(p−ℓ+1)/r^ℓ) exp(ℓ)(1−ℓ/p)^(p−ℓ),

which is bounded since p/r=2H stays bounded and p>2 eventually. Values at w=0 follow directly by continuity.

Define the normalized amplitude

Ā_jk=exp(−9r+h) ( (u−v)/(2r) )^p B_j(u) B_k(v).

Thus T_jk=C₀ exp(Φ_*) exp(9iτ) Ā_jk exp(iφ_j+iφ_k). By the product rule, (3) and (4), for b,d in {0,1},

Σ_jk |∂_u^b ∂_v^d Ā_jk|
 ≤ C exp(r) 2^(−p)exp(−p) exp(2H|u−v|) W(u)W(v).       (5)

There is no singular division by u−v in this estimate; in particular it holds on the diagonal. To integrate (5), use

exp(2H|u−v|) ≤ exp(2Hu−2Hv)+exp(−2Hu+2Hv).

For b₊=2H−1/2, which stays in a compact positive interval,

∫₀^∞ exp(2Hu)W(u)du
 = exp(b₊r) ∫_(−r)^∞ exp(b₊t−c exp(2t))dt
 ≤ C exp((2H−1/2)r).

The integral over the whole real t-axis converges uniformly: the left tail has positive exponential rate b₊ and the right tail has superexponential decay. Also

∫₀^∞ exp(−2Hu)W(u)du ≤ ∫₀^∞ exp(−(2H+1/2)u)du ≤ C.

Since p=2Hr, integrating (5) therefore gives

Σ_jk ∫₀^∞∫₀^∞ |∂_u^b ∂_v^d Ā_jk| du dv
 ≤ C exp((1/2−2H log 2)r) ≤ C exp(−γr).                (6)

Tonelli applies here to nonnegative terms. In particular b=d=0 proves absolute integral summability of the original series for each parameter value. Together with L292's pointwise exact expansion this justifies termwise integration.

It remains to retain oscillation and check boundaries. Translating y=u−r+log j gives, up to a constant,

φ_j(u)=f(y),  f(y)=a(y−exp(2y)/2).

Uniformly over every finite interval J on the real line,

|∫_J exp(if(y))dy|≤C/sqrt(a).                           (7)

Indeed the part |y|≤a^(−1/2) is bounded by its length. On each side f'=a(1−exp(2y)) is monotone and has magnitude at least c sqrt(a). Integration by parts bounds each remaining interval by reciprocal endpoint slopes plus ∫|f''|/|f'|², which is a difference of reciprocal slopes. This is the same elementary bounded-primitive argument used in L275, here valid on the entire line. It is uniform in the translated lower endpoint, including stationary points approaching u=0.

Let U_j(u)=∫₀^u exp(iφ_j(t))dt, so |U_j|≤C/sqrt(a) and U_j(0)=0. For a fixed j,k, integrate by parts in both variables on [0,R]×[0,S]. All lower-edge terms vanish because these primitives vanish at zero. The upper-edge and upper-corner terms tend to zero as R,S tend to infinity: Ā_jk and its first derivatives are polynomials times factors with superexponential decay in either variable at positive infinity. The derivatives are integrable, as also follows from (6). Thus

∫∫ Ā_jk exp(iφ_j+iφ_k)=∫∫ (∂_u∂_v Ā_jk) U_j(u)U_k(v),

and its modulus is at most (C/a)∫∫|∂_u∂_v Ā_jk|. Equivalently this is the rectangular primitive identity of L275 with the endpoints passed to infinity; no unestimated u=0 or v=0 term is discarded. Sum this estimate using (6) with b=d=1, and restore C₀ exp(Φ_*) and the Jacobian 1/2. This proves the first assertion.

For the complements subtract each core integral from its whole-sector integral and use the triangle inequality and L293's summed absolute core estimate. This yields the stated (1+r²) factor. Reflection x↦−x conjugates the original shifted integrand because the theta kernel is real on the real axis, while s^(2n) is real; it maps the two mixed sectors to each other. Finally exp(−γr)(1+r²) tends to zero, proving all asserted little-o statements. ∎

This argument does not assert that the summed absolute integrand is o(exp(Φ_*)/a): (6) without oscillation only gives O(exp(Φ_*)exp(−γr)). The two primitive bounds supply the essential extra 1/a. Small-argument parts of the same-sign sectors and the fixed-h global assembly have not been checked here.

**Mathlib.** Full statement: not checked. Supporting Gaussian moment estimates, integration by parts, Tonelli/Fubini, and exponential domination: not checked. No full or supporting library match is claimed. L269 supplies normalization and parameter identities; L292 supplies the exact reflected summands; L275 supplies the rectangular primitive mechanism, explicitly justified here at the unbounded endpoints; L293 supplies the core estimate used only for the complement conclusion.
