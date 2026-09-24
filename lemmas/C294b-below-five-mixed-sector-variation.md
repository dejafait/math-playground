# Corollary 294b: mixed-sector variation below five

**Hypotheses.** Use the even theta kernel and exact mixed-sector summands T_jk from L292, and the normalization from L294, now with integer n≥1 and

39/8≤h≤5, H=h−9/2=n/r, p=2n=2Hr,
2πexp(2r+2iτ)=h+ia, a>0, 0<τ<π/4,
Φ_*=p log r+9r−h−2aτ, C₀=(8π²)².

Let a tend to infinity over these admissible parameters. Then r~(log a)/2 and p→∞. On the mixed sector x>|s| use u=x+s>0, v=x−s>0 and the positive coordinate Jacobian 1/2. All constants and limits below are uniform over this h-band and the admissible integers n.

**Conclusion.** Put γ₀=(3/4)log 2−1/2>1/54. The whole mixed sector satisfies

(1/2) Σ_(j,k≥1) |∫₀^∞∫₀^∞ T_jk(u,v) du dv|
 ≤ C exp(Φ_*) exp(−γ₀r)/a
 = o(exp(Φ_*)/a).

For each parameter value the exact theta series is absolutely integrable termwise over this sector. The opposite mixed sector has the same signed bound. In particular the estimate holds at h=39/8, where r=8n/3 and n/log a→3/16. This supplies no same-sign sector estimate, no core-subtraction assertion, and no Laguerre sign.

**Proof.** L292's summand identity uses evenness of the kernel, positive real arguments, and cos(2τ)>0, without a lower bound h>5. We recheck the whole-sector variation calculation in this smaller band, rather than invoking L294 or C294a outside their hypotheses. Define

q(u)=(h/2)exp(2(u−r)),
E_j(u)=1−3/(2πj²exp(2u+2iτ)),
B_j(u)=j⁴exp(9u/2−q(u)j²)E_j(u),
φ_j(u)=au−πsin(2τ)j²exp(2u),
Ā_jk(u,v)=exp(−9r+h)((u−v)/(2r))^p B_j(u)B_k(v).

The exact identity is

T_jk=C₀exp(Φ_*)exp(9iτ)Ā_jk exp(iφ_j(u)+iφ_k(v)).       (1)

Indeed multiplication by exp(Φ_*) restores exp(−2aτ)((u−v)/2)^p, and the two kernel factors each have argument with imaginary part +τ. The double series converges absolutely pointwise for each fixed parameter, including on u=0 or v=0, since cos(2τ)>0 gives Gaussian decay in each index.

For u≥0 and j≥1, E_j and E'_j are bounded by constants independent of the parameters. Differentiation of the real exponential in B_j multiplies it by 9/2−2q(u)j². Hence

|B_j(u)|+|B'_j(u)|
 ≤ C j⁴exp(9u/2)(1+q(u)j²)exp(−q(u)j²).              (2)

The elementary Gaussian-moment estimate used in L294 is

Σ_(j≥1) j⁴(1+qj²)exp(−qj²)
 ≤ C q^(−5/2)exp(−q/2)  (q>0).                        (3)

To check its constant does not depend on h, when q≤1 compare the fourth- and sixth-moment sums with their integrals and maxima after scaling by sqrt(q). They are O(q^(−5/2)) and O(q^(−7/2)), respectively. The additional factor q for the latter gives the same bound, and exp(−q/2) is bounded below. When q≥1, factor out exp(−q); the remaining sum is at most C(1+q), by comparison with the convergent polynomially weighted Gaussian sum at q=1. Finally (1+q)exp(−q)≤Cq^(−5/2)exp(−q/2). Thus (3) holds for all q with an absolute constant.

Take c=39/32 and set

W(u)=exp(−u/2)exp(−c exp(2(u−r))).

Since h/4≥c, (2)–(3) give

