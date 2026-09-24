# Lemma 323: growing stationary mass in the below-five boundary strips

**Hypotheses.** Retain L295's exact theta summands F_jk, positive same-sign strip S₊, and normalization, now at

h=39/8, H=h−9/2=3/8, r=8n/3, p=2n=3r/4,
2πexp(2r+2iτ)=h+ia, a>0, 0<τ<π/4,
Φ_*=p log r+9r−h−2aτ, C₀=(8π²)²,

with integer n→∞. Thus a~2πexp(2r). In coordinates u=s+x, v=s−x, the strip is

B={u,v≥0: min(u,v)≤r/4}, ds dx=(1/2)du dv.

Set J=exp(4r/5), let 𝒥_r be the integers J≤j≤2J, and define

W_j=j^(−1/2)(1−log j/(2r))^(3r/4),
λ=2/5+(3/4)log(3/5).

All these W_j are positive for sufficiently large r. Integrals use positive area measure.

**Conclusion.** There is a constant c>0 such that, for all sufficiently large admissible r,

Σ_(j,k≥1) |∫∫_(S₊) F_jk(s,x) ds dx|
 ≥ Σ_(j∈𝒥_r) |∫∫_(S₊) F_j1(s,x) ds dx|
 ≥ c exp(Φ_*) exp(λr)/a,                              (1)

where λ>1/60. The series of absolute integrals of the summands is finite for each parameter value. In fact, uniformly over j∈𝒥_r,

∫∫_(S₊) F_j1
 = C₀exp(Φ_*) exp(−ia log j) W_j π/(2a) · (1+o(1)).   (2)

Consequently the summed-modulus boundary bound o(exp(Φ_*)/a) in L301 cannot extend to this h with the same cutoff r/4. Equation (1) does not lower-bound the modulus of the sum over indices: their phases can cancel. No total boundary sign, Laguerre sign or off-line zero is asserted.

**Proof.** We use the exact algebra and local real phase change underlying L288 and L295, rechecking the estimates at this h. Their conclusions requiring h>5 are not applied here.

The exact normalized amplitude and separated phases in the positive quadrant are

A_jk(u,v)=exp(−9r+h)((u+v)/(2r))^p j⁴k⁴
 · exp(9(u+v)/2−(h/2)(j²exp(2(u−r))+k²exp(2(v−r))))
 · E_j(u) overline(E_k(v)),
E_j(u)=1−3/(2πj²exp(2u+2iτ)),
φ_j(u)=au−πsin(2τ)j²exp(2u),
F_jk=C₀exp(Φ_*) A_jk exp(iφ_j(u)−iφ_k(v)).           (3)

The contour multiplier exp(−2aτ) is included in Φ_*. The identity holds for every h>0 with the displayed saddle relations; it uses no summability in h.

First obtain bounds on the whole quadrant, including u+v=0. For ℓ=0,1,2 the polynomial P(w)=(w/(2r))^p satisfies

|P^(ℓ)(w)|≤C exp(H(w−2r))  (w≥0).                    (4)

For t=w/(2r)>0, its ratio to the right side without C is

(p)_ℓ/(2r)^ℓ · t^(p−ℓ)exp(−p(t−1)).

Its maximum is at t=1−ℓ/p, and is bounded uniformly because p/(2r)=H=3/8. For p>2 continuity gives (4) also at zero. Thus no singular division by w is needed for the mixed derivative. Set

y=u−r+log j, z=v−r+log k,
g_h(t)=exp(h t−(h/2)(exp(2t)−1)),
M_h(t)=(1+exp(2t))g_h(t).

The factors E_j and their first derivatives are bounded uniformly for u≥0, j≥1. Applying (4) and differentiating the other exponentials in (3) gives, for b,d∈{0,1},

|∂_u^b∂_v^d A_jk(u,v)|
 ≤ C(jk)^(4−h) M_h(y)M_h(z)
 = C(jk)^(−7/8) M_h(y)M_h(z).                        (5)

To check the normalization, replacing P by its tangent exponential gives exactly (jk)^(4−h)g_h(y)g_h(z); the derivative multipliers 9/2−h exp(2y), and its z counterpart, are absorbed by the two factors 1+exp(2t). This is a per-pair estimate, without an infinite power-sum comparison.

