# L119 — Exact five-adic fake point image of the marked octic

## Hypotheses

Use L113's smooth proper curve C with its actual marking,

    Y²=G(t)=3025t⁸−31460t⁶+76230t⁴−39204t²+2673,

and L114's even-degree fake map over k=Q5. Put A5=k[theta]=k[t]/(G),
retaining the entire algebra and the common scalar quotient

    H5={delta in A5*/(A5*² k*): N(delta) in 3025 k*²}.

For nonbranch finite points the map is [t−theta]. Retain both distinct
rational infinity points and their L114 evaluations. No class-group,
global-unit, rational-point completeness or integer-lifting assumption
is made.

## Conclusion

There is a complete factor identification, with theta specified below,

    A5 ≅ L4 × L2 × U,
    L4=k(pi), pi⁴=10; L2=k(lambda), lambda²=15;
    U=k(omega), omega²=3.

Their (e,f) pairs are (4,1),(2,1),(1,2). Set

    alpha=[(pi,lambda,1)], beta=[(2,1,1)].

Then the exact norm-admissible ambient and point image are

    H5={1,beta,alpha,alpha*beta},
    mu(C(k))={1,alpha}.

All four ambient classes are distinct. Integral point coordinates are
precisely t in (1+5Z5) union (−1+5Z5), and all give alpha. Every
nonintegral t gives two points and identity image. There are no rational
branch points; both distinct infinity points have identity image. Both
classes also have finite realizations, at t=1 and t=1/5 respectively.

This is a local necessary filter by reproduction of assessed methods.
No global supported class is evaluated or removed; rational/integer
point control and any Beal signature exclusion remain unresolved.
The independent critical audit below confirms this result without correction.

## Proof

