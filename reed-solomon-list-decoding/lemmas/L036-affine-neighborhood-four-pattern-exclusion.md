# L036 — Fixed affine neighborhood excludes the four-block pattern

## Hypotheses

Let A_0={0,...,7} be disjoint from
Omega=({0,...,4} times F_191) disjoint union {*}. List the three-subsets
T of A_0 lexicographically and assign s_T=0,...,55 in that order.
Use the exact L035 family

\[
 B_{T,b}=T\cup\{(x,s_Tx+b):x=0,...,4\},\qquad b\in\mathbb F_{191}.
\]

All intercepts are included. The field and evaluation set, slope
assignment and head order are fixed; no alternative construction is
asserted. For its actual-neighborhood interpretation, use any L035 core
C, distinguished eight-set A and bijection sigma:Omega -> H minus (C
union A), with A ordered by its integer F_65537 residues.

## Conclusion

There are no four distinct members of this family whose six complete
pair intersections have size two and whose triple intersections are
empty. In particular the full L031 incidence pattern, which additionally
requires mutually disjoint pair intersections and four private pairs,
does not occur. The same absence holds in every L035 I_sigma.

Thus the L031 quadruple clause in L034 is vacuous within these prescribed
neighborhoods. This retains only that necessary condition. Nonanchored
L033 triples, full L034 admissibility, a whole-family cap, cross-core
consistency and common-center RS realization remain unproved. There is
no improvement to 955<=t_star(m)<=957 and no safety claim at 68 or 67
agreements. Auxiliary F_191 is not the actual evaluation field. This
finite exclusion has complete computational evidence below; the separate
critical review recorded below retains it without a mathematical correction.

## Proof

**Coverage and sources.** The preexisting EXPLORE assessment is
`drafts/literature/2026-10-08-affine-four-neighbor-incidence-test.md`.
It authorizes this exact finite incidence test or a complete exclusion,
not a changed slope assignment or RS-rank theorem. L035 supplies the
family and its affine intersection argument. L031 supplies the pattern
being tested; its labeled kernel theorem is not used to infer absence.
L032's different-family witness is a contrast, not an input.

The reused primary comparison inspected Alrabiah–Guruswami–Li,
*Randomly punctured Reed–Solomon codes achieve list-decoding capacity
over linear-sized fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
Definition 2.5 and Lemma 2.7 with proof, printed pp. 7–8, and
Agrell–Vardy–Zeger, *Upper Bounds for Constant-Weight Codes*, June 24,
2000 [manuscript](https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf),
definition (5), Theorems 8/32/36, printed pp. 3/6/16/17.
Neither gives this fixed-family exclusion: signed RS matrices test
labeled realizability, and ordinary shortening bounds omit this
incidence condition. No such theorem is reproved. The finite exhaustive
specialization below is therefore needed. POTENTIALLY_NEW means only
that the assessed sources did not establish coverage; it is no claim of
originality or progress beyond all literature.

**Complete head reduction.** Suppose a required quadruple existed.
Two members with the same head share its three points, contradicting
pair intersection size two. Its four heads and slopes are distinct.
For distinct slopes, equality of tail points requires
(s_i-s_j)x=b_j-b_i, so each tail intersection has at most one point.
Each of the six head intersections must consequently contain at least
one point. Empty triple intersections imply that every head point
belongs to at most two heads. There are twelve head memberships in
total. If a head point occurs twice it supplies exactly one pair-head
point and uses two memberships. Thus the sum of the six pair-head
intersection sizes is at most six, and it is also at least six.
Equality forces exactly one head point on each edge, six distinct
shared head points and no private head points. Each tail pair must now
have exactly one point.

The heads are precisely the three-edge stars of K4 with its six edges
bijectively assigned six of the eight head points. For each chosen
six-set there are 6!/4!=30 unordered configurations: two edge assignments
give the same collection of stars exactly when they differ by a vertex
permutation of K4, and these 24 permutations act freely on bijective
edge assignments. Hence there are binomial(8,6)*30=840 possibilities.
Sorting their four slopes gives a unique ordering of each quadruple.
The producer enumerates all binomial(56,4) head choices and retains
exactly the pair-size-one, empty-triple conditions. The independent
checker instead requires exactly six head points of multiplicity two,
and one common head point for every pair. Their complete ordered lists
agree and have length 840. These tests implement the proved reduction,
not an assumed generic property of heads.

