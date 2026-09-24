# Lemma 271: integrated Gaussian corrections lower the saddle threshold

**Hypotheses.** Use the actual-theta integral I_n(a) and saddle quantities r,h,τ,Φ_*,B of L269. Fix C>0, let a→+∞, set L=log a, and suppose

ceil(a^(3/4)L³)≤n≤Ca.

**Conclusion.** Uniformly in this range,

I_n(a)=(8π²)² exp(Φ_*) (4π/sqrt(det B))(1+o(1)).

In particular D_n(Ξ;a)>0 eventually. The same holds with a replaced by |a|. This lowers the sufficient threshold in L270 but does not cover every index through L266's witness cutoff.

**Proof.** The exact saddle identities and envelope bounds in L269 apply parameterwise. As in the parameter calculation of L270,

r=(1/2)log(a/(2π))+O(L^(−2)),
c a^(3/4)L²≤h=n/r+9/2≤C_1 a/L,
δ^(−1)=sqrt(a²+h²)/h≤C_2 a/h.

These follow directly from n≤Ca, r≥(1/2)log(a/(2π)), and the exact identity r=(1/2)log(a/(2π))+(1/4)log(1+(h/a)²). Set ε=sqrt(ML/h), where M is a fixed large constant. Then ε→0 and aε³→0. Constants below may depend on C,M.

On the positive saddle square |u|,|x|≤ε, with u=s−r, write the phase as

Φ=Φ_*−(u,x)B(u,x)^T/2+P_3+P_4+R_5.

Its cubic and quartic homogeneous parts, obtained by expanding 2n log(r+u)−h e^(2u)cosh(2x)−ia e^(2u)sinh(2x)+9(r+u)+2iax−2aτ, are

P_3=(2n/(3r³)−4h/3)u³−4ia u²x−4h ux²−(4ia/3)x³,

P_4=(−n/(2r⁴)−2h/3)u⁴−(8ia/3)u³x−4h u²x²−(8ia/3)ux³−(2h/3)x⁴.

All fifth derivatives are O(a+n/r⁵)=O(a) on this square, so |R_5|≤C_3 aε⁵. Taylor's theorem for the exponential, using aε³→0, gives the uniform bound

|exp(P_3+P_4+R_5)−1−P_3−P_4−P_3²/2|
 ≤C_4(aε⁵+a²ε⁷+a³ε⁹).                                      (1)

Indeed first removing R_5 costs O(aε⁵); in the quadratic exponential expansion the omitted cross terms are O(a²ε⁷), and the cubic-and-higher remainder is O(a³ε⁹). This reasoning applies to complex quantities by the absolutely convergent exponential series.

Here is an explicit finite expression for both integrated corrections. Put Δ=det B and

p=4h/Δ, q=−4ia/Δ, t=(4h+2n/r²)/Δ.

For nonnegative integers j,k define

M_(j,k)=j! k! Σ p^α q^β t^γ/(2^(α+γ) α! β! γ!),

where the sum is over nonnegative integers α,β,γ satisfying 2α+β=j and β+2γ=k; an empty sum is zero. If c_i and d_i are the coefficients of u^(3−i)x^i and u^(4−i)x^i in the displayed P_3 and P_4, respectively, the normalized correction is exactly

Q=Σ_(i=0)^4 d_i M_(4−i,i)
  +(1/2)Σ_(i,j=0)^3 c_i c_j M_(6−i−j,i+j).                    (2)

To prove this formula without assuming a positive complex measure, integrate the Gaussian with source exp(zu+wx). Successive real Gaussian integrations, or completion of squares followed by analytic continuation in the sources, give

∫∫ exp(−(u,x)B(u,x)^T/2+zu+wx)du dx
 =(2π/sqrt Δ) exp((pz²+2qzw+tw²)/2).

The positive real part of B dominates each derivative on compact source sets, so differentiation under the integral is valid. Comparing coefficients proves the formula for M and (2). It also shows that the whole-plane P_3 integral vanishes; on the symmetric local square it vanishes exactly by (u,x)↦(−u,−x).

Since Δ is comparable to a² and n/r²=O(h), all p,q,t are O(1/a). Thus each moment of total even degree 2m in (2) is O(a^(−m)). All c_i,d_i are O(a). Consequently both the quartic correction and the squared-cubic correction are O(1/a), and Q=O(1/a). This uses the signed Gaussian moments, not its modulus moments. The corrections are real: coefficients of odd powers of x and moments with odd x degree are purely imaginary, so each product in (2) is real.

The Gaussian modulus mass is O(1/h), whereas its signed mass 2π/sqrt Δ is comparable to 1/a. Hence (1), integrated in modulus and divided by signed mass, costs at most

C_5[a²(ML)^(5/2)/h^(7/2)
    +a³(ML)^(7/2)/h^(9/2)
    +a⁴(ML)^(9/2)/h^(11/2)].                                (3)

At h≥c a^(3/4)L² these three quantities are respectively

O(a^(−5/8)L^(−9/2)), O(a^(−3/8)L^(−11/2)), O(a^(−1/8)L^(−13/2)),

and tend to zero. The true kernel divided by the model kernel on this square is 1+O(a^(−1)+exp(−c_6 h)), by the theta-series estimate in L269. Since the phase correction is uniformly small, its additional relative integral error is O(1/h+(a/h)exp(−c_6 h))=o(1).

Replacing the square Gaussian integrals of 1,P_4,P_3² by whole-plane integrals also has negligible relative error. Explicitly, their coefficients are bounded by O(1+a²), their degrees are at most six, and Re((u,x)B(u,x)^T/2)≥2h(u²+x²). Splitting this exponent in half shows that the omitted polynomial-weighted tails, after division by signed mass, are at most C_7 a³ exp(−c_7 hε²) for h≥1. Choosing M large makes this o(1).

Finally the entire complementary contour is bounded, using the exact envelope comparison and swapped-box suppression proved in L269, by

C_8 δ^(−5) exp(Φ_*)[(r+1)²exp(−c_8 hε²)+exp(−n)].

Those estimates require only h≥1, ε→0, r→∞, and (ε/(r−ε))^(2n)≤exp(−n), all valid here. Relative to exp(Φ_*)/a this is at most C_9 a^6[L²a^(−c_8 M)+exp(−n)], tending to zero after enlarging fixed M. Thus the polynomial strip cost is absorbed as well. The two reflected saddle squares contribute equally by evenness in s. Combining (1)–(3), the kernel error, and the complementary estimates proves the asymptotic. The original integral is real and its leading term is positive; L269's positive multiplier relating I_n to D_n proves the sign. ∎

The required witness range starts at n=1, while this sufficient threshold still diverges. Neither this result nor its explicit correction formula proves low-index positivity or controls all bounded heights. The last term of (3) requires h≫a^(8/11)(log a)^(9/11) for this particular remainder bound; merely observing that Q is small cannot remove that requirement.

**Mathlib.** Full statement: not checked. Supporting Gaussian generating functions, differentiation under integrals, and uniform theta estimates: not checked. No full library match or named library theorem is claimed. The Gaussian moment identity and changed remainder estimates are proved above; L269 supplies the contour identity and global envelope bounds, with L270 supplying the reusable parameter estimate.
