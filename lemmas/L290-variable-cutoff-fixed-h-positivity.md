# Lemma 290: variable-cutoff fixed-h global positivity

**Hypotheses.** Use the actual theta kernel, shifted integrand F, integral I_n(a), and parameters r,h,τ,Φ_* of L269. Set

H=9/2+15/(4 log 2).

Fix H<h₀≤h₁<∞. Let a→+∞ and n≥1 be integers with h₀≤h≤h₁. Put δ=cos(2τ) and C₀=(8π²)². Errors are uniform in this compact band.

**Conclusion.**

I_n(a)=C₀ exp(Φ_*) (π/a)(|ζ(h−4+ia)|²+o(1)),

and hence D_n(Ξ;a)>0 eventually, also for negative a by evenness. The sufficient threshold H is approximately 9.91, below 96 but above the positive-sector summability boundary 5. No all-index or bounded-height assertion follows.

**Proof.** The exact parameter identities are

r=(1/2)log(a/(2π))+(1/4)log(1+h²/a²),
n=r(h−9/2), δ=h/sqrt(a²+h²),
Φ_*=2n log r+9r−h−2aτ.

Choose fixed ε,η>0 so small that q=1+ε, t=(q+η)/2<1,

2(h₀−9/2)>9q/2,
λ=−2(h₀−9/2)log t+9(1−t)>12.                 (1)

These choices exist: at ε=η=0 the second expression is 2(h₀−9/2)log 2+9/2>12, by h₀>H; the first inequality is also strict there. Define E_η={min(|s+x|,|s−x|)≤ηr} and M={|x|>|s|}.

We first prove that their union contributes o(exp(Φ_*)/a) absolutely. Set m=max(|s|,|x|), l=min(|s|,|x|), T=m+l, d=m−r. The coordinate change has bounded multiplicity and unit absolute Jacobian. L269's parameterwise strip bound gives the envelope Cδ^(−5)exp(A), where

A=2n log m+9m−h exp(2d)cosh(2l)−2aτ.

Since log(m/r)≤d/r and 2n/r+9=2h,

A−Φ_*≤2hd+h−h exp(2d)cosh(2l)
       ≤2hT+h−(h/2)exp(2(T−r)).                    (2)

On T≥qr, for all sufficiently large r, 2T+1≤exp(2(T−r))/4 uniformly: it holds at qr eventually and the ratio of the right side to 2T+1 is increasing there. Thus (2) is at most −(h/4)exp(2(T−r)). Integrating first along the segment m+l=T costs at most T. Writing T=qr+u and using exp(2u)≥1+2u proves

∫_(T≥qr) exp(A−Φ_*) dm dl
 ≤ C(r+1)exp(−(h₀/4)exp(2εr)).                    (3)

For example the remaining integral is bounded by the integral of (qr+u)exp(−K(1+2u)), with K=(h₀/4)exp(2εr)≥1. This is superexponentially small in r and absorbs δ^(−5)a=O(a^6).

On T≤qr and E_η, m−l≤ηr implies m≤tr. Dropping the negative exponential term in A, the function 2n log(m/r)+9(m−r) is increasing in m>0. Consequently

A−Φ_*≤[2(h−9/2)log t+9(t−1)]r+h≤−λr+h₁.       (4)

The area is O(r²). This retains the logarithmic penalty that the earlier envelope comparison dropped.

For M and T≤qr, the actual polynomial is l^(2n), so use instead

B=2n log l+9m−h exp(2d)cosh(2l)−2aτ.

The line l=0 is null and has zero integrand. For fixed 0<T≤qr, m=T−l and 0<l≤T/2. The derivative of 2n log(l/r)+9(T−l−r) with respect to l is 2n/l−9≥4(h₀−9/2)/q−9>0 by (1). Its maximum is therefore at l=T/2. The resulting function of T, 2n log(T/(2r))+9(T/2−r), is increasing. At T=qr this gives

B−Φ_*≤[2(h−9/2)log(q/2)+9(q/2−1)]r+h.

Since q/2<t and u↦2(h−9/2)log u+9(u−1) is increasing, this is again ≤−λr+h₁. Its area is O(r²). Together with (3)–(4), including finite coordinate multiplicities, we obtain

∫_(E_η∪M)|F| ≤ Cδ^(−5)exp(Φ_*)[(r+1)²exp(−λr)
                      +(r+1)exp(−(h₀/4)exp(2εr))].       (5)

The first term divided by exp(Φ_*)/a is O(a^(6−λ/2)(log a)²)=o(1), since λ>12 and r=(log a−log(2π))/2+o(1). The second term is smaller than every power of a. This proves the required complement estimate.

For completeness we check L288's positive-sector calculation with the new fixed cutoff; its statement for η=1/4 is not applied to a different domain without this check. Put D_η={s+x>ηr,s−x>ηr}. In L288's p,q summand coordinates the lower endpoints become

α_j=(log j−(1−η)r)/sqrt(2), α_k=(log k−(1−η)r)/sqrt(2).

They still define a rectangle. We have s>ηr, n/s≤(h−9/2)/η and n/s²≤(h−9/2)/(η²r). Thus the first and mixed derivative estimates there hold with constants depending on η,h₀,h₁. The exact lower-degree factor obeys

exp(−cp)/|V_+|≤exp(−2ηr)/(πj²),

and similarly for k, so it and its needed derivatives remain bounded. The same envelope (jk)^(4−h)g_h(p)g_h(q) is valid from log(s/r)≤(s−r)/r. Its double index sum converges uniformly because h₀>5. The global phase primitives are unchanged. Hence the rectangular variation argument bounds each clipped square by C exp(Φ_*)(jk)^(4−h)/a and its complement by the same bound times a^(−1/2). Every fixed-index stationary square eventually lies in D_η because α_j,α_k→−∞. The local expansion and finite-index-then-tail summation in L288 therefore give, with precisely the same leading coefficient,

∫_(D_η)F=C₀exp(Φ_*)[π/(2a)] · (|ζ(h−4+ia)|²+o(1)).

No new limiting interchange is needed: the unchanged summable majorant controls both normalized local integrals and proposed leading terms, and all finite-index errors are uniform in h. L288's absolutely convergent Euler-product argument gives |ζ(h−4+ia)|²≥ζ(h₀−4)^(−2)>0.

Outside E_η∪M the only sectors are D_η and its reflection under s↦−s. The evenness of k swaps the kernel factors, giving F(−s,x)=F(s,x). The full integral is therefore twice the displayed sector integral plus an error bounded by (5). It is real by the original integral representation, and its main coefficient is uniformly positive. L269's normalization D_n(Ξ;a)=2^(2n−1)I_n(a)/(2n)! finishes the proof. ∎

This calculation does not approach h=5 merely by sending ε,η to zero: its limiting sufficient condition is 2(h−9/2)log 2+9/2>12. This is a limitation of the particular bound, not an optimality theorem for actual theta integrals or all absolute estimates. Smaller logarithmic indices, sublogarithmic indices, and bounded exterior heights still obstruct L266's full witness target.

**Mathlib.** Full statement: not checked. Supporting exponential inequalities, integral bounds, rectangular variation, and asymptotic sign transfer: not checked. No full or supporting library match is claimed. The parameterwise strip estimate and normalization come from L269; the stationary-sum proof and Euler-product lower bound come from L288, with all cutoff-dependent estimates rechecked above.
