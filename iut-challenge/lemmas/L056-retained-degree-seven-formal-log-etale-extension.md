# L056 — Retained degree-seven formal log-etale extension

## Hypotheses

Retain L053's actual E_0/Q, F=Q(zeta_60,E_0[30]),
K_glob=F(E_0[7]), Omega,u,w, H=F_u subset N=(K_glob)_w,
M>=max(M_tors,31), U, alpha:E -> B=E/U and psi:B -> E.
Retain its fixed pointed Tate isomorphism over Q_3 and the changed
q_0 in Q_3 with v_3(q_0)=30, v_3(3)=1. In particular the local
subgroup U is the Tate image of mu_7, and all seven points of
V=ker(psi) are K_glob-rational. Neither K_glob=N nor q_0=3^30
is assumed. Base change those algebraic maps to N when used below.

Let R=O_N, pi a uniformizer, and k its residue field. Use precisely
L055's stable log cubic C_R^log with infinity section S over
Spec R with chart 1 -> pi. Its underlying scheme is L051's
original cubic base changed to R, with geometrically integral
split nodal special fiber. Write hat C_R^log for L055's formal
completion, with its strict pullback-log reductions. No native
tempered identification, graph-generator marking, compatible
splitting, sufficient initial data or numerical comparison is assumed.

## Conclusion

There is a proper flat algebraic R-curve D_R and a finite-etale
degree-seven map f:D_R -> C_R. There is a pointed N-isomorphism
gamma:B_N -> (D_R)_N for which f_N gamma=psi_N. The inverse image
of S is the disjoint union of seven smooth R-sections, whose
generic fibers under gamma are exactly V_N, including 0_B and Q.

The log structure M_D=f^*M_C is fs and f^log is strict log-etale.
Its strict reductions modulo pi^a, a>=1, and their formal
completion give a finite strict log-etale degree-seven extension
to precisely hat C_R^log. The generic trivial-log locus is
L053's cover (B_N minus V_N) -> (E_0,N minus S).

The special fiber of D_R is a split seven-gon with one marking
on each component. Its dual graph maps to the single-loop graph
of C_k as the connected degree-seven cycle cover: seven vertices
and seven edges, each vertex with the two distinct incident
branches mapped bijectively to the two branches at the target
node. Node smoothing thicknesses agree with the target and equal
ord_R(q_0), with units absorbed in branch coordinates.

This is a known-method specialization. The separate 2026-10-14
critical audit validates it after the origin-coordinate and local-completion
justifications below are made explicit. It supplies a model and its ordinary dual-graph
cover, not an identification with a native tempered quotient or
a native cusp label. It establishes no essential IUT flaw and
no original finite B>=A comparison.

## Proof

### Approved scope and imported results

