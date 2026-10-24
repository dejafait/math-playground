# L118 — Exact real fake two-cover point image of the marked octic

## Hypotheses

Use L113's unchanged smooth proper curve C over Q with affine equation

    Y²=G(t)=3025t⁸−31460t⁶+76230t⁴−39204t²+2673.

Use the entire field A=Q[t]/(G) of L115, with theta the image of t,
and L114's actual even-degree fake map, base changed to R:

    mu_R: C(R) -> H_R,
    H_R={delta in A_R*/(A_R*² R*): N(delta) in 3025 R*²},
    A_R=A tensor_Q R.

No supported-class enumeration, class/unit data, finite-image result or
rational-point completeness is assumed. The leading scalar 3025 is
retained; the curve is not replaced by Y²=G/11.

## Conclusion

All eight roots of G are real. Label the embeddings by their root
values theta_1>...>theta_8. A_R is R⁸ with this ordering. A sign string
below has one coordinate for each of these eight embeddings, and is
identified with its simultaneous reversal. The exact point image is

    mu_R(C(R)) = {[++++++++], [--++++++], [----++++], [------++]}.   (1)

These are four distinct classes. H_R has 64 classes, so this point image
excludes 60 of its norm-admissible real sign classes. For example,
[+--+++++] is norm-admissible and is not in (1). This is a statement
about the local ambient, not a count of removed global supported classes.
Both distinct rational infinity points have image [++++++++]. All eight
real branch points are included in (1). C(R) has four connected
components, one for each class in (1).

The proper image can filter later global supported representatives by
their ordered real signs. It does not calculate those representatives,
exclude a rational point or an integer solution, or settle Beal. The
independent critical audit below confirms this instance calculation.

## Proof

