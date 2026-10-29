# L113 — Common native cusp sign by stabilizer place reselection

## Hypotheses

Retain L105's same member, ordering, E_o,G_o,C_o and selected prime
ell>=7, L107's full K=K_C=C_o(E_o[ell]), and its fixed maps

    alpha:E_o,K -> B=E_o,K/U, psi:B -> E_o,K,
    psi alpha=[ell], V=ker(psi)=alpha(E_o[ell]).

Here U is one fixed line in M=E_o(K)[ell]; neither U nor B is
assumed defined over C_o. Retain L108's full section s over
F_mod=Q and Sigma=S minus {ell}, S={p:v_p(j(E_o))<0}.
For w=s(p), p in Sigma, use L110's actual pointed graph-cover
comparison and c_w:Z/ell Z -> V(K_w), up to orientation, and
L111–L112's field predicates and pointwise theta choices.
All source authentication and def= qualifications are inherited.

## Conclusion

For any one fixed Q in V(K) minus {O_B}, there are elements
sigma_p in Gal(K/C_o) stabilizing U setwise such that the choices

    s'(p)=sigma_p s(p)  (p in Sigma),
    s'(p)=s(p)         (p outside Sigma)

form a full section over Q. Each changed place retains its restriction
to C_o. At all the new selected completions, U is still the toric
line, L110–L112's graph, field and existential pointwise splitting
prerequisites hold on the same global cover, and the native cusp
specified by Q has label plus-or-minus one:

    {c_(s'(p))(1),-c_(s'(p))(1)}={i_(s'(p))(Q),-i_(s'(p))(Q)}.

The c on the left is induced by the actual graph cover and its
origin marking, not a freely chosen cyclic isomorphism. Equivalently
the global free cusp pair {Q,-Q} has the required local sign at every
selected place. No equality of the old and new auxiliary theta choices,
global theta splitting, full initial data or numerical conclusion is
asserted. The separate step459 critical audit below validates this
known-method specialization; it is not a candidate demonstration of
an essential IUT flaw.

## Proof

