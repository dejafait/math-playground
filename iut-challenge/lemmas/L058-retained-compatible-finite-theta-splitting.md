# L058 — Compatible finite theta splitting for the retained local cover

## Hypotheses

Retain L052–L057's unchanged curve, fields, embeddings and maps. In
particular, E=E_0 over N, F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]),
H=F_u subset N=(K_glob)_w subset Omega, and M>=max(M_tors,31).
The fixed pointed Tate isomorphism has changed parameter q_0 in Q_3,
with v_3(q_0)=30 and v_3(3)=1. Neither K_glob=N nor q_0=3^30 is
assumed. Full geometric two-torsion is N-rational, as established in
L054's proof; sqrt(q_0) and sqrt(-1) belong to unchanged N.

Let X=E minus {0_E}, with L055's actual native stable formal log
object over O_N. Let A=Y_N=(B_N minus V_N) -> X be L053/L057's
retained degree-seven cover, where psi:B_N -> E is the actual
isogeny, V_N=ker(psi), and 0_B is the selected origin cusp. Inversion
and the arithmetic graph factorization are those proved there. No
identification c(1)=plus-or-minus Q is assumed.

Use Mochizuki, EtTh, PRIMS 45 (2009), 227–349, with the odd level
l=7. The original cusp x is 0_E. Write D_x for its arithmetic
decomposition extension, I_x for its inertia, and bar D_x for its
finite image in the class-two, exponent-seven quotient of section 2.
Here finite means finite geometric kernel; bar D_x itself still
surjects onto the infinite group G_N. These are groups up to the
usual inertia/basepoint conjugacies.
Use the actual degree-two diagram preceding Definition 1.7, not a
guessed coordinate atlas. A standard theta class and a compatible
splitting are conclusions to be constructed.

## Conclusion

For a choice of that degree-two diagram over unchanged N, there is
a splitting class

sigma:G_N -> bar D_x,   1 -> (Z/7Z)(1) -> bar D_x -> G_N -> 1,

compatible with Theorem 1.10(iii)'s theta-defined sign reduction via
the actual cusp maps in the diagram. Its finite class is independent
of choosing either member of this sign reduction. This independence
does not assert independence of every auxiliary diagram or theta choice.

Proposition 2.2(ii) then constructs an additional degree-seven theta
cover T -> A over N. With this choice, the retained A and the new T
meet the graph and compatible-splitting clauses of Definition 2.5(i),
with l=7, residue characteristic 3 and N=double-dot N.

This is a local specialization of cited constructions. The separate
2026-10-14 critical audit below validates it, with arithmetic inertia
equivariance and finite-cover connectedness made explicit.
It does not identify a previously prescribed
theta cover, label Q, construct global selected/theta data, identify an
actual IUT input/action/pilot, establish essentiality, or decide the
original finite B>=A comparison. It is not a candidate IUT flaw.

## Proof

### Approved scope and imported inputs

