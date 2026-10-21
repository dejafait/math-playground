# L071 — Retained ordered-root Legendre twist classes

## Hypotheses

Retain L045 and L048's same nonsingular monic cubic
E_0/Q: y^2=g(x), its origin at infinity, its fixed embedded Q-bar,
and F=Q(zeta_60,E_0[30]). Keep M>=max(M_tors,31), the original
embeddings and completions, and the changed q_0 with v_3(q_0)=30.
Division fields contain both coordinates of every geometric point.
No coefficients are made effective and no curve is reselected.

Label g's three roots r_1,r_2,r_3 in Q-bar and write

a=r_2-r_1, b=r_3-r_1, lambda=b/a.

For each ordering (i,j,k) of (1,2,3), define

d_ij=r_j-r_i, lambda_ijk=(r_k-r_i)/d_ij,
E_ijk/F: V^2=X(X-1)(X-lambda_ijk).

These are F-models; none is identified with the specified native
Legendre descent over native T=F_tpd. Auxiliary division fields
below serve only as membership tests; F itself is unchanged.

## Conclusion

Every r_i is in F, every displayed d_ij is nonzero, and every
lambda_ijk is in F minus {0,1}. The quadratic comparison class
between E_0 over F and E_ijk is [d_ij] in F^times/(F^times)^2.
The complete table is

| Ordering (i,j,k) | lambda_ijk | d_ij | Class in F |
| --- | --- | --- | --- |
| (1,2,3) | lambda | a | [a] |
| (1,3,2) | 1/lambda | b | [b] |
| (2,1,3) | 1-lambda | -a | [a] |
| (2,3,1) | 1/(1-lambda) | b-a | [b-a] |
| (3,1,2) | (lambda-1)/lambda | -b | [b] |
| (3,2,1) | lambda/(lambda-1) | a-b | [b-a] |

For each row, the following are equivalent: its class is trivial;
E_0 and E_ijk are pointed F-isomorphic; every geometric point of
E_ijk[15] is F-rational. Consequently at least one of these six
models passes the full-15-torsion test exactly when at least one
of a,b,b-a is a square in F. All six pass exactly when E_0[4] is
F-rational.

More precisely, put K=Q(zeta_60,r_1,r_2,r_3),
R=K(E_0[4]) and J=R intersect F inside the retained Q-bar. Then

F=K(E_0[15]),
R=K(sqrt(a),sqrt(b),sqrt(b-a)),
F(E_0[4])=F(sqrt(a),sqrt(b),sqrt(b-a)).

For c equal to a, b or b-a, its class is trivial in F exactly when
K(sqrt(c)) is contained in J. These are three specified, possibly
trivial, quadratic-extension tests, not an assumption that the
three classes are independent.

This step does not determine any of those three memberships for
the retained existential curve. It proves neither that full
30-torsion forces a pass nor that it permits a failure here. The
forcing question stops at the unproved intersection J, rather
than substituting full 4-torsion for full 30-torsion. No native
model, exact-generation or original finite B>=A verdict follows.

## Proof

