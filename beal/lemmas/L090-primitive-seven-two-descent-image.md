# L090 — Exact primitive whole-fiber two-descent image at seven

## Hypotheses

Use L033/L034's entire degree-twelve modular map j on

    E0: y²+y=x³−x²−10x−20,

and L033's degree-twelve field K with defining polynomial m. Put
A7=K tensor_Q Q7. For s in Q7 minus {0,1728}, let B_s be the
coordinate algebra of the entire projective fiber j^(-1)(s). Include
every Q7-algebra isomorphism B_s -> A7 and its tautological point.
For the primitive image require one common nonzero a,b,c in Z7 with

    a³+b⁴=c¹¹, s=1728a³/c¹¹, min(v7(a),v7(b),v7(c))=0.

Use L069's X=4x, Y=8y+4, g(X)=X³−4X²−160X−1264 and its fixed
generator theta. The full two-descent map kappa has ordinary value
[4x−theta] in (A7[X]/g)^*/(A7[X]/g)^{*2}, without a scalar quotient,
with the standard exceptional root values and identity at O.
No integer solution, global class basis, class-kernel value, rank,
independence on T, or GRH assumption is imposed.

## Conclusion

A7 is the single unramified degree-twelve field U over Q7, and
U[X]/g=U³. Order its factors by the rational root alpha reducing to
4, followed by beta,gamma reducing to i,−i, where i²=−1 in F49.
The latter roots lie in the unramified quadratic subfield; their order
is immaterial. Let nu denote the nonsquare unit class of U. Then

    J7={1,(1,nu,nu)}

is the exact primitive whole-fiber two-descent image. It is also the
image without requiring primitive witnesses. All compatible scalars
in 2+7Z7 or 3+7Z7 give identity; every compatible scalar in 7Z7 gives
(1,nu,nu); all other scalar neighborhoods are incompatible. This is
not a classification of which scalars in 7Z7 are compatible.

The entire fibers at s=2 and s=9261/8 respectively realize the two
classes with common primitive witnesses. Consequently J7 is a subgroup
of order two, compared with four classes in the unrestricted image.
This is a local specialization of assessed known methods. It does not
establish independence on L084's T, improve either global dimension
bound, compute a localized class kernel or exclude an integer solution.
Independent critical review completed on 2026-10-18 confirms this local
result without changing its conclusion or global limitations.

## Proof

### Assessed inputs and imported theorems

