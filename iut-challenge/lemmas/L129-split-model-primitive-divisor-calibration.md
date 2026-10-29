# L129 — primitive-divisor test for the split enhanced model

## Hypotheses

Fix one bad nonarchimedean place and one adjacent vertical pair as in L128, conditionally on initial Theta-data and the stated lattice. Retain its base equivalence b:D->D' and prescribed ordered real value-monoid isomorphism g:M->M'. These are chosen representatives of the admitted comparisons, with the original degree line, reciprocal normalization and compatible common scale retained. This result does not select new representatives to force a compatibility.

Use the split enhanced models of IUT II Definition 4.9(ii)–(iii) at the two labels, with the original divisor functors. More explicitly, the local presentations used here have constant divisor functors

    Phi(x)=N e,       Phi'(x')=N e',

and rational-function functors

    B(x)=Z e ⊕ U(x),  B'(x')=Z e' ⊕ U'(x'),
    Div(r e,z)=r e,   Div'(r e',z')=r e'.

All notation for monoids and units is additive. The first factors are the groupifications of the non-unit splitting monoids, and the splitting is r e |-> (r e,0). The primitive generators are those of the retained monoids, not arbitrary positive elements of their real spans. The theta-cover presentation is first carried through its specified equivalence with the field-base presentation; no cover is literally identified with a field extension.

Assume the admitted unit comparison has been supplied as a natural isomorphism c:U->b^*U', with the source-prescribed ind-topology and Galois equivariance, and carries every Kummer image module I_H onto the module at the corresponding open subgroup. This is the unit/Kummer premise of the application. An arbitrary abstract group isomorphism is insufficient. Do not identify (O^times/mu)^H with O^times(H)/mu(H).

Let j:Phi->M and j':Phi'->M' denote the retained embeddings in realification, compatible with the base functors. Put t=j(e)>0 and t'=j'(e')>0. Define g_0 to be the unique positive real-linear map M->M' with g_0(t)=t'. Write C,C' for the two model categories, and R:C->A, R':C'->A' for their natural realifications followed by the elementary local presentations. Let Q_g:A->A' be L128's base-and-divisor functor; define Q_(g_0) similarly.

## Conclusion

The primitive-generator identification and c give a split-model equivalence F_0:C->C' over b that preserves Frobenius degree, linear arrows, the product splitting and all the specified Kummer image modules. Its induced real value map is g_0. There is an invertible natural comparison

    Q_(g_0) R => R' F_0.

For this construction, a comparison with the **prescribed** Q_g exists if and only if

    g(t)=t'.                                                   (P)

The same equality is necessary for any lift obtained by natural isomorphisms of these divisor/rational-function functors over b, preserving their splitting and the specified elementary realification. This is a criterion for the stated model-data mechanism, not for every equivalence of categories, permitted formal comparison or IUT construction.

No value of g(t)/t' for the original adjacent application is established here. In particular this result does not construct step530's prescribed beta_v. It identifies a single calibration obligation after the admitted base/unit premises; it does not identify the original hull, prove formal or iterate coherence, or imply native membership, finite B>=A or an essential IUT flaw.

## Proof

### Source constructions and the local specialization

