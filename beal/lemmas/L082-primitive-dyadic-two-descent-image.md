# L082 — Exact primitive dyadic whole-fiber two-descent image

## Hypotheses

Use L033's curve E0: y²+y=x³−x²−10x−20, its order-five point
T=(5,5), L034's complete modular map j, and L046's entire algebra

    A2=K tensor Q2 = Q2 × H,     H=Q2(pi), pi^11=2.

Fix this identification and L069's cubic Kummer map delta_2, whose
finite-point value is [4x−theta]. Put

    g(X)=X³−4X²−160X−1264,
    C=Q2[theta]=Q2[X]/(g),     J=H[theta]=H[X]/(g).

These are the entire fields of L071 and L078, with the same distinguished
theta, not chosen factors. In L078's coordinates,

    rho³−3pi⁴rho²+2pi⁸rho−pi=0,
    theta=−16+12pi⁷rho−2pi³rho²,
    v_J(rho)=1, v_J(pi)=3, v_J(2)=33, v_J(theta)=44.

Thus delta_2 on E0(A2) takes values in C*/C*² × J*/J*².
Let I_prim consist of its values on the tautological points supplied
by every Q2-algebra isomorphism B_s -> A2, where B_s is the WHOLE
fiber of j at a finite s, and there exist common nonzero a,b,c in Z2
with

    a³+b⁴=c^11,       s c^11=1728 a³,
    min(v2(a),v2(b),v2(c))=0,
    b odd, c even, a=7 mod 8.

These are precisely the primitive dyadic conditions of L032's 54a1
row; no condition at three, positivity over Q2, global point, global
class-group calculation, rank bound or GRH is assumed.

## Conclusion

The exact scalar domain is

    D_prim = {s in Q2 : v2(s)=6−11n for an integer n>=1}.

For EVERY such s the whole fiber B_s is isomorphic to Q2 × H.
Its identification with the fixed A2 is unique. Put

    kappa=64−theta,
    xi=[64+4pi^5+4pi^10−theta] in J*/J*².

Then kappa is a square in J, xi is nontrivial, and the exact set is

    I_prim = {(1,1), (1,xi)}.

For every allowed s, its class is (1,xi) when v2(s)=−5 (n=1),
and (1,1) when n>=2. Both classes have exact nonzero-scalar,
common-primitive-witness, whole-fiber realizations: s=2^−5 and
s=2^−16 respectively. The displayed xi is an explicit algebraic
representative in the fixed J; no unspecified root or numerical
approximation is part of its definition.

Its ramified projection has size two, strictly less than L079's full
2048-class image. This is an exact additional restriction relative to
unrestricted local points. It does not decide whether primitivity
shrinks the set already imposed by arbitrary whole-fiber compatibility,
nor establish independence from any global restriction. The set happens
to be an order-two subgroup because it is exactly the two classes
displayed, not because restricted images were assumed to be subgroups.
No filtered global dimension, rank or integer exclusion follows.
The independent critical review below confirms this specialization.

## Proof

### Imported methods and the specialization being made

