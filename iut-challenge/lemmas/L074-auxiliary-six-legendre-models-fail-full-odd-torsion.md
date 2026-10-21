# L074 — All six auxiliary ordered-root Legendre models fail full odd torsion

## Hypotheses

Fix one witness E_aux/Q: y^2=g_aux(x) from L073, in its embedded
Q-bar inside Omega, with the origin at infinity. Keep its original
monic integer cubic and fixed precision M>=max(M_tors,31) in L048's
neighborhood. Write E=E_aux in this proof. Division fields contain
both coordinates of every geometric point. Set

    K_aux=Q(zeta_60,E[2]),
    F_aux=K_aux(E[15])=Q(zeta_60,E[30]).

Use the same actual tau from L073: tau belongs to G_(K_aux), acts
as -Id on E[8], acts as Id on E[15], and fixes F_aux pointwise.
No new curve, Galois element or field enlargement is chosen.

Label the distinct roots r_1,r_2,r_3 of g_aux in this Q-bar, and put
a=r_2-r_1, b=r_3-r_1, lambda=b/a. For every ordering (i,j,k), define

    d_ij=r_j-r_i, t_ijk=(r_k-r_i)/d_ij,
    E_ijk/F_aux: V^2=X(X-1)(X-t_ijk),

with origin at infinity. These are the six explicit ordered-root
models; none is assumed to be a specified native descent over T.

## Conclusion

None of a,b,b-a is a square in F_aux. Every E_ijk is nonsingular,
geometrically pointed isomorphic to E, and fails full F_aux-rational
15-torsion. In a basis transported from E[15], the same tau acts as
-Id on E_ijk[15] for every ordering. No E_ijk is pointed isomorphic
to E over F_aux.

These are unconditional consequences for the fixed L073 auxiliary
witness, within the inspected known methods. The result does not
decide radical membership for the retained E_0, identify native T or
its model, settle exact field generation, or demonstrate an IUT flaw.
The separate step292 critical audit below validates this specialization.
STATUS remains IN_PROGRESS; it is not a complete candidate resolution.

## Proof

