# L114 — Remaining-third rank and label-1 factor partition

## Hypotheses

Use F=F_(97^20), the order-sixteen subgroup H of F_97^*, dimension
eight, L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. Assume the actual Hankel determinant D and every
coordinate locator are nonzero polynomials, both coefficient syndromes
belong to U_S for S={1,8,12,18,22,27,33}, and there are sixteen original
finite bad parameters with L104's t=0. Weights and the prescribed
original finite chart are arbitrary over F. Retain the inherited
L010/L103/L104 and L086/L109 finite-certificate qualifications.

Fix actual two-overlap supports A1={1,8,47,50}, A2={12,18,64,70}.
Put J=H minus S, and order the universe
U=binom(S,2) times binom(J,2) lexicographically, with increasing pairs.
A support is I union K for (I,K) in U. Define T as the ordered sublist
whose supports meet A1 and A2 in at most one label, after removing all
supports disjoint from A1 union A2 and the support {1,22,75,79}.
Use exactly L109's exterior block and increasing S-pair column order.
No universal occurrence of the fixed pair or seven-set is assumed.

## Conclusion

There are 351 elements of T. For each, all 756 indexed fourth supports
are covered, giving 265,356 cases. A fourth is eligible when it is
distinct from the first three supports and meets each in at most one
label. The complete eligible-case partition is

| Disposition | Indexed occurrences |
| --- | ---: |
| Rank 21 | 50,042 |
| Deficient, entire kernel contained in E_1 wedge F_97^S | 18,942 |
| Deficient and not so contained; unresolved by this filter | 24,866 |

The first two dispositions exclude that fourth over every extension
of F_97. Exactly 121 thirds have every eligible fourth excluded and
therefore cannot occur with A1,A2 under the hypotheses. In the zero-based
ordering of T these thirds have indices in the following inclusive
intervals:

    20–34, 36–37, 39–50, 52–59, 61–64, 66–68, 70–78,
    279–293, 296–299, 301–313, 315–350.

The other 230 thirds retain at least one unresolved fourth. All their
24,866 residual kernels, and every incidence-ineligible deficient kernel,
are preserved completely. No feasibility, decomposability, gate success,
rational descent, sixteen-event witness or exclusion of those 230 thirds
is asserted. This is a restricted finite-computation result; same-step
independent replay passes; the separate step-317 critical audit below
found no defect.
The seven-coordinate fifteen bound and global 11/q–16/q interval remain
unresolved.

## Proof

### Imported inputs and exact domain

Apply L109's necessary support filter and L086's pairwise linearity
only to actual equality errors. The field, code, event, nonpersistence,
sixteen finite parameters and original chart are exactly those above.
L109 gives independent lift coefficients u,v and 12–14 distinct actual
two-overlap rows. Their nonzero wedge lies in every selected row stack.
Only that necessary direction is used, never the r>=6 converse on four
rows. L113 supplies its intrinsic label-1 factor gate obstruction.

Standard coding inputs are imported through L109/L104: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following GRS shortening formula.
Distinct nonzero labels, unit multipliers and dimension eight are
unchanged. Shortening the seven labels J minus K leaves dimension one
and nonzero retained multipliers. Row intersections do not change these
hypotheses. No general coding theorem is reproved.

The ready EXPLORE assessment at invocation start was
`drafts/literature/2026-10-18-remaining-third-coordinate-factor-filter-review.md`.
This is REPRODUCTION of the assessed finite rank/factor mechanism,
without a claim of originality or progress beyond checked sources.
L111/L112 and L113's named-third exclusion describe the removed domain;
their finite certificates are not used to infer ranks of new cases.
ATTEMPTS/041's rank-only failure remains valid.

The universe has 21*36=756 elements. Explicit set comparison finds 382
thirds pairwise linear with A1,A2. Exactly thirty are disjoint from their
union: I lies in binom({22,27,33},2), and K lies in
binom({75,79,85,89,96},2). The named removed third is eligible but is not
one of those thirty. The three lists are pairwise disjoint and their
union is the complete 382-element list, leaving 351 ordered thirds.
For each third the saved fourth list equals U in order, without duplicates.
No support relabeling or H symmetry is used.

### Exact matrix and complete-basis evidence

Reproduce with

    python3 scripts/seven-coordinate/remaining_third_factor_filter.py
    python3 scripts/seven-coordinate/verify_remaining_third_factor_filter.py

The complete master certificate is
`scripts/seven-coordinate/remaining-third-factor-filter.json`.
For each third n it records the SHA-256 and path of the complete shard
`scripts/seven-coordinate/remaining-third-factor-filter/third-nnn.json`.
Every shard preserves all 756 dispositions, minor witnesses, pivot
columns, complete deficient bases and all original-stack residuals.
The independent replay is
`scripts/seven-coordinate/remaining-third-factor-filter-replay.json`.
These are full certificates, not selected-point samples or previews.

