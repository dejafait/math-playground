# L067 — Full translated-isogeny map has good reduction at thirteen

## Hypotheses

Use the geometric construction in L033, independently of its
transported-integer-solution clause:

    E0: y²+y=x³−x²−10x−20,
    E1: Y²+Y=X³−X²−7820X−263580,
    h:E0 -> E1, theta:E1 -> E0,
    theta h=[5] on E0, h theta=[5] on E1.

Both isogenies have degree five. Let j:E0 -> P1 be exactly L034's
degree-twelve FNS modular map, not the constant elliptic j-invariant.
Fix exactly L062's Q-algebra identification sigma and its point
P_sigma in E0(K), with j(P_sigma)=9261/8. Use audited L064's entire
completion F=K tensor_Q Q13, one unramified degree-twelve field;
write R=O_F and k=F_(13^12). Use audited L066's morphism on the
whole good model over R, with reduced polar divisor O+11(3T).

No primitive integer solution, choice of another localized conjugate,
rank/index certificate, GRH, Selmer/point equality or rationality of
individual pole preimages is assumed.

## Conclusion

The map

    J(Q)=j(P_sigma+theta(Q))

extends to a morphism from the full projective good model of E1 over
R to P1_R. Its generic and special fibers are separable maps of degree
60. On the geometric special fiber its complete polar divisor is

    sum_(theta_bar(q)=−P_bar) (q)
       +11 sum_(theta_bar(q)=3T_bar−P_bar) (q),

where each sum has exactly five distinct geometric points and the
two sets are disjoint. Here P_bar is the reduction of the extension
of the same localized P_sigma. No point of either set is required to
be k-rational. The generic fiber has the corresponding divisor with
P_sigma and 3T. The actual/required degree is 60/60 on both fibers.

This is a reproduction by theorem application of one local prerequisite
for a rational-j point method. It gives no rank bound, subgroup index,
coset zero bound, point classification, class removal or integer
exclusion. Independent critical application audit completed on
2026-10-14 confirms the conclusion without a mathematical correction.

## Proof

### Imported structural results and applicability

