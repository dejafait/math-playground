# L035 — Actual-line projected container is not preserved

## Hypotheses

Let L=Q_3(zeta_20,pi), where zeta_20 has order 20 and pi^27=3.
Put O=O_L, J=log(O^times), V=ker(Tr_(L/Q_3)), C=O intersect V
and M=J intersect V. Use precisely L033's admitted presentation and
reciprocity-defined finite-word reference subgroup Gamma, with its actual
primitive fixed y_1. L033 supplies

    M=F direct-sum E,   F=Z_3 y_1,
    E=direct-sum_(j=3)^108 Z_3 y_j,

and residual irreducibility on (M/F)/3(M/F). Gamma preserves M and V
and fixes F pointwise. Its generators are exactly L033's u_i,v_i,w_i
and their inverses, not a larger group. The underlying source actions
are those in **Kaiji Kondo, Anabelian aspects of the outer automorphism
groups of the absolute Galois groups of mixed-characteristic local
fields**, **arXiv:2512.09231v2, 12 December 2025, section 1,
Theorem 1.3 and its even-degree proof**, printed pp. 9–11
([versioned primary text](https://arxiv.org/html/2512.09231v2#S1)).
The integral reference transport is already established in L033's
inherited hypotheses; no new source action is introduced here.

Use audited L034's complete full lattices C,M in V and its exclusion
of q_W(C)=a q_W(M) for every rational line W in V and every
a in Q_3^times. Set

    W=Q_3 y_1,   H=V/W,   q:V->H,
    P=q(M),      N=q(C).

The scalar field of all lattice arguments is Q_3, with valuation ring
Z_3. No field coordinates of y_1, O_U-linearity, exponent twist,
separate x_2 shear or descended field valuation is assumed.

Import the full quotient-lattice result from **Peter Bürgisser,
Avinash Kulkarni and Antonio Lerario, Nonarchimedean integral geometry**,
Selecta Mathematica **32:10 (2026)**, version of record 5 January 2026,
**section 2.2**, pp. 13–14, **Lemmas 3.1.4(1–3)/3.1.5**, pp. 21–23
([primary publication](https://doi.org/10.1007/s00029-025-01120-y),
[primary PDF](https://d-nb.info/1395945926/34)). It applies to full
Q_3-lattices and their images in rational quotients; neither nesting
nor a field norm on H is required.

The stable-lattice criterion is known: **Arijit Sehanobish, Universal
Deformations and p-adic L-functions**, University of Maryland PhD
dissertation **(2019), section 3.1, printed pp. 26–28,
Corollary 3.1.9**
([primary dissertation](https://api.drum.lib.umd.edu/server/api/core/bitstreams/9c358dab-b72f-47fa-924c-da55d0ae1ea6/content)).
Its inspected sketch's last abstract-isomorphism sentence does not
establish the same-space scalar equality needed here in rank 106.
We therefore reproduce the normalized-inclusion argument, as justified
by the approved assessment, using **Nakayama's lemma, Stacks Project,
Lemma 10.20.1, tag 00DV, (2)/(4)**
([statement and proof](https://stacks.math.columbia.edu/tag/00DV)).
This retains the citation's proof qualification and checks the finite
generation and local-ring hypotheses explicitly. No fresh source
inspection or new general stable-lattice theorem is claimed.

## Conclusion

For every admitted presentation in the hypotheses, the induced Gamma
action on H does **not** preserve N=q(C): it is false that h(N)=N
for all finite words h in Gamma. In particular some finite word h
and some c in C satisfy

    q(h(c)) not in q(C),   equivalently h(c) not in C+W.

The integral projected logarithm lattice is exactly

    P=q(M) isomorphic to M/(Z_3 y_1),

and both P,N are full closed Z_3-lattices of rank 106 in the same H.

This is a **REPRODUCTION** of the known stable-lattice method applied to
the audited local inputs. It is a qualitative local container result,
not a new result beyond the checked methods or a candidate IUT flaw.
It identifies no escaping word or field-coordinate input and computes
no numerical radius. Fixed-line control, actual/native input and action
compatibility, packet/global realization, pilot transport, essentiality
and the original finite B>=A comparison remain unresolved.

## Proof

### Actual line, full lattices and induced action

The integral direct sum in L033 remains a direct sum after extending
scalars to Q_3. If m in M lies in W, write it uniquely as
m=b y_1+e with b in Z_3 and e in E. The rational direct sum forces
e=0, so M intersect W=F. The restriction q|M therefore has kernel
exactly F and image P, identifying P with M/F, not a quotient by a
larger unsaturated submodule. In particular P is free of rank 106,
and its reduction is exactly the residual module in L033.

L034's C and M are full lattices in the 107-dimensional V. The cited
quotient-lattice theorem applies to the one-dimensional rational W:
N and P are full rank-106 lattices in H. Their closedness can also
be checked directly for this application. C and M are compact as
continuous images of Z_3^107 under their basis maps. W is a closed
linear subspace of the finite-dimensional Q_3-space V, so H is
Hausdorff and q is continuous. Hence their compact images N,P are
closed in H. Thus projecting an integral container has not introduced
an open image or merely a dense submodule.

Every h in Gamma preserves V and fixes W. Consequently it induces a
Q_3-linear invertible map on H, with inverse induced by h^(-1).
Since h(M)=M, it preserves P. Under P=M/F the action and its
reduction are precisely L033's, so P/3P is Gamma-irreducible.
This uses the actual fixed line; it neither substitutes another line
nor appeals to irreducibility of the full rank-107 trace kernel.

### Putative stability forces scalar equality inside H

Suppose for contradiction that h(N)=N for every h in Gamma. Since
P and N are full lattices in the same H, their bases give invertible
rational change-of-basis matrices. Clearing their finitely many
denominators in both directions proves commensurability.

More explicitly, in a P-basis the columns of an N-basis form an
invertible 106-by-106 matrix T over Q_3. The condition 3^a N subset P
is that every entry of 3^a T belongs to Z_3. There are nonzero entries,
so the finite list of their valuations gives a least integer a satisfying
this condition. Put N'=3^a N. Minimality gives N' not subset 3P:
otherwise 3^(a-1)N subset P would contradict the choice of a.
Rational scaling commutes with the induced action, so N' is stable.

Its image (N'+3P)/3P is therefore a nonzero invariant F_3-subspace
of P/3P. By L033 this image is all of P/3P. Thus

    P=N'+3P.

The Z_3-module T_0=P/N' is finitely generated because P is finite
free. The displayed equality gives T_0=3T_0. The ideal (3) is the
maximal ideal, hence contained in the Jacobson radical of the local
ring Z_3. Nakayama's lemma in the cited form gives T_0=0.
Consequently N'=P, or

    q(C)=3^(-a) q(M)

as subsets of this very H. This proves the required same-space scalar
homothety rather than an abstract isomorphism. The direct argument uses
only finite words and their invariant subspaces, so no compact-group
closure, enlarged group or stability-extension assumption is necessary.

### Contradiction and precise nonpreservation verdict

The actual W is a rational line in V. Audited L034 excludes the
last equality for every rational line and nonzero Q_3 scalar. Its
empty necessary interval, 2<=v_3(scalar)<=-1, applies in particular
to scalar 3^(-a) and this W. Hence the supposed preservation fails.

To justify the existential escape without claiming an explicit word,
choose g in Gamma with g(N) unequal to N. If g(N) is not contained
in N, some n in N has g(n) outside N. If g(N) is contained properly
in N, choose n in N\g(N); then g^(-1)(n) is outside N. In either
case a finite word h (g or g^(-1)) sends some n in N outside N.
Since N=q(C), choose c in C with q(c)=n. Equivariance gives
q(h(c))=h(n) outside q(C). Finally q^(-1)(q(C))=C+W:
equality of two quotient classes means their difference is in W.
This proves exactly the stated quotient escape.

The verdict passes the bounded continuation test: all required line
and lattice obligations hold, and the criterion decides nonpreservation.
No field valuation has been placed on H, and no quantitative lower
bound or membership in an actual IUT input follows from this existential
quotient statement. The primitive fixed-line stop of L032 and the
independent packet/scalar-transport stops in ATTEMPTS/022–024 persist.
The separate critical audit below validates this qualitative application.

### Separate critical audit, 2026-10-08

The independent audit validates the conclusion with no change to its
hypotheses or proof. It reuses the approved primary-source coverage and
audited L033/L034, including their exact field and reference-action
qualifications. It neither reopens L034's finite certificate without
a concrete concern nor imports the dissertation's abstract-isomorphism
ending as same-space equality. This is a review of the existing
known-method application, not a new mathematical result.

First, the rank-107 integral direct sum of L033 spans V. Extending
it to Q_3 gives V=W direct-sum (Q_3 E), with y_1 nonzero.
Comparing these coordinates shows M intersect W=F; in particular no
fractional multiple of y_1 belongs to M unless its coefficient is in
Z_3. Thus q(M)=M/F is an identification induced by q itself. The
kernel of M -> P/3P is exactly F+3M: q(m)=3q(m') is equivalent
to m-3m' in M intersect W=F. Thus the Nakayama step uses precisely
the residual module proved irreducible in L033.

The quotient-image theorem applies to both full lattices in the same
V and the same rational W, regardless of whether C and M are nested.
Each image is finitely generated, torsion-free as a submodule of H,
and spans H; over Z_3 it is free of rank 106. Closedness is also
valid: finite-dimensional linear subspaces are closed, V/W is
Hausdorff, and the continuous images of the compact basis images
of Z_3^107 are compact and hence closed. No equality between an
image and its closure has been assumed. The generators and inverses
of L033 preserve M and fix y_1, so their rational extensions fix W
and induce exactly the stated invertible action on P and H.

For the scaling step, let m_0 be the minimum valuation among the
nonzero entries of the change-of-basis matrix T. Its entries lie in
Q_3, so m_0 is an integer and a=-m_0 is the least integer with
3^a N contained in P. This permits negative a; no normalization to
nonnegative exponents is hidden. At least one scaled entry is a
unit, equivalently N' is not contained in 3P. If N is stable under
every finite word, rational scaling gives stability of N', and the
induced nonzero residual subspace is invariant under exactly Gamma.
L033 forces its surjectivity, which means P=N'+3P.

The images of any 106-element basis of P generate T_0=P/N' over
Z_3. Thus T_0 is finitely generated even before invoking any
topological fact. The equality above gives T_0=3T_0. In the cited
Stacks Lemma 10.20.1, the ideal (3) is the maximal ideal of the
local ring Z_3, so Nakayama yields T_0=0. Consequently N'=P
as embedded modules in H, and N=3^(-a)P there. An abstract module
isomorphism, rational change of ambient coordinates or compact-group
closure is not being substituted for this equality.

For contradiction, L034 uses these same C=O_L intersect V and
M=J_L intersect V. Its exclusion holds for every rational line,
so applies to the actual W without requiring prescribed coordinates
or a converse realization of arbitrary lines. The proposed scalar
has valuation -a; its necessary inequalities would be
2<=-a<=-1, which are impossible. The residual-irreducibility and
nonhomothety inputs therefore meet in exactly the same rational space.

Finally, nonpreservation gives a finite word g with g(N) unequal to N.
If g(N) is not contained in N, by definition some n in N has
g(n) outside N. If g(N) is properly contained in N, take n in
N outside g(N); invertibility gives g^(-1)(n) outside N.
The inverse is itself a finite word in the specified subgroup. Since
N=q(C), the chosen n lifts to an actual c in C, and equivariance
gives the asserted escape. The preimage identity q^(-1)(q(C))=C+W
uses precisely the rational kernel W, not the integral F. Thus the
claim does not silently strengthen a quotient escape into a prescribed
input, coordinate witness or numerical radius.

The whole-kernel fixed-line obstruction and ATTEMPTS/022–024 persist.
The audit supplies
no further field valuation on H, actual/native compatibility, numerical
comparison or original-IUT flaw candidate.

## Mathlib

Full matching actual-line projected-container theorem: **not checked**.
Supporting quotient-lattice, invariant-subspace, Nakayama, compact-image
and same-space homothety coverage: **not checked**. The exact mathematical
inputs, source qualifications and full application are stated above.
Unknown Mathlib availability is not evidence of absence. No formal
verification or complete IUT resolution is claimed.
