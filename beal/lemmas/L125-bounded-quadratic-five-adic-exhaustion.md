# L125 — No additional five-adic pruning in the bounded quadratic family

## Hypotheses

Use L114's unchanged marked curve Y²=G(t)=11F(t), with

    F(t)=275t⁸−2860t⁶+6930t⁴−3564t²+243,

L115's entire degree-eight field K=Q[theta]=Q[t]/(F), and S consisting
of every maximal-ring prime above {2,3,5,11}. Work in K*/(K*² Q*)
with one common rational scalar, and norm fiber 3025 Q*². Use L118's
descending real embeddings, L122's actual dyadic transports and complete
class tables, and L119's actual three five-adic factors and point image.
The family consists of the 289 INDIVIDUAL values

    delta_(a,b)=theta²+a theta+b,  a,b in Z, −8<=a,b<=8.

No product closure, full supported group, unit basis, S-class two-torsion,
point existence or point completeness is assumed.

## Conclusion

Exactly thirteen values are S-units, exactly seven of those have square
rational norm, six of the seven pass L118, and four pass both L118 and
L122. Every one of the seven is square in each of L119's three actual
five-adic factors. Thus all four survivors pass L119 with identity class:
there is NO witness to additional five-adic pruning in this finite family.
The four pairs surviving all tests are

    (a,b)=(-2,1), (0,0), (0,3), (2,1).

This exhausts and stops the approved finite family. It gives neither a
complete supported-class calculation nor rational-point realization,
point completeness, either L095 integer exclusion or a Beal resolution.
Arithmetic replay and the separate critical mathematical audit below pass.

## Proof

