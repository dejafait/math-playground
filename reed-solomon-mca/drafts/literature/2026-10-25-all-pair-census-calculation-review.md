# Complete all-pair census — proposed ready continuation

TARGET: Compute a complete rank and kernel census of L109's two-row stacks over all unordered disjoint two-overlap support pairs at the fixed seven-set.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed exact-domain comparison in 2026-10-25-all-disjoint-pairs-two-row-rank-census-review.md; scoped duplicates and ATTEMPTS/041–043 checked, no matching complete census located and no novelty inferred.
SOURCE_EVIDENCE: Hall Theorem 5.1.1 pp. 63–64 https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf ; Marquez-Corbella–Pellikaan accepted manuscript 2016-02-29 section 5 pp. 7–8 https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf ; Conrad Theorems 4.2/7.1/7.5 pp. 11–12,23–25 https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf ; reuse the completed comparison's inspected proofs and applicability; L109 supplies the proved block and extension-field interpretation.
COMPARISON: Standard tools and arbitrary-row L109 cover the unchanged field/support hypotheses; the finite all-pair ranks and complete bases remain uncomputed. L104 already supplies local pair survivors; no two-row exclusion or L151 label transfer follows.
GAP: Certify exhaustive indexing, every original rank and complete kernel, and whether this domain provides useful stratification for later many-row tests.
REASON: One bounded REPRODUCTION calculation is source-ready; this separate literature-only recovery repairs direct source URLs without changing the target or approving uncovered mathematics. No new mathematics is established by this assessment.
SCOPE: Only L109 two-row stacks at fixed H/S over F_97, interpreted over F_(97^20); arbitrary original weights/chart; no third/fourth-row sweep or new gate solver.
LITERATURE_REASON: Supervisor recovery reports missing direct source URLs in this ready assessment; repair citation completeness while reusing the unchanged completed scope comparison rather than repeating discovery.

## Source-link recovery — step 473

The direct primary URLs now appear in SOURCE_EVIDENCE. On 2026-10-25,
Hall's author-hosted chapter and Conrad's undated 47-page author PDF
were accessible through the web tool. Hall's definition, Theorem 5.1.1
and proof on pp. 63–64 were rechecked: a field, distinct labels and
nonzero multipliers are required; the nonzero-dimension case applies
with n=16, k=8 and unit multipliers. Conrad's theorem locations were
checked; the complete proof coverage recorded in the October 18 review
is reused, not claimed as a fresh full-proof audit. The ordered exterior
basis applies over a commutative ring; the independence and subspace
statements apply over fields, here dimension seven and exterior degree
two over F_97 or F_(97^20).

The institutional shortening PDF returned an access error this turn.
Reuse the inspected primary extraction in
`2026-10-07-six-coordinate-triple-equality-obstruction.md`, section
“Primary shortening input,” and its applicability comparison in
`2026-10-25-all-disjoint-pairs-two-row-rank-census-review.md`.
That record identifies Definitions 5.1–5.2, Lemma 5.3 and the unnumbered
single-coordinate GRS shortening formula immediately following it,
printed pp. 7–8, accepted manuscript dated February 29, 2016, DOI
10.1016/j.ffa.2016.04.004. The formula multiplies retained multipliers
by their label differences from the removed label. The saved comparison
uses that formula, rather than extending Lemma 5.3's n-m>=k range
without qualification: L109 shortens the seven labels J minus K,
from dimension eight to one, with distinct retained labels and nonzero
differences throughout. No fresh retrieval or version comparison of
this manuscript is claimed. Existing inspected coverage suffices for
the unchanged target, so this access error is not an essential blocker.

The completed scope comparison's duplicate and ATTEMPTS/041–043 checks
are reused unchanged. No further mathematical claim, census evidence,
or novelty claim is added. Mathlib coverage remains not checked.

Use H and S exactly as specified in C152a, J=H minus S. Enumerate all
increasing I in binom(S,2), K in binom(J,2), with I outermost, and use
these indices for supports A=I union K. Enumerate a<b and retain exactly
A_a intersection A_b empty. Independently generate ordered disjoint pairs,
canonicalize and deduplicate, and compare the complete index sets. Record
the actual and independently required cardinalities; no cardinality is
asserted in this source-only review. No subgroup or label symmetry reduction.

Build L109's original blocks with least O-coordinate pivot and increasing
S-pair columns. Retain every pair, rank, independent original minor, pivot
convention and complete kernel basis. Independently reconstruct quotient
rows using ratio covectors and polynomial/Horner evaluation as in L110,
with the nonzero row rescalings explicitly accounted for; compare original
and reconstructed ranks/kernels. Check every original residual, basis
independence and rank-nullity. Save complete evidence to disk and print
only coverage, distributions, failures and paths. Existing helpers may be
reused with their roles identified; agreement of two calls to the same
elimination helper is not independent verification.

Use L109's existing minors argument for scalar extension, without rational
descent of actual weights, parameters or decomposable points. Retain all
kernels irrespective of rank. For the two previously studied numeric pairs,
identify literal inputs from L110/L125 and verify the corresponding two-row
prefix binding; do not infer equality of later-row loci from a rank match.

Main gap: uniform compatibility for C152a's arbitrary extracted pair.
Plausible use: an exhaustive domain and complete kernels can index later
many-row compatibility tests. Continue only if the certificate is complete
and exposes a usable stratum or a specific missing multi-row gate. If ranks
are uniform, report that absence of rank stratification and stop the
rank-only mechanism; do not launch more pair sweeps in the same turn.
An incomplete enumeration is unfinished evidence, not a census theorem.
No decomposability, full-weight, rank-one projection, original-chart,
nonpersistence, t=0 completion or sixteen-event realization is inferred.

Essential relevance inputs: L109 and C152a through L086/L152. Retain k=8,
pinned cell, coefficient syndromes in U_S, actual nonzero D/locators,
sixteen original finite events, t=0 and inherited L056/L069/L040 finite
certificates. Universal representation and challenge identification remain
open. Full matching Mathlib coverage is not checked. No new general lemma
or independent source result is required or approved.
