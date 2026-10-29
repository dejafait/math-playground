# L167 twelve-row exterior rank — bounded calculation coverage

TARGET: Compute and independently verify the stacked L109 exterior rank for L167's complete twelve-row E_2, retaining its full kernel if rank is below 21.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-family source/duplicate/failure comparison in 2026-10-27-l167-actual-row-realization-review.md, including the scoped fixed numerical-row search and /020,/028,/041–043,/048,/055 comparisons; no completed matching stack calculation was located.
SOURCE_EVIDENCE: L109 supplies the exterior blocks and rank-21 obstruction; audited L167 supplies supports. Hall Theorem 5.1.1 pp. 63–64 https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf and Conrad Theorems 4.2/7.1/7.5 pp. 11–12,23–25 https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf were reopened on 2026-10-27. Reuse inspected shortening section 5 pp. 7–8 https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf and fixed-instance comparison https://arxiv.org/pdf/1209.2887v1 through the completed assessment; shortening retrieval failed this turn.
COMPARISON: This is a finite specialization of an existing necessary linear condition, not an attempt to prove all linear families full rank or to repeat L079's full sixteen-event affine-family exclusion. No cited source or inspected local record supplies this precise twelve-row stack's rank/kernel certificate.
GAP: Determine and independently certify the rank and, if deficient, complete kernel of the original stack. A deficient kernel leaves decomposability, exact rank-one feasibility and all coding gates unresolved.
REASON: Unchanged coding/exterior coverage suffices for this bounded REPRODUCTION calculation; only a new finite certificate is needed. This separate literature recovery repairs direct-source URLs without executing mathematics or expanding the previously proposed scope.
SCOPE: Exactly L167 rows 2,3,4,5,7,8,9,11,12,13,15,16 and L109 product-defined actual maps at the original S/J over F_97, interpreted over extensions; no relabeling sweep, nonlinear solver, parameter sampling or realization construction.

## Gap, input domain and downstream relevance

The central local gap is uniform twelve-row exclusion for represented
t=0 equality pencils; arbitrary representation and challenge identification
remain independent gaps. This intermediate test checks one fixed family
that defeats marked incidence extraction. Its possible downstream use is
a concrete coding-sensitive obstruction on those twelve rows. L079
already excludes the whole sixteen-row affine equality family; a positive
rank result here would strengthen the selected-row relaxation only, not
improve the global 11/q–16/q interval or discover a new general theorem.

Essential direct inputs are L109 and audited L167. L104/L086/L010 and
their existing computational qualifications are inherited for the coding
application, not newly established. Keep F=F_(97^20), dimension eight,
unit multipliers, H the order-sixteen subgroup of F_97^*, the pinned
cell 1/4<=delta<5/16, both coefficient syndromes in U_S, sixteen original
finite events, t=0, and D and every locator nonzero as polynomials.
Weights and the original chart are arbitrary over F. S and J remain
exactly the ordered lists in L167 and L109. For the necessary geometric
test use arbitrary extension-field two-planes, never just F_97 points.

Known distance, shortening and exterior algebra are imported through
L109 with the precise source applicability recorded in the completed
comparison. Do not reprove them or add L159–L161 as premises. The
auxiliary characteristic-two affine coordinates encode incidence only.
No cross-notebook input, moment-preserving transport or recovered weight
is assumed. Full matching and supporting Mathlib coverage are not checked.

## One bounded attempt and complete evidence contract

Transcribe every selected row's I and K from canonical L167 and verify
exact row-set equality, completeness and the fixed label partition.
Construct each Q and six-row exterior block by L109 (1), choosing the
least label of S minus I as pivot and keeping the increasing S-pair
column order. Preserve all blocks and the complete stack on disk.

Compute its exact rank over F_97. If full, save the selected twenty-one
row indices, all corresponding support/covector-pair identities, the
entire square minor and a nonzero determinant residue. Independently
reconstruct all g values and quotient covectors from polynomial/Horner
evaluation or normalized quotients, rather than import the producer's
block builder; compare every matrix entry and verify the chosen minor
by a separate exact determinant path. Existing fixed-four-row artifacts
are controls or interfaces, not evidence for these twelve rows.

If rank is below 21, save a full nullspace basis and enough exact
elimination data to check its dimension, independence and annihilation.
The verifier must establish completeness, not only check selected vectors.
No preferred coordinate point can replace the whole kernel. The final
report prints actual rank, required rank 21, failures and certificate
paths; retain full evidence on disk and use bounded JSON inspection.

Interpretation is solely L109's existing necessary-condition argument
and invariance of rank under field extension. Full rank excludes a common
nonzero decomposable wedge, hence simultaneous rank-one restrictions for
these rows. A lower rank is inconclusive for that question. Plucker,
exact-rank-one, full-weight, lambda, prescribed-chart, remaining-event
and t=0 gates are not thereby passed, and are outside this calculation.

Continue only on a verified full-rank certificate or a complete retained
deficient kernel that supports a separately assessed concrete next test.
Any mismatch in transcription, quotient normalization or certificate
completeness prevents a mathematical conclusion and must be preserved.
Stop after this fixed stack; no extra label sampling or nonlinear solver
is preapproved. Historical rank-only failures remain valid. No rank,
kernel disposition, coding realization or new theorem is asserted by
this source assessment.

## Direct-source recovery, 2026-10-27

The supervisor reported missing direct source URLs in this ready assessment.
The links above repair that process issue; they do not establish a new result.
The target, duplicate/failure comparison and evidence contract are unchanged.

Hall's linked chapter, printed pp. 63–64, was reopened: Theorem 5.1.1
uses distinct evaluation points, nonzero multipliers and 0<=k<=n;
its distance assertion requires k>0. The existing n=16,k=8 application
in L104/L109 retains those conditions. No new shortening argument is made.

Conrad's undated 47-page PDF was reopened. Theorem 4.2 and its proof
(printed pp. 11–12) concern free modules and ordered wedge bases.
Theorem 7.1 and its proof (p. 23), followed by the explicit all-fields
qualification (p. 24), justify using nonzero wedges in characteristic 97.
Theorem 7.5 and its proof (p. 25) require two independent k-element sets
in a nonzero vector space, with 1<=k<=dim(V). These are supporting inputs,
not a theorem deciding this fixed stack. L109 remains the local reduction;
no reproof or new specialization was performed.

The shortening manuscript URL returned a browser access error. Its exact
section/formula and inspected applicability remain available in the reused
`2026-10-27-l167-actual-row-realization-review.md`, so this failed refresh
does not create missing essential coverage for the unchanged target.
Rosenthal–Trautmann is likewise reused, not newly read this turn.
Mathlib coverage remains not checked. No new theorem search is needed to
repair a URL omission, and no novelty claim follows from this repair.