Import the explicit model construction from [Mochizuki, The Geometry of Frobenioids I, June 2008](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf), Theorem 5.2(i)–(ii), pp.100–101. Its objects are (x,a) with a in Phi(x)^gp; an arrow from (x,a) to (y,a') consists of (f,n,d,u), where f:x->y, n>=1, d in Phi(x), u in B(x), and

    n a+d=f^*a'+Div(u).                                        (1)

Use the groupification in (1), with the [January 2024 corrections](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I%20%28comments%29.pdf). This constructed model is isotropic and birationally Frobenius-normalized by 5.2(ii). Its natural realification is Proposition 5.3, p.103: replace Phi by its realification and B by the real span of its divisor image. We do not use Corollary 5.4 to reconstruct data from an arbitrary categorical equivalence, or reprove the reconstruction theorems.

The rank-one constant hypotheses are the actual local split model hypotheses in [IUT I, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf), Example 3.2(iv)–(v), pp.71–73. The constant divisor submonoid is N times the divisor of the specified 2ell-th root of q, which lies in K_v and has positive valuation. Part (v) gives the splitting-compatible equivalence with the theta-cover presentation. [IUT II, December 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf), Definition 4.9(ii)–(iii), pp.155–156, replaces the splitting part modulo mu_(2ell) and the units modulo all torsion by their direct product, retains the original divisor functor, and uses its groupification in the model. The splitting part maps isomorphically to the characteristic quotient by units. Here that quotient is N e. Its primitive generator is fixed by every monoid automorphism, so the constant generator and its splitting are compatible with base pullbacks. Thus its groupification is Z e, with divisor the identity, as displayed in the hypotheses. Definition 4.9(viii), p.158, also explicitly describes these non-unit monoids as abstract copies of N. This does not identify their embedded positive generators across labels.

Definition 4.9(i), pp.153–155, defines the Kummer structure through its entire family I_H. The admitted class in [IUT III, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf), Theorem 1.5(iii), pp.48–50, is retained as the unit premise. When the model's functors are presented by invariants of their universal G-modules, equivariance of c carries the H-invariants to the corresponding H'-invariants and commutes with restriction and conjugation. Its preservation of the smaller specified image modules I_H is a separate retained requirement. No quotient/invariant interchange is used to infer it.

The realification hypotheses hold locally: N e is perf-factorial, and the divisor image of B is all Z e at each object, because of the splitting. Its real span is therefore the full one-dimensional value group. This is a local fact, not a claim about a global principal-divisor span. In the realified model, B^rlf=M^gp with divisor the identity. Forgetting the object coordinate a and the rational-function coordinate u gives its elementary presentation: (1) determines u uniquely from f,n,d,a,a'. This functor is fully faithful for each pair of objects and essentially surjective; it agrees with the local elementary presentation of Frobenioids II, Example 1.1(i)–(ii), pp.7–9. Consequently R takes (x,a) to x and (f,n,d,u) to (f,n,j(d)). This description also checks the actual natural realification functor used here.

### All-arrow construction and inverse

Pull C' back along b for the calculation. This retains D and its specified equivalence with D'; it is a presentation change, not the deletion of the base. Define

    h_x(r e)=r e',
    k_x(r e,z)=(r e',c_x(z)).                                  (2)

The first formula extends to groupifications. Both maps are natural; the divisor maps are constant on the generator and c is natural on the unit functors. They satisfy

    Div' k_x=h_x^gp Div,
    k_x(r e,0)=(h_x^gp(r e),0).                                (3)

Define F_0(x,a)=(b x,h_x^gp(a)), and on arrows define

    F_0(f,n,d,u)=(b f,n,h_x(d),k_x(u)).                         (4)

Applying h_x^gp to (1), using (3) and naturality under f, gives precisely the target arrow equation. Thus every arrow in (4) exists, including every degree n>1.

For composable arrows phi=(f,n,d,u), psi=(p,m,d_2,u_2), the model's composition coordinates are

    (p f,mn,f^*d_2+m d,f^*u_2+m u).                            (5)

Naturality and additivity give

    h_x(f^*d_2+m d)=(b f)^*h_y(d_2)+m h_x(d),
    k_x(f^*u_2+m u)=(b f)^*k_y(u_2)+m k_x(u).

The base and degree coordinates also agree, so (4) preserves composition. Identities have coordinates (id,1,0,0) and are preserved. On the pulled-back presentation, h^{-1} and k^{-1}(r e',z')=(r e,c^{-1}(z')) give a strict inverse on all coordinates and satisfy the same arrow equation. Returning through b and a quasi-inverse to b gives an equivalence on the original presentations. The base unit/counit isomorphisms act by the natural pullbacks of (2); hence these are inverse equivalences, not merely objectwise bijections.

The second equation in (3) verifies the product splitting. On units (4) acts by c, which preserves every stipulated I_H by hypothesis. Frobenius degree is unchanged, so linear arrows remain linear. No choice of a rational-function map remains after fixing h, c and this product splitting: (2) is forced on each direct factor.

### Realification and the primitive-arrow test

The two functors Q_(g_0) R and R' F_0 have the same object b x. On an arbitrary arrow their elementary coordinates are respectively

    (b f,n,g_0(j(d))),        (b f,n,j'(h_x(d))).

Since d is a nonnegative integral multiple of e, the divisor entries agree. Their comparison is the identity on this presentation, with inverse identity, and its naturality holds for every arrow by the displayed equality. Equivalences back to the retained source presentations give the asserted invertible natural comparison. The induced realified model map extends h to the full real ray; that extension is g_0. This argument does not substitute an ordinary field-element contact functor for the enhanced model's natural realification.

If (P) holds, g and g_0 agree on every j(d), so the same construction gives Q_g R=>R' F_0. In fact they agree on the full real ray: an ordered additive isomorphism of real half-lines is the unique positive real-linear map determined by one positive value. One may see this by equality on positive rational multiples of t and monotonicity between arbitrarily close rational multiples. Thus the entire realification square agrees, not only a selected divisor.

Conversely, let x be the terminal field-base object, let X=(x,0), and take the actual model endomorphism

    eta=(id_x,1,e,(e,0)):X->X.                                 (6)

Equation (1) holds because e=Div(e,0). The elementary images of eta under Q_g R and R' F_0 have divisor entries g(t) and t'. Every invertible arrow of the elementary target has degree 1 and divisor 0: degrees multiply to 1, and the effective divisor of a composite is a sum of nonnegative terms. Also b(x) is terminal, so its only base automorphism is the identity. Naturality at (6) of any invertible comparison between these two functors therefore forces g(t)=t'. A nonzero comparison component cannot absorb a scale error.

Finally, any divisor-functor isomorphism N e->N e' sends e to e'. Indeed, if e maps to r e' and e' maps back to s e, then r,s are nonnegative integers with rs=1, so r=s=1. For any model-data lift through such maps, (6) again has target effective divisor e', and the same naturality test applies. This proves the stated necessity only in the specified scope. Arbitrary formal diagrams, additional pullbacks/twists, or functors not specified by these data are not classified by this argument.

### Application status and decisive bound

For L128's retained reconstructed map, define the positive real scalar delta by g(t)=delta t'. The required value is **delta=1 exactly**, not merely positivity, boundedness, rationality, or equality of real spans. The actual delta for the retained adjacent enhanced models has not been obtained. III 1.5(v), pp.50–51, supplies the reconstructed real comparison and its stated common-scale compatibility; (iii) supplies the restricted unit comparison. Neither of those statements alone evaluates (P) for the splitting generator in this application. This is a limitation of the present trace, not a claim that no other cited construction can evaluate it.

There is no independent unknown mixing term between units and the splitting in this product model once h and c are fixed: (2) specifies it. The unsuccessful part of step538 is the application of its induced map g_0 to the prescribed g, not the all-arrow functor check. A new scale chosen to arrange delta=1 would change the problem unless its admissibility for the retained entire collection were established separately. The reciprocal factor [K_v:(F_mod)_v]^{-1} in the global restriction remains that of L128; it is not adjustable in this calculation.

This conditional known-construction specialization is not progress beyond the checked sources. No native value of delta unequal to 1, native counterexample, or complete candidate is supplied. The sufficient prescribed model lift is parked pending concrete additional calibration data; the whole formal comparison and IUT are not ruled out.

### P-normalized application audit (step542)

This audit retains exactly the hypotheses above. Its source assessment is the previously approved `drafts/literature/2026-10-29-p-normalized-primitive-coefficient.md`. It does not add a full D-theater lift or a new normalization. The calculation below identifies an original-model coefficient and a reconstructed anchor; it does **not** verify (P) for the retained embeddings.

To distinguish the elliptic parameter from its root, write Q_v for the Tate parameter and qbar_v for the specified 2ell-th root in IUT I, Example 3.2(iv), pp.71–72. Let nu_v:K_v^times->Z be the surjective valuation, and put e_v=nu_v(p_v). In the original arithmetic divisor ray V_v, let u_v be the positive uniformizer value. Then

    P_v^arith = e_v u_v,
    T_v^arith = nu_v(qbar_v) u_v,
    T_v^arith = c_v P_v^arith,
    c_v = nu_v(qbar_v)/e_v = nu_v(Q_v)/(2ell e_v) > 0.          (7)

Here T_v^arith is the original image of the primitive of the **q-generated submonoid**, not necessarily the primitive of the full valuation monoid. The equations follow from the definition of the valuation divisor and qbar_v^(2ell)=Q_v; roots of unity have valuation zero. No logarithm of a non-unit or quotient/invariant interchange is used. On the original reference models at the fixed place, the same initial Theta-data fixes Q_v, ell and K_v. Thus (7) gives the same rational coefficient at the two reference endpoints. This statement is about the arithmetic reference data; it does not identify their images in the retained reconstructed rays. The theta presentation carries qbar_v to the specified theta generator by IUT I, Example 3.2(v), pp.72–73. Example 3.5(ii), p.85, retains precisely the inverse coefficient log_Phi(p_v)/log_Phi(qbar_v)=1/c_v in its restriction formula. The enhanced construction in IUT II, Definition 4.9(ii)–(iii), pp.155–156, retains the original divisor monoid. Consequently neither passing to that enhanced model nor using the theta presentation authorizes replacing c_v by 1.

There is also a normalized anchor comparison at the full-constants stage of each endpoint. Import [AbsTopIII, November 2015](https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20III.pdf), Corollary 1.10(i)(a)–(b), pp.41–42, and Proposition 5.8(i)–(iii), pp.139–140; [IUT II, December 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf), Remark 1.11.5(i), p.55, and Proposition 3.3(ii), p.90. With the stated field/curve cyclotomic identification, the Kummer valuation on an original element of K_v^times is nu_v. Its value 1 corresponds to the distinguished Frobenius value F(G_v); hence the original p-divisor maps to

    P_v^D = e_v F(G_v),                                      (8)

which is exactly IUT I, Example 3.5(iii), p.86's distinguished p-value. The map can be described as inclusion in full constants, the cited Kummer comparison, quotient by units, and ordered realification. Conjugating the constants comparison does not change this divisor: the Galois action preserves valuation. These facts apply separately at each endpoint using its own original full-constants data. They do not assert that the prescribed b is induced by a comparison of those full data.

For an isomorphism of the local field groups, Proposition 5.8 preserves both e_v and F(G_v). Thus the functorially reconstructed value map gamma_v satisfies gamma_v(P_v^D)=P_v'^D, including for the larger admitted mono-analytic comparison class. This is the functorial reconstruction conclusion, not a property of arbitrary positive real-linear maps. There is no open-subgroup passage in this assertion. The different factor d_v=[K_v:(F_mod)_v] remains in the global restriction: IUT I, Example 3.5(i),(iii), pp.84,86, sends its global p-value to P_v^arith/d_v or P_v^D/d_v respectively. It is not permissible to replace d_v by e_v or delete it.

The unsuccessful check is the identification of the preceding normalized maps with the **retained** embeddings j,j'. Here is the exact square that this application would have to match at each endpoint s:

    Phi_global,s^arith --H_s--> Phi_global,s^D
           | rho_s^arith               | rho_s^D
           v                           v
           V_s          --J_s-->       M_s .                  (9)

J_s is the real-linear extension of the retained original divisor embedding, after the original arithmetic inclusion of the q-generated monoid. H_s must be the matching whole-collection identification, not one chosen afresh. IUT II, Corollary 4.6(ii), pp.137–138, with its proof and Remark 4.6.1, pp.139–140, supplies a compatible reconstructed collection. Its bad-place local interface is Remark 4.2.1(i), pp.125–126, which asserts analogues of Proposition 4.2(i),(ii) but leaves their routine details unwritten. The explicit distinguished-generator formula in 4.2(ii), p.124, concerns a **good** place. At the bad place, using that formula literally with the q-generated primitive would discard the factor in (7). The full-constants construction above supplies a normalized candidate for the bottom map of (9), and the global normalization supplies the corresponding candidate top map. This audit has not identified those candidates with both retained J_s,H_s. Uniqueness relative to specified local comparisons in 4.6(ii) does not identify a local comparison before its normalization is matched.

More explicitly, work first in the reconstructed coordinates of L128. Write

    J_s(P_s^arith) = a_s P_s^D,       a_s > 0.

This defines a_s from the retained map; it is not a new allowed parameter or a license to vary that map. Combining (7) with preservation of (8) gives, for the proposed comparison through these coordinates,

    g(t) = c_v a_0 P_1^D,     t' = c_v a_1 P_1^D,
    delta = a_0/a_1.                                          (10)

If the retained presentation is obtained by whole-collection coordinate changes, (10) must be transported along those changes together with g, rho and j; it is not computed after rescaling j alone. Thus the required test is equality of the two **actual** residual factors. No unequal-factor example, arbitrary independent rescaling of an admitted IUT pair, or asserted freedom in a_s is established here. In particular, the known common positive degree-scaling orbit in [IUT III, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf), Theorem 1.5(v), pp.50–51, neither evaluates these factors for the retained maps nor by itself identifies orbit representatives at adjacent vertical labels. The common scale concerns an entire compatible collection; the theorem's final compatibility with Frobenius-like data is stated relative to horizontal arrows. Calling both endpoints copies, or selecting the normalized candidates in place of the retained maps, would not complete this check.

Required: delta=1 for the original prescribed comparison. Actual: (7) computes the reference coefficient and (8) identifies the functorial reconstructed anchor; the match in (9), hence the residual equality in (10), remains unverified. Stop the sufficient-lift application here. This is the third mathematical EXPLORATION since step535, after steps538/540; it is not a counterexample, a new obstruction theorem, or progress beyond the checked normalization constructions. The scalar route and the full-Xi route are parked. Reopening requires a concrete verification of the retained embedding/whole-collection square or an original-hypothesis unequal-delta example, rather than another normalization chosen to force (P). The independent formal comparison is not ruled out.

## Mathlib

Full matching theorem for these split-Kummer model Frobenioids and the prescribed realification comparison: **not checked**. Supporting category-equivalence, natural-transformation and ordered-monoid facts: **not checked**. No absence or formal verification is claimed.
