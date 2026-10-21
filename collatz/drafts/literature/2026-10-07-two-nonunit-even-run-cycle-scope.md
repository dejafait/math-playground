# Two non-unit even runs — completed source comparison

TARGET: Assess published cycle restrictions for exactly two non-unit even runs and their applicability to L031's unbounded two-postspell closure language.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Targeted even-run, exponent>=3 and few-descents searches found Brox's primary first-page definition/theorem, but no inspected theorem counting only non-unit shortcut even runs; local L031/L034, Attempt 019 and the prior cycle assessment were checked for duplicates.
SOURCE_EVIDENCE: Brox, Acta Arithmetica 92 (2000), 181–188, indexed complete printed p. 181, equation (1.1), cycle/descending definitions and Theorem 1.1 statement; Hercher, JIS 26 (2023), Article 23.3.5, Definitions 5/6, Remark 7, Lemmas 8/9/11 with complete relevant parity and even-run cases, printed pp. 3–7, and Theorem 16 with full proof, pp. 10–11; prior Simons–de Weger comparison reused.
COMPARISON: Brox counts exponents>=2, including every isolated shortcut E, rather than only exponents>=3; Hercher's one-even-step versus multiple-even-step cases do not eliminate the full minimum count. No applicable uniform two-long-tail exclusion was located.
GAP: No checked result excludes L031's positive integer closure with unbounded J_i,H_i,a_i using only the count of long tails; Brox supplies a different conditional finiteness statement, and its later proof is unread and not imported.
REASON: Park the source route based only on two long tails after a concrete parameter mismatch; propose a separately reviewable reciprocal-sum target rather than another guard audit, generic cutoff or source retry.
SCOPE: Positive actual closed W_1 W_2 of L031/L034 with J_i>=2, H_i>=3, a_i>=0 congruent to 2 modulo 18, n>1 and positive odd residue-20 junctions; retain nonminimal periods and all unbounded parameters.
LITERATURE_REASON: Changed comparison parameter from total local minima to exactly two even runs longer than one; existing generic-minimum coverage supplies no theorem-level comparison for that scope.

## Proposed comparison and test

The main gap remains universal eventual descent. The proposed intermediate
target is source coverage for excluding or further restricting the
unresolved two-postspell closed language through its even-run structure.
A theorem uniform in the number of intervening length-one even runs
could constrain the larger J_i region left by L034. This downstream use
does not address divergent orbits, other cycles or universal entry.

Essential local inputs to inspect narrowly are L031's exact closure
hypotheses and L034's audited counting proof. The proposed scope retains
the isolated even inputs of OOEO and the two terminal even tails; do not
treat two long tails as two local minima, assume distinct junctions or
remove repeated one-word representations. The existence of positive
integer closure is unresolved, not an available input.

Check primary theorem statements and essential proof cases for cycles
with a bounded number of non-unit even runs, using their actual standard
terminology once located. Compare the exact allowed odd-run patterns,
positivity, primitiveness and all parameter limits. Reuse inspected
primary material where adequate. A bounded local-minimum theorem alone
does not fill the uniform gap; a discovery snippet is not coverage.

Continue to a later mathematical turn only if a precise applicable
known theorem, an identified specialization difference or an independently
testable uncovered inequality has adequate source comparison. If the
only results are generic finite-minimum cutoffs, or hypotheses exclude
these words, record that evidence and choose a different target. No
larger empty screen or repeated automatic-boundary test is proposed.

Attempt 019 preserves the automatic-guard failure. L034 and its completed
audit preserve the published minimum cutoff. This completed comparison
neither reopens those mechanisms nor asserts novelty. Mathlib coverage
for the changed run-count scope is not checked. No matching theorem was
imported and no dependent mathematics was attempted this turn.

## Completed evidence and applicability

