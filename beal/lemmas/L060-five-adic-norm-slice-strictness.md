# L060 — Whole-fiber compatibility is stricter than the five-adic norm condition

## Hypotheses

Use L033's curves, dual isogeny theta:E1 -> E0 and connecting map delta,
and L034's complete modular map j. Work over Q5 and fix L038's entire
algebra identification A=Q5 x U, where U/Q5 is unramified of degree eleven.
Write R for the integers of U and k=F_(5^11) for its residue field;
v(5)=1. Use exactly L035's sets I_all and I_fiber, including every scalar
s in Q5 minus {0,1728}, every entire-fiber isomorphism and the exceptional
good-divisor evaluations. Put

    S_N={alpha in I_all : N_(A/Q5)(alpha)=[121]}.

Norms here are on fifth-power classes. A compatible fiber uses one common
scalar on both factors. No global solution, unit/class basis, image size,
finite precision, GRH, rank or Sha assumption is made. I_fiber is not
assumed to be a subgroup.

## Conclusion

    0 < |I_fiber| <= 600 < 9765625 = 5^10 <= |S_N|.

In particular I_fiber is a proper subset of S_N. By the already audited
L040, the same statement holds for I_pow. In addition every compatible
scalar is integral and is congruent to 2 or 4 modulo five.

This decides the approved equality question by a strict cardinality
separation. It does not enumerate either image or specify an individual
excluded class; the existence of excluded classes follows rigorously
from the two bounds. It supplies a further local necessary condition,
not a global class intersection, branch exclusion or integer solution.
The independent critical audit below confirms this specialization without
correction or strengthening of its conclusion.

## Proof

### Imported inputs and the precision used

General descent and its good-divisor evaluation are imported as in L033:
Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an elliptic
curve*, Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, pp.8–10, and Section 9, pp.21–24. L033 verifies its
cohomological hypotheses and the dual direction. In particular delta
is a homomorphism, and, away from T and O, is evaluation of

    f=(x-4)y-4x^2+30x-55,
    E0: y^2+y=x^3-x^2-10x-20.