### Imported rule and precise applicability

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-real-point-image.md`.
Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8).
The precise inspected version is
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2), 21 October 2008:
Section 5 p.11 gives the exhaustive real sign rule and even-degree
scalar quotient; Section 2 p.3 gives the ordinary, branch and infinity
evaluations. The general rule is imported without reproof. Its
instance specialization requires the ordered roots and endpoint checks
below, which are not supplied by the general theorem.

The hypotheses are satisfied: R has characteristic zero, L113 proves
squarefreeness and gives the smooth proper degree-eight model, and the
leading coefficient is 3025=55²>0. L114 fixes this precise map and norm
fiber. L115 identifies the entire rational algebra; its rational
irreducibility does not imply that its real completion is a field.

### Exhaustive exact root certificate

The following exact evaluations give four disjoint positive-root
intervals. Every displayed endpoint is rational and nonzero under G.

| Interval (a,b) | G(a) | G(b) |
| --- | --- | --- |
| (1/4,1/2) | 33612689/65536 | −727903/256 |
| (3/4,1) | −36435663/65536 | 11264 |
| (3/2,2) | 5006529/256 | −173503 |
| (5/2,3) | −84351487/256 | 2737152 |

G is even. Reflection gives four further disjoint negative intervals,
with endpoint values reversed from the corresponding positive row.
The intermediate value theorem gives a root in each of these eight
disjoint intervals. A degree-eight polynomial has at most eight roots
counted with multiplicity. Consequently each interval contains exactly
one simple root and no other roots, real or nonreal, remain. In descending
order the complete isolating intervals are

    theta_1 in (5/2,3),     theta_2 in (3/2,2),
    theta_3 in (3/4,1),     theta_4 in (1/4,1/2),
    theta_5 in (−1/2,−1/4), theta_6 in (−1,−3/4),
    theta_7 in (−2,−3/2),   theta_8 in (−3,−5/2).

There are no nonreal conjugate pairs. Evaluation at these distinct
roots identifies the entire R-algebra A_R with R⁸ by the Chinese
remainder theorem. These are all eight embeddings of L115's field.

### Ordinary intervals, realizations and scalar collisions

For an ordinary point the imported map is [t−theta]. Let b_k be the
sign vector with exactly its first k entries negative. The positive
leading coefficient and the ordered-root rule allow precisely the
five intervals in this table; in every other open interval G(t)<0,
so there is no real point.

| t-interval | k | Sign vector b_k | Realizing t | G(t) |
| --- | --- | --- | --- | --- |
| (theta_1,+infinity) | 0 | ++++++++ | 3 | 2737152 |
| (theta_3,theta_2) | 2 | --++++++ | 1 | 11264 |
| (theta_5,theta_4) | 4 | ----++++ | 0 | 2673 |
| (theta_7,theta_6) | 6 | ------++ | −1 | 11264 |
| (−infinity,theta_8) | 8 | -------- | −3 | 2737152 |

The isolating intervals prove that each sample lies in its claimed
interval. Every G(t) displayed is strictly positive, so both actual
real points (t,±sqrt(G(t))) exist. No rational Y-coordinate is asserted.
The image is independent of the sign of Y.

The scalar quotient identifies a sign vector only with itself and its
simultaneous reversal. Thus b_0 and b_8 collide. No two of b_0,b_2,b_4,b_6
collide: their negative sets differ, and their first coordinates are
all negative except b_0; the reversal of b_k for 0<k<8 has first
coordinate positive and last coordinate negative, so is none of the
five initial-block vectors. This proves exactly the four classes in
(1) for ordinary points, before checking exceptional points.

### Every branch point

At a=theta_j write G(X)=(X−a) G_tilde(X). Section 2 evaluates the
branch point by the invertible element

    (a−theta)+G_tilde(theta).

At coordinate i!=j this equals a−theta_i, since G_tilde(theta_i)=0.
At coordinate j it equals G_tilde(a)=G'(a), which is nonzero. Because

    G'(theta_j)=3025 product_(i!=j)(theta_j−theta_i),

its sign is (−1)^(j−1). The coordinates before j are negative and
those after j positive. This gives every branch row explicitly:

| j | sign G'(theta_j) | Full invertible sign vector | Block k |
| --- | --- | --- | --- |
| 1 | + | ++++++++ | 0 |
| 2 | − | --++++++ | 2 |
| 3 | + | --++++++ | 2 |
| 4 | − | ----++++ | 4 |
| 5 | + | ----++++ | 4 |
| 6 | − | ------++ | 6 |
| 7 | + | ------++ | 6 |
| 8 | − | -------- | 8 |

Thus every branch image is already included and none is lost by an
invalid zero-coordinate evaluation. The replacement's norm is
G'(a)²/3025>0, also directly confirming norm admissibility.

### Both infinities and every real component

L113's smooth infinity chart is

    Z²=3025−31460q²+76230q⁴−39204q⁶+2673q⁸,
    q=1/t, Z=Y/t⁴.

At q=0 the separate points Z=−55 and Z=55 both have nonzero chart
derivative 2Z, respectively −110 and 110. They are distinct smooth
real points. L114's Section 2 evaluation at each is [3025]=[1],
with all eight signs positive. We retain both points although their
fake images coincide. No affine value of t−theta at infinity is used.

For each of the three bounded allowed intervals, the two Y-sign
branches meet at each simple endpoint, giving one circle. For the
two exterior intervals, near either infinity the even exponent in
Z=Y/t⁴ connects the positive Y branches to each other at Z=55 and
the negative branches to each other at Z=−55. At theta_1 and theta_8
the two signs meet. Hence these exterior arcs together form one
circle. A simple root has Y as a local parameter, so none of these
endpoint gluings introduces an additional real arc. There are four
connected components in total. Their images are the three bounded
classes and the identity exterior class. All real points of the
two smooth charts have now been covered. Coordinate exceptions in
transport to older models do not delete points from C(R).

### Full ambient comparison and limitations

In R⁸ a square class is exactly a vector of eight signs. Its norm
is positive exactly when it has an even number of negative entries,
because the algebra norm is the product of the coordinates and 3025
is positive. Thus there are 2⁷=128 norm-admissible sign vectors.
Multiplication by a negative real scalar reverses all eight signs;
this preserves norm parity and has no fixed sign vector. Division
by scalar signs therefore gives |H_R|=128/2=64.

Equation (1) and the endpoint checks give image size four, strictly
less than 64. The sign vector +--+++++ has exactly two negatives;
neither it nor its reversal is an allowed initial block. It supplies
an explicit excluded class. The 60 excluded ambient classes are a
local necessary restriction. No subgroup property of the point image
is assumed and no vector-space dimension for it is claimed.

Bruin–Stoll Remark 6.1 p.13 warns that determining signs of global
representatives is a separate arithmetic task. Here no such
representatives are computed. L114's known infinity classes survive,
so an empty fake-Selmer argument is still unavailable. Supported
units, ordinary S-class two-torsion, finite images, points on surviving
covers, degree-nine root recovery, remaining factors, both L095
integer systems and minus-eleven remain independent unresolved gaps.
ATTEMPTS/050–052 and unfinished L108 remain unchanged. This is local
instance progress using known methods, without a claim beyond the
general sources checked or a Beal resolution.

### Reproducible exact arithmetic

Run `python3 scripts/pair-genus-two/marked_octic_real_image.py`.
Its complete certificate is
`scripts/pair-genus-two/marked-octic-real-image-certificate.json`.
It uses only exact integer and rational arithmetic. All 17 checks
pass, with no failures: roots 8/8, branch rows 8/8, infinity rows 2/2,
point-image classes 4 versus ambient 64, and 60 ambient exclusions.
The complete root evaluations, all interval realizations, all branch
rows, both infinity rows and all 64 ambient representatives were
inspected. The degree/IVT argument above proves root exhaustion;
the imported theorem and chart arguments prove coverage, rather
than the script's counts alone. The independent critical audit follows.

### Independent critical audit, 2026-10-23

The approved audit passes without a correction. This is independent
verification of a specialization of known methods, not progress beyond
the cited general sources or a global class exclusion. The inputs remain
L113, L114 and L115; no mathematical dependency or assembly changes.
Coverage was approved in
`drafts/literature/2026-10-23-marked-octic-real-image-critical-audit.md`.

Run `python3 scripts/pair-genus-two/audit_marked_octic_real_image.py`.
The full evidence is
`scripts/pair-genus-two/marked-octic-real-image-audit-certificate.json`.
The audit imports no producer code. For t=a/b it evaluates G by the
integer homogeneous expression

    11(275a⁸−2860a⁶b²+6930a⁴b⁴−3564a²b⁶+243b⁸)/b⁸.

All sixteen endpoint evaluations agree with the full original root
rows, and all eight intervals are strictly disjoint in descending
order. Their sign changes exhaust degree eight, proving uniqueness
and simplicity of each root without numerical isolation or a count
assumed from the producer. In particular the entire real algebra is
R⁸; rational irreducibility is not used to infer a real-field structure.

The audit also samples every one of the nine complementary intervals,
including all four forbidden intervals, using bounds separated from
every root. Their signs alternate +,−,+,−,+,−,+,−,+. As there are no
roots in each gap, these are the signs throughout each gap. All five
original positive-value samples agree exactly. Each positive value has
both real square roots, which realizes its computed class; no rational
square root is claimed.

For each branch, the audit computes all seven difference signs from
the disjoint root bounds and multiplies them, retaining the positive
leading factor. This recovers all eight derivative signs and all eight
invertible replacement vectors. The branch formula is applicable over R
even though a root need not be rational over Q. Its off-root coordinates
have product G'(a)/3025, so its complete norm is G'(a)²/3025>0.
Thus no zero coordinate or inadmissible branch class was hidden.

The infinity chart agrees coefficient by coefficient with q⁸G(1/q).
At q=0 its two solutions are separately Z=−55 and Z=55, with nonzero
derivatives −110 and 110. The imported infinity rule gives [3025]=[1]
at each. Analytically q is a real parameter at each point; since t⁴>0,
the positive exterior Y-arcs join at Z=55 and the negative exterior
Y-arcs at Z=−55. At a finite root, G'(a)!=0 makes t a function of Y²
near zero, so exactly the two allowed Y-sign arcs join there.

These local descriptions make the complete arc incidence explicit:
each pair (theta_2,theta_3), (theta_4,theta_5), (theta_6,theta_7) has
two parallel arcs of opposite Y-sign. Each of theta_1 and theta_8 has
one arc to each of the two infinity points. These ten arcs have ten
endpoints, each of degree two. They form three two-arc circles and one
four-arc circle. There are no further points on the two smooth charts,
so the four combinatorial components are exactly the topological
components of C(R). The audit stores every arc and the four resulting
components and checks their distinct, constant image labels.

Finally the independent integer-mask enumeration partitions all 128
even-parity sign vectors into 64 two-element scalar orbits, each pair
being complementary masks m and 255−m. It compares every representative
with the original certificate and recomputes all point-image collisions.
Only the two exterior intervals collide; the three bounded-interval
classes remain distinct. All exceptional images occur in these four
classes. The explicit excluded vector +--+++++ survives the norm test
and belongs to none of them. The audit does not assume subgroup closure.

All 146 checks pass, with no failures: roots 8/8, branches 8/8,
infinities 2/2, components 4/4, image 4<64 ambient classes, and 60
excluded local ambient classes. The full original rows and new gap,
arc, component and scalar-orbit evidence were inspected. The chart and
degree arguments, rather than a preview or count alone, justify
exhaustiveness. Supported representatives and all global point-control
limitations stated above remain unresolved.

## Mathlib

Full matching Mathlib coverage of this exact marked-octic real image
and its exceptional-point calculation was not checked. No absence
claim is made. General real-root, norm or square-class infrastructure
alone would not constitute a matching formal result.
