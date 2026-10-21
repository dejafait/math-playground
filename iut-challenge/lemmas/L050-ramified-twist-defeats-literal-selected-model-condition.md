# L050 — Ramified twist defeats the literal selected-model condition

## Hypotheses

Fix the same E_0/Q selected in L048, with its original equation

E_0: y^2=x^3+c x^2+d x+e,  c,d,e in Z,

at the fixed precision M>=max(M_tors,31). Retain L045's
F=Q(zeta_60,E_0[30]), E_F=E_0 over F, induced place u and
embedded F_u=H=Q_3(zeta_60). Retain the absolute valuation
v_3(3)=1 and L048's v_3(q_0)=30, without q_0=3^30.
Let v be the restriction of u to Q(j(E_F)).

Interpret a Q(j(E_F))-model of E_F as a pointed elliptic curve
over that field whose base change is isomorphic to E_F over F,
or use the broader geometric-isomorphism interpretation. No
restriction to the single Q-isomorphism class of E_0 is imposed.
This explicitly states the model-class qualification in the
conclusion; the inspected exposition does not formally define it.

## Conclusion

Q(j(E_F))=Q, and v is the ordinary 3-adic place. The Q-curve

E_0^(3): y^2=x^3+3c x^2+9d x+27e

is a Q-model of E_F even under the F-isomorphism requirement.
Over Q_3 it has Kodaira type I_30^*, hence additive rather than
multiplicative reduction. Consequently the retained place fails
Dupuy–Hilado arXiv:2004.13228v1 Definition 5.3.1(4) under either
of the stated model-class interpretations: there is a permitted
model without multiplicative reduction at v.

If “model” instead means only a different equation for the fixed
Q-isomorphism class of E_0, every such model has the multiplicative
reduction of E_0 at 3; the countermodel is outside that narrower
class. The literal F-descent/geometric verdict does not decide
the author's intended convention or the native IUT definition.

This application of known twist/reduction results passes the separate
2026-10-12 critical audit below, with its model-class qualification
unchanged. It is not an essential IUT flaw, a failure
of semistability over F, or a conclusion about original finite B>=A.

## Proof

