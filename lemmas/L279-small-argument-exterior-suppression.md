# Lemma 279: suppression of the small-argument exterior

**Hypotheses.** Use the actual theta kernel k and the shifted integral I_n(a), saddle parameters r,h,τ, and Φ_* of L269. Let a→∞, let n≥1 be an integer, and suppose log a≤h≤2 log a. Put δ=cos(2τ) and

E={ (s,x)∈ℝ² : min(|s+x|,|s−x|)≤r/4 }.

**Conclusion.** There are fixed C,c>0 such that, uniformly in this range for sufficiently large a,

exp(−2aτ) ∫∫_E |s|^(2n)|k(s+x+iτ)k(s−x−iτ)| ds dx
 ≤ C δ^(−5)(r+1)² exp(Φ_*−c h r)
 = o(exp(Φ_*)/a).

This removes only a subregion of the saddle exterior. It does not assert a global Laguerre sign.

**Proof.** The saddle identities give

r=(1/2)log(a/(2π))+(1/4)log(1+h²/a²)~(1/2)log a,
δ=h/√(a²+h²),   n=r(h−9/2).

Use the global strip estimate (2) proved in L269. Its proof applies to every 0<τ<π/4, independently of that lemma's proportional-index hypothesis. It retains the entire theta series and gives an upper bound Cδ^(−5)exp(F(m,l)) for the integrand including exp(−2aτ), where

m=max(|s|,|x|), l=min(|s|,|x|), 0≤l≤m,
F(m,l)=2n log m+9m−h exp(2(m−r))cosh(2l)−2aτ.

Here |s|≤m was used only to increase the polynomial factor. The point m=0 is irrelevant to integration. The coordinate mapping has at most eight preimages, all with unit area Jacobian off null boundaries. Moreover min(|s+x|,|s−x|)=m−l. With d=m−r and ψ(d)=exp(2d)−1−2d, direct subtraction gives

F−Φ_*=2n[log(m/r)−d/r]−hψ(d)
             −h exp(2d)(cosh(2l)−1).                 (1)

The logarithmic bracket is nonpositive by log t≤t−1; every subtracted term is nonnegative.

First integrate over |d|≥r/4, allowing all 0≤l≤m. There is an absolute c₀>0 such that ψ(d)≥c₀ min(d²,|d|) for every real d. This follows from its Taylor expansion at zero, positivity away from zero, its asymptotic 2|d| on the negative tail, and exponential growth on the positive tail. Thus, for r≥4 and |d|≥r/4, ψ(d)≥c₀r/4. Split the factor exp(−hψ(d)) into two equal factors. One is at most exp(−c₀hr/8); the other is integrable with its first absolute moment, uniformly for h≥1. In detail,

∫_(−r)^∞ (r+|d|) exp(−hψ(d)/2) dd
 ≤ r ∫_ℝ exp(−ψ(d)/2) dd + ∫_ℝ |d|exp(−ψ(d)/2) dd
 ≤ C(r+1).

Integrating l first supplies its interval length m≤r+|d|. Equation (1) therefore bounds this entire unbounded portion by C(r+1)exp(Φ_*−c₀hr/8).

On the remaining portion, |d|<r/4 and m−l≤r/4 imply

3r/4<m<5r/4,   l≥m−r/4>r/2.

For large r, cosh(2l)−1≥exp(2l)/4. Consequently

exp(2d)(cosh(2l)−1)≥(1/4)exp(−r/2+r)=(1/4)exp(r/2).

Its area in (m,l) is O(r²). Dropping the other nonpositive terms in (1) bounds its integral by Cr²exp(Φ_*−(h/4)exp(r/2)). Since exp(r/2)/4≥c r eventually for any fixed c, this is at most Cr²exp(Φ_*−c h r), with c chosen no larger than c₀/8. Adding both portions and restoring Cδ^(−5) proves the inequality.

Finally, write L=log a. We have r≥L/3 eventually, h≥L, and δ^(−5)≤C(a/h)^5. Dividing the bound by exp(Φ_*)/a gives at most

C a^6 h^(−5)(r+1)² exp(−c h r).

Its logarithm is at most −(c/3)L²+6L+O(log L), which tends to −∞ uniformly. This proves precisely the required little-o estimate, despite the strip loss. ∎

The two fixed saddle squares in L278 have min(|s+x|,|s−x|)=r+O(1), so E is disjoint from them eventually. L278's exterior modulus obstruction also lies outside E. The estimate therefore does not contradict that obstruction or control the entire exterior. The complementary region still requires a signed estimate using the actual theta series; the smaller indices and bounded exterior heights in L266 remain missing.

**Mathlib.** Full statement: not checked. Supporting exponential inequalities, finite-region changes of variables, and improper integral bounds: not checked. No library match is claimed. L269 supplies the exact-series global strip estimate and saddle conventions; all new geometric and integral estimates are proved here.
