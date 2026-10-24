# L122 — Exact marked-octic fake point image at two

## Hypotheses

Use L113's smooth proper curve C with its actual marked model

    Y²=G(t)=3025t⁸−31460t⁶+76230t⁴−39204t²+2673.

Use L114's entire algebra A_2=Q2[t]/(G), theta=t mod G, and fake map

    mu:C(Q2) -> H_2,
    H_2={delta in A_2*/(A_2*² Q2*): N(delta) in 3025 Q2*²}.

For an ordinary finite point mu=[t−theta]. In the reciprocal chart
q=1/t the representative is q(1−q theta); one common rational scalar
may be removed. Retain both separate infinity points Z=±55 and their
L114 image [1]. No global units, S-class group, maximal-order computation
L116/L117 or point-completeness assumption is used.

## Conclusion

The entire two-adic algebra is L × L, where L=Q2(pi) is the totally
ramified quartic field defined by the Eisenstein polynomial

    E(X)=(9150625X⁴−48315300X³+91279980X²
                         −74245842X+22130658)/9150625.

The actual theta transports to (alpha,−alpha), with alpha specified
exactly below. The full norm-admissible common scalar quotient H_2
has 64 classes. Its exact point image has five distinct classes:

    mu(C(Q2))={ [1], [−theta], [2−theta], [3−theta], [1−2theta] }.

The four nonidentity entries have exact finite Q2-point realizations
at t=0,2,3,1/2 respectively. Identity is realized at t=1/8 as well as
at each distinct infinity point. This is a proper local filter, not a
subgroup assertion, an identified removed global class, a rational-point
classification, either L095 integer exclusion or a Beal resolution.
The separate critical mathematical audit below confirms the claim without
a correction to the field model, class counts or point image.

## Proof

