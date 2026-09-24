# Lemma 286: real-phase interpolation of the global sign bands

**Hypotheses.** Use the theta integral I_n(a), saddle parameters r,h,τ,Φ_*, and matrix B of L269. Put L=log a, let a→+∞, and let n≥1 be an integer with

L≤h≤2√a L².

**Conclusion.** Uniformly in this range,

I_n(a)=(8π²)² exp(Φ_*)[π/a+o(1/a)]
       =(8π²)² exp(Φ_*) 4π/√(det B)·(1+o(1)).

In combination with L277, for every fixed C>0, D_n(Ξ;a)>0 eventually for every integer

ceil(r(L)(L−9/2))≤n≤Ca,
r(h)=(1/2)log(a/(2π))+(1/4)log(1+h²/a²).

Evenness supplies the same assertion for |a|→∞. The lower endpoint is asymptotic to (log a)²/2 and diverges.

**Proof.** Throughout this larger range,

r~L/2, n=r(h−9/2), n/r²=O(h/r), h/a=o(1),
δ=h/√(a²+h²), δ^(−5)≤C(a/h)^5,
det B=16a²+16h²+8hn/r²=16a²(1+o(1)).                 (1)

The contour identity in L269 is parameterwise and applies without its proportional-index restriction. Write F(s,x) for its shifted integrand, including exp(−2aτ). All integrals below use positive area measure. Set ε=1/100 and let Q be the square |p|,|q|≤ε, where p=(s−r+x)/√2, q=(s−r−x)/√2.

We first extend the local proof, not the low-h exterior assertion, of L278. Its real phase is exactly A(p,q)exp(if(p)−if(q)), with

f(y)=−(a/2)(exp(2√2y)−1−2√2y),
log A=2n log(1+v/r)+9v−(h/2)(exp(2√2p)+exp(2√2q)−2),
v=(p+q)/√2.

The gradient of log A vanishes at zero. Its negative Hessian is the positive diagonal matrix with entries 4h exp(2√2p),4h exp(2√2q), plus the positive semidefinite matrix whose entries are n/(r+v)². By (1), its eigenvalues on Q lie between ch and Ch with constants independent of h in our range. Consequently all four Gaussian amplitude bounds (1) in L278 still hold. Integrating those bounds after scaling by √h gives the same uniformly bounded mixed variation on every subrectangle. The fixed real change Y=g(p), Z=g(q) defined there has bounded inverse derivatives independent of all parameters, and its transformed amplitude B has the same bounded variation.

With R=a^(−2/5), the central replacement B=1 costs O(R³+hR⁴). The exact Fresnel value and rectangular tail argument of L278 give normalized relative error

O(aR³+ahR⁴+1/(√a R)+1/(aR²))
 =O(a^(−1/5)+2a^(−1/10)L²+a^(−1/10)+a^(−1/5))=o(1). (2)

These estimates do not require h=O(L). On Q, |πexp(2z)| is comparable to a, and its real part is at least (h/2)exp(−2√2ε). The exact theta-series estimate therefore still has relative error O(a^(−1)+exp(−γh)), with γ=(3/2)exp(−2√2ε)>1. The model modulus integral is O(1/h) by the Gaussian bounds. Its relative error at the required 1/a scale is

O(1/h+a exp(−γh)/h)≤O(1/L+a^(1−γ)/L)=o(1).           (3)

Thus, writing C₀=(8π²)², the actual-kernel patch is

J=∫∫_Q F=C₀exp(Φ_*)[π/(2a)+o(1/a)]                  (4)

uniformly throughout the asserted range.

For the global complement, split at H=a^(1/8). First suppose L≤h≤H. We recheck the estimates behind L279 and L282–L284, whose stated conclusions have narrower hypotheses. For D={s+x>r/4,s−x>r/4}, the exact index-dependent coordinate rectangle, phase, and amplitude H_jk of L282 are unchanged. Its logarithmic inequality uses only n/r=h−9/2 and yields

|G_jk|≤w_jk g_h(p)g_h(q),
w_jk=(jk)^(4−h), g_h(y)=exp(−h(exp(2√2y)−1−2√2y)/2).

On D, s>r/4, so n/s≤4h and n/s²≤16h/r. The exact lower-degree theta factors and their first and mixed derivatives stay uniformly bounded since their inverse arguments are bounded by exp(−r/2)/(πj²) and exp(−r/2)/(πk²). The integrals of (1+exp(2√2y))g_h(y) and their suprema are uniformly bounded for h≥1. These are precisely the ingredients of L282's rectangular mixed-variation bound Ch²w_jk. The phase primitives are O(a^(−1/2)) on every real interval and O(a^(−1)) on intervals outside [−ε,ε]; neither bound involves h. Its rectangle integration identity consequently gives, also in our range,