### Imported method and exact scope

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-five-adic-point-image.md`.
Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
inspected [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008: Section 2 p.3 for the map and exceptional points;
Section 4 p.6 and pp.8–11, Lemma 4.4, SquareClasses and LocalImage
with their explanations, for finite-local images, square neighborhoods
and exhaustive affine/reciprocal coverage. The assessment records the
complete source cases, including nonunit leading coefficient and bad
reduction. L113 supplies squarefreeness and the smooth proper charts;
G is integral over Q5. Thus the source hypotheses apply. We specialize
the method, without reproving its general algorithm or assuming its
unit-leading/good-discriminant shortcut at five.

The following direct fieldwise bounds compress the disk search. They
prove constancy, exclusion and realization for whole disks and an
infinite reciprocal tail, rather than sampling points or claiming a
literal execution trace of the recursive pseudocode. At residue
characteristic five every element of 1+m in a local field is a square:
Hensel's lemma applies to X²−u at X=1 with unit derivative 2. All
inequalities below use that strict neighborhood. Hensel's lemma and
Eisenstein's irreducibility criterion are standard named inputs.

### Complete local models, with the actual theta

Write q=1/theta, r=q² and

    H(r)=2673r⁴−39204r³+76230r²−31460r+3025.

The reciprocal identity is t⁸H(t^−2)=G(t). Modulo five,
H(r)=r³(3r+1), whose root 3 is simple (derivative 1). There is
therefore a unique r0 in 3+5Z5 with H(r0)=0. Also

    J(u)=H(5u)/25
        =66825u⁴−196020u³+76230u²−6292u+121.

Modulo five J(u)=3u+1, with simple root 3 and derivative 3.
There is a unique u1 in 3+5Z5 with J(u1)=0. Set r1=5u1.
These two roots are distinct, with valuations 0 and 1. Dividing by
their monic linear factors gives the exact identity in Z5[r]

    H(r)=2673(r−r0)(r−r1)(r²+a r+b),
    a=−39204/2673+r0+r1,
    b=3025/(2673*r0*r1).

Division is integral because the factors are monic and 2673 is a
unit; each zero makes the corresponding remainder zero. The displayed
a follows from the cubic coefficient and b from the constant term.
Reduction gives a=0 mod 5 and

    b/5=121/(2673*r0*u1)=3 mod 5.

Consequently the ENTIRE reciprocal polynomial factors as

    H(q²)=2673(q²−r0)(q²−r1)(q⁴+a q²+b).             (1)

The first quadratic is unramified irreducible: r0=3 mod 5 is a
nonsquare. The second is Eisenstein since v5(r1)=1. The quartic is
Eisenstein since a is divisible by five and v5(b)=1. These give
degrees 2,2,4, exhausting eight; all constants are nonzero. Replacing
q by 1/theta identifies the full original algebra with these three
fields, including the original scalar polynomial G. In particular
there is no rational branch point. No field is inferred merely from
residue degrees in L117 or from global irreducibility.

Here are explicit exact transports to the models in the conclusion.
Use principal square roots (the unique roots equal to 1 modulo five)
and put

    in U:  q=omega*sqrt(r0/3),
    in L2: q=lambda*sqrt(r1/15).

Both radicands equal 1 modulo five. For L4, pi⁴=10 is Eisenstein.
In its integer ring consider

    u⁴+(a/pi²)u²+b/10=0.                            (2)

The coefficient a/pi² has normalized pi-valuation at least 2;
b/10=−1 modulo pi since (b/5)/2=3/2=4 modulo five.
Thus (2) reduces to u⁴−1, with simple root 1 (derivative 4).
It has a unique root u=1 modulo pi. Set q=pi*u. Multiplying (2)
by 10 shows q⁴+a q²+b=0. This defines an isomorphism from the
quartic factor in (1) onto L4: the domain is an irreducible
degree-four field and L4 has degree four. The two quadratic
transports are isomorphisms for the same reason. In every model
theta is EXACTLY 1/q under these transports. The units q/pi,
q/lambda, q/omega are principal units. Their choices fix labels,
and their principal-unit square classes are trivial.

With normalized valuations on the respective fields, theta has
values −1,−1,0, or base-normalized values −1/4,−1/2,0.
The ramified fields have residue F5 and U has residue F25.
For U, theta²=1/r0=2 modulo five, so its residue is not rational.

### Full square classes, norms and the common scalar quotient

Every class in A5*/A5*² has a unique six-bit description

    (pi^a 2^b, lambda^c 2^d, 5^e eta^f),
    a,b,c,d,e,f in {0,1}, eta=1+omega.                 (3)

Indeed valuations give the first bit in each field; after removing
them, unit classes are residue square classes, by the strict Hensel
neighborhood. In L4 and L2 the residue of 2 is nonsquare in F5.
In U, eta has residue norm −2=3 mod 5, so it is a nonsquare unit.
The residue norm detects its square class: for z in F25*,
(N(z))²=z^12, the square criterion in F25*. Thus norm induces the
isomorphism between the two residue square-class groups. This also
shows the proposed unit representatives exhaust the possibilities.

Write k*/k*² labels as exponents of (5,2). The exact norm table is

| component | generator | norm in k | square-class label |
| --- | --- | --- | --- |
| L4 | pi | −10 | (1,1) |
| L4 | 2 | 16 | (0,0) |
| L2 | lambda | −15 | (1,1) |
| L2 | 2 | 4 | (0,0) |
| U | 5 | 25 | (0,0) |
| U | eta | −2 | (0,1) |

The uniformizer norms are their minimal-polynomial constants, with
the degree-even sign. The other norms follow from degrees or the
quadratic conjugation omega -> −omega. Unit labels use residues in
{1,4} for squares and {2,3} for nonsquares. Therefore (3) has norm
label (a+c,a+c+f), where sums of bits are modulo two. The leading
coefficient 3025=55² is square, so the exact norm condition is

    c=a, f=0.                                       (4)

Only ONE common k* scalar is allowed. The generators 2 and 5 of
k*/k*² have images

    2 -> (0,1,0,1,0,0),
    5 -> (0,1,0,1,1,0).                             (5)

For the second row, 5=pi⁴/2 in L4 and 5=lambda²/3 in L2;
1/2 and 1/3 are both nonsquare units. Rational units become squares
in the unramified quadratic U; rational 5 is its uniformizer.
The rows are independent and norm-trivial, as required by the
degree-eight scalar norm. Every scalar orbit has four members.
Use (5) to set d=e=0 uniquely, leaving a,b,c,f. Applying (4) gives
the four distinct representatives

    000000, 010000, 101000, 111000,

namely 1,beta,alpha,alpha*beta. This is the COMPLETE norm ambient;
it is not the unrestricted quotient (which has sixteen classes).
The certificate retains all sixteen scalar orbits and all collisions.

### Integral point coordinates: all five disks

For t in Z5,

    G(t)=t²−2 modulo five.

At residues 0,1,2,3,4 these values are respectively 3,4,2,2,4.
They are never zero. The three nonsquare disks contain no C(k)
point. On each of the two remaining disks the value is a unit with
square residue, hence has two exact square roots by Hensel's lemma.
This proves both necessity and sufficiency for EVERY integral t.

On each ramified factor, for every integral t,

    t−theta=−theta*(1−t/theta),

and the last factor is a principal unit. Its normalized error has
valuation at least 1 in L4 and in L2, strictly greater than zero.
By the exact transports, [−theta]=[pi] and [lambda] respectively:
the principal unit is square, inversion preserves a square class,
and −1 is already square in Q5. This holds even when t=0.

In U, t−theta is a unit because the residue of theta is not in F5.
Its residue norm is t²−2. On both feasible disks that norm is 4,
so the unit is square in U by the preceding norm criterion. Equivalently,
within either disk the difference from its center has valuation at
least 1 while the center value is a unit, a strict constant-class
bound. Thus every integral point has the raw class (pi,lambda,1)
and fake image alpha. The center t=1 has G(1)=11264=4 mod 5;
Y²−11264 has seed Y=2 and derivative 4 mod 5. It realizes alpha
as an exact point, with no approximation promoted to equality.

### Reciprocal chart: the entire infinite tail and both infinities

If v5(t)=−n<0, then n>=1 and q=1/t is in 5Z5, q!=0.
L113's chart becomes

    Z²=3025*S(q),
    S(q)=1−(52/5)q²+(126/5)q⁴−(324/25)q⁶+(243/275)q⁸.

The four nonconstant terms have valuations

    2n−1>=1, 4n−1>=3, 6n−2>=4, 8n−2>=6.

Thus S(q) is in 1+5Z5 for every such q, with no cancellation
assumption needed, and it has two exact principal-sign square roots.
Since 3025=55², every nonintegral t has two curve points.

In every factor write t−theta=t(1−theta/t). The normalized error
valuations for the second factor are, in the order L4,L2,U,

    4n−1>=3, 2n−1>=1, n>=1.

All are strictly positive, so every second factor is a square.
The first factor is one common scalar t and disappears in the fake
quotient. Equivalently the source reciprocal evaluation
q(1−q theta) has exactly that scalar quotient. Hence every
nonintegral finite point has identity image. This bounds the entire
tail uniformly, without a numerical depth cap or unclosed disk.
For a finite realization take t=1/5. Its exact G-value is
19137536/15625; after dividing by (55*t⁴)² the value is
1739776/11=1 mod 5. The normalized square-root equation has seed
1 and derivative 2 mod 5, proving an exact finite realization.

At q=0, do not substitute into the noninvertible affine fake
representative. The two separate smooth rows are

| q | Z | derivative 2Z | L114 fake value |
| --- | --- | --- | --- |
| 0 | −55 | −110 | [3025]=1 |
| 0 | 55 | 110 | [3025]=1 |

The derivatives are nonzero in Q5, although nonunit in Z5; the
smooth generic-fiber chart, not a good-reduction claim, is used.
These are distinct points with the same image. Integral t and
q in 5Z5 cover the proper curve over Q5, including these two
points; (1) proves the rational-branch list is empty. Every feasible
disk is realized and all images are accounted for. Equations (3)–(5)
show alpha!=1 and beta outside {1,alpha}. This proves the conclusion.

### Arithmetic evidence and limitations

Run `python3 scripts/pair-genus-two/marked_octic_five_adic_image.py`.
The complete certificate is
`scripts/pair-genus-two/marked-octic-five-adic-image-certificate.json`.
It stores both simple Hensel seeds and every residue child through
modulus 15625, the full factor-coefficient congruence and product,
the exact model definitions, all five integral disk rows, the four
reciprocal coefficient bounds, all six norm-generator values, all
64 raw square-class labels in their scalar orbits, the complete norm
kernel, realizations and separate infinity rows. The approximations
illustrate and check the factor arithmetic; the exact factors and
transports are defined by the unique Hensel roots above, never by a
finite precision guess. Complete evidence is consumed by the script;
selected full load-bearing values were inspected directly.

All 31 checks pass without failures. Actual/required local degree,
integral residue disks and infinity rows are 8/8, 5/5 and 2/2;
unresolved disks are zero. Actual ratio minima are (1,1) on the
ramified integral factors and (3,1,1) on the reciprocal factors,
against required strict positivity. The properness threshold is met:
2<4. The proof supplies the infinite-tail and Hensel reasoning that
finite arithmetic flags alone cannot establish.

The initial run used a lexicographically minimal orbit representative
while expecting the d=e=0 convention. It failed only `ambient_exact`;
the full record is preserved in
`scripts/pair-genus-two/marked-octic-five-adic-image-initial-label-failure.json`.
The quotient now explicitly sets d=e=0, with uniqueness checked for
every orbit. This convention correction changes neither the scalar
orbits nor the image and ambient cardinalities. No independent critical
audit is claimed in this calculation turn.

The result provides a membership test for future global supported
representatives, alongside the real filter. It computes no supported
unit basis, ordinary S-class two-torsion, global intersection or surviving
cover points. Degree-nine root recovery, compatible remaining factors,
both L095 systems and minus-eleven remain unresolved. The known boundary
points still prevent an empty fake-Selmer-set shortcut. No progress
beyond the inspected general local method is asserted.

### Independent critical audit, 2026-10-23

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-five-adic-critical-audit.md`.
The audit confirms the exact image, ambient quotient and complete local
models without correction. This verifies an instance of the cited method;
it adds no stronger mathematical conclusion or claim beyond those sources.
The direct mathematical inputs remain L113 and L114. L117 is not used
to prove any local factor or transport, and no global irreducibility or
class arithmetic is needed here.

