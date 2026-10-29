# Selected-family configuration-budget transfer — source comparison closed

TARGET: Assess a direct selected-family counting transfer from L124's determinant-zero configuration budget to the 1532495 local cap, including overlap-triple supersaturation and completion multiplicity.
CHECKED: 2026-10-25
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the 2026-10-05/06 transfer exclusions; searched sparse/linear/expanded-triangle supersaturation and packing terminology; a targeted duplicate search located the stronger audited L030 obstruction and ATTEMPTS/021, omitted from the proposed continuation.
SOURCE_EVIDENCE: Read L030's construction, all 105 canonical residues, all-core relabeling argument, exact-cap conclusion and critical-audit section, with history/066; inspected Bailey–Burgess arXiv:1107.4120v1 p.2, Balogh–Narayanan–Skokan author manuscript Theorem 3.1 p.6 and initial cleaning, and Balogh–Garcia–Methuku arXiv:2609.38772v1 Theorem 1.3 and Lemma 5.1.
COMPARISON: L030 supplies actual 2571353-block families on every core avoiding the entire counted overlap pattern, irrespective of determinant labels; this is stronger than L028's relaxed obstruction and already rules out the proposed 1532495 local cap under the reviewed assumptions. L124's ambient budget does not remove this known counterexample.
GAP: The proposed single-core transfer is closed negatively by an existing result; additional restrictions on actual RS families or compatibility across cores are essential. No counterexample to an RS list bound is supplied.
REASON: Import the existing local obstruction instead of approving a duplicate impossible cap; propose a distinct two-core full-law compatibility review, without deriving or approving that changed mathematics here.
SCOPE: The reviewed class is every 7-uniform family on H minus a 61-core with pair intersections at most two and no L020 nonsingular triple. L030 refutes the desired universal cap in exactly this class; the source review proves no new supersaturation or multiplicity result.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and the new ambient-budget transfer lacked essential coverage; duplicate checking uncovered an already audited exact-family obstruction, so no further dependent calculation is justified.

## Completed comparison and decisive duplicate

The main gap remains arbitrary-center 67/68-agreement safety. The
intermediate target was a uniform local cap of 1532495, with L027's
core-incidence transfer as its downstream use. Its continuation test was
a justified lower count of selected-family overlap triples exceeding the
determinant-zero budget, after controlling completion multiplicity.
Its abandonment test is now met by the existing L030 construction.

The canonical result is `lemmas/L030-all-core-shared-moment-extension.md`,
Proof, **The packing avoids the entire hyperedge incidence pattern**,
the following all-core bijection argument, and **Independent critical
audit, 2026-10-07**; acceptance is recorded in history/066. L030 fixes
the seven evaluation points {16,64,70,102,112,118,121} in F_137 and the
quadratic graph packing on their product with F_137, together with four
unused ground points. Its already proved conclusions are exactly:
2571353 blocks; pair intersections at most two; no distinct block triple
with empty triple intersection and all pair intersections of size two;
and preservation of these properties under every bijection to the
963-point complement of every actual core. The proof uses the complete
105-matching determinant table over the auxiliary field, not an
assumption about the actual subgroup's determinants. Its later independent
audit regenerates the table and checks the stated scope. No audit program
was rerun in this source review, and no new verification is claimed.

Thus the putative supersaturation conclusion fails even before asking
which counted patterns have determinant zero. This is an application of
the already explicit exact-local-cap obstruction in L030, not a new
counterexample or a new mathematical derivation. The narrower threshold
1532496 cannot rescue a universal prohibition: the proposed class and
pattern avoidance are inherited on deleting blocks. This elementary
specialization merely checks the imported obstruction's applicability.
It supplies no center, global 68-support packing or unsafe RS list.
Completion multiplicity need not be settled to reject this cap route.
The actual local independence maximum is not identified.

ATTEMPTS/021 already states that the obstruction covers exact local
independence numbers, rather than only higher moment relaxations.
ATTEMPTS/019 alone was an insufficient failure check for this proposal.
This historical stop is not a ban on cross-core or additional RS
constraints; it is a direct counterexample under the present assumptions.
The new ambient count changes no hypothesis of that obstruction.

