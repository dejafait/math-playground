# L079 — Complete integral-affine dyadic Kummer classes

## Hypotheses

Use L033's curve E0: y²+y=x³−x²−10x−20, L069's Kummer
coordinates X=4x, Y=8y+4, and L078's entire local field

    H=Q2(pi), pi^11=2,
    J=H[rho], rho³−3pi⁴rho²+2pi⁸rho−pi=0,
    theta=−16+12pi⁷rho−2pi³rho².

Use the maximal rings, fixed theta, valuation normalizations, 34-bit
unit-square labels and precision proved in L078. In particular
v_J(pi)=3, v_J(2)=33 and arithmetic modulo eight has precision 99.
No global unit basis, class value, rank bound, GRH assumption or
integer solution is assumed. The independent audit below includes L078's arithmetic proof.

## Conclusion

The integral-x locus of E0(H) has a complete, explicitly realized
Kummer-class list of 2048 distinct labels, of rank 11, in L078's fixed
34-bit coordinates. Each of the 32768 disks x0+pi^15 O_H is realized
and has a certified constant label. Representatives are encoded by

    x0=sum_(i=0)^14 b_i*pi^i,
    mask=sum_(i=0)^14 b_i*2^i,   b_i in {0,1}.

The complete disk certificates are in
`scripts/ramified-dyadic-image/affine-disks.json`; one mask per distinct
class is in the `representative_masks` field of
`scripts/ramified-dyadic-image/affine-certificate.json`.

By the cited full-image cardinality theorem, this realized set is also
the abstract full image δ(E0(H)/2E0(H)) in J*/J*². It gives a membership
test: a class of odd valuation is absent; for even valuation divide by
that even power of rho, compute its L078 label, and test the list.
This equality uses point realization, exact square comparison and the
full-image theorem, not a sample count alone.

The stronger requested certificate of the complete Bruin–Stoll
LocalImage run is unfinished: reciprocal-chart terminal/rejected disks
and their exceptional treatment are not supplied here. The finite list
is exact, but no claim is made that both source algorithm charts have
been implemented. No additional global restriction rank, filtered unit
dimension, localized class contribution or integer exclusion follows.

## Proof

### Realization of every integral disk

For any x in O_H, the polynomial

    F_x(T)=T²+T−(x³−x²−10x−20)

reduces modulo pi to T²+T. Indeed the residue field is F2, so
x³−x²=0 there and both 10 and 20 vanish. Each of 0 and 1 is a simple
root, because F'_x(T)=2T+1 is a unit at every integral T. The standard
simple-root Hensel theorem gives one root y in each residue class,
for every actual x in O_H. Thus all points used below exist exactly
over H. The two roots give the same Kummer value because that value
depends only on x. They exhaust the degree-two polynomial; no square
feasibility case or rejected disk is omitted within this integral locus.
The roots can equivalently be specified by their unique Hensel limits;
a truncated y-coordinate is not substituted for an actual point.

