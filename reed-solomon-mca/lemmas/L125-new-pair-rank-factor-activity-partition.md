# L125 — New-pair complete rank, factor and activity partition

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, C=RS[F,H,8],
L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. The actual Hankel determinant D and all actual coordinate
locators are nonzero polynomials. Both coefficient syndromes belong to
U_S for S={1,8,12,18,22,27,33}. Assume sixteen original finite events,
L104's t=0, arbitrary original weights and prescribed finite chart.
Retain the inherited L010/L103/L104 and L086/L109 finite-certificate
qualifications. The two fixed supports are actual:

    A1={1,8,47,50}, A2={12,18,64,75}.

No representation or occurrence of this pair is extracted universally.
Write J=H minus S and use the lexicographic universe
U=binom(S,2) times binom(J,2), interpreting (I,K) as I union K.
Indices in this result are zero-based indices in this full 756-element
universe, for both third and fourth supports; they are not historical
L114 indices. An eligible occurrence (C,D) consists of four distinct
supports A1,A2,C,D with all six pairwise intersections of size at most one.
C need not be disjoint from the fixed pair. Do not quotient by row exchange,
label permutations or historical exclusions.

For each occurrence use L109's original 24-by-21 stack, with
z_j=min(S minus I_j) in each block and increasing S-pair columns.

## Conclusion

The entire eligible ordered domain contains 382 thirds and 100,764
occurrences. Its sufficient-filter partition, in the stated priority, is:

| First applicable disposition | Ordered occurrences |
| --- | ---: |
| Rank 21 | 56,828 |
| Whole kernel in E_c wedge F^S, for c in a selected row's overlap pair | 43,422 |
| Whole kernel omits an S-coordinate, with neither preceding filter passing | 360 |
| Residual of all these filters | 154 |

Thus 100,610 occurrences have necessary-condition exclusions. Every one
of the 154 residual complete kernels is preserved, over 54 thirds.
No feasible plane, additional recovery, third exclusion, pair exclusion
or equality witness is inferred from a residual. No actual-row assembly
or new Plucker-locus calculation is performed here. The global interval
remains 11/q–16/q.

All deficient kernels are saved, including those excluded by a sufficient
filter. The rank histogram is {18:9120,19:506,20:34310,21:56828}.
Among deficient occurrences, 43,422 pass at least one factor test and
33,574 pass at least one omission test. These sets overlap; the headline
table counts an occurrence just once. There are 162,392 passing factor
tests and 167,150 passing omission tests. Every failed test has a saved
nonzero coefficient witness, including failed tests in an excluded case.

Complete same-step independent replay passes. The separate step-358
critical audit below found no defect. This is REPRODUCTION of assessed coding/exterior mechanisms
with new labeled finite evidence, not a new general theorem or a claim
of progress beyond the checked literature.

## Proof

### Imported tools and new-label applicability

L086 makes every actual equality support pair linear, so actual third
and fourth two-overlap supports must lie in the stated domain. L109's
necessary direction supplies independent lift coefficients u,v and a
nonzero decomposable tensor p=u wedge v in every selected stack kernel.
It also supplies the rank-one projection and full-weight gates. Only
these necessary directions are used. No four-row converse is invoked.

Standard coding inputs are imported through L104/L109: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the shortening formula after Lemma 5.3.
All sixteen labels are distinct, the multipliers are nonzero and k=8.
For each new row, exactly seven labels J minus K are shortened, reducing
dimension eight to one through positive dimensions. Products of retained
label differences remain nonzero. Changing 70 to 75 in A2 changes these
products and the indexed ranks, but none of these hypotheses. No old
labeled matrix, count, kernel or exclusion is transported.