Σ_jk |K_jk|≤C exp(Φ_*)h²/a^(3/2),                    (5)

where K_jk is the signed integral outside that summand's stationary square. Absolute integral summability follows from the same envelope and Σw_jk≤4 for h≥6, so this is a legitimate summand partition.

For clipped stationary rectangles the two primitive bounds are both O(a^(−1/2)). The first estimate of L283, whose proof uses just this same variation bound and Σ_(jk>1)w_jk≤C2^(−h), therefore gives

Σ_(jk>1)|C_jk|≤C exp(Φ_*)h²2^(−h)/a.                 (6)

The principal clipped square is exactly Q eventually, since r−√2ε>r/4. Its exact first-summand integral J_11 differs from J by at most C exp(Φ_*)[a^(−1)+exp(−γh)]/h, by the same model comparison as (3). Thus (4)–(6) evaluate D at the desired precision: h²/√a≤a^(−1/4)→0, while sup_(h≥L)h²2^(−h)→0.

For completeness, the geometric estimates of L279 and L284 also extend. Their proofs require r→∞, h≥9, n=r(h−9/2), and the strip envelope (2) of L269. Splitting |m−r|≥r/4 supplies exp(−c h r); in the remaining small-argument region m−l≤r/4 the transverse exponential is at most exp(−(h/4)exp(r/2)). In the remaining mixed sector l/m≤4/5 retains the saving (4/5)^(2n)≤exp(−rh log(5/4)). Their integrated bounds are therefore still

Cδ^(−5)(r+1)²exp(Φ_*−c h r).                         (7)

Relative to exp(Φ_*)/a, (7) is at most Ca^6h^(−5)(r+1)²exp(−c h r)=o(1), since r≥L/3 and h≥L. Outside the small-argument set the two same-sign sectors and the mixed sectors exhaust the plane. Exact evenness gives F(−s,x)=F(s,x), so the negative same-sign sector equals D. This proves the global assertion for L≤h≤H, without using an absolute bound on the low-h same-sign complement.

Now suppose H≤h≤2√a L². Use instead the fixed-square exterior estimate derived in L269 (7)–(10). To verify its applicability, take the fixed u,x radius e=ε/√2, where u=s−r. This square lies inside Q. We have h≥1, r→∞, e<1, and e/(r−e)≤exp(−1/2) eventually. In that derivation the radial split supplies exp(−c h e²), the transverse split has exp(2(m−r))≥exp(−2e), and the swapped box retains (l/m)^(2n)≤exp(−n). Thus no shrinking-radius or proportional-index hypothesis is necessary for that bound, and the exterior of Q and its s-reflection has absolute integral at most

Cδ^(−5)exp(Φ_*)[(r+1)²exp(−c h e²)+exp(−n)].          (8)

Here n=r(h−9/2)≥c'LH. Dividing (8) by exp(Φ_*)/a and using δ^(−5)≤Ca^5 gives an upper bound

Ca^6[(L+1)²exp(−c e²a^(1/8))+exp(−c'La^(1/8))]→0.   (9)

The two disjoint patches contribute equally by exact reflection in s. Equations (4) and (9) complete the global asymptotic in this second range. Uniformity in both pieces proves the first conclusion. Equation (1) gives its determinant form. Reality of I_n and the positive normalization D_n(Ξ;a)=2^(2n−1)I_n(a)/(2n)! give strict positivity.

Finally n(h)=r(h)(h−9/2) is strictly increasing for h≥L eventually. The exact lower endpoint is therefore the one stated. At h=2√a L², it equals (1+o(1))√a L³. For overlap it is safer to compare in h: L277 already applies on √a L²≤h≤a^(3/4)L³, overlapping our interval. Moreover the integer ceil(√a L³) has h=(2+o(1))√a L² and hence lies strictly inside L277's interval eventually, even if it lies just above our upper endpoint. Monotonicity and this overlapping h interval leave no missing integer before the combined n-range of L277 starts. That combined range extends to Ca for every fixed C>0. Evenness gives the assertion at negative a. ∎

The intermediate sign gap is closed asymptotically. L266 still needs every index starting at 1, including the diverging set below this lower endpoint, and all bounded exterior heights. No complete RH candidate follows.

**Mathlib.** Full statement: not checked. Supporting real changes of variables, Fresnel integrals, rectangular integration by parts, absolutely summable integration, and uniform asymptotics: not checked. No library match is claimed. The existing local, sector, and global-envelope proofs cited above are extended only after checking their parameter-dependent bounds; L277 supplies the previously established high-index range.