The producer constructs L109's blocks using direct products g_K.
It independently rebuilds all 756 blocks using the differentiated
identity X^16-1=g_K(X) product_(y in S union K)(X-y):

    g_K(x)=16*x^15/product_(y in (S union K) minus {x})(x-y).

Every denominator and numerator is nonzero because labels are distinct
and nonzero and 97 does not divide 16. Scaled ratio-covector exterior
blocks agree entrywise with the direct blocks. Incremental row and
independent column elimination agree on all 265,356 stack ranks.
At each full-rank case, 21 selected original rows give a minor with
nonzero exact residue modulo 97. The replay reconstructs every such
minor independently and evaluates its determinant by column operations,
as opposed to the producer's row operations. No numerical rank is used.

At each deficient case, polynomial/Horner ratio blocks and Gauss–Jordan
elimination give 21-rank basis vectors. Their pivot columns agree with
the independent rank computation; their free-coordinate matrix is the
identity, and all residuals against the original four-block stack are
zero. This proves membership, independence and completeness. The replay
independently checks these properties against derivative-built blocks,
including all incidence-ineligible cases. The total rank histogram is

    {16:1520, 17:4047, 18:62864, 19:13385, 20:88461, 21:95079}.

Thus all 95,079 full-rank minor witnesses and all 170,277 deficient
kernels are retained. Those kernels have 327,611 basis vectors. Every
basis vector has all 24 original residuals checked: 7,862,664 scalar
residuals in total. Rank and complete bases remain valid under every
scalar extension, since ranks are determined by base-field minors.

Eligibility is recomputed directly from the three intersection sizes;
repeated rows are explicitly rejected. The eligible rank histogram is

    {18:9096, 19:593, 20:34119, 21:50042}.

For each complete deficient basis, test every coordinate pair not
containing label 1. All these entries vanish for exactly 18,942 of the
43,808 eligible deficient cases. This is precisely complete containment
in E_1 wedge F_97^S, and it proves the same containment after extension.
If any tested entry is nonzero the entire case remains unresolved;
individual factor points or other coordinate factors are not tested.
The replay independently reconstructs every status, every per-third
summary and the exact excluded/residual index lists, with empty failure
lists and all shard hashes matched. Both paths share Python, residue
arithmetic and previously audited routines; this is computational
dependence, not proof-assistant verification or a separate critical audit.

### Gate transfer, triple exclusions and residuals

Rank 21 contradicts L109's nonzero lift wedge. For a deficient kernel
contained in E_1 wedge F^S, reuse L113's proved factor obstruction.
Every nonzero tensor has a plane containing E_1. Since 1 lies in I1,
Q_1 annihilates E_1. A rank-zero restriction contradicts actual
nonpersistence by L109. Otherwise its unique recovery line is F*E_1,
whose lambda and overlap weight at 8 are zero. This fails intrinsic
full-weight gates in every prescribed original chart. Thus the whole
extension-field kernel is excluded, with rank-zero and infinity retained.

For any selected actual third at equality, L109 supplies a distinct
actual fourth because there are at least twelve rows. L086 makes it
eligible. For exactly the 121 recorded third indices, every eligible
fourth is excluded by one of the two tests. That contradiction proves
the claimed restricted triple exclusions. For each other third, at least
one eligible case remains, so this argument supplies no triple exclusion.

For the first residual, T index 0 and U index 249 give
A3={1,12,75,79}, A4={8,12,85,89}. Their four-row stack has rank 18.
Its complete kernel basis, in increasing S-pair order, is

    (0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,73,63,62,1,0,0,0,0,0,0).

The free columns are 1,6,14 (zero-based), and all 72 original
residuals vanish. This basis fails complete label-1 containment.
No further Plucker, projection, full-weight or original-chart test has
been applied to it in this step. It is an unresolved locus for this
filter, not an asserted admissible plane. Remaining-event balance,
universal representation and challenge qualifications are also open.

### Separate critical audit, 2026-10-18

Step 2026-10-18-mca-317-remaining-third-partition-critical-audit used the
unchanged ready EXPLORE assessment
`drafts/literature/2026-10-18-remaining-third-partition-audit-review.md`.
This is RESEARCH / REPRODUCTION: validation of the existing restricted
input, not a new exclusion or a novelty claim. The complete proof,
producer, verifier and every called mathematical helper were inspected.
The necessary L109 formulas and gates, L086's equality scope and L113's
entire-factor argument and audit were checked. Their previously audited
inputs and finite-certificate qualifications are retained, not independently
reproved here. The unchanged primary Hall and shortening coverage in the
assessment suffices; no further source theorem is imported.

