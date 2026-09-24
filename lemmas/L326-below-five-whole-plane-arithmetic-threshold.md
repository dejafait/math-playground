# Lemma 326: below-five whole-plane arithmetic threshold

**Hypotheses.** Let n be a positive integer tending to infinity, and put

h=39/8, r=8n/3, p=2n=3r/4,
a=a_n=sqrt(4π²exp(4r)−h²), τ=(1/2)arctan(a/h),
Φ_*=p log r+9r−h−2aτ, C₀=(8π²)².

Use the theta integral I_n(a) and Laguerre coefficient D_n(Ξ;a) of L269. Retain exactly L325's finite sum

S_r(a)=Σ_(j,k≥1) W_r(j,k)exp(ia log(k/j)),
W_r(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))^(3r/4)

when log(jk)<2r, with W_r(j,k)=0 otherwise. Set

E_r=(1+r)²exp(−r/200).

Here S_r denotes the below-five sum with exponent 3r/4, not the endpoint sum with exponent r used in L303–L307. The cutoff is retained, including when exp(2r) is an integer.

**Conclusion.** There are constants C>0 and n₀ such that for n≥n₀,

I_n(a_n)=C₀exp(Φ_*) (π/a_n)[S_r(a_n)+R_n],
R_n is real, |R_n|≤C E_r,                              (1)

and therefore

D_n(Ξ;a_n)=[2^(2n−1)/(2n)!] C₀exp(Φ_*) (π/a_n)
                 ·[S_r(a_n)+R_n].                     (2)

The prefactor is strictly positive. Thus S_r(a_n)>C E_r is a sufficient arithmetic margin for positivity, with C as in (1). Without a value for C, the condition

S_r(a_n)/E_r→+∞                                      (3)

suffices for eventual strict positivity on this sequence. Equivalently the required sufficient asymptotic margin may be written

S_r(a_n)/[(1+n)²exp(−n/75)]→+∞,

or

S_r(a_n)/[(log a_n)²a_n^(−1/400)]→+∞.                 (4)

The error tends to zero additively; no positive arithmetic lower bound, relative asymptotic, or Laguerre sign is proved here. These conditions are sufficient for this error certificate, not necessary conditions for positivity. The result concerns only the displayed height–index pairs; it gives no rounded-index assertion at every height.

**Proof.** The parameters satisfy

2πexp(2r+2iτ)=h+ia_n, n/r+9/2=h, 0<τ<π/4

exactly. In particular all three sector estimates L325, L324 and C294b apply at these same parameters. L269's contour identity is parameterwise: for each fixed n,a_n the even kernel is analytic on the smaller strip of height τ and decays superexponentially in the real argument there. Its contour-shift and absolute-integrability proof consequently applies independently of the proportional-index restriction on its asymptotic conclusion. It gives the whole-plane integral of

F(s,x)=exp(−2a_nτ)s^p k(s+x+iτ)k(s−x−iτ)exp(2ia_nx).

No constant uniform as τ approaches π/4 is required for this exact identity. Uniform asymptotic error bounds will come from the three sector estimates.

Put u=s+x, v=s−x. In the positive quadrant let

D₊={u>r/20,v>r/20},
B₊={u≥0,v≥0,min(u,v)≤r/20}.

Their images D₋ and B₋ under (s,x)↦(−s,x) partition the negative quadrant. Let M₁={u>0,v<0} and M₂={u<0,v>0}. These six regions partition the plane except for null boundaries. Absolute integrability permits this partition before any asymptotic limit. The exact theta series on D₊ and B₊ may also be integrated termwise by the absolute-integrability assertions of L325 and L324; C294b supplies this justification for each mixed sector.

Evenness of the analytic theta kernel gives

k(−s+x+iτ)=k(s−x−iτ),
k(−s−x−iτ)=k(s+x+iτ).

Since p is even, F(−s,x)=F(s,x). The absolute Jacobian of this reflection is one, so the D₋ integral equals the D₊ integral, and likewise for B₋ and B₊. There is no conjugation or additional phase in these identities. Reflection x↦−x instead conjugates F and interchanges the two mixed sectors.

