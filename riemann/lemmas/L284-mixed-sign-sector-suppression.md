# Lemma 284: absolute suppression of the mixed-sign sectors

**Hypotheses.** Use the actual theta kernel k, shifted integral I_n(a), and saddle parameters r,h,τ,Φ_* of L269. Let a→∞, let n≥1 be an integer, and suppose log a≤h≤2 log a. Put δ=cos(2τ) and

M={(s,x)∈ℝ²:(s+x)(s−x)<0}={|x|>|s|}.

**Conclusion.** There are absolute constants C,c>0 such that, uniformly for sufficiently large a,

exp(−2aτ) ∫∫_M |s|^(2n)|k(s+x+iτ)k(s−x−iτ)| ds dx
 ≤ C δ^(−5)(r+1)² exp(Φ_*−c h r)
 = o(exp(Φ_*)/a).

Thus both mixed-sign sectors have negligible total contribution, even in absolute value. No separate reflected theta-summand phase estimate is needed for this region. This statement does not itself assemble a global Laguerre sign theorem.

**Proof.** The parameter identities give

r=(1/2)log(a/(2π))+(1/4)log(1+h²/a²)~(log a)/2,
n=r(h−9/2),   δ=h/√(a²+h²).

Let E={min(|s+x|,|s−x|)≤r/4}. L279 bounds the absolute integral over M∩E by the asserted form, since absolute integration is monotone under restriction. It remains to treat M\E.

On M set m=|x|, l=|s|, so 0≤l<m and m−l>r/4 on M\E. This change of variables has unit Jacobian on each of the four sign quadrants. By the global strip estimate (2) of L269, the absolute integrand, including exp(−2aτ), is at most

Cδ^(−5)(l/m)^(2n) exp(F(m,l)),
F(m,l)=2n log m+9m−h exp(2(m−r))cosh(2l)−2aτ.          (1)

At l=0 the factor is zero, since n≥1; here m>r/4 so no division by zero occurs. This retains the exact polynomial factor lost when replacing |s| by m in the envelope. Put d=m−r and ψ(d)=exp(2d)−1−2d. The identity from L269 is

F−Φ_*=2n[log(m/r)−d/r]−hψ(d)
                    −h exp(2d)(cosh(2l)−1)≤−hψ(d).    (2)

The logarithmic bracket is nonpositive by log t≤t−1. There is an absolute c₀>0 with ψ(d)≥c₀ min(d²,|d|) on ℝ: the quotient at zero tends to 2, ψ is positive away from zero, and its negative and positive tails have respectively linear and exponential growth. Also

∫_ℝ (1+|d|)exp(−ψ(d)/2) dd<∞.                         (3)

First suppose |d|≥r/4. For r≥4, ψ(d)≥c₀r/4. Drop (l/m)^(2n)≤1, integrate l over the larger interval [0,m], and split exp(−hψ(d)) into equal factors. Equations (2)–(3), with h≥1, give

∫_(m>0, |m−r|≥r/4) ∫_0^m exp(F(m,l)) dl dm
 ≤ exp(Φ_*−c₀hr/8) ∫_(−r)^∞ (r+|d|)exp(−ψ(d)/2) dd
 ≤ C(r+1)exp(Φ_*−c₀hr/8).                             (4)

Now suppose |d|<r/4. Here 3r/4<m<5r/4. The exclusion of E gives l<m−r/4, and hence

l/m≤1−r/(4m)≤4/5.

Use F≤Φ_* from (2). The region has area at most Cr², so its contribution to the envelope integral is at most

Cr² exp(Φ_*)(4/5)^(2n)
 =Cr² exp(Φ_*−2r(h−9/2)log(5/4)).                     (5)

Eventually h≥9, so 2r(h−9/2)≥rh. Thus (5) is bounded by Cr²exp(Φ_*−rh log(5/4)). Restore Cδ^(−5) and the finite quadrant multiplicity in (4)–(5), then add the L279 bound on M∩E. Choosing c as the minimum of the three positive decay constants proves the asserted inequality.

Finally, let L=log a. Eventually r≥L/3, r=O(L), h≥L, and δ^(−5)≤C(a/h)^5. The ratio of our bound to exp(Φ_*)/a is at most

C a^6 h^(−5)(r+1)² exp(−c h r).

Its logarithm is at most −(c/3)L²+6L+O(log L), tending to −∞ uniformly. This is the required little-o estimate, with the full approach-to-strip-boundary loss included. ∎

The absolute exterior obstruction in L278 occurs near s=r and x=0, in a same-sign sector. It therefore does not contradict this bound. The positive-positive sector still requires its signed analysis; replacing |s| by m there has no gain. Combining the local result and all sector estimates requires a separate check of their domains and principal-patch normalizations. Lower indices and bounded exterior heights in L266 remain outside this statement.

**Mathlib.** Full statement: not checked. Supporting exponential/logarithmic inequalities, quadrant changes of variables, and improper integral comparison: not checked. No library match is claimed. L269 supplies the uniform strip envelope and parameter identities; L279 supplies the small-argument-region estimate. All new mixed-sector estimates are proved above.
