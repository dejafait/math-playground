# L129 boundary obstruction — completed audit-scope comparison

TARGET: Critically audit L129's s=18632 retained-size bound, including observed-column recovery, the one-label correction, approximate-base-line completion and the transferred nonstar matching.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready discovery and primary-theorem comparison in 2026-10-26-boundary-retained-star-obstruction.md and the inspected stability proof record in 2026-10-25-near-complete-common-star-rigidity.md; narrowly read canonical L129, L126 with its accepted audit, L030 hypotheses/conclusion, ATTEMPTS/105 and histories 491/501. No fresh broad search or mathematical verification.
SOURCE_EVIDENCE: Ben-Or–Coppersmith–Luby–Rubinfeld, Random Structures & Algorithms 32(1) (2008), 49–70, DOI 10.1002/rsa.20182, author preprint https://people.csail.mit.edu/ronitt/papers/convd.pdf, Theorem 1 p. 3 and proof pp. 3–6, reused from inspected assessments; L126's canonical structural/bijection paragraphs and accepted separate audit supply the local matching input through audited L125. No new external retrieval is claimed.
COMPARISON: L129 changes L127's strict-overlap recovery by recovering observed columns, correcting at most one unseen label, allowing at most one exception on each base line, and preserving five matched labels after undoing the correction.
GAP: Source coverage is ready for the separate audit; correctness of universal recovery, completion, independent-uniform reduction and auxiliary matching transfer remains unverified. No source directly imports the boundary bound.
REASON: The separate comparison finds the exact audit within the previously assessed boundary family and techniques, requiring verification of local specializations rather than another external theorem; it approves a later audit and supplies no verdict on L129.
SCOPE: Exactly TARGET under L129's stated hypotheses; acceptance, correction or rejection of this candidate and necessary input/arithmetic checks only. No lower overlap, unequal indicators, other left column, arbitrary laws, global extension or RS realization.
LITERATURE_REASON: The invocation-start audit target was REVIEW_REQUIRED; perform the mandated separate scope comparison using adequate existing coverage, without repeating external discovery.

## Approved separate audit scope

The exact target concerns canonical L129 under its original hypotheses:
q=137, unchanged T, H,K,a,b, arbitrary ambient bijections, left
distinguished column 16, equal retained common-star indicators of size
18632, and upper intersection 63 for every pair of distinct retained
supports. It does not assume equality of the original ambient stars.

Essential local inputs are L030 and audited L126, with L125 through
L126. L127 and L128 are comparisons, not necessary proof inputs to
L129. The external theorem is cited precisely in L129; reuse its
existing primary-source assessment unless a specific hypothesis gap
is found. No new general stability theorem is requested.

The critical proof obligations are the large-independent-set count,
exclusion of all column outsiders, recovery with a disappearing label,
extension by an actual-label transposition, existence of valid base
lines with at most one exception each, transport of at most 3q failures
to independent uniform additive inputs, exact completion by permutation
bijectivity, and applicability and transfer of L126's full matching.
Check that the transposition moves at most one of the six matched labels
and preserves the a/b nonstar distinction. Check both star contributions
and every displayed numerical bound. A preview of any certificate would
not establish these universal implications; no new certificate is used.

Acceptance must leave the main challenge IN_PROGRESS and preserve all
scope limits. A failed implication should be repaired within the approved
scope if possible, or recorded explicitly without converting a route
failure into a counterexample. Mathlib full/supporting coverage remains
not checked. This completed literature-only review approves a separate research audit; no audit mathematics is performed in this turn.


## Reused sources, duplicates and exact applicability obligations

The primary stability theorem has already been inspected in the undated
18-page author preprint: Theorem 1 on p. 3, with the majority-map
construction, Lemmas 1–6, identity/inverse/product cases and three
disjoint error events on pp. 3–6. It assumes a single full-domain map
between finite groups and two independent uniform inputs. For failure
probability delta<2/9 it provides a homomorphism at disagreement fraction
at most (3-sqrt(9-24 delta))/12. This is the imported theorem, not a new
stability claim. L129's passage from partial three-function equations
to that setting, its claimed error budget and its upgrade to exactness
are local audit obligations; coverage does not certify them. Preserve
the zero-error qualification. No reproof of the general theorem is needed.

The boundary discovery assessment already compares trade/intersection
and exact RS automorphism results at precise primary locations. None
there supplies the candidate boundary retained-size bound. Its optional
unread near-automorphism and blocked affine-design leads remain unused
and nonessential. This review reuses that bounded comparison and does
not claim a comprehensive search or novelty. No changed external
hypothesis or new general theorem request warrants fresh browsing.

L126's accepted audit specifically separates ambient-star rigidity and
the explicit polynomial bijection from full retention and the packing
inequality. Its structural proof is the input to compare with L129's
auxiliary labeling, rather than invoking L126's final retained-size
conclusion outside its hypotheses. The later audit must verify that
separation and its application, including the inherited complete 840-map
input, before transferring any edges. No general matching theorem is
needed for counting explicit disjoint conflicts, and no auxiliary
packing assumption is licensed. L030 supplies the fixed construction;
its moment and local feasibility results do not certify cross-core packing.

The ready boundary assessment distinguishes L127's strict threshold
18633 and L128's transfer from L129's 18632 boundary. Those results are
comparisons, not proofs at the new threshold. ATTEMPTS/105 excludes a
full-star-preserving repair only; the historical stop does not ban this
boundary audit. History/501 records a candidate, not an independent
verification. No duplicate acceptance of L129 was found in the scoped
local records. No cross-notebook input is used.

## Relevance and continuation test

The main gap remains arbitrary-center 67/68 safety and bracket 955–957.
The intermediate target is a critical verdict on L129's restricted
boundary bound. A valid bound could strengthen the two-core obstruction
for later compatibility work; independent lower-overlap, unequal-indicator,
arbitrary-law, global-extension and RS-realization gaps remain.

Continue with acceptance only after all universal implications, exact
input hypotheses and numerical comparisons pass. On a failure, preserve
it and repair within the same stated target if possible, or reject the
candidate implication explicitly. If repair needs a stronger overlap,
new label restrictions or a new theorem beyond this assessment, stop
and request separate scope coverage; do not silently change the target.
Failure of this proof is neither a counterexample to its bound nor a
disproof of the RS challenge. A complete-looking result remains an
UNVERIFIED CANDIDATE until the later critical audit is completed.

Outcome: EXPLORATION, an actionable scope approval using existing source
coverage, not a mathematical advance or an audit verdict. Completed step
classification is NOVELTY_UNCHECKED. The later audit may be classified
REPRODUCTION under this SPECIALIZE decision. No lemma or mathematical
script was modified or executed. Mathlib full and supporting coverage
remain not checked. PROOF.md and DAG.md are unchanged because no
mathematical argument or dependency changed.
