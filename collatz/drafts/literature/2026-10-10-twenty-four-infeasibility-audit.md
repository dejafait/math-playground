# Twenty-four-word infeasibility audit — ready coverage

TARGET: Critically audit L053's twenty-four-word simultaneous infeasibility proof and its exact certificate under the unchanged L051 (1)–(4) hypotheses.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready twenty-four feasibility, twenty-three audit and fixed-pair audit assessments; searched cyclic junction splitting/reciprocal mass/integer floors, the exact postspell count and unchanged pair; read full L053 and its generator, L051 hypotheses/bridge, L052 local estimates, L041 occurrence/seed/own-word passages and scoped histories 139–141/Attempt 024. No mathematical verification performed.
SOURCE_EVIDENCE: Reopened Simons–de Weger Acta Arith. 117 (2005), section 1.2 p. 52, Corollary 2 and complete proof p. 53, Lemma 12 and complete proof p. 61; reopened Hercher JIS 26 (2023), Article 23.3.5, Theorem 16 and complete proof pp. 10–11. Supporting original-source/global-minimum comparisons are reused from ready assessments.
COMPARISON: Published integer-cycle bounds support the unchanged actual-word bridge; neither those bounds nor inspected rational coding/global-minimum results give a correctness verdict for L053's new cyclic split, sharpened mass, Bezout residue alternatives or integer-floor induction in this real-height system.
GAP: Independently verify every L053 analytic implication and complete load-bearing certificate operand, including the whole-ray ceiling, all 24 cyclic factors, all residue alternatives and own-index floor bounds; no additional source theorem is essential in this fixed scope.
REASON: Changed audit-scope comparison is complete and permits one later RESEARCH/REPRODUCTION proof audit after separate supervisor approval; readiness is not an audit verdict, mathematical advance or novelty claim.
SCOPE: Exactly L053's written proof and existing certificate under L051 (1)–(4) at r=24; retain p=9809721694, q=6189245291, log24 seed, length remainder 1656/1034, all guards and endpoints. No stronger threshold, pair optimization, tail cap, new constraint or larger-count search.
LITERATURE_REASON: The newly selected L053 audit had REVIEW_REQUIRED coverage; its cyclic split, residue partition and integer-floor envelope differ from the already covered twenty-three audit and require a separate comparison despite unchanged general sources.

The target keeps exactly L051 (1)–(4) at r=24: log24 seed, length
remainder 1656/1034, all own-index guards and exact endpoints, integer
parameters/counts/scaling, positive Lambda, real s_i>=540/11 and minimum
s_0, independent tails, repeated occurrences and ties. Essential inputs
are L053, L051, L052 and L041; inherited L046/L050 passages may be
consulted narrowly if needed to check their imported per-occurrence and
product calculations. No stronger source threshold, optimized pair or
larger-count search is proposed.

The audit must test the whole-ray N ceiling and K<2N/3 before separation;
the applicability of L052's local estimates; the split R_j+R_(24-j)
bound for every 1<=j<=23; all endpoints in the product; the conclusion
that only one height can be <=30, including ties; the positive denominators
in D_32,D_63; the Bezout congruence and every residue alternative;
the lower real height used to control the endpoint shift; and both integer
floor substitutions with their signs. Check all 24 input bounds, including
the near-integer floor at index 18, with independent exact arithmetic.
An extra generated final upper transition is not a closing hypothesis.

Certificate: `scripts/postspell-word-count/twenty-four-height-certificate.json`.
Generator: `scripts/postspell-word-count/certify_twenty_four_heights.py`.
All 29 generation checks passed, along with integer assertions; that is
not an independent audit. Decimal preliminary files are unused. Full
matching Mathlib, external Lean builds and original published computation/
transcendence certificates remain unchecked. The result concerns only
the restricted cycle language; entry, unrestricted cycles, divergence
and universal eventual descent remain open.

## Relevance and decision test

Main gap: universal eventual descent of every positive start greater than 1.
Intermediate target: determine whether L053's claimed restricted exclusion
survives an independent critical audit, or isolate a specific defect.
Downstream use: support using the twenty-four-word exclusion with its
qualifications, or withhold/repair the affected implication. Universal entry,
unrestricted cycles, divergence and eventual descent remain unresolved.

Coverage is sufficient to continue to the exact saved audit after separate
approval. The later acceptance test requires every analytic, arithmetic and
actual-word obligation to pass under the written hypotheses. A failed
implication or unresolved strict sign must be preserved explicitly; it does
not establish feasibility or an actual cycle. Do not extend the count or
repeat L051's stopped sufficient predicate. No complete Collatz candidate
has been developed.

Retain integer J_i>=2,H_i>=3, nonnegative integer a_i congruent to 2
modulo 18; K=sum(3J_i+H_i), L=sum(J_i+a_i), N=K+L; positive integer
d,K_0,L_0 with K=dK_0,L=dL_0,K_0>225640000. Keep positive Lambda,
N<(8/5)K+1656/1034 and all the real-domain conditions above. No integer
parity/residue/valuation realization of real junctions or failed fixed-test
guard may be added. Formal primitive scaling does not realize an orbit.

## Primary inputs and specialization limits