### Source scope, duplicates and bounded test

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-common-cusp-label-place-reselection.md`,
with its inspected primary passages in the step456 source record.
Import the following results without general reproof:

- Sutherland, [MIT 18.783 Lecture 5, 26 September 2023](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
  Theorem 5.11, pp.5–6: quotient by a finite translation subgroup
  and uniqueness respecting its quotient map. Milne, [Elliptic
  Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
  II.1.7, p.49, supplies complementary factorization, as in L107.
- Conrad, [Transitive Group Actions](https://kconrad.math.uconn.edu/blurbs/grouptheory/transitive.pdf),
  Theorem 4.21, proof/equation (4.1), p.10: in a basis whose first
  vector spans U, its SL_2 stabilizer consists of matrices with rows
  (a,b),(0,a^(-1)), with a nonzero. The quotient-vector consequence
  below is a specialization of that displayed description.
- Mochizuki, [The Etale Theta Function, PRIMS 45 (2009)](https://ems.press/content/serial-article-files/41069?nt=1),
  section 1 pp.237–239, orientation p.244, Definition 2.5(i) p.265,
  and label discussion/Corollaries 2.8–2.9 and proofs pp.267–269:
  integral graph translations, labels from components containing
  cusp closures, and their preservation by the indicated actual
  local isomorphisms. We use actual model isomorphisms, not an
  assertion that arbitrary finite cyclic automorphisms preserve labels.
- [Stacks 58.6.2(1)–(3), 0BND](https://stacks.math.columbia.edu/tag/0BND)
  gives finite-etale pullback/monodromy compatibility, including
  basepoint inner ambiguity. The proper henselian full faithfulness
  of [58.9.1, 0A48](https://stacks.math.columbia.edu/tag/0A48) is used
  on proper models, as already checked in L110.

The Tate, Conrad-model, log and splitting imports, with versions and
proof cases, are precisely those of L108,L110–L112 and the reused
assessments identified in step456. No general theorem is reproved.
The additional same-object checks are necessary because those results
do not themselves choose a common global cusp. DH v1 Lemma 5.6.2,
p.31, only supplies the fixed-line/variable-place method, already used
in L108. L059 is a different-object label method, not an input here.
ATTEMPTS/031's marked-coordinate stop is preserved: this argument
transports the actual models, without writing a new overlap atlas.

Main gap: original finite B>=A. This intermediate could supply the
independent native common-cusp condition. Continue only if the actual
semilinear quotient action and native sign covariance pass, the
stabilizer acts transitively on nonzero quotient vectors, and all
local prerequisites survive. Abstract relabeling or mod-ell kernel
equality would fail this test. The independent III/P7, full repair,
relative factor-four excess and actual numerical comparison remain open.

### The actual semilinear action on the fixed quotient

Put G=Gal(K/C_o) and H={sigma in G:sigma U=U}. By L108, K/C_o
is Galois and its faithful action on M has image containing SL_2(F_ell).
For sigma in H, conjugate the actual pointed quotient alpha by sigma.
The curve E_o is defined over C_o and is therefore identified with its
conjugate. The conjugated quotient has kernel sigma U=U. Quotient
uniqueness gives a unique pointed K-isomorphism from the conjugate
of B to B commuting with the two quotient maps. Combined with
coefficient transport, this is a sigma-semilinear map b_sigma on B.
On geometric points, after extending sigma to an algebraic closure,
it is characterized by

    b_sigma(alpha(P))=alpha(sigma P).                  (1)

This is well-defined: two preimages differ in U, whose image under
sigma is again U. It is an algebraic semilinear map by the quotient
construction, not merely a map on torsion points. Uniqueness implies
b_sigma b_tau=b_(sigma tau), b_1=id, and inverse b_(sigma^(-1)).
These assertions do not descend B to C_o; they concern H alone.

Since [ell] is defined over C_o, (1) and psi alpha=[ell] give

    psi b_sigma=sigma psi,                            (2)

by cancellation of the surjective alpha, with semilinear meaning
on the right. Origins and inversion are preserved. Thus b_sigma
carries V to V and, under the canonical F_ell-linear isomorphism
M/U -> V(K) supplied by alpha, its action is exactly

    alpha(P) |-> alpha(sigma P).                      (3)

There is no premise that all of G acts on this fixed quotient.

### Native sign covariance through actual local covers

Fix p in Sigma and w=s(p). For sigma in H let w'=sigma w, where
(sigma w)(x)=w(sigma^(-1)x). L108 constructs the isometric field
isomorphism t:K_w -> K_w' with

    t(i_w(x))=i_w'(sigma x).                           (4)

It preserves the valuation rings, maximal ideals and residue fields,
and identifies the copies of the underlying C_o-completion.
It carries q_w to q_w': the small Tate parameter is uniquely determined
by j, which is fixed, and t preserves absolute values. The rational
Tate formulas commute with t. Transport a pointed split comparison
at w by t; it is a pointed split comparison for E_o at w'.
L108's toric-line covariance gives

    T(w')=sigma T(w)=sigma U=U.                        (5)

For clarity, transport L110's entire construction, not just its
finite kernel. The models T_1(q_w), T_ell(q_w), their rotation map,
origin sections and all inverse-image markings base change by t to
the corresponding models for q_w'. These are Conrad's same
parameterized constructions. The log is the pulled-back stable
boundary/marking log over the closed-point DVR log, so transports
with those models, as do every strict reduction and its completion.
The comparison gamma at w' is the transported comparison composed
with b_sigma^(-1) on its B-source: equation (1) makes its quotient
factorization commute, and uniqueness of that factorization identifies
it with the comparison constructed in L110 for the transported f.
Equation (2) verifies the actual complementary map psi as well.
In particular the induced map on deck translations is

    translation by v |-> translation by b_sigma(v).   (6)

On the special fiber, the normalization, branch maps, conductor
gluing and origin marking are transported as actual maps. The base
one-gon's two branches are either retained in the chosen order or
exchanged if we independently reverse orientation at w'. Its infinite
graph chain therefore has its integral index transported as n -> n
or n -> -n. Choosing the component above the origin as index zero
removes a possible offset. This is an integral graph identification:
no other multiplier in (Z/ell Z)^times arises by reducing it.

L110's residue-cover comparison and proper henselian full faithfulness
transport the actual index-one deck map with these data. Consequently
(6), including the effect on the origin marking, identifies the new
native index-one translation with b_sigma(c_w(1)) or its inverse.
Basepoint conjugacies do not affect this abelian deck group. Pulling
all local V-points back to V(K), possible because the entire V is
K-rational by L107, put

    d_w=i_w^(-1)(c_w(1)) in V(K) minus {0}.

We have proved the sign-pair identity

    {d_(sigma w),-d_(sigma w)}
        ={b_sigma(d_w),-b_sigma(d_w)}.                (7)

The identity uses actual model, marking and deck transport, rather
than only equality of kernels. It agrees with the native component
label convention: the origin has label zero and the index-one deck
map sends it to the unique cusp on the adjacent component. The
cyclic cover has one marking per component. The full non-arithmetic,
field and additional-cover hypotheses needed for the local type can
be retained as explained next; Corollary 2.9 is not used to supply
a missing theta splitting or an arbitrary generator normalization.

### Retaining field and theta prerequisites

The new completion is isomorphic to the old one as a valued field
over the same C_o-place; it has odd residue characteristic p!=ell.
The transported local base is still E_o, and (1)–(2) identify the
transported source cover and origin with the same B,psi,O_B.
Thus L110's actual graph statements hold at w'. L111's square root
of q_w transports to a square root of q_w'. Its square root of -1
transports to a square root of -1. The embedded iota may change to
its negative, which does not alter that membership. The unindexed
k=double-dot k=k_2 predicate consequently holds at w'. Full local
2-torsion and full ell-torsion remain rational. A primitive ell-th
root is present by the split Tate toric mu_ell and full ell-torsion;
transport retains its order.

Transport an entire set of L112's existing local auxiliary data at
w: its dotted diagram, common cusp, full inertia-equivariant cusp
torsors, theta function and permitted standard normalization. They
are objects and maps over this valued field; coefficient transport
preserves their equations and the theta series, which converge and
have rational integral coefficients in the Tate construction. Unit
normalizations, the sign pair and Kummer classes transport along the
field isomorphism. Equivalently one may apply exactly L112's local
construction to the transported input; its proof uses no condition
on the other selected places. The local core predicate is retained
by this actual field/curve isomorphism. At every finite inertia
level, the transported torsor maps remain equivariant, with their
possible Kummer translations, and the kernel ell I_x is unchanged.
Oddness still identifies the two finite sign classes. Proposition
2.2(ii)'s retained-origin additional cover thus transports to an
additional cover of the same B minus V over K_w', of the same
geometric index ell and with geometric connectedness preserved.

This argument establishes existential pointwise choices at w',
not equality with old auxiliary objects or a global splitting.
It does not silently apply L112's old-section conclusion to new
places: it transports its witnessed local objects and all premises.
These are the local type/field/root conditions used in the native
label convention. No indexed radical equality, C_o-defined U,
downstairs splitness or enlargement of a completion is introduced.

### Quotient-vector transitivity and choice of section

Choose a basis (u,z) of M over F_ell with U=F_ell u. The inspected
SL_2 stabilizer matrices act on M/U by multiplication by a^(-1).
For any two nonzero elements of this one-dimensional quotient there
is a unique required nonzero scalar lambda; choosing a=lambda^(-1)
and b=0 realizes it. L105's actual image contains that matrix, and
faithfulness/image identification for G supplies an element sigma
of G with this action on M. It stabilizes U and hence lies in H.
By (3), H is therefore transitive on V(K) minus {0} through actual
semilinear quotient maps. This is stronger than transitivity on
lines, and does not replace the global Q by a renamed generator.

Fix Q once in V(K) minus {0}. For each p in Sigma choose either
orientation at w=s(p), compute its actual d_w, and choose sigma_p
in H with b_(sigma_p)(d_w)=Q. Such an element exists by the preceding
paragraph. Set w_p'=sigma_p w. Equation (7) gives the desired sign
pair at w_p'. The direction is sigma_p acting on both place and
cusp; an inverse place action would not justify this conclusion.
By (5) and the preceding transport, every local prerequisite is
retained. Each sigma_p fixes C_o, so w_p' lies over the same C_o-place
as w and therefore over the same rational p. Different p have
disjoint fibers. Leaving s unchanged outside the finite Sigma gives
a full section s' over Q without any further compatibility condition.

Since Q has odd order ell, Q!=-Q. The pair is free under inversion;
the disjoint rational points {Q,-Q} descend to a rational scheme
cusp of the quotient orbicurve: on the free locus the finite constant
involution gives an etale torsor and its quotient is an algebraic
space, with this rational two-point orbit giving Spec K as the
corresponding cusp. This is precisely the cusp's local sign-pair
description, with interior inversion stabilizers retained.

All four bounded tests pass by known methods on the same objects.
This supplies one independent native cusp condition, validated by the
separate audit below. It does not settle initial data/III/P7,
exact generation or full field repair, the relative factor-four
excess, actual input/action/factorization/pilot, inherited source
qualifications or essentiality, or original finite B>=A. No progress
beyond the inspected methods or complete flaw candidate is claimed.

### Separate critical audit — 2026-10-24, step459

**Scope and source use.** This REPRODUCTION audit uses the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-common-cusp-reselection-critical-audit.md`.
The complete L113 proof, L108's completion and comparison argument,
L110's actual models, quotient factorization, residue comparison and
deck lifting, and L111–L112's field and arithmetic splitting premises
were checked against the same-object statements of L105 and L107.
The source scope and duplicate/failure screen of steps456/458 are
reused, including the exclusion of ATTEMPTS/031's marked atlas.