This is REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-primitive-seven-two-descent-image.md`.
The inspected general results do not compute a correlated whole-fiber
image. The difference supplied here is the explicit seven-adic field,
map, residue, branch and common-witness specialization.

Import Bruin–Stoll, *Two-cover descent on hyperelliptic curves*, Math.
Comp. **78** (2009), 2347–2370,
[14 March 2008 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Remark 2.1, Section 4 Lemmas 4.3–4.4 and Section 9: the odd-degree
Kummer map has the stated ordinary and exceptional conventions.
Import Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and
quadratic twists of elliptic curves*,
[arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
Lemma 1.3, Definition 1.6, Theorem 1.8 and Corollary 1.9, pp.3–6.
At every field used here the integral monic cubic has unit discriminant
−256·11^5. Its order is maximal etale; the odd-prime hypotheses give
the full norm-square unit image. This is the unrestricted baseline,
not the assertion about shared scalars.

Use J.S. Milne, *Algebraic Number Theory*,
[v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Theorem 7.33/Remark 7.36, pp.121–123 (coprime Hensel factor lifting),
Corollary 7.42/Remark 7.43, p.124 (degree ef), Proposition 7.50 and
Example 7.54, pp.127–129 (unramified extensions). Their perfect-base
and separability hypotheses hold over these characteristic-zero local
fields and finite residue fields. For exact roots use Pete L. Clark,
*Algebraic Number Theory II*,
[161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, p.58: v(f(r))>2v(f'(r)) suffices. All root lifts below
have a genuine residue root and unit derivative. In particular a unit
in an odd-residue-characteristic local field is square exactly when
its residue is square. These general theorems are cited, not reproved.

L034 supplies the complete modular map and integer polynomial identity
from Freitas–Naskręcki–Stoll (FNS), *The generalized Fermat equation
with exponents 2,3,n*, Compositio Math. **156** (2020), 77–113,
[10 June 2019 manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, pp.25–27 and (7.4). L047 supplies the unconditional
entire rational canonical-fiber identification at j(54a1)=9261/8,
using Section 7.2 and Table 5, before the GRH-dependent computations.
No GRH-dependent Selmer dimension or classification is imported.

### Entire seven-adic algebra and unrestricted baseline

Ascending coefficient lists below are over F7. The complete reduction
of m is

    [5,3,2,6,6,6,6,0,1,6,1,0,1].

The certificate verifies x^(7^12)=x modulo mbar and
gcd(mbar,x^(7^6)−x)=gcd(mbar,x^(7^4)−x)=1. These are the full
irreducibility tests for degree twelve. Thus mbar is irreducible and
separable. The entire monic polynomial defines an unramified extension
U/Q7 of degree twelve, not a selected component; its residue field is
k=F_(7^12). Indeed the residue degree is at least twelve and ef=12
forces e=1 and f=12.

The cubic reduces as

    gbar=(X+3)(X²+1).

The second factor is irreducible over F7 since −1 is nonsquare there.
The factors and all their roots are distinct. Hensel lifts the rational
root and the two quadratic roots; the unique unramified quadratic
extension embeds in U since 2 divides 12. Hence the entire cubic
algebra is U³ with the stated generator evaluations. BPT's good-prime
equality applies: E0 also has unit discriminant −11^5. Its unrestricted
image is exactly the unit tuples whose product is square. Each factor
has two unit square classes; hence this image has four elements.

### Integral map at seven, including both exceptional coordinate charts

Write j=(A(x)+B(x)y)/d(x) using the full coefficients of L034; A,B
here are map polynomials, not primitive coordinates. Put

    d=(x−16)^11, h=x^4−52820x³+1333262x²+4971236x+9789217,
    N=A+By, N'=A−B−By, J=2A−B,
    F(x,s)=h³+Js−ds².

L034's integer identity NN'=−dh³ is checked again over Z in the
certificate. The good model is smooth over Z7 by discriminant −11^5.
On d invertible the target pair is [N:d]; on N' invertible it is
[−h³:N']; on N invertible the first pair has a unit entry and its
reciprocal is d/N. The whole x=16 locus is

    (y+61)(y−60)=0,

with difference 121 a seven-adic unit. At 2T=(16,−61) one has
N=0,N'=11^22; at 3T=(16,60) one has N=11^22,N'=0.
Both nonzero numerators remain units (residue 4), and h(16)=11^8.
Thus these opens cover the affine model. At 2T the second chart
gives j=−121, residue 5, without division by d. At 3T, x−16 is
a parameter because 2y+1=121 is a unit, and d/N has order eleven.

For completeness the origin chart is verified at seven rather than
transferring a thirteen-adic conclusion. In homogeneous coordinates
put t=−X/Y,w=−Z/Y. The exact equation is

    w U0=t³, U0=1+t²+(10t−1)w+20w².

On U0 invertible define V=U0^(-1); then w=t³V, an identity of regular
functions even at t=0. For A=sum A_i x^i and B=sum B_i x^i,
with degrees eleven and ten, clearing denominators gives

    j=Q/(tH), H=(1−16t²V)^11,
    Q=sum A_i t^(23−2i)V^(11−i)−sum B_i t^(20−2i)V^(10−i).

All exponents are nonnegative, Q(0,1)=−1 since B_10=1, and H(0,1)=1.
Thus [Q:tH] defines the map at O. Its reciprocal is
1/j=−t+O(t²) with integral coefficients, and t is a parameter since
the derivative of wU0−t³ in w is one at O. The affine opens and this
origin open cover the whole model and agree on their dense overlaps.
They give a Z7-morphism with complete reduced polar divisor O+11(3T).
The reduced degree is twelve and the simple pole at O proves
separability. No reduction or chart is lost.

If s is integral, a point over U with j=s extends to the proper good
model. Its reduction cannot be either reduced pole, since the extended
map reduces to a finite scalar. Hence it is affine with x,y integral.
The necessary identity F(x,j)=0 holds even at 2T by regular extension.

### Uniform exclusion of every nonintegral scalar

For every nonzero u in 7Z7, the origin chart and its unit linear
coefficient give a unique Q7-point reducing to O with 1/j=u, by
Hensel in the parameter chart. For v7(s)<0 take u=1/s. This point is
a Q7-point of the entire finite fiber, and gives a unital algebra map
B_s -> Q7. Such a map cannot exist if B_s is the degree-twelve field
U. This excludes all negative valuations uniformly in depth and unit
part, not merely sampled scalars. Infinity itself is not in the
finite scalar domain.

### Every regular residue disk and every identification

Here 1728 has residue 6. Exact complete factorization gives:

| s modulo 7 | Full factor degrees of Fbar(x,s) |
|---|---|
| 1 | 1,1,10 |
| 2 | 12 |
| 3 | 12 |
| 4 | 1,1,10 |
| 5 | 1,1,10 |

Every row is monic, squarefree and coprime to Bbar. At every factor
the reconstruction y=(s d−A)/B satisfies the curve equation and
N' is nonzero; the regular expression −h³/N' evaluates to s.
These are verified identities in every residue field, including the
factor x=2 at s=5, which is 2T with x=16 modulo seven. The complete
factor products, irreducibility tests and reconstructions are retained
in the certificate.

Consequently these twelve distinct reduced points are the entire
degree-twelve reduced fiber. They are simple: away from d=0 the
elimination identity identifies the fiber with F=0; at 2T use the
N' unit chart, where F=h³+s(J−sd)=0 and reconstruction gives the
same equivalence. Hensel lifts each simple point over its unramified
residue extension, uniquely for each scalar s in its disk. Its residue
degree is a lower bound on its lifted degree; the lift over that same
unramified extension attains it. The twelve lifted points exhaust
the generic degree-twelve fiber from L034. Thus the table gives the
entire local factorization throughout each disk, not just at its center.
Only residues 2 and 3 give B_s isomorphic to U, and every scalar in
these two disks does give U.

For either degree-twelve polynomial H_r=Fbar(x,r), choose the square
root I_r of −1 recorded in the certificate. Direct exponentiation
in F7[x]/H_r gives

    (chi(4x−4),chi(4x−I_r),chi(4x+I_r))=(+1,+1,+1), r=2,3.

All differences are nonzero units. Their square classes therefore
lift to identity throughout both scalar disks. Every isomorphism to
U induces one of the twelve Frobenius maps on residues. Frobenius
preserves square characters, fixes the root 4 and at most exchanges
the other two roots. The equal last entries retain every identification.
No independently selected component points are used.

### Both branch neighborhoods

At zero the complete residue identity is

    Fbar(x,0)=hbar³, hbar=[4,4,0,2,1],

and hbar is irreducible of degree four. It is coprime to Bbar,dbar
and gbar(4x). Thus every compatible point in this entire scalar
neighborhood reduces to a root of hbar in F_(7^4), with uniquely
reconstructed y; every component of 4x−theta is a unit.

In F7[x]/hbar one square root of −1 is I=[2,5,2,1]. The exact
values 4x−4,4x−I,4x+I are respectively

    [3,4], [5,6,5,6], [2,2,2,1],

whose 1200th powers are 1,−1,−1. Here 1200=(7^4−1)/2. Changing
I interchanges two equal characters; every conjugate root gives the
same ordered character triple up to that exchange. Extension to k
has odd degree three: (7^12−1)/(7^4−1)=5767203 is odd. The characters
are therefore still (+1,−1,−1) in k. Hensel square testing gives
the class (1,nu,nu) for every compatible scalar in 7Z7, at every
positive valuation and every unit part. This is only an upper-bound
argument on classes and does not assert that arbitrary repeated
branch fibers lift etale or are compatible.

At the other branch the complete identity is

    Fbar(x,6)=G²,
    G=[2,3,4,3,5,5,1]=(x+2)(x+3)(x²+x+3)(x²+6x+4).

These four factors are distinct irreducibles; the two quadratic
discriminants are 3 and 6, nonsquares modulo seven. For every
s=6 modulo seven, coprime Hensel lifting applies to their SQUARES
as four relatively prime blocks of degrees 2,2,4,4. No irreducibility
or etaleness inside a block is assumed. Also gcd(Bbar,G)=1. A
compatible point has integral x satisfying one of the four lifted
blocks, so [Q7(x):Q7]<=4. Its y=(sd−A)/B lies in Q7(x), since B(x)
is a unit. Hence the whole point has degree at most four. But an
isomorphism B_s -> U of the entire fiber makes its tautological point
have residue field U, of degree twelve: its affine coordinates generate
that coordinate algebra. This is a contradiction. Thus no scalar in
the entire 1728 residue neighborhood is compatible, uniformly even
at arbitrarily deep branch valuations.

This covers every finite scalar. All compatible points lie either
in the regular identity disks or the nontrivial zero branch, and their
differences from all three theta roots are units. Actual two-torsion
and its exceptional evaluation therefore cannot occur in a compatible
fiber. The removable x=16 coordinate is included in the incompatible
residue-five table; the origin and the other cusp lie over infinity.
There is no omitted exceptional value or uncontrolled tail in this
image upper bound.

### Common primitive domain and exact realizations

The primitive scalar domain itself has a useful exact check. Put
t=s/1728 and q=1−t, both nonzero. Such a scalar admits common primitive
witnesses exactly when either

    v7(t) in 3 Z_>=0 and v7(q) in 4 Z_>=0,

or v7(t)=v7(q) is a negative multiple of eleven. Necessity follows
because the primitive equation permits at most one coordinate with
positive valuation. If c is a unit, the two valuations are 3v7(a)
and 4v7(b); if c is not a unit, a and b are units and both valuations
are −11v7(c).

For sufficiency in the first case write v7(t)=3h,v7(q)=4k and choose
b=7^k b0 with b0 a unit. Set a³=(t/q)b⁴ and c¹¹=b⁴/q. The first
prescribed power has valuation 3h, the second zero. For any unit
eta modulo seven, some unit b0 has eta b0^4 a cube: unit fourth
powers are the squares {1,2,4}, unit cubes are {1,6}, and these
products cover every unit. Choose this residue b0 and lift the
normalized cube with its unit derivative. The eleventh-power map
is bijective on unit residues since gcd(11,6)=1, and its derivative
is a unit, so c exists. In the negative case take b=b0 a unit,
make a³=(t/q)b0⁴ a unit cube by the same choice, and lift
c¹¹=b0⁴/q of valuation 11n with n=−v7(q)/11. In both cases the
same c satisfies a³+b⁴=c¹¹ and the prescribed scalar. All coordinates
are nonzero integral and at least one is a unit. This proves
sufficiency without assuming cube or fourth-power surjectivity.
It does not decide entire-fiber compatibility in the zero branch.

For an exact identity-class realization take s=2, b=2 and

    a³=16/863, c¹¹=13824/863.

The residue roots are a=1,c=5 modulo seven; the derivatives 3a²
and 11c^10 are units. Hensel supplies exact unit roots. The rational
identities a³+16=c¹¹ and 1728a³=2c¹¹ prove the required shared
witness. The regular-fiber result above gives the whole field U,
with identity class under every isomorphism.

For the nontrivial class use s0=9261/8, a=7, and lift

    b⁴=169 with b=1 modulo seven,
    c¹¹=512 with c=1 modulo seven.

Both residue equations hold and their derivatives 4 and 11 are units.
Thus these exact unit roots exist; no square root of +13 in Q7 is
assumed. The same c gives 7³+169=512 and
1728·7³/512=9261/8. Hence the triple is nonzero, integral and
primitive, and s0 is in 7Z7. L047's rational entire-fiber identification
at j(54a1)=s0, tensoring with Q7, gives B_s0 isomorphic to the entire
A7=U. This uses a known canonical fiber, not a sampled branch lift
or an unproved identification from a necessary polynomial. Every
isomorphism gives the nontrivial diagonal class by the uniform zero
branch argument. Both upper-bound classes are therefore realized,
proving exact equality with and without the primitive restriction.

### Arithmetic evidence and qualifications

Run `python3 scripts/primitive-seven-two-descent/check_image.py`.
The full certificate is
`scripts/primitive-seven-two-descent/image-certificate.json`.
All 33 named checks pass, with no failures. It retains the entire
irreducibility Frobenius sequences and gcd tests, every regular factor
and reconstruction, complete product identities, the two branch
records, all square-character values, the x=16 charts, integer map
identity and origin coefficients, primitive unit-ratio coverage and
both exact witness records. All five complete regular rows, the
complete K and branch records and both witnesses were inspected.
Irreducibility tests verify x^(7^n)=x and the gcd test at n/ell for
every prime ell dividing n; multiplication verifies every complete
factorization. These are exact certificates, not numerical evidence.
The pure polynomial utilities are reused without executing previous
calculations, and the coefficient input is L034's audited map data.
The uniform geometric and lifting arguments above are necessary in
addition to this finite arithmetic. The separate critical audit below
verifies their applicability as well as the complete finite records.

The actual local sizes are 2 versus 4. No global class is proved
removed. In particular L088's global norm constraint may make this
filter redundant, as happened at thirteen; no seven-adic comparison
on T is proved here. The unit bound fourteen and the supported bound
13+dim ker(n_S) remain unchanged, and no rank or integer conclusion
follows. L065 concerns the different five-isogeny map and is unaffected.

### Independent critical audit, 2026-10-18

This audit is REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-primitive-seven-image-audit.md`. It confirms
the stated exact image without correction. The general theorems are
reused from the precise citations above; the audit checks their actual
hypotheses and this specialization, rather than reproving them. The
following checks are required in addition to the finite replay.

