# Lemma 302: endpoint whole-plane arithmetic threshold

**Hypotheses.** Let n be a positive integer tending to infinity, r=2n,
a=a_n=sqrt(4π²exp(4r)−25), τ=(1/2)arctan(a/5), and
Φ_*=2n log r+9r−5−2aτ. Use the theta integral I_n(a) and Laguerre coefficient D_n(Ξ;a) of L269. Put C₀=(8π²)² and use the real finite phase sum T_r(a) defined in L297 (as used in L300). Define

E(r,a)=r a^(−1/10)+r exp(−r/32)+(1+r)²a^(−1/2)
       +(1+r)²exp(−r/256)+exp(−(log 2−1/2)r).

**Conclusion.** There are constants C>0 and n₀ such that for n≥n₀,

I_n(a)=C₀ exp(Φ_*) (π/a)[T_r(a)+R_n],
R_n is real,  |R_n|≤C E(r,a).                         (1)

In particular E(r,a)=O((1+r)²exp(−r/256))=o(1). The positive normalization

D_n(Ξ;a)=[2^(2n−1)/(2n)!] C₀exp(Φ_*) (π/a)[T_r(a)+R_n]  (2)

shows exactly where the remaining sign question lies. A sufficient arithmetic bound is T_r(a)>C E(r,a) for the constant in (1). Without knowing that constant, the asymptotic condition T_r(a)/E(r,a)→+∞ suffices; so does

T_r(a)/[(1+r)²exp(−r/256)]→+∞.                       (3)

These are sufficient margins for the recorded error certificate, not necessary conditions for positivity. Neither a positive lower bound nor an endpoint sign is proved here. The statement applies only at the paired heights a_n and indices n, not at a rounded index for every height.

**Proof.** These parameters satisfy 2πexp(2r+2iτ)=5+ia and n/r+9/2=5 exactly. L269's parameterwise contour identity does not require its proportional-index asymptotic: for each fixed n,a, the kernel is analytic on the smaller strip of height τ<π/4 and its decay justifies the shift and absolute integration. Thus I_n(a) is the integral over the whole real (s,x) plane of

F(s,x)=exp(−2aτ)s^(2n)k(s+x+iτ)k(s−x−iτ)exp(2iax).

Put u=s+x and v=s−x. Partition the positive quadrant into D₊={u>r/4,v>r/4} and S₊={u≥0,v≥0,min(u,v)≤r/4}. Their images under (s,x)↦(−s,x) partition the negative quadrant into D₋ and S₋. The other two regions are M₁={u>0,v<0} and M₂={u<0,v>0}. These six regions exhaust the plane except null boundaries.

Evenness of k gives k(−s+x+iτ)=k(s−x−iτ) and k(−s−x−iτ)=k(s+x+iτ). The even integer power of s therefore proves F(−s,x)=F(s,x). Both same-sign pieces double with identical integrals, not with an extra phase or a conjugation. All these changes of variables preserve positive area measure.

L300 gives

∫_(D₊) F=C₀exp(Φ_*) π/(2a)
 ·[T_r(a)+O(r a^(−1/10)+r exp(−r/32)+(1+r)²a^(−1/2))].

L301 bounds each S-piece by C exp(Φ_*)(1+r)²exp(−r/256)/a. C294a bounds each M-piece by C exp(Φ_*)exp(−(log 2−1/2)r)/a. Their statements already include the Jacobian 1/2 when expressed using u,v; L300 is in ds dx. Consequently doubling D₊ supplies π/a, and no additional Jacobian is inserted. Addition of these estimates proves (1) with a possibly larger constant.

For reality, symmetry of the finite weights under j↔k makes T_r(a) real. In the original real-contour integral defining I_n(a), conjugation is the substitution t↦−t, which swaps the two real kernel factors. Hence I_n(a) is real and so is R_n. The normalization of L269 gives (2) with a strictly positive multiplier.

Finally a/(2πexp(2r))→1. Thus the first and third errors have exponential rates 1/5 and 1 in r, respectively. The second has rate 1/32. Also log 2−1/2>1/256: for example integrating 1/t on [1,3/2] and [3/2,2] bounds log 2 below by 1/3+1/4=7/12. Each of these rates exceeds 1/256. Polynomial factors are absorbed by the slower fourth term, proving the simplified error estimate. The sign implications now follow directly from T_r+R_n≥T_r−C E. No lower bound for T_r has entered the proof. ∎

L297's absolute mass O(r) and negative principal minor supply neither (3) nor its negation for the prescribed phase vector. L298's fixed-head expansion cannot be substituted for this growing-index sum. Even endpoint positivity would leave smaller indices, neighborhoods of h=5 at arbitrary heights, and bounded exterior heights outside the result; it would not complete L266 or RH.

**Mathlib.** Full statement: not checked. Supporting measurable partitions, contour substitution, finite-sum conjugation, and exponential comparisons: not checked. No library match is claimed. L269 supplies the parameterwise contour identity and positive Laguerre normalization; L300, L301 and C294a supply the three sector estimates. The reflection, normalization, error comparison and conditional sign transfer are checked above.
