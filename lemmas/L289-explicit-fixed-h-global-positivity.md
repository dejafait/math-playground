# Lemma 289: global Laguerre positivity in explicit fixed-h bands

**Hypotheses.** Use the theta kernel k, shifted integral I_n(a), and parameters r,h,τ,Φ_* of L269. Fix 96<h₀≤h₁<∞. Let a→+∞ and n≥1 be integers with h₀≤h≤h₁. Put δ=cos(2τ) and C₀=(8π²)². All errors below are uniform in this band.

**Conclusion.** The whole-plane integral satisfies

I_n(a)=C₀ exp(Φ_*) (π/a)(|ζ(h−4+ia)|²+o(1)).

In particular D_n(Ξ;a)>0 eventually, also for |a|→∞. For example the interval 100≤h≤101 gives an index band with endpoints asymptotic to (191/4)log a and (193/4)log a. This does not assert positivity at all smaller indices or bounded exterior heights.

**Proof.** The parameter identities give

r=(1/2)log(a/(2π))+(1/4)log(1+h²/a²),
n=r(h−9/2), δ=h/sqrt(a²+h²).

We reprove the needed bounds in the fixed-h range, rather than apply the logarithmic-h conclusions of L279 or L284 outside their hypotheses. Use L269's parameterwise contour identity and denote its shifted integrand by

F(s,x)=exp(−2aτ)s^(2n)k(s+x+iτ)k(s−x−iτ)exp(2iax).

Set E={min(|s+x|,|s−x|)≤r/4}, M={|x|>|s|}, and D={s+x>r/4,s−x>r/4}. We claim

∫_(E∪M) |F| ≤ C δ^(−5)(r+1)² exp(Φ_*−hr/8).       (1)

Here and below a is sufficiently large. To prove this, put m=max(|s|,|x|), l=min(|s|,|x|), d=m−r, and ψ(d)=exp(2d)−1−2d. The global strip bound of L269 gives |F|≤Cδ^(−5)exp(A), where

A=2n log m+9m−h exp(2d)cosh(2l)−2aτ.

For m>0 its exact comparison is

A−Φ_*=2n[log(m/r)−d/r]−hψ(d)
                  −h exp(2d)(cosh(2l)−1)≤−hψ(d).    (2)

The discarded logarithmic bracket is nonpositive. The map to (m,l) has bounded multiplicity and unit absolute Jacobian on each piece. Null axes cause no difficulty.

For |d|≥r/4 we have ψ(d)≥r/4 when r≥4. Indeed for d≤−r/4, ψ(d)≥−1−2d≥r/2−1≥r/4. For d≥r/4, ψ is increasing and ψ(r/4)≥r/4: the last inequality follows from exp(r/2)≥1+3r/4 for r≥4, true at 4 and thereafter by differentiation. The finite integral

∫_ℝ (1+|d|)exp(−ψ(d)/2) dd < ∞

follows from linear growth on the negative tail and exponential growth on the positive tail. Splitting exp(−hψ(d)) into equal factors and using h≥1, integration over all 0≤l≤m therefore gives at most

C(r+1)exp(Φ_*−hr/8).                               (3)

This treats the entire far region, irrespective of E or M.

In the remaining region |d|<r/4, the condition E is m−l≤r/4 and implies l>r/2. For large r,

exp(2d)(cosh(2l)−1)≥exp(r/2)/4≥r/8.

The first inequality uses exp(2d)≥exp(−r/2) and cosh(2l)−1≥exp(2l)/4. The region has area O(r²), so (2) bounds its integral by Cr²exp(Φ_*−hr/8).

For M outside E, the polynomial in the true integrand is l^(2n), so its sharper bound is Cδ^(−5)(l/m)^(2n)exp(A). In the central region m<5r/4 and m−l>r/4 imply l/m≤4/5. Since h≥9,

2n log(5/4)=2r(h−9/2)log(5/4)≥rh log(5/4)>rh/8.

For an elementary strict last bound, log(5/4)=∫_1^(5/4)dt/t≥1/5>1/8. The central area is O(r²), and A≤Φ_*. Combining this estimate with (3) and the bound on E proves (1), restoring the finite multiplicities and strip factor.

Compare (1) with the actual main scale exp(Φ_*)/a. Since h stays in the specified compact interval, δ^(−5)≤Ca^5 and r≥(log a−log(2π))/2. Consequently the relative bound is

C a^6(r+1)² exp(−hr/8)
 ≤ C a^(6−h₀/16)(log a)²=o(1).                       (4)

The constant absorbs (2π)^(h₁/16). The strict threshold h₀>96 is exactly what makes the exponent negative; neither h=96 nor all h>5 is established by this estimate.

L288 applies to D and gives

∫_D F=C₀ exp(Φ_*)(π/(2a)) · (|ζ(h−4+ia)|²+o(1)),

with |ζ(h−4+ia)|²≥ζ(h₀−4)^(−2)>0. Outside E the two real kernel arguments have magnitude greater than r/4. Their signs partition that exterior into D, D_-={s+x<−r/4,s−x<−r/4}, and M\E. The exact evenness of k gives F(−s,x)=F(s,x): it swaps the two kernel factors, leaves the even polynomial unchanged, and leaves exp(2iax) unchanged. This reflection maps D to D_-. Thus the full integral is twice the D integral plus an error bounded by (1). Equation (4) proves the stated asymptotic. The original integral is real, and the uniform positive lower bound makes it strictly positive. The normalization D_n(Ξ;a)=2^(2n−1)I_n(a)/(2n)! from L269 preserves the sign; evenness gives negative a as well.

Finally n(h)=r(h)(h−9/2) is increasing for h>9/2 and large a, since r>0 and r'(h)>0. At h=100 and 101 its endpoint coefficients of log a are (100−9/2)/2=191/4 and (101−9/2)/2=193/4. Integers are rounded inward at the exact endpoints. ∎

This is a sufficient explicit fixed-h range, without an optimality claim. L266 still needs every index through its linear cutoff, including the smaller logarithmic and sublogarithmic indices, and bounded exterior heights. There is no RH candidate.

**Mathlib.** Full statement: not checked. Supporting contour identities, elementary exponential inequalities, integral comparison, reflection, and asymptotic sign transfer: not checked. No library match is claimed. L269 supplies the strip bound and normalization and L288 the summed sector asymptotic; the fixed-h complement and its explicit threshold are proved above. L279 and L284 motivate the decomposition but their restricted conclusions are not used as premises.
