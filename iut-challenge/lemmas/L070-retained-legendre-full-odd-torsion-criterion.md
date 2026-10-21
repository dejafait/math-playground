# L070 — Conditional retained Legendre full-15-torsion criterion

## Hypotheses

Retain the same curve E_0/Q, embedded algebraic closure Q-bar inside
Omega, and F=Q(zeta_60,E_0[30]) from L045 and L048, with the same
precision M>=max(M_tors,31). Torsion fields use both coordinates of
every geometric point. In particular E_0[30] is F-rational and
v_3(j(E_0))=-30 in the retained embedding.

Conditionally assume that the native T=F_tpd is an embedded subfield
of this F. Specify a Legendre descent

E_L/T: y^2=x(x-1)(x-lambda), lambda in T minus {0,1},

together with its geometric pointed isomorphism class: it is
origin-preserving isomorphic to E_0 over Q-bar. No rational
isomorphism, rational odd torsion on E_L, or identification of T
with a concrete division field is assumed. This hypothesis does not
construct the native T or its specified descent.

Write G_T=Gal(Q-bar/T) and G_F=Gal(Q-bar/F), with G_F subset G_T.

## Conclusion

The geometric comparison determines a quadratic character
chi:G_T -> {+1,-1} and a class d in T^times/(T^times)^2,
with chi(sigma)=sigma(sqrt(d))/sqrt(d). For a basis transported by
a geometric pointed isomorphism phi:E_0 -> E_L, the full
15-torsion representations satisfy

rho_(E_L,15)(sigma)=chi(sigma) rho_(E_0,15)(sigma) for sigma in G_T.

Consequently, on the entire subgroup G_F,

rho_(E_L,15)(sigma)=chi(sigma) Id,
ker(rho_(E_L,15)|G_F)=G_F intersect ker(chi).

The following conditions are equivalent:

1. Every geometric point of E_L[15] is F-rational.
2. chi|G_F is trivial.
3. A square root of d lies in F, equivalently d is a square in F.

These are also equivalent to E_L and E_0 being pointed isomorphic
over F, by the cited twist classification over F. The actual d and
its restriction to G_F have not been identified. Thus this gives
no passing or failing verdict for the unspecified native model,
and no equality F=T(sqrt(-1),E_L[15]). It is a conditional known-result
specialization validated by the separate step275 critical audit below,
not an IUT flaw.

## Proof

### Imported results and why this specialization is needed

