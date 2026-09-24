# Lemma 301: endpoint same-sign boundary curvature

**Hypotheses.** Use L295's exact normalized amplitude A_jk(u,v), phases φ_j, and same-sign strips S₊ and S₋, now at h=5 and integer n with 2n=r→∞. The saddle parameters obey 2πexp(2r)cos(2τ)=5 and 2πexp(2r)sin(2τ)=a, with a→∞. Thus r~(log a)/2. All integrals have positive area measure.

**Conclusion.** For c=1/256 and sufficiently large r,

Σ_(j,k≥1) |∫∫_(S₊) F_jk(s,x) ds dx|
 ≤ C exp(Φ_*) (1+r)² exp(−c r)/a
 = o(exp(Φ_*)/a).

The theta summands are absolutely integrable and integrally summable on the full positive same-sign quadrant for each such parameter value. The same signed estimate holds for S₋. This supplies the endpoint boundary-strip estimate, not an endpoint Laguerre sign.

**Proof.** Put w=u+v and P(w)=(w/(2r))^r. In L295's formula (1), set h=5 and p=r. That formula is exact at the endpoint; its derivation does not require h>5. Use

y=u−r+log j, z=v−r+log k,
g(t)=exp(5t−(5/2)(exp(2t)−1)), M(t)=(1+exp(2t))g(t).

We first control polynomial derivatives without singularities at w=0. For ℓ=0,1,2, for r sufficiently large, the tangent bound is

|P^(ℓ)(w)|≤C exp(w/2−r)  (w≥0).                         (1)

This is L295's elementary maximization with H=1/2, which remains valid here. In addition,

|P^(ℓ)(w)|≤C exp(−c r) exp(w/2−r)  (0≤w≤7r/4).         (2)

To check (2), put t=w/(2r). For t>0 the ratio of the left side to exp(w/2−r) is

(r)_ℓ/(2r)^ℓ · t^(r−ℓ) exp(−r(t−1)).

On 0<t≤7/8 its logarithmic derivative is (r−ℓ)/t−r>0 for sufficiently large r. Its maximum is therefore at t=7/8, bounded by C exp(−d r), where d=−log(7/8)−1/8. The series or integral inequality −log(1−x)−x≥x²/2 gives d≥1/128>c. At zero all these polynomial derivatives vanish for integer r>2; continuity completes the proof. The prefactors (r)_ℓ/(2r)^ℓ and (7/8)^(−ℓ) are bounded independently of r.

The exact factors E_j(u)=1−3/(2πj²exp(2u+2iτ)) and their first derivatives are uniformly bounded for u≥0, j≥1. Differentiation of the other exponential factor gives 9/2−5exp(2y), and similarly for z. Applying (1) and the product rule to L295's amplitude yields, for b,d∈{0,1},

|∂_u^b ∂_v^d A_jk|≤C(jk)^(−1) M(y)M(z).               (3)

On any rectangle with w≤7r/4, applying (2) instead gives

|∂_u^b ∂_v^d A_jk|≤C exp(−c r)(jk)^(−1)M(y)M(z).       (4)

The mixed derivative uses at most P''; no division by w or by E_j is made. Algebraically, the tangent exponential combined with the remaining factors is exactly (jk)^(−1)g(y)g(z), as in L295's calculation with h=5. Thus no extra r-dependent normalization is hidden in (3) or (4).

For a real Y define

B(Y)=sup_(t≥Y) M(t)+∫_Y^∞ M(t)dt.

The substitution q=exp(2t) gives

M(t)=exp(5/2)(1+q)q^(5/2)exp(−5q/2), dt=dq/(2q).

It proves B(Y)≤C for Y≤0 and B(Y)≤C exp(−exp(2Y)) for Y≥0: the relevant polynomial factors are bounded by C exp(3q/2) for q≥1. Both the supremum and tail integral then have the stated bound. With B_j=B(−r+log j), harmonic comparison up to exp(r) and the decreasing integral comparison beyond exp(r) give

