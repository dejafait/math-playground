# Proposed adjacent response-grid sign comparison

TARGET: Assess whether unconditional Gram-interval results yield infinitely many consecutive actual response zeros g_j,g_(j+1) with F_0(g_j)F_0(g_(j+1))>0.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact pair-sign, weak Gram-law and shifted-Gram searches located Trudgian's published occupancy argument and Korolev's explicit endpoint qualification; scoped response/count assessments and failures contain no duplicate actual-grid specialization.
SOURCE_EVIDENCE: Trudgian, Acta Arith. 148(3) (2011), DOI 10.4064/aa148-3-2, Theorems 5.1–5.3 and full 5.2–5.3 proofs pp. 242–244, §6.3 p. 247; Korolev arXiv:1106.0516v2 pp. 1–4, conventions p. 7, Theorem 4/full proof pp. 17–18; reuse recorded Kalpokas–Steuding and Christ–Kalpokas coverage.
COMPARISON: Inspected proved results supply ordinary-grid occupancy, while the recorded Selberg pair-sign assertion is not proved in the inspected passages; none supplies strict products at consecutive full-variable-phase response zeros.
GAP: Variable-grid transfer and nonzero left endpoints are independent missing steps; no conclusion about the truth of positive adjacent products is obtained.
REASON: Complete bounded comparison and park direct pair-sign import; prepare a separately approved variable-grid occupancy specialization without deriving it this turn.
LITERATURE_REASON: The changed hypothesis is sampling consecutive exact response zeros, with a two-point sign conclusion rather than a continuous fixed-shift moment; the prior ready audit does not cover this target.
SCOPE: Fixed actual F_0,G from L366, eventual consecutive simple G zeros and the full phase from L372; no RH, F_0 simplicity, noncoincidence, discriminant sign, common-zero count or replacement by a constant-angle Gram grid.

The bounded assessment is completed on 2026-10-10. Outcome: EXPLORATION,
classification NOVELTY_UNCHECKED. No theorem or mathematical script is
written. The existing ready L383 audit assessment remains unchanged.
The original proposal and continuation test below are retained as the
record of what was reviewed; the completion section qualifies the result.

Main gap: global actual-theta mixed positivity and the total L367 margin.
Intermediate target: strictly positive F_0 endpoint products at arbitrarily
late consecutive G zeros. Plausible downstream use: test an endpoint-sign
mechanism for a Wronskian zero in the open response cell, where G does not
vanish. The later application must explicitly justify that implication
using L380's sign convention and L372's simple crossings; it is not being
proved as a new lemma here. No claim about its frequency or truth is made.

Essential inputs for a later application are L366 (exact pair), L368
(carrier and right-line bounds), L372 (full variable phase and simple
crossings), and L380 (Wronskian convention). L383 is the stopped
continuous diagnostic, not a premise for positive adjacent products.
The canonical L379 absolute-margin obstruction and the common-only reset
examples L371/L373 remain relevant cautions. They do not decide this
two-point sign target. All common-zero, global-positivity, total-margin,
low-index, height-above-forty and endpoint-margin gaps remain unresolved.

Reuse the detailed source qualifications in
`drafts/literature/2026-10-08-actual-common-zero-count-bound.md` and
`drafts/literature/2026-10-08-wronskian-response-cell-signs.md`.
In particular the recorded Korolev proof opening is not its full proof;
ordinary Gram-interval occupancy cannot silently become strict endpoint
sign information. Nonzero samples counted individually do not assert
adjacent pairs, and a bounded variable phase cannot silently be frozen.
Search the exact statement, stronger unconditional pair-sign results and
obstructions; inspect the relevant primary hypotheses and proof cases
before assessing applicability. No novelty follows from the local check.

Continuation/abandonment test: approve only a source-covered consequence
or one explicit, bounded specialization whose errors preserve a strict
positive adjacent product or a signed statistic that forces one. If
available results only address constant-angle grids, single-point
nonvanishing or zero occupancy without endpoint control, record that
specific mismatch; do not repeat L379's absolute triangle enclosure or
alter L383's shift/cutoff. This new proposal receives separate review
before any mathematical application. Matching Mathlib coverage is not
checked.

## Completion: exact hypotheses and decision

The inspected primary sources are [Trudgian's published paper](https://www.impan.pl/shop/publication/transaction/download/product/82370)
and [Korolev v2](https://arxiv.org/pdf/1106.0516v2). Trudgian's
Theorem 5.3 concerns ordinary half-open Gram intervals and all strip
zeros. Its proof uses shifted-S moments, runs of one-zero intervals,
an exceptional-set estimate, and count balance. It does not state
nonvanishing at the excluded left endpoint. Korolev's Theorem 4 likewise
counts empty and multiply occupied ordinary intervals; its full proof
uses one-sided S differences. His introduction explicitly separates
these counts from strict endpoint signs. The quoted Selberg assertion
there concerns Hardy Z, whereas Trudgian §6.3 quotes critical-line zeta
values: their alternating Gram factor must be retained. No quoted
assertion is imported as a proved actual-response-grid theorem.

The stronger conclusion needed here is simultaneous strict signs on the
same consecutive actual grid. L372 gives G=D cos(phi), D>0 and
phi=vartheta+beta+eta; L379 gives F_0=-A H, A>0, at the identical
height. These are existing canonical identities, not fresh derivations.
The bounded eta is variable, not an error tending to zero in phase.
Ordinary-grid signs cannot simply be transferred, and an empty half-open
cell still leaves F_0 at its left endpoint undecided. We do not assume
that moving an endpoint preserves its sign or avoids a zero.

The new lead is the *proof mechanism* of Trudgian Theorems 5.2–5.3,
not a direct theorem application to G. A separate assessment prepares
the weaker, independently testable actual-cell occupancy specialization:
`drafts/literature/2026-10-10-variable-response-cell-occupancy.md`.
This may leave endpoint control unresolved. It is materially different
from L379's absolute value enclosure and L383's fixed correlation.
The target strict products and their Wronskian use remain unproved.

Queries included `Korolev Gram law sign Z(t_n) Z(t_n+1) positive proportion`,
`"Gram points" "same sign" zeta`, `Trudgian Gram law fails positive
proportion arxiv`, `zeta Gram intervals same sign endpoints unconditional
theorem`, and `zeta "shifted Gram points" "sign" Lester`. Additional
search hits are unread leads, not evidence of applicability or novelty.
The published source supersedes the inspected early arXiv:0811.0883v1
for this comparison. Mathlib coverage remains not checked. No lemma,
source theorem import into the canonical argument, sign, count bound,
or RH consequence was established this turn.
