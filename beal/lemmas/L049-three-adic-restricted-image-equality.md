# L049 — Equality of the three three-adic connecting images

## Hypotheses

Work over k=Q3, with valuation ring Z3 and v3(3)=1. Use L033's degree-twelve field K for 54a1 and set A3=K tensor_Q k. Use its curves

    E0: y^2+y=x^3-x^2-10x-20,
    E1: Y^2+Y=X^3-X^2-7820X-263580,

its dual five-isogeny theta:E1 -> E0 with kernel mu_5, and its Kummer connecting map. Write delta(P) for the class of P modulo theta E1(A3) under that map. Its codomain is A3^*/A3^{*5}. This uses the same rational generator T=(5,5), normalization and good-divisor evaluations as L033; ordinary f(P) evaluation is not used at its zero or pole.

Let j:E0 -> P1 be L034's complete projective degree-twelve modular map, base changed to k. It is distinct from the constant elliptic j-invariant of E0. For each finite s in k other than 0 and 1728, let Z_s=j^-1(s) be the entire scheme-theoretic fiber and B_s=Gamma(Z_s,O_Z_s). The fiber is finite affine; no factor or multiplicity is selected or discarded.

For every k-algebra isomorphism phi:B_s -> A3, let P_phi be the A3-valued point obtained from the universal fiber inclusion, as constructed below. Define

    I_all   = {delta(P): P in E0(A3)},
    I_fiber = {delta(P_phi): s in k\{0,1728}, phi:B_s -> A3 a k-algebra isomorphism}.

Define I_pow by the same data as I_fiber, additionally requiring one common triple of nonzero a,b,c in Z3 such that

    min(v3(a),v3(b),v3(c))=0,
    a^3+b^4=c^11,     s*c^11=1728*a^3,
    a=1 modulo 3,     b^2=1 or 4 modulo 9,     c in Z3^*.

These conditions imply (1728-s)c^11=1728*b^4 with the same c. No positivity or conditions at two are imposed. The sets are not assumed to be subgroups or nonempty. No primitive integer solution, global class computation, GRH, rank, Sha or Selmer/point equality is assumed.

## Conclusion

The exact three sets satisfy

    I_pow = I_fiber = I_all = {1} in A3^*/A3^{*5}.

In particular the primitive whole-fiber set is nonempty and adds no class restriction to either other image at three. This is a local comparison, not emptiness of 54a1 or any global intersection, and not an integer solution.

## Proof

### Imported interfaces and scope

L033 supplies the unconditional curves, dual-kernel/Kummer identification and good-divisor connecting map. L034 supplies the complete projective modular map and finite-fiber interface. We use these structural inputs without assuming their separate original-integer-solution hypotheses.

