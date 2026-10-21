# L112 — The marked elliptic quotient has positive rank

## Hypotheses

Use L111's smooth proper genus-one curve over Q

    E: R²=g(T)=825T⁴+2112T³+198T²−1716T−231,
    O_E=(2,165).

Its marking remains h²=3(4−T²). No rational marked lift, open
pair, rational distinguished root or integer solution is assumed.

## Conclusion

The Mordell–Weil rank of (E,O_E) over Q is at least one, hence
is not zero. An integral short model of its Q-Jacobian is

    E': y²=x³−2874960x+1739350800.

The point P=(1936,−58564) on E' has infinite order, certified by

    2P=(149284/121,11160692/1331).

This stops a finite elliptic-point enumeration based on rank zero.
It does not determine the exact rank or E(Q), decide marked lifting,
recover the distinguished root, supply compatible remaining factors,
settle either L095 integer system or handle minus-eleven.

## Proof

### Imported results and exact Jacobian

For a nonsingular binary quartic aT⁴+bT³U+cT²U²+dTU³+eU⁴,
import its invariants and Q-Jacobian model from Tom Fisher,
*On binary quartics and the Cassels–Tate pairing*, Research in
Number Theory **8** (2022), article 74, Section 2, p.2,
equations (1)–(2), DOI
[10.1007/s40993-022-00376-z](https://doi.org/10.1007/s40993-022-00376-z),
[author manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/f35e7d09-f88e-4058-959d-b8153d7708cf/content):

    I=12ae−3bd+c²,  J=72ace−27ad²−27b²e+9bcd−2c³,
    E0: Y²=X³−27IX−27J.

For the exact coefficients in the hypotheses these give

    I=8624880, J=−46962471600,
    4I³−J²=360895702709586528000 != 0,
    E0: Y²=X³−232871760X+1267986733200.

Thus Fisher's nonsingularity hypothesis holds, independently also
of L111's audited smoothness. The constant −33 in L111 is retained:
these are the invariants of its actual quartic, not of an untwisted
quartic or just a curve with the same j-invariant.

The scaling X=9x,Y=27y transforms E0 exactly into E'. In fact

    Y²−X³+232871760X−1267986733200
      =729(y²−x³+2874960x−1739350800).

The inverse is x=X/9,y=Y/27; both maps are over Q and extend
over the Weierstrass origins. This is the rational scaling in
Cremona, *Algorithms for Modular Elliptic Curves*, second edition,
CUP 1997, corrected online edition, Chapter III Section 3.1,
pp.62–63, equation (3.1.2),
[Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf).
E' is integral and nonsingular, with discriminant
213864120124199424000; no minimality assertion is needed.

Because O_E is rational, (E,O_E) identifies over Q with its
Jacobian by Q ↦ [Q]−[O_E]. Import this identification from
J.S. Milne, *Elliptic Curves*, BookSurge 2006, Chapter I,
Proposition 4.10, p.35, with the rational-field descent discussion
p.38, [author's text](https://www.jmilne.org/math/Books/ectext6.pdf).
The smooth proper genus-one and rational-origin hypotheses are
exactly those of L111. Consequently a non-torsion point on E'
proves the rank assertion for (E,O_E).

### Exact witness and torsion test

The assessment requests testing the two already known quartic points
first. Cremona, Chapter III Section 3.6, pp.89–90, equations
(3.6.4)–(3.6.8), supplies covariants g4,g6 and the map

    (T,R) ↦ (3g4(T,1)/(2R)², 27g6(T,1)/(2R)³) in E0(Q).

The full specialized covariants, written in ascending powers of T,
are

    g4=[9199872,10349856,31049568,35649504,12074832],
    g6=[4465387872,−5996016576,−46108608480,−69194537280,
        −48765071520,−15483384576,−1302931872].

They satisfy the cited polynomial identity
27g6²=g4³−48Ig²g4−64Jg³. Substitution gives

    g(2)=27225=165²,
    g4(2,1)=632491200, g6(2,1)=−2104614468000.

Hence (2,165) maps to (17424,−1581228) on E0, then to P on E';
(2,−165) maps to its negative. This degree-four covariant map is
not asserted to be a birational inverse or the origin-preserving
identification above. In particular its value at O_E need not be
the group identity. Only the rational Jacobian point is used.

The witness also has a direct arithmetic check independent of the
covariant evaluation:

    (−58564)²=3429742096
              =1936³−2874960·1936+1739350800.

The tangent denominator 2y=−117128 is nonzero, and its slope is

    m=(3·1936²−2874960)/(−117128)=−786/11.

The short-Weierstrass group law gives

    x(2P)=m²−2·1936=149284/121,
    y(2P)=m(1936−149284/121)+58564=11160692/1331.

In particular 2P is an affine nonzero point. Its x-coordinate is
not an integer: gcd(149284,121)=1, with denominator 121>1.
Import Cremona, Chapter III Section 3.3, Proposition 3.3.1, p.69:
torsion points on a nonsingular integral monic cubic model have
integral coordinates. Its hypotheses permit E' as written and do
not require a minimal model. If P had finite order, 2P would have
finite order, contradicting this necessary integrality. Therefore
P has infinite order. The Mordell–Weil theorem then gives rank
at least one, which transfers to (E,O_E) as above.

### Evidence, scope and known traps

Run `python3 scripts/pair-genus-two/elliptic_rank_witness.py`.
Its full certificate is
`scripts/pair-genus-two/elliptic-rank-witness-certificate.json`.
All 23 exact checks pass, with no failures: both images and inverse
scalings, all thirteen syzygy coefficients, nonsingularity, the
point equations and double are checked. Full relevant coefficient,
image and multiple evidence was inspected, not just a preview.
Actual multiples tested: 2; approved cap: 16. The positive-rank
certificate stops the test before the fallback box or finite-field
counts, neither of which is claimed performed. Actual lower bound
is one versus the proposed rank-zero threshold zero. No rank upper
bound, generator claim, descent completeness or BSD premise enters.

The general Jacobian, covariant and torsion results are imported,
not reproved or claimed new. The exact-instance arithmetic is the
necessary specialization under the prior saved SPECIALIZE assessment
`drafts/literature/2026-10-21-marked-elliptic-rank-zero.md`.
Positive rank does not show that infinitely many points lift through
L111's complementary square condition. The boundary origins are not
promoted to open marked pairs or integer solutions. The separate
critical audit below confirms this result; Beal remains IN_PROGRESS.

### Independent critical audit, 2026-10-21

The audit passes without a correction to the statement or mathematical
argument. Its prior SPECIALIZE coverage is
`drafts/literature/2026-10-21-marked-elliptic-positive-rank-audit.md`.
L111's already audited construction supplies the smooth proper
geometrically integral genus-one curve and rational origin. The audit
uses that result, rather than claiming a fresh audit of its dependencies.

First, multiplying L111's exact Q4 by −33 gives precisely the five
coefficients in these hypotheses. Independent invariant evaluation
gives I=8624880 and J=−46962471600. For the latter computation,
432 times the determinant of the symmetric matrix with rows
(a,b/4,c/6), (b/4,c/6,d/4), (c/6,d/4,e) expands to Fisher's J.
The value of 4I³−J² is 360895702709586528000, not zero. Fisher's
cited Q-Jacobian theorem therefore applies to this actual twisted
quartic. The nonsingular original cubic has discriminant
113656161862924666089984000. Substitution X=9x,Y=27y and its
rational inverse verify both coefficients of E', and the original
discriminant equals 3^12 times 213864120124199424000. This is an
origin-preserving Q-isomorphism of the two elliptic models. Neither
equality of j-invariants nor an unproved choice of twist is used.

Second, at O_E the quartic equation gives 165²=27225 and its
R-derivative is 330, so the point is rational and smooth. The
genus-one rational-origin identification cited from Milne I.4.10,
including the perfect-field descent on p.38 equation (9), applies
over Q. Transporting the group law by Q -> [Q]−[O_E] identifies
(E,O_E) with its Jacobian over Q, hence transfers infinite order
and rank from E'. No assertion that the covariant map preserves
this origin is required. In fact the computed covariant image is
affine, whereas the Jacobian identity is the point at infinity.

Third, independent sparse polynomial differentiation recomputes the
specialized covariants. With primes denoting T-derivatives, expanding
3(g')²−4gg'' gives exactly the displayed g4, and expanding
(g g4'−g' g4)/3 gives exactly the displayed g6. These expansions
agree coefficient by coefficient with Cremona (3.6.4), whose signs
and coefficient order were checked directly. All thirteen
coefficients of g4³−48Ig²g4−64Jg³−27g6² vanish. Evaluation at
T=2 gives the displayed 632491200 and −2104614468000. The two
denominators 2R=±330 are nonzero. Both covariant images satisfy
E0 and scale to precisely ±P on E'. Thus the displayed identities
are verified independently of the point's direct existence check.

Fourth, starting anew with P=(1936,−58564), its cubic-equation
residual is zero and the exact tangent slope is −786/11. Let
ell(X)=−58564−(786/11)(X−1936). Direct polynomial subtraction
gives the complete tangent intersection

    X³−2874960X+1739350800−ell(X)²
      =(X−1936)²(X−149284/121).

Reflecting the third intersection in the x-axis therefore gives
the claimed 2P; its cubic-equation residual also vanishes. The
tangent denominator is nonzero, so this is affine rather than O.
Its x-coordinate has gcd(149284,121)=1 and denominator 121>1.
E' is a nonsingular monic cubic with integer coefficients, exactly
the hypotheses of Cremona III Proposition 3.3.1 (p.69). No minimality
condition occurs in that proposition. If P were torsion, its affine
double would be torsion and would have integral coordinates, a
contradiction. The standard Mordell–Weil theorem then yields rank
at least one. This argument requires no upper-rank computation,
conditional analytic input, generators or saturation.

Reproduce the arithmetic with
`python3 scripts/pair-genus-two/audit_elliptic_rank_witness.py`.
It imports no producer code, uses sparse polynomial differentiation
instead of the producer's covariant tables, and verifies the tangent
intersection instead of reusing its point-addition routine. All 42
checks pass with no failures. Every one of the producer certificate's
17 top-level fields is compared completely, including the input hash,
all covariant coefficients, both signed images, both multiples and
all 23 recomputed check flags. The full reconstructed values, thirteen
syzygy coefficients, four tangent residual coefficients and both point
residuals were inspected. The producer certificate is unchanged, with
SHA-256 `de0773e6ed33b5803b0ec975983d7ff69cf757c92d566e83ec943640dc4a6210`.
Full independent evidence is
`scripts/pair-genus-two/elliptic-rank-audit-certificate.json`.

The first independent run reversed the sign in the differential
expression for g6, producing −g6 and the opposite signed images.
The coefficient comparison detected this even though the syzygy,
which squares g6, still passed. Comparison with Cremona (3.6.4)
fixed the audit implementation to the expression above. Its seven
failed checks and complete initial values are preserved in
`scripts/pair-genus-two/elliptic-rank-audit-initial-sign-failure.json`.
This was a checker sign error, not a mathematical defect in L112;
the direct witness and double already passed in that initial run.

The established bound remains rank>=1, against the proposed rank-zero
threshold 0. The audit secures the recorded stop in ATTEMPTS/051;
it adds no new rank bound beyond L112 and no progress beyond the
checked general methods. Marked lifting, rational-point completeness,
degree-nine root recovery, remaining factors, both L095 integer
systems and minus-eleven remain unresolved.

## Mathlib

Full matching exact-instance rank, binary-quartic identification and
supporting torsion-integrality coverage were not checked in Mathlib.
No absence or Lean verification is claimed.