For the exact factorization, independently reversing the even coefficients
gives H, and scaling its coefficient of r^i by 5^i/25 gives the integral
J. Their reductions are r^3(3r+1) and 1+3u. At their respective seeds
3 the derivatives are 1 and 3 modulo five. Hensel therefore defines exact
r0 and u1; r1=5u1 is a second exact root. Since r1-r0 is a unit, division
first by r-r0 and then by r-r1 has zero remainder even at the second
step. The remaining quadratic is monic after division by the unit 2673.
Its cubic and constant coefficients force the displayed a and b, so
the full identity is exact, not just a congruence. Their reductions give
a in 5Z5 and b/5=3 modulo five. Thus q^4+a q^2+b and q^2-r1 are
Eisenstein, while q^2-r0 has irreducible separable reduction. Their
degrees total eight, and their root valuations distinguish the factors.
This also proves that G has no rational root over Q5.

The field transports retain the same theta: in each field theta=1/q.
The two quadratic radicands r0/3 and r1/15 are principal units. In the
quartic model, a/pi^2 has pi-valuation at least two, b/10 has residue
four, and the equation for u has reduction u^4-1 and derivative four
at one. Its exact Hensel root gives q=pi*u, not a finite approximation.
The induced homomorphism from the Eisenstein quartic field is injective
and between fields of degree four, hence surjective. The quadratic
arguments have the same degree justification. Principal units are squares
because two is a unit in all three residue fields. These observations
justify both the transported valuations and the square-class labels.

