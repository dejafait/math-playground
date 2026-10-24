# L120 — Exact eleven-adic fake point image of the marked octic

## Hypotheses

Use L113's smooth proper marked curve C over k=Q11,

    Y²=G(t)=3025t⁸−31460t⁶+76230t⁴−39204t²+2673,

and L114's actual even-degree fake map. Retain the entire algebra
A11=k[theta]=k[t]/(G) and one common scalar quotient

    H11={delta in A11*/(A11*² k*): N(delta) in 3025 k*²}.

No global supported-unit or class-group calculation is assumed.

## Conclusion

The entire local algebra is the single field

    L=k[r]/(E(r)/243),
    E(r)=243r⁸−3564r⁶+6930r⁴−2860r²+275,
    theta=1/r.

It has degree eight, ramification index eight and residue field F11;
r is a uniformizer. The full norm-admissible scalar quotient H11 is
the singleton {[1]}, and the exact fake point image equals H11.
Thus eleven gives no additional fake-class pruning in this quotient.

There are no points with t in Z11 and no rational branch points.
Every t with v11(t)<0 has exactly two points on the affine curve,
both with fake image [1]. Each of the two distinct infinity points
also has image [1]. A finite exact realization is given below.
This is a known-method instance calculation; it supplies no global
supported-class exclusion, rational-point completeness or integer
exclusion. The separate critical audit below confirms these assertions.

## Proof