Use the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-legendre-odd-torsion-compatibility.md`.
[Sutherland, MIT 18.786, Lecture 21, 6 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
section 21.2, p.2, classifies twists for j!=0,1728 by continuous
quadratic characters, with geometric pointed automorphisms {+1,-1}.
In characteristic other than 2,3 these are the ordinary quadratic
twists of a short Weierstrass equation. Import the classification;
no reproof or originality claim is needed.

[Gonzalez-Jimenez, Lozano-Robledo and York,
arXiv:2408.04159v1, 8 August 2024](https://arxiv.org/pdf/2408.04159v1),
Lemma 3.4, proof p.12, gives the displayed twist representation
formula in transported bases for a nonsingular short Weierstrass
curve over a number field, nonzero quadratic parameter and n>2.
Only that formula is imported, not part (2)'s stronger general
division-field equality. [Yvon, arXiv:2407.14370v1,
19 July 2024](https://arxiv.org/pdf/2407.14370v1), Introduction p.2,
uses the full-coordinate convention
ker(rho_(E,n))=Gal(k-bar/k(E[n])).
[Sutherland, Lecture 20, 1 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf),
section 20.1, pp.1-2, supplies the full representations and the
closed-subgroup Galois correspondence. The extra work here is
checking the retained hypotheses and restricting the exact formula
to G_F, rather than invoking a general division-field comparison.

For context only, [IUT IV](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf),
Proposition 1.8(iv), within pp.18-21, requires full rational odd torsion
on both descents before its rational-isomorphism conclusion.
Theorem 1.10, p.22, and Corollary 2.2, pp.41-42, use the specified
Legendre descent in their field prescription, as recorded in
foundations/05 step272 (retained April 2020 version convention;
author/reproduction byte identity unverified). Those source
hypotheses are not conclusions of the present lemma.

### Common field, geometric comparison and nonexceptional j

Since Q subset T subset F and F is a number field, T is a number
field of characteristic zero. Thus E_0 base-changes from Q to T,
and the specified E_L is a nonsingular elliptic curve over the same
field: lambda!=0,1 makes the three cubic roots distinct. Its origin
is the point at infinity. The assumed geometric pointed isomorphism
is independent of any assertion about rational torsion on E_L.

L048 gives the finite value v_3(j(E_0))=-30, so j(E_0)!=0.
Also v_3(1728)=v_3(2^6*3^3)=3, so j(E_0)!=1728. Geometric
isomorphism preserves j, giving the same exclusions for E_L.
These are equalities of algebraic numbers tested in the fixed
injective embedding; no field-of-moduli identification is involved.

Both curves admit nonsingular short Weierstrass equations over T:
their given equations have the form y^2=x^3+c x^2+a x+b,
and x=X-c/3 removes the quadratic term. This is a pointed
T-coordinate change, permitted since char(T)=0. For E_L,
c=-(1+lambda). No integrality over a local ring is asserted or
required by the imported twist formula. Thus its number-field,
short-equation and characteristic hypotheses hold, with n=15>2.

### The transported representation and its full restricted kernel

Choose a geometric pointed isomorphism phi:E_0 -> E_L. The
classification identifies the automorphism
phi^(-1) sigma(phi) of E_0 with multiplication by chi(sigma).
These automorphisms are {+1,-1}, defined over T, and the
classification supplies a continuous character and a nonzero
representative d in T for its quadratic class. Changing phi
multiplies it by a geometric pointed automorphism of E_0, hence
by a T-defined sign; this does not change chi. Changing sqrt(d)
to its negative likewise does not change the character.

Transport a Z/15Z-basis P_1,P_2 of E_0[15] by phi. Such a basis
exists for geometric torsion in characteristic zero, using the
torsion theorem already cited in L045. For every sigma in G_T,
the known coordinate formula, or its expression on the same points,
reads

sigma(phi(P_i))=sigma(phi)(sigma(P_i))
              =phi([chi(sigma)] sigma(P_i)).

It gives exactly rho_(E_L,15)=chi rho_(E_0,15) in these bases;
the scalar sign commutes with the matrix regardless of the basis
convention. This is the cited formula applied to these curves,
not a new general twisting theorem.

Every geometric 15-torsion point of E_0 belongs to E_0[30]. L045
therefore makes rho_(E_0,15)(sigma)=Id for every sigma in G_F.
The displayed formula now gives rho_(E_L,15)(sigma)=chi(sigma)Id.
On the free module (Z/15Z)^2, -Id!=Id, since -1!=1 modulo 15.
Hence this last matrix is Id if and only if chi(sigma)=+1.
This proves equality of the complete restricted kernels, not just
of abstract image groups or of the action on x-coordinates.

With the full-point convention, all E_L[15] is F-rational exactly
when this kernel is all of G_F. The kernel identity proves (1)
equivalent to (2). The formula for chi shows that (2) holds exactly
when every sigma in G_F fixes sqrt(d). The fixed field of G_F in
Q-bar is F by the cited Galois correspondence, proving equivalence
with (3). The same twist classification applied over F identifies
the trivial restricted class with a pointed F-isomorphism. This
last implication is a consequence, not an input used to assume (1).

### Scope, continuation test and known traps

The proof establishes the conditional test without determining its
value for the native descent: neither a concrete lambda nor its
comparison class d has been identified in the retained setup.
Triviality cannot be inferred from full torsion on E_0 alone.
If the actual chi|G_F is proved trivial, this compatibility test
passes and a later exact-generation comparison becomes permissible.
A proved nontrivial restriction stops this specified model over
the unchanged F; an unidentified restriction leaves it conditional.
Neither branch permits silently adjoining sqrt(d) or reselecting E_0.

Even a pass gives only rationality and an F-isomorphism. It does
not prove minimal generation over T(sqrt(-1)), the native identity
of T, sufficient initial data, source-marked all-image factorization,
essentiality or finite B>=A. In particular no general division-field
equality excluded in foundations/05 step272 is used. The full kernel
is checked after restriction, where the original representation is
known to be trivial. Local completions, x-only fields, equality of
degrees and one Galois element would not substitute for this check.
ATTEMPTS/027,028,031,032 and the existing local constructions are
unaffected. There is no counterexample to IUT here and no complete
candidate solution. The separate critical audit below validates exactly
this conditional scope.

### Separate critical audit — 2026-10-17, step 275

**Verdict and inputs.** The stated conditional criterion passes the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-legendre-odd-torsion-critical-audit.md`.
This audit reuses its inspected cases of Lecture 21 section 21.2,
the transported-basis calculation in Lemma 3.4's proof, and the full
pointwise-kernel and Galois-correspondence inputs cited above. No
stronger division-field clause is imported. L045 supplies rational
30-torsion for the same curve whose j-valuation is computed in L048;
no additional direct lemma input is needed.

**Hypotheses and absence of circularity.** An intermediate field
Q subset T subset F is a finite extension of Q. Both equations are
therefore over a common number field of characteristic zero. The
three roots 0,1,lambda are distinct, so the Legendre equation is
nonsingular with its specified origin. The hypothesis supplies a
geometric pointed isomorphism, not an isomorphism over T or F.
L048's finite valuation -30 excludes j=0, and differs from
v_3(1728)=3. Thus Lecture 21's nonexceptional-j classification
applies to both curves, with geometric pointed automorphism group
exactly {Id,[-1]}. Both automorphisms are T-defined. The short
Weierstrass translations in the proof are over T and do not require
local integrality. The audit uses no rationality of E_L[15] to
obtain phi or to identify this automorphism group. In particular,
IUT IV Proposition 1.8(iv)'s two-model rationality hypothesis is
not used to produce the comparison needed to test that hypothesis.

