# L078 — Exact arithmetic for the ramified dyadic Kummer-image computation

## Hypotheses

Use L046's field H=Q2(pi), pi^11=2, and its fixed maximal ring
O_H=Z2[pi]. Use L071's distinguished cubic generator s and change
of coordinates

    s^3-4s^2+6s-2=0,      theta=28-26s+6s^2,
    g(theta)=0,            g(X)=X^3-4X^2-160X-1264.

Let J=H[X]/(g), with this same theta. L076 identifies this ENTIRE
algebra with the degree-33 compositum, a field. Valuations below are
normalized at the uniformizer of the field in their subscript. No
elliptic point, global unit basis, class-group value, GRH assumption,
or primitive integer solution is assumed.

For the image-size threshold only, use L033's curve
E0: y^2+y=x^3-x^2-10x-20. L069's origin-preserving change X=4x,
Y=8y+4 identifies it with Y^2=g(X).

## Conclusion

The element rho=pi^4/s gives the exact maximal-ring presentation

    J=H[rho],
    rho^3-3*pi^4*rho^2+2*pi^8*rho-pi=0,
    O_J=O_H[rho],
    s=4-3*pi^7*rho+pi^3*rho^2,
    theta=-16+12*pi^7*rho-2*pi^3*rho^2.

The Z2-basis pi^i*rho^j, 0<=i<11, 0<=j<3, has valuations
3i+j. Thus e(J/Q2)=33, its residue field is F2, and reduction of
these 33 coefficients modulo eight gives exact arithmetic in O_J/8O_J
with error valuation at least 99.

The 34 units

    1+rho^n,    n in {1,3,5,...,65,66},

form a basis of O_J*/O_J*^2. The digit elimination proved below and
implemented in `scripts/ramified-dyadic-image/check_arithmetic.py`
gives their unique 34-bit labels for every unit. Two units have the
same label exactly when their quotient is a square in J. A nonzero
field element is a square exactly when its valuation is even and its
unit part after division by that even power of rho has zero label.
The implementation accepts integral units; valuation normalization for
other inputs is this separate exact field operation.

This certifies arithmetic and square comparison needed for the approved
LocalImage task. It does NOT compute that image, any terminal disk,
an additional global restriction, a rank bound, or an integer exclusion.

## Proof

### Whole field, maximal ring, and fixed generator

Use the Eisenstein local-field theorem in Pete L. Clark, *Algebraic
Number Theory II: Valuations, Local Fields and Adeles*,
[author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
the previously inspected 161-page version: Theorem 2.8 and Proposition
2.9/Corollary 2.10, printed pp.64–65. In a complete discretely valued
field, a root of a monic Eisenstein polynomial generates the entire
extension, is a uniformizer, and its powers are a maximal integral
basis over the base integer ring. These general results are imported;
we verify the new coefficients and generator maps explicitly.

First construct a root rho of

    R(Z)=Z^3-3*pi^4*Z^2+2*pi^8*Z-pi

over H. The H-valuations of its constant, linear, and quadratic
coefficients are respectively 1,19,4, because v_H(2)=11. It is
Eisenstein at pi, so H[rho]/H is a totally ramified cubic extension,
with O_H[rho] its maximal ring. The relation gives

    pi/rho=rho^2-3*pi^4*rho+2*pi^8.

Therefore s'=pi^4/rho=pi^3*rho^2-3*pi^7*rho+4, using pi^11=2.
Multiplication and reduction give

    (s')^3-4(s')^2+6s'-2=0.

For example, substituting s'=pi^4/rho and multiplying this last
expression by rho^3 gives

    pi^12-4*pi^8*rho+6*pi^4*rho^2-2*rho^3
      =2*(pi-2*pi^8*rho+3*pi^4*rho^2-rho^3)=0.

The H-algebra J, expressed in L071's s coordinate, consequently maps
to H[rho] by s -> s'. Both are degree-three fields over H, so this
unital map is an isomorphism. Conversely rho=pi^4/s; s is nonzero
because its polynomial has nonzero constant term. This identifies the
entire field, with no selection of a factor. Substitution of s' in
28-26s'+6(s')^2 gives the stated theta coordinate; direct reduction
also gives g(theta)=0. Thus the map retains precisely the distinguished
generator used by the Kummer evaluation, rather than an unspecified
cubic isomorphism.