### Imported results and reason for the specialization

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-17-auxiliary-ordered-legendre-obstruction.md`.
L070–L072 record the inspected source methods for the retained witness;
their fixed-witness conclusions are not asserted for this different
curve. Here the general results are applied with auxiliary hypotheses
verified explicitly. The direct mathematical lemma inputs are L048's
family-wide invariant calculation and L073's witness and fixing element.

Import Jeffrey Yelton, *A note on 8-division fields of elliptic curves*,
[arXiv:1704.06190v2, 2 August 2017](https://arxiv.org/pdf/1704.06190v2),
degree-three definitions and Theorem 1(a),(b), printed pp.1–2. For a
monic separable cubic in characteristic different from two, its cyclic
radicals A_i, with A_i^2=r_(i+1)-r_(i+2), belong to the full 4-division
field; any actual Galois element acting as -Id on the 8-torsion negates
each A_i. This is the general theorem, not a generic-image proposition.
No generic surjectivity, radical independence or infinite-level scalar
lift is imported. The inspected specialization cases in Lemma 3,
Steps 1–4, pp.2–3, and the degree-three proof in Proposition 12,
pp.7–8, are part of the saved source coverage; no reproof is needed.

For the pointed coordinate maps use Milne, *Elliptic Curves*, second
edition (2021), [II Theorem 2.4(b), pp.52–53](https://www.jmilne.org/math/Books/EC2.pdf).
For the square-class interpretation use Auer–Top, *J. Number Theory*
95 (2002), [Introduction p.303, Lemmas 2.1–2.2 p.304 and the six-parameter
discussion p.305](https://pure.rug.nl/ws/portalfiles/portal/14410242/2002JNumberThAuer.pdf).
Their finite-field propositions are not applied over these number fields.
Use [Sutherland, Lecture 21, 6 May 2024, section 21.2 p.2](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf)
for nonexceptional-j pointed quadratic-twist classification, including
the trivial character. Import the transported-basis sign formula from
[Gonzalez-Jimenez, Lozano-Robledo and York, arXiv:2408.04159v1,
8 August 2024, Lemma 3.4 proof p.12](https://arxiv.org/pdf/2408.04159v1).
Only its coordinate formula is used, not its stronger division-field
equality. The formula is valid for both trivial and nontrivial restricted
characters; it does not require selecting an element that negates a
radical in advance. The needed pointwise-kernel convention and fixed-field
correspondence are [Sutherland, Lecture 20, 1 May 2024, section 20.1,
pp.1–2](https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf).

The general theorems are imported. The necessary work is the changed
witness's applicability, all six coordinate substitutions and signs,
and the restriction to its actual G_(F_aux). No new general twisting
or division-field theorem is being reproved or claimed.

### Auxiliary hypotheses and one fixing element

L073 supplies a nonsingular monic integer cubic in exactly L048's
fixed 3^M-neighborhood. L048's calculation holds for every cubic in
that neighborhood: c4 is a unit, v_3(Delta)=30 and hence
v_3(j(E))=3v_3(c4)-v_3(Delta)=-30. Thus j(E) is nonzero and differs
from 1728, whose 3-adic valuation is 3. The calculation concerns this
auxiliary curve, not an identification with the retained E_0.

The three nonzero 2-torsion points are (r_i,0). Therefore
K_aux=Q(zeta_60,r_1,r_2,r_3). It and F_aux are number fields of
characteristic zero. All six d_ij are nonzero and all t_ijk avoid
0 and 1, since the roots are distinct. Each E_ijk is consequently
nonsingular. The fixed element i=zeta_60^15 lies in K_aux, has
square -1 and is fixed by tau. Choose a primitive eighth root above
i in Q-bar if needed for Yelton's notation; it need not lie in K_aux.

The monic separable cubic over K_aux therefore satisfies Yelton's
degree-three hypotheses. L073 gives one actual tau with the prescribed
mod-eight action. Its mod-fifteen action is identity, and it fixes
K_aux, so it fixes every generator of F_aux=K_aux(E[15]) pointwise.
Thus this same tau belongs to G_(F_aux). Separate marginal-image
elements, x-coordinate fixing and setwise field preservation are not
substituted for this statement.

### Cyclic radicals and every signed difference

Choose Yelton's radicals in the same Q-bar:

    A_1^2=r_2-r_3=a-b,
    A_2^2=r_3-r_1=b,
    A_3^2=r_1-r_2=-a.

The imported theorem gives tau(A_m)=-A_m for m=1,2,3. It does not
require these radicals to be independent. Since tau(i)=i, the roots
s_a=A_3/i, s_b=A_2 and s_(b-a)=A_1/i have squares a,b,b-a and
are all negated by tau. Every radical is nonzero. If any s_c belonged
to F_aux, pointwise fixing would give s_c=-s_c, impossible in
characteristic zero. Its only other square root is -s_c, so none of
a,b,b-a is a square in F_aux. The same reasoning excludes a radical
that was already in K_aux; such a premise would contradict L073's
actual tau. No independence or degree-eight radical extension follows.

Here is every ordering, with an actual radical s_ijk for d_ij:

| Ordering | t_ijk | d_ij | s_ijk | tau(s_ijk) |
| --- | --- | --- | --- | --- |
| (1,2,3) | lambda | a | A_3/i | -A_3/i |
| (1,3,2) | 1/lambda | b | A_2 | -A_2 |
| (2,1,3) | 1-lambda | -a | A_3 | -A_3 |
| (2,3,1) | 1/(1-lambda) | b-a | A_1/i | -A_1/i |
| (3,1,2) | (lambda-1)/lambda | -b | i A_2 | -i A_2 |
| (3,2,1) | lambda/(lambda-1) | a-b | A_1 | -A_1 |

Indeed r_3-r_2=b-a and r_2-r_3=a-b; substitution in the definition
of t gives the six displayed fractions. The squares of A_3/i and
A_1/i are a and b-a, because i^2=-1. Also (i A_2)^2=-b.
The other three squares are the cyclic definitions themselves.
Every root in the table is negated and hence lies outside F_aux.
Changing any chosen square root by a sign preserves this conclusion.
Relations among radicals are allowed: an F_aux-valued product with
an odd number of these negated factors would contradict the actual
tau, while an even product is fixed. The proof presumes no missing
independence or trivial-character exception.

### Six pointed comparisons

For each ordering write d=d_ij, t=t_ijk and s=s_ijk. The factors of
g_aux(r_i+dX) are dX, d(X-1), d(X-t). Thus the geometric pointed map
and its inverse are

    phi_ijk(x,y)=((x-r_i)/d, y/(d s)),
    phi_ijk^(-1)(X,V)=(r_i+dX, d s V).

Since s^2=d, division by (d s)^2=d^3 gives exactly the stated
Legendre equation. These are invertible Weierstrass coordinate maps,
extending to infinity and preserving the origins by Milne's cited
theorem. In the convention x=u^2 X+r, y=u^3 V, take u=s and r=r_i.
Their complete rowwise formulas are

| Ordering | phi_ijk(x,y) |
| --- | --- |
| (1,2,3) | ((x-r_1)/a, y/(a(A_3/i))) |
| (1,3,2) | ((x-r_1)/b, y/(b A_2)) |
| (2,1,3) | ((x-r_2)/(-a), y/((-a) A_3)) |
| (2,3,1) | ((x-r_2)/(b-a), y/((b-a)(A_1/i))) |
| (3,1,2) | ((x-r_3)/(-b), y/((-b)i A_2)) |
| (3,2,1) | ((x-r_3)/(a-b), y/((a-b) A_1)) |

Every target therefore has the same nonexceptional j as E. Both
curves in each comparison admit short equations over F_aux by the
pointed translation eliminating the quadratic term, since the field
has characteristic zero. Thus the number-field, short-equation and
n=15>2 hypotheses of the imported representation formula hold.
No integral local-model assertion is needed here.

### The entire restricted torsion action, in every row

For sigma in the whole G_(F_aux), define

    chi_ijk(sigma)=sigma(s_ijk)/s_ijk in {+1,-1}.

All r_i,d_ij and t_ijk are F_aux-rational, so applying sigma to
phi_ijk changes its second coordinate by precisely this sign:
sigma(phi_ijk)=[chi_ijk(sigma)] phi_ijk. Here [-1] on the target
is (X,V) -> (X,-V); the inverse of a sign equals itself.

Choose a geometric Z/15Z-basis P_1,P_2 of E[15]. It is fixed by
every sigma in G_(F_aux), by the definition of F_aux. For the
transported basis Q_m=phi_ijk(P_m), the cited sign formula gives,
also directly on these full points,

    sigma(Q_m)=sigma(phi_ijk)(sigma(P_m))
              =[chi_ijk(sigma)] Q_m,
    rho_(E_ijk,15)(sigma)=chi_ijk(sigma) Id,
    ker(rho_(E_ijk,15)|G_(F_aux))=G_(F_aux) intersect ker(chi_ijk).

This is a statement on the entire restricted group. The following
table specializes it to all rows and to the same tau:

| Ordering | chi_ijk(sigma), for every sigma in G_(F_aux) | chi_ijk(tau) | rho_(E_ijk,15)(tau) |
| --- | --- | --- | --- |
| (1,2,3) | sigma(A_3/i)/(A_3/i) | -1 | -Id |
| (1,3,2) | sigma(A_2)/A_2 | -1 | -Id |
| (2,1,3) | sigma(A_3)/A_3 | -1 | -Id |
| (2,3,1) | sigma(A_1/i)/(A_1/i) | -1 | -Id |
| (3,1,2) | sigma(i A_2)/(i A_2) | -1 | -Id |
| (3,2,1) | sigma(A_1)/A_1 | -1 | -Id |

In each case -Id differs from Id on the free module (Z/15Z)^2.
In particular each Q_m has exact order 15 and is moved by tau:
equality Q_m=-Q_m would imply 2Q_m=0. Therefore the full restricted
kernel is proper, and not all geometric E_ijk[15] points are
F_aux-rational. This detects the y-coordinate sign which an
x-coordinate field would omit.

For completeness, the kernel formula says full rationality is equivalent
to chi_ijk being trivial on all G_(F_aux), equivalently s_ijk belonging
to F_aux by the fixed-field correspondence. The nonexceptional-j twist
classification identifies this with a pointed F_aux-isomorphism to E.
An alternative pointed geometric isomorphism differs by an F_aux-defined
sign and has the same character, so it cannot remove this obstruction.
Here every row has chi_ijk(tau)=-1; none of these equivalences is used
to assume rationality before testing it.

### Relevance, continuation test and qualifications

All six coordinate, sign and complete-kernel tests pass for this one
witness and its one fixing element. This settles the approved
intermediate target by specializing known results. It is local progress
beyond the unevaluated auxiliary test, with no claim of a theorem beyond
the inspected sources. No numerical evidence, explicit coefficients,
new curve selection or mathematical script is required.

The downstream use is a screen of these six explicit auxiliary models
before any separately assessed native-descent/generation comparison.
The retained E_0,F,K_glob,Omega,embedding,u,w,H,N,q_0 are unchanged;
equal auxiliary completions do not identify their global witnesses or
parameters. Retained scalar occurrence and radical memberships, native
T/model, exact generation, independent initial data, source-marked
all-image factorization, pilot transport, essentiality and original
finite B>=A remain unresolved. ATTEMPTS/027,028,031,032,033 remain
intact. No universal claim about all native descents is concluded.
The construction was recorded before the separately approved critical
audit below; the original proof attempt did not certify its own audit.

### Separate critical audit — 2026-10-17, step 292

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-17-auxiliary-six-legendre-critical-audit.md`
covers precisely this audit. Reuse the primary theorem versions and
essential cases cited above; no general theorem is reproved. L048 and
L073 are the direct mathematical inputs. The retained-witness conclusions
of L070–L072 are not used as auxiliary conclusions. All claims in this
lemma's Conclusion pass; no mathematical correction or additional
native-model claim is made.