**All intercepts and translations.** For each ordered head configuration,
the common vertical translation (x,y)->(x,y-b_1), fixing the head and
the spare point, sends the intercepts to (0,b_2-b_1,b_3-b_1,b_4-b_1).
It preserves this family and every intersection. This action has orbit
size 191, since translating the first intercept fixes it only at zero;
each orbit has exactly one normalized representative with b_1=0.

Let x_12,x_13,x_14 be the three crossings with line 1. They must belong
to {0,...,4}, since each tail intersection is nonempty. The equations
determine b_j=(s_1-s_j)x_1j modulo 191 uniquely for j=2,3,4. All slope
differences are nonzero. Thus the 5^3 choices cover every potentially
valid normalized intercept quadruple, including equal intercepts.
If two of these coordinates agree, their shared value on line 1 is a
triple tail point, contrary to the required empty triple intersections.
The producer can therefore use the 5*4*3=60 distinct-coordinate choices.
The independent checker retains all 125 choices before rejection.
Both retain opposite-edge coordinate reuse; only incident coincidences
force a triple point. Sorting slopes and normalizing intercepts loses
no unordered quadruple.

**Complete finite certificate.** Run

```text
python3 scripts/finite-support/affine_four_incidence.py
python3 scripts/finite-support/audit_affine_four_incidence.py
```

The producer writes `scripts/finite-support/affine-four-incidence-results.json`.
It stores all 840 head configurations and every one of the 50400 reduced
candidate rows, including intercepts, all six field crossings and both
acceptance predicates. For each edge it computes the unique crossing

\[
 x_{ij}=(b_j-b_i)(s_i-s_j)^{-1}\pmod {191}.
\]

Acceptance requires all crossings in {0,...,4} and three distinct
incident crossing coordinates at each line. The latter is equivalent
to empty tail triple intersections when all six pairs exist. None of
the 50400 rows is accepted; this is complete enumeration, not a bounded
miss. No other allowed head or intercept case remains unchecked.

The independent checker imports no producer code. It reads the complete
certificate and reconstructs every head configuration with the different
multiplicity test above. For each of the 840*125=105000 coordinate choices
it explicitly constructs all four five-point tail sets, directly
intersects each of the six pairs and each of the four triples, and saves
their sizes and the full keys. For every one of the 50400 distinct-first-
coordinate rows it also tries all 191 field coordinates for each edge
to reconstruct its unique crossing, rather than using the producer's
modular inverse. All 50400 complete producer rows and every parameter
and reduction field match exactly.

The audit writes `scripts/finite-support/affine-four-incidence-audit-results.json`,
including the producer SHA-256 and all 105000 direct-intersection rows.
Exactly 4220 rows have all six tail intersections of size one; every
one has a nonempty tail triple intersection. The number satisfying both
all six pairs and empty triples is exactly zero. All five producer
checks and ten audit checks pass, with empty failure arrays. The entire
relevant evidence is traversed by the checker, rather than sampled;
full aggregate counts, all check values and failures were inspected.
The scripts use only exact integers, finite sets and prime-field
arithmetic. The complete reductions plus this exhaustive finite
verification prove the asserted absence.

**Actual neighborhoods and qualifications.** Map each a in the sorted
actual A to its index in A_0, and map each outside point through sigma's
inverse. These maps together give a bijection of the disjoint head and
outside sets taking I_sigma to the abstract family, with precisely the
same lexicographic slopes. A bijection preserves pair and triple
intersections and private parts, so any actual incidence witness would
give an abstract one. This proves absence for every C,A,sigma without
claiming that such bijections preserve actual-field polynomial ranks.
With no incidence quadruple present, no L031 matrix needs testing in
this family. This does not prove its other labeled restrictions.

**Separate critical audit, 2026-10-08.** The assessment
`drafts/literature/2026-10-08-affine-four-exclusion-audit-coverage.md`
was already SPECIALIZE at invocation start and matches this audit exactly.
This is REPRODUCTION verification of the fixed exclusion, with no source
refresh, new construction, new rank theorem or originality claim. The
sources above remain supporting frameworks rather than a matching theorem.
L035's family and intersection proof and L031's full incidence hypotheses
were checked directly; L032's different-family witness is a trap check,
not an imported premise. No direct mathematical input or DAG edge changes.

