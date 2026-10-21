# L111 — Exact genus-one quotient of the fixed-minus-three marked curve

## Hypotheses

Use the smooth proper geometrically integral curves B,D of audited L109,
with Q(D)=Q(B)(v), v²=z, and audited L110's exact model and functions

    W²=11(T²−4)Q4(T),
    Q4=7+52T−6T²−64T³−25T⁴,
    F=T⁵+T⁴−4T³−3T²+3T+1,
    K=T²−T−1,  L=T²+T−1,
    u=(F−11−KW)/(60F),  M=2−10u,
    z=−M²(T−2)L²/[300(T+2)K²].                          (1)

All curves and function fields are over Q, of characteristic zero.
The marking is v²=z, not the auxiliary ordered extension obtained by
adjoining sqrt(−3z). No rational point of the open marked locus,
rational distinguished root, integer solution or remaining factor is
assumed. Retain L110's original scalar s=H0(u,z).

## Conclusion

Let E be the smooth proper completion of the quartic

    R²=b(T)=−33Q4(T)
           =825T⁴+2112T³+198T²−1716T−231.                (2)

It is a geometrically integral genus-one curve over Q. The rational
smooth point O_E=(2,165) makes (E,O_E) an elliptic curve, without any
claim about its Mordell–Weil group. There is a finite degree-two
Q-morphism D -> E. An exact smooth model of D is the completion of

    h²=a(T)=−3(T²−4),     R²=b(T).                      (3)

The function-field maps are

    rho=M L/[30(T+2)K],
    h=v/rho,       R=3W/h;
    W=hR/3,        v=rho(T,hR/3)h.                     (4)

They are inverse identifications of Q(D) and Q(T,h,R), preserving
the exact z and original s. The quotient map forgets h, and its
involution is (T,h,R) -> (T,−h,R). This is different from the deck
involution over B, which changes both h and R.

Every rational point of E has finite T. For P=(t,r) in E(Q), the
rational lifts under D -> E are exactly

    (t,h,r) with h in Q and h²=3(4−t²).                 (5)

For t!=±2 this gives two lifts if a(t) is a nonzero rational square,
and none otherwise. Above each of (2,±165) it gives one rational
ramification point, with h=0. There is no rational E-point at T=−2
or infinity. Consequently rational images must also satisfy (5);
a rational point of E alone is not a rational marked pair.

This is a specialization of known split-cover theory, not a
rational-point determination or an integer exclusion. Degree-nine
rational-root recovery, remaining factors, both L095 simultaneous
power systems and the minus-eleven alternative remain unresolved.
The separate critical audit completed on 2026-10-21 confirms this
construction; its proof and independent arithmetic evidence are below.

## Proof

### Source specialization and the exact marked twist