**Hypotheses and identity of the witness.** L048 states its invariant
calculation for every monic integer cubic in the fixed neighborhood,
before the global reselection. The L073 witness is one such cubic.
Since Delta(g)=3^30(U+3^(M-30)z), U is a unit and M>=31, its
discriminant is nonzero with valuation 30. The same congruences give
c4=1 modulo 3. Thus its j has valuation -30, excluding 0 and
1728 (the latter has valuation 3). This checks the sign-automorphism
hypothesis for this curve itself. It does not transfer a retained
curve's j-value by equating completions.

L073's audited conclusion supplies one actual tau fixing K_aux and
acting by (-Id,Id) on (E[8],E[15]). Restriction from its level-120
action is simultaneous, not a choice of two marginal elements.
Every root lies in K_aux through (r_i,0) in E[2], and every E[15]
point is fixed by tau. These are generators of F_aux, so tau fixes
that field pointwise. The equality with the 30-division compositum
uses both coordinates and the rational group law: for P in E[30],
P=[15]P+[16]P, with the summands in E[2] and E[15]. Conversely
both subgroups lie in E[30]. No assertion about x-coordinates alone
would establish this field identity. All fields here are number
fields inside the specified Q-bar, and i=zeta_60^15 is fixed.

**Cyclic signs and all six maps.** Yelton's degree-three theorem
applies over K_aux to this monic separable cubic in characteristic
zero. Its actual mod-eight scalar hypothesis is exactly L073's.
The cyclic differences are a-b, b, -a, in that order. Consequently
the radicals in the six rows have squares, respectively,

    a, b, -a, b-a, -b, a-b.

