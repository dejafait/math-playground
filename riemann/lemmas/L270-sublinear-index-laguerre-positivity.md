# Lemma 270: a sublinear lower threshold for Laguerre positivity

**Hypotheses.** Use the actual theta kernel, I_n(a), r, h, τ, Φ_* and B defined in L269. Fix C>0. Let a→+∞, put L=log a, and let n be an integer satisfying

ceil(a^(4/5)L²)≤n≤Ca.

**Conclusion.** Uniformly in this range,

I_n(a)=(8π²)² exp(Φ_*) (4π/sqrt(det B))(1+o(1)),

and therefore D_n(Ξ;a)>0 for sufficiently large a. The local relative error is O(1/log a); the complementary-contour error is o(1). Evenness supplies the same assertion for |a|→∞. The lower threshold is sublinear but diverges; this is not positivity at all indices or a proof of RH.

**Proof.** We extend the estimates in the proof of L269, not its fixed-ratio uniformity assertion. The saddle equation still gives, uniformly for n≤Ca,

r=(1/2)log(a/(2π))+O(L^(−2)),
h=n/r+9/2,   c_1 a^(4/5)L≤h≤c_2 a/L,
δ=cos(2τ)=h/sqrt(a²+h²),   δ^(−1)≤c_3 a/h.

Here and below constants can depend on C but not on n or a. To verify the first estimate without a lower ratio assumption, first use r≥(1/2)log(a/(2π)) and n≤Ca to obtain h/a=O(1/L), then use the exact identity r=(1/2)log(a/(2π))+(1/4)log(1+(h/a)²). The lower bound for h follows from the assumed lower bound for n and r=O(L). In particular h→∞, h/a→0 and n/r³=O(a). Also sqrt(det B) is comparable to a.

Choose a fixed sufficiently large number M>0 and use the local square radius

ε=sqrt(ML/h)

in place of L269's h^(−2/5). Then ε→0 and hε²=ML. The exact contour shift in L269 is parameterwise valid for each of these saddles. Its global kernel bound (2) has a constant independent of τ. On the two local squares the real parts of the kernel arguments are r+O(ε), so |π exp(2z)| is comparable to a and its real part is comparable to h. Thus the same series estimate gives relative kernel error O(a^(−1)+exp(−c h)). The third phase derivatives there are O(a+n/r³)=O(a). These statements use only the displayed bounds above, not a lower bound on n/a.

Consequently the absolute local Taylor-and-kernel error divided by exp(Φ_*) is at most a constant times

h^(−1)[aε³+a^(−1)+exp(−c h)].

Indeed aε³→0 in the present range, so the Taylor exponential can be bounded by its remainder, and the Gaussian modulus mass is O(1/h), exactly as in L269. Relative to the signed Gaussian mass, comparable to 1/a, this becomes

O(a²(ML)^(3/2)/h^(5/2) + 1/h + (a/h)exp(−c h))=O(L^(−1)).

The first term is O(L^(−1)) because h≥c_1 a^(4/5)L. This bound also implies aε³→0, since h/a is bounded. The omitted Gaussian tails have relative error O((a/h)exp(−c hε²)), which tends to zero after M is chosen large enough.

For completeness, the complementary-contour estimate in L269 is uniform here as well. Its exponent comparison (8) is an exact identity. The inequalities for ψ(d)=exp(2d)−1−2d and cosh(2l)−1 have absolute constants. Once ε≤1 and h≥1, integration of these bounds yields the same bound (10):

C_4 δ^(−5) exp(Φ_*)[(r+1)²exp(−c_4 hε²)+exp(−n)],

where c_4>0 can be chosen independently of a,n,M. The swapped box obeys (ε/(r−ε))^(2n)≤exp(−n) eventually, because ε→0 and r→∞. Its area is bounded. Thus its suppression also does not require n/a bounded below. Dividing the complementary bound by exp(Φ_*)/a gives at most

C_5 a(a/h)^5[(r+1)² a^(−c_4 M)+exp(−n)].

Since h≥1 and r=O(L), this is bounded by C_6 a^6[L²a^(−c_4 M)+exp(−n)]. Choose M with c_4 M>8, enlarging it if needed for the Gaussian tail constant. The first term tends to zero; the second does too because n≥a^(4/5)L². This verifies the complementary bound relative to the signed contribution, despite the polynomial cost of approaching the strip boundary.

The Gaussian identity and the equality of the two reflected contributions are exact as in L269. Their leading sum is positive, yielding the asserted asymptotic. The exact positive multiplier relating I_n to D_n in L269 then gives the sign. ∎

The threshold a^(4/5)(log a)² is sufficient, not optimal. Since it is o(a), for any fixed C greater than π/(2 log 4) this result covers the upper portion of L266's cutoff K(a)~πa/(2 log 4) at large height. It leaves all indices below the threshold and all uncontrolled bounded heights. A negative witness, if one exists at a sufficiently large height, must therefore occur below this threshold; it is not excluded.

**Mathlib.** Full statement: not checked. Supporting contour shifts, Gaussian Fourier integrals, and theta-series bounds: not checked. No library match is claimed. L269 supplies the exact identities and global envelope estimates; the uniform parameter bounds and all changed remainder estimates are proved above.
