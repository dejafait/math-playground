# L118 — Complete residual inactive-coordinate partition

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, dimension eight,
L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. The actual Hankel determinant D and all coordinate
locators are nonzero polynomials. Both coefficient syndromes lie in U_S
for S={1,8,12,18,22,27,33}. Assume sixteen original finite bad parameters
and L104's t=0, with arbitrary extension-field weights and prescribed
original finite chart. Retain all inherited L010/L103/L104 and
L086/L109 computational qualifications.

Fix actual supports A1={1,8,47,50}, A2={12,18,64,70}. Select exactly
L116's historical 599 retained indexed occurrences over its 56 thirds,
with indices (n,u), ordered third list and fourth universe inherited
from L114 through L116. Repeated kernels at different indices remain
separate. Use L109's original 24-by-21 four-row exterior stacks and
increasing S-pair columns. Neither this pair nor a seven-coordinate
representation is extracted universally.

## Conclusion

The complete historical domain has the following sufficient-filter
partition:

| Disposition | Indexed occurrences |
| --- | ---: |
| Whole kernel omits an S-coordinate, contradicting equality full activity | 360 |
| No coordinate omitted by the whole kernel | 239 |

Each passing kernel omits exactly coordinates 22, 27 and 33. One passing
record is L117's already excluded (n,u)=(0,279). The other 359 are
additional indexed exclusions relative to L112/L117; none of the nine
exchanged-row L112 overlaps passes this screen. All 599 historical
factor-filter failures remain preserved. The 239 inactivity-screen
failures include those nine old exclusions and 230 other occurrences;
failure is not feasibility. Counts are not asserted novel relative to
every possible relabeling or other historical result.

This restricted finite-computation input has complete same-step replay;
the separate step-329 critical audit below found no defect. No third, fixed pair,
universal seven-coordinate class or equality pencil is thereby excluded.
The global error interval remains 11/q–16/q.

## Proof

### Imported tools and exact specialization

Use L109's necessary direction: actual lift coefficients are independent,
and their nonzero decomposable wedge belongs to every selected original
stack. Use L104's equality full-activity conclusion: an identically zero
coordinate leaves a lift supported on at most six coordinates, so L103
bounds the entire original bad set by fifteen, with its inherited finite
certificate qualifications. The field, original chart, actual D/locator
hypotheses and sixteen actual events here are precisely those inputs'
hypotheses. Constants different from zero are active.