Use the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-13-retained-degree-seven-log-extension.md`
and its full source notes. The intermediate test addresses one
remaining local model obligation; original finite B>=A and actual
input/action/pilot/essentiality remain independent. A pass can
support a later native graph comparison. The discriminating test
requires precisely psi and C_R over unchanged N.

[Conrad, Arithmetic moduli of generalized elliptic curves,
author version July 18, 2006](https://math.stanford.edu/~conrad/papers/kmpaper.pdf),
Corollaries 2.2.3–2.2.4 (pp.8–9), section 2.5 (pp.16–18),
Example 2.5.1, Theorem 2.5.2 and Theorem 3.2.4 (pp.24–25),
are the inspected primary inputs. They supply generalized elliptic
structures/algebraization, formal polygon rotation quotients,
power isogenies, origin-compatible generic Tate identification,
and extension of generic isomorphisms over normal bases with
matching singular polygon sizes. For morphisms use [Stacks, Lemma 76.43.3, tag 0A4Z](https://stacks.math.columbia.edu/tag/0A4Z):
over a noetherian I-adically complete ring A, compatible maps on
all A/I^a reductions from an A-proper scheme to a separated
finite-type A-scheme algebraize uniquely. Schemes are a special
case of its algebraic-space statement. For the local and finiteness
checks use [Lemma 41.11.3, tag 039M](https://stacks.math.columbia.edu/tag/039M)
(etaleness of an essentially finite-type local map of noetherian
local rings is equivalent to etaleness after maximal-ideal completion)
and [Lemma 37.44.1, tag 02LS](https://stacks.math.columbia.edu/tag/02LS)
(proper and locally quasi-finite implies finite). These live statements
were inspected in the 2026-10-14 audit assessment; no revision is pinned.
These general results are imported, not reproved. Numbering is
for the author version; journal byte identity was not checked.

Reuse the Tate uniformization theorem and its explicit coordinate
series from [Kedlaya, Introduction: the Tate curve, fall 2004,
Theorem 1 and equations (4)–(5), pp.2–3](https://kskedlaya.org/18.727/tate-curve.pdf)
(citing Silverman, Advanced Topics, Theorem V.3.1), and L053's
isogeny factorization input, Milne, Elliptic Curves, second edition,
II.1.7. These identify the standard Tate group and exact kernel;
no abstract point-group isomorphism is treated as an algebraic map.

[Olsson, Logarithmic geometry and algebraic stacks, Ann. Sci. ENS
36 (2003), Proposition 3.19, Definition 4.4 and Theorem 4.6(i)–(iii),
pp.764–767](https://www.numdam.org/item/10.1016/j.ansens.2002.11.001.pdf)
give the fine-log strict-locus and infinitesimal criteria used below.
Reuse L055's fs charts and associated-log construction, with its
F. Kato 1994 chart/pullback citations. No new general log theorem,
Tate construction or algebraization theorem is needed.

### The exact one-gon target

Put r=q_0. Since r is nonzero and topologically nilpotent in R,
Conrad's construction applies over R with this variable. Denote
its algebraic one-gon by T_1(r), and its algebraic seven-gon by
T_7(r); their formal completions are the corresponding formal
Tate polygons. The generic fibers are respectively the standard
Tate elliptic curves with parameters r and r^7. This is the
substitution r=q^(1/n), n=7 in Theorem 2.5.2; it requires no
seventh root of the retained r. The normal-base theorem is used
below only for two ONE-gon models, never between a one-gon and
seven-gon.

C_R is a DR semistable genus-one curve: L051 proves properness,
flatness, connected nodal fibers and trivial relative dualizing
sheaf. Its smooth section S is an effective relative Cartier
divisor, and O(S) is relatively ample, since O(3S)=O_C(1).
Give S=Spec R the trivial group scheme and its identity action
on C_R. This extends its group law and acts trivially on Pic^0.
Thus Corollary 2.2.3 makes C_R a generalized elliptic curve with
identity S. On the smooth generic fiber its group structure is
the elliptic structure with this origin. Both C_R and T_1(r)
have one-gon geometric singular fibers. R is a complete DVR,
hence normal, and Spec N is a dense open in Spec R.

The retained pointed Tate isomorphism gives E_0,N -> T_1(r)_N.
Theorem 3.2.4 therefore extends it uniquely to a generalized
elliptic isomorphism h:C_R -> T_1(r), preserving S. No regular
I_n model, blowup, change of curve or field extension is used.
Transporting a log below will always use the fixed M_C, not a
replacement log on an isomorphic Tate equation.

### Rotation map and its algebraization

Conrad's section 2.5 gives the formally free rotation action of
Z/7Z on hat T_7(r) and its quotient

rho_hat:hat T_7(r) -> hat T_1(r).

The one-gon here is the specific quotient construction in that
section. Rotation acts simply transitively on its seven sheets;
the map is finite-etale of rank seven on every strict ordinary
reduction. Each of the seven node annuli has equation X_i Y_i=r.
The annulus identifications in the source construction commute
with rotation. In particular the quotient map near a node is
etale with the same smoothing function, rather than a power map
on its branch parameters. The orbit of the identity gives seven
sections s_i, i in Z/7Z, represented by (1,r) in the respective
annuli; they are smooth, disjoint, and map to the identity of T_1.

Apply Stacks 0A4Z with A=R, I=(pi), X=T_7(r) and Y=T_1(r).
R is noetherian and complete; the source is proper, the target
proper hence separated and finite type. The formal quotient gives
compatible maps on every R/(pi^a) reduction of these already
algebraized models. Thus it gives a unique R-morphism
rho:T_7(r) -> T_1(r), with precisely the prescribed reductions.
This use of 0A4Z is separate from algebraization of the objects
by Conrad Corollary 2.2.4.

Here is the local-completion check. If x is a CLOSED point of the
special fiber of T_7 and y=rho(x), then k(x)=k(y): on the smooth
part of the special fiber the rotation quotient restricts on each
torus component to its identical torus, and each of the seven
split nodes maps to the unique k-rational target node. Put
A=O_(T_1,y), B=O_(T_7,x), with maximal ideals m,n. These are
noetherian local rings and B is essentially of finite type over A.
For each a, the local map A/(pi^a) -> B/(pi^a) is etale, with
unchanged residue field. Its maximal-ideal completions are therefore
isomorphic, by the etale direction of Stacks 039M (the finite free
completion rank is the residue degree, here one).

This supplies an isomorphism A/m^b -> B/n^b for every b: choose
a>=b, use pi^a in m^b and pi^a in n^b, and reduce that completion
isomorphism modulo the b-th maximal-ideal power. These are the maps
induced by A -> B and hence are compatible as b varies. Their
inverse limit is an isomorphism of maximal-ideal completions
A_hat -> B_hat. The converse direction of 039M proves rho etale
at x. This argument passes from pi-adic reductions to maximal-ideal
completions; it does not identify the two topologies or use only
faithful flatness.

The morphism rho is proper, since T_7 is proper over R and T_1
is separated over R. Its non-etale locus is closed: rho is of
finite presentation between these noetherian schemes. If this
locus were nonempty, its proper image in Spec R would contain
the closed point. Its nonempty special fiber, being of finite type
over k, would then have a closed point, contradicting the preceding
local test. Thus rho is etale everywhere, in particular locally
quasi-finite. Stacks 02LS makes it finite. T_1 is connected: an
open-and-closed decomposition into two nonempty proper R-schemes
would, by the same image argument, disconnect its connected special
fiber. The finite-etale rank is locally constant and is seven on
the special fiber, so it is seven everywhere.

On the generic fiber rho_N is pointed and finite of degree seven,
hence is a homomorphism of elliptic curves. The seven compatible formal sections algebraize by 0A4Z with
source Spec R (proper over itself) and target T_7. Uniqueness
in that theorem makes their composites with rho the identity section
of T_1; their completions are the displayed formal sections.
Their disjointness and smoothness hold on the special fiber and
generically, and their inverse-image union is exactly rho^(-1)(0).
Indeed this is true on every formal reduction; for the finite
fiber over the identity, the complete-R finite algebra is already
determined by those reductions. That fiber is R^7.

### The whole generic map is L053's psi

Write D_R=T_7(r). Theorem 2.5.2 identifies D_N with T_1(r^7)_N
by a pointed isomorphism kappa respecting the multiplicative
formal group at the origin. Example 2.5.1 at n=1,m=7 gives the
degree-seven algebraic generic isogeny

a_N:T_1(r)_N -> T_1(r^7)_N.

Define a'=kappa^(-1) a_N h_N:E_0,N -> D_N. Its kernel is exactly
the retained U_N. To check this identification, the cited power
isogeny has kernel the subgroup mu_7 lifting the torus mu_7 on
the standard one-gon. Under the retained Tate uniformization
the points represented by zeta in mu_7 are precisely these lifts.
For zeta!=1, its reduction is not 1, because seven is prime to
three and reduction is injective on prime-to-three roots of unity.
The convergent Tate coordinate series reduce to

x=zeta/(1-zeta)^2, y=zeta^2/(1-zeta)^3

on the standard nodal cubic y^2+xy=x^3; terms involving positive
powers of r vanish on reduction (rewrite negative-index terms
using zeta^(-1) as in the cited series). Thus these points are
smooth and reduce to the torus parameter zeta. The identity
extends to the smooth infinity section. Multiplication by seven
is etale on the smooth group, so the lifts of these simple
torus seven-torsion points over henselian R are unique. The kernel
specified in Example 2.5.1 is therefore exactly this Tate subgroup,
not an arbitrary order-seven subgroup. Composing with the fixed
h_N identifies it with L053's U_N.

It remains to match the complementary factor, not just its degree.
The required coordinate compatibility is stronger than etaleness.
Use Conrad's construction first over Z[[t]], with t the annulus
parameter, and then substitute t=r. In the smooth formal locus
of the seven-gon, let W_i be the open formal torus attached to its
i-th smooth component. These are disjoint as formal opens, cover
that smooth locus, and rotation sends W_i to W_(i+1) by keeping
its multiplicative annulus coordinate unchanged. Hence the quotient
of their disjoint union is W_0 itself, with that SAME coordinate.
This is the smooth formal locus of the one-gon defined as the
rotation quotient in section 2.5; its identity is the image of
(1,t) in W_0. In particular rho restricts there to the identity
coordinate map, not a power map or an unspecified etale parameter
change. This uses the rotation construction, not an unverified
OCR formula for adjacent annulus overlaps.

Completing W_0 along its section X_0=1 gives exactly the
multiplicative formal-group identification (2.5.3), on both source
and quotient. Thus rho induces the identity in those formal-group
coordinates, over Z[[t]] and after base change to R. The same
coordinates enter Theorem 2.5.2's characterization of kappa and
Example 2.5.1's characterization of a_N: kappa is identity on
these formal groups, and a_N is the seventh-power map. Their
differentials are respectively 1 and 7; rho_N has differential 1.
No assertion that etaleness alone fixes a differential is used.
Consequently rho_N kappa^(-1) a_N and [7] on T_1(r)_N are
pointed homomorphisms with equal differential. Their difference
is zero: a nonzero elliptic homomorphism is an isogeny, and in
characteristic zero an isogeny is separable and unramified, so
cannot have zero differential. This gives an equality of
ALGEBRAIC maps, rho_N a'=h_N[7].

Both alpha_N and a' are degree-seven isogenies with kernel U_N.
The cited isogeny-factorization theorem supplies a unique pointed
N-isomorphism gamma:B_N -> D_N satisfying gamma alpha_N=a'.
Its degree is one by multiplicativity of degrees. Set
f=h^(-1) rho:D_R -> C_R. Then

f_N gamma alpha_N=[7]=psi_N alpha_N.

Surjectivity of alpha_N gives f_N gamma=psi_N. Thus the cover is
the retained global factor after completion, not a new cover with
isomorphic abstract point groups. All isomorphisms and maps in
this comparison are over unchanged N. The seven section generics
are ker(f_N), so gamma identifies them with all of V_N. In
particular 0_B and Q extend as two of the specified sections;
no identification of Q with a native graph generator is used.

### Fixed log, smoothing, marking and formal gluing

Define M_D=f^*M_C as the pullback log structure on the actual
algebraic D_R. This definition supplies one global sheaf, including
its units and overlap maps; it makes f strict. Every target fs
chart pulls back to the same fs monoid. Since f is etale, these
charts cover D_R, so M_D is fine and saturated without changing
its underlying scheme. At a node, use L055's chart

P_n=<x,y,c | x+y=n c>, c -> pi, XY=pi^n.

On each of the seven sheets its pullback has exactly the same
relation and base map 1 -> c. The source-annulus equation XY=r
gives n=ord_R(r): write r=u pi^n and absorb u in one branch.
The etale quotient and h identify the completed target node
with the same annulus node. The thickness is therefore the same
on source and target; it is not multiplied by seven. Equivalently,
the smoothing ideals agree under these etale local identifications.
This integer is intrinsic to the node: the relative singular-locus
Fitting ideal of the chart XY=r is (X,Y), and its quotient is R/(r),
of R-length ord_R(r). An etale split-node identification preserves
that smoothing ideal, and unit changes do not change its length.
As in L055, P_n is saturated in its own groupification and the
base groupification cokernel is free. No requirement that n
be prime to three is imposed.

Near S the target chart is N plus N with generators pi and its
relative marking parameter z. Its pullback marks f^(-1)S,
the seven disjoint smooth sections above. The parameter f^*z
is a simple relative parameter on each etale sheet, so each
marking has multiplicity one, not seven. Away from markings and
nodes the chart is the base N. At double overlaps the log maps
are the pullbacks of the actual M_C transition maps; at triple
overlaps their composites agree by functoriality. Branch exchanges
and unit twists are included. Thus node charts and marking charts
belong to a single global pullback log, rather than separately
assigned formal-coordinate logs.

Strict ordinary etaleness implies log etaleness under the cited
Olsson criteria. In detail the unique ordinary etale lift over
a square-zero thickening supplies the unique log lift: a log
map to D_R over C_R with the fixed underlying map is precisely
the induced map to f^*M_C, by the pullback universal property.
Local finite presentation holds for the finite-etale ordinary map
and the finite charts. Proposition 3.19 and Theorem 4.6 identify
this with log etaleness for these fine log schemes. This applies
also after every strict reduction modulo pi^a.

Pullbacks along D_a -> D_R and C_a -> C_R commute with f^*M_C.
Hence the reductions are strict fs and compatible. On completion
use L055's common etale reduction site and its associated-log
construction: the completed source log is f_hat^*M_hat_C, whose
charts are the same pulled-back finite monoids. Its reductions
are exactly the preceding M_(D_a) by the associated-log universal
property. Overlap cocycles remain pullbacks. This proves strictness
and log etaleness on all reductions, giving the claimed formal
log-etale extension; no limit/monoid-pushout interchange is assumed.
The algebraization is the displayed D_R^log -> C_R^log itself.

Generically the base log is trivial, and f is etale. The source
log therefore consists exactly of the seven marking logs, so
its trivial-log locus is D_N minus ker(f_N). Via gamma it is
precisely L053's Y_N -> X_N. The seven-marked source is stable:
each special P^1 has its two nodes and one smooth marking;
the genus-one generic fiber has seven distinct markings.
Properness, flatness and smooth disjoint sections were checked
above; the positive log-dualizing degree on each component gives
the usual relative ampleness criterion for a pointed nodal family.

### Ordinary cycle graph and remaining limits

The construction of T_7(r) has split standard seven-gon reduction
over k: seven P^1 components joined successively, including the
last to the first. Each is defined over k, each node is k-rational,
and the two branches are distinct. Rotation permutes components
and nodes transitively, giving a one-gon quotient. One smooth
section s_i lies on each component. Consequently the map of
dual graphs has seven vertices above the target vertex and seven
edges above its loop. At each vertex the two incident branches
map to the two distinct branches at the target node; this also
follows from the etale node map. Thus it is a connected covering
of graphs of degree seven, the cycle cover of a loop. Marking
legs map one-to-one above the target marking. Transport by h
identifies the target graph with that of the retained C_k.

This ordinary dual-graph assertion neither identifies the graph
with the native tempered quotient nor labels a native generator.
It also supplies no compatible theta splitting or full selected
data. ATTEMPTS/027,030 and the previous native graph-source stop
remain intact. Original finite B>=A and actual input/action/pilot/
essentiality are open. The formal-model test passes by known
methods, without a claim of progress beyond the sources checked.


### Separate critical audit — 2026-10-14

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-retained-degree-seven-extension-critical-audit.md`
authorizes this audit. Its verdict is a pass with two substantive
justification repairs in the proof above: the rotation's canonical
origin coordinate, and the passage from formal reductions to local
completions and algebraic finite etaleness. Neither repair changes
objects or adds a direct lemma input. This is REPRODUCTION, not a
claim of progress beyond the checked literature.

