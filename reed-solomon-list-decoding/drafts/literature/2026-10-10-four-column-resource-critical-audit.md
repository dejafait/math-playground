# Four-column resource optimum — critical audit coverage

TARGET: Critically audit L043's four-column resource optimum and nonexclusion interpretation, including all capacities, coefficients, primal/dual witnesses and integer rounding.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused exact-parameter, packing/constant-weight terminology and graph-augmentation queries in 2026-10-10-finite-nine-set-packing-lower-bound.md; searched dated local assessments, history/123–125 and ATTEMPTS/027 for this audit and stops; no completed separate critical audit was found in those paths.
SOURCE_EVIDENCE: Reused primary theorem statements and relevant graph/augmentation proof cases inspected in 2026-10-10-four-column-packing-resource-test.md: Xu–Chen v4 Proposition 2.2 (https://arxiv.org/pdf/1505.06524v4, printed p. 3) and Bailey–Burgess v2 Definition 1.1.1 (https://arxiv.org/pdf/1107.4120v2, printed p. 2); read L043 to compare scope without certifying its mathematics.
COMPARISON: Inspected sources cover the graph baseline and packing uniqueness with unchanged hypotheses; neither supplies this profile optimum, its witnesses or an actual packing from feasible counts. Existing search coverage supports a separate audit of that same finite statement, without a novelty claim.
GAP: Independently verify L043's profile completeness, counting formulas, exact witnesses, integer rounding and relaxation direction; literature approval verifies none of those mathematical assertions.
REASON: Separate approval of the newly proposed audit reuses adequate source coverage; no changed hypothesis or essential unread source requires further browsing, and the next turn should be mathematical.
SCOPE: Audit exactly L043 on Omega={0,...,8} times F_107 with all degree<=4 graphs, additions on at most four columns, ordinary five-subset uniqueness and two unused embedding points; no source augmentation, larger column scope or packing realization is approved.

Essential input is canonical L043 and its two complete exact local
certificates. A subsequent audit should independently check the eighteen
block/six resource types, actual capacities, all 108 coefficients,
graph/addition compatibility, exact dual bound and primal attainment,
rounding and distinction between feasible counts and actual blocks.
The source baseline must retain q=107,w=9,r=5, nine distinct evaluation
points and degree<=4. All additions are restricted to at most four
columns in Omega; the two extra embedding points and source optional
augmentations remain unused. Mathlib coverage has not been checked.

L041 and audited L042 are interpretation references, not mathematical
inputs to the resource optimum. An actual packing above 19800269675
would obstruct the sufficient uniform cap after at most 1024 deletions;
L043 supplies no such packing. Actual-label restrictions, cross-core
consistency, common-center realization, safety at 67/68 agreements and
ABF comparison remain unresolved. No new mechanism or expanded column
scope is approved here. The separate coverage comparison is now
complete; the next turn is the saved mathematical audit.

## Source applicability and limits

Liqing Xu and Hao Chen, *New Explicit Binary Constant Weight Codes
from Reed-Solomon Codes*, arXiv:1505.06524v4, 7 August 2015,
Proposition 2.2, printed p. 3, assumes a prime power q and
q>=w>r-1. Its graph family evaluates all degree<=r-1 polynomials
on any w distinct field points and gives q^r weight-w words of
length wq with distance at least 2w+2-2r. The saved parameters
(107,9,5) and indicated nine distinct points are within the already
assessed specialization. Import this result by the
[versioned primary citation](https://arxiv.org/pdf/1505.06524v4);
do not reprove it. Proposition 2.2 covers only the baseline here.
The previously read Theorems 2.1–2.2 and their augmentation cases
do not cover the four-column profile LP. Their optional blocks
remain absent; compatibility with them is not assumed.

R.A. Bailey and A.C. Burgess, *Generalized packing designs*,
arXiv:1107.4120v2, 15 November 2011, Definition 1.1.1,
printed p. 2, defines t-(v,k,lambda) packings for positive integers
v>=k>=t by each t-subset occurring in at most lambda blocks.
The assessed (v,k,t,lambda)=(963,9,5,1) is the resource ground
set; the 965-point embedding adds no usable resource in this target.
Import the definition by the
[versioned primary citation](https://arxiv.org/pdf/1107.4120v2).
It supplies a necessary uniqueness condition, not existence or
sufficiency of profile inequalities. The nested-floor upper bound
is unnecessary for auditing this resource optimum.

The finite lower-bound assessment already compares stronger leads:
the inspected Xu–Chen augmentation misses the downstream benchmark,
and Keevash's theorem has no verified finite cutoff at 965.
Derksen's inspected finite fiber formulas do not certify this
resource optimum. The Graham–Sloane scan remains an unread lead,
not an essential audit input. No negative search establishes novelty.
No new external retrieval was made: source versions, assumptions
and target scope are unchanged, so primary coverage is reused.

## Approved audit and discriminating test

The main gap remains arbitrary-center safety at 67/68 agreements.
The intermediate target is a critical audit of L043. Its plausible
downstream use is to retain or correct the stop on this restricted
resource-exclusion diagnostic before pursuing an actual construction.
ATTEMPTS/027 preserves that stop; it does not prohibit checking
the result or constructing a packing. The local searches found
the calculation and independent computational reconstruction,
but neither substitutes for the separate proof audit.

Read the complete relevant evidence in
`scripts/finite-support/four-column-resource-results.json` and
`scripts/finite-support/four-column-resource-audit-results.json`
during the audit; no certificate was verified in this literature
turn. Check all profile cases, formulas, signs, row/column values,
objective equality and floors against the explicit proof.
Reproving the known graph theorem is unnecessary; checking its
specialization, new compatibility argument and finite certificate
is necessary because the source does not establish them.

Retain L043 only if every load-bearing claim and scope qualification
survives. Otherwise isolate and repair the failed assertion within
this scope; do not broaden the mechanism. The comparison with
19800269675 must remain nonexclusion, and integer resource feasibility
must remain distinct from realizability. L041/L042 enter only for
downstream interpretation, not as inputs to the resource optimum;
read their canonical statements before auditing that interpretation.
All independent gaps listed above remain unresolved. No new lemma,
calculation, source theorem, boundary improvement or Mathlib coverage
finding is established by this approval.
