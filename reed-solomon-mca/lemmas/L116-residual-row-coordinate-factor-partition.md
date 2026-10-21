# L116 — Complete residual row/coordinate-factor partition

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, dimension eight,
L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. The actual Hankel determinant D and every coordinate
locator are nonzero polynomials. Both coefficient syndromes lie in
U_S for S={1,8,12,18,22,27,33}. Assume sixteen original finite bad
parameters and L104's t=0. Retain all inherited L010/L103/L104 and
L086/L109 finite-certificate qualifications. Weights and the prescribed
original chart are arbitrary over F.

Fix actual supports A1={1,8,47,50}, A2={12,18,64,70}. Use exactly
L114's ordered third list T, fourth universe U, eligibility definition,
and historical 24,866 residual occurrences over its 230 residual thirds.
An occurrence has zero-based indices (n,u) in T times U; equal kernels
in different occurrences remain separate. Use L109's original exterior
blocks and increasing S-pair columns. No universal occurrence of this
pair or seven-set is assumed.

## Conclusion

The entire historical list has the following sufficient-filter partition:

| Disposition | Indexed occurrences |
| --- | ---: |
| Whole kernel lies in E_c wedge F^S for an overlap label c of a selected row; that row fails the necessary full-weight gates | 24,267 |
| Not excluded by any of the eight tested row/label choices | 599 |

The first number includes L115's already excluded (n,u)=(0,249).
Thus there are 24,266 additional indexed factor certificates relative
to the L114 list after singling out L115, not a claim that every one
was previously unexcluded by all other results; see overlap bookkeeping
below. Exactly 174 additional thirds have every historical residual
fourth excluded. Together with L114's prior dispositions, those thirds
cannot occur with A1,A2 under the hypotheses.

The 56 remaining third indices are

    0–19, 35, 38, 51, 60, 65, 69, 79–98, 115, 145, 149,
    178, 191, 218, 278, 295, 300, 314.

Their 599 complete kernels remain unresolved by this filter. A residual
is not a feasible pencil or an equality witness. This is a restricted
finite-computation input with same-step independent replay; the separate
step-321 critical audit below found no defect. The global interval stays
11/q–16/q.

## Proof

### Imported inputs and applicability

Use L109's necessary direction and L086's equality linearity, with
exactly the hypotheses above. The actual lift coefficients u,v are
independent, and their nonzero wedge belongs to every selected stack.
L109 supplies at least twelve distinct actual two-overlap supports;
its rank-one projection and full-weight gates are necessary. Its
four-row converse is neither stated nor used here. L114 supplies the
complete historical domain and its existing nonresidual exclusions;
its separate step-317 critical audit is retained.

Standard coding inputs are imported through L109/L104: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, printed pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the shortening formula following Lemma 5.3.
The sixteen evaluation labels are distinct and all multipliers are
nonzero. Each row shortens exactly seven labels J minus K, reducing
dimension eight to one through positive dimensions and multiplying
retained multipliers by nonzero label differences. Changing the row
or its chosen overlap label does not change these hypotheses.
No standard distance or shortening theorem is reproved.

The invocation-start EXPLORE assessment is
`drafts/literature/2026-10-18-residual-row-coordinate-factors-review.md`.
This is REPRODUCTION of the assessed factor/gate mechanism exemplified
by L113 and L115, with new finite-domain certificates. Neither a new
general factor theorem nor progress beyond the checked sources is
claimed. ATTEMPTS/041–042 remain valid; rank-only and label-1-only
exclusion remain insufficient.

### Exact historical coverage and complete kernels

Reproduce from this notebook:

    python3 scripts/seven-coordinate/residual_coordinate_factors.py
    python3 scripts/seven-coordinate/verify_residual_coordinate_factors.py

