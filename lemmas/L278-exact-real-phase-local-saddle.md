# Lemma 278: exact real phase control of the low-index local saddle

**Hypotheses.** Use I_n(a), r,h,τ,Φ_* and the positive-tail model of L269. Let a→∞, L=log a, and restrict to integers n≥1 for which L≤h≤2L. Set p=(s−r+x)/√2 and q=(s−r−x)/√2 on t=x+iτ. Fix ε=1/100. Let J be the actual shifted integral over |p|,|q|≤ε, with positive area measure and with the factor exp(−2aτ) included as in L269.

**Conclusion.** Uniformly in this range,

J=(8π²)² exp(Φ_*) [π/(2a)+o(1/a)].

Moreover, the absolute integral over the complement of the two fixed saddle squares is not o(exp(Φ_*)/a). This is a local statement only. It supplies no bound on the complement of the two saddle squares and no new global Laguerre positivity range.

**Proof.** The saddle identities give r~L/2, n=r(h−9/2), and n/r²=O(h/r). The exact real-contour phase in L275 is

exp(Φ−Φ_*)=A(p,q) exp(if(p)−if(q)),
f(y)=−(a/2)(exp(cy)−1−cy), c=2√2,
A=exp(S),
S=2n log(1+v/r)+9v−(h/2)(exp(cp)+exp(cq)−2), v=(p+q)/√2.

Although the square is fixed rather than shrinking, direct differentiation gives, uniformly on it,

−Ch I≤Hess S≤−ch I, ∇S(0)=0,
A≤exp(−ch(p²+q²)),
|A_p|+|A_q|≤Ch(|p|+|q|)exp(−ch(p²+q²)),
|A_pq|≤C[h+h²(p²+q²)]exp(−ch(p²+q²)).                 (1)

Here and below c in inequalities denotes a positive constant, not necessarily 2√2. The Hessian is the sum of the negative diagonal matrix with entries 4h exp(cp),4h exp(cq) and a negative semidefinite matrix whose entries are n/(r+v)². This proves the assertions by integration from the origin and the chain rule. In particular the mixed variation expression of L275 is bounded on every subrectangle; its proof by Gaussian scaling applies unchanged.

Define

g(y)=sgn(y)√((exp(2√2y)−1−2√2y)/4), g(0)=0.

The quotient inside the square root divided by y² is smooth, positive, and equals 1 at zero. Thus g is smooth at zero, g'(0)=1, and g' is positive throughout [−ε,ε]: away from zero this also follows directly from the sign of exp(2√2y)−1. Its inverse P on [g(−ε),g(ε)] has bounded first three derivatives, with P'(0)=1. All bounds are fixed independently of a,h. Set Y=g(p), Z=g(q). The model integral becomes exactly

∫∫ B(Y,Z) exp(−2iaY²+2iaZ²)dY dZ,
B=A(P(Y),P(Z))P'(Y)P'(Z).                              (2)

The transformed amplitude has uniformly bounded mixed variation on every subrectangle. To verify this rather than assuming invariance of a norm, differentiate B once in each variable. Its mixed derivative is a bounded linear combination of A_pq,A_p,A_q,A, evaluated at P(Y),P(Z). The coordinate Jacobians are bounded above and below. Their absolute double integrals are bounded by (1): respectively O(1), O(h^(−1/2)), O(h^(−1/2)), and O(h^(−1)). The single-edge terms are bounded by Gaussian scaling as in L275; the extra terms involving A have bounded edge integrals too. The corner term is bounded. Hence the rectangle integration identity from L275 applies with a uniform constant.

Take R=a^(−2/5). Eventually [−R,R]² lies inside the transformed rectangle. On this central square, P(Y)=Y+O(Y²), P'(Y)=1+O(|Y|), and (1) implies

B(Y,Z)=1+O(R+hR²).

Thus replacing B by 1 costs O(R³+hR⁴) in absolute integral. The Fresnel integral and its integration-by-parts tail bound (as proved in L274) give

|∫_(−R)^R exp(−2iaY²)dY|²
 =π/(2a)+O(1/(a^(3/2)R)+1/(a²R²)).

The rest of the transformed rectangle partitions into four rectangles, on each of which at least one coordinate lies wholly outside [−R,R]. Quadratic-phase primitives on all subintervals are O(a^(−1/2)), and those on a tail interval are O((aR)^(−1)), by integration by parts away from zero. Applying the bounded mixed variation identity to (2) bounds the entire complementary portion by O(1/(a^(3/2)R)). This treats the possibly asymmetric endpoints g(−ε),g(ε), not just a symmetric truncation. The model error relative to 1/a is consequently

O(aR³+ahR⁴+1/(√a R)+1/(aR²))=o(1),

since h≤2L. No strip clearance or complex rotation is needed.

Finally transfer to actual theta. At the two kernel arguments z, the quantities V=πexp(2z) have modulus comparable to a and

Re V≥(h/2)exp(−2√2ε).

The exact theta series from L269 therefore gives uniformly on the whole original square

k(z)/k_0(z)=1+O(a^(−1))+O(exp(−γh)),
γ=(3/2)exp(−2√2ε)>1.

The higher-index series is bounded after factoring out its j=2 exponential, uniformly once Re V≥1. The product has the same relative error. By (1) the model modulus integral is O(1/h), so the actual-minus-model error, after removing the fixed factor (8π²)²exp(Φ_*), is

O((a^(−1)+exp(−γh))/h)=o(1/a),

because h≥L and γ>1. Combining with (2) proves the local conclusion.

To check the absolute exterior obstruction, take the fixed rectangle 2ε≤u=s−r≤3ε, 0≤x≤ε/10. It lies outside the positive p,q square (both p and q exceed ε) and far from the negative saddle. The exact real exponent satisfies

S=2n[log(1+u/r)−u/r]−h[exp(2u)−1−2u]−h exp(2u)[cosh(2x)−1].

For 0≤u≤0.03, the second bracket is at most 0.002; for 0≤x≤0.001 the last bracket including exp(2u) is less than 0.000003. The first term is at least −n u²/r²≥−h u²/r, using log(1+t)≥t−t²/2 for t≥0. Thus S≥−0.01h for all sufficiently large a. These numerical inequalities follow directly by bounding the exponential series, with ample slack. On this rectangle the same exact theta estimate applies with Re V≥(h/2)exp(−0.002), so the modulus of the product/model ratio is at least 1/2 eventually. The rectangle has fixed positive area. Its absolute integral is therefore at least c exp(Φ_*)exp(−0.01h)≥c exp(Φ_*)a^(−0.02). Dividing by exp(Φ_*)/a tends to infinity. Hence absolute integration of the full exterior cannot establish the required remainder; cancellation is essential. ∎

Here n~hL/2 is of order L². The full integral also includes regions outside these squares; their absolute strip envelope has the factor δ^(−5) of L269, with δ~h/a. The local proof does not remove that loss or control cancellation there. L266 still requires every index through its linear witness cutoff and bounded exterior heights.

**Mathlib.** Full statement: not checked. Supporting change of variables, Fresnel integration, rectangle integration by parts, and theta estimates: not checked. No library match is claimed. L274 supplies the proved Fresnel evaluation and tail estimate; L275 supplies the rectangle integration identity and phase convention; L269 supplies the theta series and contour identity. The new low-h derivative and remainder estimates are proved above.
