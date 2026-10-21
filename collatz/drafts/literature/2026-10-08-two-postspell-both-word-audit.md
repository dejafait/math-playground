# Both-word restriction — approved audit coverage

TARGET: Critically audit L038's bound max(4J_1+H_1,4J_2+H_2)<144 log(N)+95, including actual junction transfer, both offsets, independent tails and repeated periods.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the nine focused exact-target/stronger-result queries and primary comparisons in 2026-10-07-two-postspell-both-word-joint-bound.md; read full L038 for scope, L037 hypotheses/effective input/separate audit, L031 hypotheses/conclusion/general-tail valuation proof, ready joint/balance/reciprocal audit source passages, histories 069/082/083 and Attempt 019. No external search repeated.
SOURCE_EVIDENCE: Reused inspected Simons–de Weger, Acta Arith. 117 (2005), section 1.2 p. 52, Lemma 8 and proof p. 59, Lemma 12 and complete proof p. 61; Hercher, JIS 26 (2023), Article 23.3.5, Theorem 16 and complete proof pp. 10–11, Lemma 20 p. 12 and all Theorem 21 proof cases pp. 13–14; Sodelin Postspell_Guarded_Root_Descent.md sections 1,3,4, live main inspected 2026-10-07. No primary passage newly retrieved.
COMPARISON: Existing coverage matches L038's unchanged actual closed-word hypotheses and actual-prefix transfer inputs; successor-minimum bounds do not directly certify the designated-junction transfer. L037's audit covers only its selected index; L038's extension and constants require their own mathematical audit.
GAP: Independently check every load-bearing step in complete L038 and its essential inputs; coverage approval neither certifies its bound nor bounds total N or excludes integer closure.
REASON: The separately saved audit scope is adequately covered by ready literature; no changed essential hypothesis or unread essential source requires retrieval or a new discovery search.
SCOPE: Exactly L038 with J_i>=2,H_i>=3, independent integer a_i>=0 congruent to 2 modulo 18, actual positive closure W_1W_2, positive odd residue-20 n,x,n>1, exact tails and represented 1<K<N; admit both index orders, repetitions and x=n without least-root, primitive-period, consecutive-minimum, global-minimum or relative-growth assumptions.
LITERATURE_REASON: The distinct critical-audit continuation was REVIEW_REQUIRED; this turn approves its scope separately by reusing unchanged primary coverage, without another mathematical attempt.

## Reused primary inputs and limits

The ready assessment is
`drafts/literature/2026-10-07-two-postspell-both-word-joint-bound.md`.
Its recorded queries, exact source passages, source versions and stronger-result
comparison are reused; no search failure is evidence of novelty. The joint,
balance and reciprocal audit assessments clarify the imported scopes.

John Simons and Benne de Weger, *Theoretical and computational bounds for
m-cycles of the 3n+1-problem*, [Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
Lemma 12, printed p. 61, states
Lambda=(K+L)log(2)-K log(3)>exp[-13.3(0.46057+log K)].
Section 1.2, p. 52, permits nonminimal periods. Its complete proof and
Lemma 8 input have recorded coverage. Rhin's original proof and source
computations remain imported published inputs, not independently certified.
Importing the precisely stated Lemma 12 does not require reopening the
inaccessible Rhin source. The later audit must check represented counts
and actual nontrivial closure, retaining repetition scaling.

Christian Hercher, [*There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
JIS 26 (2023), Article 23.3.5, Theorem 16 and proof, printed pp. 10–11,
gives 0<(K+L)/K-log(3)/log(2)<S/(3K log(2)), where S is the
odd-state reciprocal sum. Its primitive state-set convention is handled
by L035's represented-occurrence application, inherited through L037.
The already repaired Corollary 17 comparator is not a new premise.
Lemma 20 and Theorem 21 concern successive minima and retain intervening
minima; they cannot be applied by treating the two junctions as consecutive.

Sodelin, node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001,
[Postspell_Guarded_Root_Descent.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
section 1, supplies the exact actual-prefix identities and envelope before
its final-halving size guard is used. Sections 3–4 retain terminal valuations
and failed-halving cases. The existing assessment inspected these passages
on live main on 2026-10-07; no immutable revision or Lean build is claimed.
Its descent theorem requires its own guard and is not imported for arbitrary
tails. L031 is the canonical general-tail finite-word input. E^2-only
transport from L024 is not coverage for this audit.

No reproof of general coding, Hercher or transcendence theory is needed.
Only the local quantitative transfer and elementary combination require
review. Matching and supporting Mathlib declarations remain **not checked**;
no full match or absence is asserted. Unread stronger-result leads in the
ready assessment remain unread and are not imported.

## Audit target, duplicates and decision test

The main gap remains universal eventual descent. The intermediate target
is a reliable audit of the conditional both-word restriction. Its plausible
downstream use is controlling represented odd counts in later closure
analysis, which remains unproved. L037 is narrower, not a duplicate audit.
Attempt 019's guard-only failure and history 069's count mismatch remain
preserved; the parked source route is not reopened. No cross-notebook input
is used.

Essential direct inputs are L031 and L037; the latter inherits L035/L036's
published effective estimates. The later audit must check the complete
L038 proof, the selected actual word's endpoint, both affine shifts,
a_i>=2 with no tail upper bound, and the other word's own valuations and
intermediate height. Check b>=47, represented 1<K<N, strict signs, exact
rational constants, both index orders, repeated occurrences and x=n.
Do not identify either junction with the global minimum or assume a
junction-size ratio. L037's separate audit does not certify these new steps.

Continuation/abandonment test: accept only if every load-bearing inequality
and dependency survives at this exact scope. Preserve any defect with its
precise failing step; repair only using justified covered inputs, or narrow
the claim. Changed essential scope requires new literature approval.
Independent tails, total N, positive integer closure exclusion, universal
entry, other cycles, divergent orbits and eventual descent remain unresolved.

This completed turn is STALLED, LITERATURE/NOVELTY_UNCHECKED: it supplies
separate scope approval but no new source evidence, inequality or audit
verdict. No lemma, mathematical script, PROOF.md or DAG.md was changed.
Mathematical exploration usage remains zero and no counter reset is claimed.
The unchanged TARGET is ready for one later RESEARCH/REPRODUCTION audit.
