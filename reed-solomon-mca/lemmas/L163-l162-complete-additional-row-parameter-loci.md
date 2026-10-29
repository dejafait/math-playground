# L163 — Complete additional-row loci on the fixed L162 family

## Hypotheses

Let E be the algebraic closure of F_97. Use the ordered coordinates
S=(1,8,12,18,22,27,33), J=(47,50,64,70,75,79,85,89,96), and precisely
L109's quotient maps on E^7. Original labels are zero-based in the
Cartesian lexicographic order binom(S,2) times binom(J,2), with I
outermost. For j=(I,K), write T_j=I union K, O=S minus I,
z=min O, g_j(Z)=product_(y in J minus K)(Z-y), and

    (Q_j w)_x=g_j(z)w_x-g_j(x)w_z, x in O minus {z}, increasing.

Use L162's four original labels a,b,c,d=(35,522,477,566) and vectors

    x_0=( 2,50, 5,77,16,45,81), x_1=(58,92, 4,81,71,36,26),
    y_0=(75,32, 0,69, 3, 1, 0), y_1=( 0, 0,30, 0, 0, 0, 1).

For [r:s] in P^1(E), put X=r*x_0+s*x_1, Y=r*y_0+s*y_1,
and L_[r:s]=span(X,Y). Audited L162 proves this is an injective
family of planes, with the four designated restricted ranks one
at every parameter. An additional label j is eligible exactly when
j is not a,b,c,d and |T_j intersect T_i|<=1 separately for each
i=a,b,c,d. No symmetry quotient, coding or weight assumption is made.

## Conclusion

There are exactly 112 eligible additional original labels. Define
the following set of forty original labels:

    B={145,147,148,149,160,161,171,174,
       325,327,328,329,340,341,351,354,
       577,581,582,583,595,596,609,610,
       649,653,654,655,667,668,681,682,
       723,724,726,727,748,749,751,752}.

For every eligible j the complete exact rank-one locus is

    { [r:s] : rank(Q_j restricted to L_[r:s])=1 }
       = { [1:94] } if j belongs to B,
       = empty      otherwise.

No eligible additional row has rank zero at any projective parameter.
Both [1:0] and [0:1] give rank two for all 112 rows. There are no
whole-family additional-row loci or unlisted extension-field roots.
This determines restrictions of this fixed family only, without
exhausting the original four-row locus or deciding twelve-row
compatibility, coding realization or the MCA challenge.

