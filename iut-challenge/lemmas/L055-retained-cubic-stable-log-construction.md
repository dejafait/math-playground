# L055 — Stable log structure on the retained pointed cubic

## Hypotheses

Retain L051's original pointed cubic E_0/Q, its integer coefficients
c,d,e, its infinity section S=[0:1:0], and its fixed precision
M>=max(M_tors,31). Retain the fields and embeddings supplied there
by L045 and L048:

F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]),
H=F_u=Q_3(zeta_60) subset N=(K_glob)_w
 =Q_3(zeta_420,3^(1/7)) subset Omega.

Write R_H=O_H and R_N=O_N. Use L051's stable one-pointed
scheme family C_H over R_H, with equation
Y^2 Z-X^3-c X^2 Z-d X Z^2-e Z^3=0, and put
C_N=C_H times_(R_H) R_N, with the same section. Its special
fiber is the geometrically integral split nodal cubic
Y^2 Z=X^3+X^2 Z. Its generic fiber is the same E_0 over N.

Use L054's audited dictionary only to identify EtTh's local K
with N and its punctured generic base curve with E_0 over N minus S.
The pointed Tate parameter is the changed q_0 in Q_3, with
v_3(q_0)=30 and v_3(3)=1. Neither q_0=3^30 nor K_glob=N
is assumed. No graph cover, graph label, compatible splitting,
complete selected-place set or theta datum is assumed.

For a DVR R with fraction field L, let B_R^log be Spec R with
its closed-point divisorial log structure
M_R=O_R intersect j_*O_L^times, where j:Spec L -> Spec R.
This is an etale sheaf; on Spec R it consists of nonzero elements
of R, and it has chart N -> R, 1 -> pi_R.
Interpret stable log curves by the tautological moduli-pullback
convention in the published sources specified below.

## Conclusion

The unchanged C_H and C_N admit fine saturated log structures
making them stable log curves of type (1,1) over B_(R_H)^log
and B_(R_N)^log. The second is canonically the fs log base
change of the first along the actual ramified map of these bases;
this fs product has underlying scheme exactly C_N.

The strict reductions of C_N^log modulo pi_N^r, for all r>=1,
are compatible fs stable log curves. Their formal completion is
a stable log curve over the prescribed closed-point formal log
base Spf R_N, with unchanged underlying formal pointed cubic.
Its special fiber is singular and split in EtTh's convention.
Its exhibited algebraization is C_N^log; its generic log fiber
is the smooth elliptic curve with the single marking log structure,
and removing that marking gives the original once-punctured curve.

This is a reproduction/specialization of known constructions. The separate
2026-10-13 audit below validates it with explicit atlas and formal-sheaf
justifications. It supplies one native object prerequisite,
not an essential IUT flaw or a candidate resolution. No exact node
thickness, graph factorization, label, compatible splitting, complete
initial data or finite B>=A assertion is made.

## Proof

### Imported results and scope

