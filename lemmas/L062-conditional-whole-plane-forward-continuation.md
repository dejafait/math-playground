# Lemma 62: conditional whole-plane forward continuation

**Hypotheses.** Let F(λ,z) be the exact theta family of Lemma 58, and let a<b be finite real numbers. Assume every zero of F(a,·) is real. Suppose there are bounded open sets D_n, n≥1, whose union is C, such that

F(λ,z)≠0 for all λ∈[a,b] and z∈∂D_n, for every n.             (1)

**Conclusion.** Every zero of F(λ,·) is real for λ∈[a,b], and every zero is simple for λ∈(a,b]. In each D_n the finite number of zeros counted with multiplicity is constant in λ. The sets need not be nested; a nested bounded-domain exhaustion is a special case.

A sufficient quantitative condition for (1) is the boundary test proved below. Neither (1) nor initial global reality is established here for the theta family on any specified interval.

## Proof of the exhaustion criterion

For each n the hypotheses of Lemma 61 hold: the domain is bounded and open, its boundary is zero-free throughout the interval, and every initial zero in it is real by the global initial assumption. That lemma gives reality, the finite constant multiplicity count, and simplicity strictly after a within D_n.

Fix any λ∈[a,b] and any zero z of F(λ,·). Since the union of the D_n is C, z belongs to at least one D_n. Apply the corresponding conclusion just obtained. It is real, and if λ>a it is simple. This covers every zero and proves the conclusion. No limit of zero counts or interchange of infinitely many parameter neighborhoods occurs. ∎

## A quantitative sufficient boundary test

Let D be a nonempty bounded open set, and choose R≥0 with closure(D) contained in {|z|≤R}. Put L=max(|a|,|b|), and let C be the positive constant in the kernel bound of Lemma 58. Define

M(L,R)=C∫₀^∞ u² exp(Lu²+(R+9/2)u-π exp(2u))du.

This is finite by the domination proved in Lemma 58. It bounds |F_λ(λ,z)| for λ∈[a,b], |z|≤R. In particular a fully explicit, possibly very coarse, upper bound is

M(L,R) ≤ 2C[U exp(LU²+BU)+exp(-πU)/π],

where B=R+11/2 and U=max(1,3(L+B)/(2π)). This follows by integrating the two-piece majorant of Lemma 58 with derivative orders a=1,b=0 (these derivative-order letters are unrelated to the interval endpoints).

Take a finite set T⊂[a,b] such that each λ∈[a,b] has some t∈T with |λ-t|≤h. Suppose a proved number m>0 satisfies

|F(t,z)|≥m for every t∈T and z∈∂D,

and m>h M(L,R). Then for that nearest t the fundamental theorem of calculus along the real parameter segment gives

|F(λ,z)-F(t,z)|≤|λ-t| M(L,R)≤h M(L,R).

The reverse triangle inequality gives |F(λ,z)|≥m-hM(L,R)>0 throughout [a,b]×∂D. Thus (1) holds for D. An upper bound for M may replace M in the strict inequality. Empty domains may simply be omitted from a covering family.

Conversely, if (1) holds on this D, continuity on the compact set [a,b]×∂D gives a minimum m_*>0. Choosing any finite mesh with covering radius h<m_*/M(L,R) and taking m=m_* satisfies the test. Here M is strictly positive by its integral formula. This converse is an existence statement, not a procedure for proving the lower bound: it assumes the full boundary nonvanishing already. ∎

## What remains missing for the exact theta family

For example, it would suffice to exhibit radii R_n tending to infinity, finite parameter meshes T_n with covering radii h_n, and certified numbers m_n>0 such that

inf{|F(t,z)|: t∈T_n, |z|=R_n} ≥ m_n > h_n M(L,R_n).

The open discs of radii R_n then cover C and the preceding test proves their full-interval boundary nonvanishing. More general bounded domains can be used instead. This is a concrete sufficient condition, not an established estimate or a necessary circular shape for the domains.

The required uniformity is over the whole parameter interval and the whole boundary of each selected domain. There is no requirement that inf_n m_n>0, that a single mesh work for every n, or that M(L,R_n) remain bounded. Each n may have its own lower margin and mesh. Arbitrarily fine meshes do not solve the problem unless the boundary lower bounds are proved and meet the strict inequality. Finite point samples on a circle alone do not prove its infimum bound.

Lemma 58 supplies the finite upper bounds on derivatives on compact sets. Those bounds do not supply positive lower bounds for the oscillatory transform. Likewise, discreteness of the zeros for each fixed λ allows a zero-free circle at that slice but does not show that some large circle stays zero-free for every λ in an interval. Changing the domain with λ is not an application of Lemma 61. No simultaneous sequence of barriers as above has been constructed in this write-up.

Even if the boundary condition were established, global reality at a is a separate assumption. Applying this forward theorem to conclude reality at zero requires a≤0; taking a=0 already assumes the desired reality, and taking a>0 cannot reach zero. The theorem does not remove the downward collision obstruction of Lemma 61. No theta-specific attempt has been disproved here; the result identifies the precise hypotheses for this exhaustion route.

## Verification and formalization obligations

This analytic result needs no numerical certificate. Check the quantifiers: each domain must work for the same entire interval; each zero is covered at its own fixed parameter; simplicity excludes only the initial endpoint. The derivative test uses a real parameter segment contained in [a,b] and a bound valid on the full spatial boundary. Compactness yields a positive minimum only after nonvanishing is assumed or proved.

Formalization would require applying Lemma 61 to each member of a covering family, the covering argument for arbitrary zeros, the integral derivative bound from Lemma 58, the fundamental theorem of calculus and reverse triangle inequality, and the extreme-value theorem on the parameter-boundary product. No infinite zero count is declared finite, and no theta boundary certificate or initial real configuration is a proved input.
