# L128 — one-place realified global-contact comparison

## Hypotheses

Fix conditional initial Theta-data as in Mochizuki, IUT I, Definition 3.1, and a lattice as in IUT III, Definition 1.4 (or its LGP version under Definition 3.8(iii) and Remark 3.8.2). Fix one nonarchimedean place v and one adjacent pair of labels in the same vertical column. Earlier initial-data and lattice constructions are assumed; this lemma does not verify them.

Use the reconstructed background of IUT III, Theorem 1.5(v), with a representative of its D-prime-strip comparison. At the two labels write C_g,C'_g for the reconstructed global realified Frobenioids. These are the copies of the degree-one F_mod arithmetic Frobenioid specified by IUT I, Example 3.5(i),(iii), not arithmetic Frobenioids of K. Let

    F_g : C_g -> C'_g,
    f_v : Phi_g,v -> Phi'_g,v,
    g_v : M_v -> M'_v

be the global equivalence, its prime-v divisor map and the compatible reconstructed local ordered-monoid map. Here M_v and M'_v are the realified local value monoids, and the source's compatibility reads

    rho'_v f_v = g_v rho_v.                                      (1)

The local field bases B_v,B'_v are the finite-connected-cover categories of K_v at their respective labels, supplied by the local D-prime-strip, with the induced equivalence b_v:B_v->B'_v. They are retained in the statement. An abstract isomorphism M_v≅M'_v, without b_v, is not the input.

Let A_v,A'_v be the elementary realified local Frobenioid presentations on these bases with their constant value monoids. Let L_v:C_g->A_v and L'_v:C'_g->A'_v be the source's normalized restrictions of Example 3.5(i), transported to the reconstructed copies by Example 3.5(iii) and IUT II, Corollary 4.6(ii). When using the coproduct presentation, regard these as functors into A_v^⊔ and (A'_v)^⊔. The proof below justifies their singleton images; the ambient completion is not discarded.

At each label use the normalization

    rho_v(log_mod(p_v)) = log_Phi(p_v)/d_v,
    d_v = [K_v:(F_mod)_v],                                      (2)

and its primed version. If identifying the reconstructed global background with the Frobenius-like global category, use the compatible whole-collection identifications of IUT II, Corollary 4.6(ii), with the common positive degree-scaling qualification of III, Theorem 1.5(v). No independently chosen local rescalings, preferred scale or strict vertical Kummer compatibility is assumed.

## Conclusion

The pair (b_v,g_v) induces an equivalence Q_v:A_v->A'_v, hence a componentwise equivalence on coproduct completions. On this one-place realified background there is an invertible natural transformation

    alpha_v : L'_v F_g => Q_v L_v.                               (3)

Thus the global-contact premise in step530 is available on this presentation, conditionally on the cited background reconstruction. The separate step535 conceptual audit validates this known-method specialization with the applicability and all-arrow checks below. It neither provides a functor between the original enhanced local categories nor supplies beta_v, an identification of their retained hull determinants, coherent choices through all shifts/twists, or the formal quotient comparison. It proves no pilot membership, finite B>=A or essential IUT flaw.

## Proof

### Imported constructions and their applicability

Use [IUT I, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf), Example 3.5(i),(iii), pp.84–86, for the global base, normalized restriction and its determination up to isomorphism by rho_v. Definition 5.2(iv)(a)–(f), pp.134–135, requires compatibility of the whole model collection; Remark 5.2.1(ii), p.143, constructs it functorially. In particular the restriction is a functor, not an objectwise identification inferred from equality of numbers. Example 3.5(iii) supplies the D-version of the local monoids and global category. The local group associated with its nonarchimedean D-prime-strip component is the absolute Galois group of the local field. Its comparison gives b_v by transport of finite continuous group actions. This uses the base data as well as the monoid.

Use [IUT II, December 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf), Corollaries 4.5(ii), pp.131–132, and 4.6(ii), pp.137–138, with its proof and Remark 4.6.1, pp.139–140, for the compatible reconstructed global and local data. Use [IUT III, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf), Theorem 1.5(v) and proof, pp.50–51, for their comparison between labels. Equation (1) is the meaning of that isomorphism of collections. Its last compatibility statement is relative to horizontal arrows and common positive-scaling orbits; it is not a theorem asserting strict vertical compatibility of original Frobenius-like units. Choosing representatives for the present realified calculation does not assert that stronger statement.

Use [Frobenioids II, June 2008](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II.pdf), Example 1.1(i)–(ii), pp.7–9, for the elementary local realification; Example 5.6(i)–(iii), pp.62–64, for the coproduct-valued global contact. Its contact monoid must have sufficient type and be fieldwise saturated; the full real half-line used here has those properties. The constant group-like difference and correction qualifications are retained as in the September 26 assessment. We do not apply an integral local equivalence theorem to a unit-group comparison. The elementary presentation is only after realification, with the original local base still present.