Reuse the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-13-retained-stable-log-object-application.md`
and its complete primary notes. The main unresolved claim is the
original finite B>=A with actual input/action/pilot/essentiality.
This construction could support later native-cover comparisons, but
those and the numerical bridge remain independent obligations.
The test here is an fs object on the unchanged cubic over the
prescribed base, compatible with ramification and completion.

[Mochizuki, Semi-graphs of Anabelioids, PRIMS 42 (2006),
section 0, Curves, pp.230–231](https://ems.press/content/serial-article-files/40941)
defines a stable log curve, for 2g-2+r>0, by pullback of the
universal curve over the boundary-log moduli stack. Its universal
curve log includes the marking divisor and the inverse image of
the moduli boundary. Use the ordinary Knudsen moduli theorem for
stable pointed curves as recalled in [Mochizuki, The Geometry of
the Compactification of the Hurwitz Scheme, PRIMS 31 (1995),
sections 3.2–3.4, pp.373–375](https://content.ems.press/assets/public/full-texts/serials/prims/31/3/3772/online/10.2977-prims-1195164048.pdf):
the stack has the universal pointed curve and boundary log structures.
Section 3.3 distinguishes its naturally pulled-back base log from
other log structures on the same scheme. The node description in
section 3.10, pp.379–380, supplies the canonical smoothing generator
and branch generators with their sole relation x+y=t in additive
log notation. Only these underlying curve charts are used, not an
admissible-cover theorem. The marked-chart description follows from
the displayed universal boundary-and-marking divisor; a smooth marked
section and a smooth boundary coordinate give two independent generators.
L051's audited weight-one stability, rather than older OCR of the
ampleness condition, supplies the ordinary stable-family hypothesis.

[F. Kato, Log Smooth Deformation Theory, alg-geom/9406004v3,
6 September 1994](https://arxiv.org/pdf/alg-geom/9406004v3),
Definition 2.1 supplies associated log structures; Definitions
2.7–2.12, Corollary 2.15 and Lemma 3.4 supply charts and the
fine/fs product qualifications. Theorem 4.1, printed p.8, says
that an existing fine log morphism with integral finitely generated
charts is log smooth when the groupification kernel and torsion
cokernel have invertible finite orders and the ordinary chart
comparison is smooth. Proposition 3.9 preserves log smoothness
under log base change. Import these results, not a new construction
theorem or the inaccessible Kato-2000/Olsson-2003 results.

[Stacks, Lemma 53.20.4, tag 0C58](https://stacks.math.columbia.edu/tag/0C58)
preserves at-worst-nodal relative curves under scheme base change.
[Lemma 55.14.2, tag 0CDD](https://stacks.math.columbia.edu/tag/0CDD)
gives etale node charts over an etale DVR extension of the base,
with equation uv=0 or uv=pi^n. Its proof absorbs a unit in a
branch coordinate. The generic smoothness and actual special
node here exclude uv=0 and n=0, respectively, so n is a finite
positive integer. These localizations are chart checks, not field
enlargements of the constructed object. No value of n is needed.
The live Stacks versions are those inspected on 2026-10-13.

[Mochizuki, The Etale Theta Function, PRIMS 45 (2009),
section 0 Curves p.236 and section 1 opening p.237](https://ems.press/content/serial-article-files/41069?nt=1)
specifies the formal closed-point log base, type (1,1), singular
split special fiber and smooth algebraized generic log fiber.
The published sources are separately identified: no byte identity
with the December 2008/May 2020 author sources is inferred.
Retain the prior author-version and even-level qualifications.

### Global log classifying map over the prescribed DVR log

First work over R=R_H. L051 gives the actual stable pointed
family, hence its classifying map
f:Spec R -> bar M_(1,1), with generic image in M_(1,1) and
closed image in its boundary. Here 2*1-2+1=1>0; one marking
makes the ordered and unordered conventions agree.

Let M_mod be the boundary divisorial log on bar M_(1,1).
Every local section of M_mod is a regular function invertible
on the smooth-curve locus. Its pullback under f is regular and
invertible on Spec H. Therefore it belongs to M_R. This defines
an etale sheaf map f^(-1)M_mod -> M_R respecting structure maps
and units, and hence a log morphism f^log:B_R^log -> bar M_(1,1)^log.
This construction may be checked on a moduli atlas: the sheaf maps
on two atlas pullbacks agree because both map each regular function
to its actual pullback in O_R. Since M_R is a subsheaf of O_R,
there is no further choice in that map. They descend to f^log.
The same statement on etale neighborhoods of Spec R uses their
inverse image of Spec H; it is not only a map on global sections.

More explicitly, choose an etale moduli atlas U and form
V=Spec R times_(bar M_(1,1)) U. This is an etale covering of
Spec R. On V the pullback of M_R is its generic-complement
divisorial log: at every closed geometric point an etale DVR
neighborhood has the same uniformizer, and both logs consist of
units times its nonnegative powers. Thus the function-pullback map
lands in precisely this prescribed log on V. On V times_R V,
the two atlas maps are identified by the descent isomorphism of
the actual pointed family. Pullback of functions respects that
isomorphism; their maps to the divisorial log agree. The same
equality on triple overlaps is the cocycle condition. This gives
descent of the log morphism, including its units, and does not
require a global equation for the moduli boundary.

In a node chart the natural pulled-back moduli log has smoothing
generator t with structure value a. Because the generic curve is
smooth and the closed curve has this node, a is nonzero and is a
nonunit. On an etale DVR chart write a=u*pi^n with n>=1 and
u a unit. The map just constructed sends t to the log element
represented by (n,u) in N plus R^times. Its ghost map is
1 -> n. Thus the natural moduli base log is mapped to the
closed-point log; it is not asserted equal to it or strict.

Pull back the universal pointed log curve along f^log, initially
in the category of unrestricted log schemes. The underlying
scheme pullback is C_H, since f classifies this very pointed
family. The universal log sheaf and its sheaf pushout already
give global gluing on that scheme. We now check that these local
pushouts are integral and saturated, so passing to fine or fs
products introduces no change of scheme or of this log structure.
This order avoids using a general fs product to assume the desired
underlying-scheme identification.

### Exact node monoid and unchanged node chart

At the universal node the base chart is Q_0=N with generator t,
the source chart is P_0=N^2 with branch generators x,y, and
Q_0 -> P_0 sends t to x+y. Pulling back along t -> n c (with
its unit u) gives the monoid

P_n=<x,y,c | x+y=n c>.

Absorb u in one branch coordinate, writing the scheme node as
XY=pi^n. The prelog chart is x -> X, y -> Y, c -> pi,
with base Q=N -> P_n, 1 -> c. Absorbing the unit is an
isomorphism of the node model and its associated log structure,
not a modification of C_H.

Here the node log chart is the universal-curve chart, not a new
log structure assigned to an unrelated normal form. On an etale
moduli atlas, the smoothing generator t and its two branch
generators are those of the canonical boundary log on the universal
curve. Pull them back with that curve. The underlying pointed
family is C_H, and Hurwitz section 3.10's canonical-curve description
identifies the branch lifts with the nodal parameters and their
sum with the actual smoothing section. Applying the cited nodal
normal form to this family supplies the ordinary etale comparison;
the canonical lifts give its associated-log chart. Changes of
branch order or multiplication by units are identifications in that
same log sheaf. After a=u*pi^n, replace the second branch lift by
its product with u^(-1), as well as replacing its structure function
Y by Y/u. Its sum with the first lift is now n c, exactly the
displayed chart. The cover exponent, degree and tame-cover assertions
in the surrounding Hurwitz discussion are not used. The required
input is its description of the natural log of each underlying
stable curve; an arbitrary scheme normal form alone would not
identify that log structure.

Here is the full integrality/saturation check for this actual
pushout. Map x,y,c to (n,0),(0,n),(1,1), respectively, in

G_n={(i,j) in Z^2 : i-j belongs to nZ}.

A word x^a y^b c^d, in multiplicative notation for this check,
reduces by xy=c^n to a word with at least one of a,b zero.
Its pair is (na+d,nb+d). For a reduced word, d is the smaller
coordinate, and the difference divided by n determines the only
nonzero branch exponent. Thus reduced words with the same pair
are identical. Conversely every nonnegative pair in G_n is a
unique such reduced word. This proves the presentation injects
into G_n and identifies

P_n=G_n intersect Z_(>=0)^2.

Its groupification is exactly G_n: x and c are a Z-basis,
since (i,j)=((i-j)/n)x+j c. It is finitely generated and integral.
If z in G_n and d z belongs to P_n for an integer d>0, both
coordinates of z are nonnegative, so z itself belongs to P_n.
Hence P_n is saturated in its own groupification. Saturation in
a larger ambient Z^2 is not the relevant test. At the node its
only unit is zero in additive notation, so the chart is sharp.

The same reduced-word argument identifies its monoid algebra as
Z[P_n]=Z[X,Y,T]/(XY-T^n): the monomials in the reduced words
are a Z-basis on both sides. Therefore the ordinary chart
comparison target is

Spec R times_(Spec Z[Q]) Spec Z[P_n]
 =Spec R[X,Y]/(XY-pi^n).

The actual nodal chart maps etale to this target by the cited
normal-form theorem. In groupifications Q^gp -> P_n^gp sends
1 to c, the second member of the basis (x,c), so it is injective
with free rank-one cokernel. In particular no torsion of order
n, and no restriction that n be prime to 3, is required by
Kato's criterion. It proves log smoothness at the node.

### Marking and remaining smooth charts

Near S the family is smooth and S is Cartier, by L051 over
the entire DVR. Choose an etale relative parameter z vanishing
on S; L051's chart Y=1 also provides such a parameter directly.
The source chart is Q plus N=N^2, with (1,0) -> pi and
(0,1) -> z; the base map is 1 -> (1,0). This is the pullback
of the universal base-and-marking chart. Its groupification
kernel is zero and its cokernel is Z. Its ordinary comparison
is the smooth, locally etale, parameter map to A^1_R. It is
fs and log smooth. The marking is disjoint from the node.

At every smooth unmarked point the log is the base log pullback,
with Q -> Q the identity. The ordinary comparison is the original
smooth relative curve morphism, so Kato's criterion applies here
as well. On the generic fiber pi is a unit: the node log becomes
trivial since XY=pi^n makes both X and Y units there; the marking
chart retains just its marking generator. Thus all point types
are covered, including generic points. These charts prove that
the unrestricted pullback already is fs. Its universal property
therefore also makes it the fine and fs pullback on the same C_H.
By construction it satisfies the native tautological definition
of a stable log curve of type (1,1).

### Nonstrict ramified base change and direct construction over N

Let pi_H,pi_N be uniformizers and e_ram=e(N/H). In R_N write
pi_H=v*pi_N^(e_ram) with v a unit. The actual closed-point log
morphism g:B_(R_N)^log -> B_(R_H)^log is pullback of regular
functions; its ghost map is 1 -> e_ram. It need not be strict.

At an H-node of thickness n, the ramified log pushout, disregarding
the unit which is absorbed into one branch, is

P_n plus_(N) N
 =<x,y,c,d | x+y=n c, c=e_ram d>
 =<x,y,d | x+y=n e_ram d>=P_(n e_ram).

Eliminating c proves an isomorphism of the presented monoids,
not just of their groupifications. The preceding complete proof
for every positive integer applies to P_(n e_ram), so this
pushout is already integral and saturated. The ordinary equation
XY=pi_H^n becomes XY=v^n*pi_N^(n e_ram); replacing Y by
Y/v^n yields precisely the chart XY=pi_N^(n e_ram).
No integralization, normalization, blowup or extra component occurs.
The etale chart remains etale under scheme base change.
At the marking the pushout is N plus N again, and at smooth
unmarked points it is the new base N. These are likewise fs.
Consequently the ramified log product has underlying scheme
exactly C_N at all points, not only at the node.

L051's flat proper stable family remains stable after this finite
base extension: the fibers are the same geometric pointed fibers,
and the exhibited relatively ample sheaf pulls back. The cited
nodal base-change result also applies. Therefore it has its ordinary
classifying map f_N=f_H composed with Spec R_N -> Spec R_H.
The direct log classifying map constructed by pullback of moduli
functions equals f_H^log composed with g, because both send each
such function to its same value in M_(R_N) subset O_(R_N).
Associativity of the unrestricted log sheaf pushout and the fs
chart checks identify the direct construction over N with this
ramified pullback. This proves global compatibility, not only
agreement of chosen node-coordinate presentations.

### Strict reductions and formal completion

For r>=1 put R_(N,r)=R_N/(pi_N^r) and endow its spectrum
with the pullback of M_(R_N). Its chart is N -> R_(N,r),
1 -> the residue class of pi_N. This log structure is fs even
when that class is zero or nilpotent; it is not defined by
functions invertible off a closed point of this Artinian scheme.
With this specified log, the closed immersion into B_(R_N)^log
is strict. Give C_(N,r)=C_N times_(R_N) R_(N,r) the inverse
image log structure. Its local charts are exactly P_n, N^2
and N from the N-construction, with their structure functions
reduced modulo pi_N^r. Their associated log structures are fs.
The strict-product result applies, and the underlying scheme is
exactly this ordinary reduction. Kato's base-change proposition,
or the same ordinary chart comparisons after reduction, proves
log smoothness at each r. The moduli-pullback construction also
base changes, so each reduction is stable of type (1,1).

For r'>=r, the maps R_(N,r') -> R_(N,r) give strict transition
maps of these base logs and pointed curve logs. They are compatible
because all structure functions and all gluing maps come from the
single algebraic object C_N^log. The following sheaf construction
makes the completion and all overlaps explicit.

Put C=C_N, C_r=C_(N,r), pi=pi_N and i:C_1 -> C.
Each C_1 -> C_r is a nilpotent closed immersion: its ideal is
generated by pi and has r-th power zero. It is integral,
universally injective and surjective. Hence
[Stacks, Theorem 59.45.2, tag 04DZ (EGA IV, Theorem 18.1.2)](https://stacks.math.columbia.edu/tag/04DZ)
identifies their small etale sites by base change. Transport the
structure sheaves O_(C_r) to this common site and denote them O_r.
Set O_hat=lim_r O_r, a limit of sheaves of rings. On an affine
algebraic etale chart U=Spec A over C, its restriction has sections
lim_r A/pi^r A. On a basic open the sections are instead the
completed localization lim_r (A/pi^r A)_f. This is the structure
sheaf of the formal completion, by
[Stacks, section 87.2, tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY)
and [Definition 87.38.1 and Lemma 87.38.2, tag 0GXT](https://stacks.math.columbia.edu/tag/0GXT).
In the latter lemma the inverse-image closed subspace on U is
precisely U times_C C_1, so its cartesian completion assertion
applies also to overlaps of these charts. All schemes here are
noetherian and the ideal (pi) is principal; their completions
are ordinary adic formal schemes. These are the live source
versions inspected on 2026-10-13.

Let T=i^(-1)M_C on the small etale site of C_1. The compatible
reduction maps give a prelog map T -> O_hat. Define

M_hat=(T -> O_hat)^a,

where superscript a means associated log structure, using Kato
Definition 2.1's sheaf universal property. This is one global
sheaf construction. Locally, a chart P of M_C gives the chart
P -> O_hat, with P=P_n, N^2 or N as appropriate. The chart
isomorphism follows by applying the same universal property to
the original associated-log chart and the ring map to O_hat.
It is not obtained by interchanging a monoid pushout and a limit.

For completeness the units and sheaf overlaps can be tested on
the same site. In any complete chart ring or completed basic
localization, a function is a unit exactly when its reduction
modulo pi is a unit: lift an inverse and invert 1+pi b by its
convergent geometric series. A compatible family of units has
compatible inverses and hence a unit limit. These tests hold
locally on etale charts, so identify the unit sheaves. If an
algebraic chart element becomes a unit on a smaller special-fiber
neighborhood, it is absorbed into O_hat^times by the associated
log construction. Thus the required localizations of charts are
included, not just their global monoid sections. On each double
overlap the algebraic log-chart isomorphism induces an isomorphism
after this sheaf pullback and association. Its inverse is the
pullback of the algebraic inverse. On triple overlaps their
composites are equal because the original composites are equal
and pullback is functorial. Branch exchanges and unit twists are
therefore retained. These algebraic etale charts and their
restrictions cover C_1; equivalence of the reduction sites lets
these sheaf checks be made on the same neighborhoods at every r.

Finally the pullback of M_hat along O_hat -> O_r is canonically
(T -> O_r)^a. Indeed a map from either associated log to any
log over O_r is exactly a structure-compatible prelog map from
T, by the associated-log universal property. Under the site
equivalence, (T -> O_r)^a is precisely i_r^*M_C, where
i_r:C_r -> C. These are the previously constructed M_(C_r).
The identifications commute with every transition r' -> r.
Consequently all reductions from the formal object are strict,
with exactly the asserted fs charts. The same construction on
the base gives its chart 1 -> pi. The formal log morphism is
the completion of the algebraic one; its reductions are the
stable log curves already checked above. This constructs the
formal object and its algebraization without any theorem that
associated log structures commute with inverse limits.

The base is Spf R_N with its chart 1 -> pi_N, exactly the
closed-point formal log base. The 3-adic and pi_N-adic topologies
agree: 3 is a unit times a positive power of pi_N, so their powers
are cofinal. The underlying formal pointed curve is the unchanged
completion of C_N, proper over this base. Its exhibited algebraic
model is C_N^log itself. Its special fiber remains the one integral
nodal cubic with the rational node and smooth infinity marking.
L051's geometric irreducibility and split-node checks survive residue
extension, so it is singular and split in the published EtTh sense.
The algebraic generic base log is trivial. As checked in the charts,
the generic source log is just the single marking log on the smooth
E_0 over N, hence a smooth log curve. Its trivial-log locus is
(E_0 over N) minus S, the original punctured X of L054's dictionary.

### Verdict and limitations

All tests for this bounded construction pass on the unchanged scheme:
the prescribed log base, global gluing, every chart, nonstrict
ramified comparison and compatible formal reductions have been given
and checked by the separate audit below. No independent
initial-data condition is used to conclude it, and none is concluded
from it. L054's field memberships are not needed to force an fs
structure; that result is used only for the native local dictionary.

ATTEMPTS/027 and ATTEMPTS/030 and the prior graph stop remain intact.
The construction neither globalizes the exact rational Tate curve,
retries a graph theorem nor identifies the point-group quotient with
the native graph cover. Graph factorization/label, compatible splitting,
full selected/theta data, actual input/action/pilot/essentiality and
original finite B>=A remain unresolved. This is local progress by
known methods, not a claimed advance beyond the sources checked.

### Separate critical audit — 2026-10-13

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-13-retained-stable-log-critical-audit.md`
authorizes exactly this audit. The statement passes after making
two previously compressed identifications explicit above: atlas/node
compatibility for the actual universal pullback, and the formal
associated-log sheaf with its overlap and reduction maps. These
are justification repairs within the approved construction, not a
new curve, a stronger theorem or a general inverse-limit result.

