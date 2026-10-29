# L127 — Global exact approximants preserve reconstructed value data

## Hypotheses

Work conditionally in the initial-Theta-data and LGP-Gaussian log-theta-lattice situation of IUT III, Theorem 3.11. This is an audit of the bounded finite-volume part of §3.10(Stp5) of *Essential Logical Structure*, not a verification of Theorem 3.11 or its applicability to a constructed example.

1. Fix the original holomorphic tensor packets, place labels, packet/procession weights, integral reference structures and ordered global degree line \(M\). Identify normalized global log-volumes with elements of this one line once and for all. The ordering is not reversed, and no independently chosen positive rescaling is allowed on either side of a comparison.
2. Fix the conversion constants \(r_v,r'_v\) of IUT III, Remark 2.4.2(ii), including \(r'_v=-r_v/\sum_{w\in\mathbb V^{\mathrm{bad}}}r_w<0\). The denominator is the source's fixed positive finite denominator. These constants retain the original initial data; they are not recomputed from an approximant's local measures.
3. Let \(\mathscr P\) be a collection of global direct-product regions in the finite-volume domain of Remark 3.9.5(iv)(Xi2), with the global compatibility hypotheses of Proposition 3.9(iii). In particular, the local regions are in the indicated local domains, and their normalized log-volumes vanish away from finitely many rational places. Every \(P\in\mathscr P\) lies componentwise in a fixed finite output hull \(H_*\), and its global normalized parameter \(\eta(P)\in M\) is finite and strictly negative. The individual hulls \(\varphi(P)\) and \(H_*\) are taken relative to those same holomorphic structures. This statement does not extend the exact-approximant assertion to arbitrary measurable sets outside its cited domain.
4. For each \(P\), use all the global exact hull-approximants supplied by (Xi2): write \(\Xi_{\mathrm{gl}}(P)\) for their collection, with \(H\subseteq\varphi(P)\subseteq H_*\) componentwise and \(\eta(H)=\eta(P)\). Local equality of log-volumes at every place is not required. Import the nonemptiness of this global collection from (Xi2), rather than assuming that every local \(\Xi(P_v)\) is nonempty.
5. When using line bundles, keep the weighted determinant of Remark 3.9.5(vii)(Ob3), including the inverse determinant of the integral reference structure, its common positive integer exponent \(M_{\det}\), and the prescribed degree normalization. Here \(M_{\det}\) is an integer, distinct from the ordered line \(M\). Keep the tensor-power-twist qualifications of (Ob4). The fixed comparison target is the determinant of \(H_*\), not a determinant target selected anew for each approximant.

The distinguished q-pilot and its parameter \(A\) remain separate data. Neither \(\eta(P)=A\) nor q-pilot membership in the output family is a hypothesis.

## Conclusion

For each \(P\in\mathscr P\) and \(H\in\Xi_{\mathrm{gl}}(P)\), the **reconstructed** value-group rigidifications of Remark 2.4.2(v)–(vi), obtained from \((M,\eta(P))\) and \((M,\eta(H))\) with the fixed conversion constants, agree. The common container, labeled primes, local divisor monoids and their reconstructed localization data agree up to the identifications furnished by that reconstruction. At the explicit monoid-data level used to perform the reconstruction, the data are identical.

The collection of these reconstructed rigidifications is unchanged when every \(P\) is replaced by all its permitted global exact approximants. Applying the normalized weighted/reference determinant gives the same output parameter and hence the same conclusion. This is a conditional replay of a source claim, not a result beyond the cited sources.

This conclusion neither identifies the actual relative objects of (cQ3) nor proves preservation of their marking orbits, unit/Galois data, localization isomorphisms as marked objects, or distinguished q-gluing. It does not verify the full logical-conjunction/disjunction assertion of Stp5, Stp7 symmetrization, or finite \(B\ge A\).

## Proof

### Cited reconstruction and its exact specialization

Use the following primary inputs without reproof:

- Mochizuki, [*The Geometry of Frobenioids I*, June 2008](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf), Theorem 5.1(i), pp.96–97; Proposition 5.3, p.103; Example 6.3 and Theorem 6.4(i)–(ii), pp.112–116. Applied to the source's arithmetic global realification, these give the ordered degree line used in IUT III, Remark 2.4.2(v). The precise hypotheses and correction qualifications are retained in `foundations/03-realification-and-arithmetic-degree.md` and the September 26 assessment. An arbitrary equivalence of realifications need only act by a positive factor; no scale-one conclusion is imported here.
- Mochizuki, [*Inter-universal Teichmüller Theory III*, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf), Remark 2.4.2(ii)–(vi), pp.89–91: the explicit reconstruction from the degree line, conversion constants and negative pilot parameter. Its identified local divisor monoids are the constant monoids appearing in part (v), not the entire local Frobenioids or their unit groups.
- IUT III, Proposition 3.9(i),(iii), pp.115–117, and Remark 3.9.5(iii)–(iv)(Xi2), p.128: the normalized global volume and global exact-approximant existence under the hypotheses above. No general Frobenioid or approximation theorem is reproved in this audit.

Fix copies \(M_v\) of \(M\) once. The explicit input data of Remark 2.4.2(iii) are

\[
\mathcal D_0=(M,\{M_v\}_v,\{\rho_v:M_v\longrightarrow M\}_v),
\qquad \rho_v(x)=r'_v x.
\]

The maps \(\rho_v\) reverse order, as in the source. For a finite negative \(\eta\in M\), let \(\eta_v\) be its copy in \(M_v\). Part (iv) uses the submonoids

\[
M'_v(\eta)=
\begin{cases}
\{n\eta_v:n\in\mathbb N\},&v\text{ nonarchimedean},\\
\{x\in M_v:x\le0\},&v\text{ archimedean},
\end{cases}
\qquad \rho'_v(\eta)=\rho_v|_{M'_v(\eta)}.
\]

In particular \(\rho'_v(\eta)(\eta_v)=r'_v\eta>0\). The nonarchimedean monoid has the specified nonzero generator; the ordering on \(M\) is unchanged, and no passage through \(\eta=0\) is made. The archimedean cone is the same for every negative parameter, but the copied pilot element is still specified.

For \(H\in\Xi_{\mathrm{gl}}(P)\), equality \(\eta(H)=\eta(P)\) is equality in the **same** \(M\). Consequently their copied elements \(\eta_v\), their submonoids \(M'_v\), and their restricted maps \(\rho'_v\) coincide at every \(v\). The unrigidified data \(\mathcal D_0\) never changed. Apply precisely the reconstruction of Remark 2.4.2(v): \(\mathcal D_0\) reconstructs the global realified container with its prime labeling, while the further data reconstruct its local divisor monoids and the localization data displayed there. Equal inputs therefore yield the same reconstructed data, with the source's isomorphism qualifications. Part (vi) puts them in the same container. This verifies the announced specialization; it does not reconstruct any unlisted relative marking from a scalar.

### Global family quantifiers and the retained hull

Let \(\mathcal R(\eta)\) denote the reconstructed rigidification, with its fixed ambient data understood. For every pair \((P,H)\) under consideration, the preceding argument proves \(\mathcal R(\eta(H))=\mathcal R(\eta(P))\), in the reconstructed sense just specified. Thus every value-group possibility after replacement occurs before replacement. Conversely, (Xi2) supplies at least one \(H\in\Xi_{\mathrm{gl}}(P)\) for each \(P\), so every possibility before replacement occurs afterwards. This proves equality of the two collections of reconstructed possibilities; it does not assert a bijection of the representing regions, a canonical choice of approximant, or an isomorphism of marked categories.