This is REPRODUCTION under the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-26-l162-additional-row-parameter-loci-review.md`.
Its separate critical proof audit passed on 2026-10-26, as recorded
below. No originality claim is made.

## Proof

### Imported tools and specialization

For arbitrary-field linear algebra use A. I. Kostrikin and Yu. I. Manin,
*Linear Algebra and Geometry*, Gordon and Breach, 1997 paperback,
ISBN 90-5699-049-7, Chapter 1 Theorem 3.12 pp. 20–21 and sections
6.2–6.9 pp. 44–46, [primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
The matrix [Q_j X, Q_j Y] represents the restriction on the basis
(X,Y), whose independence at every parameter is supplied by L162.
Its rank is at most one exactly when all six two-by-two minors vanish;
its rank is zero exactly when all eight entries vanish.

For polynomial gcd and Bezout identities over a field import
J. S. Milne, *Fields and Galois Theory*, Kea Books 2022,
section 1.8 p. 6 and Proposition 2.17 p. 34,
[author's text](https://www.jmilne.org/math/Books/FT0.pdf), 199-page
version inspected 2026-10-26. The proposition preserves the gcd under
every field extension, using its division and Bezout identities.
These apply to F_97 subset E. The source supplies the general tools,
not these original-label products or loci; the finite coefficient
calculation and complete witnesses below are the necessary specialization.
No general theorem is reproved, and no characteristic-zero or generic
rank assertion is used.

### Complete enumeration and polynomial certificates

Enumerate all 21*36=756 original labels in the stated order. For
each retain its I,K, its four actual support intersections, and the
eligibility Boolean. Exactly 112 satisfy the stated predicates.
All 756 records, including excluded labels, are in
`scripts/seven-coordinate/l162-additional-row-loci.json`, field
`coverage`; `rows` retains exactly the 112 eligible records in
increasing original-label order. No label is replaced or identified.

For each eligible j evaluate all seven defining products g_j(x),
construct Q_j, and retain the eight homogeneous linear entries of
M_j=[Q_j X,Q_j Y] and all six homogeneous quadratic minors in
increasing pairs of its four target rows. Entry coefficients mean
(r,s); minor coefficients mean (r^2,rs,s^2). These complete arrays
are `homogeneous_entries` and `homogeneous_minors` in each record.

On r=1 set t=s and call the six minor polynomials f_0,...,f_5 and
the eight row-major entry polynomials e_0,...,e_7. Each record retains
monic polynomials d_j,h_j, division quotients and Bezout coefficients
certifying, over F_97[t], all the identities

    f_i=d_j*q_i (0<=i<6),  sum_i A_i*f_i=d_j,
    e_i=h_j*v_i (0<=i<8),  sum_i C_i*e_i=h_j.           (1)

The two corresponding fields are `affine_minor_certificate` and
`affine_entry_certificate`; every quotient and witness is retained.
The complete verified outputs are

    d_j=t+3 for exactly the forty labels in B,
    d_j=1   for exactly the other 72 eligible labels,
    h_j=1   for every one of the 112 eligible labels.   (2)

No system of six minors is identically zero, and no all-zero entry
system occurs. The programs also explicitly handle that branch rather
than normalizing a zero polynomial. For this calculation (2) lists
all actual branches, without a square-free or splitting assumption.

For a directly readable nonempty example, label 145 has I={1,27},
K={47,64}, anchor 8, and g-values (11,54,62,69,28,79,40) on S.
Its eight entry coefficient pairs, by rows and then columns, are

    [(80,41),(53,68)], [(29,63),(63,0)],
    [(46,94),(42,0)], [(46,52),(78,54)].

Its six minor triples are

    (11,85,81), (49,14,10), (19,82,36),
    (66,22,0), (43,3,7), (7,66,32).

The quotients by t+3 are respectively
(36+81t),(81+10t),(71+36t),22,(79+7t),(67+32t).
The minor Bezout witness is simply 75*f_3=t+3; the entry witness
is 67*e_5=67*42=1. These are illustrative complete identities for
one label; the other 111 full records are checked, not inferred
from this example or symmetry.

### Completeness over E, endpoints and rank zero

For any tau in E, (1) gives equivalence between simultaneous
vanishing of all f_i(tau) and d_j(tau)=0: divisibility proves one
direction and the Bezout sum the other. This uses identities over
the base field which remain identities in E[t]; it does not test
only base-field roots. Similarly h_j=1 excludes simultaneous entry
vanishing at every affine parameter. Thus all affine rank-at-most-one
points have exact rank one. By (2) their sets are exactly empty or
{tau=-3=94}, as asserted; the linear factors have no other roots
in the algebraic closure, including any repeated or nonrational root.

The omitted endpoint r=0 is checked directly on
[Q_j x_1,Q_j y_1]. For every eligible row at least one of its six
minors is nonzero; the verification certificate retains all six,
the index and the nonzero value of a witness. Hence every endpoint
restriction has rank two, excluding both rank zero and rank one.
The same direct check on [Q_j x_0,Q_j y_0] gives rank two at s=0
for all 112 rows, consistent with d_j(0)=1 or 3 nonzero.
Together the affine chart and its omitted endpoint exhaust P^1(E).
L162's plane independence ensures these matrix ranks are the
restricted-map ranks everywhere, completing the field-valued proof.

### Exact computation and independent checking

Reproduction commands from the active notebook are

    python3 scripts/seven-coordinate/l162_additional_row_loci.py
    python3 scripts/seven-coordinate/verify_l162_additional_row_loci.py

The producer constructs maps by direct product evaluation and obtains
the witnesses in (1) by Euclid/back-substitution. Its complete output
is `scripts/seven-coordinate/l162-additional-row-loci.json`.
The verifier imports neither producer code nor other certificates.
It independently enumerates all labels and all four support predicates,
expands each g_j into polynomial coefficients and evaluates by Horner,
and reconstructs images using
(w_x/g_j(x)-w_z/g_j(z))*g_j(z)*g_j(x). Every denominator is checked
nonzero. It recovers linear entry coefficients at t=0,1 and checks
their infinity coefficients directly. It independently recovers each
quadratic minor from t=0,1,-1 using 2^(-1)=49, and checks its
homogeneous infinity coefficient directly. Degree at most two is
known from the displayed linear representatives, so this is exact
coefficient reconstruction, not inference from parameter samples.

The verifier checks every saved entry and minor coefficient, every
division and Bezout identity in (1), original-label coverage, both
endpoint ranks and all summary classifications. It does not rely on
a second gcd computation. All 4,946 checks pass, with zero failures;
756 coverage records and 112 eligible rows are reconstructed. The
full verification evidence, including endpoint nonzero minors, is
`scripts/seven-coordinate/l162-additional-row-loci-verification.json`.
The two implementations share Python and exact arithmetic in F_97;
this original same-step check is finite-certificate evidence with a
mathematical completeness argument, not proof-assistant verification.

The result addresses only the approved additional-row target. It
does not assert that any chosen larger set of eligible rows is
pairwise linear, meets degree bounds, passes coding gates, or
represents an actual equality event. Other plane families, second-pair
extraction, twelve-row exclusion, arbitrary representation, source
identification and the sharp proximity radius remain unresolved.

### Separate critical audit, 2026-10-26

The first separate critical audit under
`drafts/literature/2026-10-26-l163-critical-audit-review.md` passes
without narrowing the hypotheses or changing the conclusion. Both
complete original scripts were reviewed. The existing verifier was
replayed: all 4,946 checks pass. An additional checker, importing
neither script, is reproduced by

    python3 scripts/seven-coordinate/audit_l163.py

Its complete evidence is `scripts/seven-coordinate/l163-critical-audit.json`.
All 4,397 checks pass with no failures. This checker reads the complete
producer and verifier certificates, binds them by SHA-256 hashes, and
compares every original-label coverage record, not a sample. All 756
labels are independently reconstructed in the specified Cartesian order;
the four fixed supports and each of the four intersection predicates
give exactly 112 eligible labels. Their ordering, uniqueness and complete
retention are checked against both files.

For every eligible row, direct integer products reduced modulo 97
reconstruct all g-values, the anchor, target coordinates and Q matrix.
The images of x_0,x_1,y_0,y_1 are reconstructed directly from the
displayed covectors. Explicit coefficient multiplication reconstructs
all six homogeneous minor triples. Every entry and minor coefficient
agrees with the stored arrays. Expanded integer polynomial identities,
reduced coefficient by coefficient, check every division quotient and
every Bezout sum, including witness lengths and zero-system flags.
The exact minor gcd is t+3 at precisely the forty printed labels and
one at all 72 others; every entry gcd is one. The printed label-145
example, quotients and its two simple Bezout identities also agree.

The audit additionally reconstructs every field in the verifier's
112 row-evidence records. Its g-polynomials are obtained by elementary
symmetric sums, and all zero/infinity minors and their nonzero witnesses
match. Both endpoint ranks are two at all 112 rows. The earlier verifier's
normalized-map divisions are legitimate because every g-value is
nonzero. Its interpolation is exact: entries have degree at most one,
minors at most two, the three nodes 0,1,-1 are distinct, and 2*49=1
in F_97. The new direct-coefficient calculation avoids interpolation.

The all-parameter proof was reviewed independently of these finite
identities. Audited L162 supplies an independent basis (X,Y) at every
projective parameter. On r=1, divisibility and the Bezout identity give
both directions of the common-zero equivalence, and remain valid in
E[t]. Entry gcd one precludes rank zero throughout this chart. Thus
gcd t+3 gives exactly t=94 and gcd one gives no points, including
nonrational extension-field points. The nonzero s^2 minor coefficient
at r=0 proves rank two at the only point outside the chart; nonzero
r^2 coefficients check s=0 as well. These two charts exhaust all
projective parameters. No division by a parameter, separability
assumption, sampling inference or unverified common-root claim enters.

The direct mathematical inputs remain L109's map definitions and
L162's all-parameter family; no coding conclusion of L109 or
classification from L159–L161 is assumed. This is local verification
progress, not new mathematics beyond the cited general tools. The
implementations still share Python and ordinary integer arithmetic;
no formal verification or matching Mathlib theorem is claimed. The
audit establishes neither mutual compatibility of the forty supports
nor coding realization, and leaves the stated challenge gaps unchanged.

## Mathlib

Full matching indexed additional-row locus: not checked. Supporting
finite-field, matrix rank, polynomial gcd/Bezout and projective-line
results: not checked anew. No matching theorem name or Lean proof
is claimed; unknown coverage is not evidence of absence. The
precise standard imports and their extension-field applicability
are stated above. No scheme-theoretic or descent claim is made.