L051 supplies the flat proper stable pointed family over O_H,
with smooth generic fiber and exactly one split node disjoint
from the section. Its proof checks relative ampleness on the
whole DVR; no regular-total-space assumption is needed here.
The boundary functions pull back to elements invertible generically,
so their descent maps land in the prescribed divisorial base log.
Their smoothing element is nonzero and nonunit; thus n>=1.
The universal branch lifts are retained when choosing an ordinary
nodal comparison, and the unit is absorbed in the log lift and
the function together. This validates the actual P_n pushout,
rather than only an isomorphic underlying node equation.

Independently checking its presentation, reducing a word by
xy=c^n terminates and gives the unique pair with smaller coordinate
equal to the exponent of c. All nonnegative pairs in G_n arise.
The displayed basis x,c generates G_n, and division by a positive
integer preserves nonnegativity. Thus P_n is integral and saturated
in its exact groupification. The base generator c is primitive,
so Kato's groupification kernel and torsion-cokernel orders are
both one, invertible even in residue characteristic 3. Its ordinary
comparison is etale. At the marking the cokernel is again free
and the local parameter map is etale after shrinking; elsewhere
the ordinary smooth morphism suffices. This checks every point type.

For ramification, the relation c=e_ram d eliminates c already
in the presented pushout, giving P_(n e_ram). The very same
integrality and saturation argument applies. The unit v^n is
absorbed by Y/v^n, yielding the actual base-changed equation.
The marking and unmarked pushouts are fs as well. Hence no fs
replacement modifies the underlying scheme. Equality of the two
global constructions follows from functorial pullback of the same
moduli functions and associativity of log pushout, not merely from
agreement of individual coordinates. Properness, stability and
the smooth section survive this base change.