**Entire fields and Kummer conventions.** Every coefficient of m agrees
with L033, and every coefficient of g and the substitution X=4x,
Y=8y+4 agrees with L069. The independent Frobenius replay proves mbar
irreducible of degree twelve, not just free of small factors: its final
Frobenius remainder is x and the gcd tests at exponents six and four
are both one. A root therefore has residue degree at least twelve;
the degree bound twelve and the local degree formula force the entire
field to be unramified of degree twelve. No polynomial-index assumption
at seven is needed. The distinct cubic factors (X+3)(X²+1) lift over
the unramified quadratic subfield of U, and the cubic discriminant is
the unit −256·11^5. Consequently its order over O_U is the full etale
maximal order O_U³. BPT Definition 1.6(ii), Theorem 1.8 and Corollary
1.9 apply in residue characteristic seven and give precisely four
norm-square unit tuples. No global narrow-class assumption is used.
The coordinate change is an isomorphism at seven and the ordinary
Kummer value is exactly 4x−theta, without an additional scalar quotient.

**Whole integral map and tail.** The complete integer coefficients,
NN'=−dh³, both x=16 points, h(16) and every origin monomial are replayed.
At an affine point where d vanishes, the two possible y values differ
by 121, a unit; one of N,N' is 11^22. Thus the stated opens really
cover the affine model, in both special and generic fibers. Their
fractions agree by the integer identity. Substituting x=t/w,y=−1/w
into the curve gives exactly wU0=t³. Substituting w=t³V into the map
gives the displayed Q and H, with Q(0,1)=−1 and H(0,1)=1. These are
regular functions near O; V is the inverse of a unit, not division by
t³. The origin is the only missing point of the projective affine
chart. Thus this is a morphism on the entire smooth proper model.
Its only special-fiber poles are O, with order one, and 3T, with order
eleven because x−16 is a parameter and N a unit. The special map has
degree twelve and is separable: an inseparable map in characteristic
seven would have every pole order divisible by seven.

