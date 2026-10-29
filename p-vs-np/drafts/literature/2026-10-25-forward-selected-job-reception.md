# Forward reception of the fixed restricted job — source review

TARGET: Test forward free, zero-placeholder and substituted evaluation of the unchanged restricted job-7 commutator against complete L035 references under the original caps.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 494 searched noncommutative ABP path-polynomial dynamic programming and Raz–Shpilka ABP definitions; read the primary manuscript and the existing independent Forward evaluator, L108 §11, L097 §22, Attempt 044 and the step-492 comparison. No completed fixed-job forward test was found in these scoped sources; no novelty claim.
SOURCE_EVIDENCE: Raz–Shpilka author-hosted 16-page manuscript, Definition 1 p.4, Lemma 2 Steps 1–2 p.5 and §2.2/Theorem 4 pp.7–9; L035 (2)/(4), L036 (5)–(9), L108 §11; audit_parameterized.py Forward lines 123–214 and verify_restricted_copies.py occurrence/reference block lines 235–306.
COMPARISON: Ordered path semantics and a separately audited forward full-word implementation already exist. Their smaller-fixture success supplies no job-7 cap bound; layered homogeneous PIT does not supply the required complete raw references. The changed finite interface needs applicability and accounting checks, not a new ABP theorem.
GAP: Job-7 all-mode equality, independent complete occurrence/reference reception, cumulative retained-table/evidence charging and fixed-cap feasibility remain unperformed. No forward saving or accepting receipt is established.
REASON: Coverage suffices for one separate REPRODUCTION attempt on the identical fixed component; retain all original bounds and stop on any equality, occurrence, evidence or arithmetic-cap failure. No integration or backward retry is approved.

LITERATURE_REASON: The next target changes the evaluator and receiving obligations after a terminal backward-table cap failure; prior pruning coverage does not approve this change.

Main gap: uniform worst-case P versus NP. Nearer gap: complete nonzero-fJ
reception on the fixed opposing-units endpoint. This proposed target tests a
single independently identifiable failing component, rather than retrying a
whole extraction or backward evaluation. Its possible downstream use is a
separately received isolated Boolean witness if a changed receiving mechanism
passes all original bounds. No such feasibility is claimed.

Essential inputs: L035 (2)/(4), L036 (5)–(9), L097 §§16–22, L108 §§2,13;
output-493/restricted-boolean.json jobs[7] (a sum commutator, 81,464 records),
its original whole-operand and internal-copy maps, output-491's matching job
inventory, and output-489 row 78 / events 2642–2643. The exact failed-process
counters and missing references are recorded in output-493/reception.failure.json
and stop-summary.json. The failure receipt does not identify its failing mode;
the proposed test therefore includes all three modes.

The separate review should find primary coverage for forward ordered path
evaluation on arbitrary-root affine DAGs over the free F₂ algebra, compare
existing local evaluators and failures, and decide whether a finite test with
the existing complete L035 reference contract is justified. It must retain
the same source graph, dictionary, central multiplicities, separate copies,
all record/evidence/word/length/pair limits and cumulative retained-table
storage accounting. Do not reinterpret that cap as uncharged temporary or
live storage, release table entries to change the measure, merge copies,
substitute a zeroness-only criterion, or weaken production acceptance.

Any later attempt must compare complete references in all three modes and
independently receive every job-7 occurrence. Continuation requires all
original bounds and equalities to pass; any cap or equality failure stops
that exact evaluator. Forward storage, polynomial expansion and raw-reference
evidence feasibility are separate unresolved questions; an apparently smaller
table alone would not suffice. This review may reject or narrow the proposal
based on an essential already-known obstruction. No calculation is approved.

Full Boolean reception, all later jobs, K/H, nonzero-fJ, the independent
whole-run evidence stop, trusted paths/SHA, total interpreter resources,
general availability, L087 W₂ and unrestricted ER/Frege/SAT remain unresolved.
Attempts 037–044 remain preserved. No cross-notebook theorem is proposed.
Full matching Mathlib coverage is not checked.

## Completed review — step 494, 2026-10-25

The pending-review paragraphs above preserve the original proposal. This
section supplies its source assessment without executing it. The target text
and fixed graph are unchanged. Reuse the audited main-target statement in
foundations/01-model-and-target.md; this step selects no new P-versus-NP route.

### Primary source comparison

