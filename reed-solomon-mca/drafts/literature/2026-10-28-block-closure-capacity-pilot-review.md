# Block-closure capacity pilot — proposed ready continuation

TARGET: Test a rank-growth versus incidence-capacity certificate for all deficient complete-block closures containing L167 rows 2 and 3.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step 532's exact-statement, stronger-result, terminology, implementation and failure comparison in 2026-10-27-incidence-constrained-block-closure-review.md; no matching twelve-row certificate or local closure implementation was found in the specified paths. No novelty inferred.
SOURCE_EVIDENCE: Borchmann CLA 2012 Theorems 1–2/Lemmas 1–3 pp. 10–14 https://ceur-ws.org/Vol-972/paper1.pdf ; Crowley–Simpson–Wang Algebraic Combinatorics 8(5) (2025), section 2.1/Example 2.2 pp. 1289–1290 https://connorgs.net/assets/papers/combinatorial_flats_and_schubert_varieties_of_subspace_arrangements.pdf ; reuse L109's exterior reduction and the exact capacity/conflict/weak-duality coverage identified in the completed comparison.
COMPARISON: The sources cover closure enumeration and fixed-mask capacities, not their proposed uniform coupling. Unlike L153 this retains complete kernels/spans and incidence histories; unlike L168 it must cover all deficient completions of one pair. L151's coding-dependent exclusion cannot be imported onto relaxed support families.
GAP: Justify a sound cover and rank-growth/capacity invariant giving total selected-row capacity at most eleven on every deficient closure containing the pilot, or preserve an exact twelve-row deficient witness or complete unresolved frontier.
REASON: Essential method coverage is available for one bounded creative test of the missing rank/incidence coupling. This is a proposed ready continuation awaiting separate approval next turn, not a mathematics invocation or an established certificate.
SCOPE: Exactly original L109 S=(1,8,12,18,22,27,33), J=(47,50,64,70,75,79,85,89,96), all 756 two-plus-two supports, entire six-by-21 blocks with original pivots/order, F_97 and arbitrary extensions, L167 rows 2 and 3 mandatory, distinct selected supports, pairwise intersections at most one and integer degrees at most four. No symmetry or nonlinear sufficiency.

## Intended result and bounded attempt

The main gap is uniform twelve-row exclusion. Fix the numerical pilot
rows {8,12,70,75} and {18,22,79,85}. Seek a structural coupling between
growth of their complete exterior-block span and the capacity for selected
linear degree-four supports. The desired bound is eleven total selected
supports, strictly below twelve. This is a conjectural test target.

Use block row spaces in F_97^21 and their generated spans. The proposed
closure mask consists of the original supports whose entire blocks lie
in the span; the later proof must check its correspondence with the cited
closure machinery and establish coverage of every deficient completion.
No closure identity or new capacity implication is proved in this file.
Import general closure enumeration rather than reproduce its theorem.
If a standard theorem alone supplies a step, state its precise specialization.

First seek an invariant or complete covering/pruning rule. Any finite
pilot then stops after at most 10,000 distinct generated spans; also stop
after 1,000,000 block-containment/extension tests or one exact deficient
twelve-support witness, whichever occurs first. Save the entire pending
frontier and actual counters when any cap is met. These are work limits,
not completeness bounds. No all-pair sweep, external solver installation,
API, additional locus classification or automatic repeat is approved.

Treat every generated rank below 21, including all lower-rank branches.
Closure members are optional supports, not events or mandatory selections.
Capacity on a current closure does not bound its larger deficient
descendants. Prove coverage before using maximal deficient closures,
rank pruning, or any other reduced cover. Account for the mandatory pair
and all integer degrees when bounding selectable subsets. Do not reject
a closure merely because its full mask violates degree or pair conflicts.
If merging histories, prove that candidate exclusions and residual capacities
are preserved or retain the histories separately. Greedy matroid exchange
and maximal-clique-only capacity pruning have no approval here.

## Evidence and decision

A successful exclusion requires an exact invariant proof or a complete
cover with independently checkable span/rank and capacity certificates,
all giving at most eleven total rows. Save full evidence under a dedicated
notebook scripts subfolder if implementing; print actual/required bounds,
failure count and paths. Verify full ranks/kernels and complete relevant
certificates, not previews. A rank-deficient twelve-row witness must list
all supports, exact integer degrees and intersections, complete blocks,
and a complete nullspace/rank certificate independently reconstructed.

Such a witness stops the exterior-only exclusion claim but supplies no
decomposable plane or coding realization. A feasible fractional relaxation
only defeats the chosen dual certificate, not integer exclusion. A branch
with twelve merely possible candidates is not a witness. A capped run or
unproved covering/pruning rule is unfinished exploration; save it honestly
and reassess this mechanism without silently discarding the frontier.

Downstream use is a conditional exclusion for this pair, followed only
after separate assessment by possible extension to C152a's extracted
but unspecified pair. Essential local inputs are L109 and L167; L153
is an optional audited initial-pair check, not a new rank stratification.
L125/L151/L154/L162/L168 and ATTEMPTS/041,043,048,055 constrain interpretation,
not symmetry transfer. No cross-notebook result is used.

Coding use still requires L104/L086/L010, F=F_(97^20), k=8, unit
multipliers, the pinned 1/4<=delta<5/16 cell, both coefficient syndromes
in U_S, sixteen finite events, t=0, nonzero-polynomial D and locators,
arbitrary original weights/chart and all inherited finite-certificate
qualifications. Decomposability, exact projection ranks, weights, full
event completion, arbitrary representation and challenge equivalence
remain unresolved. Full matching Mathlib coverage is not checked.

The proposed purpose is proof_attempt/creative: discover and test an
instance-sensitive rank/capacity invariant at the central twelve-row gap.
Merely implementing known closure enumeration is reproduction and must
be reported by its actual task type rather than as creative progress.
