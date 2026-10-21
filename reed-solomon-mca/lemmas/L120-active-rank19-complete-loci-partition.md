# L120 — Complete active rank-19 loci and necessary-gate partition

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, dimension eight,
L010's shifted moments and the pinned same-support event for
1/4<=delta<5/16. The actual Hankel determinant and all actual locators
are nonzero polynomials. Both coefficient syndromes lie in U_S for
S={1,8,12,18,22,27,33}. Assume sixteen original finite bad parameters
and L104's t=0. Original weights and the prescribed original finite
chart are arbitrary over F. Retain L109/L118's inherited finite-certificate
and representation qualifications. No universal representation or
fixed-pair extraction is assumed.

Fix A1={1,8,47,50}, A2={12,18,64,70}. Select from L118's frozen
`scripts/seven-coordinate/inactive-coordinate-screen.json` exactly the
records satisfying `status == screen_failure`, `rank == 19`, no
`L112_exchanged_rows` in `prior_exclusions`, and historical index
(third_index,fourth_index) different from (0,320). The frozen file's
SHA-256 is
`90b6f145c7993d33a834f3498fb3bee60f08ca328bd8e710af216a70df6172c1`.
Keep its order and repeated kernels/support families at different indices.
The third and fourth supports at a selected record are required to be
actual two-overlap errors when applying its exclusion.

For each selected original 24-by-21 L109 stack, use increasing S-pair
columns, z_j=min(S minus I_j), and lexicographic quotient-covector pairs.
Let B0,B1 be its complete kernel basis with the identity on increasing
free columns, as explicitly saved in the certificate below. Write a
projective kernel point as p=s B0+t B1.

## Conclusion

There are exactly 223 selected indexed occurrences. Their full homogeneous
decomposable loci over every extension of F_97 and their intrinsic L109
gate dispositions are:

| Occurrences | Complete parameter locus | Points passing all four rows |
| ---: | --- | ---: |
| 219 | st=0, hence [1:0] and [0:1] | 0 |
| (38,496), (191,143) | t(t−3s)=0 | [1:3] only |
| (51,467), (178,172) | t(t+16s)=0 | [1:81] only |

All 1,784 selected-row projections at these 446 points have rank one.
Each of the 442 failed points has lambda zero at at least one row;
all canceled overlap weights and all successful rows are retained.
Consequently the 219 occurrences in the first row cannot be contained
in an equality pencil in any prescribed original chart. These are
indexed exclusions relative to the specified prior records; no assertion
of novelty under all possible relabelings is made.

The four surviving occurrences are two support families with rows three
and four exchanged. Each has exactly one intrinsically eligible plane.
For each row its prescribed finite-direction condition remains necessary;
passing these four-row tests supplies no nonpersistence construction,
t=0 realization or sixteen-event completion. Rank-20 records are outside
this result. Historical 599/239 partitions remain unchanged. No third,
fixed pair or arbitrary seven-coordinate class is excluded, and the
global interval remains 11/q–16/q. Same-step independent replay passes;
the separate step-337 critical proof/program audit below found no defect.

## Proof

### Imported results and specialization

L109's necessary direction supplies a nonzero decomposable wedge from
the actual independent lift coefficients, its homogeneous Plucker
criterion, and every projection, lambda, full-weight and prescribed-chart
gate. In particular it rejects rank-zero projection using the actual
nonpersistence hypotheses. L118 supplies the audited historical domain
and labels; its activity exclusion is not rerun or extrapolated.
These are the only direct mathematical inputs. L112/L119 are exclusions
removed from the selector, rather than sources of equations for the
remaining matrices. L086 extraction and L109's r>=6 converse are not used.

