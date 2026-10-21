# Two-postspell reciprocal sum — completed scope review

TARGET: Bound the odd-state reciprocal sum of any actual positive two-postspell concatenation by C(1/n+1/x) with explicit parameter-independent C, and test its use in Hercher's Theorem 16 under closure.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted reciprocal-sum, odd-run, geometric-growth and exact-postspell searches completed; L020/L021 formula ranges, L031 closure statement, L034 occurrence/period proof, Attempt 019, histories 057/066 and prior source assessments checked; queries and limits below.
SOURCE_EVIDENCE: Hercher, JIS 26 (2023), Article 23.3.5, Definition 6/Remark 7 and full proof, printed pp. 4–5, Theorem 16 and full proof, pp. 10–11, Corollary 17 and proof, p. 11, Theorem 27 and proof, pp. 19–20 (Lemma 26 cases not newly audited); Simons–de Weger v1.44 (2010-08-31), section 1.2 and Lemma 4/Corollary 5 with proofs, pp. 2/7; Rozier–Terracol v2 (2025-02-13), Theorem 4.1 and full proof; Sodelin postspell note sections 1–3 and reciprocal-summability packet read as qualified leads.
COMPARISON: Known odd-run geometric estimates, actual OOEO affine identities and the cycle ratio inequality support a specialization; checked generic bounds retain a minimum count or odd-step count, while harmonic-mean and infinite-orbit-set results do not give the required two-input uniform constant.
GAP: Combine the repeated OOEO portions and terminal odd spells with complete occurrence accounting to obtain an explicit parameter-independent C; the bound and any improvement under closure remain unproved.
REASON: Approve one subsequent proof attempt at the unchanged finite-word target, importing covered identities and estimates without redoing general parity theory or cycle product proofs; no essential source blocker remains and no novelty claim is made.
SCOPE: T shortcut map; actual finite W_1 W_2, W_i=(OOEO)^(J_i) O^(H_i) E^(a_i), J_i>=2, H_i>=3, a_i>=0 congruent to 2 modulo 18; n>1 and positive odd n,x=T^(D_1)(n),y=T^(D_1+D_2)(n) congruent to 20 modulo 27, with both final tails exact. Bound finite words without assuming y=n; retain closure and repeated representations for the later cycle application. No least-root, primitive-period or distinct-junction assumption.
LITERATURE_REASON: Changed quantity from long-tail count to reciprocal mass, and enlarged test domain to actual finite words; exact statement/stronger results and the specialization difference need comparison with reusable primary coverage.

## Main gap and proposed discriminating target

Universal eventual descent is still missing. With N=D_1+D_2 and
x=T^(D_1)(n), define S as the sum of 1/T^t(n) over the odd input
occurrences with 0<=t<N. Count occurrences, not distinct values.
Seek one explicit finite C valid for every finite concatenation in SCOPE,
independent of J_i,H_i,a_i and of n,x. This is a proposed inequality,
not a newly established result. Removing closure makes the test
independent of the unresolved existence of a positive closed word.

Under actual closure, a uniform bound could improve the input to
Hercher's Theorem 16 by controlling the total reciprocal mass without
a factor proportional to J_1+J_2. No rational-approximation contradiction,
finite parameter bound, integer-closure exclusion or termination is
currently available. Theorem 16's gap constraint is not sufficient for
closure, and a bound on S alone would leave these independent gaps.

Continue after review only if reusable primary results plus an identified
finite-word difference justify a concrete proof attempt. For that later
attempt, require an explicit parameter-independent C and a meaningful
comparison with the generic all-minima estimate. Abandon this proposed
uniform bound if a rigorously guarded family makes S/(1/n+1/x) unbounded;
if the only estimate grows with J_i or merely restates the cycle product,
record that limitation and reassess its usefulness. Do not assume a
positive cycle in order to furnish an unconditional test family.

Essential local inputs to read narrowly are L020/L021's affine word and
positive-offset formulas, L031's closure qualification and L034's
occurrence/period conventions. The prior cycle assessment and the
completed run-count comparison provide primary-source locations.
Check exact statement, stronger results and recorded failures before
deriving the bound. Attempt 019 stops extra boundary guards, not this
sum estimate. No budget based on one starting valuation, primitive
representation or cycle minimum may be substituted for this target.

## Completed primary comparison, 2026-10-07

This is a literature-only EXPLORATION / NOVELTY_UNCHECKED step.
It completes the separate approval requested by history 069, without
calculating C, proving a sum bound or applying it to the word parameters.
The subsequent specialization should be classified REPRODUCTION unless
new evidence justifies a different qualified classification.