## Additional primary comparisons actually inspected

József Balogh, Bhargav Narayanan and Jozef Skokan,
[*The number of hypergraphs without linear cycles*](https://sites.math.rutgers.edu/~narayanan/pdf/linear_cycles.pdf),
author manuscript dated 11 July 2017, Theorem 3.1, printed p.6
(published J. Combin. Theory B 134 (2019), 309–321): for r,k>=3 and
an n-vertex r-graph with t n^(r-1) edges, t>=2k(r-1), there is a
k-uniform collection of linear k-cycles with average degree at least
K^(-1)t^(k-2)D^(k-1) and maximum j-codegree at most
K t^(k-j-1)D^(k-j), 1<=j<=k-1; K depends on r,k,
D=t^2 n^(r-4) for r>=4 and D=t for r=3.
The initial proof cleaning deletes low positive pair/triple codegrees;
it is not a theorem about arbitrary sparse packings. For the original
7-uniform universe, the threshold is 12k n^6, outside the proposed
963-point, 1532496-block instance. Also its linear triangle has
one-point intersections, rather than the required two-point pattern.
No incidence lift or quantitative specialization is imported.
The theorem and initial cleaning were read; the remaining proof was
unnecessary for these hypothesis rejections and was not audited.

József Balogh, Ramon I. Garcia and Abhishek Methuku,
[*Counting hypergraphs without linear cycles of fixed length*](https://arxiv.org/html/2609.38772v1),
v1, 30 September 2026, Theorem 1.3 gives the asymptotic enumeration
formula 2^((1+o(1)) ex_r(n,C_k^(r))) for fixed r,k>=3.
This counts cycle-free hosts, not labeled selected-family configurations
at a finite threshold. Lemma 5.1 assumes 0<epsilon<1, odd k>=5,
a chosen C_2, n>n_0(epsilon,k,C_2), a (2,C_2)-sparse 3-graph,
and at least (epsilon/4) binomial(n,2) edges. It supplies a cycle
collection with size at least D^(k-1)n^2/K and j-codegrees at most
D^(k-j), with D=n^((k-2)/(k-1)), K=log n.
Its k>=5 restriction already excludes the needed triangle. No proof
application or numerical cutoff is inferred. Lemma 5.2 and its
fullness/switching discussion were also viewed as a lead, but its
parameter hierarchy was not fully extracted: it is not imported or
treated as coverage. No unread result is needed to use L030.

Robert F. Bailey and Andrea C. Burgess,
[*Generalized packing designs*](https://arxiv.org/pdf/1107.4120v1),
20 July 2011, Section 1.1 and Proposition 1.1.4, printed p.2:
for positive v>=k>=t and lambda, the packing number is bounded by
the displayed Johnson–Schönheim nested floors. The ordinary definition
requires each t-subset to occur at most lambda times. This is supporting
packing terminology and a cardinality upper bound, not an overlap-triple
lower count or a completion theorem. The November author-hosted URL
timed out; the readable v1 and saved November assessment suffice here.
No source blocker remains essential, and no version identity is assumed.

Reuse, without rebrowsing, the inspected Karamanlis–Dodos delta-interval
failure and Castro-Silva et al. theta-body coverage recorded in
`2026-10-06-core-conditioned-determinant-transfer.md`, as well as the
whole-triangle mismatch in `2026-10-05-triple-restriction-extremal-transfer.md`.
They do not strengthen or weaken the exact L030 obstruction.

Queries included `hypergraph supersaturation triangle pairwise intersections
size two triple intersection empty 3 packing 7 uniform`, `supersaturation
expanded triangle uniform hypergraph finite quantitative`, `supersaturation
linear hypergraphs triangles`, `generalized triangle 2-intersection
hypergraph`, and the exact Balogh–Narayanan–Skokan and Bailey–Burgess titles.
Odd-cycle, trace-hypergraph and even-cycle hits were discovery leads only;
no theorem is inferred from their snippets. Failed search is not novelty.

## Decision and changed continuation

Outcome NEGATIVE records a materially changed route decision from
reusing an existing audited theorem; it is no new extremal discovery.
No new lemma, mathematical program, certificate or DAG edge is written.
The overview now retains the stronger exact-family obstruction and
corrects its stale L121-pending wording using history/464 and L121's
canonical accepted audit. L121 is not reopened. Mathlib coverage for
the proposed transfer is not checked; L030 retains its own qualifications.

A different target is proposed in
`2026-10-25-two-core-full-law-compatibility.md`: assess coupling two
entire local laws with one common support packing. The earlier
`2026-10-07-global-pair-marginal-extension.md` only assessed an augmented
pair-moment matrix and does not cover these full-law constraints.
Narrow searches for two/adjacent/overlapping cores found no matching
completed assessment; broader duplicate coverage remains a next-review
obligation. The changed target is REVIEW_REQUIRED. No coupling,
incompatibility or safety claim is derived or approved here.

## Initial proposed scope, retained as superseded history

The main gap is arbitrary-center 67/68 agreement safety. A potentially
useful intermediate target is a direct finite counting obstruction to
a family of 1532496 seven-subsets on H minus K avoiding all of L020's
nonsingular overlap patterns, uniformly in the 61-point core K.
L027 already records why a local integer cap of 1532495 would suffice
for its 68-agreement transfer. A source review must preserve its exact
threshold and hypotheses rather than presume a solution at 67 agreements.

For a family F, the proposed count concerns ordered triples (A1,A2,A3)
with empty triple intersection and each pair intersection of size two.
Their ordered overlap pairs are (A1 intersect A2, A2 intersect A3,
A3 intersect A1). L020's zero determinant is the collinearity predicate
counted in L123/L124. Different triples of seven-subsets may have the
same overlap pairs; the three private points in each block are not part
of the configuration budget. This completion multiplicity is an essential
missing input, not a factor to suppress. No count, multiplicity bound,
or comparison is derived here.

The test for a later approved mathematical step must compare a justified
lower count of selected-family overlap triples with a justified upper
count of the determinant-zero ones, at the exact local size threshold.
Continue only if primary coverage or a documented uncovered finite target
provides a concrete test of that comparison. Reject a proposed source
application if it needs the unavailable large-parameter range, excludes
allowed antipodal triples, treats all cores as equivalent, or replaces
selected-family counts by ambient density without controlling completion
multiplicity. If the numerical comparison cannot give the needed saving,
record that obstruction and park this particular transfer mechanism.

## Reuse and preserved stops

The saved assessment
`2026-10-06-core-conditioned-determinant-transfer.md` rejected direct
application of Karamanlis–Dodos at n=963, k=7, ell=2 because its mandatory
delta interval is unavailable; its conclusion also counts pairs rather
than the required labeled triples. Repeating that application is not a
new test. Its recursive-theta coverage led to L027, and L028 subsequently
provided an above-threshold shared feasible lift. The current proposal
is a direct actual-family counting comparison using the new ambient
budget, not another optimization of that unchanged feasible set.

Essential mathematical inputs are L020's labeled support criterion,
L027's exact local threshold/transfer, L028's preserved relaxation
obstruction, and the accepted L123/L124 finite configuration data.
ATTEMPTS/010 retains determinant-zero antipodal configurations;
ATTEMPTS/019 retains the failed theta cap. The 2026-10-06 transfer source
comparison remains reusable negative evidence. No cross-notebook input
or unfinished L121/root result is assumed.

Still unresolved: selected-family supersaturation, completion multiplicity,
a sufficient local count comparison, possible sharp core bounds, RS list
realization, 67-agreement safety and qualified ABF equivalence. The bracket
remains 955–957. Full matching and supporting Mathlib coverage for the
proposed transfer are not checked. This file approves no mathematics;
the next turn performs source comparison only.