The use of (Xi2) is global: the archimedean factor belongs to its hypotheses. A failure of exact approximation at one nonarchimedean place does not negate the imported assertion. The original-hull condition remains satisfied, since the permitted approximants lie in \(\varphi(P)\), and hull monotonicity in Remark 3.9.5(ii)(P3), p.127, gives \(\varphi(P)\subseteq H_*\) from \(P\subseteq H_*\). The comparison never replaces this bounded collection by all hulls having a prescribed global volume. The algebraic equality of reconstructed inputs alone would not impose that restriction; it is retained as part of admissibility.

Also, the volume of the **union** or hull of all approximants need not equal the volume of an individual approximant. Remark 3.9.5(iv)(Xi3), pp.129–130, and (vii)(Ob6), pp.134–135, expressly distinguish these quantities. Our two inclusions compare individual reconstructed possibilities, retaining their pairwise equal-volume relation, and never identify the union's volume with \(\eta(P)\). The later family/hull and formal-quotient operations remain separate.

### Determinant normalization

Write \(D(H)=\det^{\otimes M_{\det}}(H)\) for the source's operation, including all the adjustments in (Ob3-1). Its construction uses the weighted determinants of the fixed packet summands, tensored with the inverse weighted determinant of the integral reference structure. Proposition 3.9(iii) and (Ob3-3), pp.132–133, identify its degree, with the prescribed normalization factors, with \(\eta(H)\).

This is the normalized degree assertion from the source, not an assertion that an unnormalized determinant degree equals \(\eta(H)\). In degree notation, tensoring with the fixed inverse reference subtracts the reference degree; positive tensor powers multiply degrees, with the prescribed weights. Since the weights, reference and exponent are common, applying the source's same normalization recovers the same \(\eta(H)=\eta(P)\) in \(M\). Hence the reconstruction above is unaffected by this intermediate representation. The source's possible tensor-power twists in (Ob4-2)–(Ob4-3), pp.133–134, are not asserted to vanish as relative data. Dividing by a known common exponent in the real degree line is not a choice of compatible roots in the local Frobenioids.

### Exactly what this audit does and does not preserve

The audited claim is the preservation of the value-group data **reconstructed from global log-volume**, as stated in Mochizuki, [*Essential Logical Structure of Inter-universal Teichmüller Theory*, March 2024](https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf), §3.10(Stp5)–(Stp6), pp.150–151. IUT III, Remark 3.11.1(iii)(IPL), pp.160–161, uses this reconstruction with explicit sign, product-formula and inverse-system qualifications. We stay in the finite domain and retain the signs and conversion data; no inverse-limit interchange is used.

The equal-global-volume hypothesis does not require equal local volume coordinates. Those coordinates are not the \(\eta_v\) above: each \(\eta_v\) is a copy of the **global** parameter in a prescribed model. Accordingly, the calculation identifies the model's reconstructed divisor/localization data. It does not identify the original local representatives via maps compatible with their embeddings into the output hull.

In particular, IUT III, Remark 3.9.5(ix)(cQ3), pp.141–142, specifies additional data: local objects with structure-poly-morphisms to \(D(H_*)\), their compatible arrows, a global realified object, and localization isomorphisms to the realified local objects. The proof above supplies neither those arrows nor preservation of their orbits or their relation to the fixed q-pilot. The reconstruction's localization data and these localization isomorphisms of **actual relative objects** must not be conflated. No extra global structure arrow to \(D(H_*)\) is being demanded; (cQ3) does not list one.

Thus the restricted preservation assertion passes this audit. The inference from that assertion to preservation of the algorithm's whole marked relation remains outside what has been verified. The original \(A\) was never equated with any \(\eta(P)\); preservation of an output family's reconstructed parameters cannot put an external prescribed parameter into that family. No essential flaw, complete candidate, or original-hypothesis counterexample follows.

## Mathlib

Full matching coverage for the Frobenioid reconstruction, global hull-approximants and this conditional Stp5 specialization: **not checked**. Supporting arithmetic-degree and ordered-monoid coverage: **not checked**. No claim of absence or formal verification is made.
