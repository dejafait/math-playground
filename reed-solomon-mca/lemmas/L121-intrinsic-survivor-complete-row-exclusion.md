# L121 — Complete row test excludes the two intrinsic survivor planes

## Hypotheses

Use L109's necessary equality setting: F=F_(97^20), the sixteen labels
H={x in F_97^*:x^16=1}, dimension eight, shifted moments of orders one
through eight, the pinned same-support event on 1/4<=delta<5/16,
sixteen actual original finite bad parameters, nonzero actual Hankel
determinant and coordinate-locator polynomials, and L104's t=0.
Both coefficient syndromes have their lift on
S={1,8,12,18,22,27,33}. Retain the inherited L010/L103/L104 finite
certificate qualifications. Original weights and the prescribed original
finite chart are arbitrary over F. No universal seven-coordinate
representation or fixed-pair extraction is assumed.

In increasing S order consider exactly the two L120 planes

    U=(1,0,30,88,43,87,31), V=(0,5,1,83,30,15,89),
    U'=(1,0,4,20,23,33,82), V'=(0,12,1,55,41,59,55).

The first occurs at historical indices (38,496) and (191,143), the
second at (51,467) and (178,172), with the last two selected support rows
exchanged in each pair. L120's separate step-337 audit fixes these
identifications. Each indexed application still requires its four
selected supports to be actual equality errors.

## Conclusion

For each plane the complete 756-row universe
I in binom(S,2), K in binom(H minus S,2) has exactly four rank-one
projections, all passing the intrinsic lambda and full-weight gates,
and 752 rank-two projections. There is no rank-zero projection and no
rank-one failed-weight row. The four successful directions are distinct.
They are precisely the original four selected rows, with no extra row.

| Plane | I; K | Normalized direction (alpha,beta) |
| --- | --- | --- |
| U,V | 1,8; 47,50 | (1,37) |
| U,V | 12,18; 64,70 | (1,36) |
| U,V | 1,22; 89,96 | (1,79) |
| U,V | 12,27; 75,89 | (1,90) |
| U',V' | 1,8; 47,50 | (1,20) |
| U',V' | 12,18; 64,70 | (1,15) |
| U',V' | 1,27; 75,89 | (1,50) |
| U',V' | 12,22; 89,96 | (1,91) |

The number of original finite full two-overlap recoveries is therefore
at most four in every prescribed chart, eight below L109's necessary
minimum twelve. Neither plane can be an equality lift. All four indexed
occurrences are excluded after combining this shortfall with L120's
exclusion of their other decomposable point. Thus all 223 occurrences
selected in L120 are excluded, with its 219 prior exclusions retained.
Historical 599/239 partitions remain unchanged; this is an additional
result, not a rewritten historical filter. Rank-20 records, other thirds,
arbitrary t=0 profiles and universal extraction remain outside the result.
No third or fixed pair is excluded, and the global interval remains
11/q–16/q. Same-step independent full replay passes; the separate
step-341 critical proof/program audit below found no defect.

## Proof

### Assessed inputs and precise specialization

Use L109's necessary row criterion and r=12+n_0 in 12–14. Use L120's
audited bases, complete two-point loci and exact four historical indices.
Its other 442 points already fail necessary selected-row lambda gates;
the present calculation tests only its two distinct surviving planes.
Neither an equality converse nor a new locus computation is used.