For the load-bearing quotient and label comparisons, rechecked the
primary statements and proof cases of Sutherland Theorem 5.11,
pp.5–6; Conrad Theorem 4.21, proof and (4.1), p.10; and published
EtTh p.244, Definition 2.5(i), p.265, and Corollaries 2.8–2.9,
their proofs and the intervening label definition, pp.267–269, at
the URLs cited above. These are checks of already covered imports,
not a new discovery assessment. The Tate, model, henselian and
theta/core imports retain the precise versions and hypotheses in
L108,L110–L112. No source authentication or Mathlib result is added.

**Quotient maps and composition.** Kernel equality here is equality
of finite subgroup schemes: characteristic zero makes E[ell] etale,
and all its geometric points are already K-rational. Thus sigma U=U
really permits the quotient uniqueness theorem. The resulting map
from the conjugate quotient to B is pointed and defined over K;
uniqueness over K follows as well by cancelling the surjective alpha.
It is not an arbitrary identification of isomorphic elliptic curves.
The two semilinear composites b_sigma b_tau and b_(sigma tau) agree
after alpha, so they agree. Likewise

    psi b_sigma alpha = [ell] sigma = sigma [ell]
                         = sigma psi alpha

proves (2). In particular the same map identifies the actual cover,
its entire origin fiber and inversion. On V the isomorphism M/U -> V
intertwines this action with the quotient linear action. The argument
uses only H, not a claimed action of all G or descent to C_o.

