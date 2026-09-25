# 2026-09-25 — Mixed growing words and fixed-word repetitions

Step `collatz-2026-09-25-005-mixed-growing-word-bound` concluded ADVANCE
for a restricted repetition exclusion. The
[saved test](../drafts/2026-09-25-mixed-growing-word-bound.md) records
the gap, intermediate target, and threshold. The primary
[source](https://mathprize.net/posts/collatz-conjecture/) was rechecked
and retains the universal positive-integer target. Existing changes and
inactive branches were preserved; edits were confined to this notebook.

[L005](../lemmas/L005-mixed-growing-word-congruences.md) gives the exact
single residue class for every mixed word in {(2,1),(3,1)} and proves
that every intermediate run is legal. Its exact valuation bound limits
the number of repetitions of each fixed word from every positive start.
This excludes infinite eventually periodic itineraries in the alphabet,
leaving aperiodic itineraries, other block types, and universal eventual
descent unresolved. No complete candidate has appeared.

The requested uniform divergent least-start bound was not obtained. The
fixed-word bound has word-dependent coefficients and cannot be used
uniformly over all words. Exact enumeration through length 12 exhibits
plateaus and refutes transfer of the sharp single-type bound; the
[failed transfer](../ATTEMPTS/005-single-type-bound-for-mixed-words.md)
is preserved. These finite findings neither prove nor disprove divergence
of the minima.

The new repetition identities select two shifts, n+5 and 11n+19. This
motivates testing whether their joint valuations can handle arbitrary
switching, the case left open by fixed-word repetition. A decreasing
potential bounded below by log(n+5) on both block types would exclude
infinite paths within the alphabet; cross-type valuation gains may instead
obstruct it. This is a concrete new test, not a claim that a route to
universal descent is complete. Consecutive exploration turns without an
advance or informative negative remain zero after this single step.

Validation: `python3 scripts/mixed-growing-words/check_words.py` passed
all 8,190 words through length 12, their 24,570 representatives and lifts,
4,368 odd starts in full common residue periods, and 7,905 repetition
cases, including the first failed copy. The
[output](../scripts/mixed-growing-words/result.json) records 1,041,704
direct shortcut transitions. These finite checks supplement the proof;
they are not convergence evidence. Mathematical review checked the exact
run conditions, invertibility in each congruence, the parity of both
affine coefficients, positivity of H_w(n), and the fixed-word restriction.
L005 uses L002 alone as a prior mathematical input; earlier obstructions
are comparisons, not hidden premises. Mathlib coverage is not checked.

Documentation validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with five nodes, three edges, complete lemma coverage, valid links,
and compact overviews. The sole new DAG edge is the mathematical input
L002 to L005. Structural validation does not establish proof correctness.
