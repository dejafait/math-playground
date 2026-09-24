# Lemma 288: fixed-h stationary sum and its positive zeta factor

**Hypotheses.** Use the theta integral, shifted integrand F, and parameters r,h,τ,Φ_* of L269, and the exact summands and sector coordinates of L282. Fix 5<h₀≤h₁<∞. Let a→+∞ and n≥1 be integers with h₀≤h≤h₁. Thus

r=(1/2)log(a/(2π))+(1/4)log(1+h²/a²), n=r(h−9/2).

Set D={s+x>r/4, s−x>r/4}, C₀=(8π²)², and let I_D=∫_D F(s,x) ds dx, including the contour multiplier exp(−2aτ) in F. All little-o statements are uniform over this parameter range. Define ζ(z)=Σ_(m≥1)m^(−z) only for Re z>1 in this lemma.

**Conclusion.** The positive-positive sector has the asymptotic

I_D=C₀exp(Φ_*)[π/(2a)] (|ζ(h−4+ia)|²+o(1)).

Its leading coefficient satisfies

|ζ(h−4+ia)|²≥ζ(h₀−4)^(−2)>0.

In particular I_D is real and strictly positive for sufficiently large a. This does not evaluate the full-plane integral or prove new global Laguerre signs: the remaining sectors must still be controlled at o(exp(Φ_*)/a).

**Proof.** First recheck the estimates underlying L282 rather than invoke its logarithmic-h conclusion outside its hypotheses. Put σ₀=h₀−4>1, c=2√2, ε=1/100. For each pair j,k use

b=log(jk)/2, d=log(k/j)/2,
p=(s−r+b+x−d)/√2, q=(s−r+b−x+d)/√2.

Then s=r−b+(p+q)/√2, and D is the rectangle p>α_j, q>α_k, with α_m=(log m−3r/4)/√2. The normalized exact summand is

exp(ia log(k/j)) H_jk(p,q) exp(if(p)−if(q)),
f(y)=−(a/2)(exp(cy)−1−cy),
H_jk=G_jk E,
G_jk=(jk)^(−1/2)(s/r)^(2n)exp(9v−(h/2)(exp(cp)+exp(cq)−2)),
v=(p+q)/√2,
E=(1−3exp(−cp)/(2V_+))(1−3exp(−cq)/(2V_-)),
V_±=πexp(2r±2iτ), |V_±|=sqrt(a²+h²)/2.

The omitted constant is C₀exp(Φ_*); the absolute Jacobian is one. Throughout D, s>r/4 and log(s/r)≤(s−r)/r. Hence exactly as in L282,

0<G_jk≤w_jk g_h(p)g_h(q),
w_jk=(jk)^(4−h)≤(jk)^(−σ₀),
g_h(y)=exp(−(h/2)(exp(cy)−1−cy)).                 (1)

The suprema and integrals of (1+exp(cy))g_h(y) are bounded for h≥1. Also n/s≤4h and n/s²≤16h/r. Differentiation of G_jk therefore bounds its first and mixed derivatives by Cw_jk times the corresponding products of (1+exp(cy))g_h(y), with C depending only on h₀,h₁. On D, exp(−cp)/|V_+|≤exp(−r/2)/(πj²), and likewise for q,k, so E and its first and mixed derivatives are bounded. It follows that on every rectangle in D the rectangular variation of H_jk (corner value, two edge derivative integrals, and mixed-derivative area integral) is at most Cw_jk. These are precisely the differentiation and integrability calculations in L282; they require r≥1 and h≥1, not h≥log a.

Let C_jk be the exact summand integral over D∩{|p|,|q|≤ε} and K_jk its integral over the complement within D. The global phase primitives from L282 are O(a^(−1/2)), and are O(a^(−1)) on intervals outside [−ε,ε]. The rectangle integration identity thus gives

|C_jk|≤Cexp(Φ_*)w_jk/a,
|K_jk|≤Cexp(Φ_*)w_jk/a^(3/2).                  (2)

Clipped rectangles with empty interior contribute zero. Boundary limits and unbounded rectangles are allowed by (1) and absolute integrability. Since Σ_jk(jk)^(−σ₀)<∞, termwise integration on D is justified by the same absolute majorant, and the sum of K_jk is o(exp(Φ_*)/a). Thus it remains to evaluate the clipped sum, without discarding its higher indices.

For each fixed j,k, the full ε-square eventually lies in D uniformly in h. Its normalized amplitude can be factored as W_jk A_b E, where

W_jk=(jk)^(−1/2)(1−b/r)^(2n),
A_b=exp(2n log(1+v/(r−b))+9v−(h/2)(exp(cp)+exp(cq)−2)).

