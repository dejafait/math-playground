# Lemma 324: summed variation on a smaller below-five boundary strip

**Hypotheses.** Use the exact theta summands and normalization of L323, with

h=39/8, H=3/8, r=8n/3, p=2n=3r/4,
2πexp(2r+2iτ)=h+ia, a>0, 0<τ<π/4,
Φ_*=p log r+9r−h−2aτ, C₀=(8π²)²,

and integer n tending to infinity. Thus a~2πexp(2r). In the positive same-sign quadrant set u=s+x, v=s−x and

B={u,v≥0: min(u,v)≤r/20}.

Write S₊ for this region in (s,x) coordinates, with positive area measure ds dx=(1/2)du dv, and S₋ for its reflection under s↦−s.

**Conclusion.** For sufficiently large admissible r,

Σ_(j,k≥1) |∫∫_(S₊) F_jk(s,x) ds dx|
 ≤ C exp(Φ_*) (1+r)² exp(−r/200)/a
 = o(exp(Φ_*)/a).                                      (1)

The exact theta summands are absolutely integrable and integrally summable on the full positive quadrant for every such parameter value. In particular the full integrals over S₊ and S₋ satisfy (1). This estimates only the smaller boundary strips. The same-sign interior and its arithmetic sign remain unestimated here; no Laguerre sign follows.

**Proof.** The exact formulas in L323 are

F_jk=C₀exp(Φ_*) A_jk(u,v) exp(iφ_j(u)−iφ_k(v)),
φ_j(u)=au−πsin(2τ)j²exp(2u),
A_jk=exp(−9r+h)P(u+v) B_j(u) overline(B_k(v)),
P(w)=(w/(2r))^p,
B_j(u)=j⁴exp(9u/2−(h/2)j²exp(2(u−r)))E_j(u),
E_j(u)=1−3/(2πj²exp(2u+2iτ)).                         (2)

The factors E_j and E'_j are uniformly bounded for u≥0 and j≥1. Differentiating B_j introduces the further factor 9/2−hj²exp(2(u−r)). Therefore, for b=0,1 and t=exp(2(u−r)),

|B_j^(b)(u)|≤C exp(9u/2) j⁴(1+tj²)exp(−htj²/2).       (3)

We sum this bound before estimating the polynomial. For m=4,6 and any fixed c>0, the elementary Gaussian sum bound is

Σ_(j≥1) j^m exp(−ctj²)≤C_(m,c)t^(−(m+1)/2), t>0.     (4)

Here are details valid throughout its range. For 0<t≤1, the function x^m exp(−ctx²) is unimodal, so its integer sum is bounded by its integral over [0,∞) plus twice its supremum. Substitution x=y/sqrt(t) bounds these terms by C t^(−(m+1)/2) and C t^(−m/2), respectively; the second is no larger than the required order. For t≥1 and j≥1, tj²≥(t+j²)/2, giving a bound C exp(−ct/2) after summing j^m exp(−cj²/2). This is at most C t^(−(m+1)/2). Thus (4) has constants independent of t.

Set d=h/4=39/32. Splitting the exponent in (3), and using j²≥1 in one half, gives

Σ_(j≥1) j⁴(1+tj²)exp(−htj²/2)
 ≤ exp(−dt) Σ_(j≥1)(j⁴+tj⁶)exp(−dtj²)
 ≤ C t^(−5/2)exp(−dt).                                (5)

Consequently, for b=0,1,

Σ_j |B_j^(b)(u)|
 ≤ C exp(5r−u/2) exp(−d exp(2(u−r))).                  (6)

The factor exp(5r−u/2) includes exp(9u/2) from (3). For w=u+v, the product rule in (2) and (6) now prove, for b,e∈{0,1},

Σ_jk |∂_u^b∂_v^e A_jk(u,v)|
 ≤ C exp(r−w/2) [Σ_(ℓ=0)^2 |P^(ℓ)(w)|]
    ·exp(−d[exp(2(u−r))+exp(2(v−r))]).                 (7)

Only polynomial derivatives through order two occur. The factor exp(h) in (2) is fixed and absorbed into C. All estimates in (7) concern sums of absolute values of individual derivatives; no differentiation of a conditionally convergent series is involved.

We need two polynomial estimates. First, as in L323's tangent estimate,

|P^(ℓ)(w)|≤C exp(H(w−2r)), w≥0, ℓ=0,1,2.              (8)

Indeed at t=w/(2r)>0 the ratio to this exponential is

(p)_ℓ/(2r)^ℓ · t^(p−ℓ)exp(−p(t−1)).

For ℓ≤2 its maximum occurs at t=1−ℓ/p and is uniformly bounded because p/(2r)=H. For p>2 the value at w=0 follows by continuity, without division by w. Combining (7) and (8) gives the global bound

Σ_jk |∂_u^b∂_v^e A_jk|
 ≤ C exp(r/4)exp(−(u+v)/8)
    ·exp(−d[exp(2(u−r))+exp(2(v−r))]).                 (9)

In particular Σ_jk∫₀^∞∫₀^∞|A_jk|du dv≤C exp(r/4)<∞. Tonelli and absolute Fubini justify the exact theta-series integration on the quadrant and all its subregions for each parameter. No uniform bound as r tends to infinity is claimed in this absolute-integrability assertion.

The sharper estimate needed on the small rectangle is