Ran Raz and Amir Shpilka, [*Deterministic Polynomial Identity Testing in Non
Commutative Models*, author-hosted 16-page manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
retrieved 2026-10-25, revision date unestablished: Definition 1, printed p.4,
specifies layered homogeneous linear-edge ABPs and ordered path products.
Lemma 2, p.5, assumes a size-s formula with zero free term. Step 1 permits
nonlayered graphs and constant edges; Step 2 describes intermediate vertices
as computing homogeneous components. These passages support vertexwise
path-polynomial computation, but do not give this finite arbitrary-root
interface or its storage bound. Section 2.2, pp.7–9, culminating in Theorem 4,
gives polynomial-time identity testing for the defined ABPs through
zeroness-preserving reductions, rather than complete raw word evidence.
Its proof cases inspect degree-two prefixes, linear dependencies and new
source labels. Neither those transformations nor Lemma 2's homogeneous
conversion preserve the prescribed graph/occurrence contract. F₂ is allowed;
no field-size assumption is imported. This is source coverage for standard
semantics, not an application of the PIT complexity bound to word expansion.

Queries: `noncommutative algebraic branching program path polynomial dynamic
programming topological order` and `Raz Shpilka deterministic polynomial
identity testing non commutative models algebraic branching program definition`.
Other results included Forbes–Shpilka black-box PIT and Raz–Shpilka follow-up
papers; their theorems were not inspected and are not inputs. The existing
step-492 comparison of LTW v4 Lemma 3.7 remains adequate for the unchanged
commutator construction; no extra formula-witness derivation is warranted.
Failed search coverage does not establish novelty.

### Existing implementation and exact difference

L108 §11 already records a separate forward full-polynomial audit: integer
letters with disjoint original/placeholder ranges, integer coefficient
accumulation followed by parity, all three evaluation modes, and topological
right multiplication. Its six smaller inputs passed 364 full comparisons.
The inspected implementation is `scripts/four-rule-extraction/audit_parameterized.py`,
class `Forward`, lines 123–214. It imports neither backward arithmetic nor
correction code. Thus writing another general evaluation theorem or claiming
a new forward algorithm would duplicate established local work.

`Forward.graph` initializes the designated entry with the empty word and
processes every vertex by indegree, with edge labels appended on the right.
Its interface accepts an arbitrary entry and returns a table, rather than
assuming the exit is last. Source/root validity and complete label/dictionary
validation must still come from the strict input interface. Its documented
path invariant is in L108 §11. Applying that invariant to the unchanged job
requires explicit checking of nonextremal roots, coincident endpoints, empty
paths, no-path components, constants, parallel edges, cancellation and both
placeholder maps; no new proof of these cases is supplied in this review.
The L035/L036 hypotheses allow all these cases. A research specialization
must explain them even if some are absent from this particular graph.

The old forward audit measures table size within a traversal. It subtracts
the old destination polynomial before replacing that same slot; that is
replacement accounting, not permission to discard completed vertex entries.
It neither releases processed entries nor establishes a bound for a caller
retaining multiple mode tables, operand tables, terms and references. Reusing
its scalar maximum alone would fail this target's cumulative accounting.
The later implementation must charge every simultaneously retained table and
reference, including the prior completed-mode results and complete marked
terms; retain the original cumulative retained-table measure. Temporary
integer counters must also retain polynomial-word and length guards.
Do not relabel storage as only the sink polynomial or maximum single table.

In `verify_restricted_copies.py`, the inspected job loop independently checks
all four cuts, every map/edge occurrence, connectors, central multiplicities
and exhausted partitions before forming L035 (4). Its complete operand
prefix/suffix reference and every marked term precede changed-W evaluation.
L097 §22 reports that job 7 passed that structural portion before failure,
but no full job-7 reference file survived. A new isolated receiver must
recheck the unchanged structure and regenerate the independent complete
reference once; it cannot treat the stopped execution or a hash as acceptance.
Regenerating the necessary reference for this changed forward test is covered;
rerunning the failed backward W traversal is not. All-pair products keep
F-prefix, G-prefix, central label, G-suffix, F-suffix in that order, with every
central occurrence retained even when terms cancel. Use the unchanged typed
dictionary and literal original operand copies as the reference inputs.

Attempt 044 stops backward traversal only. Attempts 041–043 and the reused
step-492 review concern record counts, whole-run evidence or other copying
mechanisms; none establishes a forward-table cap bound on this fixed job.
Their negative evidence remains valid. This is a materially different,
independently testable receiving mechanism, with no claimed saving in advance.

### Approved finite test and stopping condition

Only the exact TARGET above is approved, as REPRODUCTION under SPECIALIZE.
Essential inputs: L035 (2)/(4), L036 (5)–(9), L097 §§16–22, L108 §§2,11,13;
output-493 restricted-boolean.json jobs[7], reception.failure.json and
stop-summary.json; output-491 inventory and output-489 row 78/events 2642–2643.
Read complete relevant fields before calculation. Preserve all archives.

Receive every job-7 copy, map, central occurrence, connector and partition
independently; evaluate the identical graph forward in free, zero-placeholder
and substituted modes; compare each complete output with its full independent
L035 reference. Also retain the substituted ordered-operand commutator check
and pre-cancellation one-placeholder occurrence condition. All references,
marked terms and necessary raw evidence must be written completely and counted,
not replaced by hashes, samples or identity-test verdicts. Keep cumulative
multiplication work across this isolated reception; do not reset it per mode.

Required limits remain records/label entries 2,000,000; evidence per file and
in aggregate 200,000,000 bytes; polynomial words 1,000,000; word length 256;
multiplication pairs 100,000,000; retained table words 20,000,000, plus every
other CAPS input/framing limit. Report actual/required values and retain any
failed receipt. No feasibility estimate or mathematical calculation is made
here. Any equality, structural or bound failure stops this exact forward
mechanism. Continue only after complete all-mode and occurrence reception
passes every original cap; even success supports only a later reviewed step.

Jobs 8–244, complete Boolean reception, full K/H and nonzero-fJ, whole-run
evidence, trusted paths/SHA, total resources, general certificate availability,
L087 W₂ and unrestricted ER/Frege/SAT remain independent gaps. Mathlib full
matching coverage is not checked. No lemma, DAG, proof overview or mathematical
script changes; no new theorem or progress beyond the checked sources is claimed.

Outcome: EXPLORATION. The review identifies reusable forward coverage and its
missing caller accounting, making one separate fixed-job test actionable.