The realification invoked here is [Frobenioids I, June 2008](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf), Proposition 5.3, p.103, at the scope already recorded in foundations/03-realification-and-arithmetic-degree.md. It takes the real span of the birational divisor monoid; it does not declare the global principal-divisor span to be the entire global divisor space. In the local model of Frobenioids II, Example 1.1, the relevant span is the full local real value group, which is why that realification is elementary. No reproof of these results or of the underlying anabelian reconstruction is needed. The specialization below checks their functor-level application.

For the local submodels actually used here, the nonzero-image hypothesis in Frobenioids II, Example 1.1(ii), must also be checked; citing only its unrestricted model C_0 is insufficient. At a bad nonarchimedean place, IUT I, Example 3.2(iv), pp.71–72, takes the constant monoid generated by the positive valuation of the specified root of the Tate q-parameter, on the K_v field base. This generator is the divisor of a nonzero element of K_v and remains a nonzero divisor in each finite extension. At a good nonarchimedean place, Example 3.3(i), p.78, uses the constant p_v-generated monoid and its characteristic splitting; p_v likewise has positive valuation in each finite extension. Thus in both cases the birational image contains a nonzero generator of the local ray. Its real span is the full one-dimensional value group. Proposition 5.3 and the model description in Frobenioids II, Example 1.1(i)–(ii), therefore give the elementary constant-half-line realification on that same field base, with trivial residual units. The theta presentation in IUT I, Example 3.2(v), pp.72–73, is equivalent via product with the specified cover; if it is used, that equivalence is retained, rather than identifying its objects literally with field extensions. These are local applicability checks, not a claim that a global principal-divisor span is full or that the enhanced categories of (cQ3) are elementary.

### The bases and coproduct image

The global base is B(1)^0, equivalent to the one-object, one-arrow category. Denote its object by *. In the group-action presentation, localization is restriction of the singleton trivial action along the homomorphism from the local group to 1. Its restriction remains a singleton and has exactly one orbit. Hence the localization of * is the terminal object t_v of B_v, as a single object in B_v^⊔. Every global object lies over *, so every L_v(G) lies over this singleton component. Every global arrow lies over id_* and localizes over id_t_v. These assertions hold for every global object and arrow, not merely for a chosen reference object.

This uses the coproduct-valued restriction in Example 5.6: a general transitive global action can split into several local orbits, but the particular singleton action cannot. In retaining the K_v field base, restriction from (F_mod)_v to K_v likewise preserves the singleton. We use Example 3.5's specialized normalized restriction, not a direct application of Example 5.6 with G_Kv falsely declared to surject onto G_(F_mod)_v. Nor is the global number field replaced by K. The reciprocal factor in (2) remains part of the divisor map of this specialized restriction.

An equivalence of bases preserves terminal objects. Thus b_v(t_v) and t'_v are terminal and have a unique isomorphism

    tau_v : t'_v -> b_v(t_v).

Its inverse exists by terminality. It is a base-category comparison, not an identification of the local field with (F_mod)_v.

### Local comparison on all objects and arrows

In the elementary Frobenioid presentation, an object is a base object; an arrow is specified by its base arrow, its positive-integer Frobenius degree, and its effective divisor element at the source. This is the elementary construction used in Frobenioids II, Example 1.1(i) (Frobenioids I, Definition 1.1(iii); the constant-monoid law is also displayed in its Introduction, §I1, p.2). For a constant monoid the pullback identifications on that monoid are the constant ones. If (u,n,a):x->y and (w,m,c):y->z, composition, with the rightmost arrow first, is

    (w,m,c) (u,n,a) = (wu, mn, c + m a).                       (2a)

For a nonconstant divisor functor the c term is pulled back along u; here it is unchanged. The identity is (id,1,0). In particular there is no independent unit or object-metric coordinate in this elementary presentation. This assertion is made after applying the cited realification equivalence, not before it.

Define Q_v on objects by b_v. On an arrow with base arrow u, Frobenius degree n and divisor a, let Q_v have base arrow b_v(u), the same degree n and divisor g_v(a). This respects all operations in the composition law: g_v(0)=0, g_v(a+a')=g_v(a)+g_v(a'), and g_v(na)=n g_v(a). Constancy makes it compatible with the pullback maps. Therefore Q_v preserves identities and compositions. A quasi-inverse to b_v and the inverse of g_v give a quasi-inverse to Q_v, with the induced natural comparisons. Componentwise application defines Q_v on the coproduct completion, including its component-index maps; no components are omitted.

This construction uses no units, splitting of a non-realified category, ring isomorphism, theta function or hull marking. These data are outside the elementary realified target. It therefore cannot be used as the missing F_v on the enhanced local category.

### Restriction on arrows and naturality

