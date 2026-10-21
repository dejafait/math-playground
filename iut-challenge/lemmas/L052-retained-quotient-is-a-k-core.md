# L052 — The retained quotient is a K-core

## Hypotheses

Use the same existential pointed elliptic curve E_0/Q selected in L048,
at fixed M>=max(M_tors,31), and L045's embedded number fields
F=Q(zeta_60,E_0[30]) and K=D=F(E_0[7]). Division fields contain both
coordinates of every geometric torsion point. Put X_K=E_0,K minus its
origin and C_K=[X_K/{±1}], the stack quotient by pointed inversion.
Use the fixed absolute valuation v_3(3)=1. L048 establishes
v_3(j(E_0))=-30. No equality q_0=3^30 is assumed.

Here K-core means terminality of C_K in overline-Loc_K(C_K), with
K-morphisms, as in Mochizuki's Definition 2.1/Remark 2.1.1 cited below.
It does not mean terminality of X_K or of the coarse quotient scheme.

## Conclusion

C_K is a K-core. In the qualified May 2020 reproduction of IUT I,
Definition 3.1(d), this verifies the coricity condition on the unadorned
C_K for the retained curve and full 7-division field.

This application of known results passes the separate 2026-10-12 audit
below, which supplies the missing explicit compactification check.
It proves neither sufficient initial theta data nor an essential IUT
flaw. The level covering, cusp and full selected data, actual input and
action realization, pilot transport, essentiality and original finite
B>=A remain unresolved.

## Proof

### Imported results and scope

Reuse the IMPORT assessment
`drafts/literature/2026-10-12-native-k-core-four-exception-application.md`
and its completed primary extraction in
`drafts/2026-10-12-native-k-core-source-notes.md`.

Shinichi Mochizuki, *The Absolute Anabelian Geometry of Canonical Curves*,
Documenta Mathematica, Extra Volume (2003), pp.609–640,
[author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Canonical%20Liftings.pdf),
section 2, Definition 2.1/Remark 2.1.1, Proposition 2.3(i,ii), and
Definition 2.6(ii)/Proposition 2.7 (author-PDF printed pp.8–11,14–15),
provides the following inputs. The author-PDF pagination is distinguished
from journal pagination; no unverified byte identity is asserted.

* A punctured hemi-elliptic orbicurve is precisely the stack quotient
  [(E minus origin)/{±1}]. Over an algebraically closed field of
  characteristic zero, a non-arithmetic such orbicurve is a core
  (Proposition 2.7).
* For geometrically normal, geometrically connected, finite-type X/k,
  coricity is equivalent to coricity after separable closure
  (Proposition 2.3(i)). For a hyperbolic orbicurve over algebraically
  closed characteristic-zero k, it is equivalent after an algebraically
  closed field extension (Proposition 2.3(ii)).

Arithmeticity here is the arithmetic uniformizing-group property, not
arithmeticity of coefficients. Section 2's finite-etale-cover and
stack-quotient categories (including Remarks 2.1.2–2.1.3) concern a
common-cover class. For a finite-etale cover of hyperbolic orbicurves
over C, uniformizing groups are related by finite index, so their
arithmeticity agrees: arithmetic Fuchsian groups are defined up to
commensurability. This is the finite-index applicability argument;
no classification or core theorem is reproved.