Christian Hercher, [*There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
JIS 26 (2023), Article 23.3.5, defines his map C as our shortcut T.
His T(n_i) is instead an odd-run reciprocal sum. Definition 6 and
Remark 7, printed p. 4, give T(n_i)<3/n_i for an actual odd run;
the proof uses only positivity and growth along that run. The further
3/X_0 comparison requires cycle minima exceeding verification height X_0
and must not be used for arbitrary finite words.

Theorem 16, pp. 10–11, states for a positive nontrivial m-cycle
with K odd inputs, L even inputs and delta=log(3)/log(2):

\[
0<(K+L)/K-\delta<\frac{\sum_i T(n_i)}{3K\log 2}.
\]

Its entire product/AM–GM/logarithm proof and odd-run partition were read.
Corollary 17 retains m/X_0. Theorem 27 and proof, pp. 19–20,
give the alternative sum bound 3K/(4X_0), still dependent on K.
The source qualifies its supporting estimates by X_0>765 (Remark 31).
Neither comparator bounds a finite concatenation by its two inputs.
Lemma 26's full case audit is not imported; Theorem 27 is only a comparator.
Theorem 16 may be cited later under closure, with repetitions justified
using L034's primitive-period convention. No represented-period formula
or improved bound is established in this source turn.

John Simons and Benne de Weger, [*Theoretical and computational bounds for m-cycles of the 3n+1 problem*](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf),
v1.44, 31 August 2010, section 1.2, printed p. 2, permits repeated
return periods. Lemma 4 and Corollary 5, p. 7, bound the positive
linear form Lambda=(K+L)log(2)-Klog(3) by the reciprocal sum of
all local minima, then by m/x_min. The complete chain-equation proof
was inspected; it does not identify two postspell inputs with all minima.
The previously assessed fixed-m exclusions remain inapplicable uniformly
in J_1,J_2. Their general theory needs no reproof for this test.

Olivier Rozier and Claude Terracol, [*Paradoxical behavior in Collatz sequences*](https://arxiv.org/html/2502.00948v2),
arXiv:2502.00948v2, 13 February 2025, Theorem 4.1, equation (10)
and complete proof, bound E/n using the harmonic mean h of odd input
occurrences. The displayed lower inequality requires a paradoxical
sequence; the upper inequality holds for any finite positive sequence,
as explicitly stated after the proof. The harmonic mean is an input,
not a uniform estimate of that mean from the two word junctions.
Thus this does not already supply TARGET. Its CST conjecture is not
an available theorem. Earlier parity-coding coverage is reused.

Sodelin, [*Guarded root descent after independently unbounded return spells and odd runs*](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001, live main retrieved
2026-10-07, sections 1–3, gives the actual-word identities and positive
growth offsets used in L020. Those passages and the parity guards
were inspected. The reviewed single-word and compensation assessments
already cover these inputs; no stronger descent theorem is required.
The necessary difference is to account for every odd input inside each
block, combine repeated blocks uniformly, and attach the terminal spell.
No bound is obtained by counting only the OOEO endpoints or by treating
two postspell words as two maximal odd runs. Keep the positive offsets;
an endpoint formula alone is not an internal-state estimate.

The search also found Sodelin's [issue-7 reciprocal-summability packet](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/effective-flashes/issue-7-reciprocal-summability.md),
live main retrieved 2026-10-07, read completely as a lead. Its claimed
infinite-orbit-set result concerns distinct values and orbit-dependent
constants; aperiodicity is used to pass to time occurrences. It does not
state the required uniform finite-word bound or cover cycle occurrences.
The underlying Garcia–Tal paper and linked MathOverflow argument were
not read this turn and are not imported. They are nonessential here.
No publication status or independent verification is inferred from the
packet's self-reported audit status.

## Search, duplicates and approval limits

Queries included `Collatz cycles sum reciprocals odd elements consecutive
increasing runs Hercher Remark 7`, `Collatz "OOEO" reciprocal sum`,
`Collatz cycle reciprocal sum geometric bound local minima`,
`Collatz cycle "sum" "reciprocals" "geometric"`,
`Collatz "postspell" "reciprocal"`,
`Collatz cycles odd run sum reciprocals Simons de Weger Lemma 4`,
`site:github.com/Sodelin/Collatz-Conjecture-Work "postspell" "reciprocal"`,
`Collatz "27/16" "sum"`, and
`Collatz "odd" "reciprocal sum" cycle bound Hercher`.
No inspected primary result matches the exact uniform two-input claim.
Other repository notes, forum posts and numerical examples appeared as
search results, but were not theorem inputs; unsuccessful discovery
does not establish originality or mathematical absence.

Local review read L020's identities and positive offsets and L021's
composition/actual-word guard ranges; L031's closure qualification and
L034's complete occurrence and repetition proof fix the later cycle scope.
Attempt 019, histories 057/066 and the prior cycle/run-count assessments
show no duplicate sum estimate. The boundary-guard failure stays stopped;
the new quantity does not reopen it. The latest recorded MathPrize
statement check on 2026-10-07 is reused for the unchanged exact goal.

SPECIALIZE approves exactly TARGET and SCOPE above for one later bounded
attempt. Import the cited single-run estimate and existing affine identities;
write the finite-word combination as a local specialization, not a reproof
of the general cycle theorem. Under closure use all odd occurrences and
retain any primitive repeat factor consistently. Compare an achieved C
with both generic all-minimum and odd-step estimates before claiming
usefulness. No Diophantine lower bound, integer-closure exclusion, cycle
existence, global-minimum assumption or universal entry has been approved.
The continuation/abandonment tests above remain unchanged.

No lemma, mathematical script or mathematical application was made here.
Full matching and supporting Mathlib coverage: not checked; no absence
claim or Lean declaration is asserted. Primary text extraction supplied
the load-bearing hypotheses and full relevant proofs; PDF screenshot
requests added no legible evidence and are not counted as inspections.
