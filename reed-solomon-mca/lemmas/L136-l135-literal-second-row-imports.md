# L136 — L135 literal row-two imports cover 17 ordered occurrences

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's shifted
moments and the pinned same-support event on 1/4<=delta<5/16.
The actual Hankel determinant D and all actual coordinate locators are
nonzero polynomials. Both coefficient syndromes belong to U_S,
S={1,8,12,18,22,27,33}. Assume sixteen original finite events and
L104's represented t=0 class, with arbitrary extension-field weights
and prescribed original chart. Retain L109's inherited L010/L103/L104/
L040/L069/L086/L056 finite-certificate qualifications.

The actual fixed pair is A1={1,8,47,50}, A2={12,18,64,75}.
Use L125's full zero-based lexicographic universe binom(S,2) times
binom(J,2), J=H minus S, increasing S-pair exterior coordinates, and
original pivot z=min(S minus I). For an occurrence (n,u), assume its
third and fourth supports are also actual two-overlap errors. Preserve
their order. No universal representation or fixed-pair extraction is
assumed.

## Conclusion

The complete 99-record domain obtained from L134's historical 100
literal mismatches by removing only (94,539) has been tested against
L135's complete ordered kernel. Exactly seventeen match literally and
bind both exhaustive points to identical rejecting row-two inputs.
Writing T={95,96,97,102,103,104,105,106}, the matches are

    (a,539) for a in T, and (539,b) for b in {94} union T.

Each has inconsistent actual-error hypotheses over every extension of
F_97 and every prescribed original chart. The occurrence (539,94)
exchanges the previously certified L135 family; the other sixteen are
additional ordered bindings, not sixteen distinct unordered families.
All 82 mismatches, the historical 100/118/154 lists, and exchange
multiplicities remain saved. A mismatch does not assert feasibility.

This is a reproduced restricted input; the separate step-402 critical
audit below found no defect.
No changed-row gate, new locus, basis conversion, further filter,
third/pair assembly, universal extraction or global improvement follows.
The frozen-model interval remains 11/q–16/q.

## Proof

