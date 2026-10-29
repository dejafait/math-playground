# L123 — fixed numerical cutoffs under the semisimplified log-link

## Hypotheses

Work conditionally in the ambient situation of IUT III, Proposition 3.9, with its actual log-link and initial Theta-data. No existence of full initial data for a notebook witness is asserted. Consider the nonarchimedean part of one column. In the single-field notation, k is a finite extension of Q_p, with additive Haar measure mu_k(O_k)=1. Distinguish the two endpoints by minus and plus superscripts, even when both are written k in the source.

Use Fn, Rss and the integration isomorphism I_M:Rss(M)->R_{>=0} of Remark 3.9.4(i). Fn consists of nonnegative finite-image Borel functions with relatively compact support in the sense specified there. A subset represents its characteristic function. Import the normalized comparison T:Rss(k^-)->Rss(k^+) of Remark 3.9.4(iii), constructed using a compact positive-measure subset of units on which log_k is injective. Its diagram commutes with I_- and I_+. The positive normalization of log-volume is the same under this comparison; put ell_+=c log I_+ and ell_-=c log I_-, c>0, with log(0)=-infinity.

For a tensor packet retain every field factor, the finite-extension tensor powers and all normalization weights in Remark 3.9.4(v). Retain the source reference integral structures. If using a determinant, use the weighted relative determinant of Remark 3.9.5(vii)(Ob3-1), including the inverse reference determinant and the common positive exponent M of (Ob3-2).

Fix a genuine finite hull H as in Remark 3.9.5(i): it has positive finite measure and finite normalized log-volume b. In the single-field calculation H is contained in k^-; the packet version retains all its component hulls. Keep its determinant D=det^{tensor M}(H) and the actual local category of (cQ3), with linear structure poly-morphisms to D, its unit/Galois data, and, if local-global collections are considered, all their localization isomorphisms and compatible arrows. These data are not identified with Rss(H).

## Conclusion

1. The numerical map T preserves the finite cutoff b:

   T({x in Rss(k^-): ell_-(x)<=b})
   = {y in Rss(k^+): ell_+(y)<=b}.

   For a packet the corresponding statement uses the tuple of all factor classes and the source's normalized packet log-volume. This is a statement about numerical classes, not a construction of a hull or marking on the other side.

2. Rss(H), when H is regarded as a measure space, is not that bounded family. Its extension-by-zero map onto Rss(k) is surjective, including arbitrarily large finite log-volumes. By contrast, characteristic functions of measurable subsets contained in H have log-volume at most b.

3. In the audited invocation of Remark 3.9.4 in (Ob9), this numerical comparison is applied after the structured stages (sQ3)/(sQ4). It is not an asserted functor from Rss to the (cQ3) category, or a replacement for its marked comparison. Consequently, failure of such an extra functor, or failure of pointwise logarithmic images to preserve hull containment, does not refute this invocation. The structured comparison and its use for the distinguished pilot are not verified by conclusions 1–2.

This is reproduction and a proof-use audit of the cited formalism, not a new IUT theorem or an essential-flaw demonstration.

## Proof

### Imported comparison and the cutoff test

The source is [Mochizuki, IUT III, May 2020, Remark 3.9.4(i), (iii)–(v), printed pp.120–125](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=120), in the 199-page author text checked on 2026-10-26. Import its integration-class construction and commutative comparison diagram; no independent proof of the underlying p-adic logarithm theorem is claimed. The specialization below is needed to test a *fixed numerical cutoff*, which must not be confused with the semisimplification of the bounded region itself.

Because I_+ and I_- are bijections, their commuting diagram determines T uniquely:

T=I_+^{-1} composed with I_-.

In particular, ell_+(T(x))=ell_-(x), including the zero integration class. This identity proves the forward inclusion in conclusion 1. For the reverse inclusion, given y with ell_+(y)<=b, use x=T^{-1}(y); the same identity gives ell_-(x)<=b. At positive mass the cutoff is equivalently I_-(x)<=exp(b/c), with the zero class included separately. No choice of representative, inverse image under the p-adic logarithm, or hull on the plus side is needed. The value b is carried as a numerical endpoint; it is not forgotten.