Properness extends every U-point to O_U. Compatibility with the extended
map excludes both pole reductions when s is integral, so x,y are
integral. For negative s, put u=1/s in 7Z7. In the origin neighborhood
the equation 1/j=u has derivative −1 in t at the closed origin, while
the curve equation has derivative one in w. Hensel's implicit-function
application therefore supplies a Q7-point for every such u, with
the same unit Jacobian for all depths and unit parts. This point yields
B_s -> Q7. A unital map from the degree-twelve field U to Q7 would be
injective and Q7-linear, which is impossible. Thus the entire negative
tail is excluded, without a truncation or numerical approximation.

**All regular fibers, including the removable point.** All five complete
products, all irreducibility sequences/gcd tests, all squarefreeness and
B-unit tests, and every reconstruction are independently recomputed.
The reconstruction gives twelve distinct geometric points with the
correct curve equation and the N'-unit j-value. They exhaust the
special degree-twelve fiber, hence are simple. In particular the x=2
point in residue five is retained; it is the reduction of 2T and uses
the N' chart. On the curve the identity

    F(x,s)=(s−j)(N'−ds)

holds wherever j is finite. At 2T the second factor is a unit, so the
simple polynomial root also directly verifies the simple fiber point
there. At the other regular roots the usual elimination chart applies.
Each simple point lifts uniquely over its unramified residue extension
for every scalar in its disk. The residue degree bounds the field of
definition from below, and that lift gives the matching upper bound.
The lifted degrees sum to twelve; no generic point or multiplicity
remains. Thus the entire-algebra assertions throughout all five disks
follow, not just factorizations at five chosen scalars.

For each compatible regular residue, the replay verifies all three
nonzero differences and their characters. It additionally checks every
one of the twelve Frobenius conjugates of x with both choices of the
quadratic theta root held in the fixed target field. All give (+,+,+).
This checks the possible relative identifications explicitly, rather
than assuming that simultaneously conjugating x and theta is sufficient.
For an odd local prime, nonzero residue square characters completely
determine these unit square classes by Hensel. Every U-identification
is accounted for by its residue Frobenius automorphism.

**The two repeated branches.** At zero, the complete polynomial is the
cube of the irreducible quartic hbar. Its gcds with Bbar,dbar and gbar(4x)
are all one, and its y-reconstruction is verified. Therefore any
compatible point reduces to one of its four roots, and none of the
three Kummer differences vanishes. The independent exponentiations
give (+,−,−), for all four conjugate x roots and both quadratic-root
orderings. The residue extension to k has degree three, so its norm
exponent 5767203 is odd; a nonsquare stays nonsquare. These facts give
the claimed class uniformly over the whole zero neighborhood. They do
not assert that every scalar in it has an etale branch lift.

At residue six the entire polynomial is G² and G has the four distinct
irreducible factors displayed above. Coprime factor Hensel lifting
applies to the squares of those factors, yielding monic blocks of
degrees 2,2,4,4 for every s in that disk. Internal repeated roots do
not violate the coprime-block hypothesis. The B-unit condition ensures
that a point's y belongs to Q7(x), so any such point has degree at most
four. If B_s were U, the tautological affine point's x,y would generate
all of U: the finite fiber is contained in the affine chart and its
coordinate algebra is generated by these two coordinates. Degree at
most four contradicts twelve. This covers all branch depths, not only
the center or the primitive valuation subset. Together with the
regular tables and the negative tail, this exhausts all allowed scalars.
The surviving differences are units, so no omitted exceptional
two-torsion evaluation can change the image; O lies over infinity.

**Common witnesses and both inclusions.** Primitivity implies that two
coordinates cannot have positive valuation, since the equation would
then force the third to do so. With c a unit, the scalar valuations
are exactly 3v(a),4v(b); with c nonunit, they are both −11v(c).
Conversely, in the nonnegative case v(t/q)=3h−4k and b=7^k b0 make
(t/q)b⁴ have valuation 3h and b⁴/q valuation zero. In the negative
case b is a unit and these valuations are zero and 11n. The six
complete residue choices replayed in the certificate make each
normalized cube a unit cube; its derivative is nonzero. The unit
eleventh-power map is bijective on F7^* and has unit derivative, so
one c exists with the prescribed valuation in either case. Since
t+q=1, those very same a,b,c satisfy both required identities.
This verifies necessity and sufficiency without assuming cube or
fourth-power surjectivity on units.

At s=2 the exact fractions 16/863 and 13824/863 have residue roots
1 and 5 for the cube and eleventh power. Their derivatives are units,
their sum identity with b⁴=16 is exact, and the entire regular fiber
is U. At s0=9261/8 the fixed a=7 and residue roots b=c=1 solve
b⁴=169 and c¹¹=512 with unit derivatives; 343+169=512 and the scalar
identity are exact. In particular this argument never takes a square
root of +13 over Q7. L047's audited rational identification of the
entire canonical fiber with K uses FNS Section 7.2/Table 5 before its
GRH-dependent computation. Tensoring that rational identification
with Q7, by the same cited Stacks 01JQ fiber-product theorem, identifies
the entire B_s0 with U. Its proof does not depend on the Q3 roots
used elsewhere in L047. Thus this is an actual shared primitive
whole-fiber realization. The class upper bound and these two distinct
realizations prove both stated equalities and subgroup status.

Run `python3 scripts/primitive-seven-two-descent/audit_image.py`.
The independent script imports no construction code and does not trust
the old check flags. All 43 checks pass with no failures. The full
certificate `scripts/primitive-seven-two-descent/audit-certificate.json`
stores the exact integer-map evidence, every replayed factor/Frobenius/
gcd/reconstruction record, the additional complete conjugate character
tables, and both common-witness records. The full degree is 12 against
required 12; the excluded branch's maximum point degree is 4 against
required 12; the exact restricted/unrestricted image sizes are 2/4.
Every load-bearing original record was consumed and compared in full.
No new global class is removed, no dimension bound improves, and no
integer solution is excluded by this verification. Comparison on T
remains a distinct, unproved target requiring its own assessment.

## Mathlib

Full and supporting Mathlib coverage for this exact primitive correlated
image has not been checked. No absence claim is made. The general
local-field, Hensel, finite-field and Kummer theorems above are imported
by the precise citations given; the explicit seven-adic specialization
is documented here rather than asserted to be a library theorem.
