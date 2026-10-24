# L121 — Exact three-adic fake point image of the marked octic

## Hypotheses

Use L113's smooth proper marked curve C over k=Q3,

    Y²=G(t)=3025t⁸−31460t⁶+76230t⁴−39204t²+2673,

and L114's even-degree fake map. Retain the entire algebra
A3=k[theta]=k[t]/(G) and the single common scalar quotient

    H3={delta in A3*/(A3*² k*): N(delta) in 3025 k*²}.

No global supported-class enumeration, class-group computation,
rational-point completeness or integer-lifting assumption is made.

## Conclusion

The entire algebra is the product L × U of a totally ramified
degree-six field and an unramified quadratic field. The exact models
and images of theta are specified below. The full norm-admissible
scalar quotient and exact fake point image are

    H3={[1]}, mu(C(k))={[1]}.

There are no points with integral t, and no k-rational branch points.
Every nonintegral t gives exactly two affine points, both of identity
fake class. Both distinct infinity points also have identity image.
An exact finite realization has t=1/3.

This equality stops additional fake-class pruning at three in this
quotient. It is a reproduction of assessed known local methods, not a
global class exclusion, rational-point determination or Beal exclusion.
The separate independent critical audit below confirms these claims.

## Proof

### Imported methods and scope

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-three-adic-point-image.md`.
Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
inspected [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008. Section 2 p.3 gives the map, norm fiber and exceptional
evaluations. Section 4 pp.6–11, especially Lemma 4.4 p.8 and the complete
SquareClasses/LocalImage explanations pp.9–11, covers finite local fields,
bad polynomial reduction and all factors. The full primary extraction in
the five-adic assessment is reused as approved. L113 supplies the actual
squarefree integral polynomial and smooth proper charts; k has the
required characteristic zero and finite residue field. Its discriminant
valuation 27 does not satisfy the shortcut in Lemma 4.3, which is not used.

We compress the chart calculation by uniform fieldwise bounds, rather
than claim execution of the recursive pseudocode. Use the standard named
simple-root Hensel lemma, Hensel's irreducible-reduction unramified-extension
theorem, and the Eisenstein extension theorem over a complete discretely
valued field. At odd residue characteristic a unit with square nonzero
residue is square: the simple-root lemma applies to X²−u at a lift of
either nonzero residue root. Thus every principal unit is square.
These general inputs are imported, not reproved as new results.

### Exact whole algebra and theta transports

Put

    P(u)=3025u⁴−31460u³+76230u²−39204u+2673,
    G(t)=P(t²).

Modulo three, P(u)=u³(u+1). Its root 2 is simple, with P'(2)=2 mod 3.
Hensel gives a unique u0 in 2+3Z3 satisfying P(u0)=0. Define exactly

    b0=−2673/(3025*u0),
    b2=(b0+39204/3025)/u0,
    b4=(b2−76230/3025)/u0,
    H(t)=t⁶+b4*t⁴+b2*t²+b0.

Then

    G(t)=3025(t²−u0)H(t).                            (1)

Here is a complete algebraic verification, not an approximate
factorization. For an indeterminate u, the three b coefficients have
common denominator 3025u³ and numerators respectively

    −2673u², 39204u²−2673u, −76230u²+39204u−2673.

After clearing that denominator,

    (t²−u)*(3025u³ H(t))−u³G(t)=−P(u)t⁶.

The right side vanishes at u0; every coefficient of (1) follows.
Since u0 and 3025 are units,

    v3(b0)=5, v3(b2)=4, v3(b4)=2,
    b0/3⁵=−11/(3025*u0)=2 mod 3.                    (2)

Indeed the two terms defining b2 have distinct valuations 5 and 4,
and those defining b4 have distinct valuations 4 and 2, so cancellation
cannot change these valuations.

The factor t²−u0 has irreducible reduction t²+1 over F3. Thus

    U=k(omega), omega²=u0

is the unramified quadratic field, with residue field F9, and its
component of theta is exactly omega, a unit.

For the entire remaining factor set r=3/t and define

    E(r)=r⁶+(9b2/b0)r⁴+(81b4/b0)r²+729/b0.

The exact identity is E(r)=r⁶ H(3/r)/b0. Its nonleading nonzero
coefficients all have valuation one by (2). Consequently E is monic
Eisenstein. The field

    L=k[r]/(E)

has degree six, ramification index six and residue field F3; r is a
uniformizer. Both E and H have nonzero constants. The maps t=3/r and
r=3/t therefore give inverse isomorphisms between k[t]/(H) and L,
so H itself is irreducible. Normalize v_L(r)=1, v_L(3)=6. The actual
theta in this factor is 3/r, with v_L(theta)=5.

The two factors in (1) are coprime: their roots have base valuations
0 and 5/6 respectively. Chinese remaindering now gives the explicit
full identification

    A3 ≅ L × U, theta -> (3/r,omega), (e,f)=(6,1),(1,2).       (3)

The inverse maps and the degree sum 6+2=8 retain all factors and the
original twist G, not G/11. Neither factor is linear, so there are
no rational roots of G and no rational branch evaluations to insert.
No L117 prime decomposition or uncertified field identification is used.

### Complete square classes, norms and the single scalar quotient

Write eta=1+omega in U. Every raw square class has a unique label

    (r^a*(-1)^b, 3^c*eta^d), a,b,c,d in {0,1}.        (4)

For L, valuation parity and the two residue classes of F3* prove this,
with −1 a nonsquare unit. For U, 3 is a uniformizer. In its residue
field write w for omega, so w²=2. Then eta has residue norm
1−2=2 in F3*, hence is nonsquare. Indeed for any x in F9*,
N(x)=x⁴, and x is square exactly when x⁴=1, which is exactly when
N(x) is square in F3*. This identifies both residue square-class groups.
Hensel lifting supplies sufficiency in each field. Valuation and residue
parity also prove uniqueness of (4).

In k*/k*² use labels for powers of (3,−1). The full norm table is

| component | generator | exact norm | label |
| --- | --- | --- | --- |
| L | r | 729/b0 | (1,1) |
| L | −1 | 1 | (0,0) |
| U | 3 | 9 | (0,0) |
| U | eta | 1−u0 | (0,1) |

The norm of r is the constant coefficient of its monic degree-six
minimal polynomial. Its valuation is one and its normalized unit is
243/b0=2 mod 3 by (2). The other entries follow directly from the
degree and quadratic conjugation. Therefore the norm of (4) is

    (a,a+d) over F2.                                 (5)

The required leading coefficient 3025=55² is square, so norm
admissibility is exactly a=d=0. All four raw norm-kernel labels remain
to be quotiented by the ONE common embedded k*.

That scalar image is as follows. The scalar −1 is nonsquare in L
and square in U, since its residue 2 is w² in F9. It has label
(0,1,0,0). To label 3 in L, divide E(r)=0 by three:

    r⁶/3=−(3b2/b0)r⁴−(27b4/b0)r²−243/b0.

The first two coefficients are integral units by (2), and r has
positive valuation. Thus r⁶/3 has residue −243/b0=1. It is a
unit and is square by Hensel; r⁶ is also square. Hence 3 is square
in L. In U it is the chosen uniformizer, so the common scalar 3
has label (0,0,1,0). Since k*/k*² is generated by 3 and −1, the
scalar image is exactly these two independent directions. Both have
trivial norm, also consistent with scalar norms being eighth powers.

For a fixed label convention use the unique representative b=c=0
of each scalar orbit; do not substitute lexicographic labels for this
section. There are four raw scalar orbits, indexed by (a,d). By (5)
only (a,d)=(0,0) is norm-admissible. Consequently

    H3={[1]}.                                       (6)

This computes all raw classes, both norm bits and all common-scalar
collisions; no independent scalar quotient in each factor or subgroup
assumption on a point image is involved.

### Every integral disk is excluded

The ascending valuations of the nonzero coefficients of G are
5,4,2,0,0, at powers 0,2,4,6,8. If t is a unit, reduction gives

    G(t)=t⁶(t²+1)=2 mod 3,

which is a nonsquare unit. If t is nonzero with n=v3(t)>=1, the
five term valuations are

    5, 4+2n, 2+4n, 6n, 8n.

Only the constant term has valuation five. Hence v3(G(t))=5,
which is odd, for every such t. At t=0 the same value five holds
directly. This resolves all three integral residue disks and every
refinement; there are no integral points or unclosed disks.

### Entire reciprocal tail, exact realization and both infinities

For nonintegral t put q=1/t, n=v3(q)>=1. L113's proper chart is

    Z²=3025 S(q), Z=Y/t⁴,
    S(q)=1−(52/5)q²+(126/5)q⁴−(324/25)q⁶+(243/275)q⁸.

The four error terms have valuations

    2n, 4n+2, 6n+4, 8n+5,

respectively, with minimum at least two. Thus S(q) lies in
1+9Z3 uniformly in the unit part and all n>=1. Its unique square
root congruent to one modulo three exists by Hensel, and its negative
is the only other root. For q nonzero, Z=±55 sqrt(S(q)) and
Y=Z/q⁴ give exactly two distinct affine points at every such t.

In L, v_L(q*theta)=6n+5>=11; in U the normalized valuation is
n>=1. Both are strictly positive. Therefore in the entire algebra

    t−theta=t(1−q*theta)

is one common scalar t times a square in each factor. All these
points have identity fake class. These universal bounds cover the
infinite tail, rather than extrapolate finitely many residues.

For an exact finite realization choose q=3, t=1/3. Direct evaluation
gives S(3)=−467968/275, with v3(S(3)−1)=2. Define X to be the
unique root of X²=S(3) congruent to one modulo three; its Hensel
derivative is 2 mod 3. Set Z=55X and Y=55X/3⁴. The exact chart
identity gives Y²=G(1/3), and its fake image is identity. This defines
an exact Q3 point, not an asserted rational square of the radicand.

At q=0 the smooth chart has two separate points Z=−55 and +55,
with nonzero derivatives −110 and +110. L114's imported infinity
convention assigns each representative 3025=55² and identity image.
Both rows are retained; neither is computed by substituting zero in
the noninvertible affine representative q(1−q*theta).

The integral chart, nonzero reciprocal coordinates in 3Z3, and these
two infinity points exhaust C(k) by L113's smooth proper model.
There are no rational branch points. Thus the computed identity
image is exact and nonempty, with finite realization as well as
both infinity realizations. Alternatively (6) and either infinity
point already prove equality once the norm target has been computed.
Image/ambient=1/1 fails the strict-pruning test and stops additional
fake-class pruning at three only.

### Complete arithmetic evidence and limits

Run `python3 scripts/pair-genus-two/marked_octic_three_adic_image.py`.
The full evidence is
`scripts/pair-genus-two/marked-octic-three-adic-image-certificate.json`.
All 39 arithmetic checks pass, with no failures. The certificate stores
all seven Hensel digit steps, the exact denominator-cleared identity,
all coefficient bounds, all 16 raw square labels and their scalar
orbits, all norm/scalar generators, the three integral disks, four
reciprocal error bounds, both factorwise class bounds, the finite
realization and both infinity rows. These complete relevant fields were
inspected using the shared JSON inspector. Exact models use u0 as the
specified Hensel root; displayed rational coefficient approximants are
labeled as approximants and are not substituted for the exact field.
The algebraic identities and universal arguments above, not sampled
rows or printed flags, justify all infinite assertions.

This is a completed specialization of known methods. Its direct inputs
are exactly L113 and L114; no progress beyond the general sources is
claimed. The independent critical audit below passes. Supported units,
ordinary S-class two-torsion, surviving-cover points, degree-nine root
recovery, compatible remaining factors, both L095 integer systems and
minus-eleven remain unresolved. Neither this equality nor eleven's
equality reopens ATTEMPTS/052 or excludes any global supported class
without its actual localization. Preserve ATTEMPTS/050–052 and unfinished
L108. Known rational boundary points still forbid an empty fake-Selmer
set shortcut; no signature or the full Beal target is settled.

### Independent critical audit, 2026-10-23

The approved audit confirms the complete conclusion without correction.
This is verification of the instance input by reproduction, not a new
general theorem or a stronger local or global conclusion. The direct
mathematical inputs remain L113 and L114. No L117 decomposition, finite
Hensel approximant as a field, or global class assumption is used.

The independent script
`scripts/pair-genus-two/audit_marked_octic_three_adic_image.py` imports
no producer code. Run it with
`python3 scripts/pair-genus-two/audit_marked_octic_three_adic_image.py`.
Its complete evidence is
`scripts/pair-genus-two/marked-octic-three-adic-image-audit-certificate.json`.
All 64 checks pass, with no failures. This consumes and compares the
complete producer Hensel records, coefficient approximants, cleared
identity, residue-field evidence, norm/scalar generators, all 16 raw
labels and every chart/realization row. Producer check flags are read
only as bookkeeping; they are not premises of the audit.

For an independent exact algebra verification, write P_i for the
ascending coefficients of P and work formally in Q[u]/(P). No field
or irreducibility claim about this auxiliary algebra is needed. Since
P_0 is nonzero, u is invertible, with

    u^(-1)=−(P_1+P_2*u+P_3*u²+P_4*u³)/P_0.

Synthetic division from the leading end gives

    h4=u+P_3/P_4,
    h2=u*h4+P_2/P_4,
    h0=u*h2+P_1/P_4,
    u*h0+P_0/P_4=0.

The independent rational-vector computation verifies that these h0,h2,h4
equal the constant-end b0,b2,b4 expressions above in this algebra. It also
checks the full denominator-cleared identity over Q[u,t], before reduction
modulo P, and every coefficient of the reciprocal polynomial. Evaluating
at the unique exact Hensel root u0 is legitimate because P(u0)=0 and
u0 is a unit. Thus the exact factor and reciprocal identities follow
without substituting a finite approximation for u0. Newton digit correction
independently reproduces all seven saved lifting steps and all three
candidate errors at every step; the last residue is 1256 modulo 6561.
Those records verify only the displayed approximants.

For every u in 2+3Z3 the b0 formula has valuation five. The summands
in b2 have valuations five and four, and those in b4 have valuations
four and two. Each minimum is unique, giving the exact valuations
5,4,2 without any precision assumption. The three lower nonzero
coefficients of E have valuations 6−5=1, 4+2−5=1 and 2+4−5=1.
Its monicity and Eisenstein condition therefore hold at the exact root.
The inverse substitutions r=3/t and t=3/r are valid since both constant
coefficients are nonzero. They give the entire degree-six field, with
v_L(theta)=6−1=5. The other factor has residue polynomial t²+1, with
no root in F3, hence is the whole unramified quadratic field with unit
theta. Distinct root valuations give coprimality of these factors.
The degree sum is eight; neither factor supplies a rational branch point.

The normalized residues b0/243=2, N(r)/3=2 and r^6/3=1 are checked
from u0=2 mod 3. In the last calculation the coefficients of r^4 and
r² after dividing E by three are integral, while those terms have
positive valuation. This proves that the scalar 3 is square in L.
The full eight-element table of F9* independently checks the residue
norm criterion: a residue is square exactly when its norm is 1.
In particular −1 is square in U and eta=1+omega is not. The ordinary
norm of r is the positive constant of its degree-six monic polynomial;
the other generator norms are 1,9,1−u0. Thus the norm bits really are
(a,a+d), including the unit bit. All 16 raw rows, all four-element
common scalar orbits and their unique b=c=0 representatives agree.
The raw norm kernel has order four and equals the scalar image generated
by −1 and 3. Quotienting once gives exactly one norm-admissible class.
No componentwise scalar quotient or subgroup hypothesis for the point
image occurs.

The chart verification checks stronger assertions than nonempty ambient
equality alone. On the two unit residue disks the full twisted G reduces
to 2. On 3Z3 the constant has valuation five and the other terms have
minima 6,6,6,8, with positive slopes as v3(t) increases; t=0 is handled
directly. Hence every integral point is excluded. On the entire nonzero
reciprocal disk the four error minima are 2,6,10,13 with positive slopes.
They are all strictly greater than zero, the sufficient square threshold
in odd residue characteristic. This proves S(q) is a nonzero square for
every q in 3Z3, not just the sampled residues. Likewise the two class
bounds have minima 11 and 1 and positive slopes. Both 1−q*theta
components are square, after removing exactly the same scalar t.
There are exactly two points at every nonintegral t, since their squared
ordinate is nonzero in a characteristic-zero field.

The finite realization is checked directly from G(1/3): multiplying by
3^8/55² gives −467968/275. Its difference from 1 has valuation two,
and the derivative at the residue root 1 is 2. Hensel therefore supplies
the exact X and Y specified above; rational squareness is not asserted.
At infinity the separate rows Z=−55 and Z=55 satisfy the chart equation,
and their derivatives are units in Z3. Bruin–Stoll Section 2 p.3 assigns
each the invertible representative 3025. Its norm divided by the required
leading coefficient is 3025^8/3025=55^14, a square. Both rows are thus
identity in the stated norm fiber, while the smooth points remain distinct.

L113's two smooth proper charts cover all k-points. The imported local
square criterion applies to both complete fields even with wild
ramification, since the residue characteristic is three and the square
root derivative 2 is a unit. No good-reduction hypothesis or the
inapplicable small-discriminant shortcut is used. The ready Bruin–Stoll
coverage cited above supplies the actual even-degree map and exceptional
conventions; the proof uses uniform square bounds, not a claim to have
executed the recursive algorithm. These checks confirm image/ambient=1/1,
failing the strict-pruning threshold image<ambient. The argument assembly
and dependency DAG require no change. All global limitations stated above
remain, including the known-boundary obstruction to an empty fake Selmer set.

## Mathlib

Full matching coverage of this exact octic image and the Bruin–Stoll
finite-local algorithm is not checked. Supporting identifiers for local
square classes, Hensel lifting and Eisenstein/unramified extensions have
not been checked. Unknown coverage is not evidence of absence.
