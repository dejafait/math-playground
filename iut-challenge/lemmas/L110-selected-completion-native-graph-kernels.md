# L110 — Native graph kernels at the unchanged selected completions

## Hypotheses

Retain L109's hypotheses and fixed objects: L105's one member, ordering,
E_o,G_o,C_o and ell>=7; K=K_C=C_o(E_o[ell]) with full coordinates;
L107's single fixed line U and pointed maps

    alpha:E -> B=E/U, psi:B -> E, psi alpha=[ell],
    V=ker(psi)=alpha(E[ell]), X=E minus O, Y=B minus V;

and L108's audited section s over F_mod=Q, with
Sigma={p:v_p(j(E_o))<0} minus {ell}. Thus p in Sigma is odd and
p!=ell. Use L107's algebraic cover conclusions and L109's separately
audited same-completion pointed split Tate comparisons and exact U equality.
The inherited source authentication and def= qualifications remain.

Neither initial theta-data nor a III situation is assumed. There is no
assumption of splitness over C_o, a C_o-defined U, ell-integrality of j,
normality of K/Q, a chosen global cusp generator, a double-dot field
predicate, or a compatible theta splitting. No new global object is chosen.

## Conclusion

For each p in Sigma, put w=s(p), k=K_w, R=O_k and kappa=R/(pi).
There is a proper stable one-pointed fs log model C^log over the
closed-point log base of R, whose pointed generic fiber is identified
with (E_o)_k. Its special fiber is a split one-gon. There is an ordinary
finite-etale map g:D -> C of degree ell, with source log g^*M_C,
and a pointed k-isomorphism gamma:B_k -> D_k for which

    f g_k gamma=psi_k,                               (1)

where f:C_k -> (E_o)_k is the fixed generic identification. Here and
below a subscript k means the generic fiber; a subscript kappa means
the special fiber. All ell inverse-image marking sections are disjoint
and R-rational and correspond under gamma to the entire V_k.

Complete C^log along its special fiber and transport its generic
punctured curve to X_k by f. Let beta_w:Pi_(X_k)^tp -> Z be EtTh
section 1's arithmetic graph quotient, up to orientation, and let
beta_hat_w:Pi_(X_k) -> Z-hat be its profinite completion. Let
mu_w:Pi_(X_k) -> V_k be the actual arithmetic monodromy of Y_k -> X_k,
with deck maps the translations on B_k. There is a cover-induced
isomorphism c_w:Z/ell Z -> V_k for which

    mu_w = c_w composed with (mod ell) composed with beta_hat_w,
    ker(mu_w) = beta_hat_w^(-1)(ell Z-hat).             (2)

This is equality of actual arithmetic kernels at every already selected
w, not only of geometric kernels or degrees. The source of the native
finite quotient is the completion of D with its pulled-back log.
No common identification c_w(1) with a chosen global cusp up to sign,
compatible theta splitting, double-dot predicate or full native type is
asserted. The separate step447 critical audit below validates this
known-method specialization. It gives no complete candidate or essential IUT flaw and no
original finite B>=A conclusion.

## Proof