Exterior bases and nonzero wedges representing two-planes are imported
from Keith Conrad, *Exterior Powers*, undated 47-page author PDF inspected
2026-10-18, [Theorems 4.2, 7.1 and 7.5, pp. 11–12, 23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
They apply over F_97 and its extensions; L109 already gives the explicit
pivot reconstruction and recovery formulas. L116's whole-factor proof
and L118's omission proof are specialized below, rather than importing
their historical domains or reproving a general coding theorem.

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-new-disjoint-pair-filter-review.md`.
Its primary coverage and duplicate comparison are reused. ATTEMPTS/041–043
remain valid failures of broader rank/factor/selected-row shortcuts.
The bounded target is this partition alone, even if it had no residual.

### Exact domain, original matrices and complete rank certificates

Reproduce from the notebook:

    python3 scripts/seven-coordinate/new_pair_filter.py
    python3 scripts/seven-coordinate/verify_new_pair_filter.py

The master is `scripts/seven-coordinate/new-pair-filter.json`;
its full per-third certificates are in `scripts/seven-coordinate/new-pair-filter/`.
The complete replay is `scripts/seven-coordinate/new-pair-filter-replay.json`.
The two full execution logs have names `new-pair-filter.log` and
`new-pair-filter-replay.log` in the same parent directory.

Both programs independently construct H, J and U. Every universe member
has its two fixed-pair intersection sizes and distinctness saved. There
are exactly 382 eligible thirds. For each, all 756 fourth candidates have
their three new intersection sizes and distinctness saved, including all
ineligible candidates. The complete eligible ordered case lists agree;
there are 100,764 cases. The verifier also checks all six pairwise
intersections on every retained four-support family. No disjoint-third
restriction, historical deletion or exchange identification is used.

For every universe row the producer evaluates
g_K(x)=product_(y in J minus K)(x-y) directly. It stores the four
original covectors c_x=g_K(z)E_x^*-g_K(x)E_z^* and all six original
exterior rows. The verifier reconstructs these by differentiating

    X^16-1=g_K(X)*product_(y in S union K)(X-y).

At x in S union K this gives

    g_K(x)=16*x^15/product_(y in (S union K) minus {x})(x-y).

The denominators and numerator are nonzero. Ratio covectors
E_x^*/g_K(x)-E_z^*/g_K(z) give each original exterior row after
multiplication by the nonzero factor g_K(z)^2*g_K(x)*g_K(y).
Every original block entry, pivot and covector is compared, so the
replay checks original equations, not only a rank-equivalent system.

The producer performs incremental original-row elimination. For each
rank r it saves r independent original-row indices, r pivot columns,
the nonzero residue of that original r-by-r minor, and 21-r null vectors
in increasing free-coordinate order. Its minor residue is the product
of the insertion pivots, corrected by the sign of the permutation from
their insertion order to increasing column order. This is the determinant
because original-row additions preserve the selected minor, and the
insertion-order pivot matrix is triangular after that column permutation.

The verifier instead eliminates original columns, tracking their exact
linear relations. Its chosen columns and freshly reconstructed canonical
null basis agree with every saved case. It separately evaluates every
saved original maximal minor by column-pivoted determinant elimination.
Thus no producer rank or minor value is trusted. Each basis has identity
on its free coordinates; all 62,682 vectors have all 24 original residual
entries saved and checked, giving 1,504,368 zeros. Independence, these
residuals and the nonzero rank-r minor prove exact rank and complete
kernel, including every higher-nullity case. Both paths give the stated
rank histogram.

All entries and witnesses are in F_97. A nonzero original minor stays
nonzero after scalar extension. The complete independent null vectors
remain null and independent, bounding the extension rank from above by r.
Consequently the same basis spans the entire extension kernel. No rational
descent, extension-point sampling or assumption of a one-dimensional
kernel occurs.

### Entire-kernel factor and selected-row failure

For every deficient case, all eight choices (j,c), c in I_j, are tested.
All entries in S-pairs not containing c must vanish on every basis vector.
This is equivalent to whole-kernel containment in E_c wedge F^S. Every
failed test saves a basis index, a forbidden column and its nonzero value.
The verifier forms the complete antisymmetric matrices of its fresh basis
and independently checks every entry outside the c row and column.
All passing and failing choices remain recorded; the fixed priority is
rank, then any factor, then any omission, then residual.

For a passing (j,c), specialize L116's entire-locus argument. Any nonzero
extension-kernel tensor is E_c wedge w and its plane contains E_c. Since
c is in the chosen row's I_j, Q_j E_c=0. A rank-zero restriction Q_j|_L
contradicts actual polynomial nonpersistence by L109. In rank one, its
kernel on L is exactly the line spanned by E_c. A projective recovery
h=a E_c, a nonzero, has z_j outside I_j, hence

    lambda=h_zj/g_j(z_j)=0.

The other overlap error weight and both outside error weights are zero.
This fails L109's necessary full-weight gate; equality was assumed before
requiring full errors. Every extension point is covered by the rank-zero
or rank-one alternative, independently of the projective pivot.

The master saves coefficient certificates for both overlap labels of all
756 possible selected rows: z_j, nonzero g_j(z_j), Q_j E_c, lambda,
all four error weights and all eight original shifted-moment residuals.
The verifier independently checks all 1,512 certificates with the derivative
formula. Projections and moments vanish, lambda is zero and exactly three
error weights are zero. Checking h=E_c verifies the coefficients of these
linear identities for every h=a E_c; it is not sampling possible planes.
This establishes all 162,392 passing factor tests.

In the prescribed original basis a recovery is finite only when its
original coefficient alpha is nonzero. If alpha=0 it is omitted; otherwise
division by alpha preserves all failed zero weights. Arbitrary nonrational
original charts therefore cannot repair this intrinsic exclusion.

### Whole-kernel omission and full activity

For each deficient case and each x in S, test all six incident exterior
entries on every basis vector. Their simultaneous vanishing is exactly
whole-kernel omission of x. Each failed coordinate saves a nonzero basis
entry witness. The verifier independently checks that row of every full
antisymmetric basis matrix. It checks all seven coordinates even when
another sufficient filter already passes. There are 167,150 passing
coordinate tests in 33,574 occurrences; overlap with factor passes is
retained rather than subtracted twice.

Specialize L118's omission proof only to the necessary actual tensor.
If a nonzero decomposable p omits x, choose p_ab nonzero. Then a,b differ
from x, and L109's reconstruction u_y=p_yb/p_ab, v_y=p_ay gives
u_x=v_x=0. The actual plane is their span, so both original lift
coefficients also vanish at x. This contradicts L104's full-activity
conclusion: both coefficient syndromes are then supported on at most six
coordinates, and L103 gives at most fifteen original finite events with
the retained actual D/locator and finite-certificate premises.
Sixteen original events were assumed before this contradiction.
Nonzero constants remain active; no plane is assigned to an arbitrary
nondecomposable kernel tensor. Plane-coordinate vanishing is invariant
under the prescribed original basis and its omitted direction.

### Partition, residuals and limits

Every independent replay disposition, failure witness, complete kernel,
original minor, residual entry, per-third index and shard hash agrees.
Both runs exit successfully with no failures. The headline statuses sum
to 100,764, with precisely 154 residual ordered pairs over 54 thirds.
The first residual has universe indices (58,355),
C={1,12,70,79}, D={8,27,79,89}, rank 19 and a complete two-dimensional
kernel. Its full basis, all failed tests and all original residuals are
saved; this observation supplies no Plucker-locus or recovery assertion.

The three sufficient filters stop here for this pair. No untested residual
is dropped, no third exclusion is assembled recursively, no all-pair
sweep is run, and no four-row feasibility is interpreted as sixteen events.
Universal seven-coordinate representation, disjoint-pair extraction,
arbitrary t=0 exclusion and challenge qualifications remain open.
Same-step replay shares Python and residue arithmetic with the producer
and uses the previously audited derivative helper. It is not a separate
critical audit or proof-assistant verification. Historical artifacts,
including L124's old-pair certificates, remain untouched.

### Separate critical audit, 2026-10-20

Step `2026-10-20-mca-358-new-pair-partition-critical-audit` used the
unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-10-20-new-pair-partition-audit-review.md`.
Its TARGET matches the invocation-start action verbatim. The whole proof,
both complete programs and every called mathematical helper were inspected.
L086's equality scope, L103's six-coordinate full-event bound, L104's
shortening and full activity, L109's necessary equations, independence,
reconstruction and rank-zero/full-weight/original-chart gates, and L116/L118's
factor/omission proofs were checked. Their historical counts are not inputs
to this partition. Ready primary coverage is reused with its exact hypotheses
and inherited finite-certificate qualifications, without recomputing that chain.

Reproduce the separate audit from this notebook:

    python3 scripts/seven-coordinate/audit_l125_partition.py

The full audit certificate is `scripts/seven-coordinate/l125-critical-audit.json`;
the complete fresh log is `scripts/seven-coordinate/l125-critical-audit-replay.log`.
The wrapper binds all 390 original master, replay, shard, program/helper and
log files by hashes, checks the full saved replay and both complete historical
logs, executes the inspected independent verifier, and requires byte preservation
of every original file and equality of the entire replay. It does not run
the producer or repeat its mathematical filter search.

The direct helper's historical SUPPORTS and derivative helper's historical
SEED are unused by their imported block functions. Both use the same S,H,
with I,K supplied anew. Differentiating X^16-1 at a simple nonzero root
gives the stated values on S union K. The ratio covector is c_x/(g(z)g(x));
the exterior multiplier g(z)^2*g(x)*g(y) therefore restores each original
row entrywise. All 756 blocks and 1,512 coefficient gate certificates agree,
including all original shifted moments. Rank equivalence alone is not used.

Each inserted producer echelon row vanishes on earlier pivot columns after
elimination. On its chosen original rows and insertion-ordered columns these
operations give a triangular minor. The insertion-pivot product, corrected
by the column-permutation sign, is its original determinant. The verifier
independently eliminates columns while tracking exact relations and evaluates
every selected original minor by column-pivoted determinant elimination.
Its null vectors have the identity on free coordinates. The nonzero rank-r
minor, 21-r independent null vectors and all original residual zeros prove
exact rank and complete kernel. All 100,764 minors, 62,682 vectors and
1,504,368 residual entries pass. Nonzero base-field minors and these complete
bases give the same kernels over extensions, without extension-point sampling.

All 756 third screens and all 756 fourth screens for each of 382 eligible
thirds are reconstructed. Ordered lists, distinctness, all six intersections,
shard hashes and per-third counts agree. Every deficient case retains all
eight factor and seven omission predicates, with every nonzero failure witness.
Full antisymmetric matrices supply the verifier's separate predicate path.
Overlapping pass sets and the priority partition agree with every stated count;
no historical case is deleted and no exchange quotient is imposed. Required
and actual case counts are both 100,764; all 154 residuals over 54 thirds
persist. The full first residual (58,355), rank 19, both null vectors and
its exact labels are preserved as a regression, not a feasibility assertion.

For a whole factor, every nonzero tensor defines a plane containing E_c.
Its chosen Q has rank zero or one: actual nonpersistence rejects zero,
while rank one makes the recovery line exactly F E_c. Its lambda and three
error weights vanish. The linear coefficient certificates cover every scalar
and extension. For omission only the necessary actual nonzero decomposable
tensor is interpreted: a nonzero pivot avoiding the omitted coordinate
reconstructs two spanning vectors zero there. The whole actual lift omits
that coordinate, contradicting L104 via L103. Nonzero constants remain active.
An original chart either deletes the recovery or rescales its failed weights;
it repairs neither exclusion. No four-row converse is used.

No mathematical defect, changed dependency, new exclusion or global count
improvement was found. This separately validates a restricted finite input,
without progress beyond checked literature or proof-assistant verification.
Shared Python/residue arithmetic and inherited computational qualifications
remain. This section supersedes the overview's historical pending-audit
wording without changing the argument. All residual feasibility, third/pair
assembly, universal representation/extraction and challenge qualifications
remain open. The inexpensive filters stay stopped.

## Mathlib

Full matching coverage for this exact finite labeled partition is not
checked. Supporting coding/exterior coverage is not newly checked;
the precise standard inputs above and L109/L104 are reused within the
ready assessment. Unknown availability is not evidence of absence.
No formal verification or mathematical originality is claimed.