The master certificate is
`scripts/seven-coordinate/residual-coordinate-factors.json`, its complete
per-third shards are in `scripts/seven-coordinate/residual-coordinate-factors/`,
and the complete replay is
`scripts/seven-coordinate/residual-coordinate-factors-replay.json`.
The master records the source-master SHA-256; each shard records its
historical source path/hash, exact historical index list, dispositions,
complete bases and remaining indices. Both programs reconstruct T and U
from their definitions, match all 351 historical source shards/hashes
and all 756 ordered fourth labels in each, and select exactly the cases
whose historical status is unresolved. They compare this list with
every source residual-index list and master summary. The resulting
domain has exactly 24,866 occurrences and 230 thirds. None is deduplicated.

For every occurrence the producer rebuilds the original 24-by-21 stack
using direct products for g_j. Exact modular row elimination computes
rank. The independent replay rebuilds every block by

    g_K(x)=16*x^15/product_(y in (S union K) minus {x})(x-y)

on S union K, then normalized ratio covectors and the exact row-scaling
back to L109's blocks. The formula follows by differentiating
X^16-1=g_K(X)*product_(y in S union K)(X-y) at a simple root x.
All denominators are nonzero, and 97 does not divide 16. Exact column
elimination independently verifies every rank and the producer's
independent original-row list. The complete rank histogram is

    {18:6840, 19:593, 20:17433}.

All 39,139 saved basis vectors have 24 original-stack residuals checked:
939,336 zero scalar entries. For each rank r the basis has 21-r vectors
and its free-coordinate matrix is the identity. Thus the vectors are
independent and span the complete kernel, rather than just furnishing
some kernel points. The replay checks every coefficient and residual.
Exact ranks over F_97, and these complete bases, persist under every
scalar extension: rank is characterized by base-field minors.

For each occurrence test all eight choices (j,c), where j is one of
its four rows and c is one of the two labels in I_j. For every basis
vector retain every coefficient in a pair not containing c. All those
coefficients vanish if and only if the entire kernel is contained in
E_c wedge F_97^S. This is a linear whole-basis identity, not a union
of favorable subspaces or a sample of projective points. The replay
checks all 198,928 tests, including their nonzero coefficients when
containment fails. There are 88,518 passing row/label tests over 24,267
occurrences. Choosing the first passing test in the prescribed order
gives the following certificate histogram:

    row 1, c=8: 19036; row 2, c=12: 2620; row 2, c=18: 2611.

The L115 regression has passing tests (row 2,12), (row 3,12), (row 4,12)
and is counted just once as an occurrence. Every nonpassing occurrence
retains its whole basis and every failed sufficient-factor test.

### Entire extension-field locus and selected-row gates

Fix a passing (j,c), and take any nonzero kernel tensor p over an
extension K of F_97. Complete containment gives p=E_c wedge w, with
w_c=0, by taking w_x=p_cx in antisymmetric coordinates. Nonzero p
makes w nonzero and independent of E_c. Thus p is decomposable and
its plane is L=span(E_c,w), including every extension point and every
projective chart.

Because c is in I_j, every covector of Q_j vanishes on E_c. Hence
Q_j restricted to L has rank zero or one. In rank zero, L109's
nonpersistence argument applies to the actual lift: both coefficient
syndromes would have representatives on A_j and its locators would be
identically zero. This branch is explicitly rejected, including
deficient recovered weights. In rank one the kernel in L is the line
K*E_c. Every nonzero possible recovery therefore has h=a E_c, a!=0.
With z_j=min(S minus I_j), z_j!=c and g_j(z_j)!=0, so L109 gives

    lambda=h_zj/g_j(z_j)=0,
    e_i=h_i-lambda*g_j(i)=0 for the other i in I_j,
    e_k=-lambda*g_j(k)=0 for both k in K_j.

These violate the nonzero-lambda and full-weight gates. Equality has
already supplied full errors before this test, so the one-coordinate
recovery cannot be accepted as an actual A_j error.

Each passing test saves a separate exact gate certificate: z_j and its
nonzero g value, all four entries of Q_j E_c, h=E_c, lambda, the full
four-coordinate recovered error including its zeros, and all eight
original shifted-moment residuals. The replay independently rebuilds
each certificate using derivative values. These are the coefficients
of the identities for arbitrary h=a E_c: projection, recovered errors
and moments are linear in a. Verifying their coefficients at a=1 is
an exact identity check, not sampling possible planes. The unique-line
argument above covers every rank-one plane; rank zero is handled
separately. All 88,518 certificates pass, with their zero weights kept.