The exact-target comparison applies Corollary 2.2.3 to the actual
smooth Cartier section S: O(3S)=O_C(1) makes S ample, its trivial
group/action satisfies the Pic^0 condition, and L051 supplies the
DR curve hypotheses. Both compared singular fibers are one-gons,
so Theorem 3.2.4 extends the fixed pointed generic isomorphism over
the normal DVR R. It never compares seven-gon and one-gon models.
Conrad's substitutions are t=r for the rotation construction and
q=r^7 for its generic seven-gon identification; neither adjoins a
root of r. All constructions and uniqueness statements are over R
or its fraction field N, with no descent from a changed local field.

For the generic map, the source-approved power isogeny has degree
seven and the unique smooth torus mu_7 kernel. The seven actual
Tate points reduce to all the smooth torus seven-torsion points.
Since 7 is a unit in R, simple torsion lifts in the smooth group
are unique over this henselian DVR. Thus this is the retained U_N
as a subgroup scheme: in characteristic zero both finite kernels
are reduced, so equality of their geometric points suffices. Any
choice of inversion in naming a torus parameter preserves this
whole subgroup. The coordinate check above then gives the exact
algebraic identity rho_N kappa^(-1) a_N=[7]. Zero differential of
a difference of elliptic homomorphisms forces that difference to
vanish in characteristic zero; this is not a claim in characteristic
three. Kernel factorization over N produces gamma and gives
f_N gamma=psi_N by precomposition with the surjective alpha_N.
No mere degree or point-group match is used to identify the map.

