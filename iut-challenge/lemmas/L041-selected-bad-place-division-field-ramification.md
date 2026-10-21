# L041 — Selected bad-place division-field ramification

## Hypotheses

Use **Dupuy–Hilado, arXiv:2004.13228v1 (28 April 2020)**,
sections **2.4.2, 3.2**, **Definition 5.3.1(2),(4),(5)** and
**Definition 5.5.1**, printed pp. 7, 9, 26, 30
([versioned PDF](https://arxiv.org/pdf/2004.13228v1)). Let E/F be the
source's elliptic curve over a number field, F_0=Q(j_E), and assume
F/F_0 is finite Galois. Fix a selected bad place v in S of F_0,
of odd residue characteristic p. Let q_v be its geometric Tate
parameter, determined by j_E as in section 3.2. The parameter has
positive integer order in H_0=F_{0,v}, with the integer uniformizer
normalization of section 2.4.2. Fix the eligible prime ell with

    ell>=5, ell!=p,
    ell does not divide ord_v(q_v),
    ell does not divide [F:F_0].

Retain the source's remaining initial-data conditions; the argument
uses only the conditions explicitly displayed here. Set D=F(E[ell]),
the field of all geometric ell-torsion coordinates, not a field of
one cyclic subgroup. Let w be any selected place of D above v and
u=w restricted to F. Write H=F_u and N=D_w, with their included
local-field tower Q_p subset H_0 subset H subset N. All ord symbols
below are normalized to value 1 on a uniformizer of the indicated
field; e denotes ramification index, not total degree.

Import **Dupuy–Hilado v1, Lemma 5.4.1**, printed pp. 27–28, including
its nonsplit proof case: for an elliptic curve over a finite p-adic
field H with ord_H(j_E)<0, and a prime ell>=3 not dividing that
integer, there are an absolute inertia element sigma and a basis
P_1,P_2 of the full E[ell] such that

    sigma(P_1)=P_1, sigma(P_2)=P_1+P_2.

We use this in the restricted case ell!=p. The inspected proof uses
Tate uniformization after H(sqrt(gamma),zeta_ell), gamma=-c_4/c_6,
of degree dividing 2(ell-1), and returns an element of absolute
inertia over H. This theorem is imported without reproof: no split
reduction over the unchanged H is assumed.

The supporting imports are **J. S. Milne, Algebraic Number Theory,
version 3.08 (19 July 2020)**, **Theorem 7.38, Corollary 7.42, Remark 7.43,
Theorem 7.58(a), Propositions 8.10–8.11**, printed pp. 124,
130–131, 139–140 ([author PDF](https://www.jmilne.org/math/CourseNotes/ANTc.pdf)).
Theorem 7.38 is on p. 123; the completion-generation discussion
opening chapter 8 is on pp. 135–136, before Proposition 8.1.
These give completeness and uniqueness of the extended absolute
value, [N:H]=ef, valuation restriction by e, the unramified
inertia fixed field, and the completion/decomposition-group
identification. Finite p-adic residue fields are perfect, as required
for the inertia statement. For full geometric torsion use **Milne,
Elliptic Curves, second edition (2021), Proposition II.6.3**, printed
pp. 70–71 (characteristic-zero case), and **Theorem III.3.12 and
Proposition III.3.13**, p. 98: over an algebraically closed field of
characteristic zero the full ell-torsion has ell^2 points, and it is
unchanged by algebraically closed field extension. The geometric parameter's integer series
is also recorded in **Milne, Elliptic Curves, second edition (2021),
III.3, pp. 102–103, equations (24)–(26)**
([author PDF](https://www.jmilne.org/math/Books/EC2.pdf#page=107)).
Use Dupuy–Hilado section 3.2 for its general-local-field parameter;
Milne's discussion beginning over Q_p is supporting series evidence,
not our general-local-field torsion theorem.

## Conclusion

The prime ell divides e(N/H), and consequently

    ell divides e(D_w/Q_p).

This is a necessary condition for selected individual bad-place
division-field completions in the specified exposition. It is a
known-theorem specialization (REPRODUCTION), not progress beyond the
checked sources. No exact auxiliary field or tensor component is
tested, and no sufficient admissibility, native-IUT equivalence,
actual input/action, global construction, marked pilot transport,
essentiality or failure of original finite B>=A follows. The separate
2026-10-10 critical audit below validates this unchanged conclusion.

## Proof

### 1. Parameter and valuation normalization

Section 3.2 defines the geometric q by the integer power series in
x=1/j_E. At this bad place ord_(H_0)(j_E)<0, so ord_(H_0)(x)>0.
The inverse series has the form q=x+x^2 b_2+x^3 b_3+..., with all
b_i integers. It converges in H_0: the valuations of its terms
tend to infinity. Thus q belongs to H_0 and q/x lies in
1+x O_(H_0), hence is a unit. Equivalently the cited j-series is
j=q^(-1)(1+744q+196884q^2+...), whose parenthesis is a unit for
ord_(H_0)(q)>0. Both identities give

    ord_(H_0)(j_E)=-ord_(H_0)(q_v)<0.

This is the geometric q determined by j, not the pilot root
q_v^(1/(2ell)). It neither asserts descent of E to F_0 nor uses a
torsion uniformization over F_0.

Let e_0=e(H/H_0). By Milne 8.10, since F/F_0 is Galois, the group
Gal(H/H_0) identifies with the decomposition subgroup at u of
Gal(F/F_0). Therefore [H:H_0] divides [F:F_0]. Milne 7.42 gives
e_0 divides [H:H_0], so ell does not divide e_0. By Remark 7.43,

    ord_H(j_E)=e_0 ord_(H_0)(j_E)
              =-e_0 ord_(H_0)(q_v).

This integer is negative and prime to ell. The degree condition is
used here; prime-to-ell order in F_{0,v} alone would not suffice.
All hypotheses of the imported Lemma 5.4.1 now hold for E/H.

### 2. The completed field is the full local torsion field

Use the embedding D into N supplied by completion at w. Regard all
the geometric ell-torsion points of E as points over D; their images
in N give all geometric ell-torsion points over a local algebraic
closure as well. Indeed the completion map preserves the Weierstrass
equation, the identity and the multiplication-by-ell equation.
Distinct projective points remain distinct under an injective field
map. By Milne EC2 II.6.3 there are ell^2 such points over an algebraic
closure of F, and exactly ell^2 over an algebraic closure of H as well;
hence the embedded points exhaust the latter set. This uses full
geometric torsion, not just one cyclic subgroup; no scheme-theoretic
etaleness claim is needed. Put N'=H(E[ell]) inside N using
these coordinates. This is a finite extension of H. It contains D,
because it contains F and all the generators defining D.

The coordinates are algebraic over F and therefore over H, so N'/H
is finite and is separable in characteristic zero. Fix the common
absolute-value normalization |p|=p^(-1) in N and H for this topology
argument. Its restriction to N' is the unique extension of that on H
by Milne ANT 7.38, and N' is complete for it by the same theorem.
Thus N' is a complete metric subspace of N and is closed. This is
also consistent with the completion-generation description at the
opening of ANT chapter 8; it does not follow from the ef identity alone.
Consequently N' is closed in N. The image of D is dense in N by
the definition of completion, so D subset N' subset N implies
N'=N. This proves the full-field identification, rather than only
containment of a particular torsion point or subgroup.

The full torsion set is stable under G_H. The coordinate field N'
is therefore normal over H; it is separable in characteristic zero.
Hence N/H is finite Galois. Its faithful action on E[ell] identifies
Gal(N/H) with the image of the torsion representation rho: an
automorphism fixing every torsion point fixes all field generators,
and conversely fixing all coordinates fixes those points.

### 3. Finite inertia and ramification

Apply the imported transvection theorem to obtain sigma in the
absolute inertia of H. Its image tau in Gal(N/H) acts on the full
torsion basis by P_1 -> P_1 and P_2 -> P_2+P_1. Induction gives
tau^k(P_1)=P_1 and tau^k(P_2)=P_2+kP_1 for every integer k>=0.
Because P_1 has exact order ell, this action is the identity exactly
when ell divides k. Faithfulness of the full-torsion action shows
that tau itself has exact order ell, not merely a multiple thereof.

Absolute inertia acts trivially on the residue algebraic closure;
its restriction to N therefore acts trivially on the residue field
of N. Thus tau belongs to the finite inertia subgroup I(N/H).
No surjectivity assertion about the restriction of absolute inertia
is needed for this inclusion. By Milne 7.58(a), the fixed field
N^I is the maximal unramified subextension, whose degree over H is
the residue degree f(N/H). Together with Milne 7.42 and finite
Galois theory this gives

    |I(N/H)|=[N:N^I]=[N:H]/f(N/H)=e(N/H).

Lagrange's theorem applied to the order-ell subgroup generated by
tau proves ell divides e(N/H).

Finally valuation restriction in the tower N/H/Q_p is
ord_N|H=e(N/H) ord_H and ord_H|Q_p=e(H/Q_p) ord_(Q_p).
Their composite gives e(N/Q_p)=e(N/H)e(H/Q_p), so ell divides
e(N/Q_p). The absolute extension N/Q_p need not be Galois;
Galois inertia was used only over H. This proves the stated result.

### Scope checks

The imported nonsplit case supplies inertia over H without asserting
q_v^(1/ell) lies in N in unchanged nonsplit coordinates. Full
division-field generation is essential to the faithful transvection
argument. Neither residue reduction of a primitive root nor rational
30-torsion is a premise here. L039/L040 are prior-stop comparisons,
not inputs. The necessary ramification conclusion constructs no
initial theta data and gives no numerical comparison of A and B.

### Separate critical audit — 2026-10-10

The audit checks the displayed hypotheses against the imported
statements, without using this lemma's conclusion or any earlier
local lemma as a premise.

For normalization, the integer inverse j-series is convergent because
ord_(H_0)(1/j_E)>0 and its coefficients have nonnegative valuation.
After dividing by its leading term, every remaining term lies in the
maximal ideal. Thus no cancellation can change its leading valuation.
The q being measured is the geometric parameter in H_0, not a pilot
root or a parameter normalized in N. Galoisness of F/F_0 supplies
divisibility of the local degree through the decomposition subgroup;
the mere bound [H:H_0]<=[F:F_0] would not suffice. Both factors in
e_0 ord_(H_0)(q_v) are prime to ell. The imported local theorem's
negative-j and prime-to-ell hypotheses therefore hold over H.

For field identification, choose an algebraic closure containing the
finite extension N/H. All global torsion points are defined over D,
and both characteristic-zero point counts are ell^2. Injectivity and
the group equations show that the embedded set is the entire local
torsion set. The finite complete subfield N' contains F and every
generator of D, while D is dense in N; its closedness forces equality.
No density of F in N, identification of algebraic closures, or
commutation of an infinite coordinate construction with completion is
assumed. Stability of the finite full torsion set under every H-embedding
proves normality, and characteristic zero proves separability. The
action is faithful because the torsion coordinates generate the field.
ANT 7.38 and EC2 II.6.3 above repair the original imprecise completeness
citation and uncited torsion-count wording; they change no hypothesis
or conclusion.

For nonsplit reduction, the cited Lemma 5.4.1 covers negative j and
returns an absolute inertia element over H after its splitting-field
argument. Its inspected proof allows a ramified quadratic twist; no
unramified-splitting assumption or untwisted Tate coordinates over H
are added here. The degree dividing 2(ell-1) is prime to ell, and
our ell>=5, ell!=p assumptions lie inside the imported scope. This
audit imports that theorem, rather than re-proving Tate uniformization
or asserting that a particular radical is already in N.

For inertia, the nonzero basis vector P_1 has exact order ell.
The displayed transvection therefore has exact order ell in the
torsion image; faithfulness transfers this exact order to Gal(N/H).
The restriction of absolute inertia fixes the residue field of N,
so this element lies in I(N/H) without a surjectivity assumption.
The residue extension is finite and separable, so ANT 7.58(a) and
7.42 identify |I| with e, rather than with [N:H]. Lagrange then gives
the asserted divisibility over H. Composing normalized valuation
restrictions proves tower multiplicativity even if N/Q_p is not
normal. Thus the audit passes for exactly the stated necessary screen.

No exact field, tensor component, or sufficient local or global
realization is certified. The earlier realization stops remain valid,
and the original numerical and essentiality gaps remain independent.

## Mathlib

Full matching and supporting Mathlib coverage is not checked.
The precise external theorem imports and their applicability argument
are the informal inputs; no formal verification is claimed.