**Cocycle and basis convention.** Put c_sigma=phi^(-1) sigma(phi),
an automorphism of E_0. For sigma,tau in G_T, direct composition
gives

c_(sigma tau)=c_sigma sigma(c_tau).

Since each c_tau is a T-defined sign, this is c_sigma c_tau.
Thus the cocycle supplied by the classification is a character
with the convention used in the statement. It is continuous:
phi is defined over a finite extension of T, and a finite normal
extension containing its coefficients has an open fixing subgroup.
Replacing phi by phi a, where a is a geometric pointed
automorphism of E_0, replaces c_sigma by a^(-1)c_sigma sigma(a).
Here sigma(a)=a and both factors are signs, so the character is
unchanged. The classification supplies its square class d, also
when the character is trivial; in that case d can be represented
by 1. The word quadratic includes this trivial character.

Use column matrices in a geometric Z/15Z-basis (P_1,P_2), and
let Q_i=phi(P_i). If
sigma(P_j)=sum_i a_ij P_i, then, from sigma(phi)=phi c_sigma,

sigma(Q_j)=sum_i chi(sigma) a_ij Q_i.

This checks the displayed formula for every sigma, with exactly
the claimed direction of phi and the same transported basis.
An inverse-character convention would give the same sign, but
no such convention change is needed. This is an explicit check of
the already inspected formula's application, not a reproof of
the twist-classification theorem.

**All character cases and the source boundary.** The source proof
places its coordinate calculation after a hypothesis excluding
the quadratic radical from the original division field. That
exclusion is not needed in the preceding pointwise identity:
sigma(phi)=phi c_sigma holds for every sigma whether or not
any particular radical is already rational. The audit therefore
checks the application in all three exhaustive cases:

1. If chi is trivial on G_T, the matrix formula is the untwisted
   formula on G_T and remains so on G_F.
2. If chi is nontrivial on G_T but trivial on G_F, the same
   formula holds and restricts to the identity on G_F.
3. If chi is nontrivial on G_F, it has a value -1 there and the
   restricted matrix at every such element is -Id.

There is no assumption in cases 1 or 2 that an element of case 3
exists. No conclusion from part (2)'s stronger source field claim
is used in any case.

**Complete kernel and descent conclusion.** L045 gives
[30]P=0 and P in E_0(F) for every geometric 30-torsion point.
For P in E_0[15], 30P=2(15P)=0, hence every such P is
F-rational. Therefore rho_(E_0,15)(sigma)=Id for every sigma in
G_F, without any assertion about the representation on G_T.
The calculation above gives rho_(E_L,15)(sigma)=chi(sigma)Id
on the whole G_F. The free rank-two module has an element of
exact order 15; multiplication by -1 does not fix that element,
since 2P=0 would contradict its order. Thus the kernel is exactly
G_F intersect ker(chi), including the trivial-character cases.
This is a full-point check; x-coordinates alone would not detect
the sign.

By the full-coordinate convention, every 15-torsion point is
F-rational precisely when this entire restricted kernel is G_F.
For any representative d in T^times, the character formula says
this is equivalent to every sigma in G_F fixing sqrt(d). The
fixed field of G_F inside the same Q-bar is F, so this is exactly
sqrt(d) in F. Replacing d by d t^2 for t in T^times does not
change that condition, since t is already in F. Finally Lecture
21's classification over F identifies this trivial restricted
twist with an origin-preserving F-isomorphism. Conversely any
such isomorphism represents the trivial class, so the asserted
additional equivalence holds in both directions.

**Limits of the pass.** This audit finds no defective hypothesis
or inference in the conditional statement. It establishes no
value of chi for the actual native descent. Even if that value
is later proved trivial, rationality over F supplies no reverse
generation assertion over T(sqrt(-1)). Native T, its specified
model and exact generation are still unverified. The stronger
general source field equality is neither assumed nor adjudicated.
ATTEMPTS/027,028,031,032 remain unchanged. This is validation of
a known-method specialization, not progress beyond the checked
sources, a sufficient initial-data construction, or an essential
IUT flaw. The original finite B>=A gap remains open. No numerical
certificate or mathematical script is needed for this audit.

## Mathlib

Full matching and supporting Mathlib coverage for this conditional
twist-character specialization has not been checked. No absence
or formal-verification claim is made. This is reproduction of the
inspected classification, twist formula and full-kernel convention,
with their hypotheses checked for the retained conditional setup.
