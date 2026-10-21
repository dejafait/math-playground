# L053 — Retained rank-one algebraic cover and rational cusps

## Hypotheses

Retain the same E_0/Q, F, K=D=F(E_0[7]), Omega and places u,w
as in L045 and L048. In particular K_w=N, F_u=H, all geometric
7-torsion is K-rational, and the pointed curve E=E_0,K has, at w,
the fixed pointed Tate uniformization with parameter q_0 in Q_3,
v_3(q_0)=30 and v_3(3)=1. Retain M>=max(M_tors,31).
Neither K=N nor q_0=3^30 is assumed. Write X=E minus {0}.

For the additional global clause-(d) application below, also retain
L052's statement that C_base=[X/{±1}] is a K-core. This extra input is
not needed for the original algebraic-cover construction or its audit.

Use this fixed embedding/uniformization to select the seven points
of E[7] represented by mu_7. Let U be that subgroup, viewed globally
in E(K)[7]. Choose beta in Omega with beta^7=q_0, and let P be the
global 7-torsion point whose local Tate class is [beta].

## Conclusion

U is a K-defined constant subgroup of order seven. There are pointed
K-isogenies alpha:E -> B=E/U and psi:B -> E with psi alpha=[7],
degrees seven each. With V=ker(psi), every point of V is K-rational,
V=alpha(E[7]), and Q=alpha(P) is a nonzero generator of V.

Y=B minus V -> X is a geometrically connected finite-etale Galois
cover with constant deck group V isomorphic to Z/7Z. Its monodromy
surjects geometrically, and the original cusp decomposition group
has trivial image in V. Inversion descends and gives a cartesian
square of stacks with top row Y -> X and bottom row
[Y/{±1}] -> [X/{±1}]. The bottom map is representable finite-etale
of degree seven. The seven cusps of Y are K-rational, with origin
0_B and distinguished nonzero cusp Q.

There is a specified isomorphism of geometric POINT GROUPS

Phi:B(Omega) -> Omega^*/q_0^(7Z)

such that Phi alpha sends a Tate representative z to [z^7]. Under
Phi the seven cusps are [q_0^j], j modulo 7, and Q is [q_0].
Replacing beta by another seventh root leaves Q unchanged; replacing
P by -P negates Q.

The separate 2026-10-12 critical audit below validates this limited
algebraic-cover/rational-cusp statement. Phi is not asserted
to identify an algebraic, analytic, tempered or graph cover. In
particular the exponent 1 here is not yet a verified native graph
label ±1 from that calculation alone. The additional 2026-10-15
application below verifies the global clause-(d) predicates, using
L052 as well, and passes the separate critical audit recorded below. The later local
graph, splitting and label results are separate inputs, not consequences
of Phi. Complete initial data and an original numerical comparison
remain unproved.

More precisely, for C_basic=[Y/{±1}], its actual arithmetic monodromy
factors through EtTh's arithmetic elliptic quotient at level seven;
Y and C_basic have types (1,7-tors) and (1,7-tors)±. The K-core of
C_basic is C_base. The arithmetic and geometric diagrams of the
qualified May 2020 IUT I Definition 3.1(d) are cartesian for these
objects. The geometric theta subgroups in its last paragraph are
imported from EtTh Proposition 2.2, without choosing a global arithmetic
theta splitting. This is a known-method specialization, not a complete
initial-data assertion or candidate IUT flaw.

## Proof

### Imported results and scope

