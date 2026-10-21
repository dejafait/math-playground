# L059 — The retained cusp is on an adjacent component

## Hypotheses

Retain L053,L056,L057 and all their hypotheses: the same E_0/Q,
F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), Omega,u,w,
H=F_u subset N=(K_glob)_w, M>=max(M_tors,31), full 30-torsion,
fixed pointed Tate isomorphism, and changed r=q_0 in Q_3 with
v_3(r)=30 and v_3(3)=1. Use the actual U, alpha:E -> B=E/U,
psi:B -> E, V=ker(psi), P represented by beta with beta^7=r,
and Q=alpha(P). Neither K_glob=N nor r=3^30 is assumed.

Let R=O_N, pi a uniformizer, k its residue field, v=ord_R, and
n=v(r)=30v(3). Thus n>=30. Retain precisely L056's
f:D -> C, gamma:B_N -> D_N, origin and seven marking sections,
with f_N gamma=psi_N and source log f^*M_C. Retain L057's actual
native comparison c:Z/7Z -> V; its sign is unspecified. No
component label for Q or compatibility with an unverified atlas
is assumed. Put m=7n and t=r^7.

## Conclusion

The section of D corresponding to Q meets one of the two components
adjacent to the origin component in the retained seven-cycle.
Translation by Q extends to an automorphism of D over C and rotates
that cycle by one edge, with sign determined by the orientation.
It permutes the seven marking sections, preserves the pullback log,
and agrees with the corresponding native deck map. In particular,

    c(1)=Q or c(1)=-Q.

This is a known-method specialization. The separate 2026-10-14 critical
audit validates it with the minimal-Weierstrass/Neron identity bridge
and component-count justification made explicit below. It supplies the
local cusp label only. Global selected/theta
compatibility, actual input/action/pilot/essentiality and original
finite B>=A remain unresolved. No essential IUT flaw is claimed.

## Proof

### Approved scope and imported inputs