### Scope, imports and their use

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-selected-completion-graph-cover-comparison.md`.
Reuse its arbitrary-level model, log, graph and arithmetic-descent
coverage, including its precise source versions and relevant proof cases.
The complete L056–L057 methods and audits, and L055's log construction,
were compared as methods on different objects; none of their conclusions
on the old curve or old field is an input here. L109 supplies the missing
same-field comparison. ATTEMPTS/030's full-multiplication stop and
ATTEMPTS/031's unverified marked-coordinate stop are preserved.

The main gap remains original finite B>=A. The intermediate target is
(2), with possible downstream use in the graph part of native clause (e).
The test requires actual models, maps and residue descent; degree and
geometric point-group agreement are insufficient. The independent sign,
splitting, initial-data, repair and numerical gaps are not premises.

Import the following established results; only applicability and the
present-object comparisons are proved below.

- Conrad, [Arithmetic moduli of generalized elliptic curves, author
  version 18 July 2006](https://math.stanford.edu/~conrad/papers/kmpaper.pdf),
  Corollaries 2.2.3–2.2.4, section 2.5, equations (2.5.1)–(2.5.3),
  Example 2.5.1 and Theorem 2.5.2, pp.8–9,17–18: algebraic/formal
  Tate polygons, free rotation and its one-gon quotient, the power
  isogeny, and the generic Tate identification preserving the formal
  group at the origin. The construction works over an adic noetherian
  ring with a topologically nilpotent parameter. The theorem's formal
  variable q^(1/n) is substituted by our r, without adjoining a root.
  The essential rotation and generic-identification proof cases were
  reinspected on 2026-10-24. We use the established construction, not
  the problematic extracted annulus-overlap formula of ATTEMPTS/031.
- Tate uniformization, [Kedlaya, fall 2004, Theorem 1 and formulas
  (4)–(5), pp.2–4](https://kskedlaya.org/18.727/tate-curve.pdf), citing
  Silverman, Advanced Topics, V.3.1; and Milne, [Elliptic Curves,
  second edition (2021), II.1.7](https://www.jmilne.org/math/Books/EC2.pdf),
  for isogeny factorization. These give the standard Tate parametrization
  and the factorization of maps killing a specified finite kernel.
- [Stacks 76.43.3, 0A4Z](https://stacks.math.columbia.edu/tag/0A4Z),
  compatible-map algebraization from a proper scheme over a complete
  noetherian base to a separated finite-type scheme;
  [41.11.3, 039M](https://stacks.math.columbia.edu/tag/039M), the
  maximal-ideal completion criterion for an essentially finite-type
  local map to be etale; and [37.44.1, 02LS](https://stacks.math.columbia.edu/tag/02LS),
  proper plus locally quasi-finite implies finite.
- Mochizuki, [Semi-graphs of Anabelioids, PRIMS 42 (2006), section 0,
  Curves, pp.230–231](https://ems.press/content/serial-article-files/40941?nt=1),
  and [Geometry of the Compactification of the Hurwitz Scheme,
  PRIMS 31 (1995), sections 3.2–3.4 and 3.10, pp.373–375,379–380](https://content.ems.press/assets/public/full-texts/serials/prims/31/3/3772/online/10.2977-prims-1195164048.pdf):
  the stable pointed-curve moduli and tautological boundary/marking log
  convention, with node relation x+y=t for the smoothing generator.
  [F. Kato, alg-geom/9406004v3, 6 September 1994](https://arxiv.org/pdf/alg-geom/9406004v3),
  Definitions 2.1,2.7–2.12, Corollary 2.15, Lemma 3.4, Proposition 3.9
  and Theorem 4.1, supplies associated logs, fs chart/product tests and
  the log-smooth chart criterion. No log existence theorem on an
  unspecified model is assumed.
- Mochizuki, [The Etale Theta Function, PRIMS 45 (2009), section 1,
  pp.237–239 and Definition 2.5(i), p.265](https://ems.press/content/serial-article-files/41069?nt=1):
  the arithmetic graph quotient and its infinite formal etale chain
  cover for a split singular stable type-(1,1) log curve over the
  closed-point formal base of a finite p-adic field. The profinite
  convention and the independent splitting/field predicates were
  reinspected. Semi-graphs, Definition 2.2(ii), Remark 3.5.1 and
  Examples 3.10/5.6, pp.246,261–262,268–270,295–296, supply the
  locally trivial constituent-map comparison, with arithmetic actions.
- [Stacks 58.9.1, 0A48](https://stacks.math.columbia.edu/tag/0A48),
  equivalence on finite-etale covers between a proper scheme over a
  henselian local ring and its closed fiber; and [59.45.2, 04DZ](https://stacks.math.columbia.edu/tag/04DZ),
  etale-site equivalence for a universal homeomorphism, applied to
  nilpotent reductions. Use their complete-noetherian and finite-etale
  cases with actual maps, before puncturing. The split-node and
  finite-module completion inputs are cited at their use below.

The above general theorems are not reproved. The comparisons below
are necessary because no source theorem names this same global cover
at these selected completions. This is REPRODUCTION by known methods;
no claim beyond the inspected sources' methods or of novelty is made.
Published source locators do not remove the inherited authentication,
author/journal or def= qualifications. Mathlib is addressed separately.

### Actual pointed models over one arbitrary selected completion

Fix p in Sigma, w=s(p), k,R,kappa as above. L109 gives r=q_w in k,
0<|r|<1 and a pointed k-comparison E_r -> (E_o)_k. Thus r belongs
to R and is topologically nilpotent; R is a complete noetherian DVR.
Let

    C=T_1(r), D=T_ell(r).

These are Conrad's algebraic models over R. The generic fibers are
E_r and E_(r^ell), respectively; denote the canonical formal-group-
compatible pointed isomorphism D_k -> T_1(r^ell)_k by h. Let
f:C_k -> (E_o)_k be L109's comparison using the standard Tate curve.
These are models of the present objects, with specified generic maps;
there was no earlier fixed integral model on these new objects to replace.
In particular no old cubic, seven-gon or completion N is substituted.

The models are proper and flat, with smooth elliptic generic fibers
and split standard one-gon and ell-gon special fibers. Their identity
sections are smooth. Let S be the section of C. The one-gon with S
is a stable one-pointed genus-one fiber: its normalization is P^1
with the two node branches and the marking as three distinct points.
The generic pointed elliptic fiber is stable as well. Thus the proper
flat finitely presented nodal family with this smooth marking is stable
by the fiberwise stability condition in the imported pointed-curve
moduli theorem: the normalization of each genus-zero component has at
least three special points, and each genus-one component has a marking.
This verifies its actual stable-family hypothesis; it does not assert
stability of an unmarked smooth genus-one fiber.

Rotation gives a finite-etale formal map hat g:hat D -> hat C of
rank ell. On reduction it maps each normalization component by the
identity to the normalization of the one-gon, carrying the two branch
types individually to their corresponding target branches. The ell
rotates of the identity are smooth disjoint formal sections, one on
each component, all mapping to S. Apply 0A4Z to the proper R-scheme
D and separated finite-type C: their compatible maps modulo pi^a
algebraize uniquely to g:D -> C.

For precision, this algebraic g is finite-etale, not just generically
of the expected degree. At each closed special point x with image y,
the reduction map is etale and has kappa(x)=kappa(y). Put
A=O_(C,y), A'=O_(D,x). For every a the map modulo pi^a is etale
with identical residue field. By the etale direction of 039M its
maximal-ideal completion is a finite free module over the target's
completion. The equal-residue-field case of
[Stacks 41.3.3(2), 039H](https://stacks.math.columbia.edu/tag/039H)
makes the completed ring map surjective. A nonzero finite free module
over a local ring that is generated by its unit has rank one; the
surjection is therefore an isomorphism. This uses the actual equality
of residue fields, not an assertion that every etale local map induces
an isomorphism on completions. For every b, take a>=b;
pi^a lies in both b-th maximal-ideal powers, so these isomorphisms
give A/m_y^b = A'/m_x^b via the given map. Compatibility in b yields
an isomorphism of maximal-ideal completions of A and A'. The converse
of 039M gives etaleness at x. The non-etale locus is closed since
g is of finite presentation. If nonempty, its proper image in Spec R
would meet the closed point and its special fiber would have a closed
point, a contradiction. Hence g is etale everywhere. It is proper
since D is proper and C separated over R. Now 02LS makes it finite.
C is connected: a nontrivial clopen decomposition would specialize
to a disconnection of its connected special fiber by properness.
Consequently the finite-etale rank is constant, and equals ell.

The formal marking sections also algebraize by 0A4Z, using Spec R
as proper source. Their images under g are S by uniqueness. The
inverse-image finite R-algebra has every reduction equal to
(R/pi^a)^ell compatibly with these sections. It is complete and hence
is R^ell. This checks the entire origin fiber, not just ell sampled
points. The marked D is stable: each special component has two node
branches and one marking, and the smooth generic fiber has ell markings.

### Identification of the exact complementary isogeny

Apply Conrad Example 2.5.1 with n=1,m=ell to obtain the algebraic
power isogeny a:C_k -> T_1(r^ell)_k. Its kernel is the unique smooth
torus mu_ell subgroup lifting the identity-component ell-torsion.
This is exactly the Tate-parametrized mu_ell: since p!=ell, reduction
is injective on mu_ell. For zeta!=1 the Tate series have reductions

    x=zeta/(1-zeta)^2, y=zeta^2/(1-zeta)^3

on y^2+xy=x^3, the smooth torus point with parameter zeta. Negative
indices in the series are rewritten with zeta^(-1); all terms with
positive powers of r vanish on reduction. The identity gives S.
Multiplication by ell on the smooth group is etale. Henselian
uniqueness of lifts of these simple torsion points identifies the
two finite etale subgroup schemes. One may check this after a strict
henselization; equality there descends. In our situation L109 and
full local ell-torsion also make these points k-rational.

The comparison of maps uses the origin formal group, not an unverified
coordinate on the whole punctured cover. In Conrad's construction
over Z[[t]], rotation identifies the copies of the smooth formal torus
by retaining its multiplicative coordinate. The quotient smooth locus
is the zeroth copy with that same coordinate, and the identity is its
point X_0=1. Completing there gives exactly (2.5.3) on D and C.
Thus g has differential 1 in those formal-group coordinates. The
characterizing h of Theorem 2.5.2 also has differential 1; the power
map a has differential ell. These identities persist after t -> r.

Both g_k h^(-1) a and [ell] are pointed elliptic homomorphisms of
C_k with differential ell. Their difference has zero differential.
In characteristic zero a nonzero elliptic homomorphism is a separable
isogeny and has nonzero differential. Hence

    g_k h^(-1) a=[ell].                               (3)

Define a'=h^(-1) a f^(-1):(E_o)_k -> D_k. The kernel check and
L109's exact toric-line equality give ker(a')=i_w(U), as subgroup
schemes, not merely isomorphic abstract lines. L107's alpha_k has
that same kernel and degree ell. The cited quotient-factorization
theorem over k gives a unique pointed isomorphism gamma:B_k -> D_k
with gamma alpha_k=a'. The factor has degree one; uniqueness also
ensures k-definition if factorization is first performed geometrically.
Using (3) gives

    f g_k gamma alpha_k=[ell]=psi_k alpha_k.

Cancel the surjective alpha_k to obtain (1). The complete marking
fiber consequently corresponds to all of V_k, including the origin.
No choice of generator or label has entered this argument.

### The tautological stable log and its formal realization

Give Spec R its closed-point divisorial log with chart N -> R,
1 -> pi. Let u:Spec R -> bar M_(1,1) classify (C,S). Pullback of
any boundary-log function is regular on R and invertible on k, and
therefore belongs to this specified divisorial log. This defines a
log classifying morphism on etale charts. On overlaps the maps agree
because each is actual function pullback into the subsheaf M_R of
O_R; on triple overlaps the same equality gives descent. Thus the
morphism is global, including units, without choosing a global
boundary equation or declaring the natural base log to be M_R.

Pull back the universal pointed log curve along this morphism first
in unrestricted log schemes. Its underlying scheme is exactly C.
At the node the smoothing value is r up to a unit, because the Tate
formal annulus has equation XY=r. Write r=v pi^d, d>0, and absorb
v into one branch parameter. The characteristic chart is

    P_d=<x,y,c | x+y=d c>,  x -> X, y -> Y, c -> pi,
    N -> P_d, 1 -> c.                                (4)

The smoothing length d is intrinsic: the relative singular-locus
quotient of the annulus is R/(r). The etale universal node charts
and their strict completed charts give (4) with that same smoothing
ideal; no coprimality of d with p is needed.

Here the unrestricted pushout is already fs. Indeed map x,y,c to
(d,0),(0,d),(1,1) in G_d={(i,j) in Z^2:i-j in dZ}. Reducing by
x+y=d c leaves at most one nonzero branch exponent. The smaller
coordinate determines the c exponent and the coordinate difference
uniquely determines the remaining branch exponent. Therefore P_d
is exactly G_d intersect Z_(>=0)^2, is integral, and is saturated
in its own groupification G_d. The elements x,c form a basis of
G_d, so the base groupification has free rank-one cokernel. The
chart ring is R[X,Y]/(XY-pi^d); the ordinary node comparison is
etale. Kato's chart criterion therefore applies.

Near S the chart is N plus N, with structure values pi and a
simple relative marking parameter; away from node and marking it
is the base N. These charts are fs and log smooth too. They are
charts of the single pulled-back universal log, including branch
interchanges and unit factors on overlaps. Thus its fine/fs
refinement leaves the scheme C unchanged. Its generic log is
precisely the marking log on C_k. By the imported native definition
this is a stable log curve of type (1,1) over the specified base.

Put M_D=g^*M_C. Since g is etale, the same fs charts pull back
without changing the source scheme. The map is strict and log
etale: the unique ordinary etale lift over a square-zero thickening,
combined with the pullback-log universal property, is the unique
log lift. Finite presentation holds. At every source node (4) has
the same d, not ell*d, and each marking parameter is pulled back
simply. This is an unramified graph map, unlike the opposite power
isogeny a. Source marking logs are those of all ell sections.

For a>=1 use strict pullback logs on C_a=C mod pi^a and D_a.
Their etale sites identify with the special-fiber sites by 04DZ.
On that common site, with i:C_kappa -> C, complete the ordinary
structure sheaves and set

    M_hat_C=(i^(-1)M_C -> O_hat_C)^a,

where superscript a here denotes log association, not a reduction
index. This is one sheaf construction; its charts are (4), N^2
and N with completed structure functions. By the associated-log
universal property its pullback to each O_(C_a) is exactly M_(C_a).
The same property identifies M_hat_D with hat g^*M_hat_C. All overlap
maps and their inverses are induced from the algebraic log, so their
cocycles and all reduction compatibilities are retained. Locally units
in a complete chart ring are detected modulo pi by the geometric-series
inverse; no limit/pushout interchange is assumed. These are the usual
adic completions (Stacks [0AHY](https://stacks.math.columbia.edu/tag/0AHY),
[0GXT](https://stacks.math.columbia.edu/tag/0GXT)). The p-adic and
pi-adic topologies agree. The displayed algebraic log schemes exhibit
their algebraizations. Thus all of EtTh section 1's base, stable,
split singular special-fiber and smooth generic-log hypotheses hold.

### Residue components, branch maps, markings and descent

Normalize C_kappa. Its normalization is P^1_kappa, with two distinct
kappa-rational node points a,b and a third point t from S. Order (a,b).
The rotation map on every component normalization of D_kappa is the
actual isomorphism to this P^1, with its structural map to C_kappa.
Starting with the component of the origin, order successive components
by the branch types. Their branch pairs are b_i=a_(i+1), i modulo ell,
and each marking t_i maps to t. There is no folding: each component
has one branch of each target type. Every component, node, branch and
marking is defined over kappa.

EtTh's infinite graph cover copies precisely this normalization and
its structural maps, with components indexed by Z and gluing
b_i=a_(i+1). Its quotient by ell Z has the corresponding ell copies;
call its special cover G_0 -> C_kappa. The constituent maps, including
the two branch-inertia objects and the marking legs, are isomorphisms
as required by Semi-graphs Definition 2.2(ii) and Remark 3.5.1. No
component-to-node or node-to-smooth exceptional case is involved.

Here is the scheme-level comparison over kappa, rather than a graph
count. At a split node of either D_kappa or G_0 let A be its local
ring and A' its finite semilocal normalization. These are reduced
one-dimensional Nagata local curve rings essentially of finite type
over kappa. By [Stacks 53.19.11, 0CBW](https://stacks.math.columbia.edu/tag/0CBW),
[53.19.4, 0C4A](https://stacks.math.columbia.edu/tag/0C4A) and
[33.39.5, 0C3V](https://stacks.math.columbia.edu/tag/0C3V),

    A_hat=kappa[[x,y]]/(xy),
    A' tensor_A A_hat=kappa[[x]] times kappa[[y]].

The actual residue maps give delta:A' -> kappa, the difference of
values at the two branch points. A is contained in ker(delta).
After completion this kernel is exactly the displayed nodal ring.
Exactness on finite modules and faithful flatness of completion,
[Stacks 10.97.1, 00MA](https://stacks.math.columbia.edu/tag/00MA) and
[10.97.3, 00MC](https://stacks.math.columbia.edu/tag/00MC), imply
ker(delta)=A. The uncompleted semilocal normalization is not assumed
to be a product of uncompleted branch rings.

Away from nodes normalization is an isomorphism. Thus the curve's
structure sheaf is the subsheaf of normalization functions whose
residues agree on each indicated pair. The finite surjective
normalization is closed, so the topology too is the quotient by
exactly these pairs. The matching component maps and branch pairs
therefore give an isomorphism a_0:D_kappa -> G_0 over C_kappa.
The component maps commute with the structural maps to C_kappa,
and the residue equalizer preserves their function pullbacks. The
matching third point on each normalization retains every marking.
This proves an isomorphism of covers, not only of abstract curves.

All these maps are kappa-defined. Residue Frobenius fixes each
component and each marking; a nontrivial arithmetic translation
of indices would permute them. It is therefore excluded by this
comparison before any geometric identification is used. Reversing
the ordered branches reverses Z and leaves ell Z unchanged.

### Lifting the actual finite cover and transporting its deck maps

The quotient of the native formal chain cover by ell Z is ordinary
finite-etale: locally it copies the same smooth or nodal neighborhood,
with no ramification at a branch or marking, and has ell sheets.
Its log is the target pullback. It has special fiber G_0.
For each a, nilpotent invariance 04DZ identifies its reduction with
D_a -> C_a through the unique lift of a_0. Full faithfulness forces
these lifts to commute with reduction; hence they identify the formal
covers and their pullback logs.

Apply 0A48 to the proper C over the complete henselian DVR R.
It algebraizes G_0 as a finite-etale G -> C and lifts a_0 uniquely
to an isomorphism a:D -> G. Its completion is the native finite
quotient just identified. The statement is used on C before
puncturing, not on the nonproper X_k. The sections above S are
preserved as well: the finite-etale fiber over S=Spec R is split,
and its special points lift uniquely by the henselian finite-etale
equivalence (or 0A48 on S). Consequently (1), followed by a_k,
identifies the retained punctured Y_k -> X_k with the native cover
corresponding to beta_w^(-1)(ell Z).

To check the arithmetic quotient, take the native index-one
translation on G_0. It is a kappa-defined automorphism over C_kappa.
Full faithfulness of 0A48 lifts it uniquely to G; its powers and
ell-th-power identity lift too. Nilpotent full faithfulness identifies
its formal action with the native finite graph translations. Transport
by a and gamma gives deck maps of the actual Y_k -> X_k. Their
powers are distinct, since their reductions send the origin marking
to the ell distinct marking sections. By L107 these deck maps are
exactly the ell translations by V_k. This constructs the isomorphism
c_w:Z/ell Z -> V_k from actual maps, rather than choosing an abstract
group isomorphism to impose a desired equality.

The native profinite convention identifies its finite arithmetic
monodromy with (mod ell) beta_hat_w. Equivariance of the compared
fibers now gives the first equality in (2). Changes of lifted
basepoint conjugate the maps; both finite deck groups are abelian,
so this causes no change. Taking kernels proves the second equality.
Every comparison was over R or k and the descent was over kappa;
there is no inference of arithmetic equality from geometric equality.
The original cusp's whole trivial decomposition image from L107 is
retained by this isomorphism of covers.

The chosen p was arbitrary in the unchanged finite Sigma. The proof
therefore applies to every already selected s(p), retaining K,U,s and
the global psi. The r and local identifications may vary with p; no
extension of a completion or simultaneous choice of generators is
needed. It proves the stated graph-kernel test only. Definition 2.5's
other predicates, a common cusp sign and compatible theta splittings,
III/P7, full repair/exact generation, relative factor-four excess,
actual input/action/factorization/pilot, source qualifications,
essentiality and original finite B>=A remain open. This is a local
known-method advance validated by the separate audit below, not a complete
candidate or a new theorem claimed beyond the checked sources.

### Separate critical audit — 2026-10-24, step447

**Scope and verdict.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-selected-completion-graph-kernel-critical-audit.md`.
The complete proof passes this REPRODUCTION audit, with the supporting
completion citation and its equal-residue-field argument expanded above.
The statement and direct mathematical inputs L107,L109 are unchanged.
This validates the actual arithmetic graph-kernel prerequisite only.
It does not approve a new target or supply a result beyond the methods
already compared. Pending-audit language for L110 in the unchanged
overview is superseded by this canonical verdict.