The coding inputs are imported through L109: J. I. Hall, *Notes on Coding
Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004, [accepted manuscript 2016-02-29,
section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the shortening formula after Lemma 5.3.
Distinct evaluation labels and nonzero multipliers are unchanged;
shortening seven labels J minus K_j leaves positive dimension one.
No standard coding theorem is reproved.

For polynomial certificates import J. S. Milne, *Fields and Galois
Theory*, Kea Books 2022, [sections 1.6–1.9, printed pp. 5–7,
and Proposition 2.17, p. 34](https://www.jmilne.org/math/Books/FT0.pdf).
Polynomial division and Bezout identities certify the gcd; Proposition
2.17 preserves it under arbitrary field extension. The source assessment
also covers Lemma 2.19/Proposition 2.20, pp. 35–36, and Corollary
4.22/Proposition 4.23, pp. 66–67, for repeated/nonsplit cases. The actual
complete factorizations here have distinct F_97 roots, so no quadratic
extension or inseparability argument is required. Exterior-coordinate
interpretation is imported through L109 and the assessed Keith Conrad,
*Exterior Powers*, [Theorems 4.2, 7.1, 7.5, pp. 11–12,
23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-19-active-rank19-complete-loci-review.md`.
This is REPRODUCTION: the local record-specific census applies assessed
tools, with no claim of new general mathematics beyond the checked sources.
ATTEMPTS/041–042 remain valid obstructions to rank-only and label-1-only
extrapolation; the present test uses the entire homogeneous locus.

### Complete domain, matrices and kernels

The producer and replay are, respectively,

    python3 scripts/seven-coordinate/active_rank19_complete_loci.py
    python3 scripts/seven-coordinate/verify_active_rank19_complete_loci.py

Their full evidence is in
`scripts/seven-coordinate/active-rank19-complete-loci.json` and
`scripts/seven-coordinate/active-rank19-complete-loci-replay.json`.
The producer checks L118's separate successful audit, its before/after
hash equality, all 587 frozen artifact hashes and the audited helper hashes.
It applies the exact predicate to all 599 source records, preserving order.
`selected_manifest`, `processed_manifest` and every source array position
bind the 223 retained indices without conflating positions with indices.
The verifier independently applies the same predicate and compares the
complete ordered manifest, checking uniqueness of the historical pairs.
It also reconstructs the ordered support universe and third list from
their label definitions and checks each selected support family.

For every family the producer forms g_K(x) by direct products and
reconstructs the original covectors and exterior rows. It compares these
with the independently implemented derivative/ratio construction used in
the earlier audits. Full reverse-row Gauss–Jordan elimination freshly
recovers both kernel vectors and their free columns. All 48 original
null residuals per occurrence vanish; the basis has the identity on its
two free columns. A saved 19-by-19 original minor has nonzero residue.
Thus rank is at least nineteen by the minor, and at most nineteen by
two independent null vectors in a 21-dimensional space. The basis is
complete. These identities and the same nonzero minor persist under
every field extension.

The verifier imports neither producer nor producer helpers. It multiplies
the polynomial factors of g_K and evaluates by Horner's rule, obtaining
each quotient covector independently. It compares all 112,392 original
matrix entries, checks column rank, evaluates every saved minor by column
pivoting, and verifies the two null vectors and their identity submatrix.
All tests pass. No rank or basis is inferred from prime-field point sampling.

### All homogeneous components and infinity

For each increasing quadruple a<b<c<d in S, retain all three coefficients
of p_ab p_cd−p_ac p_bd+p_ad p_bc after p=s B0+t B1.
There are 35 equations per occurrence, 7,805 in total. Dehomogenize at
s=1 to polynomials q_l(T) of degree at most two. For each occurrence the
certificate saves a monic G, all quotient polynomials Q_l, and all
Bezout coefficients U_l satisfying, coefficientwise in F_97[T],

    q_l=G Q_l for every l,       sum_l U_l q_l=G.

The verifier checks every one of these identities by independent
coefficient multiplication. Consequently the common affine zero set
is precisely G=0 over every extension, by the imported gcd theorem or
directly by these two identities. The original homogeneous coefficients
at [s:t]=[0:1] are checked separately; infinity is never lost through
dehomogenization.

The complete G histogram is: 219 copies of T, two of T(T−3), and two
of T(T+16). Their distinct linear factors multiply back to G, leaving
constant factor one. Infinity occurs exactly in the first 219 cases.
The certificate also retains every original quadratic coefficient, not
just this histogram. These identities give precisely the three loci in
the conclusion, with two points each. In particular no identically-zero
system, empty locus, repeated point, nonsplit factor or unrecorded
extension-field point remains. The review allowed such branches; their
absence is the result of this computation rather than an assumption.

### All row gates and the four intrinsic survivors

At each of the 446 points choose its first nonzero Plucker entry p_ab
and reconstruct L109's independent basis

    u_x=p_xb/p_ab,       v_x=p_ax.

The full wedge reconstructs p. For each selected row compute Q_j u,Q_j v
and every projection minor. All minors vanish, and a nonzero component
pair is saved for each of the 1,784 projections, proving rank exactly one.
At the first such component n take

    (alpha,beta)=(-(Q_j v)_n,(Q_j u)_n),
    h=alpha u+beta v,      lambda=h_z/g_K(z).

The nonzero h generates the unique intersection line. Restore errors
by e_i=h_i−lambda g_K(i) for i in I, e_k=−lambda g_K(k) for k in K.
The certificates keep every zero weight and every successful gate.
For all points and all rows, the complete pointwise identities
h−e=lambda g_K on all sixteen labels and the original eight shifted
moment residuals are checked. These are 28,544 pointwise entries and
14,272 moment entries. All vanish.

Exactly 442 points have a lambda-zero row, including both points at
each of the first 219 occurrences; all are rejected by L109. There are
1,322 lambda-zero rows in total. No point is rejected just because it
is not prime-field sampled or because its kernel resembles an old one.
The other four points pass every intrinsic gate. Here are complete
representatives for the two support families, with S in increasing order:

    U=(1,0,30,88,43,87,31), V=(0,5,1,83,30,15,89),
    U'=(1,0,4,20,23,33,82), V'=(0,12,1,55,41,59,55).

| Representative index | Row | I; K | (alpha,beta) | lambda | Weights on ordered I then K |
| --- | ---: | --- | --- | ---: | --- |
| (38,496), U,V | 1 | 1,8; 47,50 | (18,84) | 23 | 53,25,91,62 |
| (38,496), U,V | 2 | 12,18; 64,70 | (28,38) | 92 | 75,93,67,59 |
| (38,496), U,V | 3 | 1,22; 89,96 | (90,29) | 53 | 26,23,26,61 |
| (38,496), U,V | 4 | 12,27; 75,89 | (6,55) | 92 | 89,91,67,36 |
| (51,467), U',V' | 1 | 1,8; 47,50 | (86,71) | 91 | 60,23,10,26 |
| (51,467), U',V' | 2 | 12,18; 64,70 | (9,38) | 85 | 48,68,25,64 |
| (51,467), U',V' | 3 | 1,27; 75,89 | (15,71) | 48 | 92,77,94,23 |
| (51,467), U',V' | 4 | 12,22; 89,96 | (88,54) | 85 | 85,68,60,96 |

The (191,143) and (178,172) occurrences are respectively these same
two cases with rows three and four exchanged. No occurrence is removed
for being a duplicate. Every table entry is retained and verified in the
full point certificate; `survivor_details` records its exact position.

The independent replay checks the reconstruction in every nonzero
Plucker chart: 1,641 such pivots across all points. For each chart and
row it covers every nonzero component pair of (Q u,Q v): 21,414 choices.
Each resulting intersection vector is certified to be a nonzero scalar
multiple of the canonical h, with lambda and every error weight scaled
by the same scalar. Thus none of these chart or projection-pivot choices
changes a zero gate. Full coefficient identities, rather than sampling
additional extension-field points, justify this coverage.

For the prescribed original basis write u_original=A u+B v,
v_original=C u+D v with Delta=AD−BC nonzero over F. Direct inversion
gives alpha_original=(D alpha−C beta)/Delta. The row is original-finite
exactly when D alpha−C beta is nonzero, as recorded for every rank-one
row. If it is finite, divide h, lambda and all weights by
alpha_original. A zero gate remains zero; if the expression vanishes,
the unique intersection is omitted and is not an original finite event.
This applies equally to nonrational prescribed omitted directions.
The table's nonzero weights certify intrinsic successes only, subject
to these four explicit linear finite-direction gates for each plane.
No convenient replacement of the prescribed chart is made.

### Scope and verification limits

The producer and independent replay report zero failures and zero
unresolved branches, with 223/223 occurrences and 446/446 points covered.
All 587 historical artifact hashes remain unchanged. Both paths still
share Python, residue arithmetic and the stated mathematical formulas.
Same-step replay is not a separate critical audit or proof-assistant
verification. This establishes a restricted finite-certificate input.
It neither settles any rank-20 occurrence nor tests another support
row, extracts a third or fixed pair, or improves the global bound.
The four intrinsic survivors are preserved as necessary-filter survivors;
no inference of actual nonpersistent pencils is made from four rows.

### Separate critical audit, 2026-10-19

Step `2026-10-19-mca-337-active-rank19-critical-audit` used the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-19-active-rank19-classification-audit-review.md`.
It inspected the full proof and both complete programs, all called
polynomial, projection, matrix and nullspace helpers, L109's necessary
direction and converse boundary, and L118's exact domain and separate
step-329 audit. The assessed primary citations above are reused under
unchanged hypotheses. No mathematical defect, changed dependency or
repair was found. This is REPRODUCTION validating the existing restricted
input, not a further exclusion or progress beyond the checked literature.

Reproduce this separate audit with

    python3 scripts/seven-coordinate/audit_active_rank19_complete_loci.py

The full audit certificate and complete independent-replay log are
`scripts/seven-coordinate/active-rank19-critical-audit.json` and
`scripts/seven-coordinate/active-rank19-critical-audit.log`.
The audit binds the exact frozen source hash and current program hashes,
checks all 587 prior artifact hashes and audited helper hashes, reapplies
the exact selector, and checks every record position and ordered index.
Both the 599 historical records and 239 screen failures remain unchanged.

For all 223 original matrices, direct-product and derivative/ratio
constructions agree. The derivative formula follows by differentiating
X^16−1 at each distinct nonzero label; its denominator is a product of
nonzero label differences. Reverse-row Gauss–Jordan elimination recovers
the complete saved two-vector bases and free columns. Original minor
indices are distinct and in range, and row elimination verifies every
nonzero rank-19 determinant. All certificate array lengths are checked,
so zip iteration in the independent replay cannot omit a gate or moment.

The independently implemented verifier was then executed on every record.
It reconstructs the ordered support domain and all 112,392 original
matrix entries by polynomial multiplication and Horner evaluation,
checks ranks and minors by column elimination, and verifies all null
residuals. Every one of the 7,805 homogeneous restrictions and 8,028
divisibility/Bezout identities is checked coefficientwise. Full linear
factorization and the separate homogeneous infinity test cover all 446
points, with no unresolved branch. This is complete evidence over every
extension: a nonzero minor and a complete null basis persist under scalar
extension; divisibility and Bezout identities give both directions of
the common-zero equivalence; complete factorization leaves no unread
extension roots. Prime-field point sampling is not used for completeness.

All 1,784 row projections have rank one. Every failed and successful
weight row, every sixteen-coordinate identity and every original shifted
moment passes the replay. There are 442 failed points, each with a
lambda-zero row, and four intrinsic successes. The replay verifies all
1,641 nonzero Plucker pivots and 21,414 nonzero projection-pivot choices,
including the nonzero scaling of each reconstructed intersection vector,
lambda and error vector. The separate audit matches the entire
`survivor_details` export to the point evidence, checks all eight numeric
rows printed above, and verifies both exchanged-row identifications
without merging their historical indices.

The prescribed-chart argument was checked algebraically: inverting
the original basis matrix gives alpha_original=(D alpha−C beta)/Delta,
with Delta nonzero. If its numerator vanishes, the unique row direction
is omitted; otherwise division rescales every weight by a nonzero element.
Thus zero gates cannot be repaired over F, including by nonrational
prescribed coefficients. The survivor rows remain subject to their
explicit finite-direction gates. No original chart is selected for the
user, and L109's r>=6 converse is not applied to these four rows.

Every audit check passes and independent replay exits successfully.
All 589 tracked artifacts (the prior 587 and both L120 certificates)
are byte-identical before and after the audit; all inspected code is
unchanged. Shared Python and residue arithmetic remain qualifications,
as do the inherited L010/L103/L104 finite-certificate assumptions.
No new support row, rank-20 record, third/pair exclusion or equality
completion was tested or inferred. This section supersedes pending-audit
wording in the overview; PROOF.md and the DAG stay unchanged because
the mathematical argument and dependencies have not changed.

## Mathlib

Full matching coverage for this exact indexed finite classification is
**not checked**. Supporting gcd, matrix-rank, exterior, Plucker and
finite-field results are **not newly checked**. Unknown coverage is not
absence. The precise standard inputs above are imported; the explicit
computational qualification remains after the separate audit. No
proof-assistant verification is claimed.
