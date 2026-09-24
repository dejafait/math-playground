# Lemma 245: an explicit large-tilt first-sign bound

**Hypotheses.** Use the whole-line actual theta tilt Z(r), m(r), v(r) of L244, and G of L242. Let r≥100 and s=r+1/2.

**Conclusion.** Unconditionally,

m(r)−r v(r)>2/5,   G′(r²)<−1/(10r³).

Thus the required first-sign inequality holds for x≥10000. This does not establish its remaining compact range, a positive Stieltjes representation, or all mixed reciprocal-node forms.

**Proof.** L244 gives Z(r)=2Ξ(ir), m=(log Z)′, v=(log Z)″, and G′(r²)=(rv−m)/(4r³). The definition and reflection identity in L018 give Ξ(ir)=ξ(1/2−r)=ξ(s). The completed-zeta formula in L018, all of whose factors are positive for s>1, therefore yields, with q(s)=log ζ(s) and ψ=(log Γ)′,

m=1/s+1/(s−1)−(log π)/2+ψ(s/2)/2+q′(s),

v=−1/s²−1/(s−1)²+ψ′(s/2)/4+q″(s).

All Dirichlet derivatives used here converge locally uniformly on s>1: on a compact subinterval their summands are bounded by (log n)^j n^(−1−δ), a summable sequence for fixed j and δ>0.

We first bound the gamma part. For t>1, log Γ is convex by Hölder's inequality applied to Euler's positive gamma integral. Differentiation of that integral on compact positive t intervals is justified by integrable powers of |log u|. Integration by parts gives Γ(t)=(t−1)Γ(t−1), so the derivative of the convex function at t is at least its preceding unit secant:

ψ(t)≥log(t−1).

The standard trigamma series is ψ′(t)=Σ_(k≥0)(t+k)^(−2), for t>0; see [NIST DLMF 5.15.1](https://dlmf.nist.gov/5.15.E1). Comparing the decreasing summands after k=0 with their integral gives ψ′(t)≤1/t²+1/t. Consequently the gamma and π contribution to m−rv is at least

(1/2)log((s−2)/(2π))−r/(2s)−r/s²
> (1/2)log((s−2)/(2π))−1/2−1/s.

For s≥100, π<4 and e<3 imply (s−2)/(2π)>98/8>9>e². Thus this lower bound is greater than 49/100. The rational prefactors contribute 1/s+1/(s−1)+r/s²+r/(s−1)²>0.

It remains to control the zeta contribution without continuation of a prime series. Put A_j(s)=Σ_(n≥2)(log n)^j n^(−s). Since ζ(s)≥1,

q′=−A_1/ζ≥−A_1,   q″=A_2/ζ−(A_1/ζ)²≤A_2.

Therefore q′−r q″≥−A_1−r A_2. For n≥2, both log n and (log n)² are at most n². For s≥100, the integral comparison gives

A_1+r A_2≤(1+r)Σ_(n≥2)n^(−s+2)
≤(s+1)[2^(2−s)+2^(3−s)/(s−3)]
≤(s+1)2^(3−s)<1/100.

For the last inequality the positive function (s+1)2^(3−s) is decreasing for s≥100, since its logarithmic derivative is 1/(s+1)−log 2<0 (log 2>1/2 follows by integrating 1/t on [1,2]). At 100 its value is 101/2^97<1/100, as 2^97>2^14=16384>10100. Combining bounds proves m−rv>48/100>2/5 and the claimed bound on G′. ∎

The achieved bound controls precisely the true variance, rather than the inverse-curvature upper bound screened in L244. It settles only the large-parameter portion of one necessary first sign. Even an extension to all x≥0 would not establish the positive measure or all-degree premise required for RH. No zero-location hypothesis enters the calculation.

**Mathlib.** Not checked: coverage of the full statement and supporting gamma, Hölder, and Dirichlet-series differentiation results was not checked. No matching library theorem is asserted. The DLMF trigamma identity above is a supporting classical input, not a match for this lemma. Mathlib reference portal: https://leanprover-community.github.io/mathlib4_docs/