Reuse the unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-retained-compatible-splitting.md` and
its full source record
`drafts/2026-10-14-retained-compatible-splitting-source-review.md`.
The main gap is the original finite B>=A comparison. This bounded
test supplies only an independent local covering prerequisite. The
continuation threshold is actual cusp-torsor transport, not rational
cusps alone. ATTEMPTS/027,030,031 and the parked marked-coordinate
mechanism are preserved.

[Mochizuki, The Etale Theta Function and Its Frobenioid-Theoretic
Manifestations, version of record](https://ems.press/content/serial-article-files/41069?nt=1),
section 1, pp.237–239, gives the native formal setup and graph cover.
Proposition 1.3, pp.245–247, supplies the O_N^*-orbit of theta classes;
Proposition 1.4, pp.247–248, identifies its Kummer interpretation and
values. The diagram preceding Definition 1.7, pp.253–254, defines
the dotted curves using multiplication by two, translations by
two-torsion and inversion. Definition 1.9, p.255, and Theorem
1.10(iii), pp.255–256, give standard normalization and the sign
reduction at the dotted quotient's cusp. Section 2, pp.261–264,
defines the actual finite cusp quotient; Proposition 2.2(ii) gives
the additional cover from its splitting. Definition 2.5(i), p.265,
imposes the compatibility condition under test. Import these results;
no general theta or anabelian theorem is reproved.

[Mochizuki, Galois Sections in Absolute Anabelian Geometry,
NMJ 179 (2005), 17–45, author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Galois%20Sections.pdf),
section 4 opening and Definition 4.1(i–iii), author printed pp.14–15,
identify splittings of a rational cusp extension, modulo inertia
conjugacy, with a (N^*)-hat torsor. Roots of a local coordinate give
the cotangent-vector description; a structure-group homomorphism
pushes forward this torsor. A sign structure is a reduction to the
closed subgroup {1,-1}, hence includes a nonempty torsor with that
group. The stable cotangent lattice supplies the integral structure.
We use Theorem 1.10's sign reduction itself. We do not substitute
Galois Sections Corollary 4.12's mu_12 structure or omit the latter's
primitive-twelfth-root correction in EtTh Remark 1.10.1(ii).

[Mochizuki, The Absolute Anabelian Geometry of Canonical Curves,
Documenta Mathematica Extra Volume (2003), 609–640, author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Canonical%20Liftings.pdf),
Proposition 2.3(i,ii), author pp.10–11, supplies the separable-closure
and algebraically closed characteristic-zero base-change criteria for
coricity used below. Its respective hypotheses are geometric normality,
geometric connectedness and finite type, and the hyperbolic-orbicurve
condition. L052 verifies these for the retained punctured quotient.

The section-2 odd-level statements and the complete relevant proofs
were inspected in step 207 and their load-bearing passages rechecked
in step 208. The journal's even-level Remark 2.2.1 is not used; retain
the recorded May 2020 IUT I correction. No source byte identity or
independent audit of the imported anabelian theorems is asserted.

### Local setup and the rank-one quotient

L055 checks the native formal setup on precisely the retained cubic:
finite p-adic field N, stable type (1,1) closed-point log object,
singular split special fiber, and smooth algebraized generic log fiber.
L054 gives N=double-dot N and sqrt(-1) in N. The characteristic is
zero and the residue characteristic is 3.

The non-arithmetic/core condition also holds locally. Choose the
algebraic closure of K_glob inside Omega using its retained embedding.
L052 and the cited Canonical Curves Proposition 2.3(i) give coricity
of [(E_0 minus origin)/{±1}] over that algebraic closure. Proposition
2.3(ii) transfers it along this algebraically closed characteristic-zero
extension into Omega. Apply Proposition 2.3(i) over N to descend
coricity to N. The same hyperbolic orbicurve is involved throughout;
geometric normality, connectedness and finite type persist under these
field extensions. EtTh's setup equates its non-arithmetic condition
here with admitting this core. This does not identify K_glob with N.

L053 supplies a geometrically surjective rank-one quotient with trivial
whole original-cusp decomposition image and the inversion square.
It is an elliptic quotient: the cover extends to the unramified
isogeny psi:B_N -> E, so it factors through the elliptic fundamental
group. Its exponent-seven abelian target therefore factors through
the section-2 quotient Pi_X^ell. Taking the target module to be the
actual V_N requires no chosen generator. L057 proves factorization
through the native arithmetic graph quotient. Thus Proposition
2.2's input is precisely A -> X, rather than a different cover with
an abstractly isomorphic deck group.

### Actual dotted/original cusp maps

For clarity, use E^(2) for the copy of E which is the domain of [2],
and X_dd=E^(2) minus E^(2)[2]. All four points of E^(2)[2] are
N-rational by L054. Hence [2]:X_dd -> X is the source's Galois
degree-four cover over N, with deck translations by E^(2)[2].

Let m be its distinguished nonzero two-torsion translation that acts
trivially on the special-fiber components, denoted mu in the source.
Choose another nonzero two-torsion point z, denoted Z there. These
choices are over N: the distinguished point and all alternative
points belong to the rational two-torsion group. Let

E_dot=E^(2)/<z>,   X_dot=X_dd/<z>.

The quotient by a nonzero translation is an isogeny, unramified in
characteristic zero, as in the cited degree-two construction. The
four deleted points have exactly two orbits under <z>, represented
by 0 and m. Consequently X_dot has exactly two rational cusps,
y=[0] and y'=[m], with y != y'. The remaining degree-two map
a:X_dot -> X extends to the isogeny E_dot -> E satisfying
a composed with (E^(2) -> E_dot)=[2]. In particular it is
unramified at y and sends y to x.

Inversion fixes each deleted two-torsion point and thus fixes both
y and y'. Translation by m interchanges them. Their composite
epsilon (the source's ± times mu) therefore interchanges them as
well. Set C_dot=[X_dot/<epsilon>], exactly the dotted quotient
in the source. Its compactified cusp has no epsilon stabilizer:
the two cusp points are exchanged, not fixed. It is a single scheme
cusp c over N. The quotient map b:X_dot -> C_dot is consequently
unramified at y, with residue field N there. Possible stabilizers
away from the cusps are retained in this quotient stack.

It follows that the two actual maps on generic completed cusp germs
are isomorphisms

hat O_(E,x) -> hat O_(E_dot,y),
hat O_(compactification of C_dot,c) -> hat O_(E_dot,y).

Explicitly, these are maps between N[[t]] rings with nonzero linear
term and rational residue-field identity. Their formal inverse exists
by successive determination of its coefficients. They therefore
identify punctured germs, inertia and arithmetic cusp extensions over
G_N. In the cusp decomposition notation, the induced maps are

D_y -> D_x,   D_y -> D_c,

both isomorphisms up to the usual basepoint conjugacies. They identify
the splitting torsors by roots of the pulled-back local coordinates,
as in Galois Sections section 4. These are actual maps from the
source's common dotted cusp, not an identification of abstract copies
of Z-hat(1). No linear coefficient is set equal to 1, and no
seven-gon atlas, graph label or coordinate of Q enters the argument.

In particular, a splitting class in D_c transports first through
(D_y -> D_c)^(-1), then through D_y -> D_x. This is the
dotted-to-original transport in the diagram referenced by Definition
2.5(i). It is defined on the full arithmetic extensions over unchanged
N, before taking a finite quotient. We do not need to infer a chosen
tangential section from the seven rational cusp points of A.

### Standard normalization and the finite compatible class

Propositions 1.3/1.4 provide the theta-class orbit on the native graph
construction of X. In the dotted setting sqrt(-1) in N supplies the
fourth-order point tau of Definition 1.9. The cited values statement
and Definition 1.9 give a unique unit value u in O_N^* in a standard
set of values. Multiplying the theta function by u^(-1), equivalently
acting on its Kummer class by that unit, is allowed by Proposition
1.3 and makes this value 1. Thus the chosen class is of standard type.
No field extension or prescribed representative of the seven-cover
deck group is needed for this normalization.

Apply Theorem 1.10(iii) to the identical dotted quotient objects and
the identity tempered-group isomorphism. It carries the chosen theta
orbit to itself; the standard-type, finite p-adic-field, sqrt(-1) and
odd-residue-characteristic hypotheses have just been verified. The
theorem supplies a nonempty sign reduction R_c in the full
(N^*)-hat torsor of splittings at c, compatible with its canonical
integral structure. Transport R_c by the actual cusp-extension
isomorphisms above to a sign reduction R_x in the full splitting
torsor of D_x -> G_N. This uses the theta-defined reduction itself,
rather than substituting the weaker mu_12 reduction.

The section-2 finite quotient sends I_x=Z-hat(1) to
(Z/7Z)(1) and D_x to bar D_x. Its kernel on D_x is exactly
7 I_x: section 2 identifies full cusp inertia with the central
class-two inertia and its image at level seven with Delta_Theta.
Thus any splitting class in R_x pushes to a splitting of the actual
extension bar D_x -> G_N in Proposition 2.2(ii). Functoriality of
Kummer cohomology identifies the induced action on splitting torsors
with

(N^*)-hat -> H^1(G_N,mu_7)=N^*/(N^*)^7.

The two members of R_x differ by the action of -1. But
-1=(-1)^7 in N^*, so this element has trivial image under that
homomorphism. Their finite images coincide, giving the asserted
sigma class. Its existence is proved by pushing an actual member of
the nonempty reduction; no surjectivity argument for a torsor map or
arbitrary finite splitting is substituted. Compatibility is exactly
its origin in the transported sign reduction. This finite collapse
does not select a generator of V_N or imply c(1)=plus-or-minus Q.

### Additional cover and limitations

Apply Proposition 2.2(ii) with inversion based at the actual origin
0_B of A and with this sigma. Its inversion-eigenspace splitting
s_iota identifies bar D_x with the specified quotient of the finite
image of Pi_A. The inverse image of sigma(G_N) in Pi_A defines
the additional cover T -> A over N. The proposition states that
the geometric subgroup in its finite quotient is Im(s_iota), cyclic
of order seven; the geometric index is seven. In particular this is
the cited geometrically connected additional degree-seven cover,
finite-etale on the punctured curve, with the smooth log covering
interpretation of Definition 2.3. No explicit equation for T or
global descent of it is claimed.

Definition 2.5(i) now applies to this choice: l=7 and p=3 are odd,
N=double-dot N, L057 supplies the actual graph factorization, and
sigma has the stipulated sign compatibility. Corollary 2.8 is not
used to manufacture the initial choice. This establishes the limited
local clauses stated in the conclusion; the separate audit follows.

The independent cusp-label condition, all-place/global selected data,
actual input/action/pilot/essentiality and original finite B>=A gap
remain open. In particular a successful local theta-cover construction
is not evidence of an inherent IUT flaw or a complete solution.

### Separate critical audit — 2026-10-14

Use the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-retained-compatible-splitting-critical-audit.md`.
This is an applicability audit, not a reproof of the imported anabelian
theorems. Reinspection used EtTh pp.245–248,253–256,261–265, with
the relevant proofs; Galois Sections author pp.14–15; and Canonical
Curves author pp.10–11. The odd-level and mu_12 qualifications remain.

