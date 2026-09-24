# Lemma 287: exact-summand positivity for diverging h

**Hypotheses.** Use the actual theta integral I_n(a), saddle parameters r,h,τ,Φ_* and Laguerre normalization of L269. Let a→+∞ and n≥1 be integers such that h→∞ and h≤L=log a. Equivalently, uniform statements below hold on H(a)≤h≤L for any function H(a)→∞ with H(a)≤L.

**Conclusion.** In this range,

I_n(a)=(8π²)²exp(Φ_*)[π/a+o(1/a)],

and hence D_n(Ξ;a)>0 eventually. Combining with L286, for every fixed C>0 and every H as above, all integers

ceil(r(H)(H−9/2))≤n≤Ca,
r(t)=(1/2)log(a/(2π))+(1/4)log(1+t²/a²),

have eventual strict positivity. The lower endpoint is asymptotic to H(a)log(a)/2. In particular the combined result covers sequences with n/log a→∞ and n≤Ca. It does not cover every n=O(log a), fixed indices, or bounded exterior heights.

**Proof.** We extend the estimates underlying the earlier statements, checking their parameter restrictions. Throughout our range,

r~L/2, n=r(h−9/2), n/r²≤h/r, δ=cos(2τ)=h/√(a²+h²).

Eventually h≥9 and r≥L/3. The contour identity in L269 is valid parameterwise for every n≥1 and 0<τ<π/4, so write F for its exact shifted integrand, including exp(−2aτ). Put C₀=(8π²)² and ε=1/100.

First evaluate only the exact (1,1) theta summand on its square Q: |p|,|q|≤ε, where p=(s−r+x)/√2, q=(s−r−x)/√2. The normalized integrand is

A(p,q)E(p,q)exp(if(p)−if(q)),
f(y)=−(a/2)(exp(2√2y)−1−2√2y),
A=exp(2n log(1+v/r)+9v−(h/2)(exp(2√2p)+exp(2√2q)−2)),
v=(p+q)/√2,
E=(1−3exp(−2√2p)/(2V_+))(1−3exp(−2√2q)/(2V_-)),
V_±=πexp(2r±2iτ), |V_±|=√(a²+h²)/2.

The normalization is C₀exp(Φ_*). This exact summand identity is the j=k=1 case of the algebra in L282; no higher theta terms have been replaced by a local error.

The local model proof in L278 requires only r→∞, h≥1 and n/r²=O(h/r) for its Hessian and derivative estimates. Indeed the negative Hessian of log A is the sum of the positive diagonal matrix with entries 4h exp(2√2p), 4h exp(2√2q) and the positive semidefinite matrix all of whose entries are n/(r+v)². Also ∇log A(0)=0. Thus on Q it lies between chI and ChI, giving

|A|≤exp(−ch(p²+q²)),
|A_p|+|A_q|≤Ch(|p|+|q|)exp(−ch(p²+q²)),
|A_pq|≤C[h+h²(p²+q²)]exp(−ch(p²+q²)).                 (1)

These bounds give uniformly bounded rectangular mixed variation: the sum of a corner modulus, the two edge integrals of first derivatives, and the area integral of the mixed derivative is O(1) on every subrectangle. For example, the edge integral of h(|p|+|q|)exp(−ch(p²+q²)) in p is bounded by C(1+√h|q|)exp(−chq²); the area estimate follows by scaling both variables by √h. They also give O(1) bounds when an edge first derivative is replaced by A, or the mixed derivative by A,A_p,A_q, since h≥1.

Use L278's exact real change Y=g(p), Z=g(q), where

g(y)=sgn(y)√((exp(2√2y)−1−2√2y)/4), g'(0)=1.

Its inverse P has bounded derivatives on this fixed interval. The transformed model amplitude B=A(P(Y),P(Z))P'(Y)P'(Z) has bounded rectangular mixed variation by (1) and the chain rule. With R=a^(−2/5), it equals 1+O(R+hR²) on [−R,R]². The central replacement costs O(R³+hR⁴). The Fresnel value and rectangular tail estimates used in L278 then yield

∫∫_Q A exp(if(p)−if(q))dpdq
 =π/(2a)+O(R³+hR⁴+a^(−3/2)/R+a^(−2)/R²).

All constants are uniform here: the tail decomposition uses at most four rectangles, a tail primitive O(1/(aR)), a global primitive O(1/√a), and bounded mixed variation. After multiplication by a, the error is

O(a^(−1/5)+L a^(−3/5)+a^(−1/10)+a^(−1/5))=o(1).     (2)

It remains to retain E. On Q, E−1 and its first and mixed derivatives are O(1/a), since the exponentials have fixed bounded arguments and |V_±|≥a/2. By the product rule and (1), A(E−1) has rectangular mixed variation O(1/a). The primitives of exp(±if) on any subinterval of Q are O(1/√a), as proved directly by monotone-phase integration by parts in L282. Its rectangular integration identity therefore bounds the signed correction by O(1/a²). Thus the exact principal patch J_11 satisfies