T. Brox, [*Collatz cycles with few descents*](https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9229.pdf),
Acta Arithmetica 92 (2000), 181–188, DOI 10.4064/aa-92-2-181-188,
printed p. 181, defines the odd map by 2^k(x) T_1(x)=3x+1.
Its descending elements have k(x)>=2. Cycles consist of distinct odd
integers; Theorem 1.1 states finiteness for delta(Gamma)<2 log |Gamma|.
This is neither exclusion of all such cycles nor a theorem using the
number of k(x)>=3 entries. Because O already includes one halving, an
isolated shortcut E contributes k=2, and a tail E^a contributes k=a+1.
Thus the internal even runs counted in L034 cannot be dropped from
Brox's parameter. Repeated representations require primitive-period
quantities; two named tails do not justify substituting delta=2.
This comparison uses the primary definitions and statement, not a proof
of finiteness. The later proof was not accessible and is not imported.

Christian Hercher, [*There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
JIS 26 (2023), Article 23.3.5, Lemma 9, pp. 5–6, treats a maximal
odd run followed by at least two even steps: a smaller positive
(n_i-1)/2 merges with its orbit. Both odd-run parity cases were read.
Lemma 11's proof, pp. 6–7, distinguishes one even step from at least
two, but its sum estimates still use all minima. Neither statement
asserts that the smaller companion is a member of the cycle or smaller
than its global minimum. Theorem 16 and full proof, pp. 10–11, retain
the full sum S of reciprocal odd states and bound the positive gap
between (K+L)/K and log(3)/log(2) by S/(3K log(2)). Remark 7,
p. 4, bounds each maximal odd-run contribution by 3/n_i. These are
inspected source inputs and potential future tools, not a derived
two-postspell sum bound or a new exclusion here.

L031/L034 were read completely. Attempt 019's automatic-guard failure
and the completed minimum-cutoff audit remain unchanged. The prior
cycle assessment supplies the Simons–de Weger fixed-m comparison;
it cannot be applied with m=2. No known theorem is reproved. The
current [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07, was checked on 2026-10-07: it still quantifies over
every positive integer for the original 3n+1/even-halving map.

## Bounded discovery and access record

Queries included `Collatz cycle "even" "runs" "two"`,
`Collatz cycles "non-unit"`, `Collatz cycles "even runs" theorem`,
`Collatz cycles "two" "descents" theorem`,
`Collatz cycle "exponents" "at least 3"`,
`Collatz cycles "few" "large" "exponents"`,
`Collatz cycles "even blocks" restrictions`, and
`Collatz cycles "exactly two" "exponent"`. Brox-specific queries
also tested `"Collatz cycles with few descents" "Lemma 2.2"`
and `"Collatz cycles with few descents" "Theorem 3.2"`.
The primary PDF's complete first page was returned by search indexing;
direct browser opens, the publisher download and one shell download
failed (browser internal errors; shell DNS failure). No later Brox proof
case was inferred from snippets or a secondary summary. Its incompatible
count is already explicit on the accessible first page, so retrieving
the rest is not essential to the route rejection and is parked.

Other repository, preprint and forum hits were discovery only; none
was promoted to a theorem or a dependency. No adequate uniform match
was found in this bounded search; this is not a novelty claim or proof
that none exists. Mathlib coverage remains not checked.

## Decision and separate continuation

Completed LITERATURE/NOVELTY_UNCHECKED, outcome NEGATIVE: the primary
parameter mismatch changes the routing decision. It does not establish
a cycle restriction beyond the checked sources, or mathematical progress
toward universal descent. No lemma, mathematical script or certificate
was written. PROOF.md and DAG.md need no changes.

Park a theorem search based only on the two long tails. The distinct
proposed target is an explicit parameter-independent bound on S in
terms of the two word inputs, for actual finite concatenations first,
with closure imposed only for the downstream Theorem 16 application.
The [separate pending assessment](2026-10-07-two-postspell-reciprocal-sum.md)
records exact scope and the test; it is REVIEW_REQUIRED, not approved
mathematics. Other cycles, divergence, entry and eventual descent remain
open. No mathematical exploration turn is spent or counter reset.