The supremum and integral of M_h on the whole line are finite. More precisely, with

B_h(Y)=sup_(t≥Y) M_h(t)+∫_Y^∞ M_h(t)dt,

one has B_h(Y)≤C for Y≤0 and B_h(Y)≤C exp(−exp(2Y)) for Y≥0. Indeed q=exp(2t) writes M_h as exp(h/2)(1+q)q^(h/2)exp(−hq/2), with dt=dq/(2q). Its integral at q=0 converges since h>0, and at q≥1 the polynomial factors are bounded by a constant times exp((h/2−1)q), giving the asserted tail and supremum bounds. Hence, for each fixed r,

Σ_j j^(−7/8) B_h(log j−r)<∞.                         (6)

The head j≤exp(r) is finite and the tail has Gaussian decay exp(−j²exp(−2r)). Equations (5)–(6) prove absolute integral summability of (3) on the full quadrant by Tonelli, and therefore on B. This also justifies termwise theta integration at each parameter. No limit in r is exchanged with that series.

We record the signed bounds needed for complements. Translation to y turns φ_j into a constant plus

f_a(y)=a(y−exp(2y)/2).

For every interval its oscillatory primitive has modulus at most C a^(−1/2). On intervals wholly in y≤−ε or y≥ε, for fixed ε>0, it is at most C_ε/a. To verify this, f'_a=a(1−exp(2y)) is monotone. Remove |y|≤a^(−1/2), whose length is O(a^(−1/2)); on each remaining side integration by parts gives reciprocal endpoint slopes and ∫|f''_a|/|f'_a|², the variation of 1/f'_a. The endpoint slopes are at least a fixed multiple of sqrt(a), or of a on the fixed tails. The same estimates hold for the negative phase.

For any rectangle in the positive quadrant, two integrations by parts, with primitives vanishing at its lower endpoints, bound the integral by the product of their suprema times

|A(u₁,v₁)|+∫_(u₀)^(u₁)|∂_u A(u,v₁)|du
 +∫_(v₀)^(v₁)|∂_v A(u₁,v)|dv+∫∫|∂_u∂_v A|.        (7)

By (5) this variation is at most C(jk)^(−7/8), uniformly in all endpoints, since M_h has bounded supremum and integral. All lower-edge terms vanish by the anchoring. Fixed-index amplitudes and their required derivatives decay superexponentially at the infinite upper endpoints, so limits of finite rectangles are valid, also by absolute integrability. Thus one tail coordinate in a rectangle supplies the bound C(jk)^(−7/8)a^(−3/2).

Now restrict to j∈𝒥_r, k=1. Their unique stationary point is

u_j=r−log j=r/5+O(1), v_1=r.

Choose ε=1/100. The translated square Q_j={|y|,|z|≤ε} is contained in 0<u<r/4, v>r/4 for all sufficiently large r, uniformly over these j. The complement B\Q_j is at most five rectangles with a tail coordinate: split [0,r/4]×[0,∞) outside Q_j into the two y tails and then the two z tails in |y|≤ε, and add [r/4,∞)×[0,r/4]. On the last rectangle z≤−3r/4. Empty pieces can be omitted. By (7), the normalized complementary integral therefore has modulus

|∫∫_(B\Q_j) A_j1 exp(iφ_j−iφ_1)du dv|
 ≤ Cj^(−7/8)a^(−3/2).                               (8)

This estimate treats the entire strip complement, so a local stationary contribution cannot be canceled by an uncontrolled part of the same summand.

On Q_j the exact amplitude factors as W_j D_j E, where

D_j(y,z)=exp(p log(1+(y+z)/(2r−log j))
 +(9/2)(y+z)−(h/2)(exp(2y)+exp(2z)−2)),
E=(1−3exp(−2y)/(2πexp(2r+2iτ)))
 · (1−3exp(−2z)/(2πexp(2r−2iτ))).                    (9)

Here D_j(0,0)=1. Since 2r−log j=6r/5+O(1), D_j and its derivatives through order two are uniformly bounded on the fixed square. This follows directly by differentiating its logarithm: p/(2r−log j+y+z) and p/(2r−log j+y+z)² are bounded, as are the fixed-square exponential terms. Also E−1 and its first and mixed derivatives are O(1/a). The phase equals