**Source use.** Reinspected Conrad's 18 July 2006 author version,
section 2.5 pp.17–18, including (2.5.1)–(2.5.3), Example 2.5.1,
Theorem 2.5.2 and its proof; EtTh PRIMS 45 (2009), section 1
pp.237–239; and Stacks 0A4Z, 039M, 039H(2), 0A48 with their
relevant proof cases at the links above. PDF text, not the screenshot
references returned without displayed images, supplies this inspection.
The log and conductor sources and exact cases recorded in step446's
source notes and the approved L055/L057 audit assessments are reused.
No new discovery search, source-authentication retry or general-theorem
reproof is needed. L055–L057 remain method comparisons on other objects.

**Actual models and algebraization.** L109 gives the pointed comparison
over each actual finite p-adic k, not only over its algebraic closure.
The nonzero r is topologically nilpotent in the complete DVR R. Thus
Conrad's formal variable is specialized to r for both models; the
generic parameter on D is r^ell, while every node has smoothing
parameter r. The origin on C and one marking on every D-component
supply the three special points required for stability of their
rational components. Generic genus-one fibers have markings. No
regular resolution or old integral model is substituted for C.

The source D is proper and C separated of finite type, so 0A4Z applies
to all compatible reductions of the rotation map. On the special fiber,
each normalization-component map is an isomorphism. Hence every closed
special point has the same residue field as its image, including closed
points whose residue field properly extends kappa; the split nodes have
residue field kappa. This verifies the extra premise of 039H(2).
For the local maps modulo pi^a, 039M and 039H(2) give the completed
isomorphisms as expanded above. Taking a>=b identifies the quotients
by the b-th maximal-ideal powers via the original ring map, so these
identifications are compatible. Their limit and the converse of 039M
prove etaleness at the closed special points. A nonempty closed
non-etale locus would have proper image meeting the closed point of
Spec R and a closed special point there. This contradiction proves
global etaleness. Proper quasi-finite g is finite; connected C and the
special-fiber sheet count fix its rank as ell. Algebraization of the
sections and completeness of the finite inverse-image algebra verify
the entire split marking fiber, rather than only generic rational points.