**Completion square and pointed comparison ambiguity.** If
w'=sigma w, then |sigma x|_w'=|x|_w on K; the inverse completed map
comes from sigma^(-1). Hence t really is an isomorphism of complete
valued fields. It fixes the embedded Q_p and identifies the two copies
of the same C_o-completion. Uniqueness of the small Tate parameter and
continuity give t(q_w)=q_w'. The same holds for the rational Tate
maps, with chosen algebraic roots transported as part of the data.

Write t_* for coefficient transport, and theta_sigma for the pointed
identification t_*B_w -> B_w' induced by the quotient isomorphism.
It sends t_*(i_w(v)) to i_w'(b_sigma(v)). Under the canonical
identifications of the transported parameterized models, the correct
new comparison is specified by

    gamma_w' theta_sigma = t_*(gamma_w).

To verify it, precompose with t_*(alpha_w). Equation (1) in the
semilinear-action paragraph identifies theta_sigma t_*(alpha_w)
with alpha_w' on the transported E. L110's defining identity
gamma alpha=h^(-1) a f^(-1) then identifies both sides with the
transported power/quotient map. Quotient uniqueness proves equality.
Equation (2) similarly verifies f_w' g_w' gamma_w'=psi_w'. This
removes any possible inverse-direction ambiguity in transporting gamma.

The native sign pair also does not depend on choosing this transported
f instead of another allowed pointed split comparison. L108's
nonexceptional j in characteristic zero makes any two such f differ
by ±1. If f is replaced by -f, L110's defining factorization replaces
gamma by -gamma. Conjugating an index-one deck translation through
-gamma replaces its V-point by its negative. Reversing the branch
orientation has the same sign effect. Thus every permitted comparison
gives the same unordered pair; no normalization by an arbitrary
element of F_ell^times is permitted or needed.

**Integral graph and actual deck maps.** The coefficient isomorphism
transports the proper models, their normalizations, the two ordered
branches of each node and all marked sections. Label the origin
component zero in the infinite chain. Its neighbor through the chosen
outgoing branch is then one. Preserving branch incidence sends zero
to zero and one to one; induction along the chain sends every n to n.
Exchanging the two branch types instead gives n to -n. This reasoning
takes place on the integral chain, before its ell-periodic quotient.
It uses the actual structural maps and markings, not an automorphism
of the abstract finite deck group. In particular the component next
to the origin still contains exactly the corresponding single cusp.

For the finite quotient, transport the residue-cover identification
used in L110. The resulting component and branch maps agree with
those for the new parameter; their residue equalizer gluing preserves
the entire special-fiber cover and markings. Full faithfulness on
the proper model in Stacks 0A48 makes the lifted deck diagram commute.
Only after that lift do we pass to the generic punctured cover.
Thus the transported index-one deck map is the new index-one map,
or its inverse under reversed orientation. Conjugation by the pointed
theta_sigma sends translation by v to translation by b_sigma(v).
This proves (7) for actual arithmetic maps. Abelian deck groups remove
the remaining inner basepoint ambiguity. No arbitrary nonproper or
ramified log cover is submitted to 0A48.

**Every local prerequisite survives.** The new field is finite over
Q_p with the same odd p!=ell. It has the transported square root of
q_w and fourth root of unity. In fact iota belongs to C_o, so the
chosen global iota is fixed by sigma under these completion
identifications; allowing the alternative root has no effect.
The unindexed double-dot equality, full 2-torsion, full ell-torsion
and primitive ell-th root therefore persist. The stable pointed log
model and its graph quotient transport as above. Its local core
predicate persists because transport along a field isomorphism gives
an equivalence of the defining categories of covers and quotients,
preserving their terminal core; no new comparison with a completion
as a field extension is required.

For precision about arithmetic transport, choose an extension of t
to separable closures, giving an isomorphism F_G:G_k -> G_k'. The
transported common-cusp diagram gives compatible isomorphisms F_D
of the full cusp extensions and F_bar of their finite-geometric
quotients. With rho,rho' the quotient maps, one has

    rho' F_D = F_bar rho,
    r' = F_D r F_G^(-1)