L325 states its interior approximation directly in ds dx:

∫_(D₊) F=C₀exp(Φ_*) π/(2a_n)[S_r(a_n)+ρ_n],
|ρ_n|≤C_D E_r.                                      (5)

Its factor 1/2 already incorporates ds dx=(1/2)du dv. L324 likewise bounds each same-sign boundary integral, with this coordinate factor already included, by

|∫_(B₊)F|=|∫_(B₋)F|
 ≤C_B exp(Φ_*) E_r/a_n.                              (6)

C294b bounds each whole mixed-sector integral by

|∫_(M_i)F|≤C_M exp(Φ_*)exp(−γ₀r)/a_n,
γ₀=(3/4)log 2−1/2>1/54.                             (7)

This estimate also includes its coordinate factor 1/2. Its uniform h interval contains h=39/8; no h>5 conclusion is used at this point.

Adding the six integrals and doubling (5) yields the positive normalization C₀exp(Φ_*)π/a_n. Dividing (6)–(7) by it bounds the remaining normalized error by

|ρ_n|+2C_B E_r/(C₀π)+2C_M exp(−γ₀r)/(C₀π).

Since γ₀>1/54>1/200, exp(−γ₀r)≤exp(−r/200)≤E_r. This proves the bound in (1), with a fixed enlarged C. In particular the two reflected interiors supply π/a_n exactly; neither a second Jacobian nor a second copy of the finite sum is inserted inside the brackets.

For reality, the weights and cutoff are invariant under j↔k, which conjugates every phase, so S_r(a_n) is real. The unshifted integral I_n(a_n) is real because t↦−t swaps its two real kernel factors and conjugates its exponential. Hence R_n, defined by (1), is real as well. L269's exact positive normalization D_n(Ξ;a)=2^(2n−1)I_n(a)/(2n)! now proves (2).

For an explicit comparison of scales, L325's more detailed interior error is bounded by a constant times

(1+r)²exp(r/24)a_n^(−1/10)
 +(1+r)²exp(−r/200)+exp(19r/80)a_n^(−1/2).            (8)

Here a_n/(2πexp(2r))→1. The first and third terms in (8) therefore have exponential decay rates 19/120 and 61/80 in r. Both exceed 1/200, as does the mixed-sector rate. The boundary and clipping terms control the assembled error scale; the growing stationary coefficient mass has already been absorbed in (8). Thus the achieved error is o(1) after the stated normalization, rather than only a small fraction of the absolute coefficient mass.

Finally

r/200=n/75,
log a_n=2r+log(2π)+(1/2)log(1−h²/(4π²exp(4r))).

It follows that

E_r / [(1+n)²exp(−n/75)]→64/9,
E_r / [(log a_n)²a_n^(−1/400)]→(2π)^(1/400)/4.

Both limits are strictly positive, proving the equivalence of the sufficient conditions (3)–(4). Also E_r→0 and n/log a_n→3/16. Equations (1)–(2) give the sign implication directly from S_r+R_n≥S_r−C E_r; no arithmetic positivity has been inserted into the proof. ∎

L325's upper bound Σ_jk W_r(j,k)≤C(1+r)²exp(r/24) does not give a positive lower bound for S_r(a_n). L323's stationary family is retained in this sum; its summed magnitudes cannot be substituted for the signed arithmetic value. Similarly, L296's Euler-product margin requires h−4>1 and is unavailable at h−4=7/8. L302 is an assembly precedent at a different parameter, not an input establishing the missing sign here. Even a proof of (3) would leave the other indices, passage to all heights and the full witness target unresolved. All established sign and zero-exclusion ranges are unchanged; there is no RH candidate.

**Mathlib.** Full statement: not checked. Supporting measurable partitions, reflection changes of variables, finite-sum conjugation, asymptotic exponential comparisons and contour integration: not checked. No full or supporting library match is claimed. The parameterwise contour identity and positive Laguerre normalization come from L269; L325, L324 and C294b provide the three sector estimates. Reflection, error comparison, normalization and the sufficient margin are checked above. No additional external theorem or Mathlib result is invoked.
