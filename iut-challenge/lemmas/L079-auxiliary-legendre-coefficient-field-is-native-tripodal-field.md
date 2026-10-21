# L079 — The auxiliary Legendre coefficient field is the native tripodal field

## Hypotheses

Fix L078's auxiliary curve and choices, inside its fixed algebraic
closure Q-bar of Q in Omega. Thus E=E_aux/Q has the nonsingular
monic equation y^2=g_aux(x), with distinct roots r_1,r_2,r_3.
Keep the chosen ordering (i,j,k), cross-residue difference
D=r_j-r_i, root s^2=D, and

    t=(r_k-r_i)/D, T_0=Q(t),
    E_L: V^2=X(X-1)(X-t),
    G=T_0(iota,E_L[15]).

All fields and division coordinates use this embedding. As in
L074, j(E) is rational and has v_3(j(E))=-30. Use the native
field-of-moduli and tripodal-field definitions in IUT I Definition
3.1(a),(b) and IUT IV Theorem 1.10, with the source-version
qualifications recorded below. Apply these definitions to the
geometric once-punctured curve X=(E_L minus its origin)_Q-bar.
This does not assume a full collection of initial theta-data on G.

## Conclusion

For this geometric curve the native fields are, as actual subfields
of the fixed Q-bar,

    F_mod=Q,
    F_tpd=Q(E[2])=Q(r_1,r_2,r_3)=Q(t)=T_0.

In particular L078's displayed E_L is a literal Legendre descent
over this F_tpd and its field G has the prescription
G=F_tpd(iota,E_L[15]). The induced completions proved in L078
remain those of the same G and G(E_L[7]). No assertion G=F',
G=F_aux or G=the retained F is made. The degree of T_0/Q and
the size of the mod-two image are not specified.

This is a specialization of assessed known results, validated by the
separate step312 critical audit below. It gives neither sufficient initial
theta-data nor an essential IUT flaw or the original finite B>=A.

## Proof