The invocation-start assessment is
`drafts/literature/2026-10-19-intrinsic-survivor-completion-review.md`,
DECISION SPECIALIZE. This is a REPRODUCTION finite specialization of
assessed tools; no progress beyond the checked literature is claimed.
The standard coding inputs are imported through L109: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004, [accepted manuscript 2016-02-29,
section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the shortening formula following Lemma 5.3.
The sixteen distinct labels, nonzero multipliers and dimension eight
are unchanged. Every row shortens exactly the seven labels
(H minus S) minus K, leaving dimension one through positive dimensions
and only nonzero label-difference multipliers. The exterior interpretation
is already covered by L109 and Keith Conrad, *Exterior Powers*,
[Theorems 4.2, 7.1, 7.5, pp. 11–12, 23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
No standard coding, shortening or exterior theorem is reproved.

### Complete quotient certificate

Reproduce the full calculation and independent replay with

    python3 scripts/seven-coordinate/intrinsic_survivor_full_rows.py
    python3 scripts/seven-coordinate/verify_intrinsic_survivor_full_rows.py

The complete certificates are
`scripts/seven-coordinate/intrinsic-survivor-full-rows.json` and
`scripts/seven-coordinate/intrinsic-survivor-full-rows-replay.json`.
The producer binds the source certificate and replay to L120's successful
separate audit, checks the audited code hashes and both exchanged-row
identifications, and retains all four original indices. Those three
bound input artifacts are hashed before and after and remain unchanged.
The verifier independently checks the same source hashes and bases.

Set J=H minus S. Enumerate the 21 increasing pairs I in S and 36
increasing pairs K in J, with I outermost. No incidence or seed filter
is applied. For every row use L109's g_K(X)=product_(y in J minus K)(X−y),
z=min(S minus I) and its four covectors
c_x(w)=g_K(z)w_x−g_K(x)w_z for x in S minus (I union {z}).
All g_K values on S union K are nonzero. For either displayed basis
u,v the producer saves Q, Qu, Qv and all six projection minors for every
row. A nonzero minor certifies projected rank two; all zero minors with
a nonzero entry certify rank one. A zero projection is retained as its
own branch: by L109 it would contradict actual nonpersistence for the
whole plane, rather than merely fail one optional recovery. None occurs.

At rank one choose the first nonzero component pair n and set
(alpha,beta)=(-(Qv)_n,(Qu)_n). Then h=alpha u+beta v is nonzero and
Qh=0. Set lambda=h_z/g_K(z),
e_i=h_i−lambda g_K(i) for i in I, and e_k=−lambda g_K(k) for k in K.
Every row retains lambda zero and each canceled overlap weight as an
explicit possible failure. For all eight rank-one rows in the actual
two-plane census, lambda and all four weights are nonzero. The raw
directions, lambdas and weights agree exactly with L120's eight printed
selected-row entries; normalizing the direction gives the table above.
For each row all sixteen identities h−e=lambda g_K on H and all eight
original shifted moment residuals are saved and are zero. The error is
extended by zero off I union K and h by zero off S.

For each plane the other 752 rows have a saved nonzero projection minor.
They have no nonzero h in the intersection and hence cannot supply a
two-overlap event, over F_97 or any extension. The four rank-one rows
are listed completely. The producer groups successes by normalized
projective (alpha,beta), retaining duplicate groups explicitly; both
duplicate lists are empty and each count is four. This is a complete
row/direction count, rather than a count of only successful samples.

### Independent all-moment replay and extension completeness

The verifier imports neither producer nor producer helpers. It constructs
H as the powers of eight, checks the complete ordered universe of 756
distinct rows, and reconstructs g_K by coefficient multiplication and
Horner evaluation, independently of the producer's direct products.
It compares every saved quotient entry, projected vector and minor.

Independently, for each support A=I union K it forms the original
eight-by-six homogeneous moment system in
(alpha,beta,e_(i1),e_(i2),e_(k1),e_(k2)). Its row of order d=1,...,8 is

    (sum_(x in S) u_x x^d, sum_(x in S) v_x x^d,
     -i1^d, -i2^d, -k1^d, -k2^d).

It uses reverse-column-pivot Gauss–Jordan elimination and saves every
original matrix, full reduced matrix, pivot list and complete null basis.
The four error columns have rank four in every case, also directly
checked. Every saved null vector satisfies all eight original equations,
and its free coordinates are the standard unit vectors, certifying
completeness of the basis. The rank histogram for each plane is precisely
752 matrices of rank six and four matrices of rank five. Thus all 752
rejected rows have zero kernel, and the other four have a unique kernel
line with nonzero direction coordinates. Each such line agrees, including
all four weights up to the same nonzero scalar, with the quotient recovery.
The independent verifier also checks the sixteen pointwise identities,
eight moments, each lambda/weight/finite-chart gate, and every nonzero
projection-pivot choice at every rank-one row. The direction groups and
all disposition counts agree exactly; no unresolved branch remains.

These are exact base-field matrices. Row operations use only nonzero
F_97 pivots, hence are still invertible over every extension. A full-rank
system acquires no kernel on extension, and a rank-five system's complete
one-dimensional kernel only extends scalars. Therefore neither nonprime
directions nor extension-field error weights add rows or directions.
The verifier's unexpected-rank-zero branch explicitly marks the replay
unresolved; the successful full census has no such branch.

The initial verifier run reached the first plane's summary comparison
and failed only because JSON converts numeric histogram keys to strings.
The failed full record is preserved as
`scripts/seven-coordinate/intrinsic-survivor-full-rows-replay-first-encoding-failure.json`.
The comparison now uses string keys, and the complete replay of both
planes passes with zero failures or unresolved branches. No mathematical
row disposition was changed to repair this serialization mismatch.

### Prescribed charts and the necessary shortfall

For an arbitrary prescribed basis write
u_original=A u+B v, v_original=C u+D v, Delta=AD−BC nonzero over F.
L120's audited inversion formula gives
alpha_original=(D alpha−C beta)/Delta. A recovery is original-finite
exactly when D alpha−C beta is nonzero. When finite, h, lambda and all
error weights are divided by alpha_original. These operations preserve
full weights and distinct projective directions. If the numerator is
zero, the direction is omitted. The argument permits nonrational
A,B,C,D and retains all eight explicit gates from the table; it never
replaces the prescribed chart by a convenient one.

Consequently any prescribed chart retains at most the four counted
directions on each plane. L109 requires 12+n_0>=12 actual distinct finite
two-overlap recoveries at t=0 equality. Four is insufficient even before
chart deletion. This excludes both planes, not merely a failed optional
row. L120 already excludes the other point of each of the four indexed
loci and every point of its 219 other indexed loci, proving the asserted
restricted combination. There is no remaining-event construction or
claim that four selected recoveries imply nonpersistence. No occurrence
outside the two-plane test was newly enumerated.

This is a finite-certificate input with full same-step replay. Both
implementations still share Python, residue arithmetic and the mathematical
moment convention. The separate critical audit below retains these
qualifications; the notebook remains IN_PROGRESS, with no complete
challenge candidate.

### Separate critical audit, 2026-10-19

Step `2026-10-19-mca-341-intrinsic-survivor-critical-audit` used the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-19-intrinsic-survivor-exclusion-audit-review.md`.
The full proof, both complete programs and every called helper were
inspected. Both programs are self-contained apart from Python's standard
library. L109's necessary gates and converse boundary, L104's equality
balance, and L120's separately audited complete loci, survivor export
and prescribed-chart reasoning were checked in their exact scopes.
The standard sources cited above are reused under unchanged hypotheses;
no new literature discovery or standard-theorem reproof is claimed.

Reproduce this separate audit with

    python3 scripts/seven-coordinate/audit_intrinsic_survivor_full_rows.py

The complete audit and reproduction log are
`scripts/seven-coordinate/intrinsic-survivor-critical-audit.json` and
`scripts/seven-coordinate/intrinsic-survivor-critical-audit.log`.
The audit reruns both complete programs and checks the entire outputs.
All six tracked artifacts, including both L121 certificates, the preserved
failed replay, and all three bound L120 artifacts, remain byte-identical.
Both inspected L121 programs are also unchanged. The producer rechecks
L120's audited program hashes and both exchanged-row identifications;
the new audit separately matches every successful support with the four
selected rows at each of the four historical indices.

For every one of the 1,512 rows, the independent replay reconstructs
the quotient data and the original eight-by-six moment matrix, its
complete reverse-pivot kernel, all weights, sixteen-coordinate identities,
eight shifted moments and all nonzero projection pivots. The separate
audit additionally reconstructs each original matrix and uses forward
column elimination with a saved eight-by-eight left multiplier. It
checks the full identity E M=R, the identity pivot submatrix, the zero
remaining rows and every nonzero pivot value. The multiplier is a product
of row swaps, nonzero scalings and row additions, hence invertible over
every extension. The saved reverse-pivot null vectors satisfy all eight
equations and have an identity on all free coordinates; their number is
six minus the independently verified rank. Thus they are a complete
basis, without relying on a histogram or a prime-field point sample.

The ranks are exactly six at 752 rows and five at four rows per plane.
Every rank-five row has nonzero lambda and all four error weights;
there are no rank-zero projections, canceled weights or unresolved
branches. The four normalized directions are exactly the displayed table
and are distinct on each plane. Extension scalars cannot create a kernel
at a rank-six row or a second projective solution at a rank-five row.

The preserved first replay was inspected in full. Replacing just
`Counter(str(r['projection_rank']) for r in rec['rows'])` by its version
without `str` in the current verifier reproduces the old verifier's
SHA-256 exactly. All 756 saved first-plane row records, source hashes
and producer-certificate hash match the corrected complete replay.
The old record has exactly one assertion failure, no unresolved branch,
and no first-plane summary or second-plane records. In the reconstructed
old program the assertion is the summary comparison: integer histogram
keys differ from the deserialized string keys. The correction changes
only that comparison; the subsequent full two-plane replay passes.

The threshold was checked from L104's balances at t=0:
n_0+n_1+n_2=16 and n_1+2n_2=28, so n_2=12+n_0>=12.
Equality supplies full, distinct actual errors before this count. L109
supplies independent lift coefficients and the necessary row tests;
its converse for at least six rows is never applied to these four.
For an arbitrary prescribed basis, direct inversion gives
alpha_original=(D alpha−C beta)/(AD−BC). An omitted direction is removed;
any finite direction and all its weights are rescaled by a nonzero
element. This holds for nonrational basis coefficients as well. Therefore
four is an upper bound before chart deletion and is eight below the
necessary twelve in every original chart.

L120 excludes 442 of its 446 indexed points; these two planes are its
remaining four indexed points, with the exchanged rows retained. The
combination therefore excludes precisely its selected 223 occurrences.
No mathematical defect, changed dependency or repair was found. This
REPRODUCTION audit validates an existing restricted input; it adds no
new exclusion beyond L121, general theorem, or global error bound.
Historical 599/239 partitions and rank-20 records stay unchanged.
Shared Python/residue arithmetic and inherited finite-certificate
qualifications remain. This canonical audit supersedes pending-audit
wording in the overview; PROOF.md and DAG.md are unchanged because the
argument and dependencies have not changed.

## Mathlib

Full matching coverage of this finite two-plane census is not checked.
The previously assessed coding and exterior inputs are imported through
L109; no claim of absence from Mathlib or formal verification is made.