The section and rank checks retain every marking. The formal
rotation orbit of the origin contains seven distinct smooth sections,
one on each component. Algebraization retains their maps and their
fiber: the finite R-algebra above the identity has reductions
(R/(pi^a))^7 for all a, and is therefore R^7 by completeness.
Under gamma its generic points are all of V_N, including Q and
0_B. It is unnecessary here to assign Q a component index; this
audit proves neither that index nor a native cusp label.

The local singular-locus algebra R/(r) checks exactly the smoothing
length ord_R(r); an etale sheet preserves it. The target identification
h preserves the same singular-locus ideal. Thus the source and
ACTUAL C_R have equal thickness, not merely equal special-fiber
incidence. Pulling back the fixed algebraic log M_C along f gives
one global fs log with the identical node and marking charts,
including units and branch exchanges. Near each marking its simple
parameter pulls back simply under f. The ordinary etale lifting
property and the pullback-log universal property give the unique
log lift in Olsson's strict square-zero test; finite presentation
is already known. Every strict reduction inherits these properties.

For completeness the formal pullback comparison is sheaf-theoretic.
On the common etale reduction sites from L055, put
T_C=i_C^(-1)M_C and T_D=i_D^(-1)(f^*M_C). Complete the ordinary
structure sheaves and associate the logs to their induced prelog
maps. A map from either the resulting source log or
f_hat^*(T_C -> O_hat_C)^a into a log over O_hat_D is exactly a
compatible prelog map from the inverse image of T_C and the map
of unit sheaves. The two universal properties therefore identify
these source logs. Applying the same argument to O_(D_a) identifies
the strict reductions with f_a^*M_(C_a); all these maps commute
with transition maps. This checks the claimed completed global log,
not an exchange of association with an inverse limit. Overlap
cocycles are the pullbacks of M_C's actual cocycles.

Finally the seven split components and nodes are the standard cycle,
and rotation preserves the two branch types while identifying their
indices. Each source vertex consequently has one incident branch
of each target type; no folding of the loop occurs. The seven smooth
marking legs and connected degree-seven cycle assertion follow on
the same model. These checks supply only an ordinary graph cover.
The native tempered comparison, label/splitting and full selected/theta
data remain unproved; original finite B>=A and essentiality are still
open. ATTEMPTS/027,030 and the historical native-source stop are
preserved. No new general theorem is reproved in this audit.

## Mathlib

Full matching Mathlib coverage of this formal Tate rotation,
retained isogeny extension and fs log-etale statement has not been
checked; no absence claim is made. The general algebraization,
polygon, isogeny and log inputs are imported by the precise
citations above. No mathematical script or numerical certificate
is used. The separate audit validates only this retained specialization.
