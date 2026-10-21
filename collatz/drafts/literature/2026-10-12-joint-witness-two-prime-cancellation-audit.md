# Fixed joint witness two-prime cancellation: proposed audit coverage

TARGET: Critically audit L061's fixed-order prime-square cancellation at 5 and 431, including both complete evaluations and the reduced-denominator conclusion.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused focused discovery in the approved prime-square assessment; read all of L061, L055's allocation/count range, L056/L057's coordinate/formula ranges, Attempt 030, histories 169–171 and the predecessor audit/cancellation assessments. No completed independent L061 audit occurs in these inspected records.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 and its complete printed induction, pp. 228–229; reopened pinned Mathlib PadicVal.Basic enclosing hypotheses and complete proofs at lines 181–200, 342–350 and 633–644.
COMPARISON: Known formal affine composition and prime-valuation cancellation cover the unchanged order and conclusion mechanism; the remaining specialization is independent verification of both complete finite evaluations and their precise local implication.
GAP: Essential source coverage is sufficient; complete independent arithmetic verification, transcription comparison and applicability audit remain pending, including reduced numerator as well as denominator.
REASON: This literature-only step approves the saved critical-audit scope without certifying L061, repeating its calculation or reopening the stopped two-prime diagnostic.
SCOPE: L061 only; intact swaps (0,8),(7,12), row 24 fixed, tail 166504412, K=397573379, N=630138897, unshifted Phi_pi/Delta, moduli 25 and 185761; no new factors, powers, orders or realization tests.
LITERATURE_REASON: The saved audit was REVIEW_REQUIRED; its new independent-verification and reduced-pair scope needs source comparison, reusing ready discovery and theorem coverage.

Reuse `drafts/literature/2026-10-12-joint-witness-prime-square-test.md`
where its exact hypotheses remain adequate. This approves source scope
only, without certifying mathematics or introducing a calculation.

Essential input IDs: L055 supplies all 25 triples, totals K=397573379,
N=630138897 and positive Delta; L056 supplies positive integral unshifted
offsets; L057 supplies the chronological permutation formula; audited
L060 supplies the fixed swaps/order and common zeros. L061 supplies the
two new full square evaluations and the proposed conclusion. Inspect its
complete canonical statement/proof and the whole relevant certificate
fields before verifying them, not only previews.

Approved audit scope: exactly swaps (0,8),(7,12), row 24 fixed with tail
166504412, the unshifted root Phi_pi/Delta, and moduli 25 and 185761.
Check all 25 word triples, lifted quotients, full prefix/suffix exponents,
weighted contributions and composition states at both moduli, total
denominator powers, all trial-divisor primality evidence, positive/nonzero
premises and all stored comparisons/failures. Compare the complete written
tables with an independent arithmetic representation and verify the
valuation and reduced-pair conclusion under the exact cited hypotheses.
No higher powers, other factors, order searches or realization claims are
part of the approved audit.

Attempt 030 stops the two-prime diagnostic for this order; Attempts 027–029
and the other orders' exclusions remain preserved. Integer/parity/exact-tail/
primitive realization, permuted real guards, other orders/allocations,
entry, unrestricted cycles, divergence and universal descent remain
unresolved. Supporting Mathlib declarations were inspected previously;
full matching coverage and a Lean build remain unchecked. This document
approves a continuation, not its mathematical correctness.

## Relevance and continuation test

The main gap is universal eventual descent. The intermediate target is
exactly TARGET. Its downstream use is reliable evidence about which
denominator obstructions remain for this fixed order, informing a materially
different later target. The universal quantifier and all realization gaps
remain untouched. Continue with one separate RESEARCH/REPRODUCTION proof
audit after approval. Accept the local diagnostic stop only if every
load-bearing entry agrees with independent verification and all imported
hypotheses hold; otherwise repair or suspend the affected claim. Two
agreeing generator routes and stored pass flags alone are not an audit.
Do not extend or reopen the stopped two-prime diagnostic.

## Precise primary coverage and comparison

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published PDF, section 2 equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The formal binary-word identity composes the last map on the left.
Its printed induction checks length one and appended zero, stating
appended one analogous. Only the affine identity and fixed-point formula
for a nonempty word with nonzero denominator are needed; rational parity
or cycle assertions are not imported. Here bits 0,1 mean E,O, length is
N and weight is K. Intact permutation preserves these counts. L056/L057
supply the compressed offsets and unshifted application. A general reproof
would add no necessary coverage.

[Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean):
`padicValRat.defn`, lines 181–200, assumes prime p and nonzero q represented
by integer n/d; its proof cancels the shared reduced-pair factor and checks
finite multiplicities. `padicValInt_dvd_iff`, lines 633–644, assumes prime
p and includes the zero branch, reducing to absolute-value divisibility.
`Rat.num_or_den_zero_padicVal`, lines 342–350, assumes prime p and uses
reduced-pair coprimality. The definition at lines 111–118 expresses rational
valuation as reduced numerator valuation minus denominator valuation.
These cover the mechanism. Both integers and q must be nonzero; valuations
defaulting to zero at zero cannot certify finite positive multiplicities.
The research audit must check these premises and primality independently.

The complete cited proof cases and enclosing hypotheses were retrieved,
not inferred from snippets. No essential source is blocked. Reuse the
approved prime-square assessment's focused queries and theorem comparison;
no new broad search was needed for unchanged machinery. The inspected
L060 audit concerns common zeros; L058/L059 concern the different swap
(0,6), so none duplicates this audit. Search failure establishes no novelty.
The supplied exact goal is unchanged, with primary target-statement coverage
recorded by the reused predecessor assessment.

## Independent evidence specification

Read the complete original generator before auditing and inspect complete
selected fields of
`scripts/postspell-word-count/joint-witness-prime-square-certificate.json`.
This source turn inspected generator declarations and field scope without
executing it or loading its arithmetic certificate. Navigate with the shared
JSON inspector, then use `--full` for selected load-bearing fields; previews
cannot certify the result. Review every original check and failure, including
the claimed 223 comparisons. Compare both complete written tables with
independent output, not just final residues or the summary verdict.

A separately implemented normalized affine evaluator over these odd moduli
offers a different representation using the unit 2. Its relation to stored
integer numerator triples must be justified in the research audit. Do not
use the generator as its own verifier or merely rerun it. Verify all word
triples, lifted quotients, raw prefix/suffix exponents, contributions,
previous/resulting states, sums and denominator powers, plus every trial
divisor and positive/nonzero premise. Preserve original evidence and save
full independent checks under the existing topic directory; print only
actual/required bounds, failures and paths. No script is written this turn.

Check both reduced-pair conclusions under the exact prime/nonzero
hypotheses. Complete cancellation at these primes does not establish
complete cancellation of Delta. No two-word closure converse or primitive
integer-cycle theorem applies to this rational root. Full matching Mathlib
coverage and a Lean build remain unchecked; unknown coverage is not absence.

Completed kind/classification: LITERATURE/EXPLORATION, NOVELTY_UNCHECKED.
This is new audit-scope preparation, not mathematical verification or
progress beyond inspected sources. No lemma, mathematical script,
certificate, DAG or main argument was changed. Mathematical exploration
usage is zero; the sole continuation is TARGET.