The head reduction uses the sum of all six pair-head sizes, not a bound
on a single overlap. Empty triples make each head membership multiplicity
at most two, so twelve memberships support at most six pair-head points.
The six required pair intersections each need at least one such point.
Equality consumes all memberships in exactly six multiplicity-two points,
one per edge. In the K4 representation, every vertex is recovered from its
star, and every edge from the intersection of its endpoint stars. Thus
two edge assignments produce the same unordered stars exactly through a
vertex permutation; fixing all distinct edge labels forces that permutation
to be the identity. This verifies the free 24-fold quotient, not merely the
numerical count. It excludes equal heads before ordering the slopes.

Translation by any t adds t to each intercept, fixes the head and spare
point, and permutes the full family because every intercept is allowed.
Its stabilizer on an ordered quadruple is trivial by its first intercept;
there is exactly one b1=0 representative. Distinct slopes make every
crossing equation have one field solution, so the three crossings with
line 1 recover all other intercepts. No assumption that the intercepts
are distinct is made. Two equal incident crossing coordinates give the
same full point on the common line and therefore a forbidden triple.
Opposite edges at the same coordinate can have different values and are
not discarded. Conversely, any triple tail point forces equal incident
crossings. These facts justify both the 125-case coverage and the reduced
60-case producer. No sampled actual labeling or generic-rank inference is
used in transport: a bijection of the disjoint head/outside ground sets
preserves complete intersections, with the actual head order fixing the
lexicographic slope assignment. Auxiliary field operations need not be
preserved by that bijection.

Run the additional, separate verifier

```text
python3 scripts/finite-support/critical_audit_affine_four.py
```

It reads both original certificates without overwriting them and imports
neither original program. For every six-subset of the eight-point head
it assigns its six points to K4 edges in all 6! ways, recovers the four
stars and sorts their slope keys. It obtains exactly 840 configurations,
each with 24 assignments, and matches both saved head lists in full.
For all 840*125 normalized coordinate choices it constructs the complete
eight-point blocks, tagging head and tail by disjoint integer ranges.
It intersects those full blocks for all six pairs and four triples.
The head pair size is exactly one and head triples are empty, as separately
verified for every generated configuration, so subtracting one from the
complete pair sizes recovers exactly the saved tail sizes. Every one of
the 105000 stored audit records, including its key and intercepts, matches
this reconstruction. For all 50400 distinct-first-coordinate rows, the
verifier tries all 191 field coordinates on each edge and checks its
unique solution, then matches every producer crossing and predicate.
All parameter and reduction fields, the five producer check values,
the ten saved audit check values, both failure arrays, the null witness
and the audit's producer SHA-256 are checked against the reconstructed
data. The verification does not rely on saved pass flags.

The full new certificate is
`scripts/finite-support/affine-four-critical-audit-results.json`, with
both input hashes, all 840 head summaries, counts, 858 check values and
complete failure arrays. It records 105000 candidates, 50400 reduced
rows, 52300 candidates with some equal intercepts, and 54600 with repeated
first crossing coordinates. The last two counts are overlapping diagnostics,
not disjoint classes. All six tail pairs occur in 4220 cases and empty
triples in none of those cases. All 858 checks pass; both general and
row-failure arrays are empty. The producer hash is
`29133472e2e84b55a188a8f5298c3627b5c33502ad9faf2e1c40ffaaafc8c8e1`
and the original audit hash is
`4ae3306be11b2f56b554cdc2380d2e8a2d3fa31be126e177e27a7bd819c5a35d`.
Complete row comparisons traverse the load-bearing evidence, rather than
treating previews or agreement of aggregate counts as verification.

Finally, empty triple intersections also prevent intersections between
two different pair-point sets: incident pairs would give a triple point,
and opposite pairs a quadruple point, hence a triple point. Each size-eight
block with three disjoint size-two incident overlaps would have exactly
two private points. Thus a full L031 witness certainly meets the audited
absence condition. This is an applicability check of the existing conclusion,
not an additional restriction on other incidence patterns. The audit retains
the theorem but leaves nonanchored L033, quadruples involving a separately
adjoined distinguished block, full admissibility, the L034 family cap,
cross-core consistency, common-center realization and 67/68-agreement safety
unresolved. Matching and supporting Mathlib coverage remain not checked.

## Mathlib

Matching coverage for this exact finite exclusion: not checked. Coverage
of supporting finite-set counting and prime-field operations: not
checked. No Mathlib theorem is imported or absence claim made.
