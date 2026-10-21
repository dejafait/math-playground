# Permutation-uniform modulo-five diagnostic: source comparison

TARGET: Decide whether modulo 5 excludes every permutation of L055's 25 fixed word triples.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Collatz affine composition permutations parity vector numerator modulo cycles; affine maps finite field multiset permutations dynamic programming composition prescribed counts; Collatz numerator permutations modulo 5 fixed parity words multiset affine; Collatz cycles parity vector permutations Halbeisen Hungerbuhler minimum maximum numerator. No inspected source decides this literal multiset.
SOURCE_EVIDENCE: Reused the fixed-witness-integer-realization assessment; inspected Halbeisen–Hungerbuehler (1997), section 2 pp. 228–229, equations (2)–(4), Lemma 2 and its induction cases; section 3 Lemma 4 p. 230 and section 5 Lemma 9 p. 238 with complete proof; inspected Cox–Ghosh–Sultanow arXiv:2101.04067v4, abstract and sections 1/2, PDF pp. 1–4.
COMPARISON: The exact chronological affine numerator and concatenation machinery are known; rotation/gcd and real-order comparisons do not decide arbitrary fixed-triple permutations modulo 5. A finite implementation specialization must supply the exact order-sensitive verdict and its completeness evidence.
GAP: No permutation verdict has been calculated. The next research step must verify any zero-residue order explicitly, or justify complete coverage of every ordering before claiming uniform nonvanishing.
REASON: Changed ordering scope required this literature-only comparison; essential affine coverage is now sufficient for a separate bounded REPRODUCTION attempt, without claiming originality or an integer cycle.
SCOPE: Exactly L055's 25 intact triples, fixed K=397573379 and N=630138897, unshifted integer numerator modulo 5 only; direct chronological composition, bounded explicit-order tests and, if needed, exhaustive multiset/state enumeration with a completeness proof.

## Inspected primary coverage

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Lemma 2 and equations (2)–(4), pp. 228–229, give chronological
composition and the integer numerator/fixed-point formula. The final map
acts on the left. Apply the affine identity to nonempty words with
nonzero denominator, without assuming integer realization. The proof checks
one-letter words and an appended zero; the appended-one case is stated
analogous. This input is already used in L056; no general reproof is needed.
Lemma 4, p. 230, compares distinct equal-length/equal-weight bit words
under prefix-sum ordering by a strict real numerator inequality. It supplies
no congruence verdict. Lemma 9, p. 238, assumes a nonzero bit word,
positive denominator and a rotation ending in one; it relates numerator
gcds over cyclic rotations to the denominator. Its proof treats the
ending-one identity and ending-zero doubling. Rotations do not cover
arbitrary rearrangements of whole triples. Neither statement resolves
this target. Any future use beyond this comparison needs a canonical
citation and applicability argument.

Cox–Ghosh–Sultanow, *Collatz Cycles and 3n+c Cycles*,
[arXiv:2101.04067v4, 16 April 2021](https://arxiv.org/pdf/2101.04067),
PDF pp. 1–4, reproduces affine/parity machinery in section 2 and describes
extremal cycle members and rotations in the abstract/introduction. The
inspected portion provides no fixed-triple multiset congruence theorem.
Later sections were not inspected and are not claimed absent of relevant
results. This source is a comparison, not a new load-bearing input.

Searches also returned repository claims, forum swap discussions and
arXiv:2607.24844 (*Christoffel words as extremal structures in Collatz
dynamics*). These remain unread leads, not theorem coverage. Search
failure does not establish novelty. Exact arithmetic on a specified
finite input remains an implementation specialization of the imported law;
no essential source access blocker remains.

## Local overlap and stopping evidence

Read L055's complete 25-row allocation and L056's coordinate/composition
proof and complete prime-five table. Reused
`drafts/literature/2026-10-11-fixed-witness-integer-realization.md` and
checked the targeted histories 150, 151 and 153 for ordering coverage.
L056 proves only literal-order nonintegrality. Attempt 026 stops exclusion
from the unchanged real subsystem via L055's witness; it does not stop
an order-sensitive integer diagnostic. Preserve both results.

## Approved bounded attempt and evidence standard

The main gap remains universal eventual descent. The intermediate target
is exactly TARGET. Its plausible downstream use is an integer-allocation
exclusion across all orders of this one multiset. Essential inputs are
L055's literal triples and L056's unshifted integer numerator convention,
compressed offsets and modulo-five denominator evidence. No new count
branch, parameters, allocation family or larger-prime search is covered.

First verify the 25 word data from the intact triples, including the unique
large tail; never move a tail independently. An explicit order with zero
numerator residue suffices to abandon uniform prime-five exclusion. Save
all 25 indices and full chronological residue evidence, and cross-check
against the imported integer concatenation law. A nonzero result on tested
orders alone cannot justify continuing to a uniform claim. If no zero is
found in the bounded tests, establish exact exhaustive coverage, for example
with a multiplicity-preserving finite-state search whose completeness is
proved in the research step. Grouping modulo-five maps must retain exact
multiplicities and a lift to original indices. A resource-limited search
without a witness or exhaustion is EXPLORATION, not uniform exclusion.
No such implementation, completeness proof or residue is derived here.

All nonzero numerators would extend the allocation obstruction. A verified
zero stops this diagnostic only: common divisibility by 5 does not prove
cancellation suffices or that the root is integral. Guards for the real
system after permutation, parity/valuation/residue realization, primitive
realization, other allocations/branches, entry, unrestricted cycles,
divergence and descent remain unresolved. No rational witness for a new
order is presumed. Full matching Mathlib/Lean coverage remains unchecked;
unknown coverage is not absence.

This completed step is LITERATURE/EXPLORATION, NOVELTY_UNCHECKED. It approves
coverage, not a mathematical result. The supervisor may separately approve
this changed assessment next turn; thereafter the default is the covered
bounded REPRODUCTION calculation. Mathematical exploration usage is zero
this turn; the preceding audit's one consecutive mathematical EXPLORATION
remains recorded.
