# L083 — The fixed canonical point fails the primitive dyadic two-descent test

## Hypotheses

Use L062's degree-twelve canonical fiber Z of L034's modular map on

    E0: y²+y=x³−x²−10x−20

at s0=9261/8. Fix exactly L062's Q-algebra isomorphism
sigma:O(Z) -> K and its point P_sigma in E0(K). No primitive
integer solution is assumed. Let beta_sigma=delta_2(P_sigma), where
L069's origin-preserving coordinates X=4x, Y=8y+4 identify E0 with

    Y²=g(X),       g(X)=X³−4X²−160X−1264.

The distinguished generator theta is the image of X in K[X]/(g).
This delta_2 is the two-descent map, distinct from L062's
five-isogeny connecting map and its class alpha_sigma.

Use L046's fixed entire dyadic algebra A2=Q2 × H, where
H=Q2(pi), pi^11=2, and the entire cubic fields

    C=Q2[theta],       J=H[theta].

Keep the same theta in both fields, with L071's cubic coordinate
and L078's maximal-ring identification. In particular

    v_C(2)=3, v_C(theta)=4,
    v_J(2)=33, v_J(pi)=3, v_J(theta)=44.

Use audited L082's primitive whole-fiber image

    I_prim={(1,1),(1,xi)},
    xi=[eta],       eta=64+4pi^5+4pi^10−theta.

Its primitive domain has b odd, c even and a=7 modulo eight, with
one common nonzero primitive triple in Z2 satisfying both power/scalar
identities. We do not assume that s0 belongs to that domain.

## Conclusion

Localizing the SAME P_sigma at two gives a pair (P0,P1) with

    loc_2(beta_sigma)=(1,[64+4z−theta]),

where z=pi³w and w is the unique unit root of the integral polynomial
Q defined below. The ramified class is different from both 1 and xi.
Thus

    loc_2(beta_sigma) not in I_prim.

This excludes one actual global two-descent point class from the
primitive dyadic test. It does not exclude the 54a1 branch, compute a
rank, determine a supported-unit dimension or localized class kernel,
or supply an integer solution. L062's different five-isogeny class
and its established memberships are unchanged. The independent critical
application review below confirms this exclusion without correction.

## Proof

### Imported methods and reason for this specialization