### Imported results and versioned quantifier

Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-11-selected-model-quantifier-at-three.md`.
Its primary-source comparison fixes Dupuy–Hilado,
[arXiv:2004.13228v1, 28 April 2020,
Definition 5.3.1(4), p.26](https://arxiv.org/pdf/2004.13228v1#page=26).
That condition says “every model E_Q(j_E) of E over Q(j_E) has
multiplicative reduction at v.” The preceding setup and following
Remark 5.3.2, together with section 3.3 p.9, were inspected in
the assessment; no restriction to one Q(j_E)-isomorphism class
was found there. Section 5.7.1 p.32 tests one named curve and
does not resolve the terminology. The verdict below is therefore
qualified by its explicitly stated model class, not by replacing
“every” with existence or potential multiplicativity.

Import J.S. Milne, *Elliptic Curves*, second edition (2021),
[IV.7, Example 7.12 and Corollary 7.16, pp.140–141](https://www.jmilne.org/math/Books/EC2.pdf#page=144),
for quadratic twists and their pointed isomorphism when the twist
parameter is a square. Field characteristic is zero here; residue
characteristic 3 does not obstruct this construction.

Import Barrios, Roy, Sahajpal, Tallana, Tobin
and Wiersema, *Local data of elliptic curves under quadratic
twist*, [arXiv:2501.03209v2, 2 July 2025, Definition 3.4,
Proposition 3.5 and Table 1, pp.5–7; Theorem 4.1 and Table 4,
pp.13–14](https://arxiv.org/pdf/2501.03209v2#page=13).
The proposition supplies a strongly-minimal representative; the
theorem states that, over a local field with perfect residue field
of odd characteristic, a quadratic twist of type I_n, n>0,
by a parameter of valuation one has type I_n^*. Reuse the
assessment's inspection of the odd-characteristic I_n proof
pp.8–9 and type-determination proof pp.14–15, which include
residue characteristic 3. No new twist theorem is proved here.

J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second
edition (1997), [III.1–2, pp.62–67, especially the type list
p.65 and Tate's algorithm pp.66–67](https://johncremona.github.io/book/fulltext/chapter3.pdf),
supplies invariance under pointed local coordinate changes, the
multiplicative I_n branch with n the minimal discriminant
valuation, and the distinction of additive I_n^* from I_n.
Only explicit field membership, isomorphism and theorem
hypotheses need specialization; none of these standard results
requires a reproof or numerical certificate.

### Field of moduli and an unchanged-field isomorphism

The nonsingular equation is defined over Q. Its invariants are
rational and its discriminant is nonzero, so j(E_F)=j(E_0) is
in Q and Q(j(E_F))=Q. L048 moreover gives v_3(j(E_0))=-30.
Thus j is neither 0 nor 1728 (v_3(1728)=3), consistent with
Milne's nonexceptional twist classification. The fixed embedding
restricts to the given absolute 3-adic valuation on Q, so v is
its unique 3-adic place.

Set z=zeta_60^5, a primitive twelfth root in k=Q(zeta_60)
inside F. Then t=z^2 has order six. Hence t^3=-1 and t!=-1,
so (t+1)(t^2-t+1)=t^3+1=0 gives t+t^(-1)=1. Therefore

s=z+z^(-1) satisfies s^2=z^2+2+z^(-2)=3.

In particular s!=0 and s belongs to the already fixed k subset F.
The displayed E_0^(3) is the standard quadratic twist by 3:
over any field containing s its map to E_0 is

(x,y) -> (X,Y)=(x/3,y/(3s)).

Indeed Y^2=y^2/27=X^3+c X^2+d X+e, and the inverse is
(X,Y) -> (3X,3sY). Milne's pointed twist isomorphism extends
these maps to the points at infinity. Equivalently these are
invertible weighted Weierstrass scalings, preserving that point.
Nonsingularity follows from this isomorphism after scalar extension
(or Delta(E_0^(3))=3^6 Delta(E_0)!=0). The coefficients are in Q.
Thus E_0^(3) is a Q-model of the given E_F under both model-class
interpretations in the hypotheses, without any enlargement of F,
new curve selection, or geometric-only replacement of the required
F-isomorphism. As a pointed F-curve it is the same isomorphism
class E_F; its descent over Q is different.

### Reduction theorem application at the field-of-moduli place

L048 proves that E_0's original equation is minimal over Q_3,
has unit c4 and v_3(Delta)=30, and has split multiplicative
reduction. Cremona's multiplicative branch therefore gives its
type I_30. This uses the original integral cubic, not L046's
scaled short equation or an assumption that an arbitrary equation
is already strongly minimal.

Apply Barrios et al. Proposition 3.5 to obtain the strongly-minimal
local representative needed for their Theorem 4.1. Replacing the
equation by a pointed Q_3-isomorphic representative does not change
the reduction type or the isomorphism class of its quadratic twist.
It does not reselect the global E_0. In the theorem, the field is
Q_3, its perfect residue field is F_3 of odd characteristic, the
original type has n=30>0, and the twist parameter is the element
3 of normalized valuation v_3(3)=1. It is nonsquare in Q_3
because a square has even integral valuation. These check the
ramified-twist row of Table 4. Its conclusion is type I_30^*,
independently of the splitness/Tamagawa subcases. This is additive
reduction, so E_0^(3) is not multiplicative at v.

The condition requires every permitted model to be multiplicative.
The achieved result is one permitted
additive model; it therefore negates precisely that universal
condition under the stated model class. It supplies no numerical
volume estimate or failure of original B>=A.

### Scope and continuation limits

The local theorem was applied over Q_3, the completion of the
field of moduli at v, rather than over F_u=H. Over H the element
s is present and the twist is isomorphic to E_0, so the retained
split multiplicative reduction over H is unchanged. Hence L049's
everywhere-semistability statement for E_F is compatible with this
additive Q_3-descent. All embedded H,N conclusions and v_3(q_0)=30
remain about L048's same E_0; no equality q_0=3^30 is used.

If the quantified class consists only of equations Q-isomorphic
to E_0, reduction type is invariant under that isomorphism and
L048 gives multiplicativity throughout that class. The additive
type just established also proves the twist is not Q_3-isomorphic,
and hence not Q-isomorphic, to E_0. Accordingly the two readings
are distinguished rather than adjudicated by an unstated convention.
The supplied source comparison leaves that convention unresolved.

ATTEMPTS/022,025,026,027 remain in force for their distinct fields
and exact-curve targets. This result only blocks use of the retained
place to meet the literal broad universal-model prerequisite. It
does not rule out another selected place, sufficient initial data
under a narrower convention, native IUT definitions, or IUT itself.
Other-place parameter orders, selected data, actual input/action,
marked pilot, essentiality and original finite B>=A remain open.
The independent audit below validates this local specialization;
no claim of progress beyond the imported twist results is made.

### Separate critical audit — 2026-10-12

**Verdict and inputs.** The statement passes the prior SPECIALIZE
assessment `drafts/literature/2026-10-11-selected-model-twist-critical-audit.md`.
This is an independent applicability check, not a new twist theorem.
L045 supplies the fixed cyclotomic subfield, F and its induced
completion; L048 supplies the same curve's minimality, reduction
and invariant valuations. Their completed audits are retained.
L049 is a consistency contrast only. No additional direct input
or change to the conditional conclusion is needed.

**Field, root and pointed map.** Rational coefficients and nonzero
discriminant give rational j, hence Q(j)=Q. L048 gives
v_3(j)=-30; j=0 is excluded, as is j=1728 with valuation 3.
Thus the nonexceptional twist classification cited above applies.
The restriction of the fixed place to Q is the 3-adic place,
whose completion is Q_3, irrespective of the ramification in F.

Since zeta_60 has exact order 60, z=zeta_60^5 has order 12
and t=z^2 has order 6. In characteristic zero, t^3=-1 and
t+1 is nonzero. Factoring t^3+1 and dividing by t gives
t+t^(-1)=1. Thus s=z+z^(-1) lies in the existing F and
s^2=3. This identity uses the actual chosen root, not a choice
of a new embedding or an abstract isomorphism of fields.

Substitution into the proposed map gives

(y/(3s))^2=y^2/27=(x/3)^3+c(x/3)^2+d(x/3)+e.

Both compositions with (X,Y)->(3X,3sY) are the identity.
On the ordinary projective cubic, the forward map is the
invertible diagonal projective transformation
[x:y:z]->[x/3:y/(3s):z]; it carries the homogenized equation
to the other after multiplication by 1/27 and fixes [0:1:0].
It therefore extends everywhere and is pointed. The twist is
nonsingular because of this isomorphism, and has rational
coefficients. This proves the required F-descent membership,
which is stronger than mere geometric membership.

**Local theorem and change of representative.** L048's unit c4,
minimal discriminant valuation 30 and split multiplicative
reduction give I_30 by the cited multiplicative branch of Tate's
algorithm. These facts concern the original cubic. They do not
assert that it already has the coefficient pattern needed in
Barrios et al.'s theorem.

Use that paper's Proposition 3.5 to choose a strongly-minimal
Q_3-representative. Twisting this representative gives the same
Q_3-isomorphism class as twisting E_0: a pointed isomorphism
commutes with [-1], so transports the quadratic descent datum.
More explicitly, over Q_3(s), if alpha and alpha' are the two
standard twist maps and h is the Q_3-isomorphism between the
original representatives, the map alpha'^(-1) h alpha between
their twists is Galois-invariant. Each nontrivial conjugation
changes both alpha and alpha' by [-1], and h commutes with it.
Hence this map descends to Q_3. This checks application of
Milne's cited twist construction; it does not assume an integral
coordinate change or change the global E_0.

For [Barrios et al. v2, Theorem 4.1 and Table 4,
pp.13–15](https://arxiv.org/pdf/2501.03209v2#page=13), the ring is
Z_3, the field Q_3, the uniformizer 3 and the perfect residue
field F_3. The chosen representative has type I_30; d=3 has
normalized valuation one and is nonsquare. The positive-n row
therefore gives I_30^*. Its residue-character conditions only
select the Tamagawa number, not the type. In particular the
theorem requires odd residue characteristic, not characteristic
greater than three.

The essential proof case also matches numerically: Table 1's
odd-residue I_30 row permits a1=a3=0, v(a2)=0,
v(a4)>=17 and v(a6)=30. Twisting adds 1,2,3 to these last
three valuations, giving 1, at least 19, and 33. These satisfy
the even-n I_30^* row's requirements 1, at least 18, and 33.
This is precisely the coefficient-pattern check used in the
theorem's type proof on p.15, not a reproof of Tate's algorithm.
The strongly-minimal replacement is essential to this check;
the original c,d,e are not asserted to meet these bounds.

**Quantifier and base field.** The versioned Definition 5.3.1(4)
cited above demands multiplicativity of every permitted model.
Under the stated F-descent interpretation the twist belongs to
that class, yet its Q_3-reduction is additive. Thus the universal
condition at this place fails. Under the broader geometric
interpretation the same countermodel works. Under the narrower
single-Q-isomorphism-class interpretation it is excluded: its
different Q_3-reduction type prevents a Q-isomorphism to E_0,
whereas every equation Q-isomorphic to E_0 retains type I_30.
The inspected text does not settle which class was intended.

Over H the element s is present, and the pointed isomorphism
remains defined. Accordingly the additive assertion over Q_3
does not contradict multiplicativity over H or L049's
semistability over F. The original E_0,F,H,N and v_3(q_0)=30
are retained; no torsion field of a newly selected global curve
is substituted, and no equality q_0=3^30 is used.

All approved checks pass without a correction to the result.
The audit validates a conditional known-result specialization,
not a native-definition verdict or progress beyond the imported
theorems. The intended model convention, other selected places
and orders, actual inputs/actions, pilot transport, essentiality
and original finite B>=A remain open. ATTEMPTS/028 remains a
qualified retained-place stop; ATTEMPTS/022,025,026,027 are
unaffected. No mathematical script or numerical certificate was
needed, and full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage of the selected-model condition,
the ramified-twist reduction theorem and this specialization has
not been checked. No absence claim is made. Precise primary
citations above supply the standard inputs; the explicit root and
pointed-isomorphism identities are the necessary applicability
checks. No mathematical script or numerical evidence is used.