### Imported results and specialization

Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-legendre-normalization-square-classes.md`.
Milne, *Elliptic Curves*, second edition (2021),
[II Theorem 2.4(b), pp.52-53](https://www.jmilne.org/math/Books/EC2.pdf),
gives the pointed Weierstrass coordinate transformations.
Auer and Top, *J. Number Theory* 95 (2002),
[Introduction p.303, Lemma 2.1 p.304, six-parameter discussion p.305](https://pure.rug.nl/ws/portalfiles/portal/14410242/2002JNumberThAuer.pdf),
give the general-field Legendre square-class criterion and the
root-difference halving test. Their finite-field Proposition 2.1
is not used over F. The table is the explicit specialization of
these coordinate criteria to the retained ordered roots, not a
reproof of general descent or halving.

Yelton, [arXiv:1704.06190v2, 2 August 2017](https://arxiv.org/pdf/1704.06190v2),
**degree-three definitions and Theorem 1(a), p.1**, states, for a
monic separable cubic over a field of characteristic different
from 2, that its full 4-division field is obtained from its
2-division field by adjoining zeta_4 and A_i with
A_i^2=r_(i+1)-r_(i+2), cyclically. Use this general statement,
not a generic-field-only proposition later in the paper.

For the character and odd-torsion assertions, use Sutherland,
[MIT 18.786 Lecture 21, 6 May 2024, section 21.2 p.2](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
for nonexceptional-j twist classification, and
Gonzalez-Jimenez, Lozano-Robledo and York,
[arXiv:2408.04159v1, 8 August 2024, Lemma 3.4 proof p.12](https://arxiv.org/pdf/2408.04159v1),
for the transported-basis formula rho_twist,n=chi rho_original,n.
Only that formula is used, with n=15; no stronger general
identity of division fields is imported. These are the inspected
sources used in the conditional comparison L070. The present
calculation specifies F-models directly and does not assume
L070's conditional native T or identify any such model with it.

### Retained field hypotheses

L045 makes every geometric 30-torsion point of this E_0 rational
over F. Its three nonzero 2-torsion points are exactly (r_i,0),
since the cubic is monic, separable and has characteristic zero.
They lie in E_0[30], so r_i lies in F for each i. Distinctness
implies a,b,b-a are nonzero and every lambda_ijk differs from
0 and 1. The infinity points are the specified origins.

The primitive zeta_60 gives i=zeta_60^15 in K subset F, with
i^2=-1. Therefore [c]=[-c] in F^times/(F^times)^2, and also in
K^times/(K^times)^2. L048 gives v_3(j(E_0))=-30, excluding j=0
and j=1728, the latter having v_3=3. This remains true over F
and for every geometrically isomorphic E_ijk. Thus the cited
classification has precisely the two geometric pointed
automorphisms Id and [-1]. No assertion about integral models
is needed for these field-level coordinate transformations.

### Coordinate maps, all six classes and odd torsion

Fix one ordering, and abbreviate d=d_ij, t=lambda_ijk. The
F-defined pointed substitution x=r_i+dX and y=dY gives

Y^2=d X(X-1)(X-t).

Indeed the three factors of g(r_i+dX) are dX, d(X-1) and
d(X-t), so division by d^2 gives exactly that equation. For a
choice s=sqrt(d) in Q-bar the pointed geometric comparison to
E_ijk is

phi(x,y)=((x-r_i)/d, y/(d s)).

Its inverse is (X,V) -> (r_i+dX, d s V); both extend at infinity
by the cited pointed-coordinate theorem. In particular no
cube-scaling constant or unrecorded field extension is needed
in the definition of the F-model E_ijk itself.

For sigma in G_F, sigma(s)/s is a sign chi_d(sigma).
Applying sigma to this map changes its V-coordinate by
chi_d(sigma), because the inverse of a sign equals itself.
The resulting twist character is therefore precisely that of d,
with no ambiguity between d and d^(-1) at the square-class level.
The six ordered differences are a,b,-a,b-a,-b,a-b. Computing
t=(r_k-r_i)/d gives the six entries in the table; replacing a
negative difference by its positive counterpart in the last
column is legitimate because i is in F.

By the cited classification at nonexceptional j, this twist is
trivial exactly when phi descends to a pointed F-isomorphism,
equivalently s lies in F. In particular an alternative pointed
isomorphism cannot remove a nontrivial character: it differs
from phi by one of the F-defined signs. This checks necessity
as well as the explicit isomorphism when s is in F.

Every E_0[15] point is F-rational by L045. In a basis transported
through phi, the cited formula therefore gives

rho_(E_ijk,15)(sigma)=chi_d(sigma) Id for every sigma in G_F.

On the free geometric module (Z/15Z)^2, -Id is different from Id.
Thus all of E_ijk[15] is F-rational exactly when this character
is trivial on the whole G_F, equivalently sqrt(d) lies in F.
This uses full point coordinates; x-coordinates alone would lose
the sign. It proves the rowwise equivalences without assuming
rational odd torsion on E_ijk to construct phi.

### The exact division-field boundary

Apply Yelton's Theorem 1(a) first over K and then over F.
Both fields have characteristic zero, contain all r_i and i,
and use the same monic separable cubic. Its cyclic differences
are -(b-a), b and -a. Since i already belongs to both base
fields, changing these signs does not change their radical
fields. This gives the two stated formulas for R and F(E_0[4]).
In particular all three classes vanish in F exactly when
F(E_0[4])=F, which proves the all-six criterion. It does not
make full 4-torsion necessary for just one row to pass.

The full-coordinate division fields satisfy
Q(E_0[30])=Q(E_0[2],E_0[15]). To check both inclusions, each
2- or 15-torsion point is a 30-torsion point. Conversely, for
P in E_0[30], write P=[15]P+[-14]P. The first summand is in
E_0[2] and the second in E_0[15]. The rational elliptic group
law shows that the point P is rational over the field containing
those two full sets. This handles infinity as well as affine
points, without interpreting a rational addition formula at a
pole. The 2-division field is Q(r_1,r_2,r_3), because the
nonzero 2-torsion points have y=0. Adjoining zeta_60 therefore
gives exactly F=K(E_0[15]).

For each c in {a,b,b-a}, sqrt(c) belongs to R by its displayed
formula. Since K subset F, the following are equivalent:
sqrt(c) lies in F; K(sqrt(c)) subset F; K(sqrt(c)) subset R
intersect F=J. These equivalences include the case c is already
a square in K. No independence or degree of these quadratic
extensions is presumed.

The inputs supply no value of this intersection with
K(E_0[15]), nor an effective coefficient tuple from which to
compute the retained memberships. The retained torsion rationality establishes F=K(E_0[15]);
it leaves these quadratic-extension memberships unevaluated.
Accordingly the bounded forcing test is unresolved at exactly
these three memberships. This is not a counterexample to a
universal implication and not an assertion that one is true.

### Scope and known traps

This is a specialization of the inspected known coordinate,
twist and division-field results. It makes local notebook
progress by identifying all six comparison classes and the
remaining intersection; no result beyond those sources is
claimed. A square over a completion would not establish a
square in F. Failure of one class would not exclude the other
two. Even a pass would give only an F-model comparison, not its
identification with a specified native E_L/T or the equality
F=T(sqrt(-1),E_L[15]). Independent initial data, source-marked
all-image factorization, pilot transport, essentiality and finite
B>=A remain unresolved. ATTEMPTS/027,028,031,032 are unchanged.
The separate critical audit below validates this specialization,
without deciding any of the retained memberships.

### Separate critical audit — 2026-10-17, step 279

Reuse the prior SPECIALIZE coverage in
`drafts/literature/2026-10-17-retained-ordered-legendre-critical-audit.md`.
The audit checks the application of the precisely cited known results;
it does not reprove their general statements. L045 and L048 remain
the direct mathematical inputs. L070 supplies comparison context,
not a native-model hypothesis or an additional premise.

**Same curve and source hypotheses.** L048 retains the monic cubic
g=x^3+c x^2+d x+e at the precision chosen before reselection. Its
invariant computation gives v_3(Delta)=30 and v_3(c4)=0, hence
v_3(j)=-30. Thus it is nonsingular and j is neither 0 nor 1728
(whose valuation is 3). L048 explicitly applies L045 to that same
curve, so all its geometric 30-torsion, and therefore its 2- and
15-torsion, is rational over the specified F. Both K and F below
are number fields of characteristic zero inside the same Q-bar.
In particular the characteristic restrictions of all the cited
coordinate, twist and division-field results hold.

To check the short-equation hypothesis of the cited twist formula,
the F-defined substitution x=z-c/3 removes the quadratic term of
g; for the row equation, X=Z+(1+t)/3 removes its quadratic term.
These are pointed isomorphisms over F and preserve nonsingularity.
They change neither full-coordinate division fields nor the G_F
character of a geometric comparison. Their denominators are allowed:
no assertion of integral equations is being made. Nonexceptional j
justifies exactly the pointed signs in Sutherland's classification.
No finite-field proposition of Auer–Top is applied here.

**Every row and both coordinate directions.** For each ordering,
the ordered triple of root differences (0,d,r_k-r_i) gives
g(r_i+dX)=d^3 X(X-1)(X-t). For s^2=d, the map in the proof is
therefore the Weierstrass transformation with scaling u=s:
x=s^2 X+r_i and y=s^3 V. The composition with its displayed
inverse is the identity on both affine coordinates. More explicitly,
the projective linear transformation

    [x:y:z] -> [(x-r_i z)/d : y/(d s) : z]

is invertible, restricts to the two projective cubics, and sends
[0:1:0] to [0:1:0]. This verifies extension and origin preservation
without applying a monic Weierstrass theorem to the intermediate
equation with leading coefficient d.

The six numerator/denominator pairs for t are, in table order,

    b/a, a/b, (b-a)/(-a), (-a)/(b-a), (a-b)/(-b), (-b)/(a-b).

Substituting b=a lambda gives respectively lambda, 1/lambda,
1-lambda, 1/(1-lambda), (lambda-1)/lambda and lambda/(lambda-1).
All denominators are nonzero because the roots are distinct.
The corresponding d's are a,b,-a,b-a,-b,a-b, exactly as printed.
Since zeta_60^15 has order four in K, multiplying a radical by
this element changes its square by -1. Thus the three repeated
classes, including every sign conversion, hold over K and F.

**Uniqueness and the entire restricted kernel.** Write phi_d for
the displayed map and chi_d(sigma)=sigma(s)/s. Its coefficients
give sigma(phi_d)=[chi_d(sigma)] phi_d for every sigma in G_F.
This identity holds whether or not s is already in F. Any other
geometric pointed isomorphism from E_0 to this row differs from
phi_d by a pointed automorphism of E_0, hence by an F-defined
sign. Its character is therefore the same. Consequently an
F-isomorphism exists if and only if chi_d is trivial, equivalently
s is fixed by all of G_F and belongs to F. This checks necessity;
the explicit map checks sufficiency. Repeated geometric parameters
cannot introduce another self-twist, since j is nonexceptional.

For a geometric Z/15Z-basis P_1,P_2 of E_0[15], set Q_i=phi_d(P_i).
L045 makes sigma(P_i)=P_i for every sigma in G_F. It follows directly
that sigma(Q_i)=chi_d(sigma) Q_i on the entire group. If chi_d is
trivial, every Q_i and their sums are rational over F. If it is
nontrivial, some sigma has sign -1 and moves a point of exact
order 15: equality with its negative would give order dividing 2.
Thus ker(rho_(E_ijk,15))=ker(chi_d) as subgroups of G_F, in both
cases. This verifies the elementary formula's application even
in the trivial-radical case excluded by the additional hypothesis
used later in the cited Lemma 3.4 proof. No stronger field identity
from that lemma is invoked, and no x-coordinate kernel is used.

**Both exact 4-division identities.** In Yelton's degree-three
Theorem 1(a), take the ordered roots to be r_1,r_2,r_3. Its three
cyclic differences are r_2-r_3=-(b-a), r_3-r_1=b and r_1-r_2=-a.
Over each of K and F the 2-division field is already the base
field, and zeta_4 is already present. The theorem therefore gives
exactly the two radical composita in the conclusion, with both
inclusions supplied by the cited equality. Changing the square-root
choices or the indicated signs leaves each compositum unchanged.
The theorem requires neither generic coefficients nor independence
of these radicals. All six rows pass if and only if all three
generators lie in F, equivalently F(E_0[4])=F. The weaker assertion
that some row passes needs only one generator to lie in F.

**Exact 30/15 boundary and intersection.** For a point P killed
by 30, put P_2=[15]P and P_15=[-14]P. Then 2P_2=0,
15P_15=[-210]P=0 and P_2+P_15=P. Conversely every point killed
by 2 or 15 is killed by 30. Multiplication and addition are
Q-morphisms of the pointed elliptic curve, including the origin,
so these two statements give both inclusions of the full-coordinate
division fields. Since the nonzero 2-torsion is (r_i,0), adjoining
zeta_60 gives F=K(E_0[15]) exactly, not just an inclusion or an
abstract field isomorphism.

For each c in {a,b,b-a}, the theorem puts K(sqrt(c)) inside R.
It is inside J=R intersect F if and only if it is inside F,
if and only if c is a square in F. This also holds when the
extension over K is trivial, or when two of these extensions
coincide. Nothing in this audit calculates J or makes these tests
independent. Full rational 30-torsion is not replaced by full
rational 4-torsion, and no implication in either direction of the
unresolved forcing question is inferred.

**Verdict.** The six-row criterion and exact field identities pass
this audit. The checks make the short-model applicability, all six
fractions, projective inverse and both character cases explicit;
no statement or DAG edge needs correction. This validates a local
known-result specialization, not a new theorem beyond the inspected
sources. The specified native T and E_L/T, exact generation,
independent initial data, source-marked all-image factorization and
essentiality remain open, as does finite B>=A. Foundations/05
step272's source-version and model qualifications are unchanged.
No completion membership is promoted to global membership and
ATTEMPTS/027,028,031,032 are not reopened.

## Mathlib

Full matching and supporting Mathlib coverage of this retained
six-ordering, twist and division-field specialization has not
been checked. No absence or formal-verification claim is made.
The argument imports the precisely cited general results and
writes out their applicability and coordinate specialization;
no mathematical script or numerical certificate is used.