Every finite reduction uses the pullback log, even when its
structure function pi vanishes. Its strictness supplies the
ordinary reduction scheme. The formal proof now works with sheaves
on the common etale site: M_hat is defined by association of a
single prelog sheaf, its local charts are fs, its overlap cocycles
come from the algebraic log, and its strict reductions follow by
the universal property. Nilpotent thickening, ordinary formal
completion and associated-log pullback each have their own checked
role. Neither pointwise units alone nor an unproved limit-pushout
interchange is used to establish gluing.

Finally, the special fiber is still L051's geometrically integral
split nodal cubic and the generic source has precisely the marking
log. The base log is trivial generically, so removing the section
gives L054's original punctured curve over N with the same changed
q_0. This validates only the native object prerequisite under the
retained source-version qualifications. L051 and L054 remain the
direct inputs; L045,L048 are inherited, not new assumptions.
Graph factorization/label, compatible splitting, full selected/theta
data, actual input/action/pilot/essentiality and finite B>=A remain
open. This is local validation by known methods, not a result beyond
the checked sources or an essential IUT flaw.

## Mathlib

Full matching Mathlib coverage of this retained stable-log construction
has not been checked; no absence claim is made. Supporting algebraic,
moduli and log-geometric inputs are imported by the precise citations
above. The explicit monoid and scheme-chart checks specialize them to
this fixed family. No mathematical script or numerical evidence is used.