Jeroen Sijsling, *Canonical models of arithmetic (1;infinity)-curves*,
[arXiv:1707.01158v2](https://arxiv.org/pdf/1707.01158v2), PDF dated
7 July 2017, introduction/Lemma 1.1.1 and section 3.1, Table 4, p.11,
gives the complete four arithmetic once-punctured genus-one classes
and their final pointed elliptic models. The exact table is also
readable in the [versioned HTML rendering](https://arxiv.org/html/1707.01158v2#S3.SS1).
The exceptional j-values, in table order, are

2^14*31^3/5^3, 2^2*73^3/3^4, 1728, 0.

Use the final X(Gamma) models, not the intermediate isogenous models.
Takeuchi's original classification is cited by these inspected sources;
its proof was not separately inspected and is not being reproduced.
The four-class exhaustion and core criterion are imported from the
inspected statements.

### Exact exclusion for the same curve

The valuations of the four rational exceptional values under the fixed
embedding into Omega, with v_3(3)=1, are respectively

0, -4, 3, +infinity.

Indeed 2,31,5 and 73 are 3-adic units, 1728=2^6*3^3, and the final
value is zero. None equals -30. Hence L048's j(E_0) is different from
every table value. This is an exact comparison of rational algebraic
invariants, with no approximation to E_0's coefficients or j-value.
If j(E_0) equalled one of these constants over any extension, it would
already be that same rational number over Q and would have the same
valuation in Omega, a contradiction.

### Orbicurve and categorical hypotheses

L048's E_0 is nonsingular with its Q-rational origin. Thus over K it
is a smooth geometrically connected genus-one curve, and X_K is its
smooth geometrically connected finite-type open complement of one
point. It has hyperbolic type (1,1), since 2*1-2+1=1>0.

The constant group {±1} is finite etale in characteristic zero. Its
quotient stack C_K is Deligne–Mumford, with representable finite-etale
surjective atlas X_K -> C_K: pulling this map back to an object of the
quotient stack gives its defining {±1}-torsor. The fixed points of
inversion cause no ramification of this stack atlas. Smoothness and
normality are etale-local, so C_K is geometrically smooth and normal.
The surjective image of each geometrically connected X_K remains
connected; the finite group quotient is of finite type. This checks
the geometric hypotheses of Proposition 2.3(i).

More explicitly, the geometric coarse compactification E/{±1} has
genus zero: in a Weierstrass equation inversion fixes x and negates
the y-coordinate after completing the square, and x gives the
degree-two map to P^1. Removing the origin removes one branch value.
The other three geometric nonzero 2-torsion points give three order-two
orbifold points. Inversion has no other fixed points and trivial
generic stabilizer. The orbifold Euler characteristic is
2-1-3*(1-1/2)=-1/2. To deduce hyperbolicity in the precise sense
of Definition 2.2, use the compactification and positive log-dualizing
degree verified in the separate audit below; the Euler characteristic
alone does not exhibit the required scheme structure at infinity.
C_K is exactly the punctured hemi-elliptic object in Definition 2.6(ii).

### Arithmeticity and transfer to K

K is a number field: E_0's finite geometric 7-torsion consists of
algebraic points, so adjoining their finitely many coordinates to
L045's number field F is finite. Choose an algebraic closure Kbar
and an embedding Kbar -> C. This is a complex embedding of algebraic
number fields, not an identification of Omega with C.

X_C is a once-punctured genus-one curve, whose invariant is the same
rational j(E_0). If its uniformizing group were arithmetic, Sijsling's
exhaustive four-class table would give one of the four exceptional
j-values. The exact exclusion above rules this out. The finite-etale
stack cover X_C -> C_C identifies their groups up to finite index,
so C_C is non-arithmetic as well. Proposition 2.7 consequently makes
C_C a C-core.

Apply Proposition 2.3(ii) to C_Kbar and the algebraically closed
extension Kbar -> C. Its characteristic-zero and hyperbolicity
hypotheses have been checked. It follows that C_Kbar is a Kbar-core.
As K has characteristic zero, its separable closure is an algebraic
closure. Proposition 2.3(i), with the verified geometric normality,
connectedness and finite type, now gives that C_K is a K-core.

All four comparisons and both transfer tests pass. Only L045 and
L048 are direct local lemma inputs; the source classification and
criteria are cited mathematical inputs. L051 is a separate reduction
condition, L049 background and L050 a contrasting descent predicate,
none of which is used here. The native identification retains the
May 2020 reproduction/version qualification documented in the source
notes. No claim about the level covering, cusp data, all selected
places or numerical comparison follows from terminality of C_K.
The historical stops in ATTEMPTS/022,025,026,027,028 are unchanged.

### Separate critical audit — 2026-10-12

**Verdict and coverage.** The conclusion passes under the prior IMPORT
assessment `drafts/literature/2026-10-12-retained-quotient-core-critical-audit.md`.
The repair is an explicit verification of Definition 2.2's compactification
hypothesis, formerly asserted from an Euler-characteristic calculation.
It is part of the approved applicability audit, not a new core criterion.
No theorem reproof, curve reselection or new direct lemma input is needed.
The primary passages checked are the cited CanLift section 2, printed
pp.8–11,14–15, and Sijsling v2 introduction, Lemma 1.1.1 and final Table 4.

**Compactification with a scheme cusp.** Write E=E_0,K, O for its origin,
and P=E/{±1}=P^1_K for the coarse quotient. Let b_infinity be the image
of O and B the reduced degree-three divisor of images of the nonzero
2-torsion. These divisors are defined over K and disjoint; nonsingularity
and characteristic zero make B geometrically reduced. Put
U=P minus B and W=P minus (B union {b_infinity}). Over W the involution
on E is free, so the quotient stack is canonically the scheme W.
Glue C_K over P minus {b_infinity} to U along this W. Denote the
result by Cbar. This is gluing along open substacks, so Cbar is a smooth
one-dimensional Deligne–Mumford stack, agrees with C_K away from its
new boundary D={b_infinity}, and agrees with the scheme U near D.
It is geometrically connected and generically a scheme.

For completeness, properness follows locally over the two displayed
opens of P. Over U the map Cbar -> P is the identity. Over
P minus {b_infinity}, its source is [ (E minus O)/{±1} ]; the finite
surjective atlas E minus O has finite, hence proper, composite to that
open of P. The quotient map is finite type and has finite diagonal:
locally its isomorphism relation is the union of the graphs of the two
group elements. Universal closedness follows from the proper composite
and the surjectivity of the atlas, also after every base change.
Thus this quotient is proper over the open. Properness is local on
the target, giving properness of Cbar -> P, hence of Cbar over K.
In particular this construction does not use [E/{±1}] as Cbar: that
different proper stack has order-two inertia at O's image and is not
scheme-like there.

The atlas E minus O -> C_K extends to a representable finite degree-two
map f:E -> Cbar: on the inverse image of U use the coarse quotient,
and on E minus O use the stack quotient atlas. These maps agree on
the free locus. Away from O this map is etale as a stack map. At O,
choose a local parameter z anti-invariant under inversion (replace any
parameter s by (s-[-1]^*s)/2). Since inversion acts by -1 on the tangent
line, z is a parameter and the completed coarse coordinate is t=z^2.
Thus f^*D=2O, while the relative differential vanishes to order one
at O and nowhere else. Equivalently dt/t pulls back to 2dz/z.
The local differential identities glue to

f^*(omega_Cbar/K(D)) = omega_E/K(O).

The right-hand side has degree 1 because E has genus one. Degree of
a line bundle under a finite degree-two map is multiplied by two
(equivalently compute stack degree by this finite scheme cover).
Consequently deg(omega_Cbar/K(D))=1/2>0. This explicitly verifies all
parts of Definition 2.2; the construction and calculation survive
both geometric base changes used in the proof.

**Exception list and categorical arithmeticity.** Sijsling's final
Table 4 concerns X(Gamma), with its one cusp at infinity; intermediate
isogenous models in section 3.1 do not replace those models. Its
exhaustion applies to the type (1,1) curve X_C. Direct factorization
gives v_3(2^14*31^3/5^3)=0, v_3(2^2*73^3/3^4)=-4,
v_3(1728)=3 and v_3(0)=+infinity. L048's rational j has valuation
-30, so equality with any exception is impossible in any embedding.
This excludes arithmeticity without invoking non-CM or algebraicity
of coefficients as a substitute.

CanLift Remark 2.1.2 identifies categorical and uniformizing arithmeticity
for X_C. Proposition 2.7's proof explicitly uses equality of the
common-cover categories for a punctured hemi-elliptic quotient and its
punctured elliptic double cover. Here that cover is precisely the
representable finite-etale atlas X_C -> C_C, not the ramified map to
the coarse line. Thus the non-arithmetic conclusion applies in the
categorical sense required by Proposition 2.7. Its hypotheses now give
coricity of C_C. No implication from rational coefficients is used.

**Both transfers and retained fields.** L045 supplies the number field
F. The full finite 7-torsion coordinate set of the same E_0 is algebraic,
so K=F(E_0[7]) is a number field. The finite-etale atlas verifies geometric
smoothness, normality and connectedness, finite type, dimension one and
trivial generic inertia for C_K. The compactification above verifies
hyperbolicity over Kbar. Embed the algebraic closure Kbar into C; both
fields are algebraically closed of characteristic zero. The reverse
direction of Proposition 2.3(ii) therefore carries C_C's coricity to
C_Kbar. Since characteristic zero makes Kbar a separable closure,
the reverse direction of Proposition 2.3(i) carries it to C_K. Neither
direction is an unsupported descent of a chosen morphism. The chosen
complex embedding need not respect the earlier 3-adic topology; only
equality of the rational j-invariant was transported.

The only direct local inputs remain L045,L048. Their audited statements
retain the same E_0 and K; K is not its completion N, and q_0 is not
identified with 3^30. This repairs an omitted proof obligation and
validates a known-result application, with no claim of progress beyond
the inspected sources. The qualified May 2020 native identification
and every unresolved bridge stated in the conclusion remain unchanged.

## Mathlib

Full matching Mathlib coverage for the four arithmetic classes,
punctured-hemi-elliptic core criterion and categorical base-field
transfer has not been checked. No absence claim is made. The exact
valuation comparisons and quotient applicability arguments use the
cited primary results; no mathematical script or numerical evidence
is needed.
