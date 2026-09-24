# Lemma 269: eventual Laguerre positivity at proportional indices

**Hypotheses.** Let k be the even theta kernel of L019, extended to |Im z|<π/4 as in L239. Use the generalized Laguerre coefficients D_n(Ξ;a) of L267. Fix 0<λ_0≤λ_1<∞. Let a→+∞ and let n≥1 be an integer with λ_0≤n/a≤λ_1. All constants and error limits below are uniform in this range, but may depend on λ_0,λ_1.

Define r>0, h, and τ by

(2πe^(2r))²=a²+(n/r+9/2)²,
h=n/r+9/2,   τ=(1/2)arctan(a/h).

Put

Φ_*=2n log r+9r−h−2aτ,
B=[[2n/r²+4h, 4ia], [4ia, 4h]].

**Conclusion.** With the positive square root of det B,

I_n(a):=∫∫ s^(2n)k(s+t)k(s−t)e^(2iat) ds dt
       =(8π²)² e^(Φ_*) (4π/sqrt(det B)) · (1+o(1)).

Consequently D_n(Ξ;a)>0 for every sufficiently large a in the stated index range. Evenness gives the corresponding assertion for |a|→∞. This is not a uniform assertion down to n/a=0.

**Proof.** The equation defining r has exactly one positive solution: its left side is strictly increasing from a finite value to infinity and its right side is strictly decreasing from infinity to a finite value. It gives

r=(1/2)log(a/(2π))+O((log a)^(−2)),
h~2n/log a,   δ:=cos(2τ)=h/sqrt(a²+h²)~h/a.

Indeed r≥(1/2)log(a/(2π)), hence h/a=O(1/log a), and taking logarithms of the defining equation gives the asserted estimate for r. In particular r→∞, h is comparable to a/log a, and δ^(−1)=O(log a).

For each fixed a,n shift t to x+iτ. The strip analyticity and decay in L239, on the closed smaller strip with height τ, justify the shift and Fubini, giving

I_n(a)=e^(−2aτ)∫∫ s^(2n)k(s+x+iτ)k(s−x−iτ)e^(2iax) ds dx.       (1)

For clarity, the necessary domination is a polynomial times the product of superexponentially decreasing functions of s+x and s−x. On a vertical contour edge the same bound applies uniformly between heights 0 and τ; for each fixed s those edges vanish. Absolute domination on the intermediate horizontal lines then permits integration in s. No uniform-in-τ constant is needed to obtain this parameterwise identity. Uniform estimates for its value follow next.

First we make the global strip estimate quantitative. For real y and 0<τ<π/4,

|k(y±iτ)|≤C δ^(−5/2)e^(9|y|/2) exp(−πδe^(2|y|)).             (2)

For y≥0 the theta series bounds the left side by

C e^(9y/2) Σ_(j≥1) j⁴ exp(−j²q),   q=πδe^(2y).

Here the lower-degree prefactor is absorbed since y≥0 and j≥1. The elementary sum bound

Σ j⁴ exp(−j²q)≤C e^(−q)(1+q^(−5/2))

follows for q≥1 by factoring out e^(−q) and summing at q=1, and for 0<q≤1 by comparison with the Gaussian moment integral after the scaling t=√q j (or splitting into intervals of length 1/√q). Since q≥πδ, this proves (2). Evenness and conjugation of k extend it to y<0. In particular its constant C is independent of τ.

On s>0 introduce the positive-tail model k_0(z)=8π²exp(9z/2−πe^(2z)) and its shifted phase

Φ(s,x+iτ)=2n log s+9s−2πe^(2s)cosh(2x+2iτ)+2iax−2aτ.

Its derivatives vanish at (s,x)=(r,0), since 2πe^(2r)cos(2τ)=h and 2πe^(2r)sin(2τ)=a. Its negative Hessian is B. Thus det B=16(h²+a²)+8hn/r²>0 and Re B is positive definite.

Set ε=h^(−2/5). In the square |s−r|≤ε, |x|≤ε, the real parts of both kernel arguments are r+O(ε). If v=πe^(2z) at either argument, then |v| is comparable to a and Re v is comparable to h. The exact series gives uniformly there

k(z)/k_0(z)=1−3/(2v)+Σ_(j≥2)(j⁴−3j²/(2v))e^(−(j²−1)v)
           =1+O(a^(−1))+O(e^(−c h)).                         (3)

To bound the sum, factor out e^(−3 Re v); the remaining polynomially weighted series is bounded uniformly for Re v≥1. There is no assumption about zeros of k.

All third derivatives of Φ in this square are O(a+n/r³)=O(a). Real-variable Taylor's theorem, applied to real and imaginary parts, therefore gives, for u=s−r,

Φ(s,x+iτ)=Φ_*−(u,x)B(u,x)^T/2+R(u,x),
|R|≤C a ε³.