Σ_j (|B_j(u)|+|B'_j(u)|)≤Cexp(5r)W(u).               (4)

The polynomial and its first two derivatives obey

|[d/dw]^ℓ (w/(2r))^p|
 ≤ C2^(−p)exp(−p)exp(2H|w|), ℓ=0,1,2.               (5)

For w≠0 put t=|w|/r. Dividing the derivative's modulus by the right side without C gives

(p)_ℓ/r^ℓ · t^(p−ℓ)exp(p−pt).

Its maximum is at t=1−ℓ/p for p>ℓ; the maximal value is at most (p/r)^ℓ exp(ℓ)≤exp(ℓ), since 3/4≤p/r≤1. This also proves the ℓ=0 case. Continuity handles w=0, so no division by u−v is required when applying (5).

By the product rule, (4)–(5), for b,d∈{0,1},

Σ_jk |∂_u^b∂_v^d Ā_jk(u,v)|
 ≤ Cexp(r)2^(−p)exp(−p)exp(2H|u−v|)W(u)W(v).        (6)

The factor exp(h) is bounded on the stated band. We integrate (6) using exp(2H|u−v|)≤exp(2Hu−2Hv)+exp(−2Hu+2Hv). The positive-tail exponent is

b₊=2H−1/2∈[1/4,1/2].

Consequently

∫₀^∞ exp(2Hu)W(u)du
 =exp(b₊r)∫_(−r)^∞ exp(b₊t−c exp(2t))dt
 ≤ Cexp(b₊r),
∫₀^∞ exp(−2Hu)W(u)du≤1/(2H+1/2)≤4/5.              (7)

The first t-integral is uniformly bounded: on t≤0 its integrand is at most exp(t/4), and on t≥0 it is at most exp(t/2−c exp(2t)). Both majorants are integrable. Since p=2Hr, Tonelli and (6)–(7) yield

Σ_jk ∫₀^∞∫₀^∞ |∂_u^b∂_v^d Ā_jk| du dv
 ≤ Cexp((1/2−2H log 2)r)
 ≤ Cexp(−γ₀r).                                       (8)

This is the needed index-summability estimate. For b=d=0, (1) and (8) justify absolute termwise integration at each parameter. No interchange of an a-limit with the theta series is used.

It remains to obtain the factor 1/a and account for boundaries. Translation y=u−r+log j changes φ_j, up to a real constant, into

f(y)=a(y−exp(2y)/2),

by 2πexp(2r)sin(2τ)=a. Uniformly over every finite real interval J,

|∫_J exp(if(y))dy|≤C/sqrt(a).                          (9)

The intersection with |y|≤a^(−1/2) has length at most 2a^(−1/2). On each remaining side f'=a(1−exp(2y)) is monotone and has magnitude at least a fixed positive multiple of sqrt(a), for a≥1. Integration by parts bounds the integral by reciprocal endpoint slopes plus ∫|f''|/|f'|²; the latter is the variation of 1/f' and has the same bound. This proves (9) uniformly in the translated endpoints and in j, including stationary points near u=0.

Let U_j(u)=∫₀^u exp(iφ_j(t))dt. Then U_j(0)=0 and |U_j|≤C/sqrt(a). For fixed j,k, two integrations by parts on finite rectangles, followed by their limit to the quadrant, give

∫∫ Ā_jk exp(iφ_j+iφ_k)
 =∫∫ (∂_u∂_v Ā_jk)U_j(u)U_k(v).                     (10)

All lower-edge terms vanish because the primitives are zero there. For the upper edges and corner, at each fixed parameter and pair of indices the amplitude and its first derivatives are bounded by a constant times

(1+u)^p(1+v)^p(1+exp(2u))(1+exp(2v))
 · exp(9(u+v)/2−q(u)j²−q(v)k²).

This is a product of integrable one-variable factors, each tending superexponentially to zero at positive infinity. Thus even the integrals along the upper edges vanish as their endpoints tend to infinity. The derivative integral in (10) converges absolutely by (8) and the bounded primitives. This verifies every boundary term before summation.

Taking moduli in (10), summing (8) with b=d=1, and restoring (1) and the Jacobian 1/2 proves the claimed Cexp(Φ_*−γ₀r)/a bound. Reflection x↦−x conjugates the shifted integrand, since the kernel is real on the real axis and the polynomial s^p is real. It maps x>|s| to x<−|s| with positive area preserved, proving the opposite-sector bound as well.

Finally a rational lower bound establishes the strict decay without numerical evidence:

log 2=2∫₀^(1/3) dt/(1−t²)
 >2∫₀^(1/3)(1+t²)dt=56/81,
γ₀>(3/4)(56/81)−1/2=1/54.

Thus exp(−γ₀r) tends to zero uniformly, strictly meeting the required little-o threshold. At h=39/8 the identities give r=8n/3 and a=sqrt(4π²exp(4r)−(39/8)²), so n/log a→3/16. ∎

The window reaches below the coefficient 1/4 in L296's positive logarithmic bands only for the mixed-sector input. The same-sign regions and their arithmetic leading coefficient remain uncontrolled here. In particular no conclusion about actual Laguerre signs, zero exclusion, or RH follows from this estimate alone. L293's core estimate is not invoked outside its stated range.

**Mathlib.** Full statement: not checked. Supporting Gaussian moment sums, polynomial derivative estimates, Tonelli/Fubini and integration by parts: not checked. No full or supporting library match is claimed. The exact summand algebra comes from L292; L294 supplies the normalized variation and bounded-primitive method, with every estimate used below five checked above.