Use the unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-retained-component-specialization-label.md`
and its detailed step-211 source record. This proof tests actual
adjacency, not merely whether a component class generates a cyclic
group. It replaces neither the field nor the curve.

The following general inputs are imported, not reproved:

- [Tate, A review of non-Archimedean elliptic functions](https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf),
  “Isogenies,” unnumbered theorem and proof, printed pp.16–17:
  if t_2^a=t_1^b, the representative map z -> z^b gives an algebraic
  isogeny E_(t_1) -> E_(t_2) of degree ab for positive a,b.
  Use the characteristic-zero case over the complete field N.
- [Cremona, Computing in component groups of elliptic curves](https://johncremona.github.io/papers/component.pdf),
  section 2.1, theorem and proof, pp.2–3: the split Tate component
  homomorphism is [z] -> v(z) modulo v(t), with unit classes in
  the identity component. For the standard equation
  y^2+xy=x^3+a_4x+a_6, v(a_4)>=v(t), v(a_6)=v(t).
  Its positive-valuation proof gives v(x)=e, v(y)=2e when
  0<e=v(z)<v(t)/3. The complete series, including its negative
  indices, is used there; no finite approximation is substituted.
- [Liu, Algebraic Geometry and Arithmetic Curves, 2006 paperback](https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf),
  Example 8.3.53, pp.365–367, Lemma 10.3.21, pp.513–514, and
  Corollary 10.3.25, p.515: resolving a split node of thickness d
  inserts d-1 multiplicity-one rational components in a transverse
  chain. The two outer components attach to the original branches.
  The completed calculation describes the actual blowups. This
  applies in residue characteristic three, also when 3 divides d.
- [Conrad, Minimal models for elliptic curves, November 21, 2015](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
  Definition 3.6, Proposition 3.7 and its factorization discussion,
  pp.7–8; Theorem 3.10 and Remark 3.11, p.8; Corollary 4.7, p.12;
  Theorems 5.4 and 5.5, pp.14–15:
  normal proper contractions are determined by their contracted
  components; the positive-genus minimal regular proper model is
  dominated uniquely by every regular proper model; its smooth
  locus is the Neron model. The smooth locus of a minimal Weierstrass
  model is the Neron identity open subgroup (5.5); its minimal regular
  resolution is the minimal regular proper model (4.7). We use this for isomorphisms and
  translations, never to extend an arbitrary finite map.

Keep the recorded source qualifications: Tate's manuscript revision
and publication byte identity are unpinned; Cremona's author preprint
corresponds to ANTS VIII, LNCS 5011 (2008), pp.118–124, without a
byte-identity claim; Liu's primary book is on a third-party mirror;
Conrad Theorem 5.4 cites BLR 1.5/1 for its general proof. Reuse
L053's precise Milne II.1.7 quotient-factorization citation and
L056's Conrad 2006 section 2.5 model/thickness construction. All
are within the prior assessment. The specializations below are
needed because none of these general inputs labels the actual Q.

### Algebraic normalization through the actual quotient

Write tau_s for the standard Tate parametrization at s and
eta:E_0,N -> E_r for the fixed pointed Tate isomorphism. Tate's
theorem gives algebraic N-isogenies

    A:E_r -> E_t,       A(tau_r(z))=tau_t(z^7),
    b:E_t -> E_r,       b(tau_t(z))=tau_r(z).

The parameter equalities are t=r^7 in both cases; their degrees
are seven and bA=[7]. The kernel of A is exactly the image of
mu_7: z^7 in r^(7Z) is equivalent to z in mu_7 r^Z. These are
equal finite subgroup schemes because characteristic zero makes
both reduced. Thus ker(A eta)=U_N, the actual kernel of alpha_N.
Quotient factorization gives the unique pointed N-isomorphism

    lambda:B_N -> E_t,       lambda alpha_N=A eta.

The degree is one because both quotient maps have degree seven.
Precomposing with the surjective alpha_N gives the exact equality
b lambda=eta psi_N. Also, on geometric points,

    lambda(Q)=A eta(P)=tau_t(beta^7)=tau_t(r).

This uses an algebraic theorem and the actual alpha, not promotion
of L053's abstract Phi. Define the generic identification
i=lambda gamma^(-1):D_N -> E_t. Then

    b i=eta f_N,        i(gamma(Q))=tau_t(r),

and i preserves the origin. We compare models using precisely i.
No equality between a guessed annular coordinate and a Weierstrass
coordinate is required; nor is an extra normalization assertion
about L056's kappa. The fixed generic map and marked point have
already been matched by algebraic factorization.

### The actual common regular model and its contraction

D is projective: it is finite over the projective cubic C. It is
flat and semistable with smooth generic fiber, seven split components
and seven split nodes of thickness n, by L056. Its only surface
singularities are those thick nodes. Their local equations are
XY=u pi^n with u a unit; they are normal, and the smooth locus
is regular. Liu therefore gives a regular proper resolution
p_D:M_D -> D. Its special fiber is a split cycle with

    7 + 7(n-1)=m

components. Every original component has multiplicity one, as do
the inserted components. The seven strict transforms of D_k occur
every n edges in this cycle. The original smooth markings, including
the origin, lift without modification; all lie on those strict
transforms. This counts edges geometrically, not in an abstract group.

Let W be the standard Tate one-gon of parameter t, in its standard
integral Weierstrass equation. It is Weierstrass minimal over R.
Indeed Cremona's section 2.1 gives v(c4(W))=0. In the usual
Weierstrass change x=u^2 x'+a, y=u^3 y'+b x'+d, the invariants
satisfy c4(W')=u^(-4)c4(W) and Delta(W')=u^(-12)Delta(W).
An integral equation with strictly smaller discriminant valuation
would require v(u)>0 and hence v(c4(W'))<0, impossible for an
integral equation. This checks the hypothesis of Conrad 5.5 over
this R, rather than assuming minimality survives an arbitrary base
change. Its node is split and has thickness v(t)=m:
this is the same one-gon construction and smoothing-ideal calculation
as in L056, now with parameter t. The model is projective semistable,
and Liu gives p_W:M_W -> W with a split m-cycle. Its original
component's strict transform contains the origin. Both M_D and M_W
are regular proper models of the SAME E_t, the former using i.

Here is a component-count check of minimality; minimal resolution
and minimal regular model are not assumed synonymous. Let M be
the minimal regular proper model of E_t. Write mathcal E for its
Neron model. Conrad 5.4 identifies M^sm with mathcal E. For the
minimal W just checked, Conrad 5.5 gives W^sm=mathcal E^0 as
models with their fixed generic identification. Properness of W
and the Neron mapping property give

    E_t^0(N)=W^sm(R)=mathcal E^0(R),    E_t(N)=mathcal E(R).

Here the left subgroup is precisely Cremona's nonsingular-reduction
subgroup; a section with smooth closed reduction factors through
W^sm. It is not an unproved identification of two component-group
notations. Cremona's theorem now provides m sections tau_t(pi^j),
0<=j<m, in distinct special-fiber Neron components. If two had
reductions in the same geometric component, their difference would
reduce into mathcal E_k^0, hence lie in mathcal E^0(R), contradicting
their distinct valuation classes. Each of these components has a
k-rational point and is a translate of mathcal E_k^0=W_k^sm, a
geometrically integral split torus. Thus they are distinct k-defined
irreducible open subsets of M_k. Two cannot lie in the same
irreducible vertical component: their nonempty disjoint open subsets
would contradict its irreducibility. Consequently M has at least m
irreducible special-fiber components. This uses injectivity of the
rational quotient into geometric components, not an unstated
surjectivity or a rational/geometric component-count equality.
Conrad 3.10 gives domination maps M_D -> M and M_W -> M.
A proper birational morphism of normal models identifies each
noncontracted vertical component with exactly one target component
at its generic point. Indeed the local ring of a target component
is a DVR, and its birational proper lift is unique by the valuative
criterion. Every target component is dominated, by properness.
Since each source has exactly m components, neither domination can
contract one. Any positive-dimensional fiber would contain a vertical
component (the generic fiber map is an isomorphism). Hence both maps
are quasi-finite, therefore finite; finite birational maps to a normal
scheme are isomorphisms. This proves M_D=M=M_W under their actual
generic identifications, without an unassessed finite-map extension
or a no-(-1)-curve shortcut. Conrad 4.7 independently identifies
M_W with M, since Liu's resolution is the minimal desingularization
and W is minimal; it is not being applied directly to D.

Under this identification p_D is precisely a contraction of the
seven disjoint chains inserted at D's nodes, to those actual nodes.
It is the identity away from their fibers, and D is normal. Hence
it has Conrad's contraction universal property. Its uncontracted
components are the seven strict transforms already specified,
including the origin component. This identifies the retained model,
not merely an abstract seven-gon with the same generic curve.

### Valuation one anchors the geometric cyclic order

Set T=tau_t(pi). Since m>=210, Cremona's inspected e=1<m/3
case gives v(x(T))=1 and v(y(T))=2. Write
a_4=pi^m A_4 and a_6=pi^m A_6, with A_4 in R and A_6 in R^*.
In the first blowup of W at (pi,x,y), the pi-chart has equation

    y_1^2+x_1 y_1=pi x_1^3+pi^(m-1) A_4 x_1+pi^(m-2) A_6,
    x=pi x_1, y=pi y_1.

The section T reduces to x_1!=0, y_1=0. This is a smooth point
on the exceptional line y_1=0: the partial derivative with respect
to y_1 reduces to x_1, a unit there. It is not the intersection
of the two exceptional lines y_1=0 and y_1=-x_1.

To check which end of the chain this is, use the x-chart with
s=pi/x and z=y/x. Its equations are

    xs=pi,
    z^2+z=x+A_4 x^(m-1)s^m+A_6 x^(m-2)s^m.

At x=s=z=0 the derivative in z is 1. Thus locally the two
special-fiber branches have parameters x and s with xs=pi.
The branch x=0,z=0 is the same exceptional line as y_1=0;
the branch s=0 is the strict transform of the original cubic.
They meet transversally in a regular surface at this point.
Liu's resolution proceeds only at the remaining singular points,
so neither this intersection nor the smooth specialization of T
is changed. The component containing T in M_k is consequently
adjacent to the original component containing the origin.
This is an actual first-blowup computation; it uses no formal
overlap formula from ATTEMPTS/031.

Translations of E_t extend to automorphisms of M by uniqueness
of the minimal regular proper model, applied also to the inverse.
On M's smooth locus these are the Neron translations: both maps
extend the same generic translation and the Neron extension is
unique. They therefore add the corresponding class in the component
group. Translation by T acts on the m components with order m,
because its class is 1 modulo m. It is a graph automorphism of
the m-cycle and sends the origin component to the adjacent component
just located. A cycle automorphism of order m>2 cannot be a
reflection. Labeling vertices successively, every cycle automorphism
has form j -> a+j or j -> a-j (images of one vertex and one
neighbor determine it). It follows that T translates the cycle
by one edge, up to its orientation.

Choose the orientation in which this translation is +1. Neron
specialization is a homomorphism, so a point of component class j
acts by the same component permutation as jT. In particular
tau_t(r), whose class is v(r)=n modulo m, rotates M_k by n edges.
Units in r do not affect this conclusion: their Tate classes lie
in the identity component and act trivially on the component set.
This step anchors the valuation labeling to geometric cyclic order;
an arbitrary generator of Z/mZ would not suffice.

### Descent of the translation, markings and native label

In M_k the seven retained components form the subset
{0,n,2n,...,6n} in that oriented indexing. Indeed the origin is
retained and each of D's seven node resolutions inserts exactly
n-1 components between consecutive retained components. The
translation by tau_t(r) thus preserves this subset and rotates
it by one retained edge; it also permutes the seven contracted
chains. The contraction universal property gives an automorphism
g:D -> D satisfying p_D composed with the translation equals
g p_D. Applying the inverse translation proves invertibility.
Its generic fiber is gamma composed with translation by Q composed
with gamma^(-1), by the actual identification i above.

As psi(Q)=0, f_N g_N=f_N. Since D is flat with schematically
dense generic fiber and C is separated, f g=f on the whole model.
Thus g is an automorphism over the actual C. It preserves the
inverse image f^(-1)S and permutes its seven sections. The image
of the origin section is precisely the section of Q, by equality
on the generic fiber and separatedness. Each component of D_k
has exactly one of these marking sections, so Q is on the adjacent
retained component determined above. The source log is f^*M_C;
the automorphism over C induces its pullback-log automorphism,
including all strict reductions and the formal completion.

Finally L057 identifies the one-index native deck map with the
actual deck translation by c(1), moving the origin marking to the
unique marking on the next component in its chosen orientation.
The two orientations of the retained cycle differ by sign. Hence
g moves that marking as does the native map of index +1 or -1.
Their generic deck transformations are translations on B_N, and
a translation is determined by its value at the origin. It follows
that Q=c(1) or Q=c(-1)=-c(1), as asserted. This comparison uses
the actual marking sections and deck maps, not a relabeling by an
arbitrary element of (Z/7Z)^*.

### Limits and checks

Only the two resolutions and generic isomorphisms were compared.
The finite isogeny b was never extended to minimal regular models;
Conrad's warning in Remark 3.14 is respected. The m-cycle, the
seven retained components and the thick seven-gon remain distinct.
All maps, sections and contractions are over unchanged R or N.
No representative beta in N is needed for the calculation at P:
the algebraic map is evaluated geometrically and its result tau_t(r)
is N-rational. Global versus completed fields remain distinct.
ATTEMPTS/027,030,031 are preserved. This proof closes a local
prerequisite by known methods; it does not establish a complete
initial datum or a numerical flaw.

### Separate critical audit — 2026-10-14

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-retained-adjacent-cusp-critical-audit.md`
covers this audit and the necessary applicability repairs. Verdict:
the local label passes after explicitly checking W's minimality,
identifying the nonsingular-reduction subgroup via Conrad 5.5, and
justifying the rational-to-geometric component lower bound above.
No new lemma input, field, curve, subgroup, marking or log is introduced.