Here v_J(rho)=1 and v_J(pi)=3, so v_J(2)=33. The residue field is
F2. The relative maximal integral basis together with L046's basis
for O_H gives the asserted 33-element Z2-basis. If

    a=sum c_(i,j)*pi^i*rho^j,        c_(i,j) in Q2,

then, for a nonzero a,

    v_J(a)=min_(c_(i,j)!=0) (33*v2(c_(i,j))+3i+j).

The 33 weights 3i+j are distinct modulo 33, so a minimum cannot
cancel. This proves the valuation formula for all coefficients, not
only integer test vectors. In particular every unit reduces to one
in F2. Reducing coefficients modulo eight changes a by an element
of 8O_J, which has valuation at least 99. All multiplication uses
the two monic relations, so the resulting quotient-ring computation
is exact; no uncertified power order is substituted for O_J.

### Sufficient precision and the exceptional last digit

Import the dyadic square-neighborhood fact used in the proof of
Bruin–Stoll, *Two-cover descent on hyperelliptic curves*, Math. Comp.
78 (2009), 2347–2370,
[DOI](https://doi.org/10.1090/S0025-5718-09-02255-8),
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 4, Lemma 4.4 and its proof, printed pp.7–8: a principal unit
1+c with v(c)>v(4)=2v(2) is a square, by the strict Hensel inequality
for T^2-(1+c) at T=1. This is an imported general square test. Our
specialization needs v_J(c)>=67, since v_J(2)=33. Modulo 8O_J has
precision 99 and therefore determines every required digit through
66. A change of unit lift modulo eight multiplies it by a principal
unit of valuation at least 99, so its square class is unchanged.
For the eventual LocalImage disk calculation over H, the separate
base quantity is v_H(4)=22, not 66 or the rational value two.

Every unit q has the form 1+z with v_J(z)>=1, except q=1, which
is immediate. Put m=v_J(z). For the possible leading term of q^2-1,

    q^2-1=2z+z^2.

If m<33, its valuation is 2m, even and strictly below 66. If m>33,
its valuation is 33+m>66. If m=33, both summands have valuation 66;
their leading residues are both one in F2 and cancel, giving
valuation at least 67 (or zero difference). Consequently a unit
whose difference from one has odd valuation below 66, or valuation
exactly 66, is NOT a square. This checks the boundary digit explicitly;
discarding digit 66 would lose one square-class direction.

### Complete unit digit elimination

Let I={1,3,...,65,66} and g_n=1+rho^n for n in I. Start from an
arbitrary unit a and residual r=a. Process n=1,...,66 in increasing
order, maintaining v_J(r-1)>=n. If v_J(r-1)>n, do nothing. If the
valuation is n, its leading residue is one, and perform one of these
two operations:

* If n is odd or n=66, replace r by r/g_n and record g_n.
* If n is even and n<66, replace r by r/(1+rho^(n/2))^2 and record
  the square-root factor 1+rho^(n/2).

In the second case n/2<=32, and the preceding leading-term calculation
shows that (1+rho^(n/2))^2-1 has valuation exactly n. In both cases
the leading residue cancels, so the new residual satisfies
v_J(r-1)>=n+1. This induction proves termination with

    a = (product of recorded g_n) * q^2 * r,
    v_J(r-1)>=67,

for a unit q. The residual is a square by the imported neighborhood
fact. Hence the 34 units generate all unit square classes. This is
an effective specialization of square comparison needed by the
approved algorithm, not a replacement proof of LocalImage.

For independence, a nonempty product of distinct g_n has its
difference from one of valuation equal to the smallest chosen n:
every other term has larger valuation. That minimum is odd below
66, or is 66, so the product is not a square by the preceding
criterion. Thus the 34 generators are independent. Every class has
exactly one recorded subset; labels add by bitwise XOR, since a
repeated generator contributes its square. This proves the algorithm
for every unit, not just the checked examples. For arbitrary field
elements, valuation parity is necessary for a square. Dividing an
even valuation by the corresponding square power of rho reduces
the question to this unit criterion. Thus J*/J*^2 has dimension 35,
including its valuation direction.

### Exact implementation and verification boundary

Run `python3 scripts/ramified-dyadic-image/check_arithmetic.py`.
The full [certificate](../scripts/ramified-dyadic-image/arithmetic-certificate.json)
contains the exact generator maps, 34 basis-unit records, 33 explicit
square-root examples, every digit eliminator, and complete residual,
representative and square-root factors for each tested normal form.
All 79 checks pass, with no failures. The exact coordinate, precision
and complete check fields were inspected, together with the selected
fixed-element normal forms. No finite enumeration of all units is
claimed or needed: completeness is the digit induction above.

The implementation indexes pi^i*rho^j by 3i+j. Its multiplication
table is exact integer reduction by R and pi^11=2 before reduction
modulo eight. It computes unit inverses by seven Newton steps
b -> b*(2-a*b). Initially v_J(1-a)>=1, and each step squares the
error, so the final error has valuation at least 128>=99. The script
also verifies the product is exactly one in O_J/8O_J. Each recorded
digit operation checks its increased valuation and the final
reconstruction a=p*q^2*r modulo eight. These checks verify the
implementation of the proven normal form, not just output counts.

The inherited units u=1-s and h=5-theta, and their product, have
labels {11}, {55,66}, and {11,55,66}, respectively, where the entries
are the selected generator exponents, consistent with the rational
comparison in L071.
Only h is already supplied there as a point image; these comparisons
give no new point-image generator. No elliptic disk was processed.
In particular, the 34-bit ambient coordinates are NOT a Kummer-image
membership test until the point-image subspace is certified.

For the pending image check, import Barrera Salazar–Pacetti–Tornaria,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020, Lemma 1.3, printed p.4. Its arbitrary finite
base-field formula is |E(H)/2E(H)|=[O_H:2O_H]*|E(H)[2]|.
Here g remains irreducible over H because J is the entire field of
degree three. Hence E(H)[2]={O}, [O_H:2O_H]=2^11, and the required
image cardinality is 2048. This is an imported completeness check;
it supplies neither representatives nor terminal disks. The original
full LocalImage target remains unfinished, with zero terminal disks
certified in this step. Global independence from L077 and L074's
localized class contribution remain independent gaps. This is local
progress reproducing assessed methods, without a novelty claim.

### Independent critical audit — 2026-10-16

The approved complete-certificate audit confirms this arithmetic input.
The Eisenstein coefficients have H-valuations 1,19,4; hence the cited
maximal-ring theorem applies over the complete DVR O_H. The exact maps
rho*s=pi^4 and 484*(s−1)=−92−62*theta+3*theta² are checked in both
polynomial presentations. They retain the fixed generator and entire
cubic, with inverse maps, rather than just a root in a possibly larger
algebra. L069's coordinate identity is exact and disc(g)=−256*11^5
is nonzero. The coprime-degree argument of L076 retains all 33 degrees.

The valuation formula is valid because the 33 basis weights are distinct
modulo 33, including for rational coefficients. It proves coefficient
integrality and the precision 99. For any square unit its root is a unit;
writing that root as 1+z exhausts the residue field F2. At v_J(z)=33,
the leading residues of 2z and z² cancel, so valuation 66 cannot occur
for the difference of a square unit and 1. This verifies the often
problematic last digit. At every smaller even digit the eliminator is
an actual square, while the earliest digit of a nonempty class-generator
product is a forbidden square digit. Generation, independence and
uniqueness of labels therefore follow without numerical assumptions.

An independent implementation, using H-polynomial convolution followed
by cubic reduction, imports no construction or replay module. Run

    python3 scripts/ramified-dyadic-image/audit_complete_certificate.py

It checks exact identities with arbitrary-size integers and all stored
34 generator, 33 square, four fixed-element and 66 eliminator witnesses.
Modular inputs are reduced before multiplication; all intermediate
integer values are below 10^9, within the int64 bound. The inverse and
normal-form reconstruction identities are checked independently, not
accepted from stored success flags. For class certification, a complete
square-factor/residual identity suffices; ancillary digit traces are
not treated as independent evidence. The strict residual bound exceeds
66 in every checked normal form. General Eisenstein, Hensel and Kummer
results remain the precise cited imports above, not new theorems.

The separate [audit certificate](../scripts/ramified-dyadic-image/complete-independent-audit.json)
records 23/23 aggregate checks, no failures, input hashes and complete
coverage totals for L078–L081. Every load-bearing record is processed;
the report contains summaries, not a claim that its summaries alone
prove the mathematics. No constructor artifact is overwritten. This
confirms the arithmetic and abstract cardinality input, without any
global restriction, class-group or integer conclusion.

## Mathlib

Full matching maximal-ring presentation, explicit 34-bit class basis,
implemented digit reduction and elliptic local-image specialization:
**not checked**. Supporting Eisenstein, complete discrete valuation,
strict Hensel, finite-extension and square-class declarations:
**not checked**. Unknown coverage is not evidence of absence.
