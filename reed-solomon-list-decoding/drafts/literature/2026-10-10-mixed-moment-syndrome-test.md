# Mixed-moment syndrome — proposed bounded test coverage

TARGET: Test the four-coordinate mixed-moment syndrome Phi(B)=(sum x,sum x^2,sum x^3,sum c*x) on all (3,2,2,2)-profile nine-sets in nine F_107 columns for a same-syndrome pair intersecting in at least five points.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed bounded search in 2026-10-10-column-aware-syndrome-packing.md; no matching theorem or completed local test was found.
SOURCE_EVIDENCE: https://arxiv.org/pdf/math/0311385v1 — Harm Derksen, Error correcting codes and B_h-sequences, v1 (21 November 2003), Definition 1, Proposition 2/full proof, Corollary 4/full proof and Theorem 5(a,b), printed pp. 2–3; primary text rechecked on 2026-10-10.
COMPARISON: Known B_4 fibers separate distinct indexed points; the proposed mixed moments lack that guarantee and require their own conflict test, with no novelty claim.
GAP: Prove separation for the full profile universe or certify a same-syndrome conflicting pair; no finite packing guarantee exists yet.
REASON: A bounded compatibility test is independent of the failed maximum-neighborhood certificate and directly checks column information before any threshold calculation.
SCOPE: Only the displayed map over F_107 with column labels 0,...,8 and all profile placements; start with three-value cyclic reassignments among the size-two columns. No map optimization is covered.

Separately approved on 2026-10-10 for the exact TARGET above. This
source review repairs the missing direct URL and approves a bounded
compatibility test; it establishes no mathematical result. Reuse the
full comparison in `2026-10-10-column-aware-syndrome-packing.md`.

Essential inputs: L045 fixes Omega, the profile universe and conflict
criterion; L043 supplies the compatible graph baseline for downstream
use only. A negative witness must list both complete nine-sets,
verify distinct points, both profiles, all four exact syndromes and
their full intersection. A positive result needs a universal proof,
then an exact finite image/pigeonhole comparison against 5774752369;
a bounded unsuccessful search cannot substitute for it. Park this
specific map on a certified conflict without changing it in the same
attempt. No prior stop on other algebraic constructions is inferred.

The downstream use is the L041/L042 local-cap comparison, subject to
its separate audit/application. Actual-label transfer, cross-core
consistency, common-center RS realization, 67/68 safety and ABF
comparison remain unresolved. Matching Mathlib coverage is not checked.

## Separate approval and source applicability

The direct primary PDF was retrieved in this review. Definition 1
requires distinct sums of h indexed terms, allowing repeated indices.
Proposition 2 assumes that property for the labels in an abelian group
and concludes minimum distance at least 2h+2 within each weight fiber.
Its complete proof cancels common indices and pads shorter sums to h;
thus its hypothesis covers all smaller differences, not only size h.
Corollary 4 then uses pigeonhole over the group. Theorem 5 requires
distinct field labels and a polynomial nonzero at them; neither branch
states separation for the displayed mixed moments. Its proof cites
Bose–Chowla and is not imported or reproved for this test.

L045's Hypotheses and universe-count definition were inspected: points
are pairs (c,x), all labeled profile placements are included, and a
conflict means intersection at least five. The first three moment
coordinates use values x rather than distinct pair indices. No inspected
source asserts the needed separation for this map. The parent review's
bounded search is reused with unchanged hypotheses; no new broad
search or novelty inference is needed for this exact diagnostic.
The local parent review, history/133 and ATTEMPTS/029 contain no completed
test of this map. L043–L045 remain inputs or contrasts as specified
above, not evidence for syndrome separation.

Approval is EXPLORE, limited to testing this fixed map and recording
complete conflicting nine-sets if found. Begin with the proposed cyclic
reassignments; these are a search restriction, not an exhaustive reduction.
Do not change coefficients or claim a packing guarantee after a bounded
search. Universal separation and an effective image bound are independent
unresolved requirements. No new lemma, calculation or script is supplied
by this approval. Matching Mathlib coverage remains unchecked.