for an actual full section r. These are isomorphisms over F_G, not
an unwarranted assertion that the two absolute Galois groups are
literally the same. Full inertia and its subgroup ell I transport;
Kummer cocycles of a in k^times go to those of t(a). Thus the affine
translations from the cusp-coordinate derivatives are retained.
The two sign-related classes still have the same finite image, since
t(-1)=-1 and ell is odd.

Transport the witnessed dotted objects, theta class and its chosen
unit normalization, rather than claiming independence of all old
choices. The valued-field isomorphism preserves convergence, units,
the normalized value 1 and the integral structures on these transported
objects. Roots or coefficients used in the construction are transported
too; no rational-coefficient premise for every auxiliary theta object
is needed. Consequently the witnessed sign reduction transports to
one for the new local input. At the additional-cover stage the
isomorphism F_P on L112's actual quotient sends its subgroup J to
J'=F_P(J). It sends the geometric subgroup D and W=J intersect D
to their new counterparts. Hence [P':J']=ell, J' surjects onto G_k',
and its geometric coset action is transitive. The additional cover
remains geometrically connected, based at the transported O_B, on
the same global B minus V. This checks existential pointwise
splittings and covers, without asserting a global theta splitting.

**Transitivity, section and global cusp.** In a basis (u,z) with
U=F_ell u, the matrix diag(lambda^(-1),lambda) is in SL_2(F_ell)
and acts on M/U by lambda. L105's actual image over C_o supplies
its preimage in G; that preimage belongs to H. Let d_bar and Q_bar
be the inverse images of d_w and Q under M/U -> V. Both are nonzero,
so choose lambda with lambda d_bar=Q_bar. Equation (7) then
gives the required pair at sigma w. There is no need for H to act
transitively on all places: the chosen orbit of w already suffices.
Every sigma fixes C_o, so these choices stay in the old C_o-fibers.
The finite prescriptions over distinct rational primes are disjoint,
and the old section supplies every other place.

Finally Q!=-Q since ell is odd and Q is nonzero. In the compactified
inversion quotient of B minus V their two rational branches form a
free orbit with trivial stabilizer and quotient Spec K. This is a
rational scheme cusp, not a removal of the interior stack stabilizers.
Its closures give precisely the local sign-pair description already
checked, with the same global Q at every selected place.

**Verdict.** L113 passes this separate critical audit with its stated
existential local-choice and source qualifications. The sign ambiguity,
semilinear direction and full arithmetic theta transport have been
made explicit; the statement and direct mathematical inputs are
unchanged, so no DAG edge is added. This validates one local-data
input by known methods, not mathematics beyond the inspected sources.
No original-hypothesis IUT contradiction or finite B>=A bound results.
All independent limitations listed above remain, and no complete
candidate or complete initial-data verdict is asserted.

### Same-object native-clause comparison — 2026-10-25, step461

