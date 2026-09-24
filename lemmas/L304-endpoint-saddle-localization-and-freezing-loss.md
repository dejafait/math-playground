# Lemma 304: endpoint Mellin localization and absolute freezing loss

**Hypotheses.** Let r tend to infinity through real values, put c=1/2+1/r, σ=1+1/r, and retain S_r(a)=Z_r(a;c) and W_r from L303. For real v define

K_r(v)=Γ(r+1)(2r)^(−r) exp(2r(c+iv))(c+iv)^(−r−1)/(2π),

F_r(v,a)=ζ(σ+i(a+v))ζ(σ+i(v−a)),
B_r(a)=F_r(0,a)=|ζ(σ+ia)|².

**Conclusion.** The following statements hold uniformly in real a:

∫_ℝ K_r(v)dv=1,  ∫_ℝ |K_r(v)|dv=O(1),

∫_(|v|>log(r)/sqrt(r)) |K_r(v)F_r(v,a)|dv
 =O(r²exp(−(log r)²/8)).                                      (1)

Nevertheless the exact frozen-factor remainder is

S_r(a)−B_r(a)=Σ_(j,k≥1) [W_r(j,k)−(jk)^(−σ)]exp(ia log(k/j)),  (2)

and its coefficientwise absolute certificate satisfies

A_r:=Σ_(j,k≥1) |W_r(j,k)−(jk)^(−σ)|=r²+O(r).                 (3)

At a=0 the signed difference is −r²+O(r). Thus localization alone does not justify a uniform-in-a small freezing error. The guaranteed elementary square lower bound is B_r(a)≥(r+1)^(−2); (3) does not yield an error smaller than this bound. These conclusions do not give a lower bound on the actual remainder at L302's heights a_n, or refute a signed arithmetic comparison there.

**Proof.** L298's scalar inversion formula at t=2r gives ∫K_r=1; this use is also the j=k=1 term of L303's inversion. Absolute convergence holds since r>0. Write

|K_r(v)|=P_r(1+(v/c)²)^(−(r+1)/2),
P_r=Γ(r+1)(2r)^(−r)exp(2rc)c^(−r−1)/(2π).

Stirling's formula Γ(r+1)=sqrt(2πr)(r/e)^r(1+O(1/r)) gives

P_r=sqrt(r)/(c sqrt(2π)) · exp(2−r log(1+2/r))(1+O(1/r))
    =O(sqrt(r)).

Here c lies between 1/2 and 1 for r≥2, and the displayed exponential is bounded (indeed tends to one). On |v|≤c, the elementary inequality log(1+x²)≥x²/2 for |x|≤1 gives

|K_r(v)|≤C sqrt(r) exp(−r v²/4).

For |v|>c, put x=v/c and split the power as

(1+x²)^(−(r+1)/2)
 ≤2^(−r/4)(1+x²)^(−r/4−1/2)
 ≤2^(−r/4)(1+x²)^(−2)  (r≥6).

Its integral is O(sqrt(r)2^(−r/4)). The inner Gaussian integral is O(1), proving the asserted bounded absolute mass. For V=log(r)/sqrt(r)<c, splitting exp(−rv²/4) into two equal exponential factors bounds its integral over V<|v|≤c by C exp(−rV²/8). The outer exponential tail can be absorbed into this bound for large r. Hence

∫_(|v|>V) |K_r(v)|dv=O(exp(−(log r)²/8)).

Absolute Dirichlet convergence and the decreasing integral comparison give

|F_r(v,a)|≤ζ(σ)²,  r≤ζ(1+1/r)≤r+1.

This proves (1). It is a superpolynomial tail estimate, not an exponentially small error at L302's scale.

Both Dirichlet factors in B_r(a) are absolutely convergent. Expanding their product and subtracting L303's exact finite sum proves (2). In particular this remainder is exactly what subtracting F_r(0,a) under the normalized Mellin integral produces; no Gaussian approximation has been made.

Let M_r^full=Σ W_r(j,k). L297 proves M_r^full=4r+o(r), including the full unrestricted sum in its proof. For any nonnegative numbers w,b, b−w≤|w−b|≤b+w. Summing these inequalities yields

ζ(σ)²−M_r^full≤A_r≤ζ(σ)²+M_r^full.

Since ζ(σ)²=r²+O(r) and M_r^full=O(r), this proves (3). At a=0 all phases in (2) equal one, so S_r(0)−B_r(0)=M_r^full−ζ(σ)²=−r²+O(r). This is a test of a uniform freezing assertion, not a test at the prescribed growing heights.

For completeness, the absolutely convergent Euler product at σ>1 has reciprocal Dirichlet expansion 1/ζ(s)=Σ μ(m)m^(−s), with |μ(m)|≤1. Therefore |1/ζ(σ+ia)|≤ζ(σ)≤r+1, and B_r(a)≥(r+1)^(−2). The sufficient comparison for a sign would require |S_r(a_n)−B_r(a_n)|<B_r(a_n) with a surplus exceeding the sector error. The bound (3), used by triangle inequality in (2), is of order r² rather than o(r^(−2)); its ratio to the guaranteed square lower bound is of order r⁴. Even an o(1) remainder is not obtained this way. Also r²exp(−(log r)²/8) is a larger scale than (1+r)²exp(−r/256), although a proved polynomial positive margin could tolerate such a tail. These are failures of the stated certificates, not estimates from below for the actual signed error at a_n. ∎

The saddle width shrinks, but the arithmetic factor depends on r as well as a; it cannot be frozen solely from the kernel's localization. A comparison retaining cancellation between arithmetic phases is still possible in principle. No endpoint Laguerre positivity, additional global sign range, or RH candidate follows.

**Mathlib.** Full statement: not checked. Supporting Stirling asymptotics, gamma/Fourier inversion, the absolutely convergent Euler product and reciprocal Möbius series: not checked. No library match is claimed. The named standard Stirling formula and absolutely convergent Euler product are used only in their stated classical domains; scalar inversion is supplied by L298, the exact full sum by L303, and the full weight mass by L297. All localization and coefficient-error estimates are proved above.