Here aε³=O(a^(−1/5)(log a)^(6/5))→0. Combining with (3), the integral over the square differs from the model Gaussian integral over that square by at most

C(8π²)²e^(Φ_*) η/h,
η=aε³+a^(−1)+e^(−c h).                                      (4)

Indeed |e^R−1|≤C|R|, and the integral of the Gaussian modulus on the whole plane is

2π/sqrt((2n/r²+4h)4h)=O(1/h).

Successive real Gaussian Fourier integration gives the signed integral

∫∫ exp(−(u,x)B(u,x)^T/2) du dx=2π/sqrt(det B),                (5)

which is positive and comparable to 1/a. The omitted Gaussian tails outside the square have modulus at most C h^(−1)exp(−c h ε²), since both diagonal entries of Re B are at least 4h. The relative errors from (4) and this truncation are bounded by

C(a/h)[η+exp(−c h ε²)]=o(1).                                (6)

For the largest term, (a/h)aε³=O(a^(−1/5)(log a)^(11/5))→0. This explicitly absorbs the logarithmic cancellation loss.

It remains to bound every part of (1) outside the two squares centered at (s,x)=(±r,0). Bound (2) gives a global modulus envelope, apart from Cδ^(−5), with exponent

2n log|s|+9m−h e^(2(m−r))cosh(2l)−2aτ,
m=max(|s|,|x|),   l=min(|s|,|x|),   0≤l≤m.                  (7)

At s=0 the actual polynomial is zero; the logarithmic expression is understood by its limiting exponential. Replacing |s| by m only increases (7). Write F(m,l) for this larger exponent and d=m−r. Direct subtraction gives

F(m,l)−Φ_*
 =2n[log(m/r)−d/r]−h[e^(2d)−1−2d]
  −h e^(2d)[cosh(2l)−1].                                   (8)

The first term is nonpositive. The function ψ(d)=e^(2d)−1−2d is bounded below by c min(d²,|d|) for all real d: its quotient by d² tends to 2 at zero, its negative tail grows linearly, and its positive tail grows faster than linearly. Also cosh(2l)−1≥2l².

Consider first the part with |d|>ε. Integrating l over [0,m] and using (8) bounds its envelope integral by

 e^(Φ_*)∫_(m>0, |m−r|>ε) m e^(−hψ(m−r))dm
 ≤C e^(Φ_*)(r+1)e^(−c h ε²).                               (9)

For a detailed uniform bound, split the exponent in half: one half supplies e^(−c h ε²), and the integral of (r+|d|)exp(−(h/2)ψ(d)) over d>−r is O(r+1) for h≥1, by the quadratic bound on |d|≤1 and linear bound on |d|>1. If |d|≤ε but l>ε, then e^(2d) is bounded below and (8) gives the same exponential saving; the domain has area at most C(r+1)². These estimates include all sign choices of s,x, with only a fixed multiplicity factor.

The remaining envelope box has |m−r|≤ε, l≤ε. Where |s|=m, this is exactly the two local squares already considered. Where |s|=l, retain the factor dropped in passing to F:

(|s|/m)^(2n)=(l/m)^(2n)≤[ε/(r−ε)]^(2n)≤e^(−n)

for all sufficiently large a. Its area is O(ε²), and F≤Φ_* by (8). This controls the apparent competing envelope maximum near s=0, |x|=r. Combining the regions, the full complementary integral has modulus at most

Cδ^(−5)e^(Φ_*)[(r+1)²e^(−c h ε²)+e^(−n)].                  (10)

Relative to e^(Φ_*)/a this tends to zero, since hε²=h^(1/5), r=O(log a), δ^(−1)=O(log a), and n≥λ_0 a. Thus neither a nonlocal region nor the approach to the strip boundary spoils (6).

Finally the integrand in (1) is even in s: evenness of k swaps its two factors under s↦−s. Hence the negative-s square contributes exactly the same as the positive one. Equations (3)–(10) prove the asserted factor 4π/sqrt(det B). The original integral is real by t↦−t and conjugation. L267 gives D_n(Ξ;a)=2^(2n−1)I_n(a)/(2n)!, with a positive multiplier, proving eventual strict positivity. The dependence on a is even in the original cosine integral. ∎

The constants deteriorate as λ_0 tends to zero. In particular this proof does not cover all 1≤n≤K(a) from L266, where K(a)~π|a|/(2log 4); it covers any fixed proportional subinterval at large heights. No RH conclusion follows without the remaining indices and heights.

**Mathlib.** Full statement: not checked. Supporting holomorphic contour shifts, Gaussian Fourier integrals, theta series, and uniform asymptotic estimates: not checked. No library match is claimed. The elementary series estimates and both local and complementary-contour bounds are proved here; strip analyticity and the Laguerre integral identity are the previously established supporting results specified above.