The division by i in rows one and four and multiplication by i in
row five are valid because i^2=-1 and tau(i)=i. Each of these six
nonzero radicals is negated by the same tau. No degree or independence
of their compositum is assumed. In particular a trivial radical class
would imply a nonzero fixed element equal to its negative; the actual
tau excludes this case, rather than a generic-image hypothesis doing so.

For a row (i,j,k), direct substitution gives
g(r_i+dX)=d^3 X(X-1)(X-t). The six numerators r_k-r_i and
denominators d are (b,a), (a,b), (b-a,-a), (-a,b-a),
(a-b,-b), (-b,a-b). Their ratios are exactly the displayed six
parameters. All denominators are nonzero, and neither 0 nor 1
occurs, since the three roots are distinct.

The factors ds in the six y-coordinate denominators are, respectively,

    a A_3/i, b A_2, -a A_3, (b-a)A_1/i, -b i A_2, (a-b)A_1.

Each has square d^3. In the same order the six inverse maps are

    (X,V) -> (r_1+aX,       (a A_3/i)V),
    (X,V) -> (r_1+bX,       (b A_2)V),
    (X,V) -> (r_2-aX,       (-a A_3)V),
    (X,V) -> (r_2+(b-a)X,   ((b-a)A_1/i)V),
    (X,V) -> (r_3-bX,       (-b i A_2)V),
    (X,V) -> (r_3+(a-b)X,   ((a-b)A_1)V).