### Imported method and normalization

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-two-adic-point-image.md`.
Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2), 21 October 2008:
Section 2 p.3 and Section 4 pp.6–11, specifically Lemma 4.4 p.8,
SquareClasses pp.9–10 and LocalImage pp.10–11 with their explanations.
These cover integral squarefree polynomials over characteristic-zero
complete discretely valued fields with finite residue field, including
dyadic fields and bad polynomial reduction. L113 verifies degree eight,
squarefreeness and both smooth proper charts; L114 fixes the exact map.
No odd-residue shortcut is used.

Use the standard strong Hensel lemma in the following explicit form:
v(f(a))>2v(f'(a)) implies a root whose difference from a has valuation
v(f(a))−v(f'(a)); the root is unique in the usual strict derivative ball.
In L below normalize v_L(pi)=1, so v_L(2)=4. Applied to X²−(1+epsilon)
at 1, it shows 1+epsilon is square whenever v_L(epsilon)>8. This is
the strict dyadic square neighborhood underlying the cited algorithm.
Over Q2 a nonzero number is square exactly when its valuation is even
and its normalized odd unit is 1 modulo 8, the finite square test in
SquareClasses step 4. The general algorithm and Hensel test are imported;
the following full models, tables and disk compression are instance work.

### Exact entire local algebra, including theta

Put P(S)=3025S⁴−31460S³+76230S²−39204S+2673, so G(t)=P(t²).
Direct expansion gives

    P(1+4r)/256=3025r⁴−4840r³+484r+44.                 (1)

All nonleading coefficients of E have positive v2, with valuations
(1,1,2,2) in ascending order and unit leading coefficient. Eisenstein
therefore defines one degree-four field L, with e=4 and residue field F2.
Write

    A(X)=3025X²−6050X+3036, B(X)=2541−2420X.

Its defining numerator is exactly

    A(X)²−2(X−1)B(X)²=9150625 E(X).                  (2)

In L define r=−A(pi)/B(pi). The denominator is a unit, and (2) gives
r²=2(pi−1). Thus v_L(r)=2 and pi=1+r²/2. Also

    3025(pi−1)²+11+r(2541−2420pi)=0,

so substitution of r²=2(pi−1) gives (1) equal to zero. These are exact
identities in L, not finite-precision definitions. For reproducibility
the same r has power-basis coefficients

    r=468−1126pi+(2585/3)pi²−(5500/27)pi³.

Let beta=1+2r. Then

    beta²−(1+4r)=4r²,
    v_L(4r²)=12>8=2v_L(2beta).

Strong Hensel defines a unique alpha with alpha²=1+4r and
v_L(alpha−beta)=8. Hence v_L(alpha−1)=6 and v_L(alpha+1)=4.
Equation (1) gives G(alpha)=G(−alpha)=0. Moreover

    pi=1+(alpha²−1)²/32,

so Q2(alpha)=L, and similarly Q2(−alpha)=L. They have different
minimal polynomials: every Q2-embedding preserves the unique extension
of the valuation, whereas v_L(alpha−1)=6 and v_L(−alpha−1)=4.
The two distinct irreducible degree-four factors exhaust degree eight.
The Chinese remainder map therefore identifies the entire A_2 with
L × L, with theta exactly (alpha,−alpha). In particular no rational
branch point exists. The constant twist and leading coefficient 3025
have not been changed.

For computations only, take two Newton steps from beta. Residual
valuations at beta, beta_1 and beta_2 are respectively 12,16,24;
derivative valuation is always 4. Thus the final rational L-element
alpha_0=beta_2 has v_L(alpha−alpha_0)>=20. All evaluations below
have component valuations at most six, so 20>6+8 makes this
approximation sufficient for exact square classes. The exact alpha
is always the Hensel root above, not the approximant.

### Complete square, norm and common scalar tables

Every L-element has a unique expansion sum_(i=0)^3 a_i pi^i with
a_i in Q2. Its nonzero summands have distinct valuations modulo four,
so its valuation is min_i(4v2(a_i)+i). Integrality is equivalent to
all a_i in Z2. This proves O_L=Z2[pi], without importing an uninspected
maximal-order certificate. The ideal pi^9 O_L has coefficient bounds
(8,4,4,4). Hence a complete residue system for O_L/(pi^9) is

    (a0,a1,a2,a3), 0<=a0<8, 0<=a1,a2,a3<4,

with 512 elements and 256 units, characterized by a0 odd. Multiplication
uses E followed by these coordinate reductions. It is a quotient-ring
calculation, not coefficientwise multiplication. A unit is a square
in L exactly when its residue belongs to the complete set of unit
squares in this ring: necessity is reduction of a unit square root;
sufficiency follows by dividing by its lifted square and applying the
strict 9>8 square neighborhood. Enumerating all 256 units gives exactly
the following eight square residues:

    (1,0,0,0), (1,0,2,0), (1,2,1,0), (3,0,1,2),
    (5,2,3,0), (7,0,3,2), (7,2,0,0), (7,2,2,0).

Their 32 disjoint multiplicative cosets exhaust every unit residue.
Choose the lexicographically smallest member of each coset, sort these
representatives lexicographically, and number them 0,...,31. Every
square class has the unique label 32p+i, represented by pi^p times
unit representative i, with p in {0,1}. To label an arbitrary element,
divide by pi to its full valuation first, then take that unit's coset.
This fixes all 64 field labels, including identity label zero.

For each representative compute its exact multiplication matrix in
the basis (1,pi,pi²,pi³). Its determinant is N_(L/Q2). The full
64-row determinant/norm-class table is saved in the certificate below.
Its norm labels run through all eight Q2 square classes; each occurs
eight times. The complete 64-by-64 multiplication comparison also
checks multiplicativity of these norm labels. No norm bit is omitted:
the rational label records both valuation parity and odd unit modulo 8.

In A_2 the norm of a pair is the product of its two field norms. As
3025=55², the raw norm fiber consists of pairs with equal norm labels.
There are eight fibers of size eight in each component, hence
8*8²=512 raw pairs. The single diagonal Q2 scalar group has labels

| scalar | 1 | 5 | 2 | 10 | −1 | −5 | −2 | −10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| field label | 0 | 22 | 12 | 29 | 5 | 8 | 19 | 15 |

These eight labels exhaust Q2*/Q2*², are distinct in L, and form the
complete common scalar image. Its diagonal action on pairs is free,
preserves the norm fiber, and gives 512/8=64 classes in H_2. It does
not allow independent scalar choices in the two factors. Canonicalize
a pair by the lexicographically smallest pair in its eight-element
common scalar orbit. All raw pairs, all canonical pairs and the
complete multiplication table are retained in the certificate.

### All coordinate disks, including the infinite tail

For t even, direct expansion gives G(2u)=1 modulo 8 coefficientwise.
Every t in 2Z2 has two points. Both t−alpha and t+alpha are units.
Changing t within a residue disk modulo 8 changes each by valuation
at least 12>8, so its raw classes are constant on each of the four
even disks. This is a strict square-neighborhood bound in L.

For t odd, write t=a+16u, a in {1,3,5,7,9,11,13,15}. The coefficient
minimum of G(a+16u)−G(a) is exactly 13 for each a. Each G(a) has
valuation ten, and their units modulo 8 in this order are

    3, 1, 5, 7, 7, 5, 1, 3.

Thus the whole disks a=3,13, and only those odd disks, have points.
These statements use the complete shifted polynomials, not sampled
values of u. For any odd t the two component valuations are (6,4)
if t=1 modulo 4 and (4,6) if t=3 modulo 4: compare t±1 with
alpha−1 of valuation six and alpha+1 of valuation four. Changing
t modulo 16 changes its value by at least 16>6+8=14, proving
constant classes on both feasible odd disks. These arguments also
show G never vanishes at a rational coordinate.

For the entire nonintegral chart put q=1/t in 2Z2. Its curve polynomial
is G_rev(q)=3025−31460q²+76230q⁴−39204q⁶+2673q⁸.
Coefficientwise G_rev(2u)=1 modulo 8, so every q in 2Z2 has points.
Remove the one permitted common scalar q from the affine reciprocal
representative q(1−q theta). Its two components are (1−q alpha,
1+q alpha), both units. Changes in q modulo 8 have valuation at least
12>8, so q=2,4,6 modulo 8 give constant classes. On the full tail
q in 8Z2 both components are themselves within valuation at least
12>8 of one and hence square. This uniformly includes all nonzero
tail valuations; a literal unbounded search is unnecessary. At q=0
use the separate infinity rule, not this affine expression.

### Exact labels, realizations and comparison

The complete feasible disk table in the fixed convention is:

| chart and center | modulus | raw field labels | common scalar quotient |
| --- | --- | --- | --- |
| t=0 | 8 | (8,22) | (0,5) |
| t=2 | 8 | (22,5) | (0,8) |
| t=4 | 8 | (5,0) | (0,5) |
| t=6 | 8 | (0,8) | (0,8) |
| t=3 | 16 | (10,17) | (2,6) |
| t=13 | 16 | (31,18) | (2,6) |
| q=2 | 8 | (5,8) | (0,22) |
| q=4 | 8 | (22,22) | (0,0) |
| q=6 | 8 | (8,5) | (0,22) |
| q=0 tail | 8 | (0,0) | (0,0) |

The finite center values G(0)=2673, G(2)=−173503 and
G(3)=2737152 have rational square labels (even valuation, unit 1).
For q=2 and q=8 the reciprocal values are −727903 and 34878632657,
respectively, both odd and 1 modulo 8. Strong Hensel therefore supplies
exact Q2-points at t=0,2,3,1/2,1/8. These realize every quotient label.
The two finite Y-signs have the same fake evaluation. In particular
t=0 here is a two-adic coordinate, not a newly asserted Q-rational point.
Both distinct infinity rows Z=−55 and Z=55 have L114 image [1],
the already realized identity (0,0), and remain separate smooth points.

All finite and reciprocal coordinates and all exceptional points have
now been exhausted. The image is exactly

    {(0,0),(0,5),(0,8),(0,22),(2,6)},

whereas the full H_2 has 64 classes. This proves the claimed 5<64
properness. We calculated a set before making any comparison; no
subgroup property of a point image is assumed. The actual point-class
representatives in the conclusion follow directly from the chosen
centers and the one common reciprocal scalar removal.

### Complete arithmetic evidence and limitations

Reproduce with

    python3 scripts/pair-genus-two/marked_octic_two_adic_image.py
    python3 scripts/pair-genus-two/replay_marked_octic_two_adic_image.py

The full artifacts are
`scripts/pair-genus-two/marked-octic-two-adic-image-certificate.json`
and `scripts/pair-genus-two/marked-octic-two-adic-image-replay.json`.
The producer passes all 99 checks with no failures. It saves the exact
field identities and all Newton residuals, every unit residue and coset,
all 64 exact norms, the full multiplication table, scalar transports,
all 512 raw norm pairs and 64 quotient pairs, every shifted odd-disk
polynomial, every feasible row and both infinity evaluations. Actual
and required square precision are 9 and 9; approximation error bound
20 strictly exceeds required 14. Component disk bounds are respectively
12>8, 16>14 and 12>8, including the uniform tail.

The arithmetic replay imports no producer code and passes 291 checks
with no failures. It consumes every coset and field norm, using integer
residue arithmetic and Leibniz determinants rather than the producer's
rational residue arithmetic and Gaussian determinants. It compares the
complete norm fibers/quotient, all Newton equations, all odd polynomials,
all ten feasible disk rows and both infinity rows. Selected full values
were also inspected with the scoped JSON inspector. This is full
arithmetic replay within the reproduction, not the later independent
critical mathematical audit of the proof and its source application.

The result supplies a local membership filter on future supported
representatives. It computes no global units or ordinary S-class
two-torsion, removes no identified global class, controls no surviving
cover points, and recovers no degree-nine distinguished root or remaining
factor. Both L095 integer systems, minus-eleven and the general Beal
gap remain open. The known rational infinity points preclude an empty
fake-Selmer-set shortcut. Preserve L108, ATTEMPTS/050–052 and the
three-/eleven-adic equality stops. This is an instance reproduction
of assessed known methods, not progress beyond their general theory.

### Independent critical mathematical audit, 2026-10-23

The audit approved before invocation by
`drafts/literature/2026-10-23-marked-octic-two-adic-critical-audit.md`
passes. This validates the local input by reproduction of the cited
methods; it is not a new general result or a global class exclusion.
The direct mathematical inputs remain L113 and L114. No argument or
dependency change is needed.

The exact-field argument is essential. All five Eisenstein coefficient
valuations are checked, and the polynomial identity (2) is verified
before reduction. Polynomial Euclidean inversion of B gives exactly
the displayed r, with v_L(B)=0, r²=2(pi−1), and the zero quartic
residual in (1). Thus r and pi are exact field elements. For beta,
the residual has valuation 12 and the derivative valuation 4, so the
strong Hensel inequality is strict. The chosen root satisfies
v_L(alpha−beta)=8; since v_L(beta−1)=6 this gives
v_L(alpha−1)=6. Adding 2 gives v_L(alpha+1)=4. The identity
pi=1+(alpha²−1)²/32 proves that alpha generates L. If alpha and
−alpha had the same minimal polynomial, a Q2-embedding between their
root fields would preserve v2 extended to the algebraic closure. Their
distances from 1 have valuations 6/4 and 4/4 in that normalization,
a contradiction. Each factor therefore has degree four, they are
distinct, and together exhaust G. This also rules out every rational
branch point, independently of the coordinate tests. The field is not
defined by the Newton approximation.

The two Newton updates are independently recomputed by polynomial
Euclidean inversion, instead of the producer's matrix inversion.
Their full rational coefficient vectors and residuals agree. The
residual valuations are 12,16,24 and the derivative valuation stays
4. The final approximation consequently differs from the same exact
alpha by valuation at least 20. Every integral-center evaluation has
valuation at most six, so its relative error has valuation at least
14>8. In the reciprocal chart q is integral, and its multiplication
only improves the approximation error. No approximate root is used
to prove exact algebra identification or point existence.

For the maximal ring, the four summand valuations 4v2(a_i)+i are
distinct modulo four. Therefore their minimum cannot cancel, and an
element is integral if and only if all four coefficients are integral.
This proves O_L=Z2[pi]. The condition v_L(x)>=9 is exactly that its
coefficients lie in 8Z2,4Z2,4Z2,4Z2 respectively. These additive
bounds describe the ideal pi^9 O_L, so reduction of the actual
polynomial multiplication gives its ring structure. Every nonzero
field square class has one valuation parity and one unit square class.
A unit that is a square modulo this ideal differs from a lifted unit
square by relative valuation at least 9>2v_L(2)=8; Hensel makes that
condition sufficient as well as necessary. The audit enumerates every
one of the 256 units, their eight square residues, and all 32 disjoint
cosets. It independently reconstructs the multiplication tensor and
the entire unit-class multiplication table. All entries agree, fixing
the label convention and all 64 field classes without a sample-based
completeness assumption.

The norm calculation uses a different determinant presentation:
for each of the 64 independently constructed representatives u, it
computes Res(E,u) from the full Sylvester matrix. Because E is monic,
this is the product of u at its four roots, hence the field norm.
Fraction-free rational elimination retains every matrix and pivot
trace. All full rational norms and both components of their rational
square labels agree with the original data. Each of the eight norm
labels occurs eight times. All 4096 class products preserve these
labels. Every rational scalar representative is normalized directly
in L; the eight distinct labels form the claimed subgroup. Its diagonal
action is free: fixing even one component forces the scalar square
class to be identity. Its norms are rational fourth powers, so it
preserves the norm fiber. All 512 raw pairs and all 64 common-scalar
orbits are recomputed and compared in full. Independent scalar choices
in the two components are never allowed.

For exhaustive point coverage, every finite t is either integral or
has q=1/t in 2Z2. Both even-chart polynomials, G(2u) and G_rev(2u),
are checked coefficientwise to be 1 modulo 8. They therefore have
nonzero square values for every u in Z2. All eight full odd shifted
polynomials G(a+16u) are recomputed; the constant terms have valuation
ten, and every nonconstant coefficient has valuation at least thirteen.
Consequently division by 2^10 leaves the odd unit unchanged modulo 8
throughout the disk, not merely at its center. Exactly a=3,13 permit
points. For an odd t, the distances t−alpha and t+alpha have valuations
(6,4) when t=1 modulo 4, and (4,6) when t=3 modulo 4: in each
comparison the two summands have unequal valuations, so cancellation
is impossible. Changing t by 16 changes either component by valuation
at least 16>6+8. Even t and reciprocal q have unit components, and
their modulo-eight changes have valuation at least 12>8. These are
uniform bounds for every member of each disk. For every nonzero
q in 8Z2, v_L(q alpha)>=12>8 proves both components square, covering
all tail valuations without a finite depth cutoff. This accounts for
all coordinate disks and supplies the necessary containment argument.

Every full feasible disk row, including its curve value, square label,
component valuations, strict bound and scalar projection, is recomputed.
The finite centers t=0,2,3 and reciprocal centers q=2,8 have even
curve valuation and normalized unit 1 modulo 8. Dividing out that
even valuation and applying strong Hensel at 1 gives actual Q2 square
roots; these are exact points and realize all five classes. Negative
rational values in this list cause no two-adic obstruction. The two
Y signs have the same evaluation, since no finite branch case occurs.
Thus the independently recovered set is exactly
{(0,0),(0,5),(0,8),(0,22),(2,6)}; no subgroup closure is assumed.

At infinity, L113's smooth chart has the two distinct points Z=−55
and Z=55: 2Z is nonzero in Q2, which suffices for smoothness even
though it is not a two-adic unit. L114 imports Bruin–Stoll Section 2
p.3's evaluation [3025] at each point. Since 3025=55² this is the
identity in both factors; its norm is square as required. Both separate
rows are verified and retained. The expression q(1−q theta) is never
evaluated at q=0. These known rational points still prevent an empty
fake-Selmer-set argument.

Reproduce the independent arithmetic with

    python3 scripts/pair-genus-two/audit_marked_octic_two_adic_image.py

The full evidence is
`scripts/pair-genus-two/marked-octic-two-adic-image-audit-certificate.json`.
It imports neither producer nor replay and uses only Python's standard
library. All 102 checks pass, with no failures. It consumes and compares
every mathematical section of the original certificate, including all
cosets, norms, raw/quotient pairs, shifted polynomials and point rows;
it does not rely on the producer's check flags. Actual/required residue
precision is 9/9, alpha error is 20>14, and component bounds are
12>8,16>14,12>8. Full load-bearing rows were also inspected directly.

The initial audit run had one aggregate record-comparison failure:
the ten curve values were computed as exact integers whereas the
producer serialized the same values as rational strings. Every value
agreed mathematically. Using exact Fraction values for that serialization
resolved the mismatch. The initial full evidence is preserved in
`scripts/pair-genus-two/marked-octic-two-adic-image-audit-initial-check-failure.json`.
No mathematical statement or original certificate was changed. The
source application is the unchanged integral squarefree characteristic-
zero dyadic case of the cited Bruin–Stoll method, with strict square
neighborhoods replacing the general recursion by exhaustive disks.
The proof above supplies the containment and realization obligations;
arithmetic equality alone would not establish them.

This confirms 5<64 as a strict necessary local filter. Global supported
representatives, units, ordinary S-class two-torsion, surviving-cover
points, degree-nine root recovery, remaining factors, both L095 systems
and minus-eleven are still unresolved. No global class has been shown
removed by this audit, and Beal remains IN_PROGRESS.

## Mathlib

Full coverage of the Bruin–Stoll dyadic fake point-image algorithm,
its even-degree common scalar quotient, these exact quartic transports
and the complete instance tables was not checked. No absence or formal
verification claim is made. The proof uses the precise primary citation,
standard named Eisenstein/strong Hensel results and exact finite arithmetic.
