# Hybrid moving-mask reductions: source review

2026-10-31; literature only. No mathematical audit is performed here.
The saved review target is in
`drafts/literature/2026-10-31-family003-hybrid-mask-reduction-scope.md`.
Actual-Xi all-degree positivity is the main gap. The proposed intermediate
audit could reduce L541's retained hybrid contract to two more primitive
estimates; even success would leave their verification and Xi transfer open.

## Evidence actually inspected

Primary source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).

Read the entire statement of `lem:completed-quadratic-reduction`,
2518–2566, and its essential support proof, 2567–2626. This includes
the square-factor zero mask, the complete divisor expansion, fixed
S-parts, original source-support reconstruction, arbitrary complex
coefficients, and nonempty quotient normalization. The final bounded-
coefficient norm corollary is not the proposed primitive: the weighted
output `eq:completed-quadratic-reduction` is needed instead.

Read 7036–7053 (`eq:cubic-large-sieve`, both stars, orientations and
support caveat), 7054–7084 (entire hybrid statement), and 7085–7194
(entire hybrid proof). Read L541's retained hybrid hypothesis and the
previous terminal audit working record only for the downstream contract.
No backward use of their conclusions is permitted.

Scoped searches for hybrid/completed-quadratic/moving-mask/row-mark
in ATTEMPTS returned no matches. Searches of the family003 assessments,
source notes, L541 and the immediately relevant history found only this
nomination and earlier retained contracts, not a completed matching audit.
No existing changes were reset or discarded.

## Comparison and scope decision

The quadratic theorem explicitly accepts arbitrary complex coefficients
independent of its row; bounded coefficients are needed only for its
separate corollary. Thus the next audit can test the actual inner
P'-polynomial without first bounding it pointwise. Its source support
retains permitted S-primes and shared n/b primes. The theorem's weighted
output, not merely its collapsed norm estimate, exposes the r and c'
charges needed for the next sieve. These are inspected theorem hypotheses
and source claims, not new implications proved this turn.

The cubic display allows squarefree primary indices without a rational-
norm squarefreeness condition or an additional S-exclusion. This is
essential for the original j=n/r, rather than its S-stripped part. The
manuscript fixes h,t before treating their collision mask as coefficient
support. Whether every grouping, zero identity and charge is justified
is the mathematical task deliberately left to the later audit.

Reuse the independent-source overlap assessment in
`drafts/literature/2026-10-31-family003-reflected-energy-terminal-audit.md`
and its source notes: Goldmakher–Louvel v2 Definition 1/Theorem 1.1/
Corollary 1.2 and Xu–Sang v2 definitions (1.1)–(1.2)/Theorem 1.1
were previously inspected and do not supply this masked implication.
No additional generic-sieve search was needed. Heath-Brown's original
Theorem 2 remains an unread lead after the recorded 403. The future
audit expressly retains the pinned cubic display, including its stated
orientation and support, so it cannot claim to audit that original input.

The separate audit assessment specifies the exact factors, cases and
failure tests. Source scope is adequate for that conditional reproduction;
there is no new norm bound or source-independent conclusion. Mathlib
coverage was not checked. No cross-notebook input is proposed. No new
creative sign mechanism is justified by this absolute-energy review.