**Scope and precise limited conclusion.** Use the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-24-reselected-native-clauses-assembly.md`.
Under this lemma's unchanged hypotheses, take F=C_o, K=K_C,
X_0=(E_o)_K minus O, Y=B minus V,
Z=[X_0/{±1}] and A=[Y/{±1}]. Choose exactly

    Vbad_mod=Sigma=S minus {ell},
    mathcal V=s'(V(Q)), mathcal Vbad=s'(Sigma),
    epsilon=the cusp of A represented by {Q,-Q}.

Then the global clause-(d) predicates, full-section predicate, designated
bad-place local-type and local-theta-model predicates, and the nonzero
native cusp predicate in Definition 3.1(d)–(f) hold simultaneously on
these objects, subject to the inherited source qualifications. This is
a narrowed comparison: the all-place fundamental-group injections and
the final directed-cover consequences are not established in this step.
In particular it is not a verdict that every assertion of (d)–(f), or
that complete initial theta-data, has been verified.

**Imports and reason for the application.** The precise predicate source
is Mochizuki, *IUT I*, May 2020, 186-page
[reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf),
Definition 3.1(b)–(f), printed pp.61–63. Its section 1 construction,
pp.37–38, Definition 1.1 and Remark 1.1.2, p.39, will not be applied
without checking its explicit hypothesis (*). Import also published
EtTh Proposition 2.2(i)–(iii), complete proof pp.263–264, Definition
2.3, p.264, and Definition 2.5(i), p.265, at the journal link already
cited above. These statements and proof cases were reinspected for
this application; their general constructions are not reproved.
L107's global application and L110–L113's separate audits are reused.
The application is needed to check simultaneous witnesses, not to
claim an additional general theorem or to reopen the marked atlas or
source-authentication attempts in ATTEMPTS/031,035.

**The one section and support.** L108 retains L103's support predicates:
Sigma is finite, contains 3, excludes 2 and ell, and E_o is
multiplicative at every C_o-place above Sigma. Reselection changes no
restriction to C_o. Thus the designated subset is nonempty and has
the required odd residue characteristics, and its full F-fibers retain
multiplicative reduction. The assertion here about full fibers is the
retained input, not a conclusion from testing only selected places.
Because s' is a section over Q and different rational-place fibers
are disjoint, restriction gives a bijection mathcal V -> V(Q), with
mathcal V intersect V(K)bad exactly s'(Sigma). The complement includes
the selected ell-place and the infinite place. If ell belongs to S,
it is still outside this designated bad subset. Nothing here supplies
a graph/sign test at ell or ell-integrality.

**Global and local covers are the same covers.** L107's separately
audited global application establishes the actual arithmetic elliptic
quotient, core Z, types of Y and A, all three global clause-(d)
diagrams, and geometric theta subgroups on the present K,U,alpha,psi.
Changing selected places does not change any of them. For any selected
w, define all local curves by the actual embedding K -> K_w.
Associativity of base change applied to L107's stack square gives

    A_(K_w) times_(Z_(K_w)) (X_0)_(K_w)=Y_(K_w).

The corresponding squares after an algebraic-closure base change
are also cartesian. Keep compatible geometric basepoints through
these actual maps and retain every inversion stabilizer. This proves
the curve-square assertion at all selected places, without an assertion
that a completion is a finite algebraic extension of K. A proof or
precise import of the associated geometric-base-extension and
decomposition-group identifications is still needed to justify all
the displayed all-place group injections in clause (e). That extra
assertion is withheld, rather than inferred solely from the squares.

**Bad-place type and the local theta models.** Fix p in Sigma and put
w=s'(p), k=K_w. L113's proved transport gives witnesses to L110–L112
at this w for the unchanged Y -> X_0, its origin O_B, and inversion.
In particular k is finite over Q_p with odd p distinct from ell,
k=double-dot k, and the actual arithmetic monodromy factors through
the graph quotient with the recorded integral normalization. Its
factorization is in EtTh's arithmetic elliptic quotient by L107,
not only on the geometric subgroup. The transported finite cusp
splitting comes from the allowed theta sign reduction on the actual
common-cusp diagram, as required in L112.

EtTh Definition 2.5(i) therefore applies to A_k and Y_k on these
witnesses. Its hypotheses are not being replaced by rationality of
cusps or by equality of geometric graph kernels. L112 already gives
the additional geometrically connected degree-ell cover T_w -> Y_k.
Apply Proposition 2.2(iii) to that very splitting and the retained
inversion with origin O_B. The proposition supplies the quotient
theta orbicurve H_w and its cartesian double-cover square with T_w,
Y_k and A_k. Its odd-level proof identifies the order-two coset
normalizing the splitting subgroup; no independently chosen lift of
inversion is imposed. Definition 2.3 and then Definition 2.5(i) give
the required theta types of T_w,H_w.

These are models of the geometric theta covers recalled in L107.
This finite-quotient comparison does not require assuming the full
all-place fundamental-group injections left open above. Choose an
algebraic closure of k containing an image of the fixed algebraic
closure of K. The global finite geometric theta quotient in L107
defines a connected finite-etale Galois cover over the latter
algebraically closed field. It is geometrically connected and stays
connected after this field extension. Its pulled-back monodromy is
therefore surjective by the finite-etale correspondence. The natural
geometric-group maps preserve the defining commutators, ell-th powers
and covering subgroups, so induce maps on the finite theta quotients.
On the rank-one curve the intrinsic local and global quotients both
have order ell^2, and their inversion quotients both have order
2ell^2, by EtTh Proposition 2.2's construction as used in L107,L112.
Surjectivity just proved makes these maps isomorphisms. They commute
with the retained origin inversion. Thus the eigensubgroup and the
unique order-two coset in parts (i),(iii) agree under these maps.
Restriction of L112's arithmetic splitting subgroup to the geometric
group is exactly that eigensubgroup. Taking full profinite preimages
therefore gives the pullbacks of L107's geometric theta groups,
up to compatible basepoint conjugacy. The same correspondence
identifies their covers over the local algebraic closure. This verifies local models, not
a global arithmetic theta model or a global splitting. Independent
choices at finitely many selected bad places need no common arithmetic
section, and do not alter the global cover or cusp.

**One cusp and the limit of the verdict.** The point Q is fixed once
in V(K) minus zero. L107 identifies V with the source rank-one quotient
E_o[ell]/U. Thus epsilon is the nonzero quotient cusp in clause (f).
At each bad selected place, L113's sign identity identifies its
actual two branches with the native index-one pair. Oddness makes
Q and -Q distinct, so their inversion orbit is free and gives the
rational scheme cusp of A. No independent relabeling occurs at any
place. This proves simultaneous satisfaction of the listed predicates.

For directed covers the source instead requires hypothesis (*) on
a specified mod-ell abelianized geometric fundamental group. The
retrieved text flattens the decorations distinguishing its curves;
the precise subscript has not been certified here. In particular
full rational E_o[ell], rational V, and a rational epsilon must not
be silently promoted to trivial action on a module attached to B or
Y. Nor is a missing verification a counterexample to (*). The
directed-cover import, including generic-fiber covers at good places
above ell, is therefore withheld. Screenshot references supplied no
viewable image and the shell download failed DNS; neither is evidence
for a particular subscript or for author/journal byte authentication.

This is a partial REPRODUCTION application of the checked sources,
with the two remaining comparison obligations explicitly isolated.
The new assembly awaits a separate critical review; the earlier
critical audit validates its inputs, not this added application.
Complete (a)–(c)/initial-data/III/P7, exact generation/full repair,
relative factor-four excess, actual input/action/factorization/pilot,
authentication/def=, essentiality and finite B>=A remain independent.
There is no complete flaw candidate.

### Separate critical audit of the assembly — 2026-10-25, step469

**Scope and imported tools.** This audit executes the unchanged SPECIALIZE
assessment `drafts/literature/2026-10-25-native-assembly-critical-audit.md`.
It checks exactly step461's listed simultaneous predicates, using the
same objects and the prior step459 transport verdict. Reused the source
comparison and failure screen, and reinspected EtTh section 2 opening,
Definition 2.1 and Proposition 2.2(i)–(iii), including its complete proof,
pp.261–264; Definition 2.3, p.264; Definition 2.5(i), p.265, at the journal
URL above. The native comparison is the same qualified IUT I May 2020
reproduction, Definition 3.1(b)–(f), pp.61–63. Neither authentication nor
the parked directed-module extraction is retried. No general source
theorem is reproved.

For geometric base change reuse the already covered direct imports:
Landesman, *Invariance of the tame fundamental group under base change
between algebraically closed fields*,
[arXiv:2005.09690v3, 20 January 2024](https://arxiv.org/html/2005.09690v3),
Theorem 1.1 and its preceding characteristic-zero observation (smooth-curve
case: Lemmas 2.6,2.9 and Proposition 2.10); Zoonekynd, *The Fundamental
Group of an Algebraic Stack*,
[arXiv:math/0111071v1](https://arxiv.org/pdf/math/0111071v1), Corollary 6.4,
pp.13–14; and Stacks 0BND cited above. These are the source tools also
used in L114, not an invocation of L114 as a mathematical input. In
particular no conclusion depending on this assembly is used to prove it.

**The same global witnesses.** L108 gives the full section and the
all-F-fiber multiplicative-reduction assertion for Sigma, not only an
assertion at the selected completions. Step459 changes a selected place
only by an automorphism fixing F=C_o, so preserves that assertion and
its restriction to F. It changes neither Sigma nor any global field,
curve or map. Since 3 belongs to Sigma and 2,ell do not, the designated
set is nonempty with the required residue characteristics. The image
of s' maps bijectively to V(Q), and its intersection with the inverse
image of Sigma is exactly s'(Sigma). Calling the complement good is
only the source's designation; it does not imply good reduction there.

L107 step435 supplies the global covers, core and three diagrams with
these exact objects. The global origin is still O_B. For each completion,
base change preserves the actual quotient-stack atlas and gives
A_k times_(Z_k) (X_0)_k=Y_k. No stabilizers are removed, no descent of U
is assumed, and the finite-etale curve square alone is not used to
claim completion-group injections. Those are a separate result.

At every designated w, step459 transports the entire pointed graph
model and L112's witnessed dotted diagram and theta normalization. Thus
one may use the transported splitting for the transported graph model;
there is no independent reselection of incompatible witnesses. The
field is finite over Q_p, p is odd and distinct from ell, the unindexed
double-dot equality holds, the local core remains the one in L112,
and the actual arithmetic rank-one quotient factors through the graph.
The full cusp decomposition group has trivial rank-one image, by the
split origin fiber of the same isogeny. These verify the premises of
EtTh section 2 and Definition 2.5(i). In particular the splitting is
obtained from the allowed sign reduction, not chosen merely because
its finite extension happens to split.

**The arithmetic inversion construction.** Fix such a w and write
P_Y,P_A for the images of pi_1(Y_k),pi_1(A_k) in the source's quotient,
whose geometric kernels are D_Y,D_A. Thus P_Y has index two in P_A,
D_Y has order ell^2 and D_A has order 2ell^2. These D's are finite
geometric kernels in this paragraph, not the full profinite groups.
Let W be Proposition 2.2(i)'s minus eigensubgroup of D_Y. Its order is
ell; part (ii) identifies P_Y/W with the actual finite-cusp extension
bar D_x over G_k. Retain L112's actual section sigma:G_k -> bar D_x
and put J=(P_Y -> bar D_x)^(-1)(sigma(G_k)). L112 checks

    J intersect D_Y=W,  J -> G_k surjective,  [P_Y:J]=ell.

The source's part (iii) applies to this very sigma. Choose an order-two
representative tau in its specified geometric coset modulo W. The
proof on pp.263–264 shows that tau centralizes P_Y/W: it uses odd ell
and the absence of 2-torsion in the indicated splitting-torsor and
invariant-quotient groups. It does not require an invariant representative
of a full infinite-inertia section or a globally chosen theta section.
Consequently tau normalizes J, since J is the inverse image of the
specified section image in P_Y/W. It also normalizes W. Define

    J_A=J union J tau,       L_w=W union W tau.

These are subgroups of P_A,D_A respectively. They are independent of
the chosen representative within tau W, because W is contained in J.
The two cosets are distinct: tau lies outside P_Y. Hence

    J_A intersect P_Y=J,   [J_A:J]=2,   [P_A:J_A]=ell.

Moreover tau is geometric. For j in J and e in {0,1}, the image of
j tau^e in G_k equals the image of j. Thus j tau^e is geometric exactly
when j belongs to W, giving

    J_A intersect D_A=L_w,   L_w intersect D_Y=W.

J and J_A are closed and of finite index (J is the inverse image of a
compact section image, and J_A is its two-coset union), hence open.
Pulling them back to the full arithmetic groups gives T_w -> Y_k and
H_w -> A_k. J_A surjects onto G_k because J does; their geometric
coset actions are transitive. They therefore define geometrically
connected covers. The subgroup intersection J_A intersect P_Y=J,
with index two, is the cartesian double-cover square in Proposition
2.2(iii). This checks its actual arithmetic application, including the
inversion coset; an arbitrary lift of inversion would not suffice.
Definitions 2.3 and 2.5(i) now give the listed local theta types with
these same choices.

**Natural geometric identification.** Choose compatible basepoints
and an embedding of the fixed algebraic closure Fbar into an algebraic
closure Omega of k. The maps on geometric groups induced by scalar
extension are isomorphisms for X_0 and Y by Landesman's cited result:
these are smooth connected separated characteristic-zero curves with
smooth projective elliptic compactifications. For Z and A, compare
Zoonekynd's exact atlas sequences with quotient {±1}; the left map is
the scheme isomorphism and the right map is the identity. The middle
map is therefore an isomorphism. This retains the actual atlas even
at its fixed points. These imports establish the needed comparison
without any appeal to L114's arithmetic-model assertion.

The source forms its finite quotient on the original punctured curve,
then takes the image of the specified rank-one covering subgroup. The
natural isomorphism on that original geometric group preserves closed
iterated commutators and closed power subgroups, and the natural
covering diagram preserves the specified rank-one subgroup. It follows
that it identifies the finite geometric quotient on Y with L107's
Q_Y, and the compatible atlas identifies the quotient on A with Q_A.
No order comparison is substituted for these maps. The same observation
identifies the geometric kernel of the arithmetic quotient with the
intrinsic construction over Omega: the arithmetic quotient kills exactly
the stated subgroup of the geometric kernel, and no arithmetic elements.

These maps preserve the origin inversion, so carry W to L107's M.
They carry tau W to the specified order-two coset in Q_A/M, by its
characterization in Proposition 2.2(iii), and hence L_w to L107's L.
For full geometric groups write f_Y,f_A for the natural isomorphisms,
and q_Y,q_A for L107's quotient maps. The geometric groups of T_w,H_w
inside the local full groups are consequently

    (q_Y f_Y)^(-1)(M),       (q_A f_A)^(-1)(L).

Indeed they are the inverse images of J intersect D_Y=W and
J_A intersect D_A=L_w computed above. These are exactly the full
pullbacks of L107's geometric theta subgroups. Their compatibility with
the atlas follows from L intersect Q_Y=M. The finite-etale correspondence
identifies the geometric covers and square, with the same compatible
basepoint conjugacy. This proves the model identification, not merely
agreement of degrees or abstract finite groups.

**Cusp and verdict.** The fixed nonzero Q in V(K) is unchanged by this
pointwise construction of further covers. It specifies the free pair
{Q,-Q} of rational branches in A's compactification. Step459 identifies
that pair at every designated w with the native index-one sign pair
through the actual graph comparison. The origin O_B used for inversion
is separate from this nonzero pair and is retained throughout. No new
local generator or relabeling has been introduced. Thus the full section,
global cover, designated local type, local theta models and nonzero
native cusp predicates of step461 hold simultaneously.

The limited assembly passes this separate REPRODUCTION audit. This
supersedes step461's pending-review wording and discharges the model
premise retained in L114; the independent group comparison remains a
separate argument. There is no new lemma input or DAG edge. The direct
source imports above avoid a circular L113/L114 dependency. This is local
validation by known constructions, not progress beyond the inspected
sources. Directed (*), complete initial data/(a)–(c)/III/P7, exact
generation/full repair, factor-four excess, actual action/factorization/
pilot, authentication/def=, essentiality and original finite B>=A remain
unresolved. No complete candidate or inherent IUT flaw is demonstrated.

## Mathlib

Full matching coverage is unchecked. No Lean formalization, theorem
name search or claim of absence is made; this is an informal
same-object specialization of the cited results.