**Setup.** Let k be the elements of Omega algebraic over the embedded
K_glob. This is an algebraic closure of K_glob, since roots in Omega
of polynomials over k remain algebraic over K_glob. Omega is also an
algebraic closure of N. L052's exact punctured quotient is smooth,
geometrically connected and of finite type, with scheme-cusp
compactification of positive log-dualizing degree 1/2. Apply Canonical
Curves Proposition 2.3(i) from K_glob to k, 2.3(ii) from k to Omega,
and 2.3(i) backwards to N. This verifies local coricity without
identifying K_glob and N. The punctured elliptic curve admits this
core through its finite-etale quotient-stack map. L054 gives
N=double-dot N and sqrt(-1) in N; L055 gives the actual split singular
stable log object. Thus EtTh p.253 conditions (I),(II) and the
section-1 setup hold. All four points of E[2] are N-rational.

**Arithmetic transport.** The actual diagram agrees with EtTh p.253.
Translations by z,m commute with inversion because they have order
two. The affine involution exchanges y,y', so its quotient has a
scheme cusp, regardless of interior stack stabilizers. The isogeny
a is etale in characteristic zero, and b is etale at that free cusp
pair. Both residue maps at y are the identity on N. The local degree
of each chosen cusp branch is one; its global degree two is not a
cusp ramification index.

