# Two-postspell logarithmic restriction — approved critical-audit coverage

TARGET: Critically audit L036's conditional min(J_1,J_2)<5 log(N)+4 restriction, including boundary heights, Simons–de Weger Lemma 12 applicability and repeated-period counts.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged exact-target, stronger-result and obstruction searches recorded in 2026-10-07-two-postspell-logarithmic-parameter-balance.md; read full L036, L031 hypothesis/conclusion and general-tail valuation proof, L035 hypothesis/conclusion and period application, Attempt 019, histories 069/074/075 and the ready reciprocal audit assessment. No external search was repeated.
SOURCE_EVIDENCE: Reused Simons–de Weger, Acta Arith. 117 (2005), 51–70, section 1.2 p. 52, Lemma 8 and proof p. 59, Lemma 12 and proof p. 61; author v1.44 (2010-08-31) comparison; Hercher, JIS 26 (2023), Article 23.3.5, Theorem 16 and proof pp. 10–11 as recorded in the ready reciprocal audit assessment. These sources were previously inspected, not newly retrieved this turn.
COMPARISON: The existing inspected theorem hypotheses cover the exact audit language, including represented repeated periods; L031 supplies general-tail valuation identities and L035 the audited upper input. The new target is a review of their local combination, not a request for a stronger lower bound or a reproof of imported theorems.
GAP: Independently audit L036's boundary-height consequence, strict inequalities, represented counts and exact constants. Source readiness does not certify those mathematical steps, integer closure exclusion or universal descent.
REASON: Approve the new critical-audit continuation using adequate unchanged coverage; no missing essential source requires retrieval, and no new estimate or audit verdict is established in this literature turn.
SCOPE: Exactly L036 with J_i>=2,H_i>=3, independent a_i>=0 congruent to 2 modulo 18, actual positive integer closure, positive odd residue-20 n,x,n>1 and exact tails; allow repeated periods and equal junctions, without least-root, primitive-period or relative-growth assumptions.
LITERATURE_REASON: The saved distinct audit target was REVIEW_REQUIRED and requires separate scope approval; reuse ready coverage rather than perform further discovery or repeat primary retrieval.

Essential inputs are L031 and L035, the published lower bound cited
in L036, and L036 itself. The unchanged source evidence in
`drafts/literature/2026-10-07-two-postspell-logarithmic-parameter-balance.md`
may be reused while its hypotheses and source scope remain unchanged.
No new essential source blocker is identified. This file approves
coverage for a later critical audit; it does not perform that audit now.

The intended audit retains J_i>=2,H_i>=3, independent a_i>=0 congruent
to 2 modulo 18, positive odd residue-20 n,x,n>1, actual closure,
exact tails and repeated periods. Check the additive 23, all strict
inequalities, K versus N, the source's nontriviality and nonminimal
period scope, and exact rational estimates producing A=5,B=4.
Continue only if every load-bearing step has matching hypotheses;
otherwise identify the exact error and its effect on (1).

Universal eventual descent, integer closure exclusion, unbounded
asymmetry, other cycles, divergent orbits and universal entry remain
unresolved regardless of the audit outcome. Mathlib matching coverage
is not checked. No new mathematical result is derived here.

## Precise imported statements and review boundaries

Simons and de Weger, *Theoretical and computational bounds for m-cycles
of the 3n+1 problem*, [published article](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
Lemma 12, printed p. 61, states
Lambda=(K+L) log(2)-K log(3)>exp[-13.3(0.46057+log K)].
K,L are odd/even input counts for a positive nontrivial shortcut cycle;
section 1.2, printed p. 52, permits a nonminimal period. The reusable
assessment records inspection of the complete Lemma 12 proof and its
Lemma 8 input. Its source computational height bounds and Rhin's
Proposition, p. 160, remain imported published inputs. Rhin's original
proof was inaccessible and is not independently audited here. This
limitation is not an essential blocker to importing Lemma 12 itself.

Hercher, *There are no Collatz m-Cycles with m <= 91*,
[JIS 26 (2023), Article 23.3.5](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
Theorem 16, printed pp. 10–11, gives
0<(K+L)/K-log(3)/log(2)<S/(3K log(2)).
The ready reciprocal audit assessment records the full theorem/proof
inspection and state-set versus occurrence qualification. L035's
separately completed audit is recorded in history 073 and its canonical
audit section; its cycle conclusion is the input to L036. A later
L036 audit must check its own hypotheses match L035 and retain the
represented count convention. No reproof of Hercher or Rhin is needed:
only the local combination and elementary constant estimates require
independent review.

The prior parameter-balance assessment also compares the author v1.44
cycle bounds and Rozier–Terracol v2, Proposition 6.3. Stronger exponents
with an unspecified effective threshold are not substitutes for the
explicit published estimate used here. No inspected result states this
exact min-parameter specialization; that bounded comparison makes no
novelty or absence claim. The prior searches and primary passages are
reused because neither target assumptions nor essential source scope
changed. No primary source is claimed newly read this turn.

## Duplicates, failures and later audit test

Attempt 019 excludes boundary guards as an independent closure
contradiction; it does not prohibit their height consequences from being
combined with the independent lower estimate. History 069 preserves the
two-long-tail count mismatch and blocked Brox route; neither is needed
for this audit. L024's E^2-only transport remains outside the general-tail
input scope. L031's already canonical identities are the covered input.
The audit neither reopens those routes nor generates another lemma.

The later mathematical review must check the full L036 proof against
L031/L035 and the cited theorem: positive boundary heights with additive
23; nontriviality; represented K,N and K<N; every strict sign; natural
logarithm monotonicity; exact arithmetic and inequalities yielding A=5,
B=4. Repetition and x=n are allowed and must not be silently removed.
These are audit obligations, not computations completed in this review.

Continue if all load-bearing steps survive the covered audit. A genuine
defect must be recorded with its effect on the restriction and repaired
within covered scope, or routed to a new assessment if hypotheses change.
No independent certification of the imported computations or Rhin proof,
bound on the larger J_i or total N, or Collatz resolution is approved.

Completed outcome is STALLED, LITERATURE/NOVELTY_UNCHECKED: adequate
existing coverage approves a distinct audit, but no new source or
mathematical evidence was produced. Mathematical exploration usage stays
zero. Next turn defaults to that mathematical audit with this assessment;
no further literature review is justified absent a specific changed need.
