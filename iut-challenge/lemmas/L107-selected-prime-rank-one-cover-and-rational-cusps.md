# L107 — Same-selected-prime rank-one cover and rational cusps

## Hypotheses

Fix exactly one member, ordering o, literal elliptic curve E_o,
G_o, C_o=G_o^nor and prime ell>=7 supplied by L105, in its fixed
algebraic closure. In particular

    E_o: V^2=X(X-1)(X-t_o),
    G_o=Q(t_o)(iota,E_o[15]), iota^2=-1.

Put K_C=C_o(E_o[ell]), adjoining both coordinates of every geometric
ell-torsion point, and let E=(E_o)_(K_C), with origin O. No member,
ordering, prime or base field is replaced during this construction.
Choose any one-dimensional F_ell-subspace U of the K_C-valued points
of E[ell], regarded
as a constant subgroup scheme of E. No definition over C_o or local
Tate-line prescription is required. Let X=E minus {O}.

The original algebraic statements below use characteristic zero and
full K_C-rational ell-torsion. L105's large-image conclusions and the
quotient-core conclusion of L106 are not premises for those statements.
The additional global application uses L106's core conclusion over
this same K_C. It makes the native dictionary F=C_o, K=K_C;
it does not assert that C_o satisfies every initial-data clause.

## Conclusion

There exist pointed K_C-isogenies

    alpha:E -> B=E/U, psi:B -> E, psi alpha=[ell],
    deg(alpha)=deg(psi)=ell.

The complete scheme-theoretic origin fiber V=ker(psi) is the constant
order-ell group alpha(E[ell]), isomorphic to (Z/ell Z)_(K_C).
Consequently

    Y=B minus V -> X

is a geometrically connected finite-etale Galois cover of degree ell,
with constant deck group V acting by translation. Its geometric
monodromy surjects onto V. All ell cusps of Y in B are K_C-rational.
The whole decomposition group of the original cusp O of X has trivial
image in V, including both inertia and residue-Galois action.

Inversion induces the following 2-cartesian square, with its natural
2-commutativity isomorphism:

    Y  ----------------------> X
    |                          |
    v                          v
    [Y/{+1,-1}] -------------> [X/{+1,-1}].

The bottom map is representable finite-etale, finite locally free of
degree ell. These are quotient stacks, retaining inversion stabilizers.

The original algebraic specialization is validated by the separate
step431 critical audit below. The additional step433 application
establishes the global clause-(d) covering predicates in the qualified
IUT I reproduction: the actual arithmetic elliptic-quotient
factorization, the types (1,ell-tors) and (1,ell-tors)±, the K_C-core
[X/{±1}], all three cartesian diagrams over F=C_o, and the recalled
geometric theta subgroups as full profinite inverse images. This
additional application is validated by the separate step435 audit below.

Neither assertion supplies local graph type, native cusp label,
compatible arithmetic splitting, place section or complete initial
data. No numerical comparison or essential IUT flaw follows.

## Proof

### General imports and the specialization being tested