**Origin map and complementary factor.** In the imported rotation
construction the quotient identifies the zeroth smooth formal torus
with the corresponding target torus without changing its coordinate.
Its completion at the identity is the specified formal group (2.5.3).
Thus g has differential 1 in these coordinates. Theorem 2.5.2 fixes h
by the same formal-group identification, and Example 2.5.1 fixes a by
the ell-th power operation. Consequently g_k h^(-1) a has differential
ell. All maps here are pointed elliptic maps over the same k, so their
difference with [ell] is a homomorphism. In characteristic zero a
nonzero such homomorphism is separable with nonzero differential;
equation (3) follows. Etaleness of g alone would not justify this step.

The kernel comparison is also specific. Since p!=ell, ell-th roots of unity
reduce injectively; the Tate-series reductions in the proof identify
their smooth torus points. The ell-torsion equation is etale at these
points, so henselian uniqueness identifies its lifts with the kernel
in Example 2.5.1. The check may be made over the strict henselization
and descended. L109 then identifies this actual subgroup with i_w(U).
Quotient factorization gives gamma over k, and surjectivity of alpha_k
permits cancellation in f g_k gamma alpha_k=psi_k alpha_k. This fixes
the actual psi and its complete marking fiber. Neither matching degrees
nor an abstract isomorphism of cyclic groups replaces this calculation.

