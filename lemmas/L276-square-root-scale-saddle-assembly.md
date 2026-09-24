# Lemma 276: uniform saddle positivity in a square-root-scale band

**Hypotheses.** Use the theta kernel, integral I_n(a), saddle parameters r,h,τ, phase Φ_*, and matrix B of L269. Let a→+∞, with integer n≥1 satisfying

√a(log a)² ≤ h=n/r+9/2 ≤ 2√a(log a)².

All limits below are uniform over these integers. Write C₀=(8π²)².

**Conclusion.** With the positive square root,

I_n(a)=C₀ exp(Φ_*) 4π/√(det B) · (1+o(1)).

Consequently D_n(Ξ;a)>0 throughout this band for all sufficiently large a. The same holds with a replaced by |a|. The band has n between (1/2+o(1))√a(log a)³ and (1+o(1))√a(log a)³; this is not positivity at every larger index or every smaller index.

**Proof.** The unique saddle and exact shifted-contour identity are those proved in L269. Their existence and parameterwise contour shift do not require n/a bounded below. The defining equation gives, uniformly here,

r=(1/2)log(a/(2π))+(1/4)log(1+(h/a)²)~(1/2)log a,
n=r(h−9/2),   δ=cos(2τ)=h/√(a²+h²),
δ^(−5)≤C a^(5/2),   det B=16a²+16h²+8hn/r²~16a².

In particular n≤a eventually, and n≥c√a(log a)³. The hypotheses used for the local estimates in L273–L275 thus hold with fixed comparison constants, independently of the chosen integer.

Fix 0<κ<1/4. Choose a fixed M>0 sufficiently large as specified below, and put R=κh/a and ε=√(M log a/h). Around the positive saddle write u=s−r and p=(u+x)/√2, q=(u−x)/√2. Both radii tend to zero and R/ε→0 uniformly. Partition its outer p,q square into the inner radius-R square and the annulus of L275.

First consider the inner square. On the rotated square of L273 the actual holomorphic form differs from C₀ exp(Φ_*) times its quadratic model by relative error bounded by

η=C[aR³+a^(−1)+exp(−c h)].

The quadratic form there is real positive definite with eigenvalues comparable to a. Therefore its absolute integral is O(1/a), and the actual rotated integral equals C₀ exp(Φ_*)[G+O(η/a)+O(exp(−caR²)/a)], where G=2π/√(det B)>0. Orient the rotated plane by continuation of the original real area orientation; the determinant-one opposite rotations introduce no additional complex factor. Equivalently ds∧dt=−dp∧dq, and reversing the p,q orientation compensates this fixed minus sign.

The actual form is closed throughout the strip-contained homotopy. Stokes and L274's signed connector estimate transfer this value back to the original inner square with additional error at most C exp(Φ_*)(E+η)/a, where

E=1/(√a R)+a hR⁴+(h/a)²+exp(−c aR²).

Every term tends to zero uniformly: respectively they are bounded by constants times (log a)^(−2), (log a)^10/√a, (log a)^4/a, and exp(−c'(log a)^4); also aR³=O((log a)^6/√a). Thus the actual inner square contributes C₀ exp(Φ_*)[G+o(1/a)]. This uses the signed sum of the connectors, not the false assertion that their individual absolute integrals are negligible.

L275 bounds the annulus by

C exp(Φ_*)[1/(a^(3/2)R)+(a^(−1)+exp(−c h))/h]
=o(exp(Φ_*)/a),

uniformly here. Its proof uses only ε→0, r→∞, n/r²=O(h/r), and the displayed fixed comparisons for h, so its constants are uniform on this band for fixed M. Hence the whole positive outer square contributes C₀ exp(Φ_*)[G+o(1/a)].

It remains to bound the full complement; an estimate for a differently shaped square cannot be substituted without checking inclusion. The outer p,q square contains the u,x square of radius e=ε/√2, since |u|,|x|≤e implies |p|,|q|≤ε. Use its reflected copy at the negative saddle as well. The complement of the two outer squares is consequently contained in the complement of these two radius-e u,x squares. Absolute integration is monotone under this inclusion.

The envelope proof in L269, equations (7)–(10), applies with radius e: it uses only h≥1, e→0, r→∞, and e/(r−e)≤exp(−1/2), all valid uniformly here. Explicitly its loss is δ^(−5), its exponent is bounded above by Φ_*−hψ(m−r)−h exp(2(m−r))(cosh(2l)−1), where ψ(v)=exp(2v)−1−2v, m=max(|s|,|x|), l=min(|s|,|x|). The region |m−r|>e has an exp(−c h e²) saving after integration; for |m−r|≤e and l>e the last term gives the same saving. The two remaining swapped boxes, |x| near r and |s|≤e, retain the dropped factor (l/m)^(2n)≤exp(−n). Thus the complementary absolute integral is at most

C δ^(−5) exp(Φ_*)[(r+1)² exp(−c h e²)+exp(−n)].

Here c>0 is fixed independently of M and the band parameters once e<1/2. Dividing by exp(Φ_*)/a and using h e²=(M/2)log a bounds this by

C a^(7/2)[(log a)² a^(−cM/2)+exp(−c'√a(log a)³)].

Choose M so that cM/2>5. This expression tends to zero uniformly. Increasing fixed M does not change any of the preceding local limits. Thus the polynomial cost of approaching the theta-strip boundary is absorbed, with no unestimated region between the local and far contours.

Finally the shifted integrand is exactly even in s, by evenness of k, so reflection gives an equal contribution from the negative outer square. The original integral is real, and therefore

I_n(a)=C₀ exp(Φ_*)[2G+o(1/a)].

Since G~π/(2a)>0, this proves the claimed asymptotic and positivity. The positive multiplier D_n(Ξ;a)=2^(2n−1)I_n(a)/(2n)! recorded in L269 supplies the Laguerre assertion. Evenness in a and n=r(h−9/2) give the remaining claims. ∎

This band lies below L271's sufficient threshold but does not connect to it by an established uniform estimate. In particular the full interval through L266's height-only witness cutoff, and bounded heights, remain unproved. No RH candidate follows.

**Mathlib.** Full statement: not checked. Supporting Stokes theorem, contour shifts, Gaussian bounds, and uniform asymptotics: not checked. No library match is claimed. The analytic inputs are the estimates proved in L269 and L273–L275; the domain inclusion, parameter uniformity, and far-contour comparison are checked above.