### Imported methods and exact local model

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-eleven-adic-point-image.md`.
Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
using the inspected [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008. Section 2 p.3 defines the fake map, norm target and
exceptional evaluations. Section 4 pp.6–11, especially Lemma 4.4 p.8
and LocalImage pp.10–11, permits bad reduction, ramified local fields
and nonunit leading coefficients. Reuse the complete source extraction
in the five-adic assessment. The general algorithm is not reproved.
Here uniform chart estimates compress the search completely; no
unexecuted disk algorithm is asserted to have run.

Use also the standard Eisenstein extension theorem for a complete
discretely valued field and the simple-root form of Hensel's lemma.
For odd residue characteristic the latter implies: a unit is a square
exactly when its residue is a square; in particular every principal
unit is square. Indeed a nonzero residue square root has unit
derivative 2 times that root. These are imported standard results,
not proposed new local-field theorems.

Direct coefficient comparison gives

    G(t)=11t⁸ E(1/t).                                (1)

The leading coefficient 243 of E is an eleven-adic unit. Its nonzero
lower coefficients have valuations one: 275=11*25,
−2860=−11*260, 6930=11*630 and −3564=−11*324, and none of
25,260,630,324 is divisible by eleven. Thus E/243 is monic
Eisenstein. It is irreducible over k and its root r generates a
degree-eight totally ramified extension with residue field F11 and
uniformizer r. Normalize v_L(r)=1, so v_L(11)=8.

The nonzero constant coefficient of G makes theta invertible in A11.
Equation (1) gives inverse algebra maps r -> theta^(-1) and
theta -> r^(-1), between two degree-eight algebras. Hence these are
isomorphisms, identifying the entire original algebra and its actual
theta, not a field inferred from ramification degrees. In particular
G has no root in k: a rational root would yield a root of the
irreducible E. There are no rational branch evaluations to add.
All subsequent square classes refer to this exact model; replacing G
by G/11 as a curve equation has not occurred.

### Complete square classes, norms and common scalars

The nonzero squares in F11 are exactly {1,3,4,5,9}, so −1 is
nonsquare. Every element of L* is a power of r times a unit; a unit
has precisely the two classes distinguished by its residue. Hensel's
lemma proves sufficiency of a square residue. Thus every square class
has the unique label

    [r^a (−1)^b], a,b in {0,1}.                      (2)

Valuation parity distinguishes a, and residue square parity after
removing the valuation distinguishes b. This proves both completeness
and distinctness of all four raw classes.

Since E/243 is the actual monic minimal polynomial and has even
degree,

    N(r)=275/243=11*(25/243), N(−1)=1.

The unit 25/243 reduces to 3, which is square in F11. Therefore in
k*/k*², with generators (11,−1), the exact norm label of (2) is
(a,0). As 3025=55², the norm condition is exactly a=0.

It remains to quotient by exactly the embedded common k*. Rational
−1 has label (0,1) in (2). For rational eleven, the equation E(r)=0
gives

    r⁸/11=(324r⁶−630r⁴+260r²−25)/243.

This unit has residue −25/243=8 in F11. Consequently 11/r⁸ has
residue 7, also nonsquare, and [11]=[−1] in L*/L*².
The standard valuation/residue description over k likewise gives
k*/k*² generated by 11 and −1. Hence its entire image in L*/L*²
is exactly {1,−1}. This also follows from every rational valuation
being multiplied by eight; there is no hidden odd-valuation scalar.
The two scalar orbits are

    {(0,0),(0,1)} and {(1,0),(1,1)}.

Only the first has square norm. Thus H11 has exactly one class.
The norm is well-defined on the scalar quotient because a scalar
has norm its eighth power. This computation compares with the full
norm ambient, not an ambient having some additional local restriction.

### Exhaustive integral chart

For any t in Z11, all nonconstant coefficients of G are divisible
by 11², while G(0)=11*243. Therefore

    G(t)/11 = 243 = 1 mod 11, v11(G(t))=1.

Odd valuation excludes a square, so all eleven residue disks and
every deeper subdisk contain no point. There is no unresolved zero
disk. Consistently, for any such t,

    t−theta=−r^(-1)(1−tr), v_L(tr)>=1

(with t=0 treated as exact equality). The last factor is square by
the strict principal-unit bound >0, and the raw class has a=1,
whose norm is not square. This is a consistency check, not a
substitute for the square obstruction in G.

### Exhaustive reciprocal chart, infinite tail and finite realization

For every nonintegral t put q=1/t and n=v11(q)>=1. The base
coordinate q is distinct from the field uniformizer r. L113's chart
is

    Z²=3025 S(q), Z=Y/t⁴,
    S(q)=1−(52/5)q²+(126/5)q⁴−(324/25)q⁶+(243/275)q⁸.

The four error terms have valuations 2n,4n,6n,8n−1 respectively.
Their minimum is at least two, strictly greater than zero. Thus
S(q) is in 1+11² Z11 for every q in 11 Z11, independently of its
unit part and with no cancellation assumption. Hensel's lemma at
the seed 1 supplies its unique principal square root. For q!=0,
Z=±55 sqrt(S(q)) and Y=Z/q⁴ give exactly two affine points.
S(q) is a nonzero unit, so these two are distinct.

The actual theta has v_L(theta)=−1, whereas v_L(t)=−8n. Hence

    t−theta=t(1−theta/t),
    v_L(theta/t)=8n−1>=7>0.

The parenthetical factor is square in the entire field, uniformly
over all n>=1 and all units. The remaining factor t is ONE common
k* scalar. Thus every such point has fake image [1]. This also
proves directly that the entire reciprocal tail has constant fake
class, without extrapolating finite approximations.

For an exact finite realization take t=1/11, q=11. Exact evaluation
gives S(11)=4170589184/25, with v11(S(11)−1)=2. The equation
X²−S(11)=0 has seed X=1 modulo eleven and derivative 2, a unit.
Define X to be its unique root equal to 1 modulo eleven, and set
Z=55X, Y=Z/11⁴. These satisfy the original curve exactly and give
the identity fake class. A stored rational radicand is not asserted
itself to be a rational square.

### Both infinity points and exact image

At q=0, the smooth chart has Z=−55 and Z=+55. Their derivatives
in Z are −110 and +110, nonzero in k, so both are distinct smooth
points (no good-reduction assertion is needed). L114, using
Bruin–Stoll Section 2, assigns each the representative 3025=55²
and image [1]. Do not evaluate the noninvertible affine expression
q(1−q theta) at q=0. The two points remain separate rows.

The integral chart, q in 11 Z11 with q!=0, and these two infinity
points exhaust C(k). There are no rational branch points by (1).
Every chart image has been computed, and the finite realization
already realizes the sole class. Alternatively norm containment
and either infinity point prove exactness once H11 is known to be
a singleton. Consequently mu(C(k))=H11={[1]}. Equality, 1=1,
fails the proposed properness test and stops extra fake-class
pruning at eleven. It does not imply that all global supported
classes survive this place; their norm membership must first hold.

### Arithmetic evidence and limits

Reproduce with
`python3 scripts/pair-genus-two/marked_octic_eleven_adic_image.py`.
The full certificate is
`scripts/pair-genus-two/marked-octic-eleven-adic-image-certificate.json`.
It records the reciprocal identity, all Eisenstein valuations, the
complete 8-by-8 multiplication matrix for r and its exact rational
determinant, all four raw labels and both scalar orbits, all eleven
integral residue rows, every reciprocal coefficient and strict bound,
the finite Hensel definition and both infinity rows. All 23 arithmetic
checks pass with no failures. The full relevant fields were inspected
using the shared JSON inspector. The universal valuation arguments
above justify the infinite tails; finite rows alone are not their
proof. This producer calculation is not an independent critical audit.

The direct inputs are L113 and L114. No L117 decomposition is needed.
This reproduces known local methods, without progress beyond the
sources checked. Supported units, ordinary S-class two-torsion,
other local images, rational points on surviving covers, degree-nine
root recovery, compatible remaining factors, both L095 integer
systems and the minus-eleven alternative remain open. Known boundary
points still prevent empty fake-Selmer-set exclusion. Preserve the
parked backend and prior failures; equality here is not a global ban
on local methods or a Beal signature exclusion.

### Independent critical audit (2026-10-23)

The prior SPECIALIZE assessment
`drafts/literature/2026-10-23-marked-octic-eleven-adic-critical-audit.md`
approved this audit. It confirms the statement without a mathematical
correction, by reproduction of the cited methods. The direct inputs
remain exactly L113 (actual curve and smooth proper charts) and L114
(entire fake map, norm fiber, scalar quotient and infinity convention).
Neither L117 nor global class arithmetic is used. This verification
does not strengthen the local theorem or certify any global exclusion.

**Entire field and same theta.** Independently reverse the coefficients
of L113's actual G and divide by eleven. The result is exactly E, with
coefficient valuations (1,infinity,1,infinity,1,infinity,1,infinity,0).
Thus the named Eisenstein theorem applies to E/243 over Q11, proving
degree eight, e=8, f=1 and v_L(r)=1. The explicit inverse is

    theta=(52/5)r−(126/5)r³+(324/25)r⁵−(243/275)r⁷.

Exact polynomial reduction modulo E/243 verifies r*theta=1 and
G(theta)=0 in all eight coordinates. Conversely E(theta^(-1))=0
follows from the coefficient identity (1) in A11; theta is invertible
because G has nonzero constant term. These mutually inverse maps
identify the entire algebra and actual generator. They also rule out
a rational root of G, hence any missing rational branch evaluation.

**Full quotient.** The complete residue square set is {1,3,4,5,9}.
After removing a power of r, every unit has one of the two residue
classes, and Hensel lifts every nonzero residue square. Distinctness
comes from valuation parity and then residue parity. Thus the four
raw representatives 1,−1,r,−r are exhaustive. Independent quotient
multiplication constructs every entry of the multiplication matrix of
r; a Leibniz determinant, rather than the producer's elimination,
gives N(r)=275/243. Its normalized unit has residue 3, so the norm
labels of those four rows are respectively (0,0),(0,0),(1,0),(1,0).
The target 3025 is square. No norm-admissible row is omitted.

Reduction of r^8/11 gives exactly

    −25/243+(260/243)r²−(70/27)r⁴+(4/3)r⁶.

All coefficients are integral over Q11; the positive powers have
positive L-valuation. Its residue is 8, so 11/r^8 has residue 7.
This proves [11]=[−1], using that r^8 is square. The rational square
classes generated by 11 and −1 therefore have image exactly {1,−1}.
Quotienting by this single scalar image gives two orbits; only the
even-r-valuation orbit has square norm. The full H11 is consequently
{[1]}. Scalar norms are eighth powers, so this condition descends to
the quotient. This conclusion does not assume subgroup closure of a
point image or good reduction.

**Universal chart verification.** The coefficient valuations of G
are (1,infinity,2,infinity,2,infinity,2,infinity,2). For every integral
t the constant term has strictly smaller valuation than every other
nonzero term, yielding v11(G(t))=1; the eleven residue rows and all
their refinements are excluded. For t=0 the same obstruction holds.
The consistency calculation for t−theta uses v_L(tr)>=1 (or tr=0),
strictly inside the square neighborhood at odd residue characteristic.

For q=1/t with n=v11(q)>=1, exact coefficient division by 3025 gives
the four S(q) error valuations 2n,4n,6n,8n−1. Each is increasing
with n; their respective minima are 2,4,6,7. Hence the sum has
valuation at least two for every unit part and every n, including all
infinite tails. Cancellation can only increase that valuation.
Hensel at 1 yields a unique square root congruent to 1 mod 11;
its negative gives the other root. Since S(q) is a unit, these are
exactly two distinct points for each nonzero q in 11 Z11. In L,
v_L(q theta)=8n−1>=7>0, so 1−q theta is square and t−theta is one
rational scalar times a square. Thus both points have identity image.
These are uniform inequalities, not a finite-precision extrapolation.

**Realizations and coverage.** At q=11 the independent evaluation
gives S=4170589184/25 and v11(S−1)=2. The root X=1 mod 11 of
X²=S exists with unit derivative 2; Y=55X/11^4 and t=1/11 satisfy
the original equation, as checked by the exact chart identity.
Neither X nor Y is claimed rational. At q=0 the two solutions Z=−55
and +55 have nonzero derivatives −110 and +110 in Q11. L114's
imported convention gives each representative 3025 and identity
class, without evaluating an affine expression at zero. Smoothness
over Q11 does not require those derivatives to be integral units.
L113's proper two-chart model covers every point: integral t,
nonintegral t with q in 11 Z11 minus zero, and both infinity rows.
The stronger point assertions are therefore verified independently
of the shorter norm-singleton argument.

**Complete arithmetic evidence.** Run
`python3 scripts/pair-genus-two/audit_marked_octic_eleven_adic_image.py`.
It does not import or execute the producer. Its full certificate is
`scripts/pair-genus-two/marked-octic-eleven-adic-audit-certificate.json`.
All 64 checks pass, with no failures. All 18 producer payload fields
are reconstructed and compared completely, including the entire
matrix, four raw classes, both scalar orbits, eleven integral rows,
all reciprocal coefficients/bounds, finite realization and both
infinity rows; producer check records are checked only afterward for
consistency. Complete producer fields and the independent inverse,
uniform bounds and failure list were inspected with the JSON inspector.
The field/square-class theorems and universal arguments above supply
the logical implications; matching stored flags alone is not proof.
The result remains image/ambient=1/1, whereas strict pruning would
require fewer than one image class. This secures the local stop only.

## Mathlib

Full matching coverage of this exact octic image and the Bruin–Stoll
finite-local algorithm is not checked. Supporting Mathlib identifiers
for Eisenstein extensions, Hensel lifting and local square classes
have not been checked. Unknown coverage is not evidence of absence.