Σ_(j≥1) B_j/j ≤ C(1+r).                               (5)

Indeed beyond that cut the tail is bounded by a constant times Σ j^(−1)exp(−(j/exp(r))²), whose corresponding integral is bounded after scaling. Equation (3) with b=d=0 now proves

Σ_jk ∫₀^∞∫₀^∞ |A_jk| du dv ≤ C(1+r)².                (6)

This proves absolute integral summability and justifies the exact theta-series interchange for each parameter value. No uniform-in-r summability assertion is needed.

We use the uniform phase primitive estimate from L295,

sup_J |∫_J exp(±iφ_j(u))du|≤C a^(−1/2),               (7)

valid for every interval J and every j. It also follows from L300's elementary derivative argument after rescaling coordinates. In particular, it includes stationary points in the strips. For a rectangle [u₀,u₁]×[v₀,v₁], choose the primitives to vanish at its lower endpoints. Two integrations by parts bound the oscillatory integral by C/a times

|A_jk(u₁,v₁)|+∫_(u₀)^(u₁)|∂_u A_jk(u,v₁)|du
 +∫_(v₀)^(v₁)|∂_v A_jk(u₁,v)|dv
 +∫_(u₀)^(u₁)∫_(v₀)^(v₁)|∂_u∂_v A_jk|dv du.         (8)

Thus (3) bounds this variation by C(jk)^(−1)B(u₀−r+log j)B(v₀−r+log k). On rectangles contained in w≤7r/4, (4) gives the additional factor exp(−c r). This argument accounts for the upper corner and both upper edges; lower-edge terms vanish by construction. For unbounded rectangles use finite truncations and (6) to pass to the limit.

Set L=r/4 and V=3r/2. Partition [0,L]×[0,∞) into R_low=[0,L]×[0,V] and R_high=[0,L]×[V,∞). On R_low one has w≤7r/4, so (4), (5), (7), and (8) give the summed bound

Σ_jk |∫_(R_low) A_jk exp(iφ_j−iφ_k)|
 ≤ C a^(−1) exp(−c r)(1+r)².                         (9)

For R_high retain its lower v endpoint in B. It is r/2+log k in the translated coordinate, whence

Σ_(k≥1) k^(−1)B(r/2+log k)
 ≤ C Σ_(k≥1) k^(−1)exp(−exp(r)k²)
 ≤ C exp(−exp(r)/2).                                 (10)

The last inequality follows by writing exp(−T k²)≤exp(−T/2)exp(−k²/2) for T≥1. Equations (3), (5), (7), and (8) bound the summed high-rectangle integrals by C a^(−1)(1+r)exp(−exp(r)/2), smaller than (9).

Transpose the rectangles to control [0,∞)×[0,L]. Their intersection [0,L]² also obeys (9), since w≤r/2. Inclusion-exclusion and the triangle inequality therefore prove the same bound (9) for min(u,v)≤L, with a larger constant. Restore the fixed factor C₀exp(Φ_*) and Jacobian 1/2 from L295. Reflection s↦−s preserves the full integrand, as checked there, and maps S₊ to S₋. This proves both claims. Finally (1+r)²exp(−c r)→0, which is the required normalized threshold. ∎

Together with L300 this controls the omitted pieces of the same-sign quadrants at h=5. A quantitative positive lower bound for the endpoint phase sum and endpoint mixed-sector estimates are still missing. Even these would not address all smaller indices or bounded exterior heights. The result uses the admissible subsequence 2n=r and claims no uniform neighborhood of h=5.

**Mathlib.** Full statement: not checked. Supporting polynomial derivative estimates, exponential tail integration, harmonic-sum comparison, rectangular integration by parts, and Tonelli/Fubini: not checked. No library match is claimed. L295 supplies the exact amplitude, normalization, reflection and primitive bound; L300's moving-domain variation mechanism is used with the lower limits retained. The curvature saving, split-strip estimate and endpoint summation are proved here.