exp(r−w/2)|P^(ℓ)(w)|≤C exp(−r/200),
0≤w≤53r/50, ℓ=0,1,2.                                 (10)

To prove it, put again t=w/(2r). Apart from the bounded factor (p)_ℓ/(2r)^ℓ, the expression is t^(p−ℓ)exp(r(1−t)). For 0<t≤53/100 its logarithmic derivative is (p−ℓ)/t−r>0 once (11/50)r>2. Its maximum is therefore at 53/100 and is bounded by

C exp(r[47/100+(3/4)log(53/100)]).

For an exact rate comparison set q=47/153. Integrating the geometric series for 1/(1−q²) gives

log(100/53)=2Σ_(m≥0)q^(2m+1)/(2m+1)
 >2(q+q³/3)>19/30.

The second strict inequality has rational difference 39877/107447310. Hence 47/100+(3/4)log(53/100)<47/100−(3/4)(19/30)=−1/200. At w=0 the required derivatives vanish for p>2. This proves (10), including all polynomial derivative orders actually used in (7).

We now retain the oscillation and all boundaries. The elementary primitive estimate in L323 gives, for either sign and every interval J,

|∫_J exp(±iφ_j(u))du|≤C a^(−1/2),                    (11)

uniformly in j and the endpoints. It follows by translating y=u−r+log j to the phase a(y−exp(2y)/2), removing |y|≤a^(−1/2), and integrating by parts on the two remaining monotone-slope intervals. Their reciprocal endpoint slopes and the variation of the reciprocal slope are O(a^(−1/2)). This estimate permits stationary points in the boundary strip.

For any finite rectangle R=[u₀,u₁]×[v₀,v₁] in the quadrant, anchor the two primitives at its lower endpoints. Two integrations by parts bound the normalized signed integral by C/a times

V_jk(R)=|A_jk(u₁,v₁)|
 +∫_(u₀)^(u₁)|∂_u A_jk(u,v₁)|du
 +∫_(v₀)^(v₁)|∂_v A_jk(u₁,v)|dv
 +∫_R|∂_u∂_v A_jk|du dv.                             (12)

Both upper edges and the upper corner are displayed. The lower terms vanish because of the anchored primitives. Infinite endpoints will follow from finite truncation and the already proved absolute integrability.

Set L=r/20 and V=101r/100. On R_low=[0,L]×[0,V], one has u+v≤53r/50. Equations (7) and (10), with the Gaussian factor bounded by one, give

Σ_jk V_jk(R_low)≤C(1+L)(1+V)exp(−r/200)
                  ≤C(1+r)²exp(−r/200).                (13)

The same bound holds on [0,L]² and on the transposed low rectangle. This sums the mixed derivative over the area and the first derivatives along their edges; no supremum is moved outside an infinite index sum.

On R_high=[0,L]×[V,∞), retain the second Gaussian factor in (9). For v≥V it satisfies

exp(−d exp(2(v−r)))≤exp(−d exp(r/50)).

For each finite truncation [0,L]×[V,T], (9) thus bounds every term in the sum of (12) by the corresponding corner, edge or area evaluation of

C exp(r/4)exp(−d exp(r/50))exp(−(u+v)/8).

Its one-dimensional integrals over any subinterval of [0,∞) are at most 8, and its corner values are at most 1 after removing the common factor. It follows that

Σ_jk V_jk([0,L]×[V,T])
 ≤C exp(r/4)exp(−d exp(r/50)),                         (14)

uniformly in T. This is O(exp(−r/200)) as r→∞. Passage to T=∞ in the signed integrals is valid by parameterwise absolute integration; the sum of their moduli obeys the same bound by Fatou, or by domination by the absolute summand integrals. The transposed high rectangle obeys the identical estimate. Thus moving stationary indices, infinite endpoints and all boundary terms have been covered.

Finally B is the union of [0,L]×[0,∞) and [0,∞)×[0,L], with intersection [0,L]². Split each infinite rectangle at V, apply (11)–(14), and use inclusion-exclusion and the triangle inequality separately for each pair j,k. This proves

Σ_jk |∫_B A_jk exp(iφ_j−iφ_k)du dv|
 ≤C(1+r)²exp(−r/200)/a.

Restoring C₀exp(Φ_*) and the Jacobian 1/2 proves (1). L295's reflection identity F(−s,x)=F(s,x) uses only evenness of the theta kernel and p=2n, so it remains valid at these parameters and transfers the full integral bound to S₋. Since (1+r)²exp(−r/200)→0, the achieved error meets the required little-o threshold. ∎

L323's stationary family lies near u=r/5, v=r and is outside this smaller strip. It must be included in the retained interior instead of being assigned to this error. Neither its combined arithmetic sign nor that of the entire interior is inferred from (1). The global low-index signs and established zero-exclusion ranges are unchanged.

**Mathlib.** Full statement: not checked. Supporting Gaussian lattice-sum bounds, polynomial derivative estimates, geometric-series integration, rectangular integration by parts, and Tonelli/Fubini: not checked. No full or supporting library match is claimed. L323 supplies the exact below-five summands, normalization and primitive estimate; L295 supplies the reflection identity. The pointwise Gaussian index summation, derivative saving and smaller-strip bound are proved here. L301's endpoint result and L323's larger-strip obstruction are retained with their original qualifications.