For fixed b, r→∞ and n/r remains in a fixed compact interval. On the fixed square, A_b and its derivatives through order two are bounded uniformly, and A_b(0,0)=1. Use the exact real phase substitution of L280,

Y=g(p), Z=g(q),
g(y)=sgn(y)sqrt((exp(cy)−1−cy)/4), g'(0)=1.

This is a smooth increasing diffeomorphism on the fixed interval: the quotient under the square root divided by y² is smooth and strictly positive there. Its inverse P and the needed derivatives are bounded. The transformed amplitude B=A_b(P(Y),P(Z))P'(Y)P'(Z) has bounded rectangular variation and B(0,0)=1. Its phase is −2aY²+2aZ². On the central square of radius R=a^(−2/5), B=1+O_jk(R), so replacing it by 1 costs O_jk(R³). On the remaining at most four rectangles, the Fresnel tail primitive is O(1/(aR)), the unrestricted primitive is O(a^(−1/2)), and the variation bound gives O_jk(a^(−3/2)/R). Extending the constant central Fresnel integral to the plane adds O(a^(−3/2)/R+a^(−2)/R²). The product of the two opposite Fresnel integrals is π/(2a). All these errors are o(1/a).

On this fixed square E−1 and its first and mixed derivatives are O(1/a). Its product with A_b has variation O_jk(1/a). Applying the two unrestricted phase primitive bounds shows that retaining E changes the signed integral by O_jk(1/a²), not merely by an absolute O(1/a) error. Consequently

C_jk=C₀exp(Φ_*) exp(ia log(k/j)) W_jk[π/(2a)+o_jk(1/a)].   (3)

Every error here is uniform in h₀≤h≤h₁. Expanding the real logarithm for this fixed b gives

log W_jk=−(1/2)log(jk)+2r(h−9/2)log(1−b/r)
         =(4−h)log(jk)+O_jk(1/r).

Thus W_jk=w_jk(1+O_jk(1/r)). The phase exp(ia log(k/j)) need not converge; it has modulus one and causes no problem for error estimates.

To sum (3) rigorously, normalize by C₀exp(Φ_*)π/(2a). Bound (2) dominates each normalized C_jk by C(jk)^(−σ₀), while the proposed leading term w_jk exp(ia log(k/j)) is dominated by (jk)^(−σ₀). For any tolerance, choose a finite index square so both tails are uniformly below that tolerance. On the finite square (3) and the weight expansion give an error tending uniformly to zero. This proves the summed little-o assertion despite the varying phases and clipped domains. Absolute convergence now factors the leading double sum:

Σ_jk(jk)^(−(h−4))exp(ia log(k/j))
 = (Σ_j j^(−(h−4)−ia))(Σ_k k^(−(h−4)+ia))
 = |ζ(h−4+ia)|².                                      (4)

For completeness, the required uniform lower bound uses only absolute convergence in Re z>1. For a finite set of primes up to P, geometric-series multiplication and unique prime factorization give

∏_(p≤P)(1−p^(−z))^(−1)=Σ_(m: all prime factors ≤P)m^(−z).

The right side converges to ζ(z) as P→∞ by domination by Σ m^(−Re z). For Re z=σ≥σ₀,

|∏_(p≤P)(1−p^(−z))^(−1)|
 ≥∏_(p≤P)(1+p^(−σ))^(−1)≥ζ(σ)^(−1)≥ζ(σ₀)^(−1).

The middle inequality follows by expanding the finite product ∏(1+p^(−σ)) as a sum over a subset of positive integers and bounding it by ζ(σ). Passing to the limit proves the stated bound without any zero-free assertion in the critical strip. Finally x↦−x preserves D and conjugates F, because the kernel is real on the real axis and its analytic extension respects conjugation. Thus I_D is real; (4) and the lower bound imply eventual strict positivity. ∎

The positive lower bound supplies the needed main coefficient, but the recorded whole-complement bound from L287 has relative size O(a^6 h^(−5)(r+1)²exp(−c h r)). At fixed h this need not tend to zero. Therefore (4) alone cannot extend the global sign range to every fixed h>5. The boundary h=5 is also excluded: the majorant loses absolute summability there. These are separate limitations, not failures of the sector asymptotic.

**Mathlib.** Full statement: not checked. Supporting theta series, Fresnel integrals, rectangle integration by parts, absolutely convergent series products, and Euler products: not checked. No full or supporting library match is claimed. L269 supplies the parameterwise contour identity and kernel conventions, L280 the translated summand algebra and exact phase change, and L282 the elementary variation and primitive calculations whose parameter ranges are explicitly rechecked above. The zeta factorization and lower bound are proved here within the absolutely convergent half-plane.