Reuse the unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-12-native-rank-one-cover-cusp-application.md`
and its primary-source case record
`drafts/2026-10-12-native-cover-cusp-source-notes.md`.
[Sutherland, MIT 18.783 Lecture 5 (26 September 2023)](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
Theorem 5.11 and its field-of-definition qualification, pp.5–6,
give the subgroup quotient as a separable isogeny, defined over the
subgroup's field of definition and unramified; Theorem 5.25, p.14,
gives deg([7])=49 in characteristic zero.
[Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II.1.7, p.49, gives isogeny factorization from kernel inclusion;
II.6.3, p.70, gives the full rank-two prime-to-field-characteristic
torsion. All maps here are separable; no inseparable set-kernel
argument is used. These theorems need no reproof.

Reuse the named, Galois-equivariant Tate uniformization theorem from
L048's ready sources: [Kedlaya, Introduction: the Tate curve,
fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf), Theorem 1
and its discussion, pp.2–4, together with Milne III.3, pp.102–103.
It identifies the standard split Tate POINT GROUP over Omega with
Omega^*/q_0^Z, by passing through finite extensions. It has no
prime-to-residue-characteristic torsion restriction. Only this
point-group assertion is used below; no algebraization of a new
analytic cover or graph-classification theorem is imported.

[Mochizuki, EtTh, December 2008 author text](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf),
Definition 2.1, pp.32–33, specifies the rank-one quotient, geometric
surjectivity, cusp decomposition condition and inversion square;
Definition 2.5(i), p.36, separately imposes local graph type. The
[IUT I author text, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(d)–(f), pp.62–63, imposes the further local cover and
cusp marking conditions. These source predicates are comparisons,
not premises yielding graph type. Prior inspected wording is reused;
current native retrieval failed and byte identity remains unchecked.

### The actual global subgroup and factor

L045 identifies the full global and local geometric torsion sets
for the same curve under the fixed embedding. By the definition of
K, their coordinates belong to K. In the local Tate group, roots
of unity inject: if zeta=q_0^n, taking valuations gives n=0 and
then zeta=1. Thus mu_7 selects exactly seven distinct points.
Their addition is multiplication of representatives, so they form
a subgroup of E(K)[7]. Characteristic zero makes E[7] finite-etale;
the union of these K-rational points is therefore a K-defined
constant subgroup scheme U. This does not assert definition over F
or preservation by Gal(K/F).

Apply the cited subgroup quotient to U. The resulting alpha:E -> B
has degree seven and kernel U. Since U is contained in ker([7]),
Milne II.1.7 supplies the unique pointed K-isogeny psi with
psi alpha=[7]. Degrees of finite maps of smooth curves multiply
(equivalently, their function-field degrees do), so deg(psi)=49/7=7.
All fields have characteristic zero, hence these isogenies are
separable and unramified. Equivalently, the unramified quotient
description applies to their geometric finite kernels.

For any T in E[7], psi(alpha(T))=0. The kernel of alpha restricted
to E[7] is U, so its image has 49/7=7 points. A separable degree-seven
isogeny has seven geometric kernel points. Consequently
V=alpha(E[7]) exactly. Every such point is K-rational, since alpha
and the entire E[7] are K-defined. The origin of B is alpha(0).

The class [beta] satisfies [beta]^7=[q_0]=1 and belongs to the full
local 7-torsion, hence corresponds to the stated global P in E(K)[7].
If P belonged to U, beta would be zeta q_0^n for some zeta in mu_7
and integer n. Raising to seven would give q_0=q_0^(7n), impossible
since v_3(q_0)>0. Thus Q=alpha(P) is nonzero, and its order in the
seven-element group V is seven. A different beta is zeta beta,
so changes P by an element of U and does not change Q.

### Punctures, monodromy and the original cusp

The preimage of 0 under psi is exactly V, so restriction gives
Y -> X, finite-etale of degree seven. B remains an integral smooth
elliptic curve over the algebraic closure, and deleting finitely many
points leaves it connected; thus this cover is geometrically
connected. Translation by V acts on Y over X, freely and transitively
on every geometric fiber, as follows by subtracting two preimages
under the group homomorphism psi. These translations are K-defined,
since V is constant. Thus the cover is Galois with constant group V.
The standard finite-etale monodromy correspondence gives a quotient
pi_1(X) -> V; geometric connectedness means that its geometric
restriction acts transitively on a fiber. A subgroup of the regular
translation group V is transitive only if it is all of V, proving
the required geometric surjectivity.

The cover extends to the finite-etale map psi:B -> E over the missing
origin. Therefore the cusp inertia acts trivially on its fiber.
Its unramified residue action is the G_K-action on V above 0, which
is trivial because every point of V is K-rational. The whole cusp
decomposition image is consequently trivial, not just its inertia
image. One can equivalently pull back to the henselian neighborhood
of the K-rational origin: its finite-etale cover with split rational
fiber is the disjoint union of seven trivial covers. Changing the
choice of a cusp decomposition subgroup by conjugation does not
change this trivial-image conclusion.

### Inversion and the stack square

Since psi is a group homomorphism, it commutes with inversion;
inversion preserves V and hence Y. For the same group G={±1}, an
equivariant map Y -> X gives the cartesian square stated above.
Here is the explicit quotient-stack check. An S-point of
X times_[X/G] [Y/G] consists of a map x:S -> X, a G-torsor T over S
with equivariant map T -> Y, and an isomorphism of its induced
X-object with the quotient-stack object of x. That isomorphism
trivializes the torsor compatibly with x. In this trivialization,
the equivariant Y-map is precisely a map y:S -> Y with psi(y)=x.
These constructions are inverse, including on arrows and after
base change. Thus the fiber product is Y. No freeness of inversion
on X or Y is required; their 2-torsion stabilizers are retained.

The atlas X -> [X/G] is surjective and etale, since G is finite
etale in characteristic zero. Base change along this atlas makes
the bottom map exactly Y -> X, already finite-etale of degree seven.
Representability, finiteness, etaleness and degree therefore descend
to [Y/G] -> [X/G]. This is a statement about the quotient STACKS,
not a cartesian square of coarse ramified quotients.

The compactification B of Y has exactly V as its puncture set.
Every puncture is K-rational, as proved above; 0_B supplies the
origin cusp and Q the chosen nonzero global cusp.

### Exact point-group calculation and its boundary

The surjective isogeny alpha on geometric points identifies
B(Omega) with E(Omega)/U. Under Tate uniformization this is
Omega^*/(mu_7 q_0^Z). The map z -> z^7 gives an isomorphism

Omega^*/(mu_7 q_0^Z) -> Omega^*/q_0^(7Z).

It is well-defined because replacing z by zeta q_0^n z changes
z^7 by q_0^(7n). If z^7=q_0^(7n), then z/q_0^n belongs to mu_7,
so the kernel is trivial. Every element of Omega^* has a seventh
root in the algebraically closed Omega, proving surjectivity.
This proves the stated Phi as an isomorphism of abstract geometric
point groups, without drawing an algebraic-cover conclusion from it.

The equality psi alpha=[7] shows that psi, in these point-group
coordinates, sends [t] modulo q_0^(7Z) to [t] modulo q_0^Z:
write t=z^7 and apply [7] to [z]. Its kernel is therefore exactly
the seven classes [q_0^j], j modulo 7. Since beta^7=q_0, Phi(Q)
is [q_0], and inversion gives [q_0^(-1)]. This proves the exact
exponent calculation and does not identify that exponent with a
native graph label. Even an abstract Galois-equivariant point-group
description would not supply the required tempered/graph map.

### Original construction's remaining bridge and qualifications — 2026-10-12

The approved rank-one kernel, global factor, inversion square,
rational-cusp and trivial decomposition tests pass. Full graph
factorization and the generator marking remain unverified. The
ready source notes identify a profinite tempered-graph quotient
and additional local base-field predicates; they do not retain the
exact comparison theorem from this algebraic factor to that quotient.
Repeated direct retrieval of the native author text failed this turn.
No unassessed analytic/algebraic or graph bridge is supplied to fill
that gap. This is not a demonstrated mismatch, nonexistence result,
essential IUT flaw, or original finite B>=A failure.

No change has been made to E_0,F,K,N,q_0 or the selected U. A complete
section of selected places, conditions at other bad places, local
square-root/base-field checks, higher theta coverings, compatible
splittings, actual input/action/pilot/essentiality and numerical
comparison remain open. L051's reduction and L052's quotient coricity
are separate previously established prerequisites, not additional
mathematical inputs to this limited construction.

### Separate critical audit — 2026-10-12

**Verdict and imported audit criteria.** The limited statement passes
the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-12-retained-rank-one-algebraic-cover-critical-audit.md`.
This is an independent applicability check of known constructions,
not a native graph-cover theorem. Besides the isogeny and Tate inputs
cited above, use the following inspected primary results:

- Stacks Project [Theorem 58.6.2, tag 0BND](https://stacks.math.columbia.edu/tag/0BND)
  identifies finite-etale covers of a connected scheme with finite
  fundamental-group sets, compatibly with pullback; [Section 58.7,
  tag 03SF](https://stacks.math.columbia.edu/tag/03SF) gives the
  connected Galois-cover criterion.
- [Lemma 10.153.7, tag 04GK](https://stacks.math.columbia.edu/tag/04GK)
  identifies finite-etale algebras over a henselian local ring with
  those over its residue field.
- [Proposition 95.15.3, tag 04UV](https://stacks.math.columbia.edu/tag/04UV)
  describes quotient-stack objects and arrows by equivariant maps
  from fppf torsors. [Lemma 100.3.1, tag 04ZP](https://stacks.math.columbia.edu/tag/04ZP)
  descends representability by algebraic spaces; [Lemma 100.3.3,
  tag 04XD](https://stacks.math.columbia.edu/tag/04XD) and
  [Section 100.3, tag 04XB](https://stacks.math.columbia.edu/tag/04XB)
  descend the finite, etale and finite-locally-free properties.

These are the live tag statements inspected on 2026-10-12 in that
assessment, with no repository byte-identity claim. Their hypotheses
are checked below; their general theorems are imported, not reproved.

**Fields, subgroup and factorization.** Here Omega is L045's algebraic
closure of Q_3. It contains the embedded global algebraic closure, but
K is a number field and K_w=N is its completion. L045's equality of
the full geometric torsion sets applies to the same E_0 retained by
L048. Thus a torsion point obtained from the local Tate map has global
coordinates in K, even though its multiplicative representative need
not be algebraic over Q. L048 supplies a pointed Q_3-isomorphism to
the Tate curve for the changed q_0, with positive valuation 30.
The finite-extension Tate theorem gives the point group over Omega
by taking the union of finite extensions; completeness of Omega
itself is not an added hypothesis.

The intersection mu_7 with q_0^Z is trivial by valuation. The seven
Tate images therefore form a subgroup of the actual E(K)[7]. In
characteristic zero, the corresponding reduced subgroup scheme is
finite-etale and constant over K, so the cited quotient theorem
applies. The kernel inclusion U subset E[7] is a subgroup-scheme
inclusion, since both schemes are finite-etale. It gives psi after
alpha; uniqueness also ensures definition over K if factorization
is first performed geometrically. Multiplicativity of degrees gives
degree seven, and separability in characteristic zero makes the
kernel reduced with seven points. The image of E[7] under alpha
has exactly 49/7 points and is contained in that kernel, proving
equality and rationality of the entire fiber, not just one point.

The chosen [beta] cannot lie in U: such membership would imply
30=7n*30 for an integer n. Consequently Q has exact order seven.
Changing beta multiplies it by an element of mu_7 and hence leaves
Q unchanged. These conclusions use the changed parameter only
through beta^7=q_0 and its positive valuation.

**Geometric monodromy and whole cusp decomposition.** Both E and
B are geometrically integral, and deleting their specified finite
sets leaves connected smooth curves. The restriction Y -> X is
the base change of the finite-etale isogeny psi. Its seven geometric
fiber points are a torsor for the constant group V. Every translation
by V is a deck transformation, and these are all deck transformations:
on a connected finite-etale cover an automorphism is determined by
its value on one fiber point, allowing at most seven. Thus the cited
Galois-cover criterion applies with group V. The geometric cover is
also connected, so its monodromy is transitive on this regular
V-set and must equal V. This supplies geometric surjectivity,
not merely arithmetic connectedness.

For the cusp, set R=O_(E,0)^h, the henselization at the global
K-rational origin. It is a henselian local ring with residue field
K, not the finite residue field at w. The pullback of B is finite
etale over R, and its closed-fiber algebra is K^7: all points of V
are rational and the isogeny is etale, so every fiber length is one.
Lemma 10.153.7 therefore identifies this algebra with R^7. Restricting
to the punctured henselian neighborhood remains the disjoint union
of seven trivial sheets. By pullback compatibility in Theorem 58.6.2,
the entire local fundamental-group action on the fiber is trivial.
Its image is the cusp decomposition action (up to conjugation).
This checks both the inertia and residue-Galois parts and proves
the stated trivial image independently of a choice of splitting.

**Stack objects, arrows and descent.** Inversion commutes with psi
and preserves its kernel, so the same constant group G of order two
acts on the two punctured curves and the map is equivariant. For
any test scheme S, the object associated to x:S -> X in [X/G] is
the trivial torsor G_S with its equivariant X-map. An object of
the asserted fiber product includes an isomorphism from the induced
torsor object of (T,T -> Y) to this particular trivial object.
That isomorphism is part of the data: its inverse at the identity
section selects a section t of T, and the Y-map sends t to a unique
y:S -> Y above x. Conversely y specifies the trivial torsor with
its equivariant Y-map and the required isomorphism.

An arrow in this fiber product is a torsor isomorphism respecting
the prescribed trivializations. It must carry t to t' and therefore
is unique if it exists; compatibility with the Y-maps says exactly
y=y'. In particular no stabilizer automorphism survives the chosen
trivialization. This proves the equivalence on objects and arrows,
functorially in S, and thus the 2-cartesian assertion. It does not
remove the inversion stabilizers in either quotient stack.

By the torsor description, base change of X -> [X/G] to any scheme
object is its G-torsor, so this atlas is surjective finite-etale.
The preceding fiber-product computation identifies the base change
of the bottom map with Y -> X. Lemma 100.3.1 first descends
representability by algebraic spaces; Lemma 100.3.3 then descends
finite etaleness. The finite-locally-free rank is seven on the
surjective atlas and hence everywhere. This proves the stated
degree without asserting a cartesian coarse-quotient square or
assuming inversion acts freely.

**Point-group isomorphism and exact scope.** A nonconstant isogeny
of proper smooth curves is surjective; over algebraically closed
Omega its fibers contain Omega-points. Hence alpha really gives
B(Omega)=E(Omega)/U. In multiplicative representatives its source
quotient is Omega^*/(mu_7 q_0^Z). Raising to the seventh power is
well-defined into Omega^*/q_0^(7Z). Its kernel is exactly
mu_7 q_0^Z: z^7=q_0^(7n) implies z/q_0^n in mu_7.
It is onto because Omega is algebraically closed. Under this
isomorphism psi is reduction modulo q_0^Z, since psi alpha=[7]
and every target representative has a seventh root. Its kernel
consists of the seven distinct classes [q_0^j]; distinctness follows
from positive valuation and j modulo seven. Thus Phi(Q)=[q_0]
and Phi(-Q)=[q_0^(-1)] exactly.

These checks supply no analytic structure on Phi, no tempered graph
factorization and no identification of a graph generator. Exponent
one is only the stated point-group computation. All limited claims
pass without a mathematical correction or new direct lemma input;
the additional citations and full arrow/decomposition checks make
the audit explicit. L045 and L048 remain the direct inputs. The
rank-two substitution stop and native-source blocker remain intact.
Native local base-field predicates, graph/label, full selected/theta
data, actual input/action/pilot/essentiality and original finite B>=A
remain unresolved. This is validation of a partial input by known
methods, not progress beyond the checked source theorems.

### Additional global clause-(d) application — 2026-10-15

**Scope and precise imports.** This application uses the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-15-retained-global-cover-clause-application.md`.
It adds only missing applicability details to the existing cover. Use
[EtTh, PRIMS 45 (2009)](https://ems.press/content/serial-article-files/41069?nt=1),
section 2 opening/Definition 2.1, pp.261–262, Proposition 2.2 with its
proof, pp.263–264, and Definition 2.3, p.264. Use also [CanLift](https://www.kurims.kyoto-u.ac.jp/~motizuki/Canonical%20Liftings.pdf),
section 2 opening, Definition 2.1 and Remark 2.1.1, author-PDF pp.8–9.
The relevant passages were retrieved for application; this reuses the
ready assessment rather than conducting a new literature comparison.
The native clause is [IUT I, May 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf#page=62),
Definition 3.1(d), printed p.62. Author/journal byte identity remains
unverified. No source theorem is reproved here.

Keep K=K_glob=F(E_0[7]), not N. Write X_F=E_0,F minus its origin,
C_F=[X_F/{±1}], X=X_F times_F K, C_base=C_F times_F K,
and C_basic=[Y/{±1}]. These are the existing objects. All geometric
groups below use one algebraic closure of F and compatible basepoints;
the embedded global algebraic closure inside Omega can supply it.
The K-defined origin on B is exactly 0_B, so its inversion is the
one already used in the cartesian square.

**Actual arithmetic elliptic quotient.** Let Pi=pi_1(X),
Delta=ker(Pi -> G_K), and let mu:Pi -> V be this cover's actual
monodromy, with translations as its deck identification. Take the
closed subgroup N_7 of Delta generated by all commutators and seventh
powers. It is characteristic in Delta and hence normal in Pi. The
geometric kernel of EtTh's arithmetic elliptic quotient at level seven
is precisely N_7: its geometric quotient is Delta^ab/7 Delta^ab.

For any a,b in Delta, mu([a,b])=0 because V is abelian, and
mu(a^7)=7mu(a)=0 because V has exponent seven. Continuity kills the
closed subgroup they generate. Thus mu factors through Pi/N_7,
not merely through an abstract cyclic group isomorphic to its deck
group. Its geometric restriction is onto V by the earlier connectedness
proof. Its restriction to the whole original-cusp decomposition group
is trivial by the earlier split-henselian-fiber argument. Both facts
therefore hold for the factored quotient. The actual nonzero cusp Q
identifies V with a free rank-one Z/7Z-module if such an identification
is required; the source's quotient symbol and the point Q are distinct.
No choice changes the monodromy kernel.

The smooth pair (B,V) is the compactification with seven distinct
K-rational markings; (E,{0}) is the base pair. The isogeny is etale
also at these markings. Giving the pairs their marking log structures
therefore gives exactly the smooth log covers used in Definition 2.1.
The quotient just checked and inversion at 0_B show that Y and C_basic
have its stated types. This applies to their associated hyperbolic
orbicurves, as stipulated in that definition. The base (E,{0}) has
type (1,1); its admission to EtTh's core setting follows also from the
core argument next. The full [7] cover of degree 49 is never substituted.

**The specified core, in the actual category.** Put
A=C_basic and Z=C_base for this paragraph. Let f:A -> Z be the actual
representable finite-etale degree-seven map already proved. In CanLift's
notation, objects of overline-Loc_K(A) are finite-etale stack quotients
of objects finite-etale over A; arrows are finite-etale K-morphisms,
without a requirement to lie over A. If T is such an object, choose
its presenting cover W -> A and quotient W -> T. The composite
W -> A -> Z is finite-etale, so T belongs to overline-Loc_K(Z).
This inclusion is full because the rule for arrows is identical.
Moreover Z belongs to overline-Loc_K(A): use the identity cover of A
and its actual finite-etale quotient f. Equivalently its quotient
relation is A times_Z A with the two etale projections; f is surjective.

By L052, Z is terminal in overline-Loc_K(Z). Every object T of the
full subcategory overline-Loc_K(A) consequently has a unique arrow
to Z in that subcategory. Since Z is itself an object there, it is
terminal there, proving that the K-core of C_basic is precisely
C_base with its actual structure map f. The same reasoning for the
finite-etale atlas X -> C_base shows that X admits this K-core, as
required at the start of EtTh section 2. This does not assert that
C_basic or X is itself a core. Smoothness, geometric normality and
connectedness descend from the corresponding curves through their
finite-etale stack atlases; generic stabilizers are trivial. Thus the
defining categories apply. No unproved general cover-invariance theorem
or change to coarse quotients is used.

**All three native diagrams.** The actual stack square over K is
cartesian by the earlier torsor proof. Composing its right side with
base change from F gives

```text
Y  ------> X_F
|           |
v           v
C_basic -> C_F .
```

Indeed its fiber product is
C_basic times_(C_F) X_F = C_basic times_(C_base) X = Y.
The horizontal maps are finite-etale over F: first the degree-seven
cover over K, then the finite separable base change K/F. The vertical
maps are the actual degree-two stack atlases, with stabilizers retained.
The bottom map is not asserted Galois. No descent of the subgroup U
to F is required.

Here is the arithmetic group check, rather than an abstract group
identification. In P=pi_1(C_F), set J=pi_1(X_F) and
H=preimage(G_K) under P -> G_F; H=pi_1(C_base). Let S be the image
of pi_1(C_basic), an open subgroup of H. The actual square identifies
pi_1(Y) with R=S intersect J inside P. Thus the native arithmetic
square has rows R -> J and S -> P, and is cartesian. It uses the
map G_K -> G_F from the retained K/F. Both Y and C_basic are
geometrically connected over K, so their images in G_F are G_K,
not all of G_F unless K=F. The topological inclusions are the ones
from the actual covers.

Let D=ker(P -> G_F)=pi_1(C_F over Fbar). Then
Delta_X_base=J intersect D,
Delta_C_basic=S intersect D, and Delta_Y=R intersect D.
It follows that

Delta_Y = Delta_C_basic intersect Delta_X_base inside D.

These are exactly the geometric kernels in their arithmetic sequences:
the restrictions to S and R have quotient G_K. Hence the square with
rows Delta_Y -> Delta_X_base and Delta_C_basic -> D is cartesian too.
All its arrows are open inclusions, by finite etaleness. Changes of
compatible basepoints conjugate these subgroups simultaneously and
preserve the assertions; incompatible independent conjugations are
not silently identified. These checks establish the diagrams, without
asserting any new F-descent or uniqueness theorem from the explanatory
parenthesis that invokes clause (c).

**Geometric theta recall and limit of the conclusion.** Apply EtTh
Proposition 2.2(i)–(iii), with odd level seven, to this actual basic
cover and inversion. Over Fbar its arithmetic Galois group is trivial,
so the cusp extension has its unique section from the trivial group.
The proposition supplies the prescribed geometric theta subgroups
Delta_X_theta contained in Delta_C_theta contained in Delta_C_basic,
and their finite-etale covers have the types in Definition 2.3.
The uniqueness here is that of the source's geometric subgroups,
with its permitted basepoint conventions. This is the geometric
recall in the last paragraph of Definition 3.1(d). It supplies no
chosen global arithmetic cusp splitting, and imposes no descent of
L058's local splitting. The basic cover remains C_basic; it is not
replaced by this further theta cover.

Thus the bounded global clause-(d) application passes, subject to the
stated source-version qualification. Its separate critical audit is
recorded below. The only added direct lemma input is L052; L045,L048 remain
inputs to the original construction. L057,L060 and L061 are separate
local/selected/q-order results and are not used in this global proof.
Native F_mod and rho, the independent initial-data clauses, actual
input/action/pilot/essentiality and the original finite B>=A comparison
remain unresolved. This application changes none of U,0_B,Q,K,N,q_0.

### Separate critical audit of the global application — 2026-10-15

**Verdict and scope.** The additional application passes the pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-15-retained-global-cover-clause-critical-audit.md`.
This checks applicability of the cited results to the actual retained
objects, not their general proofs or the independent initial-data clauses.
The primary passages reinspected are EtTh, PRIMS 45 (2009), pp.261–264,
section 2 opening through Definition 2.3, including the whole proof of
Proposition 2.2; CanLift, author-PDF pp.8–9, section 2 opening through
Remark 2.1.1; and IUT I, qualified May 2020 reproduction, Definition
3.1(d), p.62, at the links above. The reproduction qualification remains.
No assertion about a new source version or journal byte identity is made.

**Equality of kernels, not an abstract quotient match.** Write
C=closure([Delta,Delta]), and T=closure([Delta,C]). EtTh first takes
Delta/T, then the closed subgroup of seventh powers in that quotient,
and finally kills the image of C when forming its elliptic quotient.
Consequently the kernel of the composite geometric elliptic quotient
is the closed subgroup generated by C and all seventh powers in Delta:
T is already contained in C, and every seventh power in Delta/T is
the image of a seventh power in Delta. This kernel is exactly N_7.
Its arithmetic quotient is formed with this same geometric kernel;
no elements outside Delta are killed. Thus Pi/N_7 is the source's
actual arithmetic elliptic quotient, over G_K, not just an extension
with an isomorphic geometric kernel or quotient.

The original monodromy mu is continuous with finite target V. Its
closed kernel contains the commutators and seventh powers, so contains
N_7. The induced map Pi/N_7 -> V therefore has exactly the same
pulled-back covering kernel in Pi as mu. The source's geometric
surjectivity follows from the actual connected geometric cover; its
cusp condition follows from the whole decomposition action, not only
inertia. In particular the split fiber at the global origin has residue
field K and seven K-rational points, as in the original audit. No
argument replaces that field by the completion N or its residue field.

The chosen origin is 0_B and psi is pointed. Hence the inversion in
EtTh's construction is the retained inversion, and the resulting
cover is Y, with quotient C_basic. The markings are distinct and
psi is unramified at all of them. The log structures of the smooth
marked pairs consequently introduce no extra ramification. This
verifies the exact Definition 2.1 type, not merely its degree.

**Core inheritance.** Both A=C_basic and Z=C_base are smooth,
geometrically connected finite-type K-stacks with trivial generic
stabilizer: away from the finite fixed set the inversion action is
free. Thus CanLift's defining categories apply. A presentation
W -> T of an object T of overline-Loc_K(A), with W finite-etale over A,
also presents it as an object over Z by composition with f:A -> Z.
All arrows in either category are finite-etale K-morphisms, so the
inclusion on these objects is full. No arrow is required to commute
with a separately chosen structure map to A or Z.

For the reverse membership needed for terminality, f is surjective
finite-etale: its base change to X is the surjective degree-seven
cover Y -> X. The identity cover of A lies in Loc_K(A); the two
projections A times_Z A -> A are finite-etale, and their stack quotient
is Z by descent along f. This is an allowed quotient in CanLift's
definition, without asserting a degree-seven group action on A.
In particular Z belongs to overline-Loc_K(A). L052's terminality
therefore restricts to this full subcategory and supplies a unique
arrow from every T to Z; its arrow from A is f itself. Replacing f
by X -> Z gives the same check for X. This verifies the non-arithmetic
base hypothesis at the opening of EtTh section 2. The argument neither
declares A itself a core nor uses the coarse quotient in place of Z.

**The three squares and their geometric kernels.** Use geometric
basepoints related by the actual maps. The torsor calculation gives
Y=C_basic times_(C_base) X; associativity with C_base=C_F times_F K
gives Y=C_basic times_(C_F) X_F. All covers are finite-etale and all
four objects connected. In P=pi_1(C_F), the subgroups J,S,H from the
application are therefore actual open subgroups; H is the inverse
image of G_K, since C_base is the constant-field pullback. The
stabilizer of the selected point in the fiber product is S intersect J.
That fiber product is the connected Y, so its full fundamental group
is R=S intersect J, not just the group of an unverified component.
This proves the arithmetic square in profinite groups, including its
topology, as the intersection of closed open subgroups of P.

Geometric connectedness over K gives the surjections S -> G_K and
R -> G_K. Composing with G_K -> G_F is their actual arithmetic map;
it is not a surjection to G_F in general. With D=ker(P -> G_F), their
geometric kernels are exactly S intersect D and R intersect D. The
base curve has geometric kernel J intersect D. Associativity of
intersection proves

    R intersect D = (S intersect D) intersect (J intersect D).

This is the third, geometric square inside D. Each inclusion is open
in its target, since it is the restriction of an open inclusion in P.
The vertical degree-two covers remain connected after algebraic
closure, so these vertical geometric inclusions also have index two.
Compatible basepoint changes conjugate the entire diagram. None of
this requires U to descend to F, or drops the interior stack inertia.

**Geometric theta import.** Use the same basic cover after base change
to the chosen algebraic closure of F. L052's geometric core argument
retains EtTh's non-arithmetic hypothesis there. The field has
characteristic zero and the level seven is odd; these are the
hypotheses of Proposition 2.2, unlike the additional local hypotheses
of Definition 2.5. Over this algebraically closed field G is trivial,
so the cusp extension's section is the unique map from the trivial
group. The splitting torsor therefore contributes no arithmetic
choice. Proposition 2.2(i),(ii) gives the inversion eigensubgroup
in the finite theta quotient; part (iii) supplies the order-two
coset and the compatible quotient cover. Its proof's odd-level
condition applies at seven; no even-level remark is used.

The finite eigensubgroup is not itself the open subgroup of the full
geometric fundamental group. Take its inverse image under the
source's quotient map to obtain Delta_X_theta; similarly take the
inverse image of the subgroup including the specified order-two
coset to obtain Delta_C_theta. These are open, with
Delta_X_theta contained in Delta_C_theta contained in Delta_C_basic,
and with successive indices two and seven. Definition 2.3 gives the
stated types. The source's uniqueness concerns these subgroups with
its basepoint conventions, not a distinguished arithmetic splitting
or a selected generator. This is precisely the final geometric
recall in Definition 3.1(d), not a replacement of C_basic by a theta
cover. No descent of a prescribed local splitting is asserted.

The audit supplies no new direct lemma input: L045,L048,L052 suffice.
It validates one global initial-data prerequisite by known results.
The native field/rho setup, independent initial-data conditions and
actual input/action/pilot/essentiality and finite B>=A remain outside
this conclusion. No essential IUT flaw or complete candidate results.

## Mathlib

Full matching Mathlib coverage of this selected global factor,
stack square, cusp decomposition and point-group specialization has
not been checked. Unknown availability is not absence. The result
applies cited subgroup quotient, factorization and Tate results;
it claims no progress beyond those known constructions. No numerical
certificate or mathematical script is needed for the exact group,
fiber and stack checks above.
Full matching Mathlib coverage of the additional arithmetic quotient,
core-category specialization, native diagrams and geometric theta
subgroups is likewise unchecked; no absence claim is made.