For either actual map, choose parameters t at its target and u at y.
The pullback is t=a_1 u(1+h(u)), with a_1 in N^* and h in uN[[u]].
For each positive integer n, 1+h has a unique n-th root in
1+uN[[u]], by successive coefficient comparison and division by n
in N. After adjoining an n-th root of a_1 to the constants, an n-th
root of t is its product with that formal unit root and an n-th
root of u. Inertia fixes the first two factors. Its action on the
third therefore identifies the full Z-hat(1) inertia with exponent
one, at every level, G_N-equivariantly. The actual ring maps fix N,
so their cusp-extension maps are over the same G_N. The punctured
germ description is precisely the one in Galois Sections section 4;
the dotted quotient is scheme-like here and admits it as well.

An extension isomorphism sends a section modified by an inertia
1-cocycle to its image modified by the induced inertia cocycle.
Inertia conjugation changes it by a coboundary. Hence these maps
induce affine isomorphisms of splitting torsors equivariant for the
identity on H^1(G_N,Z-hat(1)). Use compatible geometric basepoints
through the common germ; changing them conjugates the construction
together. The nonzero constant a_1 may translate its torsor origin
by a Kummer class; the actual map retains that translation. It does
not change equivariance, and it is not discarded by identifying
abstract copies of the torsor. This argument concerns N[[u]], not
integral coordinates or a derivative equal to one. Theorem 1.10's
integral compatibility is used at its stated dotted cusp; no extra
claim about preservation of stable cotangent lattices by the generic
germ maps is needed for Definition 2.5(i)'s compatibility clause.

