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
asserted. This known-method specialization awaits a separate critical
audit; it is not a candidate demonstration of an essential IUT flaw.

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
This supplies one independent native cusp condition, pending a
separate critical audit. It does not settle initial data/III/P7,
exact generation or full field repair, the relative factor-four
excess, actual input/action/factorization/pilot, inherited source
qualifications or essentiality, or original finite B>=A. No progress
beyond the inspected methods or complete flaw candidate is claimed.

## Mathlib

Full matching coverage is unchecked. No Lean formalization, theorem
name search or claim of absence is made; this is an informal
same-object specialization of the cited results.