**Log structure and completion.** The classifying-map construction
pulls the boundary log into the specified divisorial log of R: on every
etale chart its functions are regular and generically invertible, and
their unit and overlap identifications are their actual pullbacks.
This is a log morphism before the universal curve is pulled back.
At the node the completed smoothing ideal is (r); writing r=v*pi^d
and absorbing v gives the chart (4). In its groupification, x,c form
a basis, y=d*c-x, and the nonnegative cone is exactly P_d. Hence
saturation is in the correct lattice, and the base cokernel is free
even when p divides d. The smooth ordinary chart comparison and Kato's
criterion apply without an invertibility assumption on d. The marking
and smooth charts are the pullbacks of that same universal log.

Strict etale pullback along g retains these fs charts, the thickness d
and every marking. Strict reduction does not replace the log by a
divisorial log of an empty complement. On the common reduction site,
the single completed prelog sheaf and log association induce all the
strict reduction logs by their universal property. Algebraic overlap
maps and cocycles persist after completion; no association/inverse-limit
commutation is assumed. The algebraic models exhibit the required
algebraizations. These checks verify the actual EtTh section 1 object.

**Residue descent and arithmetic maps.** Both special covers consist
of the same kappa-defined normalization copies and the same structural
maps to C_kappa. Each branch pair is the actual b_i=a_(i+1), and the
third marked point is retained. The finite semilocal normalization at
each split node satisfies the cited completion hypotheses. For its
residue-difference map delta, the finite module ker(delta)/A becomes
zero after completion, since the completed equalizer is precisely
kappa[[x,y]]/(xy). Faithful flatness makes that module zero already
over A. This proves structural descent, without identifying an
uncompleted semilocal normalization with a product of branch rings. Together
with the quotient topology and the smooth locus it proves a_0 as an
isomorphism over C_kappa, with markings, over kappa itself.