The norm audit computes multiplication determinants in the three binomial
models, obtaining (-10,16,-15,4,25,-2) for all six generators. Valuation
and residue-square tests give exactly the two norm bits in (4).
Independently enumerating all 24 nonzero elements of F5[omega]/(omega^2-3)
confirms that its twelve squares are exactly the elements of square norm,
that 1+omega is nonsquare, and that every rational residue unit is square.
Together with the valuation decomposition and Hensel, this proves the
six-bit description is complete. The identities 5=pi^4/2=lambda^2/3
give the scalar-five row; scalar two gives the other row. All 64 vectors
are partitioned into sixteen four-member cosets. In every coset exactly
one vector has d=e=0, and the norm is constant on the coset. Exactly
sixteen raw vectors have square norm, leaving four quotient classes.
The representatives alpha and beta are distinct from the identity and
from each other in this quotient. No independent component scalar or
assumed subgroup property of the point image enters this calculation.

For integral coordinates, coefficient reduction gives G(t)=t^2-2 on
all five residues, with values (3,4,2,2,4). Thus precisely the two disks
t=1 or -1 modulo five have points, with two roots for every coordinate.
The ramified factors have theta-valuation -1, so for all integral t
the relative error -t/theta has valuation at least one (or is zero).
Their classes are [pi] and [lambda]. The unramified theta has residue
2omega, so t-theta has norm t^2-2 modulo five and is square in both
feasible disks. This proves containment and realization on entire disks,
not only the representative centers.