For the prescribed original basis u_original,v_original, a recovered
direction h=alpha*u_original+beta*v_original is finite only if
alpha!=0. Its actual error is the projective error divided by alpha.
When alpha=0 it is omitted; when alpha!=0 every failed zero weight
above stays zero. Neither basis coefficients nor the omitted point are
assumed rational, and no replacement original chart is chosen. Thus
the intrinsic gate failure excludes the whole kernel over F and every
extension independently of the finite-direction gate.

### Third exclusions, duplicates and limitations

The 174 new excluded third indices are exactly L114's historical 230
residual indices minus the 56 indices displayed in the conclusion;
both full lists occur in the master and are independently replayed.
If one such third were actual, the at-least-twelve-row conclusion of
L109 supplies a further actual fourth distinct from the first three.
L086 makes it eligible. Either L114 already excludes that indexed
fourth or it is in the historical residual list and is excluded by the
whole-kernel/gate certificate above. This contradiction proves precisely
those 174 triple exclusions. A third with even one remaining occurrence
is not excluded by this assembly. No recursive use of new third
exclusions to remove additional fourths is performed.

Indexed filter counts are distinct from previously unknown mathematical
loci: a fourth may itself be an already excluded third with the same
first pair. The certificate records its historical class (a disjoint
L112 third, the named L113 third, an L114-excluded third, or an L114
residual third). This is overlap bookkeeping only; neither producer
nor replay uses those classes to add exclusions. In particular the
24,266 additional indexed certificates are not all asserted novel
relative to every reordered older result. L115 is explicitly marked
as a known regression. The 174 newly excluded thirds were outside all
those previous third lists.

The complete overlap histogram has 211 excluded and nine retained
occurrences whose fourth is a disjoint L112 third; the other 24,056
excluded and 590 retained occurrences have a fourth in L114's historical
residual-third list. There are no named-L113 or old-L114-excluded fourths
in this historical residual domain. Thus the nine retained occurrences
are already impossible by L112 after exchanging the selected third and
fourth, but remain deliberately recorded as failures of this sufficient
factor test. No extra third exclusion is inferred from this bookkeeping.

The complete replay reports no failures. Both paths still share Python,
residue arithmetic and earlier audited low-level utilities; this is
explicit computational dependence, not proof-assistant verification or
a separate critical audit. The 599 retained kernels have not been
solved for general Plucker loci or simultaneous gates. They assert no
actual recovery, t=0 converse or sixteen-event completion. Arbitrary
seven-sets, universal representation or seed extraction, the uniform
fifteen bound and challenge-definition qualifications remain unresolved.

### Separate critical audit, 2026-10-18