The finite quotient of the native chain copies smooth and nodal
neighborhoods and has pullback log, so ordinary finite-etale comparison
applies. Nilpotent full faithfulness identifies all reductions and their
transition maps. The proper henselian theorem is applied to C before
puncturing. It lifts a_0 and every index translation, including all
composition laws. The split fiber over S retains the marked sections.
The ell powers are distinct on those sections; after transport by gamma
they exhaust L107's actual translation deck group V_k. Thus c_w comes
from actual deck maps. EtTh's quotient on p.238 is arithmetic and its
profinite convention retains the finite mod-ell quotient. Equivariance
of the identified covers therefore gives equation (2), including the
arithmetic kernel. The comparison over kappa excludes a hidden residue
Galois permutation of the sheets; geometric kernel equality alone would
not do so. Abelian deck groups remove basepoint conjugation ambiguity.

**Boundary.** The same argument applies separately at every fixed
s(p), with the same U, global cover and selected prime. No new section
or completion is chosen. The double-dot field predicate, common sign,
compatible splitting, independent initial data/III/P7, exact generation
and full repair, relative factor-four excess, actual input/action/pilot,
source qualifications, essentiality and finite B>=A remain unresolved.
There is no complete candidate. No numerical calculation or mathematical
script is required for this audit.

## Mathlib

Full matching Mathlib coverage of the stable log model, native tempered
graph quotient and this arithmetic-kernel specialization has not been
checked. Supporting coverage is likewise not assessed here; unknown
availability is not absence. The precise imported results and full
applicability comparisons above constitute the informal argument.
There is no numerical certificate, mathematical script or formal
verification claim. The separate informal audit above adds no Mathlib
coverage or formal-verification claim.
