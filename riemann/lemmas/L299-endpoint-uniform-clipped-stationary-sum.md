# Lemma 299: endpoint uniform clipped stationary sum

**Hypotheses.** Use the exact summand coordinates, positive sector D, phase f, and normalization C₀exp(Φ_*) of L288, now at h=5, with a→∞ and integer n satisfying 2n=r. Thus r=(1/2)log(a/(2π))+(1/4)log(1+25/a²). Set ε=1/100. Let C_jk be the integral of the exact (j,k) summand over D intersected with |p|,|q|≤ε, with positive area measure. Use W_r and T_r(a) from L297.

**Conclusion.** The finite sum of clipped stationary patches satisfies

Σ_(j,k≥1) C_jk = C₀exp(Φ_*) π/(2a) [T_r(a)+O(r a^(−1/10)+r exp(−r/32))].       (1)

In particular the additive error in brackets is o(1). This is a sum of separately assigned summand patches, not the integral of the full kernel over their union. The nonstationary complement of these patches in D is not estimated here. Neither endpoint sector positivity nor a global sign extension follows.

**Proof.** Write b=log(jk)/2, v=(p+q)/√2, s₀=r−b. In the notation of L288 the normalized amplitude on a full patch is exactly

H_jk=W_r(j,k) A_b E,
A_b=exp(r log(1+v/s₀)+9v−(5/2)(exp(cp)+exp(cq)−2)), c=2√2,
E=(1−3exp(−cp)/(2V_+))(1−3exp(−cq)/(2V_-)),
|V_±|=sqrt(a²+25)/2.

The phase and exterior factor are exp(if(p)−if(q)) and exp(ia log(k/j)), respectively. These are algebraic identities from L288, not an application of its conclusion outside its h-range.

A clipped patch is nonempty only if

log j, log k < 3r/4+√2ε.                                  (2)

For these indices s₀≥r/4−√2ε. For large r, s₀≥r/5 and s₀+v>0 throughout the full ε-square, including its portion outside D. Thus A_b and its derivatives through order two are bounded by an absolute constant there, uniformly in both indices. To see the uniformity directly, |v|≤√2ε, r/s₀≤5, and each derivative of r log(1+v/s₀) is bounded using r/(s₀+v) and r/(s₀+v)². Its value is bounded by the mean value theorem and the bound on r/s₀. The exponential terms and their derivatives are bounded on the fixed square. Also A_b(0,0)=1. The factors E−1 and their first and mixed derivatives are O(1/a), uniformly on this square.

The global oscillatory primitive estimate used in L288 is O(a^(−1/2)) for every interval. Together with the rectangular variation bound for A_b E just proved, it gives, for every clipped rectangle,

|C_jk| ≤ C C₀exp(Φ_*) W_r(j,k)/a.                        (3)

Boundary endpoints are included by continuity. The same estimate applies to the full patch integral, denoted J_jk. All central weights in (2) are positive because log(jk)<3r/2+2√2ε<2r.

We next make the local asymptotic quantitative and uniform. Apply L288's exact real phase change Y=g(p), Z=g(q), where

g(y)=sgn(y)sqrt((exp(cy)−1−cy)/4), g'(0)=1.

On the fixed interval its inverse P and its needed derivatives are bounded. The phase becomes −2aY²+2aZ². The transformed amplitude

B(Y,Z)=A_b(P(Y),P(Z))P'(Y)P'(Z)

has uniformly bounded first and mixed derivatives, B(0,0)=1, and uniformly bounded rectangular variation. Set R=a^(−2/5); the central square |Y|,|Z|≤R lies in the transformed patch for large a. Replacing B by 1 there costs O(R³) in absolute integral, since B−1=O(R). Its complement in the transformed rectangle is at most four rectangles with one coordinate of magnitude at least R. On that coordinate the Fresnel primitive is O(1/(aR)); on the other it is O(a^(−1/2)). Rectangular integration by parts bounds this complement by O(a^(−3/2)/R). The constant central Fresnel integral differs from the full-plane product π/(2a) by O(a^(−3/2)/R+a^(−2)/R²). Finally B times the transformed E−1 has variation O(1/a), so its signed integral is O(a^(−2)) by the two unrestricted primitive bounds. Every constant here is uniform over (2). Consequently

J_jk = C₀exp(Φ_*) exp(ia log(k/j)) W_r(j,k)
       · [π/(2a)+O(a^(−11/10))].                        (4)

Indeed R³=a^(−6/5), a^(−3/2)/R=a^(−11/10), and a^(−2)/R²=a^(−6/5). This improves fixed-pair little-o to a uniform relative error O(a^(−1/10))=o(1/r).

It remains to justify replacing the clipped index set by J_r². Define the good indices by log j,log k<3r/4−√2ε. Their full patches lie in D, so C_jk=J_jk. Every remaining nonempty clipped patch, and every pair in J_r² that is not good, has at least one index m with

log m≥3r/4−√2ε.                                        (5)

Their total W_r mass is O(r exp(−r/32)). Here is a discrete tail justification, to avoid treating a moving boundary as a fixed-index limit. W_r decreases in each coordinate, as proved in L297. Put K=ceil(exp(3r/4−√2ε)). For K≥2, monotone integral comparison gives

Σ_(j≥K,k≥1) W_r(j,k)
 ≤ ∫_(K−1)^∞ [W_r(x,1)+∫₁^∞ W_r(x,y)dy] dx.

After x=exp(u), y=exp(v), the double integral is bounded by

∫_B^∞ L exp(−L²/(8r))dL=4r exp(−B²/(8r)),

where B=log(K−1), using L297's bound Q_r(L)≤exp(−L²/(8r)). The single integral is bounded by

∫_B^∞ exp(−L²/(8r))dL ≤ (4r/B)exp(−B²/(8r)).

For large r, B≥r/2. The union bound for j≥K or k≥K therefore proves the asserted O(r exp(−r/32)) tail, including indices outside (2). Values at the zero cutoff cause no issue because W_r was extended by zero. L297 also gives Σ_(j,k≥1)W_r(j,k)=O(r).

Sum (4) on good indices. Its normalized error is O(r a^(−1/10)). Replace their leading sum by T_r(a), using (5) and the tail estimate. Bound the remaining clipped patches by (3) and the same tail. This proves (1). Only finitely many clipped patches are nonempty by (2), so no interchange of an infinite family of patch integrals is used. Finally r~(log a)/2 implies both errors in (1) tend to zero. ∎

The result supplies the clipped stationary input only. A positive lower bound for T_r(a) exceeding the total normalized error, the nonstationary complement in D, and the other sectors remain needed even for h=5. Lower indices and bounded exterior heights would still be required for L266's full witness target.

**Mathlib.** Full statement: not checked. Supporting Fresnel integrals, rectangular integration by parts, monotone sum-integral comparison, and smooth inverse change of variables: not checked. No library match is claimed. L288 supplies the exact summand algebra and phase substitution; its primitive argument is reused without its h>5 summation conclusion. L297 supplies the endpoint weights, their monotonicity, and Gaussian mass majorant. The uniform local error and moving-boundary tail estimates are proved here.
