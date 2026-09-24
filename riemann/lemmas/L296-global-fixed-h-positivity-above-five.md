# Lemma 296: global fixed-h Laguerre positivity above five

**Hypotheses.** Use the theta kernel k, integral I_n(a), Laguerre coefficients D_n(Ξ;a), and parameters r,h,τ,Φ_* of L269. Fix 5<h₀<h₁<∞. Let a→+∞ and let n≥1 be integers with h₀≤h≤h₁. Put C₀=(8π²)². Limits below are uniform over these admissible parameters.

**Conclusion.** The whole-plane integral satisfies

I_n(a)=C₀ exp(Φ_*) (π/a)(|ζ(h−4+ia)|²+o(1)).

Consequently D_n(Ξ;a)>0 eventually on this entire band, also with a replaced by |a|. More explicitly, define

r_a(t)=(1/2)log(a/(2π))+(1/4)log(1+t²/a²),
N_a(t)=r_a(t)(t−9/2).

Every integer ceil(N_a(h₀))≤n≤floor(N_a(h₁)) has this sign for sufficiently large a. The endpoints are asymptotic to ((h_i−9/2)/2)log a. In particular every fixed band c₀ log a≤n≤c₁ log a with 1/4<c₀<c₁<∞ has eventual positivity. No assertion at h=5, h tending to 5, smaller indices, or bounded exterior heights follows.

**Proof.** L269's parameterwise contour identity holds for every a,n under consideration, independently of its proportional-index asymptotic. Write its shifted integrand as

F(s,x)=exp(−2aτ)s^(2n)k(s+x+iτ)k(s−x−iτ)exp(2iax).

For fixed parameters it is absolutely integrable by the contour domination in that identity. Thus measurable partitions and changes of variables below are legitimate before taking asymptotic limits.

Partition the plane by the signs of u=s+x and v=s−x. The axes u=0 or v=0 are null sets. In the positive quadrant define

D₊={u>r/4,v>r/4},
S₊={u≥0,v≥0,min(u,v)≤r/4}.

These partition that quadrant up to boundaries. Let D₋ and S₋ be their images under (s,x)↦(−s,x), and let M₁={u>0,v<0}, M₂={u<0,v>0}. These six regions exhaust the plane up to null sets, with no positive-measure overlaps.

Evenness of the analytic theta kernel gives exactly

k(−s+x+iτ)=k(s−x−iτ),
k(−s−x−iτ)=k(s+x+iτ).

Since (−s)^(2n)=s^(2n), this proves F(−s,x)=F(s,x). The reflection has absolute Jacobian one, so both same-sign integrals are doubled without conjugation or an additional phase. L288 gives

∫_(D₊) F=C₀ exp(Φ_*) (π/(2a))(|ζ(h−4+ia)|²+ε_D),

where sup|ε_D|→0 on the specified band. L295 gives |∫_(S₊)F|=o(exp(Φ_*)/a), and reflection gives the identical bound for S₋. L294 gives |∫_(M_i)F|≤C exp(Φ_*)exp(−γr)/a for i=1,2, where γ=2(h₀−9/2)log 2−1/2>0. Positivity of γ follows already from h₀>5 and log 2>1/2. Since r→∞ uniformly, both bounds are little-o at the required scale. The factor 1/2 for the (u,v) Jacobian is already included in L294 and L295, whereas L288 is stated directly in ds dx. No further coordinate factor is inserted.

Adding the six regions gives the asserted asymptotic with an additive error o(1) in its parentheses. This uses signed integrals; an absolute-integrand little-o bound is neither asserted nor needed. All constants can depend on the fixed compact band, and all three cited estimates are uniform on exactly that band.

L288 proves |ζ(h−4+ia)|²≥ζ(h₀−4)^(−2)=:m>0 using only the absolutely convergent half-plane Re z>1. The integral I_n(a) is real: in its original real contour representation, conjugation is the substitution t↦−t. Hence its normalized real value is at least m−|o(1)|, and is positive once the error is below m/2. The positive normalization from L269,

D_n(Ξ;a)=2^(2n−1)I_n(a)/(2n)!,

preserves this sign. The original integral is even in a by the same substitution t↦−t, proving the negative-height assertion.

Finally the saddle identities imply exactly r=r_a(h) and n=N_a(h). For sufficiently large a, r_a(t)>0 for t≥9/2 and

r_a'(t)=t/(2(a²+t²))>0,
N_a'(t)=r_a(t)+(t−9/2)r_a'(t)>0.

Thus inward rounding of the two exact endpoints gives precisely the stated integer band. Uniformly on fixed compact t-intervals, r_a(t)=(log a)/2−(log(2π))/2+O(a^(−2)), proving the endpoint asymptotics. Given 1/4<c₀<c₁, choose fixed h₀,h₁ with 5<h₀<9/2+2c₀ and h₁>9/2+2c₁. The endpoint asymptotics place the entire requested c-band inside this h-band for large a. This proves the last sign assertion without taking any nonuniform limit toward 5. ∎

The result lowers L290's sufficient fixed-h threshold to 5, strictly and on compact bands only. L266 still requires every 1≤n≤K(a), rather than just logarithmic bands above coefficient 1/4. In particular the low-index and bounded-height gaps remain; this is not an RH candidate. The summable weight (jk)^(4−h) used by L288 and L295 loses its summable majorant at h=5, so substituting that endpoint is unjustified.

**Mathlib.** Full statement: not checked. Supporting measurable partitions, reflection substitutions, uniform asymptotic sign transfer, and monotonicity of the parameter map: not checked. No full or supporting library match is claimed. The contour identity and Laguerre normalization are supplied by L269, the sector main term and zeta lower bound by L288, and the signed complementary estimates by L294 and L295. The assembly and index conversion are proved here.