For the packet, apply the imported comparison in each of the finitely many field factors and use the tensor-power identifications of Remark 3.9.4(v). Each factor's integration value is unchanged. Therefore their products, the specified extension-degree powers, and the specified weighted sums of their logarithms are unchanged. Applying the identical source normalization gives equality of the packet log-volumes. In the relative determinant description the reference determinant correction is retained on both sides; it cannot be dropped and then reconstructed by declaring an arbitrary determinant degree to be the same number. Division by the fixed positive common exponent M preserves the comparison. This checks compatibility of the numerical calculation, not a transport of the determinant object, its field actions or its marking.

At a bad place, Remark 3.9.4(iv), p.124, additionally retains the q-monoid and its numerical embedding n |-> -n log(q). The identity of numerical coordinates just proved is consistent with this specified embedding. It neither rescales q nor obtains q by applying log_k to a general hull. Nothing in that consistency check proves that the class at n=1 is in the output cutoff.

### Why the bounded hull cannot be substituted for its cutoff

Put m=mu_k(H), so 0<m<infinity. For any real t>=0, the constant function t/m on the measure space H belongs to Fn(H), and its integral is t. Its extension by zero belongs to Fn(k) and has the same integral. Hence the image of Rss(H) in Rss(k) contains the unique class of each mass t. It is all of Rss(k), and its positive classes have unbounded log-volume. This is also the special case of the ample-subspace isomorphism in Remark 3.9.4(i), pp.121–122.

If E is instead a measurable subset of H, then mu_k(E)<=m by monotonicity of measure, so c log(mu_k(E))<=b, with the stated convention at zero. The function t/m above need not be a characteristic function, and scalar multiplication of such a function is not an allowed rescaling of a fixed pilot. Thus these are genuinely different operations: passing to all integration classes of functions on H, retaining only classes below b, and retaining objects marked to D. Neither conclusion 1 nor conclusion 2 identifies any two of the corresponding structured categories.

### Type and necessity check at (Ob9)

An object of the local (cQ3) category has the form (X,[a]), where a:X->D is a linear Frobenioid morphism and [a] is its Aut(D)-orbit. An arrow f between two such objects must respect those orbits under composition. This description, and its local-global enlargement, is the supplied source definition recorded in foundations/02; the meaning of linear is imported there from [Frobenioids I, June 2008, Definition 1.2(i), p.21](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf#page=21). In particular, a linear morphism is not by definition an inclusion between two fixed embedded lattices. No such inclusion is assumed here.

The map T has integration classes as its arguments and values. Neither an X nor a morphism a nor a localization isomorphism is such an argument. The formula T=I_+^{-1}I_- therefore constructs no functor between categories marked to D. Conversely, the cutoff identity above does not require such a functor: it concerns an already specified number b and already specified numerical classes.

The decisive source-order check is [Remark 3.9.5(vii)(Ob9-1), pp.138–139, and (ix)(cQ3)–(cQ4)/(iQ5), pp.141–144](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=138). There the structured comparison precedes the numerical stage; (iQ5) explicitly discards unit/Galois structure. The closed-loop assertion is assigned to the preceding stages. This rules out attributing construction of the marked category to T itself. It does not establish that the preceding assertion is correct.

[Corollary 3.12(xi-d)–(xi-f), pp.183–184](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=183), still requires the particular input pilot to be accounted for by the relative output construction. Its asserted consequence is A in (-infinity,B]. Our cutoff computation only says that an existing numerical inequality is preserved; it supplies no premise placing that particular pilot in the interval. The relative constraint carried through (sQ3)/(sQ4), with the specified intertwinings and formal-quotient qualifications, remains the unresolved source-level premise. An equivalence between arbitrary marked categories is neither proved necessary nor imposed as the only possible way to discharge it.

Thus the proposed objection to *numerical semisimplification for failing to construct markings* is abandoned. No original-hypothesis counterexample, contradiction, full formal-quotient descent, global pilot comparison or finite B>=A follows. The earlier ordinary-model, coordinate and scaled-enclosure stops remain intact.

## Mathlib

Full Rss/Frobenioid comparison: not checked. Supporting integration, order and finite-product facts: not checked. No absence or formal verification is claimed. The result is a source-based specialization with its complete cutoff argument above.