Algebraic normalization is through the actual alpha: the kernel of
A eta is U_N and the equality b lambda=eta psi_N is tested after
surjective precomposition. Thus i sends gamma(Q) to tau_t(r) and
0_B to the origin; neither a guessed atlas nor an arbitrary generator
identification enters the model comparison. Both resolutions have
exactly m=7n split multiplicity-one components. The domination count
rules out every exceptional component and hence every positive-
dimensional fiber. Normality then makes the finite birational
comparison an isomorphism with the specified generic map.

The first-blowup equations have been checked by substituting
(x,y)=(pi x_1,pi y_1) and (pi,y)=(xs,xz), dividing the Weierstrass
equation by pi^2 and x^2 respectively. Near x=s=z=0, the derivative
in z is 1, so the completed local surface has equation xs=pi.
The exceptional component x=0,z=0 and the original component s=0
therefore meet transversally. In the pi-chart the valuation-one
section has x_1 a unit and y_1 in pi R, so it is a smooth point of
that same exceptional component. On the overlap s=1/x_1 and
z=y_1/x_1; the endpoint s=0 lies in its closure. Neither this endpoint
nor that section meets a subsequent resolution center. This checks
geometric adjacency, not merely an order-m component class.

Neron translation acts on every component because the m rational
classes account for all m components after comparison. Translation
by T has permutation order m>2 and sends the origin to a neighbor,
so is an oriented one-edge rotation. Translation by tau_t(r) has
class n and moves by exactly n edges; units contribute class zero.
The retained subset is exactly {0,n,...,6n}. Its complement consists
of the seven separate exceptional chains, each sent to another such
chain. Thus p_D composed with the translation is constant on each
connected contracted fiber, and Conrad's contraction property applies
to the actual p_D. The inverse translation gives the inverse descent.
Equality over C is checked on the schematically dense generic fiber.
The resulting automorphism preserves f^*M_C and its strict reductions,
and sends the origin to the actual Q-section. L057's one-index native
map sends the origin to the unique mark on a neighboring retained
component; the two orientations give exactly the two signs. Equality
of marked images fixes the generic translations, proving c(1)=+Q or
-Q without changing c by any other unit modulo seven.

This is validation and repair of a known-method specialization, not
a claim of mathematical novelty or an essential IUT flaw. The
independent global selected/theta, actual input/action/pilot and
numerical B>=A obligations remain open.

## Mathlib

Full matching Mathlib coverage of this retained quotient, regular-model
contraction and native-label specialization has not been checked.
No absence claim is made. Standard algebraic Tate, component, resolution,
Neron and contraction inputs are imported by the precise citations
above. No mathematical script or numerical certificate is used.