The origin-preserving coordinate change in L069 identifies these points
with Y²=g(X), where g(X)=X³−4X²−160X−1264. The standard monic-cubic
Kummer evaluation is [X−theta], with no scalar quotient: Denis Simon,
*Computing the rank of elliptic curves over number fields*, LMS J.
Comput. Math.5 (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Section 1.1,
Propositions 1.1–1.2, printed p. 8; also Barrera Salazar–Pacetti–Tornaría,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020, Section 1, pp. 3–4. These are the previously assessed
Kummer interface, imported without reproof. The cubic remains
irreducible over H by L078, so no finite Weierstrass point is present.
In particular these evaluations are always nonzero.

### Uniform terminal disks and precision

In theta's displayed coordinates the three summands have J-valuations
132,88,44 respectively. Thus v_J(theta)=44. For integral x,
v_J(4x)>=66, so v_J(4x−theta)=44. This even valuation can be removed
by the square rho^44. Put exactly

    A=4/rho^44,   B=−theta/rho^44,
    U(x)=(4x−theta)/rho^44=A*x+B.

Then A is integral of valuation 22, B is a unit, and every U(x) is a
unit. These are field identities, before any reduction. If x−x0 belongs
to pi^15 O_H, then

    v_J(U(x)−U(x0)) >= 22+3*15=67.

As U(x0) is a unit, U(x)/U(x0) belongs to 1+rho^67 O_J. L078's
imported strict Hensel square-neighborhood theorem makes this ratio a
square, since 67>2v_J(2)=66. Hence every disk has one constant class,
not merely one computed residue value. This is the square-constancy
mechanism used in Bruin–Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. 78 (2009), 2347–2370,
[DOI](https://doi.org/10.1090/S0025-5718-09-02255-8),
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 4, Lemma 4.4 and its proof, pp. 7–8. The specialization is stated
explicitly to retain the changed model's factor 4 and actual ramification;
we do not copy v(4)=2 from the rational base.

The pi-adic residue digits 0,1 give exactly 2^15 disjoint residue disks
covering O_H. For each mask the implementation computes U(x0) modulo
8 O_J, at precision 99. This is after exact normalization, so dividing
by rho^44 does not reduce that precision to 55. That distinction is
essential: reducing 4x−theta modulo eight before normalization would
not suffice. The normalized input error 99 and the disk variation 67
both exceed the strict square threshold 66.

### Exact certificate and every collision

Run

    python3 scripts/ramified-dyadic-image/check_affine_disks.py
    python3 scripts/ramified-dyadic-image/verify_affine_certificate.py

The implementation constructs

    rho^(-1)=pi^10*(rho²−3pi⁴rho+2pi⁸)/2

in the exact rational coefficient algebra, raises it to the 44th power,
and obtains A,B. It verifies every coefficient of A,B is integral and
checks rho^44*A=4 and rho^44*B=−theta exactly, before reduction.
These computations use L078's monic field relations, not an assumed
power order. Full exact coefficients are saved in `exact_normalizers`.

All 32768 masks are enumerated in Gray-code order. Changing digit i
adds or subtracts exactly A*pi^i modulo eight. Each disk record saves
its mask, normalized input, 34-bit label, selected class generators,
square-root factor and final residual. L078's digit procedure verifies

    U(x0)=representative * square_root_factor² * residual  (mod 8),
    v_J(residual−1)>66.

The residual and modulus error are both squares in the required unit
neighborhood. This establishes each class equality. Different labels
are inequivalent by L078's proved basis independence; equal labels are
exact square-class collisions, not collisions of a coarser invariant.
The histogram and one explicit mask per class retain every collision.

The certificate has 15/15 passing checks and no failures. It records
32768/32768 disks, 2048 distinct labels, and 11 independent original
point-label witnesses. The rank is recomputed by binary elimination.
Since 2048=2^11, these labels fill their span, including identity.
The replay reads every full disk record, checks its exact normalized
input, rebuilds the labeled representative from the fixed generators,
checks the full square-factor/residual reconstruction, covers every
mask exactly once, compares the entire collision histogram and
recomputes independence from the original witness labels. Its 8/8
checks pass with no failures; the complete verification is in
`scripts/ramified-dyadic-image/affine-verification.json`.
This replay verifies the stored evidence; it is not an independent
audit of the mathematical square-class basis in L078.

### Abstract full-image equality and remaining chart obligation

Import Barrera Salazar–Pacetti–Tornaría, cited above, Lemma 1.3, printed
p. 4: for any finite H/Q2,

    |δ(E0(H)/2E0(H))|=[O_H:2O_H]*|E0(H)[2]|.

This is the ready assessment's already inspected general theorem.
L078 specializes its hypotheses: H has degree 11 and the entire cubic
algebra is a field, so E0(H)[2]={O} and the right side is 2048.
Every one of our 2048 inequivalent classes is realized by an actual
point. They therefore exhaust this abstract full image. Infinity's
class is identity, which occurs in the list. For any class of even
valuation, division by rho to that even exponent removes a square;
L078 then decides its unit label. All image labels have even valuation
because their integral representatives above have valuation 44. This
proves the stated membership test for every nonzero field element.

The cardinality theorem also ensures that nonintegral points cannot
add a class, but does not construct or enumerate their reciprocal
terminal disks. The approved task explicitly requests those records,
as well as exceptional-chart treatment, so its full algorithmic
certificate remains open. Nothing here claims a run of SquareClasses
in the reciprocal chart. The integral-affine stage is an exact
specialization of known methods with independently unresolved global
unit independence, S-class arithmetic, rank and integer-point gaps.

### Independent critical audit — 2026-10-16

The complete audit confirms the stated integral-affine and abstract full
image claims. For every integral x, both simple residue roots lift; this
is exact realization on every disk, not a finite-coordinate approximation.
The fixed theta has valuation 44, strictly smaller than 66+v_J(x), so
normalization by rho^44 removes a square and introduces no cancellation.
The exact identities rho^44*A=4 and rho^44*B=−theta independently certify
the saved integral normalizers. Computation starts with A*x+B, at
precision 99; it does not divide an already truncated numerator.

The independent verifier described in L078 reads all 32768 full records.
It recomputes each center's normalized input, reconstructs its class from
the fixed generator product and a unit square-root factor, and verifies
the residual bound. It compares every mask, every collision multiplicity,
every advertised representative's actual label and every independence
witness. Actual/required disks are 32768/32768; distinct classes are
2048/2048, of rank eleven, and the minimum residual bound is 67>66.
The disk variation is also 67>66. No stored success flag substitutes for
an equation or a count. Evidence and reproduction command are in L078's
independent audit section and its separate certificate.

The cited BPT formula is used specifically over the finite dyadic field
H, with [O_H:2O_H]=2^11 and no nonidentity rational two-torsion because
g is irreducible over H. Kummer injectivity then makes the 2048 realized,
inequivalent classes the entire image. This does not require the
parameter-chart calculation or subgroup closure of a sampled subset.
The later L081 chart supplies the separate pointwise coverage obligation;
neither calculation is a literal execution of the source's cubic-X tree.
No correction of the claimed image is required by this audit, and no
additional global direction is obtained.

## Mathlib

Full matching ramified-field integral-affine image, explicit 2048-class
list, disk certificate and implementation: **not checked**. Supporting
Hensel, maximal-ring square classes, Kummer maps and local image-size
declarations: **not checked**. Unknown coverage is not absence.
