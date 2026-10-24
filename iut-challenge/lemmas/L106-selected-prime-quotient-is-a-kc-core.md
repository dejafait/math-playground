# L106 — The selected-prime quotient is a K_C-core

## Hypotheses

Retain the one member, ordering and prime ell>=7 selected in L105,
within L089's fixed family, domains and algebraic closure. Use L090's
literal pointed curve and full-coordinate field and L092's normal closure:

    E_o: V^2=X(X-1)(X-t_o),
    F=G_o=Q(t_o)(iota,E_o[15]), iota^2=-1,
    C_o=G_o^nor, K=K_C=C_o(E_o[ell]).

Adjoin both coordinates of every geometric ell-torsion point in the
same fixed closure. Put X_K=(E_o)_K minus its origin O and
mathcal C_K=[X_K/{±1}], the quotient stack by pointed inversion.
The invariant j(E_o) is rational; L089 and L105 retain
v_3(j(E_o))=-30 with the absolute normalization v_3(3)=1, and
L090's pointed geometric comparison identifies this invariant with
that of the selected original Q-curve.

Use K-coricity in Mochizuki's Definition 2.1/Remark 2.1.1 below:
mathcal C_K is terminal in overline-Loc_K(mathcal C_K), with
K-morphisms. Neither its coarse quotient nor X_K is the tested core.

## Conclusion

mathcal C_K is a K_C-core for this unchanged member and selected prime.
This imports the known punctured-hemi-elliptic criterion and verifies
its hypotheses on the actual object. It supplies only the unadorned
quotient's core predicate in the qualified native clause-(d) dictionary;
it does not construct native initial theta-data over C_o.

The separate step427 critical audit below validates this application. Native covering,
cusp and section data, a III situation, P7, exact generation/full repair,
the relative factor-four excess, actual input/action/factorization/pilot
transport, source authentication/def= qualifications, essentiality and
original finite B>=A remain unresolved. No complete flaw candidate or
progress beyond the imported general results is claimed.

## Proof

### Known inputs, duplicate check and bounded target

Use the invocation-start IMPORT assessment
`drafts/literature/2026-10-23-selected-prime-quotient-core-application.md`.
Its primary coverage and the completed extraction in
`drafts/2026-10-12-native-k-core-source-notes.md` are reused without
another source refresh. L052's separate audit supplies a worked
applicability method, including the formerly omitted compactification
check; its conclusion for the old curve and prime seven is not a
premise here. ATTEMPTS/029 parks redundant source approval, not this
changed-member application; ATTEMPTS/034–035's cyclic-normality and
authentication stops are not reopened.

Import Shinichi Mochizuki, *The Absolute Anabelian Geometry of Canonical
Curves*, Documenta Mathematica, Extra Volume (2003), 609–640,
[author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Canonical%20Liftings.pdf),
section 2, Definition 2.1/Remarks 2.1.1–2.1.3, Definition 2.2,
Proposition 2.3(i,ii), Definition 2.6(ii) and Proposition 2.7,
author-PDF printed pp.8–11,14–15. Retain that pagination/version
qualification; author-PDF/journal byte identity is not asserted.
The needed statements are:

- A non-arithmetic punctured hemi-elliptic orbicurve
  [(E minus O)/{±1}] over an algebraically closed characteristic-zero
  field is a core (Definition 2.6(ii), Proposition 2.7).
- For a geometrically normal, geometrically connected finite-type
  object over k, coricity is equivalent to coricity over its separable
  closure (Proposition 2.3(i)).
- For a hyperbolic orbicurve over an algebraically closed field of
  characteristic zero, coricity is equivalent after an algebraically
  closed field extension (Proposition 2.3(ii)). Definition 2.2 requires
  a proper orbicurve compactification, scheme structure near its
  boundary and positive log-dualizing degree.

The finite-etale common-cover categories in section 2 identify the
arithmeticity of a punctured elliptic curve and its hemi-elliptic
quotient; Proposition 2.7's proof uses precisely this identification.
Over C, Remark 2.1.2 relates it to arithmeticity of uniformizing
Fuchsian groups. A representable finite-etale cover gives a finite-index
inclusion of those groups. Arithmeticity is a commensurability property,
so it agrees for these two objects. We verify the actual cover below.