Reuse the pre-existing SPECIALIZE source comparison for this exact
target. The necessary structural inputs are the named Neron mapping
theorem and the good-reduction identification with the abelian model,
stated in Andrew Snowden, *Lecture 9: Neron models*, Math 679 (2013),
[author lecture](https://websites.umich.edu/~asnowden/teaching/2013/679/L09.html),
“Definition and basic properties,” “Classification of minimal regular
models” and “Types of reduction.” They extend generic maps from a
smooth R-scheme uniquely into the good abelian model. Supporting
scheme statements are Damien Robert, *Theory of abelian varieties and
their moduli spaces*, [author draft](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/books/avtheory.pdf),
footer March 7, 2023: Theorem 2.3.11, p.15 (abelian-scheme structure),
Example 3.1.8, p.27 (Neron identification), Proposition 3.1.19, p.31
(prime-to-residue-characteristic isogeny extension), and Proposition
2.3.15, p.16 (finite flatness and locally constant isogeny degree).
The inspected Robert passages include proof sketches, not a rereading
of the underlying BLR proofs. The inaccessible BLR scan is not an
independent premise. We use Proposition 3.1.19's stated hypothesis,
not the reversed divisibility wording in its sketch.

For multiplication use J. S. Milne, *Abelian Varieties*, Chapter V in
Cornell–Silverman (eds.), *Arithmetic Geometry*, Springer (1986),
103–150, [corrected author text, January 2, 2022](https://www.jmilne.org/math/xnotes/AVs.pdf),
Proposition 20.7, printed p.44: on an abelian scheme of relative
dimension one, [5] is finite flat of rank 25 and is etale when five
is invertible. This does not by itself assign rank five to theta;
that rank uses the preceding isogeny/constant-degree theorem.

Proper point extension is the valuative criterion in
[Stacks, tag 0BX5](https://stacks.math.columbia.edu/tag/0BX5).
Finite flatness on our locally Noetherian models gives finite local
freeness by [02KB](https://stacks.math.columbia.edu/tag/02KB);
rank strata and base change are covered by
[04MH](https://stacks.math.columbia.edu/tag/04MH) and
[02KD](https://stacks.math.columbia.edu/tag/02KD).
For degree multiplication and separability of the composite use
[02NZ](https://stacks.math.columbia.edu/tag/02NZ) and
[09HB](https://stacks.math.columbia.edu/tag/09HB), respectively.
These general results are imported, not reproved. The work below
checks their hypotheses and the particular map's whole pole divisor.

### Whole models, point extension and dual identities

The two projective Weierstrass models have discriminants −11^5 and
−11, as certified in L033. These are units in R. Thus they are proper
smooth relative curves with geometrically integral genus-one fibers
and origin sections. R is a connected complete DVR; each model is
an abelian scheme, and is its generic elliptic curve's good Neron
model. The hypotheses of Robert's Theorem 2.3.11 are met: properness,
smoothness, section, connected base and abelian geometric fibers.
Smoothness and flatness over the DVR make the generic fiber dense;
the models are reduced and integral.

Localize the fixed P_sigma using the canonical map K -> F; no new
field identification or conjugate is selected. Properness and
separatedness extend this F-point uniquely to a section P of E0/R.
This includes points with nonintegral affine coordinates: the
extension is to the projective model, not an affine chart.

Since the source models are smooth over R, the Neron mapping theorem
extends h and theta uniquely to morphisms of these whole models.
The group-homomorphism equalities extend as well: the two maps on
each smooth source product obtained from addition agree generically
and hence agree by uniqueness. Origins extend to origins. Likewise
the dual identities extend to

    theta_R h_R=[5]_E0,   h_R theta_R=[5]_E1.

Here each side is a morphism from the same smooth model and agrees
on its generic fiber. No equality is deduced merely from equality
on a set of R-valued points. Consequently translation tau_P on E0/R
is an everywhere defined automorphism, with inverse tau_(−P), and
reduces to translation by P_bar.

### Isogeny rank and etaleness, including the special fiber

The generic h and theta have degree five, prime to characteristic
thirteen. Robert's Proposition 3.1.19 therefore makes both extensions
fiberwise isogenies. By Proposition 2.3.15 they are finite flat with
locally constant degree over the base; connectedness of Spec(R) and
their generic degree give special degree five as well. The target
models are locally Noetherian, so both maps are finite locally free
of rank five. Base change to either geometric fiber preserves that
rank. This rules out a degree loss and a nonfinite special map.

For completeness etaleness is checked for these particular extensions.
Their tangent modules at the origins are free R-modules of rank one.
Differentiating the two extended dual identities shows that both
composites of their tangent maps are multiplication by five. Five
is a unit in R, so each tangent map is an isomorphism. Group
translation identifies differentials at every geometric point with
the differential at the origin. Equivalently, on the models their
maps on invariant relative differentials are isomorphisms everywhere.
The exact sequence for relative differentials thus gives
Omega_(E1/E0)=0 for theta_R (and likewise for h_R). The maps are of
finite presentation, so this is the unramified condition; with their
finite flatness it gives etaleness. This is the usual etale criterion,
applied to these two maps, consistent with Milne's [5] theorem.

In particular theta_bar is surjective etale of degree five. Over an
algebraic closure of k every fiber consists of exactly five distinct
points, each with ramification index one. We do not infer that these
points are rational over k or lift to five separate R-sections.
The same statement holds over an algebraic closure of F. None of
the quotient-kernel points is excluded by using an affine formula.

### Composition and complete pole pullback

L066 supplies a morphism j_R on all of E0/R, after base change to
this entire R, retaining O and both x=16 charts. Define

    J_R=j_R tau_P theta_R : E1/R -> P1_R.

All three maps are defined everywhere, so this is a whole-model
extension with the claimed generic restriction. This argument retains
the origin, every kernel point and every point sent by tau_P theta_R
to a cusp or to the removable 2T chart. At a preimage of 2T the
finite value of j is still −121; no denominator there creates a pole
or a base point. Points mapping to O or 3T are accounted for next.

On the geometric special fiber L066 gives precisely the polar
divisor (O_bar)+11(3T_bar). Translation pulls it back to
(−P_bar)+11(3T_bar−P_bar). These points are distinct: O_bar and
3T_bar are distinct on L066's smooth model, and translation is an
automorphism. Pulling further back by theta_bar yields the two
disjoint sets in the conclusion. Each has five distinct points and
all ramification indices are one, by the preceding etaleness check.
Thus a local parameter at either target pole pulls back with exact
order one, preserving the pole multiplicities one and eleven. No
other poles exist, since away from these points j_bar is regular.
This proves the complete divisor, rather than a count on a selected
fiber or on k-rational points. Its degree is 5+11·5=60.

Both geometric curves are smooth projective integral curves, and
theta_bar and j_bar are nonconstant finite surjective curve maps;
translation is an isomorphism. The associated function-field
extensions are finite, so 02NZ gives degree 5·1·12=60 for their
composite, agreeing with the full infinity-divisor calculation.
L066 proves separability of j_bar, and theta_bar is etale. Their
function-field extensions, with the intervening translation
isomorphism, are separable, so 09HB gives separability of J_bar.
Also 13 does not divide 60, independently excluding a nontrivial
inseparable degree. This does not assert that J_bar is etale: the
five poles with multiplicity eleven remain ramified.

On the generic geometric fiber L034 gives the same original poles
O+11(3T), and theta has degree five and is etale. The identical
pullback argument gives the stated generic divisor and degree sixty;
characteristic zero gives separability. Thus both required degrees
agree, without replacing the translated map by the original map or
only checking the curves' discriminants. Since F is the entire
K tensor Q13, this covers every completion above thirteen.

### Relevance and limitations

The continuation threshold is met: an entire integral extension with
generic/special degree sixty and separable reduction. The proof is an
application of existing structural theorems to the assessed map, not
a new extension theorem or an independently recomputed quotient.
No mathematical script or numerical point sample is needed for this
application; the audited model and original-map arithmetic are reused.

This supplies a reduction prerequisite only. Unconditional rank below
twelve, enough global generators with index control, coset rationality
zero tests, other-class coverage and global primitive power lifting
remain unresolved. ATTEMPTS/029–030's fixed-class survivors are not
challenged. In particular map degree sixty is not a bound of sixty
on rational-j points. The independent critical application review is
recorded below is separate from the original proof attempt.

### Independent critical application audit, completed 2026-10-14

This audit reuses the inspected structural sources cited above, rather
than treating their availability as verification of the application.
It checks the following complete chain with the same input models and
fixed point. No general extension theorem is reproved and no new
arithmetic certificate is asserted.

**Models and the fixed section.** L033's geometric construction and its
critical audit establish the two displayed projective Weierstrass
models, discriminants −11^5 and −11, and both degree-five dual maps.
These geometric facts precede and do not assume L033's separate
integer-solution transport. L064's audited whole-field result makes R
the integer ring of one unramified degree-twelve extension of Q13;
there are no omitted local factors. Both discriminants are units in R.
Thus the models are smooth and proper with origin section and
geometrically connected genus-one fibers. Spec(R) is connected and
Noetherian. The abelian-scheme and good Neron-model identifications
cited above apply to exactly these models, not merely to birational
affine equations. Their products over R are smooth too.

L062 defines P_sigma by Spec(K) -> Spec(D) -> E0 for the single fixed
isomorphism sigma:D -> K. Base change along K -> F therefore supplies
one F-point. The valuative criterion extends this point uniquely to an
R-section of the proper separated E0-model. It makes no assertion that
its original affine coordinates are integral. The Neron mapping
property extends each homomorphism from the smooth source model;
applying uniqueness on the smooth products verifies compatibility with
addition. Applying it on each model verifies both dual identities.
The extended section consequently defines translation and its inverse
on every point of the model. These steps require neither a new sigma
nor a rational lift of any special-fiber pole preimage.

**Special degree and etaleness.** For each geometric fiber, the two
compositions are multiplication by five on an elliptic curve. By the
cited multiplication theorem these compositions are nonconstant finite
maps of degree twenty-five. Hence neither factor can be constant. An
origin-preserving nonconstant map between these smooth projective
elliptic curves is a surjective finite homomorphism, so the extensions
are indeed fiberwise isogenies. This checks the hypothesis of Robert
Proposition 2.3.15 directly, in addition to the prime-to-thirteen
extension statement of Proposition 3.1.19. That finite-flat theorem
and its locally constant degree clause apply. Since the base is
connected, generic degree five implies special degree five for each
factor. Equivalently, finite local freeness on the connected target
has rank five; neither the rank twenty-five of the composite alone
nor a product-of-degrees equation alone would determine this rank.

Choose bases for the two free rank-one relative tangent modules at the
origins. The tangent maps are multiplication by scalars a and b in R,
with ab=ba=5. Thus a and b are units in R. For a smooth group scheme,
translation trivializes its relative cotangent bundle by invariant
differentials, compatibly with homomorphisms. Consequently
theta_R^* Omega_(E0/R) -> Omega_(E1/R) is an isomorphism on the
entire model. In the exact relative cotangent sequence its cokernel
Omega_(E1/E0) is zero. The map is finite and the target Noetherian,
so it is of finite presentation; the vanishing gives unramifiedness.
Together with the already proved flatness this gives etaleness.
The same argument applies to h_R. Base change retains rank five and
etaleness. A finite etale algebra of dimension five over an
algebraically closed field is a product of five copies of that field,
so every geometric fiber has exactly five distinct points. This
argument does not assume that its five points are k-rational.

**All poles on both geometric fibers.** L034's full characteristic-zero
calculation gives poles O and 3T with orders one and eleven; the
removable 2T value is −121. L066's whole-model chart audit gives exactly
the same poles and orders after reduction. In particular 3T is the
finite point (16,60), distinct from O on both fibers; its reduction is
(3,8), while 2T reduces to (3,4). Neither pole coalescence nor an
unaccounted pole at 2T is possible.

Let L be either an algebraic closure of F or an algebraic closure of
k, and use subscript L for the corresponding maps and points. The
translation preimages of the poles are precisely −P_L and
3T_L−P_L, which remain distinct. Surjectivity and etaleness of theta_L
give two disjoint five-point fibers over them. At each point q in
either fiber, a uniformizer u at its target pulls back to a
uniformizer times a unit: its order is exactly one. If the original
pole order is m in {1,11}, write j=u^(−m)v with v a local unit after
the appropriate translation. The pulled-back unit is still a unit,
so J has order exactly −m at q. Away from these two fibers j is
regular after composition, hence there are no further poles. Thus
on each of the two geometric fibers the full divisor is exactly

    sum_(theta_L(q)=−P_L) (q)
       +11 sum_(theta_L(q)=3T_L−P_L) (q).

Its degree is five plus fifty-five, namely sixty. These are statements
about all geometric points and their local orders, including origins
and kernel points, rather than a residue-field point sample.
Preimages of 2T stay regular under composition with the actual
L066 chart. The whole-model composition exists before this divisor
calculation, since its three constituent morphisms exist everywhere.

The nonconstant maps between smooth projective integral curves are
finite and dominant. Their finite function-field degrees multiply to
12 times 1 times 5, agreeing with the full divisor degree sixty in
each case. In characteristic thirteen, L066 gives separability of j
and the audited etaleness gives separability of theta; translation is
an isomorphism. Transitivity of separability therefore applies. Also
the inseparable degree is a power of thirteen dividing sixty and must
be one. Characteristic zero supplies generic separability. None of
this makes J etale at its poles of order eleven.

The continuation threshold is met: actual/required degrees are 60/60
on both fibers and no model-extension, multiplicity or separability
defect was found. The direct mathematical inputs are unchanged, so no
DAG edit is needed. This is independent verification of
the existing theorem application, not a new theorem beyond the sources
checked or a new restriction on integer solutions. No mathematical
script was needed: the audited field and original-map arithmetic are
inputs, and the present obligations are the structural application
and complete divisor pullback. Rank below twelve, generators/index,
coset zero bounds, other-class coverage and primitive power lifting
are still unresolved. ATTEMPTS/029–030 remain unchanged.

## Mathlib

Full matching translated-map certificate: **not checked**. Supporting
Neron/abelian-scheme extension, isogeny finite flatness and etaleness,
translation, divisor pullback and function-field degree/separability
coverage: **not checked**. Unknown coverage is not evidence of absence.
The complete local field and original chart arithmetic are reused from
audited L064 and L066; their exact source qualifications remain in force.