−a log j+f_a(y)−f_a(z).

For completeness use the exact real change

Y=g(y), Z=g(z),
g(t)=sgn(t)sqrt((exp(2t)−1−2t)/2), g'(0)=1.

It is a smooth increasing diffeomorphism on the fixed interval: the quotient of the radicand by t² is smooth and strictly positive there. Its inverse and the needed derivatives are bounded. The phase becomes −a log j−aY²+aZ². The transformed D_j including the Jacobian has bounded first and mixed derivatives and value one at the origin. Put R=a^(−2/5). Replacing this amplitude by one on |Y|,|Z|≤R costs O(R³). Its complement in the transformed fixed rectangle has at most four rectangular pieces; a Fresnel tail primitive is O(1/(aR)) and the unrestricted primitive is O(a^(−1/2)), giving O(a^(−3/2)/R) by (7). The product of the two opposite full Fresnel integrals is π/a. Extending the constant central integral to this product costs O(a^(−3/2)/R+a^(−2)/R²). Finally the transformed E−1 has variation O(1/a), so its signed integral costs O(a^(−2)). These estimates are uniform over 𝒥_r and give

∫∫_(Q_j) A_j1 exp(iφ_j−iφ_1)du dv
 =exp(−ia log j)W_j[π/a+O(a^(−11/10))].              (10)

Indeed R³ and a^(−2)/R² are a^(−6/5), while a^(−3/2)/R=a^(−11/10). This checks the stationary error for growing indices rather than using a fixed-index asymptotic.

We next compare the complementary error (8) with W_j/a. Uniformly on 𝒥_r,

W_j ≥ c exp(−2r/5)(3/5)^(3r/4).                      (11)

For example j≤2exp(4r/5) gives the factor 2^(−1/2)exp(−2r/5), and

1−log j/(2r)≥(3/5)(1−5log 2/(6r)).

The inequality log(1−x)≥−2x for 0≤x≤1/2 bounds the remaining power below by the constant 2^(−5/4). Therefore

j^(−7/8)/W_j ≤ Cexp(μr),
μ=−3/10−(3/4)log(3/5)=1/10−λ.                       (12)

A rational bound verifies the relevant exponents. Expanding 1/(1−t²) and integrating over 0≤t≤1/4 gives

log(5/3)=2Σ_(m≥0)(1/4)^(2m+1)/(2m+1)
 <1/2+(2/3)Σ_(m≥1)(1/4)^(2m+1)
 =1/2+1/90=23/45.

The strict inequality follows from the denominators for m≥2. Hence λ>2/5−(3/4)(23/45)=1/60, and μ<1/12. Since a~2πexp(2r), (8) divided by W_j/a is at most Cexp(−11r/12). Equations (8) and (10), and the Jacobian 1/2, now prove (2), with uniform relative error O(a^(−1/10)+exp(−11r/12)). In particular its modulus is at least C₀exp(Φ_*)πW_j/(4a) for large r.

Finally 𝒥_r contains at least exp(4r/5)/2 integers for large r. Summing (11) over them yields

Σ_(j∈𝒥_r)W_j≥c exp((2/5+(3/4)log(3/5))r)=c exp(λr).

This proves (1), with a finite total series by (6). The required normalized upper bound would tend to zero, whereas this normalized lower bound tends to infinity. The retained factors exp(−ia log j) have not been summed, so no inference about their combined sign or magnitude is valid. ∎

The obstruction lies in stationary indices inside the chosen boundary region. It does not apply to a smaller strip that excludes this family, or to a calculation retaining these indices in the arithmetic main sum. It leaves C294b's mixed-sector estimate, L301's h=5 result, and all established sign and exclusion ranges unchanged.

**Mathlib.** Full statement: not checked. Supporting Fresnel integrals, smooth real phase substitution, rectangular integration by parts, polynomial derivative bounds, and Tonelli/Fubini: not checked. No full or supporting library match is claimed. L295 supplies the exact summand, strip and normalization; L288 supplies the translated stationary-weight and real phase method, with the growing-index local estimate and all below-five bounds proved here. L301 is the estimate being tested, not an input outside its hypotheses.