### Imported methods, exact scope and support

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-bounded-quadratic-five-adic-pruning.md`.
This is REPRODUCTION of known methods on a finite instance, not a claim
of progress beyond the checked general sources. Import J.S. Milne,
*Algebraic Number Theory*, v3.08, 19 July 2020,
[author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Propositions 2.4/2.6 pp.26–28 (integrality and ring closure), norm and
Proposition 2.19/Corollary 2.20 pp.31–32, Proposition 4.1(c) pp.68–69
(principal-ideal norm, including the non-Galois case). For norm,
localization, common scalars and certified signs import Nils Bruin and
Michael Stoll, *Two-cover descent on hyperelliptic curves*, Math. Comp.
78 (2009), 2347–2370, [DOI](https://doi.org/10.1090/S0025-5718-09-02255-8),
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2), 21 October 2008,
Section 2 p.3, Sections 4–5 pp.6–11 including Lemma 4.4 and
SquareClasses, and Section 6 pp.11–13, ad 7,12,16 and Remark 6.1.
L114/L115 give the unchanged characteristic-zero squarefree even-degree
algebra, and 3025=55² makes the norm test a positive rational square
test. These source results and the exact L118/L119/L122 images are
imported without reproof; only the instance evaluations below are new
local notebook work. Bad reduction at two and five is retained.

For p outside {5,11}, F/275 is a monic polynomial over Z_p. Its root
theta is integral in every maximal-ring completion above p. Closure
under polynomial evaluation makes every delta_(a,b) integral there.
None is zero: a nonzero polynomial of degree two cannot annihilate
theta, whose minimal polynomial has degree eight by L115. For p outside
S, the principal-ideal norm formula therefore gives

    v_p(N(delta))=sum_(P|p) f(P/p) v_P(delta),

with all summands nonnegative and every f(P/p)>0. Hence delta is an
S-unit if and only if its rational norm has no prime outside S. There
is no cancellation of opposite ideal valuations in this equivalence.
No maximality assertion about Z[theta] is used.

### Complete norm and eligibility certificate

For q(t)=t²+a t+b, divide F by the MONIC q, keeping the entire integer
quotient and remainder F=q Q+(c t+d). Then

    N(q(theta))=(d²−a c d+b c²)/275².                    (1)

Indeed the full conjugate-product norm is Res(F,q)/275², retaining the
nonmonic leading coefficient. Swapping the two resultant arguments has
positive sign because 8*2 is even. At the two roots lambda,mu of q,
with multiplicities retained, the product of F-values is
(d+c lambda)(d+c mu)=d²−a c d+b c². This argument also applies when
q has a repeated root; no squarefree restriction on trial q is imposed.

The producer enumerates both a and b from −8 through 8 with no gcd or
other restriction. At descending k=8,...,2, replace a remainder term
z t^k by −a z t^(k−1)−b z t^(k−2), recording z in Q. Evaluate (1),
reduce the rational number, then strip 2,3,5,11 from its numerator and
denominator by exact division. The residual denominator is one in all
289 rows. Exactly these thirteen rows have residual numerator one:

| Pairs (a,b) | Exact norm | Exponents at (2,3,5,11) |
| --- | --- | --- |
| (-4,3),(-2,-3),(2,-3),(4,3) | 254803968/75625 | (20,5,-4,-2) |
| (-3,0),(3,0) | 60466176/75625 | (10,10,-4,-2) |
| (-2,1),(0,-1),(2,1) | 1048576/75625 | (20,0,-4,-2) |
| (-1,0),(1,0) | 248832/75625 | (10,5,-4,-2) |
| (0,0) | 59049/75625 | (0,10,-4,-2) |
| (0,3) | 47775744/121 | (16,6,0,-2) |

All other 276 residual numerators exceed one, so each has a prime
outside S and is ineligible. This needs no factorization of those
residuals. The odd exponent five of 3 rejects six eligible rows from
the norm fiber. The remaining seven appear below. Positivity and exact
integer square roots of reduced numerators/denominators give the same
test independently of the exponent-parity test. The certificate stores
every quotient, remainder, reduced norm, signed exponent and residual;
no undecided row is omitted.

The independent replay constructs, for EVERY trial value, the full
8-by-8 multiplication matrix of b+a theta+theta² in basis
(1,theta,...,theta⁷), using theta⁸=−sum_(i<8)(F_i/275)theta^i.
Exact rational Gaussian elimination, with row swaps and all pivots
retained, reproduces every norm in (1). It also reconstructs all nine
coefficients of each division identity and every support decision.
This checks the norm formula independently of its producer evaluation.

### Exact real and dyadic evaluations of all seven rows

L118's eight disjoint root intervals are used in descending order.
Bisect the outer positive interval at 11/4 and the interval (3/4,1)
at 7/8, reflecting these refinements at the negative roots. The signs
of F at these new midpoints are positive, respectively
2105916019/65536 and 6500988499/16777216. Thus the refined intervals
are (5/2,11/4), (3/2,2), (3/4,7/8), (1/4,1/2) and their negatives
in descending order. All eight endpoint sign changes are retained.
For each q, its maximum and minimum on a closed isolating interval
are obtained from its endpoints and its vertex −a/2 if present. All
seven values have strict constant sign on each interval. Compare the
eight signs modulo simultaneous reversal with L118's actual image.

At two use L122's exact theta=(alpha,−alpha) in L×L, normalized
v_L(2)=4, and its approximant alpha0 with v_L(alpha−alpha0)>=20.
Here v_L(alpha+alpha0)=4, since alpha0 is a unit and their difference
has valuation at least 20. The error in evaluating q at either sign is

    (alpha−alpha0)(alpha+alpha0 ± a),

so a certified absolute error bound is

    B(a)=20+min(4,4v2(a)),  with B(0)=24.               (2)

Cancellation in the second factor can only improve this lower bound.
For each approximate value record its full valuation w, normalize by
pi^w, and apply L122's COMPLETE unit-coset table modulo pi^9. Every
B(a)−w below is strictly greater than 8, so the approximation has the
same valuation and square class as the exact value. This is a
value-dependent check, not an inherited linear precision assertion.

| (a,b) | Positive norm root | Ordered real signs | Raw dyadic labels | Quotient | w in the two factors | B−w |
| --- | --- | --- | --- | --- | --- | --- |
| (-3,0) | 7776/275 | ----++++ | (17,18) | (2,24) | (4,6) | (16,14) |
| (-2,1) | 1024/275 | ++++++++ | (0,0) | (0,0) | (12,8) | (12,16) |
| (0,-1) | 1024/275 | ++----++ | (1,1) | (1,1) | (10,10) | (14,14) |
| (0,0) | 243/275 | ++++++++ | (0,0) | (0,0) | (0,0) | (24,24) |
| (0,3) | 6912/11 | ++++++++ | (0,0) | (0,0) | (8,8) | (16,16) |
| (2,1) | 1024/275 | ++++++++ | (0,0) | (0,0) | (8,12) | (16,12) |
| (3,0) | 7776/275 | ++++---- | (18,17) | (2,24) | (6,4) | (14,16) |

Each quotient is the minimum of the full eight-element diagonal scalar
orbit from L122; independent factor scalars are never allowed. The
actual dyadic point image is {(0,0),(0,5),(0,8),(0,22),(2,6)}, not its
span. Thus (0,-1) fails both real and dyadic tests, and the rows with
a=±3 fail at two after passing the real test. Exactly four rows pass both.

The replay evaluates alpha² as the EXACT element 1+4r from L122,
using alpha0 only in the linear term. This is independent of the
producer's alpha0² evaluation. For a nonzero its error is at least
20+4v2(a), and for a=0 the error is zero. It gives the same raw
labels and complete common-scalar orbits. Every applicable replay
relative bound also exceeds 8.

### All three five-adic factors, including cancellation

Use the EXACT L119 transports: theta=1/q in L4=Q5(pi), pi⁴=10,
in L2=Q5(lambda), lambda²=15, and in U=Q5(omega), omega²=3.
In the two ramified factors q has normalized valuation one. For each
of our seven values,

    delta=theta²(1+a q+b q²).

The first factor is a nonzero square. For ramification index e=4 or 2,
the perturbation has lower bound min(e v5(a)+1,e v5(b)+2), omitting
zero terms. For a=±3 or ±2 the bound is 1 in both fields; for
(a,b)=(0,-1),(0,3) it is 2; at (0,0) the perturbation is exactly zero.
All nonzero bounds exceed zero. Hensel with unit derivative 2 makes
these principal units squares, so both actual ramified class labels
are (0,0). This uses L119's exact root transports, not finite field
approximations to define a field.

For U let r0 be L119's unique root in 3+5Z5 of

    H(r)=2673r⁴−39204r³+76230r²−31460r+3025,

and let s be the principal root sqrt(3/r0). Then theta=omega*s/3,
and the exact value is

    (1/r0+b)+(a s/3)omega.                              (3)

Successive simple-root Hensel lifting to modulus 5^8 gives
r0=131783 mod 390625 and s=9221 mod 390625. Substitution gives
H(131783)=806098628055247106250000, divisible by 5^8; H' remains
a unit because H'(3)=1 modulo five. The computed radicand is 261216
modulo 390625, and 9221² equals it modulo that modulus. Its principal
choice and derivative 2s a unit prove the certified s error. Inversion
of units preserves this precision. Substituting these rational
approximants in (3) has absolute U-error at least 8 in all seven rows.

In the unramified field, valuation is the minimum of the two rational
coefficient valuations, since (1,omega) is an integral residue basis.
After dividing by 5^w, the following complete residues in F25 and
residue norms x²−3y² certify the unit square classes:

| (a,b) | w | Unit residue (x,y) | Residue norm | Relative error bound |
| --- | --- | --- | --- | --- |
| (-3,0) | 0 | (2,4) | 1 | 8 |
| (-2,1) | 0 | (3,1) | 1 | 8 |
| (0,-1) | 0 | (1,0) | 1 | 8 |
| (0,0) | 0 | (2,0) | 4 | 8 |
| (0,3) | 2 | (3,0) | 4 | 6 |
| (2,1) | 0 | (3,4) | 1 | 8 |
| (3,0) | 0 | (2,1) | 1 | 8 |

The cancellation in theta²+3 has been resolved: its valuation is TWO,
not zero, and the strict relative bound is 8−2=6>0. Every valuation
is even, and every unit residue is square: the residue norm detects
squares in F25*, as proved in L119. The strict error bounds make these
exact classes; they are not guesses from residue samples. Thus the U
class is (0,0) in every row, completing all three actual factors.
The replay independently lifts r0 and s by Newton iteration to 5^10
and obtains the same valuations and normalized residues.

Every raw six-bit label is consequently 000000. Its FULL common-scalar
orbit is {000000,000010,010100,010110}, with canonical representative
000000 when coordinates d=e=0 as in L119. This belongs to the actual
point image {000000,101000}. No subgroup/span substitution is needed.
All seven pass, so no eligible norm-square value passing the real and
dyadic filters fails the five-adic filter.

### Evidence, duplicates and scope of the stop

Reproduction commands, relative to this notebook, are

    python3 scripts/pair-genus-two/marked_octic_bounded_quadratic.py
    python3 scripts/pair-genus-two/replay_marked_octic_bounded_quadratic.py

Complete producer evidence, with all 289 rows, exact divisions, all
eight refined root intervals, all seven full local evaluations and
scalar orbits, is
`scripts/pair-genus-two/marked-octic-bounded-quadratic-certificate.json`.
The full matrices and elimination traces and all local replay records
are in `scripts/pair-genus-two/marked-octic-bounded-quadratic-replay.json`.
All 1,454 replay checks pass, with no failures. Actual/required minima
are 12>8 at two, 6>0 in U, and 1>0 for nonzero ramified perturbations.
Zero perturbations are explicitly identities, not missing bounds.
The replay consumes complete evidence, rather than treating a preview
or producer success flag as verification. This is an arithmetic replay;
the separate critical mathematical audit is recorded below.

Three surviving values are manifest global squares: (theta−1)²,
theta² and (theta+1)². The rejected rows a=±3 have L124's already
known joint image; they are not new dyadic witnesses. The row theta²−1
has the real rejection pattern already seen in C123a, up to scalar.
The fourth survivor theta²+3 is only localized here; no global
scalar-square relation or rational-point image is asserted. C124b's
mask-17 relation remains preserved and is outside this box (b=−9).
These comparisons are duplication checks, not additional proof premises.

The negative conclusion applies only to the stated individual values.
It does not enumerate their product closure or the full supported
square-class space, and enlarging the box is not part of this step.
Full units/S-class two-torsion, other classes, surviving-cover points,
degree-nine root recovery, compatible remaining factors, both L095
systems and minus-eleven remain open. Known rational infinity points
survive; no rational-point or integer emptiness follows.

### Separate critical mathematical audit — 2026-10-24

The invocation-start SPECIALIZE assessment was
`drafts/literature/2026-10-24-bounded-quadratic-exhaustion-critical-audit.md`.
This audit is REPRODUCTION using the precise Milne and Bruin–Stoll
citations above and the unchanged L114/L115/L118/L119/L122 inputs.
It verifies the finite negative result without changing its statement,
proof mechanism or direct mathematical inputs. No broader novelty,
supported-group completeness or point classification is claimed.

The support equivalence is valid in the maximal ring, not just a
polynomial order. At every prime outside S, the monic equation F/275
makes theta integral, and polynomial evaluation preserves integrality.
All prime-ideal valuations are therefore nonnegative, with positive
residue-degree weights in the norm formula. Vanishing of their sum
forces each to vanish. Conversely, support of the principal ideal
inside S forces rational norm support inside S. Degree eight ensures
that none of the quadratic trial values vanishes. The norm fiber is
square because the actual leading coefficient is 3025. The resultant
identity uses 275², not 3025 or a monic replacement without scale,
and remains valid for repeated roots of the trial quadratic.

The separate audit implementation imports no producer, replay or local
arithmetic module. It reconstructs all 289 multiplication matrices
directly by reducing shifted quadratic polynomials, checks every entry
and elimination pivot of the stored replay, and compares every full
division identity and resultant norm. It checks every signed support
exponent, residual numerator/denominator, square decision and norm root.
The ordered 17-by-17 box and the exact seven-row local list are checked
in full. This confirms thirteen S-units, seven square norms and no
undecided trial. It also checks every stored replay comparison, while
independently verifying the evidence on which the conclusion depends.

At the real place, eight disjoint refined sign-changing intervals exhaust
degree eight; exact endpoint and vertex bounds give all 56 strict signs.
The only scalar identification is simultaneous reversal. Comparison with
L118's actual four classes confirms six real survivors. At two, the
quartic equation and the full valuation formula reconstruct the unit
residue ring. All 256 units, eight square residues and 32 disjoint cosets
are enumerated independently, and all imported unit labels agree.
Direct normalization gives the eight rational scalar labels in the
displayed theorem order; their sorted set is the certificate convention.
All seven complete diagonal orbits are recomputed, with no independent
component scalars or point-image span substituted.

The alpha0 residual has valuation 24 and its derivative valuation four;
its distance from the original seed beta has valuation eight. Strong
Hensel therefore identifies the same exact alpha with error at least
20. Since alpha0 is a unit, alpha+alpha0=2alpha0+(alpha-alpha0) has
valuation exactly four. This justifies (2), including possible extra
cancellation in the multiplier. Each approximate value has error of
strictly larger valuation than the value itself, so its full valuation
is exact. The minimum relative bound is 12>8. Independently replacing
alpha0² by the exact 1+4r reproduces every replay component and class;
for a=0 this replacement is exact. The actual five-class point set
leaves precisely the four stated real/dyadic survivors.

At five, L119's transports give theta=1/q with q a uniformizer in
both ramified factors. The two perturbation terms have the stated
valuations, so their sum has at least their minimum; cancellation can
only improve the bound. The nonzero minimum is 1>0, and at (0,0)
the perturbation is identically zero. Thus both factors are squares
for all seven rows. In U, the residue basis (1,omega) prevents
cancellation between the two rational coefficients. All Hensel
residuals, principal-root choices and coefficient approximations are
checked. The simple-root derivatives and unit inversion justify
absolute error at least eight. The full normalized residues and the
replay's independent precision-ten root balls agree. In particular
theta²+3 has valuation two, residue (3,0) after division by 25, and
relative error 6>0. Every valuation is even and every residue norm
is in {1,4}; the F25 norm square test therefore proves exact squareness.
All seven raw classes are identity, and their complete four-element
common-scalar orbits belong to the actual L119 point image.

Run from this notebook:

    python3 scripts/pair-genus-two/audit_marked_octic_bounded_quadratic.py

Full evidence, including hashes of the preserved producer/replay and
dyadic input, every norm decision, all local rows and every comparison,
is `scripts/pair-genus-two/marked-octic-bounded-quadratic-audit-certificate.json`.
All 3,514 comparisons pass with no failures; strict actual/required
bounds are 12>8 at two, 6>0 in U and 1>0 for nonzero ramified
perturbations. The initial audit harness compared the scalar labels in
theorem order with their stored sorted order. That sole comparison
failure is preserved in
`scripts/pair-genus-two/marked-octic-bounded-quadratic-audit-initial-order-failure.json`;
checking both the ordered labels and their sorted set repairs the
harness without altering any mathematical result or original evidence.

The audit passes. The finite family supplies zero additional five-adic
removals; it remains exhausted under this target. This is a verified
finite stop, not a ban on other mechanisms. Full supported arithmetic,
surviving-cover points, degree-nine recovery, remaining factors, both
L095 systems and minus-eleven remain unresolved. The manifest squares
and known infinity classes survive. No argument or DAG change is needed.

## Mathlib

Full matching coverage of this finite instance, the fake two-cover
scalar quotient and the imported local tables is not checked. No absence
or formalization claim is made. General source results are imported by
the precise citations above; the instance uses exact rational arithmetic.