### Imported results and why specialization is needed

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-auxiliary-legendre-native-two-torsion-field.md`.
The general results below are imported, not reproved. The work here
checks the geometric object and the two embedded stabilizers for
this particular auxiliary curve.

IUT I, Definition 3.1(a),(b), printed pp.61–62, uses the moduli of
the once-punctured elliptic curve and its elliptic completion.
The inspected [May 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf)
is reused; byte identity with the author endpoint is unverified.
In [IUT IV, April 2020 author text](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf),
Proposition 1.8(ii),(iii), printed pp.18–19, proofs p.20,
identifies the minimal moduli field over a perfect field through j
and makes the two-torsion action independent of descent when the
pointed geometric automorphisms are {+1,-1}. Theorem 1.10, p.22,
defines F_tpd by the full two-torsion field of an F_mod-model.
Only these definitions and elementary inputs are used, not its
log-volume estimate. Theorem 1.10 and Corollary 2.2, pp.41–42,
record the separate Legendre prescription.

Import [Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
I Proposition 4.18 and Remark 4.19, p.38: an isomorphism of
nonempty opens of nonsingular projective geometrically irreducible
curves over a perfect field extends uniquely to the completions.
Import the nonexceptional-j pointed automorphism classification
already used in L074: [Sutherland, Lecture 21 (6 May 2024),
section 21.2, p.2](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf).
In characteristic zero, j!=0,1728 implies Aut(E,O)={+1,-1}.

Import [Antieau–Meier, arXiv:1608.00851v3 (5 May 2020)](https://arxiv.org/pdf/1608.00851v3),
Definition 4.1, Proposition 4.5 and Corollary 4.6, printed
pp.13–15, including their proofs. Over Z[1/2], a full level-two
structure is an ordering of the three nonzero two-torsion points.
Its coarse coordinate on y^2=product(x-e_m) is
(e_3-e_1)/(e_2-e_1). Over an algebraically closed field, equality
of that coordinate is equivalent to an isomorphism respecting the
ordered points. This follows from the stated equivalence with
B C_2 over the parameter scheme. The following paragraph makes
the coarse permutation action equivariant but warns that the
Legendre section itself need not be equivariant. Rational twists
are therefore retained below.

Use the standard fundamental theorem of infinite Galois theory:
closed subgroups of Gal(Q-bar/Q) are determined by their embedded
fixed fields. The two-torsion kernel and the stabilizer of t in its
finite Galois orbit are open and closed. The latter is not assumed
normal before the comparison; closedness suffices for fixed fields.

### Same geometric object and its native moduli field

L078 retains the pointed geometric isomorphism with formulas

    (x,y) -> ((x-r_i)/D, y/(Ds)),
    (X,V) -> (r_i+DX, Ds V).

Here s is algebraic over Q since s^2=D, and D,s are nonzero.
Consequently this is an isomorphism over Q-bar of this very E
with this very E_L, preserving the unique origin. It identifies
their once-punctured curves as well.

The curves are smooth projective geometrically irreducible curves
over the perfect field Q-bar: both cubics are separable of degree
three and the origins are their smooth points at infinity.
Every geometric isomorphism of the punctured curves extends by
Milne's cited result. Its extension must preserve the omitted point:
the bijection already sends the two open complements onto one
another, and each remaining complement consists of one point.
Conversely a pointed isomorphism restricts to the punctured opens.
Thus the native punctured moduli object is exactly the pointed
elliptic moduli object here, without an added level marking.

In particular E/Q is an actual Q-model of this geometric object.
Its j lies in Q, so the native j-field description gives
F_mod=Q. This is the field of moduli of the same auxiliary
geometric curve; it is not inferred by equating local completions.
By L074, v_3(j)=-30 excludes j=0 and also j=1728, since
v_3(1728)=3. The cited automorphism classification therefore
gives Aut_Q-bar(E,O)={+1,-1}. IUT IV 1.8(iii) applies and
permits computing the native two-torsion action using the actual
Q-descent E, regardless of the twist used for E_L. Its kernel
fixes the complete E[2], whose nonzero points are precisely
P_m=(r_m,0). The origin adds no field generator. Hence the
native definition yields

    F_tpd=Q(E[2])=Q(r_1,r_2,r_3).

### Both inclusions of the actual stabilizers

Write Gamma=Gal(Q-bar/Q), let rho_2 be its action on E[2],
and set K_2=ker(rho_2). Since E is Q-defined, sigma in Gamma
permutes the three P_m. It acts on their roots and on t in
the fixed embedding.

First, sigma in K_2 fixes all r_m and therefore fixes
(r_k-r_i)/(r_j-r_i)=t. Thus

    K_2 subset Gal(Q-bar/Q(t)).

Conversely suppose sigma(t)=t. Consider the two objects over Q-bar

    (E; P_i,P_j,P_k),
    (E; sigma(P_i),sigma(P_j),sigma(P_k)).

They are both objects of M(2): their points are distinct nonzero
two-torsion, and any ordering of these points is a full level-two
structure. Their coarse parameters under the cited coordinate map
are t and

    (sigma(r_k)-sigma(r_i))/(sigma(r_j)-sigma(r_i))=sigma(t)=t.

All denominators are nonzero and characteristic is zero. The
algebraically closed field case of Antieau–Meier 4.5–4.6 therefore
supplies an isomorphism of these ordered objects. Since the
underlying Q-defined curve in both is E, this is a pointed
geometric automorphism a of E satisfying

    a(P_i)=sigma(P_i), a(P_j)=sigma(P_j), a(P_k)=sigma(P_k).

The only possibilities are a=+1 and a=-1, and each fixes every
point of E[2], since -P=P for two-torsion. Hence sigma fixes
all three P_m and also the origin. Thus sigma lies in K_2.
This proves the reverse inclusion and gives the exact equality

    Gal(Q-bar/Q(t))=K_2=Gal(Q-bar/Q(r_1,r_2,r_3)).

Taking fixed fields gives equality as subfields of our fixed Q-bar,
not just an abstract field isomorphism. Combining it with the
native computation above proves T_0=Q(t)=F_tpd. No assertion
about how many permutations are realized by Gamma was needed.

### Consequence and limitations

L078 already gives t!=0,1 and the displayed nonsingular Legendre
equation over T_0. Substituting the proved T_0=F_tpd into that
same equation and into G's definition gives the conclusion about
the model and its field prescription. Its fields, generators,
places and local isomorphism are unchanged, so L078's embedded
completion equalities still apply. No new torsion or completion
argument is being inferred from the moduli theorem.

The geometric isomorphism used above need not descend to T_0,
and no claim that the original E_aux and E_L are T_0-isomorphic
is required. The ordered coarse comparison takes place only over
Q-bar; it does not discard a rational quadratic twist or assert
equivariance of the Legendre section. Nonexceptional automorphisms
are essential for the stabilizer converse.

This establishes the approved intermediate field identification,
not a new general theorem beyond the checked sources. It neither
transfers the retained E_0's global hypotheses to G nor proves
other native initial-data conditions. Retained radical memberships
and scalar occurrence, marked all-image factorization, pilot
transport, essentiality and original finite B>=A remain unresolved.
The retained and auxiliary curves, global fields and geometric
parameters remain distinct; in particular no q_aux=q_0 or
q_aux=3^30 is asserted. ATTEMPTS/027,028,031,032,033 remain
preserved and are not reopened. The construction preceded the
separately approved critical audit recorded below.

### Separate critical audit — 2026-10-18, step 312

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-auxiliary-native-tripodal-field-critical-audit.md`
covers exactly this audit. The complete proof above, L074's
same-witness invariant and coordinate checks, and L078's proof and
step307 audit have been checked against the cited sources. Reopened
IUT IV 1.8(ii),(iii), their proof and 1.10's definition; Antieau–Meier
4.5 and its complete proof, 4.6 and its proof and equivariance
warning; and IUT I 3.1(a),(b) in the qualified reproduction. Reuse
the recorded Milne and Sutherland coverage. No new general theorem
is needed. Both field identities pass, with the following explicit
applicability checks.