We use only those statements, not an uncomputed isogeny quotient size.
The source of the complete modular map is Freitas–Naskręcki–Stoll,
*The generalized Fermat equation with exponents 2, 3, n*, Compositio
Math. **156** (2020), 77–113,
[June 10, 2019 author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, pp.25–27, equation (7.4), specialized and audited in L034.

For lifting use Pete L. Clark, *Algebraic Number Theory II*,
[161-page author-hosted notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, printed p.58, version retrieved 2026-10-08 with revision
date unidentified. The hypothesis is |G(a)|<|G'(a)|^2; the root is unique
in |z-a|<|G'(a)|. These hypotheses and the coprime factor version in
Milne, *Algebraic Number Theory*, v3.08, July 19, 2020,
[Theorem 7.33 and Remark 7.36](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
pp.121–123, were already assessed for L038–L040. No new general lifting
theorem is proved here.

As in L035, over Q5 or U every unit in 1+125R is a fifth power: apply
the strong form to G(Z)=Z^5-u at Z=1, with v(G(1))>=3>2v(G'(1))=2.
The case u=1 is immediate. Thus two units congruent modulo 125 have
the same fifth-power class. This is a sufficient bound, not an assumed
minimal precision. Simple-root lifting below always has unit derivative.

### Every compatible scalar is in the two integral residue disks

For a compatible whole fiber, let (x,y) be its projection to E0(U).
L040 proves [Q5(x):Q5]=11: the whole-fiber projection generates U by
x,y, and y has degree at most two over Q5(x). It also proves that any
integral compatible scalar has residue 1,2 or 4; for a nonintegral
scalar v(s)=-n it proves that x is integral,

    n=11k0,  k0>=1,  v(x-16)=k0,
    (x-16)^11=t J(x)+t^2 h(x)^3,  t=s^(-1),             (1)

where J=2a-b, h and a,b are L034's exact integral polynomials and
J(16)=h(16)=1 modulo five. These necessary statements include all
exceptional charts and use only the complete-map polynomial identity.

Suppose s is nonintegral. Write t=5^(11k0)c with c in Z5^*, and
x=16+5^k0 z with z in R^*. Dividing (1) by 5^(11k0) gives

    G(z)=z^11-c J(16+5^k0 z)
                 -5^(11k0)c^2 h(16+5^k0 z)^3=0.

This polynomial is in Z5[z] and reduces to z^11-cbar. Since
5^11=5 modulo eleven, eleven does not divide 5^11-1. Raising to the
eleventh power is therefore bijective on k^*. The unique residue root
of z^11=cbar lies already in F5^*, since raising to eleven is also
bijective there. Its derivative 11z^10 is nonzero. Hensel over Q5
supplies a root z0 in Z5 with that residue. Hensel uniqueness over U
makes every root with the same residue equal to z0. Our z has that
unique residue, so z=z0 is rational. Hence x is rational, contradicting
degree eleven. This excludes every k0 and unit c, not just bounded
negative valuations.

If s=1 modulo five, the polynomial

    F_s(X)=h(X)^3+sJ(X)-s^2(X-16)^11

has the same reduction as L038's F1: the product of its two distinct
irreducible degree-six factors. Coprime Hensel lifting gives a
factorization into two monic degree-six polynomials over Q5, uniformly
for all such s. A root of F_s cannot have degree eleven. Thus residue
one is impossible as well. The only remaining scalars are

    s in (2+5 Z5) union (4+5 Z5).                       (2)

This uses L038's full residue factorization, not just its fixed-scalar
nonisomorphism conclusion. The other integral residues were excluded
uniformly in L040.

### At most 600 whole-fiber connecting classes

For r=2,4 the exact reductions of F_s, in ascending coefficients, are

    Fbar_2=[0,3,1,2,0,4,4,2,3,1,4,3,1],
    Fbar_4=[0,1,2,4,3,3,4,2,3,4,0,3,1].

For each r, gcd(Fbar_r,Fbar_r')=gcd(Fbar_r,bbar)=1. The certificate
below provides full Bezout identities, verified by coefficient
multiplication. Consequently all residue roots are simple and b is
a unit at every integral root of F_s. We do not assume (X-16)^11 is
a unit: for r=4 its gcd with Fbar_4 is X-1.

Because F_s is monic integral, x is integral; the curve equation makes
y integral too. The residue xbar in k cannot be rational. Otherwise
simple-root lifting of F_s from xbar over Q5, followed by uniqueness
over U, would give x in Q5. The prime degree eleven then implies
that xbar has degree eleven. In particular xbar is not zero.

L033's polynomial identity on the curve is

    f(x,y) f(x,-y-1)=-(x-5)^5.

Both factors are integral. Since xbar is not zero, the right side is
a unit, so f(x,y) is a unit. In particular the U component cannot be
T or any exceptional rational point. This unit assertion is essential
to the precision comparison.

Fix a scalar residue modulo 125 satisfying (2), and a root xbar of
the corresponding Fbar_r in k. There is at most one x modulo 125R
lifting it and satisfying F_s(x)=0 modulo 125R: successive lifts
modulo 25 and 125 solve linear equations whose coefficient is the
unit Fbar_r'(xbar). The coefficients of F_s modulo 125 depend only
on s modulo 125. Thus any two actual points with this scalar residue
and xbar have the same x modulo 125, even if their exact scalars differ.

The identity

    a(x)+b(x)y=s(x-16)^11

holds at every finite fiber point by regularity, including 2T where
the original expression for j has a removable denominator. Since b
is a unit here, it determines y modulo 125 from x and s modulo 125.
It follows that f(x,y), a unit, is determined modulo 125, and therefore
its fifth-power class is determined. Each of the two scalar residues
modulo five has 25 lifts modulo 125; each degree-twelve reduction
has at most twelve roots in k. The U-component image thus has size
at most 2*25*12=600. This upper bound may overcount; no irreducible
degree-eleven factor computation at residue four is required.

All U embeddings and whole-fiber isomorphisms are included in these
residue roots. Finally L035 gives, for every whole-fiber class
(alpha_0,alpha_U),

    alpha_0 N_(U/Q5)(alpha_U)=[121].                   (3)

For a fixed alpha_U this uniquely determines alpha_0 in
Q5^*/Q5^{*5}. Therefore projection to the U component is injective on
I_fiber and |I_fiber|<=600. This remains valid when the rational
component is T and requires a good divisor: (3) already includes that
case, and we have not evaluated f(T) as a unit or divided by it.

### At least 5^10 unrestricted norm-slice classes

Let Q=2T=(16,-61). Choose one z in R for each residue in k and put
x_z=16+5z. The polynomial in y defining E0 has value zero modulo five
at y=-61 and derivative -121=4 modulo five. Hensel gives a unique
y_z congruent to -61; thus P_z=(x_z,y_z) is an actual U point.
Write y_z=-61+5w. Expanding the curve equation modulo 25 gives

    -121w=726z modulo 5,  hence w=-6z modulo 5.

Here 726=3*16^2-2*16-10. At Q,

    f(Q)=-1331,
    df/dx=(16-4)(-6)-61-8*16+30=-231.

Consequently

    f(P_z)/f(Q)=1+5z modulo 25R.                      (4)

These are units and ordinary evaluations; all x_z have residue one,
so none of these points is T or O. Each class
eta_z=delta(P_z)/delta(Q) belongs to the unrestricted connecting image
because delta is a homomorphism. For distinct residues z,z', the ratio
of their representatives is 1+5(z-z') modulo 25 and is not a fifth
power. Indeed, a hypothetical fifth root is a unit; its residue has
fifth power one, hence equals one in the characteristic-five field k.
The root is therefore 1+5w, whose fifth power is 1 modulo 25. This
contradicts z-z' nonzero modulo five. We obtain 5^11 distinct unit
classes in delta(E0(U)).

The norms of these classes lie in the unit fifth-power quotient of
Q5, which has at most five elements. To justify the bound with the
same sufficient precision, there are 100 units modulo 125, and the
fifth-power map on that finite multiplicative group has kernel

    {1,26,51,76,101}.

For verification, a fifth root of one has residue one, so it is
1+5w modulo 125; its fifth power is 1+25w modulo 125. This equals
one precisely when w=0 modulo five, giving those five roots. Thus
there are twenty fifth-power residues and five quotient classes.
Units with representatives in the same quotient class differ by a
fifth power times a unit in 1+125Z5; the latter is a fifth power by
the lifting argument above. The bound of five follows.

By the pigeonhole principle at least 5^10 of the eta_z have the same
norm class. Divide these by one chosen eta_z in that collection; the
result is 5^10 distinct norm-one classes in delta(E0(U)). Giving them
identity Q5 component embeds them in I_all with total norm one.
L039 supplies a class alpha_* in I_fiber, and L035 gives its norm
[121]. Multiplying alpha_* by the constructed norm-one classes gives
5^10 distinct elements of I_all, all with norm [121]. We only use
the subgroup property of I_all, never of I_fiber. This proves the
lower bound for S_N. L039 also proves the asserted nonemptiness.

### Verification, downstream scope, and qualifications

Run `python3 scripts/five-adic-norm-slice/check_bounds.py`.
The full certificate is
[bounds-certificate.json](../scripts/five-adic-norm-slice/bounds-certificate.json).
It retains both complete relevant residue polynomials, all Bezout
coefficients for squarefreeness and b-invertibility (and the nonunit
d-gcd at residue four), the nonintegral unit evaluations, exact
derivative calculations, the rational fifth-power residues, and both
bounds. All 25 checks pass. The complete load-bearing residue-two,
residue-four, quotient and bound fields were inspected. Actual upper
bound 600 is below the required lower bound 9765625. The complete
nonintegral argument and the uniform precision proof above are
necessary in addition to the arithmetic certificate.

This specializes the assessed descent and local-lifting methods. The
general theorems are imported; the explicit varying-scalar argument is
needed because the inspected sources do not decide this comparison.
Classification is REPRODUCTION, with no certified claim of originality.
No quantifier-elimination implementation or source image-size formula
is needed. The finite residue evidence is used with proved completeness,
not treated as a p-adic sampling experiment.

For a future global intersection this proves that the norm equation
alone loses local information. The excluded classes need not occur in
the global class image; no certified global units, ordinary/S-class
value, simultaneous other-place compatibility, rational point or
integer lifting follows. Independent twists and residual signatures
remain unresolved. The separate review below checks the entire-fiber
degree argument, all nonintegral scalars, the uniform unit precision,
norm-based injection and translated lower-bound family.

### Independent critical audit, 2026-10-12

The prior SPECIALIZE assessment for this exact audit is reused. No
mathematical correction is required. The following review establishes
the reliability of this local input; it adds no image enumeration or
stronger restriction, and makes no claim of originality.

First, the affine-generation premise in audited L040 is applicable to
every isomorphism: the complete finite fiber avoids O and its algebra
is generated by x,y. Projection onto U is surjective. Since the curve
equation is quadratic in y, x must have degree eleven. L040's complete
coprime degree-six blocks exclude integral residues zero and three.
For residue one, the independent arithmetic below multiplies L038's
two degree-six blocks to the exact reduction of F_s and checks their
coprimality. Milne Theorem 7.33 lifts both degrees for every scalar in
that disk. A root in a field annihilates one lifted factor and cannot
have degree eleven. Internal irreducibility of a lifted block is not
needed for this exclusion.

For negative scalars L040 supplies integral x and n=11k0, k0>=1.
The scaled polynomial G is integral over Z5 for every unit c and every
such k0. Every derivative term from J(16+5^k0 z) or h(16+5^k0 z)
vanishes modulo five; the remaining derivative is 11z^10. The exact
value gcd(11,5^11-1)=1 proves a unique nonzero residue root in k.
Its F5 root exists since gcd(11,4)=1, and is therefore the same root.
Choose its integer representative r. Both over Q5 and over U,
G(r) lies in the maximal ideal and G'(r) is a unit, so Clark Theorem
1.79 applies in the identical ball |z-r|<1. If G(r)=0 the root is r
itself and simple-root uniqueness still applies. Otherwise the strict
Hensel inequality supplies it. The rational root and the proposed U
root coincide. This contradicts the required degree of x and excludes
all negative valuations, with no bounded-depth assumption.

In the two remaining disks F_s is monic integral. Thus x is integral;
a negative valuation of y would give v(y^2+y)=2v(y)<0, contradicting
the integral right side of the curve equation. Independent Bezout
checks give gcd(Fbar_r,Fbar_r')=gcd(Fbar_r,bbar)=1 for r=2,4.
If xbar were in F5, simple-root uniqueness over Q5 and U would again
make x rational. In particular xbar is not zero. The independently
checked identity f(x,y)f(x,-y-1)=-(x-5)^5 then makes both factors
units. For each scalar modulo 125 and residue root, successive simple
lifts determine x modulo 125, and a+by=sd determines y modulo 125
because b is a unit. These identities hold by regularity even where
d=0; indeed gcd(Fbar_4,dbar)=X-1, so inverting d would be invalid.
The same residue pair therefore determines the unit f modulo 125.
Its ratio with any other such f belongs to 1+125R, where the strong
Hensel inequality 3>2 proves fifth-power triviality. This yields at
most 2*25*12 U classes, regardless of isomorphisms or collisions.

The rational component can include T. L035's good-divisor norm proof
deforms the entire fiber while retaining algebra generation, so (3)
holds there as well. For each U class it determines exactly one
rational fifth-power class. No evaluation of f(T), invertible d, or
subgroup property of I_fiber is used. The 600 bound thus applies to
the complete product image, not merely to a selected factor.

For the lower bound, unit derivative -121 lifts y for every chosen
z in R, not just for rational z. Direct differentiation gives dy/dx=-6,
f(Q)=-1331 and df/dx=-231, hence df/f=1 modulo five. All P_z and Q
avoid the exceptional descent support, and their ratios represent
connecting classes by L033. Distinct residues of z have ratio
1+5(z-z') modulo 25. A fifth root of that ratio would be a unit with
residue one: in characteristic five, W^5=1 has only the root one.
Its fifth power would be one modulo 25, a contradiction. There are
therefore 48828125 distinct unrestricted unit classes. Norms of units
are units, and the rational unit quotient has at most five classes,
as verified both by the binomial formula and the complete mod-125
fifth-power table. Dividing one norm fiber by a fixed member preserves
distinctness and gives at least 9765625 norm-one classes. The product
connecting map allows identity in the Q5 component independently of
the U point. Translation by L039's whole-fiber class stays in the
subgroup I_all and has norm [121]. This verifies the lower bound in
the correct S_N without asserting closure of I_fiber.

Run `python3 scripts/five-adic-norm-slice/audit_bounds.py`. It imports
no construction code, reconstructs J from 2a-b and d by binomial
coefficients, checks the integer elimination and f-conjugate identities,
and multiplies every saved Bezout witness independently. All 49 checks
pass. The [complete audit certificate](../scripts/five-adic-norm-slice/bounds-audit-certificate.json)
retains the full coefficients, residue cases, witness products, unit
table, derivative data and bounds. Complete selected load-bearing
original and audit fields were inspected. Actual upper bound 600 is
strictly below required lower bound 9765625. The uniform arguments
above, in addition to the finite certificate, are essential. All direct
mathematical inputs remain those already recorded for L060 in the DAG.

## Mathlib

Full explicit norm-slice strictness and the cardinality bounds: **not
checked**. Supporting Hensel, residue-field, elliptic connecting-map,
finite-group and norm declarations: **not checked**. Unknown coverage
is not evidence of absence.