J_11=C₀exp(Φ_*)[π/(2a)+o(1/a)].                       (3)

Next consider D={s+x>r/4,s−x>r/4}. We recheck the global bounds of L282 and the first bound of L283, rather than apply their logarithmic-h conclusions directly. For indices j,k their coordinates have s=r−log(jk)/2+(p+q)/√2>r/4 and the exact normalized amplitude H_jk=G_jk E_jk obeys

|G_jk|≤w_jk g_h(p)g_h(q),
w_jk=(jk)^(4−h),
g_h(y)=exp(−(h/2)(exp(2√2y)−1−2√2y)).

This follows solely from log(s/r)≤(s−r)/r and n/r=h−9/2. The integrals and suprema of (1+exp(2√2y))g_h(y) are uniformly bounded for h≥1. On D, n/s≤4h and n/s²≤16h/r. The exact lower-degree factors and their first and mixed derivatives are bounded because their inverse theta arguments are at most exp(−r/2)/(πj²) and exp(−r/2)/(πk²). Differentiating G_jk therefore gives the same rectangular mixed-variation bound Ch²w_jk as in L282, for all r≥1,h≥9. None of these bounds requires h≥L.

The phase is f(p)−f(q) plus a constant of modulus one. Its primitives are O(a^(−1/2)) on every interval, and O(a^(−1)) on intervals outside [−ε,ε]. Partitioning D outside each summand's square into at most four rectangles and applying the variation bound gives

Σ_jk |K_jk|≤Cexp(Φ_*)h²/a^(3/2).                      (4)

Here Σ_jk w_jk≤4 for h≥6. The same envelope is absolutely integrable and summable, so termwise integration of the entire theta product on D is justified. The clipped squares are rectangles. Using two O(a^(−1/2)) primitives on each and the elementary estimate Σ_(jk>1)w_jk≤C2^(−h) gives

Σ_(jk>1)|C_jk|≤Cexp(Φ_*)h²2^(−h)/a.                  (5)

This is the first estimate of L283 with its proof checked on the larger parameter domain; its comparison with restricted full patches is unnecessary. The principal square lies inside D eventually, so C_11=J_11. Equations (3)–(5) evaluate the integral over D with relative errors o(1), h²/√a and h²2^(−h). Both displayed errors tend to zero uniformly for H(a)≤h≤L.

Finally the absolute geometric estimates underlying L279 and L284 require only r→∞, h≥9 and n=r(h−9/2), as their proofs show. For specificity, with m=max(|s|,|x|), l=min(|s|,|x|), d=m−r, their strip envelope satisfies

F_env−Φ_*≤−h(exp(2d)−1−2d).

On |d|≥r/4, splitting this exponential in half supplies exp(−chr), leaving an integrable first moment O(r+1). On |d|<r/4 within the small-argument set m−l≤r/4, the transverse exponential supplies exp(−(h/4)exp(r/2)). In the remaining mixed-sign sector, |s|=l and l/m≤4/5, so retaining (l/m)^(2n) gives exp(−rh log(5/4)). Restoring the strip factor δ^(−5) and finite quadrant multiplicities, the union of the small-argument set and the mixed-sign sectors has absolute integral bounded by

Cδ^(−5)(r+1)²exp(Φ_*−chr).                            (6)

The constants c,C are absolute and independent of h,a. Dividing (6) by exp(Φ_*)/a bounds its ratio by

C a^6 h^(−5)(r+1)²exp(−chr).

Its logarithm is at most (6−cH(a)/3)L+O(log L), which tends to −∞. This verifies the actual required scale even for arbitrarily slowly diverging H. It does not assert that (6) suffices for bounded h.

Outside this union the only sectors are D and its reflection in s. Exact evenness of k gives F(−s,x)=F(s,x); hence the reflected sector has precisely the same integral. Together (3)–(6) prove the asserted global factor π/a. The positive normalization from L269 gives the Laguerre sign.

For the combined index statement, n(h)=r(h)(h−9/2) is strictly increasing for h>9/2, since r>0 and r'(h)>0. The new interval ends at h=L exactly where L286 begins; hence rounding the lower endpoint upward leaves no missing integer. L286 reaches Ca for each fixed C. The asymptotic lower endpoint and the sequence formulation follow from r~L/2 in the new range. Evenness extends the statements to negative real a. ∎

The error h²2^(−h) tends to zero here but is not a little-o in a when h is fixed. Nor have the small-argument strip losses been controlled at every bounded h. This result therefore does not settle L266's required signs from index 1 or give an RH candidate.

**Mathlib.** Full statement: not checked. Supporting Fresnel integration, smooth real changes of variables, rectangle integration by parts, theta expansions and absolute-series Fubini: not checked. No library match is claimed. The cited lemmas supply supporting identities and estimates; their narrower asymptotic conclusions are not invoked outside their stated ranges. The parameter extensions and exact-factor signed correction are proved above.