Composition in either order gives the identity. To check the omitted
point explicitly, homogenize each forward map as the invertible
projective linear transformation

    [x:y:z] -> [(x-r_i z)/d : y/(ds) : z].

It sends y^2 z=product_m(x-r_m z) to
V^2 Z=X(X-Z)(X-tZ) and sends [0:1:0] to [0:1:0]. Its inverse
is the homogenization of the corresponding map above. Thus these
are pointed isomorphisms of the complete nonsingular curves, with
Milne's parameter u=s, not only affine substitutions. They preserve
the elliptic group laws and transport full torsion bases. Characteristic
zero also permits the pointed translations to short equations required
by the cited representation calculation, without changing the fields.

**The whole restricted kernel.** Fix any row and any sigma in
G_(F_aux), before specializing to tau. Since s^2=d is fixed,
sigma(s)/s is a sign; composition makes this a character. All other
coefficients of phi are fixed, so sigma(phi)=[chi(sigma)] phi.
The inverse sign in the y-denominator is the same sign, which checks
the orientation of this formula. For a full basis P_1,P_2 of E[15],
every sigma fixes both points, hence

    sigma(phi(P_m))=[chi(sigma)]phi(P_m), m=1,2.

This proves the asserted scalar matrix on the entire restricted group
in every row. The argument also works when chi is trivial; it does
not use the excluded stronger division-field assertion in Lemma 3.4.
Since 1 and -1 are distinct in Z/15Z, its kernel is exactly the
character kernel, equivalently the subgroup fixing s. It is not merely
a necessary condition on one torsion point. In every row chi(tau)=-1,
so tau moves both exact-order-15 basis points: a point equal to its
negative would be killed by 2 as well as 15. Thus the full restricted
kernel is proper, and full F_aux-rational 15-torsion fails. An x-only
test would lose precisely this sign and is insufficient.

**Alternative pointed isomorphisms and limits.** All six targets
have E's nonexceptional j. The cited pointed automorphism classification
therefore says that any other geometric pointed comparison is [epsilon]
phi for epsilon=+1 or -1. Both signs are defined over F_aux, so this
change leaves the same character. It cannot turn a nontrivial character
into a rational pointed isomorphism. This proves the last conclusion,
without assuming rational torsion on the target in advance. It concerns
alternative comparisons to each fixed target, not a classification of
all possible native descents.

This audit validates a known-method auxiliary obstruction. It neither
identifies the native T/model nor proves that the six targets exhaust
the native possibilities. Exact generation, retained scalar occurrence
and radical memberships, independent initial data, marked all-image
factorization, pilot transport, essentiality and finite B>=A remain
unresolved. The direct inputs and argument are unchanged; no new DAG
edge, numerical certificate or mathematical script is needed.

## Mathlib

Full matching and supporting Mathlib coverage of this auxiliary
specialization has not been checked. No absence or formal-verification
claim is made. The general division-field, coordinate, twist and kernel
inputs are precisely cited; the auxiliary applicability, six signs and
full restricted actions are the explicit specialization above.
