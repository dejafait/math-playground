# Lemma 285: global Laguerre positivity in the logarithmic-h band

**Hypotheses.** Use the actual theta kernel k, integral I_n(a), saddle parameters r,h,τ, phase Φ_*, and matrix B of L269. Let a→+∞ and let n≥1 be an integer satisfying log a≤h≤2 log a. All asymptotic assertions are uniform in this band.

**Conclusion.** With the positive square root,

I_n(a)=(8π²)² exp(Φ_*) [π/a+o(1/a)]
       =(8π²)² exp(Φ_*) 4π/√(det B) · (1+o(1)).

Consequently D_n(Ξ;a)>0 throughout this band for sufficiently large a, and likewise with a replaced by |a|. Its index endpoints are (1/2+o(1))(log a)² and (1+o(1))(log a)². This is a band assertion, not positivity at every larger or smaller index.

**Proof.** Put L=log a and C₀=(8π²)². The parameterwise shifted-contour identity proved in L269 applies here: its proof only requires a fixed τ<π/4 and the strip decay, not proportional indices. Denote its integrand, including exp(−2aτ), by

F(s,x)=exp(−2aτ)s^(2n)k(s+x+iτ)k(s−x−iτ)exp(2iax).

For each a,n it is absolutely integrable. We have r~L/2, n=r(h−9/2), and δ=cos(2τ)=h/√(a²+h²).

First evaluate the principal exact-summand patch. Let Q=Q_11 be the square |p|,|q|≤ε=1/100 of L278 and L282, and let J_11 be the integral over Q with k in each factor replaced by the exact first theta summand T_1. Let J be the actual-kernel patch integral of L278. The model is k_0(z)=8π²exp(9z/2−πexp(2z)), and

T_1(z)/k_0(z)=1−3/(2V),  V=πexp(2z).

On Q, |V| is comparable to a and Re V≥(h/2)exp(−2√2ε). The theta-series bound in L278 gives k/k_0=1+O(a^(−1))+O(exp(−γh)), where γ=(3/2)exp(−2√2ε)>1. Hence the difference between the products of the two actual factors and of the two T_1 factors is at most C[a^(−1)+exp(−γh)] times the modulus of the model product. L278's real-amplitude estimate bounds the integral of the latter, including the polynomial and contour-shift factors, by C exp(Φ_*)/h. Therefore

|J−J_11|≤C exp(Φ_*)[a^(−1)+exp(−γh)]/h
         =o(exp(Φ_*)/a).

Indeed its relative bound is O(1/h+a exp(−γh)/h), which tends to zero uniformly since h≥L and γ>1. L278 now implies

J_11=C₀ exp(Φ_*)[π/(2a)+o(1/a)].                       (1)

This explicitly distinguishes the actual-kernel patch from the first-summand patch. All integrals here use positive area measure; the p,q coordinate map has absolute Jacobian one, so introduces no minus sign.

Let D={s+x>r/4, s−x>r/4}. By L282, absolute summability permits termwise integration on D, with each summand partitioned into its own clipped stationary square and complement. In its notation and that of L283,

∫∫_D F=Σ_(j,k≥1)C_jk+Σ_(j,k≥1)K_jk.

There is no partition by the union of overlapping summand patches. L283 gives C_11=J_11 and Σ_(jk>1)|C_jk|≤C exp(Φ_*)h²2^(−h)/a. L282 gives Σ|K_jk|≤C exp(Φ_*)h²/a^(3/2). Thus

∫∫_D F=J_11+o(exp(Φ_*)/a),                            (2)

since h²2^(−h)≤4L²a^(−log 2)→0 and h²/√a≤4L²/√a→0. This uses the first conclusion of L283 directly; its comparison with restricted full squares is unnecessary for this assembly.

To check the whole-plane partition, put

E={min(|s+x|,|s−x|)≤r/4},
D_-={s+x<−r/4, s−x<−r/4},
M={(s+x)(s−x)<0}.

Up to null boundaries, the four disjoint regions E, D, D_-, and M\E exhaust ℝ²: outside E each of the two real kernel arguments has magnitude greater than r/4, so their signs give exactly the last three possibilities. L279 bounds the integral of |F| over E, and L284 bounds it over M and therefore over M\E. Each bound is at most Cδ^(−5)(r+1)²exp(Φ_*−c h r). Dividing by exp(Φ_*)/a gives logarithm at most −cL²/3+6L+O(log L), tending to −∞. No region is omitted or counted twice.

Finally evenness of the analytic kernel gives

k(−s+x+iτ)=k(s−x−iτ),
k(−s−x−iτ)=k(s+x+iτ).

Since (−s)^(2n)=s^(2n), F(−s,x)=F(s,x) exactly. Reflection (s,x)↦(−s,x) maps D to D_- with unit absolute Jacobian and leaves exp(2iax) unchanged. Their integrals are equal, not merely conjugate. Combining this identity, the partition bounds, (1), and (2) gives I_n(a)=2J_11+o(exp(Φ_*)/a), proving the first asymptotic with its stated factor.

The determinant identity from L269 is det B=16(a²+h²)+8hn/r². Here h=O(L) and n/r²=O(h/r), so det B=16a²(1+o(1)). Hence 4π/√(det B)=π/a·(1+o(1)), proving the second form. The original integral is real by conjugation and t↦−t; its positive leading term dominates the uniform error. The exact identity D_n(Ξ;a)=2^(2n−1)I_n(a)/(2n)! in L269 has a positive multiplier, giving the claimed sign and evenness in a.

For the band interpretation, the parameter relation is

r(h)=(1/2)log(a/(2π))+(1/4)log(1+h²/a²),
n(h)=r(h)(h−9/2).

For large a and L≤h≤2L, r>0, r'(h)>0, and h>9/2, so n(h) is strictly increasing. Evaluating its endpoints gives the two stated asymptotic index endpoints; admissible integers are those between the exact endpoints, rounded inward. ∎

This closes a global sign band far below the earlier square-root threshold. It does not interpolate between the bands. In particular L266 still requires all indices through a cutoff asymptotic to π|a|/(2log 4); this lemma leaves indices below the new band, the gap above it before the existing high-index range, and bounded exterior heights unresolved. No RH candidate follows.

**Mathlib.** Full statement: not checked. Supporting contour shifts, even-function changes of variables, absolutely summable integration, and asymptotic sign transfer: not checked. No library match is claimed. L269 supplies the contour identity, determinant, and Laguerre normalization; L278 supplies the local asymptotic and model bounds; L279, L282, L283, and L284 supply the regional estimates used above. The patch comparison, partition, and normalization assembly are proved here.