Take any arrow h:G_1->G_2 in C_g. Write n(h) for its Frobenius degree and delta_v(h) for the v-component of its divisor. On the elementary presentation, the source restriction has the following data:

    L_v(G_i) = t_v,
    L_v(h) = (id_t_v, n(h), rho_v(delta_v(h))).                   (4)

These are precisely the base, tensor-degree and divisor data of normalized restriction; the formula is a presentation of the cited restriction, not a new replacement for it. The global category and its objects have not been collapsed in the domain of L_v. Only their images in the local elementary category are being described. Local realification removes the residual unit data, so there is no extra arrow coordinate in (4).

The isomorphism F_g of reconstructed Frobenioids preserves Frobenius degree and carries the v-divisor through f_v. Prime-label compatibility ensures that no different prime component is selected. Consequently the arrow data of the two composites are

    L'_v(F_g(h)) = (id_t'_v, n(h), rho'_v f_v(delta_v(h))),
    Q_v(L_v(h))  = (id_b_v(t_v), n(h), g_v rho_v(delta_v(h))).    (5)

Their divisor entries coincide by (1). This includes (2): in particular g_v rho_v(log_mod(p_v)) is computed using log_Phi(p_v)/d_v, not using log_Phi(p_v). No assertion that d_v=1 is made. If representatives of the permitted common degree-scaling orbit change, (1) must still hold for the corresponding whole-collection maps; the calculation does not authorize rescaling only one entry of (5).

For every G define alpha_v(G) to be the elementary arrow over tau_v with Frobenius degree 1 and divisor 0. It is invertible: its inverse is the arrow over tau_v^{-1} with degree 1 and divisor 0. For h:G_1->G_2, composition on either side of

    Q_v(L_v(h)) alpha_v(G_1)
       = alpha_v(G_2) L'_v(F_g(h))                              (6)

has the same base arrow tau_v, degree n(h), and the common divisor entry of (5). Since base transport acts trivially on the constant monoid and alpha's divisor is zero, the elementary composition law gives (6) for every h. This proves naturality, including non-linear Frobenius-degree arrows, not only isomorphisms or divisors. It also proves naturality in the singleton image inside the coproduct completion.

More explicitly, put a=g_v rho_v(delta_v(h)). The left-hand composite has divisor a+n(h)0=a, and the right-hand composite has divisor 0+1a=a, by (2a). Their common base arrow is tau_v. No commutativity between a Frobenius-degree arrow and an arbitrary divisor arrow is assumed. An inverse arrow in this presentation must have degree 1 and divisor 0: degrees multiply to 1, while a sum of nonnegative divisors can vanish only when both summands vanish. Thus the chosen components are precisely the invertible lifts of the terminal-base comparison; no unmentioned additive offset is used to absorb a normalization discrepancy. Any discrepancy produced by dropping the reciprocal d_v in (2) cannot be repaired by these components; when d_v=1 that factor of course changes nothing.

Finally, return from the elementary models to the chosen source presentations using their equivalences and the natural identifications of the source restriction. The uniqueness-up-to-isomorphism assertion of IUT I, Example 3.5(i), applies with the retained base functor and normalized rho_v; it identifies the presented restriction with the source one. Whiskering (6) by those equivalences yields (3). Only existence of this natural comparison for the chosen background comparison is claimed. No simultaneous strictification over every allowed choice, twist or log-iterate is deduced.

The objectwise lambda_v of (cQ3) is not rho_v and is not a component of alpha_v. In step530, alpha_v may be used as the first factor in the transported localization isomorphism only when the other displayed comparison factors exist. This proof establishes none of those further factors and does not change the original hull, reference determinant, weights, degree line, refined labels, q-gluing or finite negative output parameters.

### Critical-audit boundary (step535)

The audit checks all five stated cases. The original local field base and its nonzero submodel survive realification; restriction of the global singleton has one local orbit even inside the coproduct completion; the selected reconstructed Frobenioid comparison preserves degree and prime-divisor data with (1); formula (2a) verifies naturality for every degree n>=1; and the source's up-to-isomorphism restriction characterization permits return from this presentation. Here preservation of degree/divisor data uses the specified isomorphism of reconstructed Frobenioids in II 4.6(ii) and III 1.5(v), not an arbitrary equivalence of categories deprived of its Frobenioid structure. Likewise the base equivalence comes from the retained D-prime-strip representative, not from a real-monoid isomorphism. Compatible whole-collection choices are required throughout. No assertion of preferred choices, vertical Kummer compatibility of original units, all-iterate coherence or an enhanced beta_v is added. The audit verifies this conditional source application; it does not independently verify the cited reconstruction theorems or the initial Theta-data.

## Mathlib

Full matching theorem for these realified Frobenioids and normalized global-contact functors: **not checked**. Supporting elementary category, equivalence and natural-transformation constructions: **not checked**. No absence or formal verification is claimed. The result is a conditional application of the cited constructions, not mathematics claimed to go beyond the checked literature.