Use the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-23-selected-prime-rank-one-cover-and-cusps.md`.
It already compares the following general-primary inputs and their
relevant proof cases; they are imported rather than reproved here.

- [Sutherland, MIT 18.783 Lecture 5, 26 September 2023](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
  Corollaries 5.2,5.10, Theorems 5.8,5.11, pp.2-6, and Theorem
  5.25, p.14: subgroup quotients and their base-field qualification,
  separable isogeny kernels and fibers, and deg([n])=n^2 with
  separability when n is prime to the characteristic. In particular
  separable isogenies here are unramified finite maps of smooth curves.
- [Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
  II.1.7, p.49, supplies the isogeny factorization from kernel
  inclusion; II.6.3, p.70, gives geometric prime-to-characteristic
  n-torsion as a free rank-two Z/n-module.
- Stacks Project [Theorem 58.6.2, tag 0BND](https://stacks.math.columbia.edu/tag/0BND)
  and [Section 58.7, tag 03SF](https://stacks.math.columbia.edu/tag/03SF)
  give the finite-etale monodromy correspondence, its pullback
  compatibility and connected Galois-cover criterion.
  [Lemma 10.153.7, tag 04GK](https://stacks.math.columbia.edu/tag/04GK)
  gives the finite-etale equivalence over a henselian local ring
  and its residue field.
- Stacks Project [Proposition 95.15.3, tag 04UV](https://stacks.math.columbia.edu/tag/04UV)
  describes quotient stacks by equivariant maps from torsors.
  [Lemma 100.3.1, tag 04ZP](https://stacks.math.columbia.edu/tag/04ZP)
  descends representability by algebraic spaces; [Lemma 100.3.3,
  tag 04XD](https://stacks.math.columbia.edu/tag/04XD) and
  [Section 100.3, tag 04XB](https://stacks.math.columbia.edu/tag/04XB)
  descend finiteness, etaleness and finite local freeness.

L053 provides an audited method on different objects; its conclusion,
Tate-selected line and local point-group coordinates are not transferred.
No general quotient, monodromy or descent theorem needs a reproof.
ATTEMPTS/030's rank-two/full-multiplication obstruction is respected:
the proposed covering map is psi of degree ell, not [ell] of degree
ell^2. The other parked routes screened in the assessment are unused.

The main gap remains finite B>=A. Passing this bounded test supplies
one global cover prerequisite for a later native-data comparison.
The test requires the actual degree, entire rational cusp fiber,
geometric connectedness, whole cusp decomposition and stack square.
Failure of any hypothesis would require narrowing this construction;
passing does not discharge its independent local/native obligations.

### The line, quotient, complementary factor and entire fiber

The characteristic-zero field K_C contains the complete geometric
ell-torsion by its full-coordinate definition. Milne II.6.3 therefore
identifies the K_C-valued points of E[ell] with F_ell^2. In particular the stipulated
line U exists. The finite-etale scheme E[ell] is split over K_C;
the union of the ell rational points of this line is a closed
constant subgroup scheme. It is Galois invariant over K_C, which
checks the quotient theorem's field-of-definition hypothesis.

The subgroup quotient gives the pointed K_C-isogeny alpha:E -> B,
with kernel U and degree ell. Since U is a subgroup scheme of
ker([ell]), Milne II.1.7 supplies the unique pointed factor psi
with psi alpha=[ell]. If the factorization is first taken over
the algebraic closure, uniqueness makes it invariant under G_(K_C)
and hence defined over K_C. Degree multiplicativity gives

    deg(psi)=deg([ell])/deg(alpha)=ell^2/ell=ell.

Characteristic zero makes both isogenies separable; the imported
isogeny results make them finite-etale. Thus ker(psi) is reduced
and has exactly ell geometric points. For every T in E[ell],
psi(alpha(T))=O. The restriction of alpha to E[ell] has kernel U,
so its image has ell^2/ell=ell points and is contained in ker(psi).
Equality follows on geometric points, and also on subgroup schemes
because both are finite-etale. Every image point alpha(T) is
K_C-rational, since alpha and T are defined there. Hence

    V=alpha(E[ell]) is canonically isomorphic to E[ell]/U

is a constant order-ell subgroup scheme of B, and the complete
fiber over O is a disjoint union of ell copies of Spec(K_C).
This asserts rationality of that fiber, not full rationality of
B[ell]. Its origin is O_B=alpha(O); any P outside U gives a
nonzero rational cusp alpha(P), without prescribing a local label.

### Puncturing, deck transformations and geometric monodromy

Removing the entire inverse image V of O makes Y -> X a base
change of psi, so it is finite-etale of degree ell. Over an
algebraic closure of K_C, B is a smooth integral elliptic curve.
Removing finitely many points leaves a nonempty integral open curve,
hence Y is geometrically connected. Translations by V preserve Y
and commute with psi. If b,b' belong to the same geometric fiber,
their difference b'-b lies in V and is unique. Thus this action is
free and transitive on every geometric fiber, making Y -> X a
torsor for the constant group V. Its ell translations are all deck
transformations: on a connected finite-etale cover a deck map is
determined by one fiber point, by the monodromy correspondence, so
there can be at most ell of them.

Choose a geometric basepoint of X and one lift in Y. The V-torsor
gives its monodromy homomorphism pi_1(X) -> V, with the usual
basepoint qualifications. Geometric connectedness and the cited
correspondence say that the geometric fundamental group acts
transitively on the fiber. Its image is a subgroup of the regular
translation group V. Such a subgroup is transitive only if it
equals V, proving geometric surjectivity. The smooth proper
compactification B has precisely V as its removed points, already
proved rational over K_C; these are all ell cusps of Y.

### The whole original-cusp decomposition action

Let R be the henselization of the local ring of the smooth curve
E at its K_C-rational point O. This is a henselian DVR with residue
field K_C, not a valuation ring at a finite number-field place.
The pullback of B along Spec(R) -> E is finite-etale, and its
closed-fiber algebra is K_C^ell by the complete fiber calculation.
The henselian equivalence, Stacks tag 04GK, therefore identifies its
algebra over R with R^ell. In particular its restriction over the
punctured henselian trait Spec(Frac(R)) is the disjoint union of
ell trivial sheets.

The morphism Spec(Frac(R)) -> X identifies the local action on
this fiber with the original cusp decomposition action, up to
conjugation, by pullback compatibility of finite-etale monodromy.
The split cover just obtained has trivial action of the entire
local fundamental group. Thus the decomposition image in V is
trivial. This checks inertia as well as the residue-Galois part;
unramified extension over O alone would check only inertia.
Conjugating the choice of cusp decomposition group preserves
the trivial-image assertion. No arithmetic theta splitting or
chosen local line has entered this argument.

### Inversion: the actual fiber-product groupoid and descent

Let G={+1,-1} be the constant order-two group over K_C. Since
psi is a group homomorphism, it commutes with inversion and V is
inversion invariant. Thus G acts on Y and X and psi is equivariant.
These actions need not be free.

For a test K_C-scheme S, an object of

    X times_([X/G]) [Y/G]

consists of x:S -> X, a right G-torsor P on S with equivariant
map f:P -> Y, and an isomorphism theta from its induced X-torsor
object to the trivial torsor object associated to x. Use the
convention f(pg)=g^(-1)f(p). The latter trivial object is S times G
with map (s,g) -> g^(-1)x(s). In particular theta is an actual
torsor trivialization compatible with the X-maps. Its inverse at
the identity section gives a section p of P, and y=f(p) satisfies
psi(y)=x. Conversely a map y:S -> Y gives this object using the
trivial torsor and f(s,g)=g^(-1)y(s). Every given object is isomorphic
to the object recovered in this way via its theta.

An arrow in the fiber product must respect theta and theta', hence
carry their selected sections p and p' to each other. Equivariance
determines the torsor arrow uniquely from that section; compatibility
with f and f' holds exactly when y=y'. Thus these constructions give
inverse equivalences on objects and arrows, naturally in S. This
proves the displayed square is 2-cartesian, not just a bijection
on isomorphism classes. The quotient-stack stabilizers have not been
deleted: at any geometric point they are the actual subgroups of
the same G fixing that point. Equivariance sends each stabilizer
injectively into the stabilizer of its image.

The presentation X -> [X/G] is representable surjective etale,
since G is finite-etale. Pullback of the bottom map along this
presentation is exactly Y -> X by the just-proved square.
Stacks tags 04ZP and 04XD first give representability by algebraic
spaces and then the finite-etale, finite-locally-free properties.
The pulled-back finite locally free algebra has rank ell, so that
rank descends on this same surjective presentation. This proves
degree ell for the bottom map with all inversion stabilizers
retained. No coarse quotient substitutes for either stack.

### Boundary of the result

All tests in the approved algebraic target pass. The construction is
over the unchanged K_C for the unchanged E_o and selected ell, using
an arbitrary K_C-rational line. It chooses no line compatible with
any selected completion, and the rational cusp statement gives no
native graph-generator marking. Native graph/splitting/section data,
clause-(d) and III/P7, exact generation/full repair, the relative
factor-four excess, source authentication/def= qualifications, actual
input/action/factorization/pilot, essentiality and the original finite
B>=A remain unresolved. This is local notebook progress by known
sources, not progress beyond the sources checked or a complete flaw
candidate. The separate critical audit below validates this limited result.

### Separate critical audit — 2026-10-23, step431

**Scope and imports.** The limited statement passes the invocation-start
IMPORT assessment
`drafts/literature/2026-10-23-selected-prime-rank-one-cover-critical-audit.md`.
This checks applicability of the precise general theorems cited above;
it neither reproves them nor transfers L053's old-member verdict.
L105 supplies the one fixed member, ordering and prime ell>=7. Its
upstream L089,L090,L092 fix the nonsingular Legendre equation and
number fields in the same closure. Only characteristic zero and the
full-coordinate definition of K_C enter this cover argument. No
large-image, local reduction, ell-integrality or coricity premise is
needed. In particular L106 is not a dependency.

**Subgroup schemes and descent.** Milne II.6.3 applies because ell is
invertible in K_C. It gives ell^2 geometric points, all K_C-rational by
definition, and the finite-etale group scheme is therefore split.
The stipulated line is a subgroup scheme, not merely an abstract
subgroup of an unspecified geometric fiber. Its Galois invariance is
over K_C; no invariance over C_o is claimed. These are precisely the
base-field hypotheses of Sutherland Theorem 5.11.

The quotient alpha has this full kernel and degree ell. Kernel inclusion
in [ell] gives the unique factor psi by Milne II.1.7. Any geometric
factor and its Galois conjugate have the same composite with the
surjective alpha, hence are equal, checking the descent assertion.
The multiplication degree is ell^2, so degree multiplicativity gives
ell for psi, not ell^2. In characteristic zero the isogenies are
separable and unramified; as finite maps of smooth curves they are
finite etale. The ell distinct points alpha(E[ell]) lie in ker(psi).
That kernel is a reduced degree-ell scheme, so there are neither
missing geometric points nor hidden fiber multiplicities. Equality
after the algebraic-closure base change is equality of these finite
etale subgroup schemes over K_C. All image points are K_C-rational.
This establishes the complete constant kernel, without asserting that
the quotient curve has full rational ell-torsion. ATTEMPTS/030's
full-multiplication obstruction is not invoked as a rank-one cover.

**Connectedness and the entire cusp action.** After algebraic-closure
base change, B is integral and deletion of its finite kernel leaves a
nonempty integral curve. Thus the pulled-back finite-etale map Y -> X
is connected geometrically as well as arithmetically. Translation by
V acts simply transitively on each fiber: the unique translating
element is the difference of two points in that fiber. This verifies
the torsor claim and its full deck group by Stacks 0BND/03SF. Applying
the same correspondence geometrically, transitivity of the geometric
monodromy on the regular V-set forces its image to be V.

For the decomposition test, the ring R is the henselization at the
rational origin of the global smooth curve. It has residue field K_C.
The finite-etale pullback of B has residue algebra K_C^ell; Stacks
04GK makes the entire algebra R^ell. Its generic fiber is therefore
Frac(R)^ell. The original-cusp decomposition action is the image of
the local fundamental group of this punctured henselian trait in
pi_1(X), up to conjugation. Pullback compatibility in 0BND identifies
its action here with that on these trivial sheets. Thus the whole
image vanishes, with no need to choose a splitting of the local
arithmetic sequence or assume injectivity of its map into pi_1(X).
Rationality of every cusp and extension across O are both used; one
rational cusp or unramifiedness alone would not justify this conclusion.

**Fiber-product arrows and stack degree.** Inversion is equivariant
for the actual psi. In the quotient-stack description of 04UV, the
isomorphism theta in an object of the fiber product is part of the
data, not an equality of coarse images. Its inverse on the identity
section trivializes the torsor and selects p, hence y=f(p) with
psi(y)=x. Conversely y supplies exactly the trivial torsor object.
For an arrow, compatibility with theta forces p to map to p';
G-equivariance then determines the entire torsor map. Compatibility
with the Y-maps holds exactly when y=y'. These constructions commute
with pullback in the test scheme, verifying both full faithfulness
and essential surjectivity of the stated equivalence.

The atlas X -> [X/G] is representable surjective etale since G is
finite etale. Its pullback of the bottom map is the actual Y -> X.
Thus 04ZP tests representability by algebraic spaces and 04XD/04XB
descend finiteness, etaleness and finite local freeness; the locally
free rank on this same atlas is ell. Nonfree inversion introduces
no omitted hypothesis: trivialization removes automorphisms in the
fiber-product groupoid, while the two quotient stacks retain their
stabilizers. Equivariance only requires the induced inclusion of
stabilizers, not equality of those stabilizers or free actions.

**Verdict and limits.** Every assertion in the approved limited
statement passes, with no changed mathematical argument or direct
input. This is an imported-criteria applicability audit
(KNOWN_IMPORTED), not new mathematics beyond the checked sources.
It validates a global algebraic prerequisite only. The arbitrary
line has no prescribed local behavior; graph/splitting/section data,
native clause-(d)/III/P7, full repair and the original finite B>=A
remain unestablished. No complete flaw candidate is obtained.

### Additional global clause-(d) application — 2026-10-24, step433

**Approved scope and imports.** Use exactly the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-23-selected-prime-global-cover-clause-application.md`.
L053's application and separate audit are method comparisons on other
objects, not inputs to this conclusion. Reuse the inspected general
results, rather than reprove them:

- Mochizuki, *The Etale Theta Function and Its Frobenioid-Theoretic
  Manifestations*, Publ. RIMS 45 (2009), 227–349,
  [journal PDF](https://ems.press/content/serial-article-files/41069?nt=1),
  section 2 opening and Definition 2.1, pp.261–262; Proposition 2.2
  and its complete proof, pp.262–264; Definition 2.3, p.264.
- Mochizuki, *The Absolute Anabelian Geometry of Canonical Curves*,
  [author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Canonical%20Liftings.pdf),
  section 2 opening, Definition 2.1 and Remark 2.1.1, printed pp.8–9,
  for the finite-etale common-cover category and its fixed-field
  convention. Author-PDF/journal byte identity remains unverified.
- The target predicate is Mochizuki, *IUT I*, May 2020,
  [186-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf#page=62),
  Definition 3.1(d), printed p.62. Its identity with author/journal
  bytes remains unverified. This is the qualified statement tested,
  not a new authentication claim.

These same passages were retrieved for applicability, without a new
literature assessment. Retain the saved odd-level correction
qualification concerning IUT I Remark 3.1.6; EtTh's even-level Remark
2.2.1 is unused. The source's additional local Definition 2.5
conditions are outside this global application.

Write F=C_o, K=K_C, X_F=(E_o)_F minus O, C_F=[X_F/{±1}],
Z=C_F times_F K=[X/{±1}], and A=[Y/{±1}]. All objects, maps and
the origin O_B are those already constructed. Fix one algebraic
closure Fbar containing K and compatible geometric basepoints.
Both fields are number fields; K/F is finite separable. Neither a
completion nor G_o replaces F. The main gap remains finite B>=A.
This bounded target can supply one further global prerequisite;
an actual failed quotient, core or diagram condition would stop
or narrow the application.

**The actual arithmetic quotient.** Let Pi=pi_1(X), with geometric
kernel Delta=ker(Pi -> G_K), and let mu:Pi -> V be the actual
continuous monodromy from the original construction. Define N_ell
as the closed subgroup of Delta generated by its commutators and
ell-th powers. It is characteristic in Delta, hence normal in Pi.

To compare with the source's successive quotients, put
C=closure([Delta,Delta]) and T=closure([Delta,C]). EtTh first kills
T, then the closed subgroup of ell-th powers in Delta/T, and finally
the image of C in forming its elliptic quotient. The preimage of
the resulting geometric kernel is N_ell: T is contained in C,
ell-th powers of classes are images of ell-th powers in Delta,
and killing C makes the remaining quotient precisely
Delta^ab/ell Delta^ab. All quotients of profinite groups here use
closed kernels. The arithmetic quotient uses this same geometric
kernel and kills no elements outside Delta. Thus EtTh's arithmetic
elliptic quotient is the actual Pi/N_ell over G_K.

Since V is abelian of exponent ell, mu kills every commutator and
ell-th power in Delta. Its kernel is closed, so it contains N_ell.
It therefore induces Pi/N_ell -> V with exactly the original
covering kernel on pullback to Pi. The geometric image remains all
of V by the original geometric-connectedness argument. The whole
original-cusp decomposition group has trivial image by the original
split-henselian-fiber argument, with residue field K. Its factored
image consequently vanishes as required. V is a free rank-one
F_ell-module, whether or not a generator is chosen. This verifies
the actual quotient in Definition 2.1, beyond an abstract deck-group
order calculation.

The pointed compactifications are (E,{O}) and (B,V), with their
smooth marking log structures. The isogeny psi is etale at every
marked point, and the reduced pullback of O is exactly V. These
log structures therefore pull back without boundary ramification.
The origin O_B belongs to V and is the origin used for inversion.
The resulting smooth log covers and quotient orbicurves are exactly
those of Definition 2.1. Hence Y has type (1,ell-tors), and A has
type (1,ell-tors)±. No full degree-ell^2 multiplication cover has
been substituted. Admission of the base curve to EtTh's core
setting is checked next, without a local Tate-line assumption.

**Core in the fixed-K category.** The original square gives the
surjective representable finite-etale map f:A -> Z of degree ell.
Both objects are smooth, geometrically connected finite-type
K-stacks and generically schemes: their smooth connected curve
atlases are finite-etale, and inversion is free away from its
finite fixed locus. Thus they satisfy CanLift's category hypotheses.

If Q is an object of overline-Loc_K(A), take its finite-etale
quotient presentation W -> Q with W finite-etale over A. The
composite W -> A -> Z is finite-etale, so the same presentation
makes Q an object of overline-Loc_K(Z). This gives a full inclusion
of categories, because in both cases arrows are finite-etale
K-morphisms, without a condition of lying over the starting object.
Conversely, the identity cover of A and the actual finite-etale
equivalence relation A times_Z A present Z as a stack quotient.
Surjectivity of f ensures this quotient is Z. Thus Z belongs to
overline-Loc_K(A); no Galois property of f is needed.

L106 makes Z terminal in overline-Loc_K(Z). Fullness and the just
proved membership therefore make it terminal in overline-Loc_K(A).
In particular the unique arrow from A to this core is the actual f.
The same reasoning with the finite-etale atlas X -> Z shows that
X admits this K-core. This checks the source's starting hypothesis;
it does not assert that either A or X is itself a core. L106's
geometric coricity checks also apply after base change to Fbar,
so the same core setting is available for the geometric theta import.

**The three actual cartesian diagrams.** The original square and
associativity of fiber products give

    A times_(C_F) X_F = A times_Z X = Y.

Thus the scheme/stack square with top row Y -> X_F and bottom
row A -> C_F is 2-cartesian. Its horizontal maps compose the
actual K-covers with the finite separable extension K/F, so are
finite-etale over F. Its vertical maps are the actual degree-two
stack atlases. This uses no descent of U or B to F, and retains
the interior stabilizers of both quotient stacks.

In P=pi_1(C_F), identify J=pi_1(X_F) by its actual degree-two
cover, and H=pi_1(Z) with the preimage of G_K under P -> G_F.
The latter identification follows from Z=C_F times_F K. Let
S=pi_1(A) inside H, using compatible basepoints, and R=pi_1(Y)
inside P. The fiber product above is the connected Y, so the
finite-etale correspondence identifies its subgroup with

    R=S intersect J.

Consequently the arithmetic square with rows R -> J and S -> P
is cartesian in profinite groups. These are actual open subgroups
with their induced profinite topology. Geometric connectedness of
Y and A over K gives image G_K in G_F for both R and S, rather
than an asserted surjection to G_F.

Put D=ker(P -> G_F). The geometric groups of X_F, A and Y are,
respectively, J intersect D, S intersect D and R intersect D.
For S and R this uses their surjections to G_K and the injection
G_K -> G_F. Associativity of intersection now gives

    R intersect D = (S intersect D) intersect (J intersect D)
        inside D.

This is the geometric cartesian square of clause (d). Every arrow
is an open inclusion in its indicated target, being an intersection
of an open inclusion with a closed subgroup. Compatible changes of
basepoints conjugate the entire configuration simultaneously.
The diagrams do not require unrelated subgroup conjugations to
coincide. No assertion that K=F, that A -> C_F is Galois, or that
all initial-data clause-(c) hypotheses have been proved is used.

**Geometric theta subgroups, with inverse images explicit.** Apply
EtTh Proposition 2.2(i)–(iii) to these same basic objects over Fbar.
The characteristic is zero and ell is odd. The base admits the
core just checked. The arithmetic group G_(Fbar) is trivial, so
the cusp extension's splitting has the unique section from the
trivial group. No arithmetic splitting over K is selected.

Write D_Y=pi_1(Y_(Fbar)) and D_A=pi_1(A_(Fbar)). In the source's
finite theta quotients let q_A:D_A -> Q_A be the quotient map,
with its restriction q_Y:D_Y -> Q_Y onto the index-two subgroup.
Here Q_Y is the source's finite basic geometric theta group, not
the full D_Y. Proposition 2.2(i),(ii) gives its cyclic order-ell
eigensubgroup M=Im(s_iota). Part (iii) gives the specified order-two
coset modulo M in Q_A. Let L be the subgroup of Q_A generated
by M and an order-two representative of that coset.
It is independent of that representative. Define the full groups
by the preimages

    D_Y_theta=q_Y^(-1)(M), D_A_theta=q_A^(-1)(L).

The proposition identifies L intersect Q_Y=M and gives the
successive indices [D_A_theta:D_Y_theta]=2 and
[D_A:D_A_theta]=ell. In particular these are open subgroups with

    D_Y_theta contained in D_A_theta contained in D_A.

They correspond by Definition 2.3 to the recalled geometric covers
of types (1,ell-torsTheta) and (1,ell-torsTheta)±. Uniqueness has
exactly the source's subgroup and compatible-basepoint conventions.
The finite M and L themselves have not been mistaken for open
subgroups of the full profinite groups. These are the geometric
subgroups recalled at the end of native clause (d), not a
replacement of the original basic cover by a theta cover.

**Verdict and boundary.** All predicates in the approved global
application pass for the same member, ordering, selected prime,
K_C and chosen line U, subject to the stated source qualification.
This is a REPRODUCTION of known methods with same-object
applicability details, not progress beyond the checked sources.
The additional argument and its new direct input L106 await
separate critical audit; the original algebraic audit is unchanged.

An arbitrary K_C-defined U has not been shown compatible with
any selected completion. Local graph/label/splitting/section data,
III/P7, exact generation/full repair, the relative factor-four
excess, actual input/action/factorization/pilot, source
authentication/def= qualifications, essentiality and original
finite B>=A remain open. Ell-integrality is unused. No complete
flaw candidate or sufficient native initial data is asserted.

### Separate critical audit of the global application — 2026-10-24, step435

**Scope and verdict.** The step433 application passes the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-24-selected-prime-global-clause-critical-audit.md`.
The member, ordering, E_o, G_o, C_o, selected ell, full K_C, line U and
actual isogenies are unchanged. This is a REPRODUCTION audit of a
known-method specialization, not a new general theorem or a full
initial-data assertion. L105 and L106 remain the direct inputs.
The pending-audit statements in step433 and the overview are superseded
by this verdict; no mathematical conclusion or assembly is enlarged.

Reinspected EtTh section 2 opening/Definition 2.1, pp.261–262,
Proposition 2.2 and its complete proof, pp.262–264, and Definition 2.3,
p.264, at the journal link above. Reinspected the three diagrams and
final geometric paragraph of the qualified IUT I reproduction,
Definition 3.1(d), p.62. CanLift's defining-category evidence is reused
from the approved assessment, the completed extraction in
`drafts/2026-10-12-native-k-core-source-notes.md`, and L053's method
audit. Its author endpoint returned metadata but the new targeted text
request timed out; no new CanLift extraction or screenshot inspection
is claimed. This does not replace or invalidate the prior inspected
coverage. No authentication retry or new source theorem is needed.
The reproduction/byte-identity and odd-level correction qualifications
of step433 remain. EtTh's even-level remark is not used.

**Closed quotient and actual monodromy.** Keep step433's Pi, Delta,
C and T. In the successive source quotient, the preimage of the
closed subgroup generated by ell-th powers is the closed normal
subgroup generated by T and the ell-th powers of elements of Delta.
Indeed, every element of Delta/T has a lift in Delta and its ell-th
power is the image of that lift's ell-th power. The final elliptic
quotient also kills C. Since T is contained in C, the combined
kernel is exactly N_ell, not merely a subgroup of it. Equivalently,
both resulting quotients have the universal property of the maximal
continuous abelian exponent-ell quotient of Delta. Closedness is
essential here: the finite-target monodromy kills the closed generated
subgroup, rather than just the algebraic subgroup of words.

N_ell is characteristic in the normal geometric subgroup Delta.
It is therefore normal in Pi, and Pi/N_ell still maps onto G_K with
kernel Delta/N_ell. This checks that the source kills no arithmetic
elements. For the induced monodromy bar(mu),

    preimage_Pi(ker(bar(mu))) = ker(mu).

Thus the actual Y, not merely an abstract degree-ell cover, is recovered.
Its geometric monodromy is onto V because the geometric cover is
connected and V acts regularly on its fiber. The henselian calculation
uses residue field K and the entire fiber V of rational points; the
whole cusp decomposition group, not only inertia, acts trivially.
These checks give both extra conditions of the source rank-one quotient.
The pointed origin O_B, inversion, and reduced smooth markings are
the actual ones. Etaleness at every cusp makes the marking logs pull
back. Hence the type assertions concern this same cover and quotient.

**Core-category membership and fullness.** Set A=[Y/{±1}] and
Z=[X/{±1}] as before. The actual f:A -> Z is representable,
surjective and finite-etale. Surjectivity follows on the atlas X,
where its pullback is the surjective isogeny restriction Y -> X.
Inversion has a finite fixed locus, so the connected smooth atlases
also show that A,Z are generically schemes. These are the required
geometrically connected smooth finite-type K-objects.

For an object Q of overline-Loc_K(A), compose its finite-etale cover
presentation with f. This makes Q an object of overline-Loc_K(Z).
All finite-etale K-arrows between any two such objects are allowed
in both categories: the arrows are not required to be over A or Z.
The inclusion is therefore full. In the other direction needed for
terminality, Z itself belongs to overline-Loc_K(A): the identity
cover A and its finite-etale descent relation A times_Z A present Z.
This can equally be checked with the actual geometrically connected
scheme presentation Y. Its V-translations and inversion satisfy
iota t_v iota^(-1)=t_(-v), so define the constant semidirect-product
action V semidirect {±1}. The V-torsor Y -> X identifies [Y/V]=X;
inversion descends to the actual inversion on X. The quotient-torsor
description therefore identifies [Y/(V semidirect {±1})]=[X/{±1}]=Z.
Since Y -> A is already finite-etale, this is a finite-group quotient
of a cover of A as well. It does not assume f is Galois.

L106's terminality in overline-Loc_K(Z) now restricts to the full
subcategory containing Z. Its unique arrow from A is f because f
is already such an arrow. Applying the same membership checks to
X -> Z gives X a K-core as required at the opening of EtTh section 2.
L106's audited reverse transfers also establish coricity after the
chosen algebraic closure. Neither coricity of A nor a coarse-space
replacement is used.

**All three diagrams and their topology.** The atlas square identifies
A times_Z X with the geometrically connected Y. Since
X=X_F times_(C_F) Z, associativity identifies the actual full fiber
product A times_(C_F) X_F with Y. Its connectedness is proved before
using a subgroup intersection. All horizontal arrows are the given
finite-etale K-covers followed by the constant-field K/F cover;
the vertical arrows remain degree-two quotient-stack atlases.

With compatible basepoints in P=pi_1(C_F), take J=pi_1(X_F) and
H=pi_1(Z). The latter is exactly the inverse image of the embedded
G_K under P -> G_F. The actual subgroup S=pi_1(A) lies in H.
For any two finite-etale covers, the stabilizer of a pair in the
product fiber is the intersection of its stabilizers. Applied to
the connected fiber product here this gives R=pi_1(Y)=S intersect J,
not merely the group of one unexamined component. The subspace
topology on this intersection is its profinite topology, since both
subgroups are open in P. This proves the arithmetic cartesian square.

Both A and Y are geometrically connected over K; hence S and R
surject onto G_K. Their maps to G_F are the compositions with the
injective inclusion G_K -> G_F. Writing D=ker(P -> G_F), their
geometric kernels are therefore S intersect D and R intersect D;
the base curve's is J intersect D. Consequently

    R intersect D = (S intersect D) intersect (J intersect D)

inside D, with the same induced profinite topology. Each inclusion
is open in its target by restriction of an open subgroup of P.
The geometric vertical indices are two, since both geometric atlas
covers are connected torsors of degree two. Changes of compatible
basepoints conjugate this entire diagram. No independent conjugacies,
surjection from S onto G_F, or definition of U over F is assumed.

**Finite theta quotients versus full open subgroups.** Over Fbar the
source cusp extension has trivial arithmetic quotient, so its section
from G_(Fbar)=1 is unique. This checks the splitting premise without
selecting a section over K. The same actual basic cover is used.
Proposition 2.2 gives Q_Y of order ell^2 and its order-ell eigensubgroup
M, and an index-two extension Q_Y inside Q_A. Its specified coset has
order-two representatives normalizing M. For any such representative
iota, L=<M,iota> has order 2ell and L intersect Q_Y=M: its elements
are precisely M and M iota, and iota lies outside Q_Y. If iota' is
another representative of this coset modulo M, then iota'=m iota
for m in M, so it generates the identical L together with M. Thus
the representative does not create an extra subgroup choice.

The quotient maps are compatible, with

    D_Y = q_A^(-1)(Q_Y),   q_Y = q_A restricted to D_Y.

Indeed Q_A is obtained by quotienting D_A by the source kernel
contained in D_Y, and the quotient retains D_A/D_Y of order two.
It follows that D_A_theta intersect D_Y=D_Y_theta. Surjectivity of
the finite quotient maps gives, with full inverse images,

    [D_A_theta:D_Y_theta] = [L:M] = 2,
    [D_A:D_A_theta] = [Q_A:L] = ell,
    [D_Y:D_Y_theta] = [Q_Y:M] = ell.

All three are indices of open profinite subgroups. This also checks
the theta cartesian square in the same geometric setting. Uniqueness
means precisely the source's compatible-basepoint subgroup convention;
it asserts neither uniqueness of arbitrary conjugate embedded groups
nor an arithmetic theta splitting. The basic cover is not replaced
by its further theta cover. Characteristic zero and odd ell>=7
meet the theorem's hypotheses; its odd-level proof uses no Tate
parameter or local graph assumption.

**Boundary.** The audit validates this global prerequisite, with no
new mathematical input or change to the DAG or overview assembly.
It leaves local compatibility of the fixed line U, graph labels,
compatible local splittings, place section, III/P7, exact generation
and full repair unresolved. The relative factor-four excess, source
qualifications, actual input/action/factorization/pilot and essentiality
remain. Original finite B>=A is unchanged; no complete flaw candidate
is obtained. Full matching/supporting Mathlib coverage remains unchecked.

## Mathlib

Full matching and supporting Mathlib coverage for this exact-field
application is unchecked; this does not assert absence. No formal
verification is claimed. The quotient/factorization, monodromy,
henselian and stack-descent theorems are imported by the precise
citations above; only their same-member applicability is supplied
here (REPRODUCTION).
The added core-category, native-diagram and geometric-theta
specialization likewise has unchecked matching/supporting Mathlib
coverage; no absence or formal verification is claimed. Its source
theorems are the precise imports in the additional application.