**The actual geometric object.** L074 gives a separable monic
cubic over Q and rational j with v_3(j)=-30 for this E_aux itself.
L078 keeps that curve and the chosen ordering, with D nonzero,
t different from 0,1 and s^2=D. The displayed inverse maps are
defined over the same Q-bar and preserve the origins, so they
identify precisely the geometric curve used in the hypotheses.
Both completions are nonsingular projective geometrically
irreducible curves over a perfect field, as required by Milne
I.4.18/4.19. Apply the extension theorem also to the inverse
punctured isomorphism. Uniqueness makes the extensions inverse;
their bijection of the open complements then forces their unique
omitted points to correspond. This checks pointedness, not just
birational equivalence. The native moduli object has no ordered
two-torsion marking: that marking enters only the later stabilizer
test. Thus the Q-model and IUT IV 1.8(ii) compute F_mod=Q for
the object specified in IUT I 3.1(b).

**Descent independence in this embedding.** The finite valuation
-30 excludes j=0 and differs from v_3(1728)=3. Characteristic zero
and the cited automorphism classification give exactly the two
pointed signs. IUT IV 1.8(iii) therefore applies over the perfect
base Q: its two-torsion representation factors through the group
of base automorphisms. The actual Q-model supplies a section of
1.8(ii); pulling back along this section is the usual action on
E_aux[2]. Changing the geometric identification with E_L changes
it only by a pointed sign, which acts trivially on two-torsion.
Consequently the kernel, as a subgroup of the same G_Q, is the
one fixing all (r_m,0). Theorem 1.10's field definition can be
evaluated using this model. Its separate initial-data and reduction
assumptions for the estimate are not supplied by this computation.

**Both stabilizer inclusions.** A member of ker(rho_2) fixes each
root and hence t, proving the first inclusion. For the converse,
sigma(t)=t compares two ordered objects over Q-bar, both with
underlying pointed curve E_aux because its coefficients lie in Q.
Their three nonzero two-torsion points are distinct, so each
ordering is a full level-two structure. The base is algebraically
closed with 2 invertible; their parameters avoid 0 and 1 and equal
t by the displayed formula. Antieau–Meier 4.5–4.6 therefore give
an isomorphism respecting that order. In the presentation by B C_2,
over this algebraically closed field the torsors are trivial, so
the comparison is an actual geometric isomorphism, not merely
equality of field-valued coarse points over a nonclosed field.
It is an automorphism of E_aux, hence a sign. Both signs fix all
E_aux[2], forcing sigma(P_m)=P_m for all three m. This proves
the reverse inclusion for the full subgroup fixing t, without
assuming which permutations G_Q realizes.

**Fixed fields and the prescription.** Each group is closed:
rho_2 has finite continuous image and t is algebraic with finite
orbit. The original description of both groups as kernels has
been clarified above; no normality of the t-stabilizer is needed
or used before their equality. Infinite Galois correspondence
now gives Q(t)=Q(r_1,r_2,r_3) inside the specified closure.
Together with the native kernel calculation this is the asserted
F_tpd, not an abstract isomorphic copy. L078's same equation is
defined over this field, and substitution in its literal definition
of G proves the field prescription. Its generators and induced
places have not changed, so its two audited completion equalities
remain applicable.

**Verdict and boundary.** The audit validates L079's conclusions
for every allowed cross-residue choice and either sign of s. It
uses only geometric ordered comparison, never rational equivariance
of the Legendre section or a T_0-defined comparison with E_aux.
No full mod-two image, degree-six claim, G=F', or Galoisness of
G/Q follows from the argument. In particular native initial-data
admissibility remains a separate obligation even though the field
prescription matches. The direct mathematical inputs remain L074
and L078. No main-argument or DAG change is needed; this canonical
audit supersedes the overview's pending-audit wording. This is
verification of a known-method specialization, not progress beyond
the checked sources or a resolution of the original finite B>=A gap.

## Mathlib

Full matching and supporting Mathlib coverage for this native
field/moduli specialization is **not checked**. No absence or
formal-verification claim is made.