**Matrix identity and arithmetic.** The direct-product covectors are
exactly (1) of L109. If d_x(w)=w_x/g(x)-w_z/g(z), then
c_x=g(z)g(x)d_x. Thus each exterior ratio row is multiplied by the
nonzero factor g(z)^2*g(x)*g(y). The derivative formula above recovers
the same g values from the simple roots of X^16-1. The audit compares
all 4,536 rows (756 complete blocks) entrywise through the direct,
derivative and polynomial/Horner constructions, including every scaling
factor. No block identity is inferred just from agreeing ranks.

The verifier's full-rank branch recomputes the determinant of each saved
21-by-21 original-row minor by column operations, checks its nonzero
residue, unique valid row indices and all 21 pivot columns. This proves
rank 21 directly for all 95,079 cases. For each of the 170,277 deficient
cases, independent column elimination proves the rank and pivot profile.
Exactly 21-rank vectors with a free-coordinate identity matrix are
linearly independent; their 24 original residuals vanish, so rank-nullity
makes them a complete basis. All 327,611 vectors and 7,862,664 scalar
residuals are checked, including incidence-ineligible cases. The column
elimination retains earlier pivot zeros in each new pivot vector; its
chosen columns are therefore independent and span every processed column.
The determinant elimination uses invertible column additions/swaps and
tracks pivots and swap signs. Both operate exactly modulo 97.

**Domain and dispositions.** The verifier independently reconstructs H,
S, J, all 756 supports, all 382 eligible thirds, the thirty removed
thirds and the distinct named removal. It compares each ordered third
and every ordered fourth list, the exact indexed shard paths, hashes,
intersection counts and repeated-support rejections. The supplement
also compares the removed thirty with the explicit product of the pair
sets displayed above. Hence all 351*756=265,356 cases are covered with
no omitted or duplicated index. Every saved rank histogram, per-third
summary, residual index list and complete master summary agrees with
reconstruction. The written inclusive intervals expand to exactly the
121 excluded indices, with precisely the complementary 230 indices left.

For each deficient basis the verifier tests every entry on every pair
not containing label 1. It reconstructs the containment bit and status
rather than trusting them. This validates all 18,942 eligible factor
exclusions and preserves all 24,866 residual occurrences. The factor
identity for a complete basis extends to the entire kernel after scalar
extension: nonzero base-field minors preserve rank and the same independent
basis has the full extended dimension. No finite-point test or descent
of the original chart or weights is used.

**Universal-fourth implication and gate scope.** At equality L109 supplies
at least twelve distinct actual rows, so a fourth different from any
selected three exists. Audited L086 makes that actual fourth eligible.
Its nonzero lift wedge must lie in the corresponding four-row kernel.
Rank 21 forbids it. In a label-1 factor kernel every nonzero tensor is
E_1 wedge w with an independent w, so its plane contains E_1. Because
1 lies in I1, Q_1 E_1=0. Projection rank zero contradicts the actual
nonpersistent locators by L109. At rank one the only recovery line is
F*E_1, with lambda=h_12/g_1(12)=0 and h_8-lambda*g_1(8)=0. All denominators
are nonzero. Rescaling, an arbitrary extension or a prescribed original
chart cannot turn these intrinsic zero weights into a full error; the
original infinite direction is already inadmissible. L113's special
third plays no role in this intrinsic argument. Thus all eligible fourths
are impossible for each of the 121 stated thirds. This does not use a
four-row converse, infer actual feasibility from a residual kernel, or
require any exclusion theorem for the thirty removed thirds.

Run the complete audit with

    python3 scripts/seven-coordinate/audit_remaining_third_partition.py

Its full evidence is
`scripts/seven-coordinate/remaining-third-partition-critical-audit.json`,
with the complete replay output in
`scripts/seven-coordinate/remaining-third-partition-critical-audit.log`.
The audit invokes the inspected verifier on all original certificates,
records before/after hashes of the manifest, replay and all 351 shards,
and records the six used script hashes. All 4,546 checks pass; the full
replay exits zero and all 353 certificate files remain byte-identical.
Every claimed count above is compared with the reconstructed output;
there are no failures. The producer need not be rerun to validate its
saved evidence: every original case and witness is checked. Both paths
still share Python, exact residue arithmetic and some previously audited
helper infrastructure. This is not proof-assistant verification.

No mathematical defect, repair or changed dependency was found. The
original argument and DAG are unchanged. This canonical audit supersedes
pending-L114-audit wording in the overview without changing its argument.
L115 remains a separate one-occurrence exclusion and is not an input to
this partition. The historical residual list is preserved; it is unresolved
by this filter, not a claim that every occurrence remains unclassified by
all later work. ATTEMPTS/041–042, arbitrary t=0 profiles, universal
representation and challenge qualifications remain open as stated.

## Mathlib

Full matching coverage for this labeled finite partition is not checked.
Supporting coding sources and L109's exact exterior reconstruction are
reused as stated. No Mathlib absence, formal verification or mathematical
novelty is claimed.
