# Fixed derivative error-budget audit — source coverage approved

TARGET: Critically audit L101's M=Y=128 second-derivative error budget and finite-arithmetic enclosure contract, without evaluating the derivative.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-target queries and duplicate/failure comparison in drafts/source-notes/2026-10-21-complex-derivative-sources.md; separately matched the completed L101 audit scope to primary statements in drafts/source-notes/2026-10-21-fixed-derivative-audit-coverage.md; no novelty claim.
SOURCE_EVIDENCE: Cremona (1997), Proposition 2.13.1 and Mellin proof, printed pp.42–43 https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36; Wuthrich v2 Lemma 4/proof printed pp.6–7 and Section 4.1 printed p.8 https://arxiv.org/pdf/1608.06423v2#page=9; DLMF 4.5.4 https://dlmf.nist.gov/4.5.E4; Johansson v1 Section 2/2.1 printed pp.2–3 https://arxiv.org/pdf/1802.07942v1#page=2; FLINT official callback/integration/accuracy contract https://raw.githubusercontent.com/flintlib/flint/main/doc/source/acb_calc.rst (mutable main, accessed 2026-10-21); Wiles analytic-zero/one theorem printed p.4 https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=4.
COMPARISON: Primary sources cover L101's imported formula, coefficient majorant, single-prime sign and conditional rigorous integration; they do not directly certify its fixed-cutoff inequalities, parameter sensitivity or assembled error radius. Those local specializations are exactly the separate audit, not a new derivation authorized here.
GAP: Source coverage is ready; mathematical correctness of L101's full remainder bounds, parameter bookkeeping and finite contract remains unaudited. No backend, finite kernel outputs or zero-excluding derivative interval exists.
REASON: Separate literature comparison of the newly completed specialization is now finished; approve the unchanged proof-audit target under SPECIALIZE, reusing adequate known-method coverage without approving its truth.
SCOPE: Proposed proof audit only; no derivative computation, implementation, backend installation, cutoff enlargement or BSD claim.

The result to audit is the canonical
[L101](../../lemmas/L101-conductor389-second-derivative-error-budget.md),
not a numerical preview. Essential local inputs are L030's exact model,
conductor and modularity, L031's independent a_389/sign and elementary
parameter rules only, audited L099's rank>=2, and foundations/02's
analytic-zero/one theorem. Do not use L035's published analytic order or
L100's p-adic squeeze as a replacement for the complex hypotheses.

Check Cremona's factor four and the passage from completed L to L'';
the finite nonzero analytic order and lower-vanishing argument; and the
Fricke convention. Verify the coarse outward c enclosure, every rational
comparison in both geometric remainders, disjoint coverage of the
omitted pieces, and the absolute-error versus interval-width distinction.

Review the finite-interval derivative estimate giving |S'|<200, the
actual midpoint/radius contract, all signed weights and the sufficient
output widths. Match the holomorphic callback and logarithm branch
conditions to the inspected finite-integrator contract. Backend and
finite outputs remain unavailable; this is a conditional enclosure
contract, not an executed certificate. The FLINT main URL is mutable
and was inspected previously on the stated date, not pinned here.

Continue toward any finite replay only after a separate audit validates
the bound and qualifications. If it finds an error, preserve the old
proof and record a precise repair or obstruction. No independent audit
or approval of this new target was performed in the derivation turn.

Separate step 395 approves source coverage only. The unchanged TARGET
is ready for a REPRODUCTION proof audit; it remains mathematically
unaudited. Correct Wuthrich Section 4.1 to printed p.8 (PDF page 9)
when the canonical proof is next audited; no lemma was edited in this
literature turn. See the separate source-coverage record for the exact
source comparison, qualifications and continuation test.