Step `2026-10-18-mca-321-residual-coordinate-partition-critical-audit`
used the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-10-18-residual-coordinate-partition-audit-review.md`.
The complete proof, both named programs and every called mathematical
helper were inspected. L109's independence, necessary exterior equations,
rank-zero rejection and full-weight/original-chart gates, L086's equality
scope, and L114's audited exact domain and complete-basis provenance were
checked. L113/L115 supply comparisons for the intrinsic argument; L112
is used only to interpret overlaps with its already excluded third list,
not to establish any new factor disposition or any of the 174 exclusions.
The ready Hall/shortening coverage is reused with its precise hypotheses
and inherited computational qualifications. No new source theorem or
enlarged mathematical solver is introduced.

Run the separate audit from this notebook:

    python3 scripts/seven-coordinate/audit_residual_coordinate_partition.py

Full evidence is
`scripts/seven-coordinate/residual-coordinate-partition-critical-audit.json`;
the complete verifier output is
`scripts/seven-coordinate/residual-coordinate-partition-critical-audit.log`.
The audit binds the L114 source to its successful step-317 audit by
checking all 353 recorded artifact hashes, including every historical
shard, and both used mathematical-helper hashes. It independently
reconstructs the 382 eligible thirds, the thirty disjoint removals and
the named removal, and checks the exact ordered 351-third list.

For every one of the 756 supports, all six original exterior rows agree
entrywise with the derivative/ratio construction: 4,536 block rows,
each with all 21 coefficients compared. Algebraically
`c_x=g(z)g(x)*(w_x/g(x)-w_z/g(z))`, so the exterior scaling is the
nonzero `g(z)^2*g(x)*g(y)`. Differentiating the product at a simple
H root gives exactly the derivative values used by the verifier,
including values at K for the recovered error. Thus equality of ranks
alone is not the bridge to the original matrix.

The inspected column-elimination helper maintains zero entries at all
previous pivots in each new pivot vector. Its selected columns are
independent and span every processed column. It therefore proves each
saved rank exactly; the saved original-row submatrix independently has
that rank. For rank r, the 21-r null vectors have an identity on their
free coordinates and vanish on every original row. Rank-nullity then
proves completeness. The full replay verifies all 24,866 occurrences,
39,139 vectors and 939,336 residual entries, with the stated rank
histogram. Exact base-field minors justify persistence of both rank
and this basis after scalar extension.

Every one of the 198,928 row/label tests is reconstructed, including
all off-factor coefficients in failures. All 88,518 passing gate
certificates, the first-passing-factor histogram and every retained
index agree with the saved evidence. For a passing factor, the proof
above covers the entire locus: p=E_c wedge w is nonzero and defines
the plane containing E_c; rank zero is excluded by actual polynomial
nonpersistence, and rank one has unique intersection line K E_c.
The recovered error has only its c-coordinate nonzero. Checking the
linear identities at h=E_c checks their coefficients for every scalar
multiple, not sampled points of the plane locus. The other overlap and
both outside weights remain zero in every finite original chart;
an omitted direction is ineligible. All eight shifted moments are
rechecked. No unexamined projective pivot or extension-field branch
is discarded by this intrinsic argument.

The audit expands the written 56 residual-third indices and compares
their complement in the historical 230 to the exact 174 new indices.
It additionally records, for each of those 174 thirds, every eligible
fourth and its exclusion reason: frozen L114 rank/factor disposition
or the corresponding new L116 factor certificate. Actual eligibility
is independently recomputed from all three pair intersections.
At least twelve distinct actual rows, supplied by L109, guarantee a
further fourth; L086 makes it one of these eligible cases. Its nonzero
lift wedge is contradicted in every case. This establishes the universal
fourth implication separately for every claimed third, without using
any new third exclusion recursively or using a four-row converse.

The complete overlap histogram is also reproduced: 211 excluded and
nine retained L112-disjoint fourths, and 24,056 excluded and 590 retained
historical-residual fourths. The known L115 occurrence has precisely
the three listed passing tests. All nine older L112 exclusions remain
recorded as failures of this filter, and no additional third is removed
on their account. Thus indexed new certificates are not misreported as
previously unknown loci.

The full verifier exits successfully and there are no audit failures.
All 584 recorded manifest, shard and replay files are byte-identical
before and after this audit. Both implementations still share Python,
residue arithmetic and the stated audited helper infrastructure; no
proof-assistant verification is claimed. No mathematical defect, repair,
new exclusion or changed dependency was found. This canonical audit
supersedes the pending-audit wording above and in the overview, which
is left unchanged because the argument has not changed. The 599 filter
residuals over 56 thirds remain preserved; arbitrary t=0 coverage,
universal representation/extraction and challenge qualifications remain
unresolved. This is validation of an existing restricted input, not
progress beyond the checked literature or a global count improvement.

## Mathlib

Full matching coverage for this exact finite labeled partition is not
checked. Supporting coding/exterior-rank coverage is not newly checked;
the precise coding inputs above and audited L109 are imported with their
qualifications. Unknown coverage is not absence. No formal verification
or mathematical originality is claimed.