John Simons and Benne de Weger, *Theoretical and computational bounds for
m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
[published paper](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
section 1.2 p. 52 allows nonminimal periods and counts all local minima.
Corollary 2 and complete proof p. 53 give K>225640000 for a nontrivial
positive integer cycle, using Crandall's Lemma 1, the then-verified height
301*2^50 and continued-fraction denominators 225644606/397573379.
Lemma 12 and complete proof p. 61 give
Lambda>exp[-13.3(0.46057+log K)] by Rhin's Proposition p. 160 and
Lemma 8. These passages were reopened. Supporting Lemma 8/original-source
coverage and computational qualifications are reused, not recertified.
Their domain is actual integer cycles, not arbitrary real junctions.

Christian Hercher, *There are no Collatz m-Cycles with m <= 91*, JIS 26
(2023), Article 23.3.5,
[Theorem 16 and complete proof pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf):
for a cycle with odd/even counts K,L, its positive linear form is less
than one third of the full odd-input reciprocal mass. Reopened the cycle
product, arithmetic/geometric mean step, strict logarithmic comparison
and maximal-odd-run partition. The previously inspected correction leaves
Theorem 16 unchanged; amended Theorem 21 and the full-minimum cutoff are
unused. No replacement of the full minimum count by 24 is licensed.

L041's existing all-r argument provides the actual-word bridge: occurrence
partition and primitive scaling, seed at the smallest designated junction,
own-word identities and shifted endpoints. Its relevant proof ranges were
read. L052's estimates before count-specific assembly use these same
real-domain guards occurrence by occurrence; its twenty-three-word final
contradiction is not an input at twenty-four. The audit must check this
applicability rather than impose integer realization on the real system.

Reuse the completed assessments
`2026-10-10-twenty-four-simultaneous-feasibility.md`,
`2026-10-10-twenty-three-infeasibility-audit.md` and
`2026-10-10-fixed-pair-range-critical-audit.md` in this directory.
Their inspected Halbeisen–Hungerbuehler coding and stronger global-minimum
comparisons do not decide this designated-junction system. A rational
coding theorem is unnecessary for a contradiction with no witness claim.
The exact pair residual, Bezout identity, finite residue partition,
geometric split and floor induction are explicit specialization checks,
not additional imported Collatz theorems. A later audit should verify
them directly; reproof of published coding/cycle/transcendence results is
unnecessary. No new mathematical derivation was performed in this review.

The published distributed computation, Roosendaal communication,
continued-fraction and Rhin/Crandall originals remain qualified imports.
Original computation/transcendence certificates, external Lean builds
and full matching Mathlib coverage are unchecked. Unknown Mathlib
availability is not evidence of absence. Previously preview-only stronger
cycle/extremal-cycle leads remain unused and nonessential to this fixed
audit; no stronger odd-count threshold is introduced.

Reopened the [MathPrize page](https://mathprize.net/posts/collatz-conjecture/)
dated 2021-07-07 on 2026-10-11. Its exact target remains convergence to 1
from every positive integer under f(n)=n/2 for even n and f(n)=3n+1 for
odd n. This agrees with local GOAL and the existing foundation conventions;
prize adjudication supplies no mathematical premise.

## Searches, duplicates and recorded failures

Focused queries on 2026-10-11:

- `Collatz cycles cyclic junction heights split reciprocal sum integer counts Bezout floor bounds`
- `Collatz "postspell" "twenty-four" infeasibility`
- `Collatz cycle "9809721694" "6189245291"`

Returned material included general rational-cycle/cycle-bound papers,
repositories and forums. Snippets and repository claims are not theorem
evidence. Only the primary passages identified above were newly inspected
as mathematical sources; no inspected result supplied a full matching
verdict. Existing focused discovery and stronger-result comparisons are
reused. A failed search does not establish novelty.

Scoped histories 139–141 record the completed L052 audit, changed-count
coverage and L053 attempt, respectively. No independent L053 audit is
recorded there; its generation checks explicitly are not such an audit.
Attempt 024 preserves L051's failed fixed predicate at twenty-three:
the half-log guard fails and T_23 exceeds the required threshold.
L053 uses different retained information, so this stopped predicate is
neither renewed nor a ban on the present audit. Earlier scalar/guard-only
stops are preserved through the reused assessment; no scalar survivor is
treated as simultaneous feasibility.

## Certificate scope for the separate audit

Read the full existing generator identified above for scope only, without
execution or certificate validation. The later audit must inspect complete
relevant certificate evidence with the scoped JSON inspector and independently
check it, rather than rely on saved flags, decimal previews or regeneration
alone. In addition to the obligations above, check every binary reduction,
all rounded summands and complete rounding/remainder budgets, outward
epsilon cancellation and every complete operand. The reported 29 rational
checks plus modular/residue/floor assertions remain unaudited here.

Verify that the cyclic segments partition all 24 inputs, that absence of
a second low height is proved with ties/repetitions retained, and that the
residue alternatives cover all cases, including a zero residue. Inspect
the full near-integer index-18 floor argument. Compare both final count
alternatives with the strict primitive threshold. Real junctions need no
integer realization; actual-word applicability requires the qualified bridge.

Completed EXPLORATION, LITERATURE/NOVELTY_UNCHECKED, actual task
literature_comparison: changed audit-scope coverage, no mathematical
advance or verification beyond the sources checked. No lemma, mathematical
script or certificate was written or executed. PROOF.md and DAG.md are
unchanged. Mathematical exploration usage stays zero after L053's advance.
The newly ready assessment receives separate supervisor approval before
one RESEARCH/REPRODUCTION audit; this preserves the completed L053 attempt.
