# Prescribed affine four-neighbor incidence test — ready continuation

TARGET: Test whether four distinct members of L035's prescribed affine neighborhood satisfy the full L031 incidence pattern, retaining all intercepts and valid coordinate reuse.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed comparison in 2026-10-08-affine-neighbor-four-pattern.md searched exact 191/56/10696 parameters, affine/transversal/Pasch configurations and doubly constant-weight terminology, and checked relevant local proofs/failures; no inspected matching finite test or local duplicate was found. No novelty inference follows.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/pdf/2304.09445v3 (AGL Definition 2.5/Lemma 2.7 and proof, printed pp. 7–8) and https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf (AVZ June 24, 2000 manuscript definition (5), Theorems 8/32/36, printed pp. 3/6/16/17); relevant AGL statement/proof and AVZ theorem statements rechecked 2026-10-08; exact applicability and local duplicate/failure comparison reused from 2026-10-08-affine-neighbor-four-pattern.md.
COMPARISON: Known signed equality matrices and affine intersection tools cover the methods, but neither they nor ordinary double-weight bounds or asymptotic high-girth existence settle this exact attached-head family. L032's cubic witness does not transfer; L035's pair/anchored audit is not a quadruple certificate.
GAP: Find and rigorously verify one full incidence witness, or give a complete exclusion argument for the prescribed family; actual-label realizability and any quantitative family cap are separate gaps.
REASON: One independently testable additional restriction can decide the viability of whole-pattern avoidance without reopening the stopped anchored graph. Only the exact finite specialization needs mathematical work; no new general design or RS theorem should be reproved.
SCOPE: L035's fixed lexicographic 56-slope assignment, evaluation set {0,1,2,3,4}, auxiliary F_191, attached three-subsets of an eight-point head and every intercept; abstract four-block incidence only. No slope/evaluation-set search, actual-label rank test or whole-family bound.

The separate literature-only approval step repaired the missing direct
source URLs on 2026-10-08. The exact target and EXPLORE scope are retained;
the next invocation defaults to its finite mathematical test, subject to
supervisor validation. No new lemma, witness, exclusion proof or
mathematical computation was produced by this repair. Detailed citations,
source hypotheses, search/access evidence and rejected theorem transfers are in
[the completed review](2026-10-08-affine-neighbor-four-pattern.md).

## Direct-source recovery check

Both primary PDFs above were retrieved successfully on 2026-10-08.
AGL Definition 2.5 uses a prime power q and a hypergraph on t vertices,
with signed Vandermonde rows and the last coefficient block omitted.
Lemma 2.7 assumes an agreement hypergraph of distinct RS codewords at
the given evaluations; its full proof uses their nonzero coefficient
difference vector. This is necessary rank evidence, not a converse or
an abstract incidence exclusion. The saved finite test does not import
a new rank specialization.

AVZ Theorem 36 (142) shortens a positive exact head weight with an integer
floor; Theorem 32 identifies the zero-head base with a constant-weight
maximum, and Theorem 8 (37) gives its disjoint-support value. Their
statements were rechecked; prior definition (5) coverage is reused.
These bound ordinary double-weight families and do not impose the six
pair intersections required here. L035 already contains their local
application, so no reproof is warranted.

Recovery reused the prior search log, inspected-source comparison and
local failure checks rather than repeating discovery. The optional
unread hash-design leads remain parked and are not essential premises.
This is a process repair, labeled STALLED; it supplies no new mathematical
evidence and leaves the exploration counter unchanged. Mathlib coverage
remains not checked.

The main gap is arbitrary-center 68-agreement safety in C001a's instance,
with 955<=t_star(m)<=957. The intermediate target is exactly the finite
incidence question above. A whole-pattern absence proof could retain
one necessary condition for a future L034 neighborhood analysis; a
witness would stop that sufficient avoidance approach in this family.
Neither promises the 184665717 whole-family cap or an unsafe RS list.

For a finite representation, use an abstract head A_0={0,...,7}, disjoint
from Omega=({0,...,4} times F_191) disjoint union {*}. Order its triples
lexicographically, assign slopes s_T=0,...,55 in that order, and use
B_(T,b)=T union {(x,s_T*x+b):x=0,...,4}, for every b in F_191.
This is the prescribed L035 model. The later proof must explain the
order-preserving head and outside-bijection correspondence to an actual
neighborhood; no actual-label rank invariance is assumed.

Test four distinct members B_1,...,B_4. Require each of the six complete
intersections U_ij=B_i intersect B_j to have size two, the six U_ij to
be mutually disjoint as **points**, all triple intersections to be empty,
and each private part B_i minus the union of the other three blocks to
have size two. Shared points can lie in the head or tail. Opposite edges
may reuse x with different y; do not require twelve distinct coordinates
or six distinct tail-coordinate groups. Do not discard repeated head
classes or intercept coincidences without a proved reason.

First seek one exact witness. Save all four (T,s_T,b) keys, all 32 block
entries, every full pair/triple intersection and all private parts in a
complete disk certificate, and check them directly. A witness stops
whole-pattern avoidance immediately; no actual subgroup rank calculation
is included in this step. If attempting exclusion instead, justify all
reductions and coverage of every permitted quadruple, slope repetition
and intercept. L035's pair-offset table alone cannot certify absence.
Any common-translation normalization needs its full quadruple justification
and orbit accounting. A bounded search miss is not an exclusion proof.

Continuation/abandonment test: a verified witness parks this family's
whole-pattern avoidance route. Rigorous complete absence permits only
the stated necessary-condition conclusion and a later separately assessed
continuation. Incomplete coverage is EXPLORATION, with the exact unchecked
cases saved for resumption. Keep the family fixed throughout this attempt.

Essential inputs are L035, L031 and L032; L029 supplies the affine method,
L034 the downstream distinction between incidence and labeled admissibility,
and C001a the actual target/threshold. Preserve ATTEMPTS/019–021,023–024.
Nonanchored L033, actual-label ranks, full admissibility, family conversion,
cross-core consistency, common-center RS realization, 67-agreement safety
and ABF equivalence remain unresolved. Auxiliary F_191 is not assumed
embedded in E or F. Matching Mathlib coverage: not checked. The optional
unread anti-Pasch/perfect-hash leads are not mathematical premises.