The complete modular map, its degree twelve, polynomial elimination
identity, and torsion coordinates are the audited inputs L033–L034.
Their primary source is Freitas–Naskręcki–Stoll, *The generalized Fermat
equation with exponents 2, 3, n*, Compositio Math. **156** (2020),
77–113, [final author manuscript, June 10, 2019](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, pp.25–27, especially (7.4). Neither the GRH-dependent
Selmer data nor the global cusp elimination is used. The source's
non-cusp constancy lemma excludes this domain; the argument here uses
the assessed alternative of uniform square neighborhoods directly.

Use the simple-root Hensel theorem from Pete L. Clark, *Algebraic
Number Theory II: Valuations, Local Fields and Adeles*,
[inspected 161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.75 and Corollary 1.77, p.57, and Theorem 1.79, p.58,
for uniqueness and the strict residual/derivative estimate. All simple-root
applications below have integral coefficients and unit derivative over
the stated complete local field; the square-neighborhood applications
instead use the strict inequality with derivative two. Use the monic-cubic Kummer
homomorphism, including its origin evaluation, from Denis Simon,
*Computing the rank of elliptic curves over number fields*, LMS J.
Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Section 1.1,
Propositions 1.1–1.2, p.8, for the number-field formulation used in
L069. For its required local-field scope use Barrera Salazar–Pacetti–
Tornaría, *On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3, September 17, 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1, p.3: the Kummer injection for a monic square-free cubic over
any field of characteristic different from two. Both Q2 and H satisfy
this hypothesis, and g has nonzero discriminant −256·11^5. The
origin-preserving change X=4x, Y=8y+4 identifies the stated curve
with Y²=g(X), so its affine evaluation is exactly [4x−theta].
The strict square-neighborhood fact is the Hensel input used in
Bruin–Stoll, *Two-cover descent on hyperelliptic curves*, Math. Comp.
**78** (2009), 2347–2370,
[author manuscript, 14 March 2008](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 4, Lemma 4.4 and proof, pp.7–8: 1+u is square if
v(u)>2v(2). L078 also proves that an odd valuation strictly below
2v_J(2)=66 of a unit's difference from one certifies nonsquareness.
These general inputs are cited, not reproved. What remains to derive
is the uniform scalar/fiber coverage and its precise square bounds;
the sources and the unrestricted image do not supply those conclusions.

### Exact common primitive scalar witnesses

For a permitted triple b is odd and c is even, so a³=c^11−b⁴
is odd. Put n=v2(c)>=1. Since v2(1728)=6,
v2(s)=6−11n. In particular s is nonzero and is neither 1728 nor
any finite integral scalar.

Conversely take any s with that valuation and set

    d=1728/(1728−s),       e=s/(1728−s).

Then v2(d)=11n and e is a unit. The unit d/2^(11n) has a unique
eleventh root u in Z2*: modulo two its root is one and its derivative
is eleven, a unit. Set c=2^n u and b=1. The unit e has a unique
cube root a in Z2* by the same theorem, with derivative three.
Writing w=1728/s gives v2(w)=11n and e=−1/(1−w), so e=−1 mod 8.
Every odd cube equals its base modulo eight; hence a=7 mod 8.
Now

    e+1=d=c^11,       a³=e,
    s c^11=1728 e=1728 a³.

This proves both required identities with the SAME c, b⁴=1 and
primitive nonzero coordinates. No fourth-root surjectivity is used.
It covers every unit part of s and every n>=1.

### Uniform full fibers, including all identifications

Write m=11n−6>=5 and beta=2^m s in Z2*. Use L034's integral
polynomials h,J0(x)=2a0(x)−b0(x), and d0=(x−16)^11, where
a0,b0 are modular polynomials, not the primitive coordinates above.
The necessary monic degree-twelve relation is

    F(x,s)=h(x)^3+J0(x)s−(x−16)^11 s².

Put A(z)=h(16+z)^3, B(z)=J0(16+z), and
F(16+z,s)=sum C_i z^i. The source coefficients give deg B=11,
all A_i,B_i integral, and B_0,B_1 odd. For the latter parities,
translation by the even integer sixteen preserves the constant and
linear coefficients modulo two, while

    J0(0)=−104748564078368391,
    [x]J0(x)=199736619430410535.

The degree-twelve leading coefficient of A is one. Therefore

    v2(C_0)=−m,
    v2(C_i)>=−m for 1<=i<=10,
    v2(C_11)=−2m,       C_12=1.                 (1)

Indeed C_0=A_0+s B_0 has its uniquely smallest term s B_0;
C_11=A_11+s B_11−s² has its uniquely smallest term −s².
These bounds are symbolic for all beta, not a finite sampling.

For a rational root, substitute z=(2^(2m)U)^−1 and multiply by
(2^(2m)U)^12. The resulting integral polynomial has coefficients
C_(12−i)2^(2mi). Its constant and linear coefficients are odd;
all others have valuation at least 3m>0 by (1). It reduces to
1+U, so Hensel gives a unit root and a rational z0 with

    v2(z0)=−2m,       x0=16+z0, v2(x0)=−2m.

For the degree-eleven root set z=pi^m W and divide F by C_0.
Using pi^(11m)=2^m, the normalized polynomial is exactly

    Q_beta(W) =
      [2^m A(pi^m W)+beta B(pi^m W)−beta² W^11]
      /[2^m A_0+beta B_0].                    (2)

Its denominator is a rational odd unit, all coefficients lie in O_H,
and its reduction modulo pi is 1+W^11. This has simple root one.
There is a unique unit root w_beta in O_H. Put

    z1=pi^m w_beta,        x1=16+z1.

Then v2(z1)=m/11. Because m=−6 mod 11, the denominator of this
valuation in lowest terms is eleven. Consequently Q2(z1), a subfield
of the degree-eleven field H, has ramification index divisible by
eleven and equals H. Its eleven distinct conjugates together with x0
exhaust the roots of the monic degree-twelve F.

L034's b0 is integral and monic of degree ten with odd constant
coefficient. At x1, v2(x1)>0, so b0(x1) is a unit. At x0 its
degree-ten term is uniquely smallest in valuation, so b0(x0)!=0.
The same holds at all conjugates. Both z0 and z1 are nonzero.
Thus at all twelve roots the exact formula

    y=(s(x−16)^11−a0(x))/b0(x)

reconstructs the curve and j=s, by L034's elimination identity.
The complete map has fiber length twelve; these twelve distinct
points exhaust the whole fiber, without hidden multiplicities or
omitted charts. This proves B_s=Q2 × H for every allowed s.
The poles O and 3T have no finite image, and the removable x=16
point 2T has image −121, outside this scalar domain. No limiting
cusp is substituted for a finite point.

There are no unaccounted identifications. Every automorphism of H
would send pi to pi times an eleventh root of unity. Such a root is
an integral unit reducing to one in F2; Hensel uniqueness for
U^11−1 forces it to be one. Hence Aut_Q2(H) is trivial. The
rational factor cannot be permuted with the degree-eleven factor.
Every isomorphism B_s -> A2 therefore gives the SAME pair (P0,P1)
under the fixed A2 identification. In particular independent choices
of rational and ramified scalar are never introduced.

### The rational Kummer component is always trivial

At P0, the original curve equation and v2(x0)=−2m force
v2(y0)=−3m: the terms x0³ and y0² are uniquely smallest on their
respective sides. Set t=−x0/y0, so v2(t)=m, and set
v=1/(x0 t²), an odd unit. The parameter identity of L081,
obtained by exact substitution, is

    v−1+t²v+(10t⁴−t³)v²+20t⁶v³=0.

It implies v2(v−1)>=2m. Multiplication of 4x0−theta by the
nonzero square (tv/2)² gives

    q=v−(theta/4)t²v².

In C, use the normalized valuation v_C(2)=3 of L071. The same
theta maps into J, so v_C(theta)=44/11=4. Hence

    v_C(q−1)>=min(6m,6m−2)=6m−2>=28>6=2v_C(2).

The imported strict square-neighborhood theorem makes q a square.
Thus [4x0−theta]=1. The evaluation is nonzero: 4x0 has negative
valuation, whereas theta has positive valuation. Neither O nor a
finite two-torsion exception is being evaluated by an affine formula.

### The ramified valuation tail and the one remaining annulus

First kappa=64−theta is a nonzero square in J. It is the Kummer
value at 3T=(16,60), and 3T=2(4T) in the order-five group supplied
by L033. A Kummer homomorphism kills doubles. This uses the point
only to evaluate a square class, not as a finite-scalar realization.
The displayed theta has valuation 44, while v_J(64)=198, so
v_J(kappa)=44.

At P1 the exact value is kappa+4z1, and

    v_J(4z1/kappa)=66+3m−44=22+3m.           (3)

It is always positive, so the value has valuation 44 and is nonzero.
When n>=2, m>=16 and (3) is at least 70>66. The ratio to kappa
is a square by the strict square-neighborhood theorem. This covers
the ENTIRE infinite valuation tail, with no upper bound on n.

When n=1, m=5 and (3) is 37. Since 37 is odd and below 66,
L078's square obstruction shows that the ratio to kappa is not a
square. Thus this component is nontrivial for every scalar in this
annulus. It remains to prove that all its unit parts give one class.

Take beta,beta' in Z2*. Their difference is in 2Z2. In (2) the
numerator coefficients are integral polynomials in beta and the
denominator is an odd unit; subtraction therefore shows that every
coefficient of Q_beta−Q_beta' lies in 2O_H=pi^11 O_H. Evaluating
at w_beta' gives v_H(Q_beta(w_beta'))>=11. For any two units U,V,
the divided difference (Q_beta(U)−Q_beta(V))/(U−V) is a unit:
its reduction is the divided difference of W^11+1 at U=V=1,
namely eleven=1 in F2. Consequently

    v_H(w_beta−w_beta')>=11,
    v_H(z1(beta)−z1(beta'))>=m+11.

At m=5 the ratio of the two Kummer values therefore differs from
one by valuation at least

    66+3(5+11)−44=70>66.                    (4)

This proves square-class constancy on ALL odd beta, retaining the
fixed H identification. It is stronger than testing finitely many
unit residues, and does not assume the points themselves are equal.

### An explicit class representative and both exact realizations

Choose s*=2^−5, so m=5 and beta=1. Let w* be the exact unit root
of (2). We need its approximation only to prove equality with the
displayed explicit class, not to establish existence of a point.
Modulo pi^10 the factor 2^5 A vanishes, the denominator of (2) is
one, and

    B(pi^5 W)=1+pi^5 W mod pi^10.

This uses the proved odd B_0,B_1 and integrality of all higher
coefficients; every rational odd integer is one modulo pi^10
because 2=pi^11. For W0=1+pi^5, binomial expansion gives
W0^11=1+pi^5 mod pi^10. Hence Q_1(W0)=0 mod pi^10.
The unit divided-difference property above implies

    w*=1+pi^5 mod pi^10,
    z1(s*)=pi^5+pi^10 mod pi^15.

The ratio of kappa+4z1(s*) to kappa+4pi^5+4pi^10 differs from
one by J-valuation at least

    66+3*15−44=67>66.                       (5)

Thus its square class is exactly xi as defined in the conclusion.
Moreover v_J(4(pi^5+pi^10)/kappa)=37, so the same odd-valuation
test proves directly that this explicit xi is nontrivial.
The precision in (5) is STRICT; equality with 66 would not suffice.

The scalar-witness construction and the two Hensel lifts above at
s=2^−5 give an actual permitted whole fiber of class (1,xi).
At s=2^−16 they give an actual permitted whole fiber of class (1,1).
In both cases c, a and both elliptic points are exact Hensel roots,
all are in the required fields, and b=1. In particular neither class
is represented only by the excluded cusp parameter zero. Necessity
of the scalar domain and the uniform class proofs exhaust every
permitted triple and every whole-fiber identification. This proves
the asserted two-element set.

### Scope, verification and remaining gap

The proof uses exact coefficient parities and uniform inequalities;
no mathematical script, sampled scalar list or truncated root is
needed. The load-bearing bounds are 28>6 for the rational component,
70>66 for the tail and unit variation, 67>66 for the explicit
representative, and the odd obstruction 37<66 for nontriviality.
The complete fiber degrees are 1+11=12 for every allowed scalar.
L079 supplies the separate full ramified comparison of 2048 classes;
the actual restricted projection has two. The strict local reduction
does not itself remove an independent global direction or change
L077's supported-unit upper bound fourteen versus desired eleven.
The localized class contribution and integer power lifting remain
unresolved. This is a specialization of the assessed methods, with
no claim of novelty beyond the sources checked and no Beal candidate.

### Independent critical audit — 2026-10-17

This audit confirms the exact statement without changing its scalar
domain, representative or cardinality. It corrects the method citations
above: Clark Theorem 1.79 supplies uniqueness; BPT Section 1 explicitly
supplies local-field Kummer scope. Simon's number-field statement alone
is not used as a local theorem. The ready audit assessment had already
inspected both sources. No new general theorem is asserted here.

For scalar sufficiency, the two defined values satisfy d−e=1 exactly.
Their valuations are 11n and zero, respectively; after removing
2^(11n), both root equations are unit equations with odd derivative.
Odd roots are unique because there is only one nonzero residue in F2.
As 11n>=11, e=−1 modulo eight. Thus b=1, a³=e and c^11=d
give the same c in both identities, nonzero primitive coordinates and
a=7 modulo eight. Conversely b odd and c even force a odd and the
claimed valuation of s. No permitted scalar is zero or integral.

The coefficient hypotheses can be verified without a numerical root
or a sampled beta. In L034's complete b=b1*b2, both degree-five
factors are monic with odd constants; their linear coefficients are
271927184 (even) and −37789861 (odd). Hence b has odd constant
and linear coefficients. Since J0=2a0−b, J0 also has odd constant
and linear coefficients. Translation by sixteen preserves these
parities. The polynomial h is monic integral of degree four, so
A=h(16+z)^3 is monic integral of degree twelve; B is integral of
degree eleven. These facts independently imply all thirteen bounds
(1), including the unique −m constant term and −2m degree-eleven
term. They justify (2) by exact substitution, with odd denominator.

For the rational reciprocal polynomial, the coefficient of U^i is
C_(12−i)*2^(2mi). Its first two coefficients are units, while for
every i>=2 its valuation is at least (2i−1)m>=3m. Thus it has
exact reduction 1+U. For Q_beta, the reduction is exactly 1+W^11:
2^m A vanishes, only B's constant survives, and beta and that
constant reduce to one. The derivative at the unique residue unit
is one. Both Hensel applications therefore meet the cited complete,
integral, simple-root hypotheses. Since gcd(m,11)=1, the ramified
root has degree eleven over Q2; characteristic zero gives eleven
distinct conjugates. The rational root has valuation −2m, distinct
from the other roots' m/11, so all twelve roots are accounted for.

At the ramified roots x=16+z is integral of strictly positive
valuation, making b(x) a unit. At the rational root, its negative
valuation makes the monic degree-ten term of b uniquely minimal.
Thus b and x−16 are nonzero at every root. L034's exact identity
then reconstructs y and j, giving twelve distinct curve points.
Their number equals the full degree of the map, so no further
component or multiplicity remains. The excluded poles and removable
x=16 chart cannot supply extra finite points here. Aut_Q2(H) is
trivial: any eleventh root of unity in H reduces to one, whose lift
under U^11−1 is uniquely one. Distinct factor dimensions prohibit
permuting the two components. This proves uniqueness for the whole
algebra identification, not just a choice of one ramified root.

For the rational component, substitution of t=−x/y into the original
equation gives exactly L081's displayed parameter polynomial. The
valuation equation 2v2(y)=3v2(x) gives v2(t)=m and v2(v)=0;
the polynomial then gives v2(v−1)>=2m. The entire rational cubic
is the Eisenstein field of L071, with v_C(2)=3. Its embedding in J
has ramification index eleven, so v_C(theta)=4. Multiplication by
(tv/2)^2 is an exact nonzero square normalization. The two error
terms have valuations at least 6m and 6m−2, proving the claimed
minimum 28>6. The affine value cannot vanish by its unequal term
valuations. This covers every rational component uniformly.

On the ramified component, 3T=2(4T) and the local Kummer homomorphism
prove that kappa is a square. Its valuation is exactly 44, since
the two terms have valuations 198 and 44. Consequently the perturbation
has exact relative valuation 22+3m. For n>=2 it is at least 70>66;
for n=1 it is exactly 37. L078's proof of the odd leading-valuation
obstruction applies to the latter unit ratio: if q is a unit, writing
q=1+z shows q²−1 has even valuation below 66 or valuation greater
than 66. Thus 37 certifies nonsquareness, not merely insufficient
precision to prove a square. The Kummer value itself stays nonzero.

For any odd beta,beta', the difference of their normalized polynomial
coefficients is in 2O_H. Indeed, subtracting the two fractions in
(2) has unit denominator and numerator divisible by beta−beta'.
At any two units the divided difference reduces to eleven=1 in F2.
If the lifted roots coincide there is nothing to prove; otherwise
this proves their difference has H-valuation at least eleven. Scaling
by pi^5 gives valuation at least sixteen for the z difference, so
the relative Kummer error is at least 66+48−44=70>66. This checks
all unit parts, without changing the fixed field identification.

For beta=1,m=5, modulo pi^10 the normalized polynomial is
1+pi^5 W−W^11. Its value at 1+pi^5 vanishes: all binomial terms
of order at least two contain pi^10, and 11 is one modulo pi^11.
The same unit divided difference gives the stated pi^10 root error
and pi^15 z error. The explicit denominator kappa+4pi^5+4pi^10
still has valuation 44, so the relative error is at least 67>66.
Its ratio to the square kappa has difference of exact valuation 37,
proving the explicit representative is nontrivial as well.

Finally n=1 and n=2, beta=1 give the two finite scalars stated in
the conclusion. The same scalar construction and complete Hensel
fibers apply at each; no class is realized only at a cusp. These
realizations and the exhaustive bounds prove the exact correlated
set. L079's independently audited size 2048 is only the unrestricted
ramified comparison and is not used to infer restricted exhaustion.
All direct mathematical inputs in the existing DAG row are retained;
no new dependency is needed. The checks above are symbolic, so no
mathematical script or numerical certificate was required. No global
unit independence, class value, rank improvement or integer conclusion
is certified by this audit.

## Mathlib

Full matching primitive scalar domain, uniform whole-fiber realization
and exact correlated two-descent image: **not checked**. Supporting
Hensel, local valuation, elliptic Kummer and square-neighborhood
declarations: **not checked**. Unknown coverage is not evidence of
absence. The exact source citations and local hypotheses above are
the inputs to this informal proof. The independent critical review above
confirms the local specialization, without a Mathlib coverage claim.