Import Jeroen Sijsling, *Canonical models of arithmetic (1;infinity)-curves*,
[arXiv:1707.01158v2](https://arxiv.org/pdf/1707.01158v2), PDF dated
7 July 2017, introduction/Lemma 1.1.1 and section 3.1, final Table 4,
p.11; the table is readable in the
[versioned HTML](https://arxiv.org/html/1707.01158v2#S3.SS1).
These give the complete four arithmetic once-punctured genus-one
classes with final X(Gamma) invariants

    2^14*31^3/5^3, 2^2*73^3/3^4, 1728, 0.             (1)

Intermediate isogenous models are not substituted for this final table.
Takeuchi's original classification is a cited antecedent of the inspected
sources; its proof was not separately inspected or reproved. The HTML's
generated date does not change the versioned PDF's theorem date.

The main gap is original finite B>=A. This intermediate core condition
could remove one independent obstruction to a native construction over
C_o, leaving the other prerequisites above unresolved. The test is to
exclude all four values (1), exhibit the actual scheme-cusp geometry,
and check both field-transfer hypotheses. An exceptional invariant or
failed hypothesis would stop or narrow this application. No universal
criterion, classification or source theorem is reproved.

### All four exceptional invariants for the actual member

L105 retains the selected original curve's height-30 condition from
L089. L090's explicit pointed geometric isomorphism to E_o preserves j,
so j(E_o) is the same rational number with v_3(j(E_o))=-30. The four
values in (1) have respective absolute 3-adic valuations

    0, -4, 3, +infinity.                              (2)

For the first value 2,31,5 are units; for the second 2,73 are units
and the denominator has valuation four; 1728=2^6*3^3; and v_3(0)
is +infinity. None equals -30. Equality of j(E_o) with any rational
constant in (1) in an extension field would already be equality of
these rational numbers, contradicting (2) in the fixed 3-adic embedding.
Thus the exclusion is independent of the later complex embedding.
No coefficient approximation or non-CM criterion replaces this test.

### Stack atlas and compactification with a scheme cusp

L090 gives t_o different from 0,1. Thus E=(E_o)_K is a smooth
geometrically connected elliptic curve with K-rational origin, and
X=E minus O is a smooth geometrically connected finite-type curve.
Characteristic zero makes the constant group {±1} finite etale.
The quotient mathcal C=[X/{±1}] is a one-dimensional Deligne–Mumford
stack; X -> mathcal C is representable finite-etale, surjective of
degree two, because its pullback to any quotient-stack object is the
defining {±1}-torsor. Fixed points of inversion do not ramify this
stack atlas. Geometric smoothness and normality follow etale-locally,
and geometric connectedness follows from the surjective connected
atlas after every algebraically closed extension. Finite type descends
along this atlas. The finite group relation also gives finite diagonal.

The coarse quotient P=E/{±1} is P^1_K, with coordinate X in the
Legendre equation. Its branch values are 0,1,t_o and b_infinity,
the image of O. Let B={0,1,t_o} be the reduced degree-three divisor.
The three nonzero two-torsion points have inertia of order two;
all other points of mathcal C have trivial inertia. In particular
mathcal C is generically a scheme and is exactly the punctured
hemi-elliptic object of Definition 2.6(ii).

Put U=P minus B and W=P minus (B union {b_infinity}). The inversion
action is free over W, so mathcal C restricted to W is the scheme W.
Glue mathcal C, over P minus {b_infinity}, to the scheme U along W.
Call the resulting stack mathcal Cbar, with boundary D={b_infinity}.
It is smooth of dimension one and agrees with the scheme U near D.
All these opens, their identifications and D are defined over K.

Here is an explicit properness check. Over U the map mathcal Cbar -> P
is the identity. Over P minus {b_infinity}, its source is [X/{±1}],
whose atlas X has finite composite to that open of P. The quotient
is of finite type with finite diagonal (the finite group relation),
hence separated. Its universal closedness follows from that finite
composite and the surjective atlas, after every base change: the image
of a closed substack is the image of its closed inverse image in X.
It is therefore proper over the open. Properness is local on the
target, so mathcal Cbar -> P is proper, and mathcal Cbar is proper
over K. It is geometrically connected and generically a scheme.
The full quotient [E/{±1}] would retain inertia at b_infinity and is
not the compactification just constructed.

The maps E minus O -> mathcal C and E restricted over U -> U agree
on their common free locus. They glue to a representable finite
degree-two map f:E -> mathcal Cbar, as finiteness and representability
are local on the target. Away from O it is the finite-etale stack
atlas. At O choose a parameter s; inversion acts as -1 on the tangent
line, so z=(s-[-1]^*s)/2 is an anti-invariant parameter. Completed
local coordinates on the scheme neighborhoods are z and t=z^2.
Thus f^*D=2O and the ramification divisor is exactly O. Equivalently,
dt/t pulls back to 2dz/z. The differential identities give

    f^*(omega_(mathcal Cbar/K)(D)) = omega_(E/K)(O).

The right-hand line bundle has degree one, since E has genus one.
Degree under this finite degree-two scheme cover multiplies by two
(or defines the rational stack degree), so

    deg(omega_(mathcal Cbar/K)(D))=1/2>0.              (3)

This verifies Definition 2.2, including scheme structure at the cusp,
rather than inferring it from an Euler characteristic alone. The atlas,
gluing, differential calculation and degree remain valid after both
geometric base changes used next.

### Arithmeticity and both transfers over the actual K_C

L090 defines a number field G_o and L092 its finite normal closure C_o.
The geometric ell-torsion of the same E_o is finite etale in
characteristic zero; its finitely many coordinates are algebraic over
C_o. Hence the full field K=C_o(E_o[ell]) is a number field. This is
neither a completion nor an old prime-seven division field. No image,
disjointness or extra normality premise is needed.

Choose an algebraic closure Kbar and an embedding Kbar -> C, where
C here denotes the complex numbers. It need not respect the earlier
3-adic embedding into Omega. The once-punctured genus-one curve X_C
has invariant j(E_o). If its uniformizing group were arithmetic, the
complete four-class list would force this invariant to equal a value
in (1), contrary to (2). Thus X_C is non-arithmetic. Its actual
representable finite-etale double cover of mathcal C_C, checked above,
identifies their common-cover arithmeticity as in the cited section 2.
Consequently mathcal C_C is non-arithmetic in the categorical sense
required by Proposition 2.7. It is a C-core by that proposition.

Apply Proposition 2.3(ii) to the hyperbolic orbicurve mathcal C_Kbar
and the algebraically closed characteristic-zero extension Kbar -> C.
The hyperbolicity check is (3) with its scheme cusp. The reverse
direction of the equivalence makes mathcal C_Kbar a Kbar-core.
Characteristic zero identifies Kbar with a separable closure of K.
The geometric normality, connectedness and finite type of mathcal C_K
were checked using its actual atlas. The reverse direction of
Proposition 2.3(i) therefore makes mathcal C_K a K-core, as claimed.
Neither step is an unsupported descent of a chosen comparison map.

All four exceptions and both transfers pass for the one retained
member. L105's large-image conclusion is an independent prerequisite,
not a core-criterion hypothesis. No change of prime, curve, field
prescription, level cover or marked cusp was used. This is an
application of known results, with no new classification or full
native-data assertion. The source/version qualifications and the
independent unresolved obligations in the conclusion remain intact.

### Separate critical audit — 2026-10-23, step427

This audit uses the invocation-start IMPORT assessment
`drafts/literature/2026-10-23-selected-prime-quotient-core-critical-audit.md`.
It checks the full application above, not the classification's proof.
The primary defining passages were checked against CanLift section 2,
Definition 2.1/Remarks 2.1.1–2.1.3, Definition 2.2, Proposition 2.3
with proof, and Definition 2.6(ii)/Proposition 2.7 with its branch cases;
Sijsling's introduction and final Table 4 were checked at the versioned
URLs cited above. These checks reuse approved coverage and do not
constitute a new literature assessment. All version qualifications remain.

**The actual invariant and field.** L089's surviving original member
retains the height-30 condition at three. L105 chooses within that family
once, and L090's displayed mutually inverse pointed geometric maps give
the same j for the literal E_o. They need not descend to T or C_o for
this invariant equality. Thus the rational number tested really has
v_3=-30. Direct valuation of each of the four final constants gives
0,-4,3,+infinity, respectively; none is discarded by a non-CM shortcut.
Since these are rational equalities, a new complex embedding cannot
undo their exclusion. L092 supplies a finite C_o and E_o is defined over
its subfield G_o. Full geometric ell-torsion is finite in characteristic
zero, so its full coordinate field K_C is finite over C_o. No assertion
about its degree, completion or image is required. Neither an old
prime-seven field nor a new member has entered the application.

**Atlas, separatedness and the cusp.** For a test scheme T carrying an
object of [X/{±1}], the pullback of X is its defining torsor, finite
etale of rank two over T. This checks representability and etaleness
even at the three interior fixed points. Smoothness, normality and
finite type descend from this atlas; geometric connectedness follows
from its surjectivity and the geometric connectedness of X. The free
open W is dense. The Legendre x-map is finite of degree two to P, so
X is finite over P minus infinity. To make the diagonal check explicit,
its pullback to X times_P X is the union, indexed by the two group
elements, of their graphs. Each graph is closed because X is separated
over P, and is a closed immersion into X times_P X. Their finite
disjoint union is finite. Hence the quotient has finite relative
diagonal. For every base change of P minus infinity, the image of a
closed substack equals the image of its closed inverse image in the
finite atlas over that base; the latter image is closed. This proves
universal closedness as well as separatedness and finite type.

The two target opens P minus infinity and U cover P. On their
intersection W the quotient is the scheme W, and the gluing map is
the identity over P. Consequently the gluing is an algebraic smooth
stack, and the proper morphisms just checked glue to a proper morphism
to P. It is proper over K. Its added point is the ordinary K-rational
point of U, so its boundary is a reduced scheme divisor. The three
interior stabilizers remain; the stabilizer at O in the full proper
quotient has not been retained by mistake.

**Degree and logarithmic differentials.** The source opens E minus O
and the inverse image of U cover E. Their maps agree on the free
overlap, giving the stated f. On the first target open f is the rank-two
torsor; on U it is the degree-two x-map. Both are representable finite
flat of rank two. Near the boundary, the anti-invariant parameter z
exists since 2 is invertible and inversion has tangent action -1.
The completed invariant ring is K[[z^2]], so f has ramification index
two at O. Elsewhere f is etale as a stack morphism, including above
the three stack points. Thus the differential divisor is O, with no
extra terms at nonzero two-torsion. The ordinary differential pullback
and f^*D=2O give

    f^*omega_Cbar = omega_E(-O),
    f^*(omega_Cbar(D)) = omega_E(O).

Equivalently, the logarithmic local generator pulls back as
dt/t=2dz/z. The right side is a generator because 2 is a unit.
The finite flat rank-two cover multiplies line-bundle degrees by two,
where the proper stack degree counts stabilizers. Since the degree on
E is one, the required degree is exactly 1/2, strictly positive. These
local checks and the gluing are preserved by geometric base change.
This verifies every part of the hyperbolic-orbicurve hypothesis.

**Arithmeticity and reverse transfers.** The complex punctured elliptic
curve has signature (1;infinity), so the final four-class table applies
to precisely this object. The finite-etale stack double cover puts it
and the quotient in the same common-cover category, exactly as used
in CanLift Proposition 2.7's proof. The categorical arithmeticity test
therefore passes; rational coefficients are not an arithmeticity test.
The non-arithmetic hemi-elliptic quotient is a complex core by the
imported criterion. Proposition 2.3(ii) is an equivalence, and its
algebraically closed characteristic-zero and hyperbolicity premises
hold for Kbar embedded in C. Its reverse direction gives the Kbar-core.
Proposition 2.3(i) is also an equivalence for the geometrically normal,
geometrically connected finite-type stack already checked. Since
Kbar is a separable closure in characteristic zero, its reverse
direction gives the K_C-core. This uses neither a descent of an
arbitrarily chosen map nor a compatibility of complex and 3-adic places.

**Verdict and limits.** The audit passes without changing the statement
or its mathematical inputs. The explicit diagonal and finite-flat
checks above confirm the existing construction; they reveal no failed
hypothesis or new general theorem. This is validation of a known-result
application, not progress beyond the imported results. L052 remains a
method comparison, not a direct input. L089,L090,L092,L105 are the
unchanged direct inputs in the DAG. The audit supersedes the overview's
pending-audit wording; its argument and assembly need no change.
Native covering/cusp/section data, III, P7, exact generation/full repair,
the relative factor-four excess, source qualifications, actual
input/action/factorization/pilot, essentiality and finite B>=A remain
open. Ell-integrality was not used. No complete flaw candidate is claimed.

## Mathlib

Full matching Mathlib coverage for the arithmetic four-class list,
punctured-hemi-elliptic core criterion and categorical base-field
transfers is unchecked, not known absent. No formal verification is
claimed. The proof uses the cited primary theorems and exact invariant,
stack-geometry and field-hypothesis checks; no mathematical script or
numerical certificate is needed.
