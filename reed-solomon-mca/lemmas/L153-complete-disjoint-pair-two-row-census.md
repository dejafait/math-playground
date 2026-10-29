# L153 — Complete disjoint-pair two-row rank and kernel census

## Hypotheses

Work over F_97 or an extension E of F_97. Fix

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

Let U=binom(S,2) times binom(J,2), with I outermost and both pairs
in increasing lexicographic order. Its zero-based indices are 0–755.
An index (I,K) means the support I union K. For each support use
L109's six-by-21 block N_(I,K), with pivot z=min(S minus I), increasing
covector pairs and increasing S-coordinate-pair columns. Consider every
unordered pair of disjoint supports, indexed a<b, without symmetry
reduction. The matrix for the pair is N_a stacked above N_b.

This finite matrix conclusion needs no equality-pencil hypothesis.
Its coding use retains L109's represented class: F=F_(97^20), k=8,
the pinned 1/4<=delta<5/16 cell, coefficient syndromes in U_S, actual
nonzero D and locators, t=0, sixteen original finite events, arbitrary
weights and original chart, and inherited L056/L069/L040 computational
qualifications. C152a's relevance is its extraction of some such actual
pair; it identifies no numeric pair and is not used to compute a rank.

## Conclusion

There are exactly **79,380** pairs. Every original twelve-by-21 stack
has rank **12** and a complete nine-dimensional kernel over F_97 and
over every extension E. The complete pair registry, original maximal
minors and canonical kernel bases are saved in the certificates below.
All **714,420** kernel basis vectors and **8,573,040** original residual
entries were checked; every residual is zero. Independent ratio-matrix
verification checked another 8,573,040 residual entries and the same
complete kernels. There were no failed comparisons.

In particular rank supplies **no stratification of these pairs**.
It excludes none: L109's necessary exclusion threshold is rank 21,
whereas a twelve-row matrix has rank at most twelve. This closes the
bounded rank-stratification mechanism, not the uniform compatibility
problem. Equal ranks do not imply equal kernels, equal gated loci or
transport of any label-specific exclusion.

## Proof

### Imported input and finite specialization