The underlying descent theorem is Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS **356** (2004), 1209–1231, [DOI](https://doi.org/10.1090/S0002-9947-03-03366-X), [June 13, 2001 long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf), Lemmas 4.2–4.5, printed pp.6–7, and Section 5, pp.8–10. L048 has already verified the actual field, good reduction of both curves, prime-to-three kernel exponent and rational kernel count required by these lemmas. We import its resulting full-image statement, rather than reprove descent or repeat the local-field calculation.

L047 imports Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113, [June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), Section 5 pp.17–18 and Section 7.2 p.25/Table 5 p.27. Its audited specialization gives common primitive witnesses and an entire canonical-fiber isomorphism; the source's GRH-dependent Selmer calculations are not inputs.

The affine tensor-product/base-change interface is [Stacks Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ). Applied to a finite fiber and Spec(k) over Spec(Q), it identifies the entire base-changed fiber. L047 verifies the canonical field identification before that base change. An arbitrary twelve-dimensional algebra is not identified with this fiber merely by dimension.

### Transport of the tautological point

The universal fiber inclusion is a k-morphism i_s:Z_s -> E0; by the defining fiber square, its composite with j is the constant morphism with value s. Since Z_s is finite affine, Z_s=Spec(B_s). The k-algebra isomorphism phi:B_s -> A3 induces the contravariant morphism

    Spec(phi): Spec(A3) -> Spec(B_s)=Z_s.

Set P_phi=i_s composed with Spec(phi). This is by definition an A3-valued point of E0, and j(P_phi)=s. Thus its connecting class is defined by precisely the delta used in I_all. This construction works for every allowed isomorphism; it makes no choice of an embedding into one factor or of an affine generator. The projective inclusion requires no division by a coordinate denominator. L033's good-divisor map remains defined even at exceptional points. Consequently

    I_pow subset I_fiber subset I_all.

The first containment follows from imposing the additional witness conditions on exactly the same s and phi. It does not change the point or its connecting map, so any class collisions are retained.

### Unrestricted singleton and restricted nonemptiness

L048 identifies A3 with a single degree-twelve field F, with ramification index six and residue field F9, and proves delta_F(E0(F))={1}. Transporting through its Q3-algebra identification gives I_all={1} for the same theta and Kummer map. In particular every P_phi constructed above has class 1. Triviality alone would leave open whether either restricted set is empty.

Use L047 for nonemptiness. It supplies exact a,b,c in Z3^* with

    a=7, b^2=13, c^11=512,
    a^3+b^4=343+169=512,
    s=9261/8,     B_s isomorphic to A3.

All three coordinates are nonzero units, so their minimum valuation is zero. Also a=1 modulo 3, b^2=4 modulo 9 and c is a unit. The same c gives s*c^11=1728*a^3 and (1728-s)c^11=1728*b^4. Both a and b are nonzero, so s is neither 0 nor 1728; L047 gives finite s. Choose any one of the supplied entire algebra isomorphisms phi:B_s -> A3. The preceding transport defines P_phi, and this very s, phi and common witness satisfy every condition defining I_pow. Hence delta(P_phi) belongs to I_pow, proving nonemptiness. L048 forces this class to be 1.

Together the two containments, nonemptiness and singleton I_all give the asserted three equalities. No fourth-power surjectivity, fresh root lifting or selected-factor existence argument is used.

### Relevance, threshold and qualifications

The required threshold was an exact comparison with restricted nonemptiness, not merely a bound on the unrestricted image. It is met: all three actual images are the nonempty singleton. Retire the additional primitive fourth-power class filter at three; enumeration cannot shrink it further under these definitions. This is REPRODUCTION assembly under the saved SPECIALIZE assessment, not a claim of a new general theorem or progress beyond the checked sources.

The global 54a1 intersections and L045 quotient classes remain unevaluated. Other twists and residual signatures are independent unresolved gaps. The local triple has b^2=13, so it is not an integer triple. Equality of local sets supplies neither compatibility with a single global integer solution nor a Beal resolution. The independent assembly audit below confirms this local conclusion without correction.

### Independent assembly audit, 2026-10-10

The audit reuses the already audited L047 and L048 conclusions. It does
not rerun their root, field or reduction calculations. L033's structural
isogeny and good-divisor construction and L034's complete finite map
are unconditional: their separate integer-solution hypotheses enter
only their arithmetic applications. Thus this local assembly does not
assume the integer solution it is intended eventually to constrain.

For transport, apply [Stacks Lemma 26.6.4, tag 01I1](https://stacks.math.columbia.edu/tag/01I1),
statement and full proof inspected in the approved coverage on 2026-10-10,
to X=Spec(A3) and Y=Spec(B_s). The specified map phi has domain B_s
and codomain A3, so its scheme morphism has exactly the direction used
above. Because phi is a k-algebra map, this is a k-morphism. The finite
fiber is affine by L034; its actual inclusion into the projective E0
gives P_phi in E0(A3). The defining fiber square gives j(P_phi)=s
through the structure map k -> A3. No affine presentation of E0, inverse
of phi, selected residue field, or division by a coordinate is needed.
The conclusion applies to each allowed phi, not merely a preferred one.

For the identity of the connecting maps, write gamma:A3 -> F for
L048's k-algebra isomorphism. It induces a bijection on curve points
and an isomorphism gamma_*:A3^*/A3^{*5} -> F^*/F^{*5}. The rational
curves, theta, T and f are the same in L033, L048 and this lemma.
More explicitly, for any P choose one of L033's rational points
R in {2T,3T,4T} for which (P+R)-(R) is good. Field transport fixes R
and commutes with the rational group law. It preserves nonzero finite
values of f, so the transported divisor is also good and

    gamma_* delta_A3(P)
      = [gamma(f(P+R)/f(R))]
      = [f(P^gamma+R)/f(R)]
      = delta_F(P^gamma).

This checks the normalization as well as the isogeny direction, without
an appeal to an unspecified choice of Kummer coordinates. It includes
T and O, because the good-divisor ratio, rather than f(P), is used.
Every point over F is transported from a point over A3. L048's full
image is therefore precisely gamma_*(I_all)={1}, and the inverse image
of 1 is 1. No field factor has been lost: L048 identifies the entire
algebra as this one field. Its verified good-reduction, Tamagawa and
dual-kernel hypotheses are unchanged by this identification.

Nonemptiness needs a separate input. L047 gives a=7, b^2=13,
c^11=512 in Z3, with all three coordinates units. Its single triple
satisfies a^3+b^4=c^11 and both scalar identities with s=9261/8.
Its residues are a=1 modulo 3 and b^2=4 modulo 9; c is a unit.
These are all the extra conditions in the definition of I_pow.
The scalar is finite, nonzero and different from 1728. In particular
no valuation, sign, condition at two, or independent choice of c on
a field factor is tacitly imposed. L047's canonical rational fiber
identification, base changed as in Stacks Lemma 26.17.2 (tag 01JQ),
provides an isomorphism for the entire B_s. It supplies at least one
allowed phi and hence one element of I_pow by the transport just
checked. Dimension equality alone would not have supplied this step.

Finally, a pair (s,phi) admitted by I_pow is admitted unchanged by
I_fiber. Every such pair gives a point admitted by I_all, with exactly
the same delta. Thus the two containments hold even if many pairs give
the same class, without any subgroup assertion. A nonempty subset of
the singleton I_all is that singleton, proving both equalities.
Exceptional evaluations and all allowed isomorphisms are retained.

The audit finds no error or missing hypothesis within the stated local
scope. This is REPRODUCTION verification, not a new restriction or a
repair of the mathematics. It confirms the stop for this additional
class filter. It neither evaluates L045's class nor establishes global
emptiness, compatibility of local witnesses across primes, or an
integer solution. No repeated assembly audit or witness enumeration
is warranted by this passing result.

## Mathlib

Full matching three-adic restricted-image comparison: **not checked**. Supporting affine-scheme/algebra correspondence, finite-fiber base change, connecting maps and set-containment declarations: **not checked**. Unknown availability is not evidence of absence. The cited primary results and audited local inputs supply the interfaces used here.
