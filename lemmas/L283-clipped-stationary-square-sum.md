# Lemma 283: clipped stationary squares and the full patch sum

**Hypotheses.** Use the parameters, exact summands, sector D, squares Q_jk, and positive area measure of L282, with a→∞ and log a≤h≤2 log a. Set ε=1/100. Let C_jk be the integral of the exact shifted (j,k) summand over D∩Q_jk. Let P_a and J_jk be the restricted index set and full-square integrals of L281. Define J_11 by the same full-square integral for j=k=1.

**Conclusion.** Uniformly in this range,

Σ_(jk>1)|C_jk| ≤ C exp(Φ_*) h² 2^(−h)/a = o(exp(Φ_*)/a).

Moreover, the absolutely convergent clipped sum satisfies

|Σ_(j,k≥1) C_jk − (J_11+Σ_((j,k)∈P_a)J_jk)|
 ≤ C exp(Φ_*) h² exp(−(log 2−1/5)h)/a
 = o(exp(Φ_*)/a).

Thus centers outside P_a and squares crossing the boundary of D create no unresolved error at this scale. This is a statement about separately assigned summand patches, not integration of the full kernel over their union. It does not cover the other argument-sign sectors or extend the global Laguerre sign range.

**Proof.** In the coordinates of L282, D∩Q_jk is the rectangle

(max(−ε,α_j), ε) × (max(−ε,α_k), ε),
α_m=(log m−3r/4)/√2,

up to measure-zero boundaries; if either lower endpoint is at least ε, the integral is zero. This rectangular geometry is why no new boundary-curve estimate is required. All nonempty rectangles lie in D, including those whose center is outside D. In particular s>r/4 on them, so the bounds of L282 do not require the central value r−log(jk)/2 to be positive.

For clarity, the exact normalized integrand on this rectangle is H(p,q)exp(if(p)−if(q)), times (8π²)²exp(Φ_*)exp(ia log(k/j)). L282 proves, for every rectangle in D, that the sum of the corner value, two edge first-derivative integrals, and mixed-derivative area integral of H is at most Ch²w_jk, where w_jk=(jk)^(4−h). It also proves that the primitive of either exp(if) or exp(−if) on every real interval is bounded by C/√a. The rectangle integration identity used there therefore gives

|C_jk| ≤ C exp(Φ_*) h² w_jk/a.                         (1)

If an endpoint lies on the boundary of D, apply that result first to rectangles with endpoints in D and pass to the limit. The amplitude is continuous on the closure of this finite rectangle and has the same uniform derivative bounds there, since s≥r/4>0. Hence this limiting operation preserves (1). The exact lower-degree factors of both theta summands remain in H throughout; no absolute-error replacement is made.

For t=h−4≥2, integral comparison gives

q_t=Σ_(m≥2)m^(−t) ≤ 2^(−t)+2^(1−t)/(t−1) ≤3·2^(−t).

Thus Σ_(jk>1)w_jk=2q_t+q_t²≤C2^(−h), with an absolute constant absorbing the shift by four. Summing (1) proves the first assertion and absolute convergence. In fact only finitely many clipped squares are nonempty at each a, since nonemptiness requires m<exp(3r/4+√2ε) for each index. The estimate remains uniform as this finite set grows.

For j=k=1, both real kernel arguments on Q_11 are at least r−√2ε>r/4 for sufficiently large a. Therefore C_11=J_11 exactly. The triangle inequality now gives

|Σ_jk C_jk−J_11−Σ_(P_a)J_jk|
 ≤Σ_(jk>1)|C_jk|+Σ_(P_a)|J_jk|.

Apply the first assertion and L281's full-square sum bound to obtain the second assertion. This comparison does not presume that the clipped and full higher-index patches agree, nor that patches assigned to distinct summands are disjoint. Both sums are separately negligible, which suffices for their difference.

Finally the larger displayed error divided by exp(Φ_*)/a is bounded by C(log a)²a^(−(log 2−1/5)), tending to zero since log 2>1/5. This meets the required little-o threshold, rather than merely a bound at the main scale. ∎

Together with L282's absolute-series justification, the sector integral equals Σ_jk C_jk+Σ_jk K_jk. The latter sum is o(exp(Φ_*)/a), so replacing the sector integral by J_11+Σ_(P_a)J_jk is justified. Evaluation of the principal patch is supplied by the existing local saddle analysis; no control of a different sign sector is implicit in this identity. Smaller indices and bounded exterior heights required by L266 remain unresolved.

**Mathlib.** Full statement: not checked. Supporting rectangle integration, integration by parts, and positive-series bounds: not checked. No library match is claimed. L282 supplies the exact sector coordinates, the uniform mixed variation and primitive estimates, and termwise integration; L281 supplies the restricted full-patch sum estimate. The clipped-domain geometry and comparison are proved here.