**Normalization.** The action in Proposition 1.3, p.247, is on the
denominator-free dotted theta class; Proposition 1.4(iii) identifies
it with multiplication of the theta function. Its allowed group is
O_N^* because double-dot N=N. Multiplication by the inverse of the
unit value in Definition 1.9 stays in this orbit and makes it
standard. Identical dotted objects and the identity tempered-group
isomorphism satisfy Theorem 1.10's orbit hypothesis. N is finite
over Q_3, contains sqrt(-1), and has odd residue characteristic.
Part (iii) therefore supplies the nonempty sign reduction. Its
transport is equivariant by the preceding calculation; neither
rational cusps nor the corrected mu_12 theorem substitute for it.

**Finite quotient.** Write rho:D_x -> bar D_x for the actual
section-2 restriction. It is the identity on G_N, so its kernel is
contained in I_x. EtTh p.261 identifies I_x with the full central
inertia in the class-two quotient, whose image at odd level seven
is mu_7 by natural reduction. Consequently ker(rho)=7I_x.
The map on splitting torsors comes from Z-hat(1) -> mu_7.
Naturality of Kummer cocycles identifies it with
(N^*)-hat -> N^*/(N^*)^7: a root of any constant gives the same
cocycle before and after reduction. Thus the two sign-related
sections have the same finite class, since (-1)^7=-1. Existence
comes from an actual member of the transported sign reduction,
not from surjectivity of a torsor map. This proves neither that
every finite splitting is compatible nor independence of all choices.

**Retained cover and connectedness.** L053's actual monodromy is
geometrically surjective onto V of order seven, extends through psi
over x, and kills the whole D_x. Its geometric abelian exponent-seven
image factors through the elliptic quotient, and L057 supplies the
arithmetic graph factorization. Choose the lift of x at 0_B, matching
its decomposition group with the retained inversion. In the image
bar Pi_A let W=Im(s_iota). Proposition 2.2 gives W normal of order
seven and bar Pi_A/W=bar D_x; the geometric kernel bar Delta_A
has order 49, with W of index seven in it. The inverse image J of
sigma(G_N) meets bar Delta_A exactly in W and surjects onto G_N.
It is closed (all these groups and section images are compact), of
index seven, hence open in the profinite group bar Pi_A. Moreover
bar Delta_A acts transitively on the seven cosets, since J surjects
onto G_N. Pulling J back to Pi_A therefore defines a degree-seven
finite-etale cover which remains connected over an algebraic closure.
This is Proposition 2.2(ii)'s additional cover, with the smooth log
interpretation of Definition 2.3. The arithmetic group bar Pi_A is
not finite; only its geometric kernel is finite.

The claimed local clauses pass this audit. No new direct mathematical
input or DAG edge is needed. This certifies a known-method local
specialization, not progress beyond the cited theta theorems. Q's
label, global selected/theta data, actual input/action/pilot/essentiality
and original finite B>=A remain open.

## Mathlib

Full matching theta/cusp-torsor coverage was not checked. No presence
or absence is inferred. The load-bearing inputs here are the precisely
cited published theorems; supporting general formal/finite-cover
results in Mathlib, if available, would not constitute a full match.