The saved SPECIALIZE assessment is
`drafts/literature/2026-10-17-canonical-point-primitive-dyadic-test.md`.
The complete modular map and elimination/reconstruction identities
are L033–L034's audited inputs from Freitas–Naskręcki–Stoll,
*The generalized Fermat equation with exponents 2, 3, n*, Compositio
Math. 156 (2020), 77–113,
[final author manuscript, June 10, 2019](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, pp.25–27, including (7.4). L062 supplies the canonical
fiber and fixed sigma before any GRH-dependent Selmer calculation.
No restricted scalar-constancy theorem from FNS is applied to s0.

Use the general-field Kummer injection and affine evaluation X−theta
from Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic
twists of elliptic curves*,
[arXiv:2001.02263v3, September 17, 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1, p.3. Its hypotheses are a field of characteristic different
from two and a monic square-free cubic. They hold over K, Q2 and H:
disc(g)=−256·11^5 is nonzero. L069 gives precisely the stated
origin-preserving coordinate change. Nonvanishing of both affine
evaluations is checked below; there is no primitive-scalar premise.

Use Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, p.58, for certified Hensel existence and uniqueness.
The two normalized equations below are integral with unit derivative
at the residue root one, so they satisfy its strict inequality.
Use the strict square-neighborhood consequence in Bruin–Stoll,
*Two-cover descent on hyperelliptic curves*, Math. Comp. 78 (2009),
2347–2370, [March 14, 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 4, Lemma 4.4 and proof, pp.7–8: a unit 1+u is square
when v(u)>2v(2). For nonsquareness use L078's proved complementary
criterion: a unit whose difference from one has odd valuation below
2v_J(2)=66 is not square. No general descent or square-test reproof
is needed. The specialization required here is reconstruction of the
fixed fiber and two exact class comparisons, which the sources do
not themselves decide.

### Reconstructing the entire fixed fiber

Write L034's modular polynomials as a0,b0 and set

    h(x)=x^4−52820x³+1333262x²+4971236x+9789217,
    B(z)=(2a0−b0)(16+z),       A(z)=h(16+z)^3.

Then A is monic integral of degree twelve and B is integral of
degree eleven. Its constant coefficient B0 is odd. Indeed translation
by sixteen preserves constant parity and
(2a0−b0)(0)=−104748564078368391 is odd. These are exact source
coefficient facts, also checked in L082's audit. L034's necessary
monic fiber relation becomes

    F(16+z,s0)=A(z)+s0 B(z)−s0² z^11=sum C_i z^i.

Put beta=9261, so s0=beta/8 and beta is odd. Integrality, the
degrees and B0 odd give

    v2(C0)=−3,
    v2(C_i)>=−3 for 1<=i<=10,
    v2(C11)=−6,       C12=1.                       (1)

The constant term has the uniquely smallest summand s0 B0, of
valuation −3; the degree-eleven term has the uniquely smallest
summand −s0², of valuation −6. This proves all bounds in (1)
without an approximate root calculation.

For the rational root put z=(64U)^−1. Multiplication by (64U)^12
gives the integral polynomial

    R(U)=sum_(i=0)^12 C_(12−i) 64^i U^i.

Its constant is one, its linear coefficient is odd, and for i>=2
its coefficient has valuation at least 6i−3>=9. Thus R reduces to
1+U. The residue root one has unit derivative; Hensel gives a
unique unit U0 in Z2 and hence z0=(64U0)^−1, with

    v2(z0)=−6,       x0=16+z0,       v2(x0)=−6.

For the ramified root put z=pi³W and multiply F by eight. Since
pi^33=8, the normalized equation is exactly

    Q(W)=[8A(pi³W)+beta B(pi³W)−beta² W^11]
          /[8A0+beta B0].                         (2)

The denominator is a rational odd unit. All coefficients are
integral over O_H, and reduction modulo pi gives 1+W^11. The
only residue unit is one and its derivative is eleven, a unit.
Hensel therefore gives a unique unit w in O_H with Q(w)=0.
Put z=pi³w and x1=16+z. Then

    v_H(z)=3,       v2(z)=3/11,       F(x1,s0)=0.

The value 3/11 has denominator eleven in lowest terms, so the
ramification index of Q2(z)/Q2 is divisible by eleven. Since
Q2(z) is a subfield of H, which has degree eleven, Q2(z)=H.
The same holds for x1. Its eleven distinct characteristic-zero
conjugates and the rational x0 are twelve distinct roots of the
monic degree-twelve F; the negative valuation of x0 distinguishes
it from every conjugate of x1. They exhaust the polynomial.

These roots reconstruct actual points of the entire modular fiber.
L034's b0 is monic integral of degree ten with odd constant. At x1
we have v2(x1)=3/11>0, so b0(x1) is a unit; the same holds for
all its conjugates. At x0 the monic degree-ten term of b0 has
uniquely smallest valuation −60, hence b0(x0) is nonzero. Both
z0 and z, and all conjugates, are nonzero. The exact formula

    y=(s0(x−16)^11−a0(x))/b0(x)

therefore reconstructs y in each root field. L034's elimination
identity proves y²+y=x³−x²−10x−20 and j(x,y)=s0 at every root.
There are twelve distinct points and the full map has degree twelve,
so they exhaust the scheme-theoretic fiber. No pole, removable chart
or multiplicity is missing. In particular x=16 is not encountered;
its finite removable value is −121, different from s0. The poles
O and 3T lie above infinity. We have proved

    O(Z) tensor Q2 is isomorphic to Q2 × H

by reconstruction at this scalar, independently of L082's
primitive-scalar formulas.

### Why these are the localizations of the same fixed point

The fixed map sigma tensor 1 identifies this entire fiber algebra
with K tensor Q2. Affine base change is tensor product by
[Stacks Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ).
Thus its tautological point is exactly loc_2(P_sigma). Polynomial
evaluation of X−theta commutes with these maps and with adjoining
the same theta; it gives loc_2(beta_sigma), rather than a new class
chosen after localization.

There is no alternative identification affecting our computed pair.
The rational and degree-eleven factors have different dimensions and
cannot be permuted. L082's field-only automorphism argument gives
Aut_Q2(H)={1}: an automorphism sends pi to pi times an eleventh
root of unity; that unit reduces to one in F2 and the simple-root
uniqueness for V^11−1 forces it to be one. This argument does not
require any scalar condition. Hence the reconstructed entire-fiber
isomorphism and sigma tensor 1, followed by the fixed A2
identification, agree. The rational root x0 and ramified root x1
are the coordinates of that one localized point, not independently
chosen local witnesses. We have not changed theta by a cubic
automorphism.

### Rational component: a strict square certificate

At P0 the curve equation and v2(x0)=−6 force v2(y0)=−9:
the uniquely smallest term on the right is x0³, of valuation −18,
and y0 must have negative valuation, making y0² uniquely smallest
on the left. Put

    t=−x0/y0,       v=1/(x0 t²).

Then v2(t)=3 and v is a rational unit. Direct substitution in the
original curve equation gives the exact parameter identity

    v−1+t²v+(10t⁴−t³)v²+20t⁶v³=0.

Its terms after v−1 have valuations at least 6,9,20,
respectively, so v2(v−1)>=6. Multiplying 4x0−theta by the
nonzero square (tv/2)² gives

    q=v−(theta/4)t²v².

In C the two error terms in q−1 have valuations at least
18 and 4−6+18=16. Consequently

    v_C(q−1)>=16>6=2v_C(2).

The strict square-neighborhood theorem makes q square in C, hence
[4x0−theta]=1. The affine evaluation is nonzero, since
v_C(4x0)=−12 differs from v_C(theta)=4. This is an exact bound
for the Hensel point, not the class of a finite approximation.

### Ramified component: two exact nonsquare comparisons

Put kappa=64−theta. L082 proves that kappa is square in J and
v_J(kappa)=44. Its square class is also directly certified by
3T=(16,60)=2(4T) and the Kummer homomorphism. This torsion point
is used only for its square class, not as our finite-fiber point.
At P1, x1=16+z, so the Kummer value is

    nu=64+4z−theta=kappa+4z.

Because v_J(z)=3v_H(z)=9, we have

    v_J(4z)=66+9=75>44,
    v_J(nu)=44,       v_J(nu/kappa−1)=75−44=31.   (3)

Thus nu is nonzero, and nu/kappa is a unit whose difference from
one has odd valuation 31<66. L078's exact obstruction makes this
ratio nonsquare. Since kappa is square, [nu] is not 1.

For the other allowed class, use precisely L082's representative
eta=kappa+4pi^5+4pi^10 in the same fixed J. The perturbation to
kappa has valuation 66+15=81, so v_J(eta)=44. Moreover
v_J(z)=9, whereas v_J(pi^5)=15 and v_J(pi^10)=30. The minimum
is unique, giving

    v_J(z−pi^5−pi^10)=9,
    v_J(nu/eta−1)=66+9−44=31<66.                (4)

Again the ratio is a unit with odd leading valuation, so it is
nonsquare. Hence [nu] differs from xi. Equations (3)–(4) are
complete nonsquare certificates with exact valuations; no root
truncation, insufficient-precision inference or numerical label
comparison is involved. Both affine evaluations are now certified
nonzero, justifying the ordinary Kummer formula throughout.

### Scope and stopping decision

The rational component is 1 and the ramified component is neither
allowed class. This proves the asserted exclusion and meets the
single-witness stopping test. The achieved strict square bound is
16>6; both nonsquare comparisons have exact odd valuation 31<66.
All twelve fiber points and the unique whole identification are
accounted for. No mathematical script or finite approximation was
needed for these symbolic certificates.

This result specializes the assessed general methods; it is local
progress in the notebook and makes no claim of novelty beyond the
sources checked. It gives no independent additional unit direction
beyond L077's restrictions, no reduction of the supported-unit upper
bound fourteen to eleven, and no computation of localized class
contributions. Other global point classes and primitive integer
lifting remain unresolved. L062/L065's five-isogeny survivor is a
different class under a different map and is not contradicted.
The independent critical review below confirms the exclusion; there
is no complete Beal candidate.

### Independent critical application audit — 2026-10-17

The pre-existing SPECIALIZE audit assessment covers precisely this
fixed point, both full local factors and the two comparisons. This
independent symbolic audit confirms the conclusion without a correction
or an additional mathematical input. The source theorems remain cited
imports; the following checks concern their specialized application.

**Coefficient and Hensel checks.** Read the complete a0 coefficients
and both degree-five factors of b0 from L034's canonical polynomial
transcription. They are integral; a0 has degree eleven and leading
coefficient 743, while b0 is monic of degree ten and both its factors
have odd constants. Thus 2a0−b0 has degree eleven and odd constant.
Translation by sixteen leaves that constant odd. The displayed h is
monic integral of degree four. Consequently A is monic integral of
degree twelve, B is integral of degree eleven with B0 odd, and the
terms of C0 have valuations at least zero and exactly −3. For each
of the TEN indices 1 through 10 the two terms have valuations at
least zero and at least −3. At index eleven the extra term −s0² has
valuation −6, strictly below the other two; index twelve is exactly
one. This verifies all thirteen bounds in (1), without a sampled
unit part or an approximate coefficient.

In R the coefficients at degrees zero and one are 1 and 64C11,
both units. At every degree i from 2 through 12 the coefficient
valuation is at least 6i−3>=9. Hence R is integral over Z2 and
reduces to 1+U with derivative one. Its unique unit root gives
v2(z0)=−6. Substituting z=pi³W and multiplying F by eight gives
exactly the numerator of (2): the potentially fractional term is
−(beta²/8)pi^33 W^11=−beta² W^11. The denominator is odd.
Modulo pi, the A term vanishes and only B0 survives from B, so
Q reduces to 1+W^11. Its residue-unit root is one and its derivative
is 11=1 in F2. Both polynomials therefore satisfy Clark's integral,
complete-field and strict simple-root hypotheses. No primitive-scalar
hypothesis of L082 is needed for either lift.

**Entire fiber and fixed point.** For the ramified root,
v2(z)=3/11. The value group of Q2(z) thus forces its ramification
index to be divisible by eleven; inclusion in the degree-eleven H
forces Q2(z)=H. Characteristic zero gives eleven distinct conjugates,
all of valuation 3/11. Together with z0 of valuation −6 they exhaust
the monic degree-twelve polynomial. Since v2(x1)=3/11, b0(x1)
is a unit. At x0 the uniquely minimal term of monic b0 is x0^10,
of valuation −60. Thus b0 and x−16 are nonzero at every root.
Substitution into L034's exact identity

    (s0 d−a0)^2+b0(s0 d−a0)−b0²(x³−x²−10x−20)=−d F(x,s0)

proves the reconstructed curve equation; division by d proves the
modular equation. Distinct x values give distinct points. The finite
map between smooth projective curves is flat of degree twelve, as
used in L034, so these twelve geometric points exhaust its fiber
length, with multiplicity one at each. Neither a hidden factor nor
an exceptional chart remains: x=16 is absent and O,3T are poles.

The reconstruction gives an isomorphism from the entire fiber
algebra to Q2 × H. Its comparison with the localization of L062's
fixed sigma is an automorphism of that product. Factor degrees one
and eleven prevent permutation. Every Q2-automorphism of H sends
pi to pi times an eleventh root of unity. That root is a unit with
residue one; the unit derivative of V^11−1 makes its lift uniquely
one. Thus the product automorphism is identity. This verifies that
we computed the actual localized P_sigma, not a substitute point.
The extension to the cubic algebras sends the polynomial generator
to the same theta. L069's coordinate change is origin preserving,
g is square-free in characteristic zero, and its evaluation commutes
with this tensor-product identification. The general-field BPT
Kummer formula is therefore applicable once nonvanishing is checked.

**Rational square.** The right side of the curve equation at x0 has
unique minimum valuation −18. This forces v2(y0)=−9. Hence
v2(t)=3 and v2(v)=0. Substituting x=1/(vt²), y=−1/(vt³), and
multiplying the curve equation by v³t⁶ gives exactly the parameter
identity in the proof. Its three error terms have valuations at
least 6,9,20, so v2(v−1)>=6. L071's formula
28−26s+6s² for theta has term valuations 6,4,5 in C, giving
v_C(theta)=4. The normalization by (tv/2)² is a nonzero square
and gives q exactly. Its two errors have valuations at least 18
and 16, proving v_C(q−1)>=16>2v_C(2)=6. The strict square
criterion applies. Also v_C(4x0)=−12 differs from 4, so the
evaluation is nonzero, independently of the square test.

**Two ramified nonsquares.** In the fixed J, v_J(2)=33,
v_J(pi)=3 and v_J(theta)=44; the last value also follows directly
from L078's theta formula, whose three term valuations are 132,88,44.
Thus v_J(kappa)=44. The exact order-five identity 3T=2(4T), the
nonzero evaluation at 3T and the Kummer homomorphism make kappa
a square. This uses no primitive-point or finite-scalar assumption.
Now v_J(z)=9, so nu has valuation 44 and
v_J(nu/kappa−1)=66+9−44=31. Similarly eta has valuation 44,
since its perturbation of kappa has valuation 81. The valuations
of z,pi^5,pi^10 are respectively 9,15,30, with unique minimum,
so v_J(nu/eta−1)=31 exactly. Both denominators and nu are nonzero.
Both ratios are units. L078's proof applies: for any unit square
(1+u)^2, v_J(2u+u²) is even when below 66, and cannot be the
odd value 31. Hence neither ratio is square. This verifies both
comparisons against the fixed representative, not merely inequality
of scalar domains or failure of a sufficient square test.

The rational class is identity and the ramified class is outside
both allowed classes. The audit therefore secures exactly L083's
fixed-point exclusion. Its eight direct DAG inputs match the uses
above; there is no dependency on a rank bound, class-kernel value,
unit independence or primitive integer lift. No finite-precision
computation or mathematical script is needed for these exact symbolic
certificates. The argument, supported-unit upper bound fourteen and
remaining global gaps are unchanged; the five-isogeny survivor is
unaffected. This is verified local specialization of known methods,
not a claimed advance beyond the sources checked.

## Mathlib

Full matching fixed-canonical-point exclusion and its reconstruction:
**not checked**. Supporting general Kummer, tensor-product base
change, Hensel, valuation and square-neighborhood declarations:
**not checked**. Unknown coverage is not absence. The precise cited
inputs and canonical field identifications above are retained.