For nonintegral coordinates put n=-v5(t)>=1. Dividing the reversed
polynomial by 3025 independently gives the four displayed coefficients
of S. The valuations of their terms are 2n-1,4n-1,6n-2,8n-2, whose
minima are 1,3,4,6. Positive slopes prove strict positivity for all n,
so the square-root existence argument covers the full tail. The errors
-theta/t in the three factors have valuations 4n-1,2n-1,n, with minima
3,1,1. Thus every factor t-theta is t times a square; the SAME t is
the allowed common scalar. The strict inequalities also cover every
unit part of t. The exact values at 1 and 1/5 and their square-root
seeds verify both finite realizations independently. At q=0 the two
distinct rows Z=+55 and -55 have nonzero derivative, of five-adic
valuation one. They are smooth over Q5 without asserting smooth
reduction over Z5. L114's invertible exceptional representative 3025
gives identity at each. L113's two charts exhaust the smooth proper
curve; there is no rational branch exception or omitted annulus.

Run `python3 scripts/pair-genus-two/audit_marked_octic_five_adic_image.py`.
The complete independent evidence is
`scripts/pair-genus-two/marked-octic-five-adic-image-audit-certificate.json`.
The auditor imports no producer code and does not execute it. It computes
Hensel digits by the linear Taylor/Newton congruence and checks all fifty
child residuals; synthetic division and coefficient identities verify
the whole factor product modulo 15625. Determinant norms, the complete
residue-field square table and independent coset partition verify all
norm labels and collisions. Every final certificate field is consumed:
the mathematical data are compared with independent reconstructions,
while the producer's flags are checked only for report consistency.
The analytic arguments just reviewed, not the finite roots or flags,
prove the exact transports and unbounded chart statements.

All 82 independent checks pass. Actual/required coverage is degree 8/8,
integral disks 5/5, infinity rows 2/2, raw labels 64/64 and scalar cosets
16/16. The strict ratio minima remain (1,1) and (3,1,1), all above zero;
the exact point image has size two against norm ambient four. The entire
initial-failure record is also compared: only the orbit keys, ambient
labels, excluded-witness label and associated checks/failure list differ.
The old lexicographic representatives describe precisely the same cosets
as the final d=e=0 representatives. Its sole failed flag was ambient_exact,
and the original file remains unchanged. No mathematical correction is
hidden in that convention change.

The audit closes the reliability question for this local input. It does
not evaluate any global supported class, compute units or S-class
two-torsion, determine rational points or solve either L095 system.
The other global and integer-lifting gaps stated above remain open.

## Mathlib

Full matching Mathlib coverage of this exact octic local image and the
full Bruin–Stoll finite-local algorithm is not checked. The proof uses
standard Hensel, Eisenstein, residue-square and finite-field norm facts;
supporting Mathlib theorem identifiers have not been checked. Unknown
coverage is not an absence claim.