Standard coding results are imported through these lemmas, without a
new distance or shortening proof: J. I. Hall, *Notes on Coding Theory*,
[Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the shortening formula after Lemma 5.3.
Here all sixteen labels are distinct, multipliers are nonzero, and
shortening exactly seven outside labels reduces dimension eight to one
through positive dimensions. No changed coding hypothesis is introduced.

Exterior coordinates and the association of a nonzero elementary wedge
to its two-plane use Keith Conrad, *Exterior Powers*, undated 47-page
author PDF retrieved 2026-10-18,
[Theorems 4.2, 7.1 and 7.5, printed pp. 11–12, 23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
These apply to the seven-dimensional free vector space over F_97 and
every extension, not merely to real vector spaces. The needed explicit
coordinate reconstruction is already proved in L109; the specialization
below explains coordinate omission, rather than reproving these theorems.

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-18-residual-kernel-inactive-coordinate-review.md`.
This is REPRODUCTION of assessed exterior/coding tools with a new local
census; no general coding theorem or progress beyond the checked
literature is claimed. ATTEMPTS/041–042 remain valid. Whole-kernel
coordinate omission differs from L116's common-factor containment.

### Complete historical domain, ranks and bases

Reproduce from this notebook:

    python3 scripts/seven-coordinate/inactive_coordinate_screen.py
    python3 scripts/seven-coordinate/verify_inactive_coordinate_screen.py

Full certificates are
`scripts/seven-coordinate/inactive-coordinate-screen.json` and
`scripts/seven-coordinate/inactive-coordinate-screen-replay.json`.
The first binds its master, shards and helpers to the successful separate
L116 step-321 audit. All 584 audited artifact hashes and five code hashes
are checked; before/after audit manifests agree, and all these artifacts
are checked unchanged again at the end. The source master is
`scripts/seven-coordinate/residual-coordinate-factors.json`.
Both programs reconstruct the ordered 756-support universe, 382 eligible
thirds, thirty disjoint removals and named removal, leaving the ordered
351-third historical list. They select exactly the unresolved records
in L116's shards and compare the saved remaining-index lists. There are
599 distinct indexed records over exactly the 56 saved third indices;
none is deduplicated by matrix or unordered support family.

For every selected record the producer reconstructs all original stack
entries from the direct products defining g_K. It compares them
entrywise with the independently rebuilt derivative/ratio construction
from the audited helper. That helper differentiates
X^16-1=g_K(X)*product_(y in S union K)(X-y) at each simple root x,
giving g_K(x)=16*x^15/product_(y in (S union K) minus {x})(x-y).
Every denominator is nonzero, as is 16 modulo 97. Its ratio covectors
rescale to the original exterior rows by the nonzero factors
g_K(z)^2*g_K(x)*g_K(y), as checked in the L116 audit. Thus these are
the original equations, not just matrices with the same rank.

Exact original-row elimination and independent column elimination
agree on every rank. The rank histogram is {19:593,20:6}.
The selected original-row submatrix is separately checked to have that
rank. Each saved basis agrees with its historical source and contains
21-r vectors with an identity on the complementary free columns.
Every coefficient is a canonical F_97 residue. All 1,192 vectors have
their 24 original residuals checked, giving 28,608 zero entries.
Independence, rank-nullity and these residuals prove completeness.
The replay independently performs full Gauss–Jordan elimination in
reverse original-row order, eliminates all other rows at each pivot,
and freshly reconstructs every complete nullspace. Every basis agrees.

Base-field ranks persist over every extension, since the nonzero
maximal minor remains nonzero and all larger minors are zero. The
saved independent null vectors consequently remain a complete basis
after scalar extension. This justifies interpreting whole-basis
identities over F and over arbitrary extensions; finite field-point
sampling is not used.

### Coordinate omission implies an inactive actual lift coordinate

For a coordinate x, the screen retains every one of the six incident
entries p_xy, y!=x, on every vector of the complete kernel basis.
All these entries vanish if and only if every kernel tensor omits x.
Every failure saves a particular nonzero coefficient with its basis
and column index. The replay forms every full antisymmetric seven-by-
seven matrix from each freshly reconstructed basis vector and tests
its x-row for zero, independently checking every stored incident
coefficient and every nonzero witness.

Suppose a screen passes at x and an actual equality pencil exists.
Its wedge p is nonzero and decomposable by L109. Extend its entries
antisymmetrically, with p_aa=0. Choose p_ab!=0; the six incident
zeros imply a,b!=x. L109's reconstruction is

    u_y=p_yb/p_ab,   v_y=p_ay.

For this decomposable p the reconstructed independent u,v have
u wedge v=p and span its actual lift plane. Since p_xb=p_ax=0,
u_x=v_x=0. Every vector in that plane has zero x-coordinate. In
particular both original coefficient vectors have zero x-coordinate,
so the actual affine lift has that coordinate identically zero.
This contradicts L104's equality full activity via L103. This argument
does not make any assertion about the plane of a nondecomposable tensor;
only the necessary actual decomposable tensor is interpreted.

The vanishing of a coordinate on a plane is basis invariant. Thus
changing to the prescribed original affine basis, including one with
a nonrational omitted point, cannot restore activity. No original
finite-direction gate, full error weight, nonpersistence assumption or
constant-coordinate case has been discarded. The contradiction uses
sixteen actual original finite events before applying the fifteen bound.

### Complete partition, overlaps and limitations

Both paths check all 4,193 coordinate tests. Exactly 360 occurrences
pass, each with omitted set {22,27,33}; every other coordinate in these
records has a nonzero witness. All seven coordinates in each of the
239 failures have a nonzero witness. The complete indexed partition
and coefficients are recorded, not just positive examples or a preview.
Both paths agree on every record and summary and report no failures.

Overlap bookkeeping, without adding exclusions or recursively removing
thirds, gives:

| Earlier comparison | Pass | Fail |
| --- | ---: | ---: |
| L117 occurrence (0,279) | 1 | 0 |
| L112 with the selected third/fourth exchanged | 0 | 9 |
| Neither comparison | 359 | 230 |

L112 is used only for its exact thirty-disjoint-third comparison; L117
only identifies its independently excluded index. Neither establishes
the omission implication or any of the 360 screen dispositions.
No additional third or fixed-pair exclusion is inferred. In particular,
these passing four-row systems are not an exhaustive new fourth-support
analysis for any third, and the failing kernels need their own necessary
Plucker/projection/full-weight/chart tests. No four-row converse is used.

Both implementations share Python, residue arithmetic and the audited
derivative helper; their same-step agreement alone is not a separate
critical audit or proof-assistant verification. Arbitrary t=0
profiles, seven-sets, universal representation/fixed-pair extraction,
the uniform fifteen bound and challenge-definition qualifications remain
unresolved. The complete historical failures and original stop evidence
are preserved.

### Separate critical audit, 2026-10-18

Step `2026-10-18-mca-329-inactive-coordinate-partition-critical-audit`
used the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-10-18-inactive-coordinate-partition-audit-review.md`.
The full proof, both complete programs and all their called mathematical
helpers were inspected. The exact L104 full-activity passage through
audited L103, L109's independence and pivot reconstruction, and L116's
step-321 complete-domain audit were checked with their hypotheses.
The precise Hall, shortening and Conrad inputs above were reused within
the ready source assessment; no new general theorem was imported.
L112 and L117 were inspected only for the stated overlap comparisons.

Reproduce this separate audit from the notebook:

    python3 scripts/seven-coordinate/audit_inactive_coordinate_partition.py

The full audit certificate is
`scripts/seven-coordinate/inactive-coordinate-partition-critical-audit.json`;
its complete independent-verifier output is
`scripts/seven-coordinate/inactive-coordinate-partition-critical-audit.log`.
The audit does not rerun or enlarge the producer's screen. It checks all
584 step-321 artifact hashes and all five recorded code hashes, binds
the saved screen to its master/audit/program hashes, reconstructs the
ordered 756/382/30/351 support domains, and compares every selected shard,
source shard and retained index. The complete ordered 599-record domain
over 56 thirds and the full screen manifest agree.

For every selected original 24-by-21 matrix, direct-product entries agree
with the derivative/ratio construction. The nonzero scaling is exactly
g(z)^2*g(x)*g(y); differentiating X^16-1 at the distinct nonzero H labels
justifies every derivative value. Original row elimination and column
elimination give the stated ranks, and the selected original rows attain
that rank. All 1,192 basis vectors have the identity free-coordinate
submatrix and all 28,608 residual entries zero. Thus these are complete
kernels, not merely collections of null vectors. The inspected reverse-row
Gauss–Jordan verifier was then executed on all records: it reconstructs
every complete basis, all 4,193 coordinate tests and every nonzero failure
witness, including every failed coordinate in passing records. It also
reconstructs the full indexed partition and all summary fields.

The audit confirms that every passing record omits exactly {22,27,33}.
It independently reconstructs the thirty disjoint-third comparison set
and checks that its nine exchanged-row occurrences all fail this screen.
It matches (0,279) to L117's exact four supports, rather than relying only
on the index label. Hence the full overlap table is correct: one L117
pass, 359 other passes, nine L112 failures, and 230 other failures. This
is only the stated indexed comparison, not an exhaustive historical
novelty assertion or a recursive third exclusion.

The extension-field implication needs no point sampling. Exact rank and
complete-basis certificates persist under scalar extension by minors.
For an actual nonzero decomposable tensor, any nonzero pivot p_ab has
a,b different from an omitted coordinate x. L109's reconstruction gives
both reconstructed x-coordinates zero, hence the entire actual plane lies
in that coordinate hyperplane. Both original coefficient vectors lie in
this same plane, even with a nonrational prescribed omitted direction.
Their syndromes are therefore represented on a six-set; L103 bounds the
entire original finite bad set by fifteen, with the unchanged actual
D/locators and inherited finite certificates. Equality supplies sixteen
events before this contradiction. A nonzero constant coordinate is never
classified as inactive. No plane is assigned to a nondecomposable vector.

The independent verifier exits successfully and every audit check passes.
All 587 recorded source/target artifacts, including both screen outputs,
are byte-identical before and after the audit; all called code is unchanged.
The shared Python, residue arithmetic and helper limitations remain, as
do the inherited L103 computational qualifications. No mathematical repair,
new exclusion, changed dependency or global bound follows from this audit.
This validates an existing restricted input, not progress beyond the
sources checked. It supersedes the pending-audit wording in the overview;
that overview and the DAG are unchanged because the argument is unchanged.
All 599 historical failures and all 239 screen failures remain preserved.

## Mathlib

Full matching coverage for this exact labeled finite partition is not
checked. Supporting full matching exterior/coding coverage is not newly
checked; Conrad's precise exterior tools and the coding inputs above
are imported through the assessed scope. Unknown availability is not
absence. No formal verification or mathematical originality is claimed.