Use exactly L109's formula (1). Its entries depend only on the labels
and belong to F_97. Its necessary coding interpretation and its complete
Plucker, rank-one projection, full-weight and original-chart gates are
retained, not reproved or inferred from this census.

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-all-pair-census-calculation-review.md`.
The inspected coding inputs are J. I. Hall, *Notes on Coding Theory*,
[Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following single-coordinate GRS
shortening formula. The assessment reuses prior inspected shortening
coverage despite its latest access error. L109 already verifies sixteen
distinct labels, nonzero multipliers, dimension eight and seven successive
shortening deletions leaving dimension one with nonzero retained
multipliers. This census changes none of these hypotheses.

For ordered exterior bases the assessment imports Keith Conrad,
*Exterior Powers*, undated 47-page author PDF inspected 2026-10-18,
[Theorems 4.2, 7.1 and 7.5, pp. 11–12, 23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
These apply over F_97 and its extensions. The actual block formula and
minors argument are already in L109. No general coding or exterior-power
theorem is reproved. The new local evidence is the complete finite
registry and its exact bases; the cited sources do not supply those
label-specific certificates. This is REPRODUCTION, with no mathematical
originality or advance beyond the checked sources claimed.

### Complete indexing

There are binom(7,2)binom(9,2)=756 individual supports. For each one,
a disjoint partner chooses two of the remaining five S labels and two
of the remaining seven J labels. Thus the number of unordered pairs is

    756 * binom(5,2) * binom(7,2) / 2 = 79,380.

The producer enumerates all a<b in the full universe and tests literal
support disjointness. It groups the retained pairs by their two overlap
pairs, only for file storage: there are 105 batches, each with 756 pairs.
This grouping deletes no pair and identifies no labels or matrices.

The independent verifier constructs the universe by first enumerating
four-subsets of H, retaining exactly those with two S labels, and then
splitting them into (I,K). For each support it independently constructs
ordered disjoint partners from the two complement sets. There are exactly
158,760 distinct ordered pairs. Sorting each pair and deduplicating gives
exactly the complete saved unordered index set, with each saved index
occurring once and a<b. As a separate cardinality check, choose four
labels in each part, one of three unordered partitions of the S four-set,
and one of six assignments of two J labels to the lexicographically first
S pair. This gives binom(7,4)binom(9,4)*3*6=79,380. The exact set comparison,
not the count alone, certifies coverage.

### Original entries, minors and complete kernels

The producer explicitly reuses the audited original block constructor
`block` in `zero_anchor_support_filter.py` and incremental elimination
`eliminate` in `new_pair_filter.py`. These are software reuse from L109
and L125, not a transfer of either old labeled census. Every one of the
756 original blocks is saved, including pivot and four covectors.

For each original twelve-by-21 stack the certificate records the rank,
independent original row indices, increasing pivot columns, the nonzero
original minor residue, all kernel basis vectors, and all original
residuals. Incremental row elimination gives an echelon system. For each
free coordinate its back-substitution vector is one there, zero in all
other free coordinates, and solves every pivot equation. Consequently
the basis has an identity matrix on the free coordinates. Its minor
residue is the product of insertion pivots, corrected by the sign needed
to sort insertion columns; row additions preserve that selected original
minor. This computation reports rank twelve in every case.

The verifier imports neither producer module. It generates H as the
sixteen powers of 8, checks its order (8^8=-1), expands each seven-root
polynomial g_K and evaluates it on H by Horner's rule. Its exact zero
set on H is checked to be J minus K. In particular g_K is nonzero on
S union K. For x in (S minus I) minus {z} it forms

    d_x = E_x^*/g_K(x) - E_z^*/g_K(z).

The original covector is c_x=g_K(z)g_K(x)d_x. Hence each original
exterior row for x<y is the ratio exterior row multiplied by the explicitly
saved nonzero scalar g_K(z)^2*g_K(x)*g_K(y). The verifier reconstructs
and compares every original block entry, covector and pivot. It uses
full Gauss–Jordan reduction of the ratio stack, separately from the
producer's incremental elimination. Its pivots and entire canonical
null basis agree in every case.

For every saved original maximal minor the verifier computes its
determinant by elimination on its transpose; every residue agrees and
is nonzero. It separately checks all original and ratio residuals and
the basis identity on free coordinates, with rank plus nullity equal
to 21. Thus each nonzero twelve-by-twelve minor proves rank at least
twelve, the row count proves rank at most twelve, and nine independent
null vectors span the entire kernel. This is a complete finite exact
certificate, not a sample or inference from a histogram.

### Scalar extension and historical prefix bindings

Every minor and basis entry lies in F_97. A nonzero minor remains
nonzero in E. The nine null vectors remain null, and their identity
on free coordinates remains an independence certificate. Rank-nullity
over E therefore shows that they span the entire E-kernel as well.
This uses L109's existing minors mechanism. No descent of a decomposable
point, actual weights, parameters or chart is asserted.

The verifier reads L110's saved literal seed inputs and L125's saved
literal pair inputs. It checks their zero-based prefix bindings against
this universe and compares all entries of the two six-row original
blocks to the previously saved original blocks. The bindings are:

| Prefix | Pair indices | Second support | Original maximal minor residue |
| --- | --- | --- | ---: |
| L110 | (0,411) | {12,18,64,70} | 15 |
| L125 | (0,412) | {12,18,64,75} | 46 |

Both first supports are {1,8,47,50}. Both prefixes use all twelve
original rows and pivot columns
0,3,4,8,9,11,12,13,15,16,18,19 (zero-based). Their complete bases
are separately verified and retained. They are different kernels:
in the canonical basis vector for free column 5, coordinate 0 is 11
for L110 and 67 for L125. This is an explicit reminder that a common
rank and pivot profile do not identify the kernels. No later-row locus,
count or exclusion is transferred.

### Reproduction and limits

Run from the notebook:

    python3 scripts/seven-coordinate/all_disjoint_pair_census.py
    python3 scripts/seven-coordinate/verify_all_disjoint_pair_census.py

The master is `scripts/seven-coordinate/all-disjoint-pair-census.json`;
its 105 full original batches are in
`scripts/seven-coordinate/all-disjoint-pair-census/`.
The complete independent replay master is
`scripts/seven-coordinate/all-disjoint-pair-census-replay.json`, with
per-pair replay evidence in the matching `all-disjoint-pair-census-replay/`
directory. The master records all batch hashes; the replay also records
the inspected source-code hashes. Full execution logs have matching
`all-disjoint-pair-census.log` and `all-disjoint-pair-census-replay.log`
names. All 1,114,800 replay comparisons passed. Original zero residuals
are saved in full; replay batches record each independently recomputed
minor, rank, pivots, complete-basis hash and residual counts.

These paths share Python, finite-field arithmetic, specified labels and
standard elimination theory. Same-step independent replay is not a later
critical audit or formal verification. No numerical approximation is used.
The bound is only for this fixed finite H/S; it makes no assertion over
other supports, fields or challenge parameters.

Uniform ranks provide no rank strata. The registry may supply concrete
inputs to a separately assessed many-row test. The still-missing gate
is simultaneous compatibility of at least twelve actual two-overlap rows
through one decomposable point of an arbitrary pair kernel, retaining
pairwise linearity, degree at most four, all rank-one/full-weight gates
and the original finite chart. None is tested here. L104's local survivor
and ATTEMPTS/041–043 remain consistent with this outcome. No pair exclusion,
universal representation, t=0/sixteen-event realization or challenge
identification follows. The frozen interval remains 11/q–16/q.

### Separate critical audit — step 480, 2026-10-25

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-l153-critical-certificate-audit-review.md`
authorized this RESEARCH / REPRODUCTION audit. The original producer,
independent replay, original block constructor and incremental elimination
were read against L109's formula (1). No defect was found in the finite
claim or its scalar-extension argument. This validates an existing input;
it supplies no new exclusion or advance beyond the checked sources.