Import the factor-cover construction in Nils Bruin, *The arithmetic
of Prym varieties in genus 3*, Compositio Math. 144 (2008), 317–338,
DOI 10.1112/S0010437X07003314, inspected
[arXiv:math/0408069v2](https://arxiv.org/pdf/math/0408069v2),
Section 2.2, manuscript pp.4–5, construction preceding Proposition
2.2 and its proof. It gives the projections from the split cover
y1²=f1(x), y2²=f2(x) of y²=f1(x)f2(x), for even-degree factors.
The genus-two quadratic–quartic case, with its constant-twist
ambiguity, is explicitly recorded in Jordan Docking,
*2-infinity-Selmer rank parities via the Prym construction*,
J. Number Theory 265 (2024), 208–225, DOI 10.1016/j.jnt.2024.06.009,
[arXiv:2108.09564v2](https://arxiv.org/pdf/2108.09564v2),
Section 2, Table 1 Case II, manuscript p.4.
We use the actual projections, not just the Prym's dimension or
the unrelated theorem for a genus-three base. These general results
do not choose this instance's twist or give its rational origin;
the following exact calculations supply that necessary specialization.

Define a,b,rho as above. Direct cancellation in Q(B) gives

    a*rho²
      =−3(T²−4)M² L²/[900(T+2)²K²]
      =−M²(T−2)L²/[300(T+2)K²]=z,
    a*b=9W².                                          (6)

Thus the square multiplier is exact, with a=−3(T²−4) and no
suppressed constant. In particular its sign and rational square
class differ from the untwisted auxiliary ordered field.
All divisions are generic function-field operations. T is
nonconstant by L110, so F,K,L,T+2 are nonzero functions. Also rho
is nonzero: if M were identically zero, (1) would give z=0,
contradicting L109's original nonempty open. L110 identifies W as
a nonzero function, and v is nonzero since v²=z. Hence h and the
denominators in (4) are nonzero functions.

Substitution in Q(D) now gives h²=a and R²=9W²/a=b.
Conversely, in (3) put W=hR/3 and use (1) to define u,z,rho.
Then W²=ab/9 is L110's sextic and v=rho h satisfies v²=z
by (6). Both compositions fix T,W,v and T,h,R respectively:
the products hR=3W and v=rho h give the inverse formulas.
This verifies the full fields, not just a match of invariants.
One can equivalently use y1=h, y2=R/3 in Bruin's construction;
their product is W and their squared factors are a,b/9.

The original scalar on the cover remains precisely

    s=H0(u(T,hR/3), z(T,hR/3)),

with H0 and all coefficients as in L109/L110. It is not replaced
by a function on E. No descent of s to E is needed or assumed.

### Geometric integrality, degree and the proper quotient

The exact polynomial Euclidean algorithm gives

    gcd(a,a')=gcd(b,b')=gcd(a,b)=1.                     (7)

Thus a has two simple roots, b four simple roots, and the two
root sets are disjoint over Qbar. Over Qbar(T), each of a,b,ab
is nonsquare, since it has a simple zero. The square classes of
a,b are independent, so the extension adjoining both roots has
degree four. For completeness, b cannot become square after
adjoining sqrt(a): writing a possible root as x+y sqrt(a)
forces xy=0 by its vanished sqrt(a) coefficient. This would make
b or b/a square in Qbar(T), contradicting those simple zeros.
This argument checks the instance's geometric component and
degree; it does not reprove the general Prym theorem.

Consequently (3) is geometrically integral, as is (2). For E the
double cover of the T-line has exactly four simple finite branch
points and no branch at infinity. Riemann–Hurwitz gives
2g(E)−2=2(−2)+4=0, so g(E)=1. We import Riemann–Hurwitz in
[Stacks, Section 53.12, tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B);
all maps here are characteristic-zero separable maps of smooth
proper curves. No rational point was used in this genus calculation.

In particular [Q(T,h,R):Q(T,R)]=2. Its nontrivial automorphism
fixes T,R and negates h, so its fixed field is exactly Q(E).
The inclusion is therefore an actual degree-two quotient field.
Under (4), the deck involution v -> −v over B negates both h,R,
whereas this quotient involution negates W=hR/3. They must not
be confused.

Here are full smooth charts, including every finite denominator
zero from (4). On the finite chart (3), the two equation gradients
are (−a',2h,0) and (−b',0,2R). They have rank two: if h=0,
then a' and R are nonzero; if R=0, then b' and h are nonzero;
otherwise their h,R entries already give rank two. The disjoint
simple branch sets prove each assertion. At infinity set

    x=1/T,   H=h/T,   S=R/T².
    H²=−3+12x²,
    S²=825+2112x+198x²−1716x³−231x⁴.                   (8)

At x=0 both H,S are nonzero, so these charts are smooth as well.
Gluing by these coordinate changes gives a finite curve over P¹
(each chart is defined by monic equations), hence a proper smooth
model of (3). E is similarly covered by (2) and the second equation
of (8). Projection to T,R on the finite chart, or x,S at infinity,
is the same proper morphism. Thus the formulas cover every point,
rather than deleting h=0 or a pole of rho.

Equivalently import [Stacks Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1):
the verified field isomorphism identifies this smooth proper curve
with L109's D, and the inclusion Q(E) into Q(D) extends uniquely
to a nonconstant proper morphism. Such a morphism of proper smooth
integral curves is finite, with degree the computed field degree
two. Its use is justified by the inverse fields above, including
the correct Q-form. The affine denominators do not require
pointwise inversion on the proper normalization.

As a consistency check, a has order one at both E-points above
each of T=2 and T=−2, since b is nonzero there and T−t is a
uniformizer. These are four geometric ramification points of
D -> E. At the two geometric infinity points it has order −2,
so it gives no ramification; elsewhere it is a unit. Hence
2g(D)−2=2(0)+4=4, agreeing with L109's g(D)=3. The étale map
D -> B remains a different degree-two morphism.

### Rational origin and the normalized lifting interface

At T=2 one has Q4=−825, b=27225=165² and a=0. The two E-points
(2,±165) are rational smooth points because 2R!=0. Select
O_E=(2,165). By the definition in [Stacks Section 105.2, tag 072J](https://stacks.math.columbia.edu/tag/072J),
a smooth proper geometrically connected genus-one curve with a
rational point is an elliptic curve. No Weierstrass conversion
or rank calculation is necessary for this assertion.

At T=−2 one has Q4=−9 and b=297=9*33, nonsquare in Q. At infinity
E has S²=825=25*33, so its infinity fiber has residue field
Q(sqrt(33)) and contains no rational point. These are normalized
smooth charts; the latter statement is not about a singular
weighted or plane closure. Both boundary tests and the exact
origin succeed, so the conditional integer scan |T|<=10 is not
needed and was not run. These tests classify only the specified
T-fibers, not the entire original s-boundary or E(Q).

Every E(Q)-point is finite and has residue equation h²=a(t) in
the smooth finite model (3). Its actual rational fiber is therefore
exactly (5). At t=2 the fiber is ramified with one point for each
sign of R, not two points distinguished by an assumed nonzero h.
These give the two rational marked points over B's (T,W)=(2,0).
They are boundary points: u=z=0 and s=phi(0)=1. They do not
represent disjoint roots in a regular fiber or primitive integers.

The agreement with L109's normalized-unit rule can be checked
without substituting zero into a discriminant. At B's T=2 point,
W is a uniformizer by L110, and

    (h/W)²=a/W²=−3/(11Q4) -> 1/55²,
    rho -> 1/12,
    v/W -> +1/660 or −1/660.                            (9)

The point with R=165 gives the plus sign because R=3W/h;
R=−165 gives the minus sign. Thus z/W² has residue 1/660²,
exactly L110's audited normalized unit, and both rational lifts
are retained. At T=−2 a zero of h can accompany a pole of rho;
one must use (3),(8) or the proper extension, never infer v=0
from the affine product rho h. There are no rational points there.
Likewise (8) retains the four geometric points at infinity;
their full residue field is Q(sqrt(33),sqrt(−3)), so none is
rational. Every other omitted F,K,L or rho value is covered by
the smooth charts and the same verified field identification.
L109's normalized-unit rule still governs D -> B at all such
points; (5) instead describes the different map D -> E.

### Verification and limits

The prior saved SPECIALIZE assessment is
`drafts/literature/2026-10-20-marked-pair-genus-one-quotient.md`.
The source methods are reused; no new literature search or claim
of originality is made. Precise twist, coordinate, field-degree
and origin verification is needed because the general construction
does not determine them for this instance.

Run `python3 scripts/pair-genus-two/marked_quotient.py`.
Its full output is `scripts/pair-genus-two/marked-quotient-certificate.json`.
All 28 checks pass, with no failures. The certificate stores exact
rational coefficients, input hashes, all twelve full identity
residuals in both field bases, the squarefree/coprime gcds and
boundary arithmetic. Both directions of (4) were checked in the
respective degree-four fields; all residual coefficients are zero.
The actual/required projection degree is 2/2 and quotient genus
1/1; their mathematical justification is the field and proper-model
argument above, not the printed numbers. The complete relevant
residuals, gcds, square multiplier and check values were inspected.

The first script run failed on Python coercion between the two
field layers; returning NotImplemented from the lower layer for
upper-layer arithmetic repaired it before a certificate was written.
This was an implementation failure and supplied no mathematical
evidence. It is not concealed as a failed twist or an arithmetic
counterexample.

The rational-image interface could support a later point method,
as in Bruin–Stoll, *Two-cover descent on hyperelliptic curves*,
Math. Comp. 78 (2009), 2347–2370,
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
Section 8, manuscript pp.14–15: points of the factor curves still
require lifting. Here no rational-point completeness, height bound,
rank, integer elimination or compatible degree-nine factor follows.
This is local progress by explicit specialization of inspected
known methods. The subsequent critical audit is recorded below.

### Independent critical audit, 2026-10-21

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-marked-genus-one-quotient-critical-audit.md`.
The audit confirms the existing conclusions without a mathematical
correction. L109's marked function field and L110's exact functions
and completed exceptional-chart audit are the mathematical inputs.
The following verifies this instance, not the general split-cover
or curve-extension theorems imported above.

First, independently expand a=12−3T² and b=−33Q4 and check
ab=9f, where f=11(T²−4)Q4. Substitution of the original M,K,L
gives z=a rho² with the exact constant −1/300 retained. The full
saved rho,z rational functions agree coefficient by coefficient
with the independent calculation. Their nonvanishing is checked
in Q(T)[W]/(W²−f); all polynomial denominators are nonzero since
T is transcendental. In particular this calculation does not
identify the marked extension with the auxiliary ordered extension.
The maps (4) satisfy h²=a, R²=b and hR=3W in Q(D).
In the reverse direction W=hR/3 and v=rho(T,W)h satisfy
W²=f and v²=z. Recomputing u and rho after recovering W gives
back v as well as u,z; reversing the other composition gives
back h,R. Thus both fields, not just one relation or invariants,
are identified over Q. The complete coefficients c_i of phi are
independently reconstructed from (3T²+T+1)^5(1−5T). Since both
u and z are fixed by composition, every term
c_i binom(i,2j)u^(i−2j)(−3z)^j is fixed. This proves preservation
of L110's entire H0 scalar without a truncated scalar expansion
or an assumption that s descends to E.

Second, the independently computed monic gcds in (7) all equal
one. Over Qbar(T), a,b,ab have simple zeros and hence are
nonsquares. If b=(x+y sqrt(a))², comparing the sqrt(a) coefficient
gives xy=0; the alternatives would make b or b/a a square,
contradicting their simple zero divisors. Consequently the
biquadratic field has degree four and is geometrically integral.
The subfield Q(T,R) has degree two over Q(T), so its index is
exactly two. Its fixing involution negates h and fixes R, whereas
the marked deck involution fixes W and negates both h and R.
These are different maps, even though both are double covers.

For completeness, properness and finiteness can be checked on
the actual chart rings. Let A_E=Q[T,R]/(R²−b). The finite chart
of D is A_E[h]/(h²−a), free of rank two over A_E with basis
1,h. At infinity put B_E=Q[x,S]/(S²−b_infinity(x)), with
b_infinity as in (8); the chart is
B_E[H]/(H²+3−12x²), again free of rank two. On the overlap
H=xh and S=x²R, so the finite free maps glue. Both E and D
are finite over P¹; they are therefore proper. Their generic
fields are the geometrically integral fields just verified, and
the finite charts have no vertical component because their
coordinate rings are free over Q[T]. The finite-chart Jacobian
rank test from (7), and 2H,2S nonzero at x=0, prove geometric
smoothness everywhere. Thus these are the full smooth proper
models, including every zero of F,K,L or rho. The inverse
function-field maps extend uniquely by Stacks Theorem 53.2.6
(0BY1). Alternatively the verified properness, integral
one-dimensional source and nonconstant image meet every
hypothesis of Stacks Lemma 53.2.4 in
[Section 53.2, 0BXX](https://stacks.math.columbia.edu/tag/0BXX),
which makes the extended map finite. The chart calculation
also verifies its degree two and flatness directly.

The map E to P¹ has four simple finite branch points, and its
infinity chart has two geometric points with S nonzero and x
a parameter; neither is ramified. All fields have characteristic
zero and the geometric curves are connected and smooth proper,
so the cited Riemann–Hurwitz formula applies and gives genus one.
For D to E, at each point above T=2 or T=−2 the function a has
order one: b is nonzero there, T−t is a parameter, and
a'(2)=−12, a'(−2)=12. These are exactly four geometric branch
points. At infinity a=x^(−2)(−3+12x²), whose unit factor has
nonzero residue; after replacing h by H the cover is unramified.
It is also unramified at every other finite point, where a is
a unit and 2 is invertible. This independently gives g(D)=3
from 2g(D)−2=4, consistent with L109.

Third, b(2)=27225=165² and 2R=330 at the proposed origin.
Thus O_E is indeed a rational smooth point, supplying the
section required by the cited elliptic-curve definition. The
complete smooth infinity fiber has S²=825=25*33; it is one
degree-two closed point over Q, with no rational point. Also
b(−2)=297=9*33 is nonsquare, so all rational E-points are
finite and have T different from −2. The full infinity fiber
of D has H²=−3, S²=825. The two constant square classes are
independent over Q (33 is nonsquare and positive, and both −3
and −99 are negative), so this is one degree-four point with
residue field Q(sqrt(33),sqrt(−3)), or four geometric points.
It adds no missing rational lift.

For a rational finite P=(t,r), base change of the finite free
chart gives exactly Spec(Q[h]/(h²−a(t))). If a(t) is nonzero,
the split and nonsplit quadratic algebras give respectively two
rational lifts or none. If t=2, the fiber is Spec(Q[h]/(h²)),
one rational point of length two, rather than two rational
points. In the source completed local ring, h is a parameter:
T−2=h²/(−12)+higher powers, since a'(2)=−12, and R is the
unique formal root of R²=b(T) with residue r. This proves the
ramification and multiplicity, not merely the number of signs.
It applies separately to r=165 and r=−165. The finite-free
fiber description exhausts every E(Q)-point.

Finally these two points map to B's T=2,W=0, where W is a
parameter since f'(2)=−36300. The identity W=hR/3 shows that
D to B is unramified there. With rho(2,0)=1/12,
h/W=3/R has residues ±1/55, so v/W has residues ±1/660 and
z/W² has residue 1/435600. This agrees exactly with audited
L110 and L109's normalized-unit criterion. Here u=z=0 and
s=1, so these are boundary points, not regular marked pairs.
At other exceptional affine denominators the already verified
proper field isomorphism identifies the local integral closures;
L110's complete charts and L109's normalized-unit rule therefore
apply, without substituting a zero or pole into v=rho h. The
lifting criterion for D to E is distinct from the everywhere
étale marked lifting criterion for D to B.

Reproduce the independent arithmetic with
`python3 scripts/pair-genus-two/audit_marked_quotient.py`.
It imports neither the producer nor its arithmetic classes.
Elements use four coordinates over Q(T), and inversion solves
the multiplication matrix by Gaussian elimination rather than
the producer's nested quadratic norms. All 94 checks pass with
no failures; all sixteen complete four-component residuals vanish.
The checker compares every saved polynomial, the full rho,z,
all twelve original residuals, both input hashes, all boundary
values and the producer's 28 check flags with independent exact
arithmetic. All relevant evidence was inspected in full; no
preview or reported count substitutes for a proof. The original
certificate is preserved, with SHA-256
`5a780e96f16bc15e8d3fcaa45b129ba0f1514069850073ed50378f2141c9207f`.
The full replay is
`scripts/pair-genus-two/marked-quotient-audit-certificate.json`.
Actual/required degree is 2/2 and quotient genus 1/1; the
geometric argument above justifies these values independently
of their printed assertions.

This establishes the reliability of the existing specialization,
not progress beyond the checked general methods. No rational-point
completeness, rank, degree-nine rational-root recovery, compatible
remaining factor, L095 integer exclusion or minus-eleven conclusion
has been established.

## Mathlib

Full matching split-cover, exact-instance quotient and elliptic-origin
coverage were not checked. Supporting results were not searched in
Mathlib in this step. No absence or Lean verification is claimed.