### Assessed inputs and source scope

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-21-l135-literal-reuse-review.md`.
This is RESEARCH / REPRODUCTION: local indexed progress by literal import
of audited algebraic subresults, not progress beyond the general sources
checked. L109 supplies the necessary nonzero actual wedge, full-weight
and prescribed-chart direction. L125 supplies the original domain and
complete kernels. L134 supplies the audited historical mismatch domain,
including its L132 provenance. L135 supplies only its unconditional
kernel/locus and individual row-two subresults with the step-398 audit.
Its inconsistent four-actual-support hypotheses are not imported as a
theorem about changed supports. ATTEMPTS/041–044 and previous reference
comparisons remain preserved; their stopped filters are not reopened.

Import the standard tools through these inputs, using the ready primary
extractions recorded in the assessment:

- J. I. Hall, *Notes on Coding Theory*, undated author GRS chapter,
  [Theorem 5.1.1 and proof, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
- I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
  that have an error correcting pair*, FFAA 40 (2016), 224–245,
  DOI 10.1016/j.ffa.2016.04.004, [accepted manuscript 2016-02-29,
  section 5, Definitions 5.1–5.2 and formula after Lemma 5.3,
  pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
- K. Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and proofs,
  pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
- J. S. Milne, [*Fields and Galois Theory*, Kea Books 2022,
  sections 1.6–1.9 pp. 5–7 and Proposition 2.17 p. 34](https://www.jmilne.org/math/Books/FT0.pdf).

The labels are distinct, multipliers nonzero, and k=8. Each row shortens
exactly seven J-minus-K labels through positive dimensions eight to one;
all label-difference products remain nonzero. Exterior bases and the
nonzero-wedge/plane correspondence apply over any field, here in degree
two and dimension seven. L109 gives the explicit reconstruction criterion.
Polynomial division/Bezout and extension-gcd invariance underlie L135's
already audited split homogeneous locus; no new polynomial solving,
general-theorem reproof or original-chart rational descent is required.

### Complete original domain and kernel binding

Reproduce from this notebook, with assertions enabled:

    python3 -E -B scripts/seven-coordinate/l135_literal_reuse.py
    python3 -E -B scripts/seven-coordinate/verify_l135_literal_reuse.py

Full evidence is in `scripts/seven-coordinate/l135-literal-reuse.json`
and `scripts/seven-coordinate/l135-literal-reuse-replay.json`.
The producer specializes the inspected L134 binding program; its
independent replay specializes the separate row-reduction path and
imports no producer helper. Historical files remain unchanged.

The complete prior certificate `scripts/seven-coordinate/l133-literal-reuse.json`
and replay are SHA256-bound to the step-394 L134 audit manifest. Every
audit check passes and their complete mismatch lists agree. The list
contains exactly 100 distinct ordered records, with (94,539) once.
Removing only that record gives precisely 99 distinct ordered entries,
compared in full and in order with the new overlay. The entire historical
154 list agrees with L125's audited master; the 118 and 100 lists remain
explicit. All 54 historical per-third residual lists bind to unchanged
audited shards, without recursive deletion or exchange quotients.

Every tested occurrence keeps its original shard pointer, complete
record, four support labels, minor rows/columns/residue and full ordered
null basis. The record is identical in the prior unmatched overlay and
L125's shard. The complete 756-row universe is regenerated. All four
supports are distinct and all six pair intersections have size at most
one. L125's original master, replay and shard hashes are checked, as
are the audited column-kernel and determinant helpers.

For every row the producer expands g(X)=product_(y in J minus K)(X-y),
evaluates it on S union K, and reconstructs all four original covectors

    c_x=g(z)E_x^*−g(x)E_z^*, x in (S minus I) minus {z},

and their six exterior rows. Every original block agrees with L125.
The independent replay instead uses differentiation at the simple roots
of X^16−1:

    g(x)=16*x^15/product_(y in (S union K) minus {x})(x-y).

All denominators are nonzero. Elementary symmetric sums independently
recover the ascending polynomial coefficients. Thus the row-two input
comparison includes the actual polynomial, g-values, pivot, covectors
and original block in exactly the original normalization.

The producer's column elimination tracks relations among original
columns; its determinant path pivots columns. Independent replay uses
full row reduction and row-pivoted determinant elimination. Both recover
every complete ordered null basis and original nonzero rank-r minor.
Each basis has the identity on its increasing free columns and all
24 original residual entries per vector vanish. Independence, the
nonzero minor and these null vectors prove rank r and completeness over
every extension: the same minor and identity remain nonzero there.
The 99 records comprise 91 rank-19 and eight rank-20 stacks. All
49,896 original entries and 4,560 null residual entries pass replay.
These are input checks, not a renewed rank/factor/activity filter.

Every comparison uses the entire ordered basis in the same 21 exterior
coordinates. For each mismatch the certificate saves the basis-length
difference or first differing entry with both values. There is no
proportionality test, relabeling, sampled-point test or basis conversion.
The complete two-program comparison gives exactly the seventeen stated
indices; all 82 other dispositions are independently replayed.

### Literal source locus and unchanged row-two rejection

L135's complete step-398 audit has no failures. Its seven input hashes,
including programs, helpers, original shard and both full certificates,
bind unchanged. The source replay's certificate hash, full original
matrix, null residuals and all 35 homogeneous coefficient triples agree.
Both source points, complete plane representatives, row-two gate records,
original-row replay and every saved nonzero exterior/projection pivot
choice for that row are retained verbatim.

For every literal match the source basis is

    B0=E_1 wedge E_12,
    B1=u wedge v,
    u=(1,25,15,0,54,67,84), v=15E_18.

L135's unconditional algebraic subresult gives the complete homogeneous
decomposable locus p=sB0+tB1 as st=0 over every extension, including
infinity: its only nonzero restrictions are 13st,63st,62st,st at
(1,8,12,18), (1,12,18,22), (1,12,18,27), (1,12,18,33).
All 35 restrictions, affine division/Bezout coefficients and both
projective endpoints are bound literally. Thus the only candidate
planes are L0=span(E_1,E_12) and L1=span(u,15E_18), with the identical
source representatives. No new locus has been computed.

The fixed second row has I={12,18}, K={64,75}, z=1. Its covectors
annihilate E_12 and E_18, while

    Q_2 E_1=(12,60,56,19), Q_2 u=(44,36,37,14).

Both projections have rank one. L135's imported intersection lines are
F E_12 and F E_18, respectively. In the precise saved representatives,
their (alpha,beta) are (0,12) and (0,44), lambda=0, and weights on
increasing I then K are (12,0,0,0) and (0,78,0,0).
Their eight original shifted moments and sixteen pointwise identities
per point are retained, not just a failure flag. Every target row-two
input equals the source input, so these exact representatives, gates,
moments and all nonzero pivot records apply unchanged to both points
of every matching kernel. All 34/34 exhaustive point/row bindings pass.
No changed-third/fourth-row gate is calculated or needed.

For completeness, the imported prescribed-chart argument is symbolic:
write u_original=A u_i+B v_i, v_original=C u_i+D v_i, with
Delta=AD−BC nonzero. The first original coefficient of
h=alpha u_i+beta v_i is (D alpha−C beta)/Delta. If its numerator
vanishes the direction is outside the prescribed finite chart;
otherwise normalization rescales all weights by the same nonzero scalar.
The lambda-zero and outside-zero weights therefore cannot be repaired,
including for nonrational chart entries. The exact finite-gate pairs
(D_coefficient,C_coefficient)=(0,85),(0,53) are bound to source replay.

L109's necessary actual-wedge direction forces an actual pencil into
the complete kernel and one of these two exhaustive planes. Its
necessary full-weight gate rejects each plane already at row two.
This contradiction proves each indexed exclusion. Only necessary
directions are used; the r>=6 converse supplies no four-row realization.

### Qualifications and limits

The complete independent replay checks every original input, comparison,
mismatch witness and point/row binding, with zero discrepancies. Both
implementations share Python and residue arithmetic. This is same-step
replay, not a separate critical audit or proof-assistant verification.
The inherited finite-certificate qualifications remain. The old exchange
(539,94) is distinguished from sixteen additional ordered bindings;
no count of new unordered families or third/pair exclusion is inferred.
Unmatched records remain unresolved, as do universal representation and
extraction, sixteen-event equality and certified challenge definitions.

### Separate critical audit, 2026-10-22

Step `2026-10-22-mca-402-l136-critical-audit` completed the exact
invocation-start SPECIALIZE target in
`drafts/literature/2026-10-22-l136-critical-audit-review.md` as
RESEARCH / REPRODUCTION / proof_audit. The entire proof, both complete
binding programs and their called `column_kernel` and `determinant`
helpers were inspected. The imported derivative module has no search
on import; none of its mathematical routines is called in this overlay.
L109's necessary nonzero-wedge/full-weight/chart direction, L125's
original domain and complete-kernel proof/audit, L134's audited mismatch
domain with L132 provenance, and L135's unconditional algebraic and
individual-row subresults with step-398 audit were checked. The supplied
primary-source assessment is reused with its exact hypotheses; no general
theorem is reproved or source-freshness claim made.

Reproduce from this notebook with assertions enabled:

    python3 -E -B scripts/seven-coordinate/audit_l136.py

The complete manifest, execution output, per-occurrence comparisons,
source bindings and checks are in
`scripts/seven-coordinate/l136-critical-audit.json`.
The bounded wrapper copies 89 original program/input/output files into
an isolated tree preserving relative paths. Both entire binding programs
run with `-E -B`, ignoring inherited Python optimization settings. Both
full certificates reproduce byte for byte. Every copied file and all
89 originals remain unchanged. No older filter or enlarged search runs.

Independent four-subset generation gives the full 756-row universe and
the specified fixed pair. All 54 historical shard residual lists agree
with L125's audited master. The complete 154/118/100 lists and prior audit
hash maps bind unchanged. Only (94,539) is removed from the 100 list,
leaving 99 distinct ordered original records. Their unique pointers,
support labels, original minors, complete ordered kernels, residuals and
prior unmatched dispositions agree. Full fresh replay reconstructs all
49,896 original entries and 4,560 null residual entries. The direct
product and derivative constructions agree in the original normalization;
column and row elimination independently recover the kernels and minors.
Identity on free columns and a nonzero rank-r minor certify completeness
over every extension, rather than just the base field.

All seventeen matches equal the displayed index set; all 82 mismatches
retain their exact differing-entry or basis-length witnesses. The old
exchange (539,94) is distinguished from sixteen additional ordered
bindings. Literal equality concerns the entire ordered basis in the same
exterior coordinates. It therefore imports L135's unconditional
homogeneous locus, not its inconsistent four-actual-support conclusion.
All 35 homogeneous restrictions, affine quotients, Bezout coefficients
and both endpoints agree with the audited source. The restriction st
itself and the other multiples of st leave exactly the two projective
points over every extension, including infinity.

Both complete row-two inputs, plane representatives and gate records
bind literally. The audit independently reconstructs all 28 nonzero
exterior/projection pivot choices for this row, checking a nonzero
proportionality scalar, intersection vector and all weights in each case.
These cover four projection components at the sole exterior pivot of
the first point and four components at each of six pivots of the second.
The original pointwise identities, all eight shifted moments per point,
and finite-chart coefficient pairs (0,85),(0,53) agree. All 34 target
point/row bindings are complete. No changed-row calculation is needed.

The row-two intersection lines are F E_12 and F E_18. Their zero z=1
coordinate gives lambda zero and zero outside weights, contrary to the
necessary full-error condition. For an arbitrary original basis the
coordinate matrix is [[A,C],[B,D]], with determinant AD-BC nonzero.
Inversion gives first coefficient (D alpha-C beta)/(AD-BC): if zero,
the direction is omitted; otherwise normalization multiplies every weight
by a nonzero scalar and preserves the failure. This covers nonrational
prescribed charts without selecting a favorable one. Only L109's
necessary direction is used, never its r>=6 converse.

All 503/503 audit checks pass, with zero failures. No mathematical defect
or changed direct dependency was found. This validates the existing
restricted reproduced input, adding no indexed exclusion or progress
beyond the checked literature. Shared Python/residue arithmetic and the
inherited finite-certificate qualifications remain; this is not a
proof-assistant verification. This verdict supersedes historical
pending-audit wording without changing the argument, PROOF.md or DAG.md.
All historical lists and stopped-route evidence remain, and no third/pair
assembly, universal extraction, challenge-definition closure or global
interval improvement follows.

## Mathlib

Full matching indexed import/exclusion: **not checked**. Supporting coding,
exterior, polynomial and matrix coverage: **not checked** here. Unknown
availability is not absence. The precise standard citations and finite
certificate qualifications above are retained; no novelty is claimed.