The new `scripts/seven-coordinate/audit_l153.py` imports none of those
programs and does not regenerate any original certificate. It fixes the
literal H/S/J, checks H against all roots of X^16-1 in F_97, constructs
the ordered universe from four-subsets of H, and compares the exact
complete disjoint unordered pair set with all original records. It checks
all 105 batches, their grouping and uniqueness, and both literal historical
prefix bindings against the original L110/L125 artifacts. Counts supplement
the exact set equality; no symmetry reduction or sampled acceptance is used.

It evaluates each seven-root product directly, reconstructs every original
covector and exterior entry in the prescribed order, and checks all saved
blocks in full. Separately, all saved replay polynomial evaluations, pivots,
nonzero row scales and ratio entries are checked against these original
values. The identity c_x=g(z)g(x)d_x fixes both the sign and row multiplier;
all these factors are nonzero because the roots lie outside S union K.

For each original stack, the audit checks twelve distinct original rows,
twelve increasing distinct pivot columns, and the whole nine-by-21 basis
with canonical F_97 entries. It evaluates the selected original minor by
fraction-free integer condensation, checking every division exactly and
accounting for row swaps. This is the integer determinant verification
already used in L109, implemented independently here; it does not call
either modular determinant routine. Its reduction modulo 97 agrees with
every original nonzero residue. All original and ratio residuals are
evaluated in full, and the basis restriction to the nine free coordinates
is checked to be the identity. Thus acceptance does not depend on trusting
either producer back substitution or replay Gauss–Jordan elimination.
The saved replay records are also compared in full. Their basis hashes
are supplementary bindings, not substitutes for checking the actual vectors.

The complete run checked 95,256 original block entries, 79,380 integer
minors, 714,420 entire basis vectors, 8,573,040 original residual entries
and 8,573,040 ratio residual entries. All 1,119,770 recorded comparisons
passed. Every original/replay input digest was rechecked after the run;
none of those artifacts was rewritten. Both prefix minors are 15 and 46,
and the stated free-column-5 basis coordinates remain 11 and 67.

For completeness over an arbitrary extension E/F_97, the inclusion of
fields is injective, so each certified nonzero minor remains nonzero.
The twelve-row upper bound on rank remains twelve; hence rank over E is
exactly twelve. The nine saved vectors remain null under this inclusion.
Their free-coordinate identity makes every E-linear relation trivial:
looking at its nine free coordinates gives all nine coefficients zero.
Rank-nullity over E now gives dimension 21-12=9, so these vectors span
the entire E-kernel, including vectors with non-base-field coefficients.
This checks the existing scalar-extension proof without assuming that
planes, recovered weights, event parameters or a chart descend to F_97.

Reproduce only this audit from the notebook with:

    python3 scripts/seven-coordinate/audit_l153.py

The complete master is `scripts/seven-coordinate/l153-critical-audit.json`;
the 105 full per-pair evidence files are in
`scripts/seven-coordinate/l153-critical-audit/`. They retain every integer
determinant and both full residual arrays, with bindings to the unmodified
original bases. The log is `scripts/seven-coordinate/l153-critical-audit.log`.
The source and complete input manifests are recorded in the master.
Shared Python, exact integer arithmetic and the standard determinant and
rank-nullity arguments remain trusted infrastructure; this is not formal
proof-assistant verification. The audit checks no twelve-row feasibility,
gated locus, uniform exclusion or challenge identification. L154 may use
this validated finite kernel input only under its unchanged hypotheses.

## Mathlib

Full matching finite census: **not checked**. Supporting matrix rank,
rank-nullity, scalar extension, finite-field, exterior-power and coding
coverage is not checked anew. L109's source and Mathlib qualifications
are retained. Unknown coverage is not evidence of absence; these Python
certificates are not a formal proof-assistant verification.
