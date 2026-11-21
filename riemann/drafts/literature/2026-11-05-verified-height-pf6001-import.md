# Verified-height PF6001 — fixed-order import gate

TARGET: Import known PF_6001 nonnegativity for the actual coefficient sequence (a_j), with precise sector, product-limit and normalization qualifications.
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the completed exact-scope comparison in 2026-11-05-verified-height-pf6001-scope.md, step660; no additional browsing or broader target is needed.
SOURCE_EVIDENCE: Michałowski [2607.16795v1](https://arxiv.org/html/2607.16795v1#S1.SS2) Section1.1/(1)–(3), Section1.2 and Remark8.3; Katkova [math/0505174v1](https://arxiv.org/pdf/math/0505174v1) Definition2/(8), Theorem B and Theorem1 product-limit proof pp.4–6; Platt–Trudgian [2004.09765v1](https://arxiv.org/pdf/2004.09765v1) Theorem1 and Section2 pp.2–3. Exact source access and indexing qualifications are retained in the scope assessment.
COMPARISON: Known finite-order coefficient PF coverage contains order6001 for all ordered minors. Import this bounded input; L813 covers only an order-five cell and L466 concerns different Laguerre coefficients. No strictness, determinant-margin, hybrid-path or all-order conclusion is covered.
GAP: Write only the canonical citation/applicability for the actual ordinary coefficients, safe sector index, conjugate-grouped repeated zero factors and coefficient/minor limits with positive scaling. Stop on a genuine mismatch; no source reproof is approved.
REASON: Record known signs and rule out redundant bounded-order negative-minor searches while leaving the main RH gap and stopped hybrid conditioning unpaid. Step661 repairs missing direct source URLs and approves the unchanged target for next-turn applicability work.
SCOPE: One RESEARCH / KNOWN_IMPORTED applicability step after approval, using L018/L021 and L776 definitions; no determinant computation, mathematical script, strictness lemma, maximal-order optimization or enlargement to all degrees.

Use G(w)=xi(1/2+sqrt(w)/2)/8=sum a_j w^j with the square-root
expression interpreted through its entire series, a_j=0 for j<0.
PF_6001 means nonnegativity of every finite minor of size at most6001
of [a_(q-p)]_(p,q>=0), with increasing rows and columns. Preserve the
ordinary coefficient normalization a_j=M_(2j)/(8*4^j*(2j)!).

Cite the sector/height conclusion already stated in Michałowski
Section1.2; do not reproduce its zero-geometry proof as new mathematics.
Check m=6001 against m+1<=pi H with the published H, retaining the
closed verified-height range and conjugation/zero-height cases.
The source's G matches the target. When citing Katkova's polynomial
sector theorem and entire passage, state the positive constant,
order-one-half genus-zero product, real grouped finite products,
repeated factors, compact convergence and fixed finite minors.
Retain explicit positive scale factors for arbitrary increasing indices
if using Katkova's b_j rather than the already matching G.

Schoenberg's original full text was inaccessible; cite its exact named
theorem as reproduced in Katkova Theorem B, without inventing an original
theorem number or claiming to have read its proof. Do not use Katkova's
mismatched printed PF44 inference or an unaudited maximal-order endpoint.
The import is citation-based; it does not require rerunning the published
zero verification. Full matching Mathlib coverage is unchecked and
must be stated honestly in the canonical file.

Essential local inputs are L018/L021 and the ordinary-coefficient
conventions of L776. L813 is an existing normalization/overlap check;
L466 supplies a precise existing height citation, not a sign premise.
L830/L831 and the hybrid reference have no role as positivity inputs.
No cross-notebook input is needed. Actual all-degree signs, strict
margins, hybrid regularity and RH remain open. The downstream use is
one known bounded sign region and the removal of redundant searches.

## Step661 recovery approval (2026-11-05)

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; this review repairs traceability without broadening the target or repeating discovery.

Opened all three versioned primary URLs above. Rechecked Michałowski
Section1.1–1.2, Katkova Theorem B and the complete short Theorem1
product-limit argument, and Platt–Trudgian Theorem1. They match the
scope assessment's recorded statements. This is renewed access and
process validation, not new mathematical evidence or a reproof.
The original Schoenberg proof remains unread; Katkova's reproduced
statement supplies the cited sector theorem. The printed PF44 index
inference remains excluded. No theorem about strict signs or hybrid
matrices is added.

The unchanged exact target is approved as IMPORT for the next turn.
The canonical applicability step must still check the local coefficient
conventions and real grouped products as specified above; this review
does not preempt those checks. Mathlib matching coverage remains
unchecked. Existing overlap and failure comparisons in the scope
assessment remain adequate and are reused.
