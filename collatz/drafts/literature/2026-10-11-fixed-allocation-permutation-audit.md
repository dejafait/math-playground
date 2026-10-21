# Explicit permutation diagnostic: critical-audit source coverage

TARGET: Critically audit L057's explicit permutation and the failure of uniform modulo-five exclusion.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the four targeted permutation/affine queries and theorem comparisons in 2026-10-11-fixed-allocation-permutation-mod-five.md; inspected the full L057 proof, L055's complete allocation, L056's coordinate/composition section, Attempt 027 and histories 154–155. No new discovery search was required for the unchanged fixed multiset.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), published PDF section 1 p. 227 and section 2 pp. 228–229, equations (2)–(4), Lemma 2 and every printed induction case; inspected the generator's input and evaluation scope without running or independently verifying it.
COMPARISON: Known chronological affine composition covers the formal numerator and fixed denominator; the local explicit order, complete residue evidence and limited negative implication require a separate independent audit, not a new general theorem.
GAP: Coverage is sufficient; independent verification of the intact triples, all chronological contributions, implementation/certificate and implication remains outstanding. No mathematical audit is completed here.
REASON: This separate literature-only turn approves the saved critical-audit scope for a later RESEARCH/REPRODUCTION step; it does not certify L057 or reopen the stopped uniform diagnostic.
SCOPE: Only L057's swap of intact indices 0 and 6 in L055's fixed 25-triple multiset, unshifted numerator modulo 5, fixed denominator and complete finite evidence; no other primes, valuations, allocations or real-system feasibility tests.
LITERATURE_REASON: The newly proposed L057 critical audit had REVIEW_REQUIRED coverage; this turn checks its essential formal-composition hypothesis and evidence scope while reusing ready permutation literature rather than repeating discovery.

## Main gap, intermediate use and discriminating test

The main gap remains universal eventual descent. The exact TARGET is an
independent critical audit of one negative arithmetic diagnostic. A sound
audit would distinguish a stopped uniform modulo-five route from L056's
still-valid literal-order obstruction and guide later diagnostic selection.
It cannot supply unrestricted cycle exclusion or descent.

Continue with the saved proof audit if its source and evidence scope is
adequate, as this comparison finds. Retain L057 only if independent
arithmetic agrees with every load-bearing record and the implication stays
within uniform nonvanishing. Repair a concrete discrepancy if possible;
otherwise suspend the unsupported claim. Successful generator flags or
bounded previews alone do not pass this test. No new diagnostic follows
automatically.

## Primary theorem and applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
section 2, equations (2)–(4) and Lemma 2, pp. 228–229.
The source defines branch compositions on real inputs in chronological
order, with the last branch acting on the left. It supplies the integer
numerator recurrence, explicit sum, concatenation and affine fixed-point
formula. The induction checks length one and appending zero; the
appended-one case is stated analogous. For the unique fixed root use a
nonempty word with nonzero denominator. The rational parity conclusions
of Lemma 1 are outside this audit's needed input.

The proposed audit uses exactly the same O/E convention, length N and
odd-letter count K. L055 supplies the nonempty literal allocation and
positive denominator; intact permutations preserve these totals. L056
supplies the unshifted compressed offsets. Formal affine composition
does not require integer realization. These are applicability checks for
existing inputs, not a new local derivation. No general coding reproof
is warranted. L031's two-word closure converse must not be extended to
twenty-five words.

## Independent audit scope and evidence

Essential inputs are L055's complete indexed allocation, L056's formal
integer offsets and denominator convention, and L057's complete order,
proof and table. Verify all 25 index multiplicities and the intact final
tail 166504412. Check all exact prefix/suffix exponents, every weighted
contribution, both complete numerator evaluations and the written-table
match using independent residue arithmetic.

Inspect complete relevant evidence in
`scripts/postspell-word-count/fixed-allocation-permutation-mod-five-certificate.json`
and `scripts/postspell-word-count/fixed-allocation-permutation-written-table-check.json`.
Review the generator
`scripts/postspell-word-count/test_fixed_allocation_permutation_mod_five.py`,
including literal-table parsing, tail assignment, integer-triple
composition, binary powering, six-swap stopping and failure recording.
This turn read its input/evaluation scope only; it did not execute a
mathematical check or independently certify a record. The later audit
must inspect the entire relevant arrays, not just hashes or pass counts.
If reproduction is useful, save full audit evidence under the existing
topic directory and print concise actual/required values and failures.

The claimed implication needs one explicit zero-residue order, rather
than exhaustive permutation coverage. Common divisibility by 5 must not
be promoted to full cancellation or integrality. No permuted real-system,
parity, valuation, residue or primitive-realization guards are supplied.

## Reuse, duplicates and limitations

The predecessor permutation assessment already compares primary real
numerator ordering and cyclic-rotation/gcd results; neither comparison
decides arbitrary intact-triple orders modulo 5. Its uninspected leads
remain unused, and unsuccessful searches do not establish novelty.
L056's earlier critical audit covers its literal order, not this new
table. History 155 records a transcription check, explicitly not an
independent critical audit. Thus the proposed audit does not duplicate
an already completed independent review.

Preserve L055/L056 and Attempts 026/027. The real-subsystem stop and
uniform-prime-five stop are distinct and neither prohibits this audit.
Full matching Mathlib/Lean coverage remains unchecked; unknown coverage
is not absence. Inherited published qualifications remain unchanged.
Other allocations/branches, entry, unrestricted cycles, divergence and
universal descent remain unresolved. No cross-notebook input is used.

This source review is LITERATURE/EXPLORATION, NOVELTY_UNCHECKED. It approves
coverage only, leaving L057's correctness for the separate REPRODUCTION
audit. It spends no mathematical exploration turn; the recorded counter
remains zero after the preceding informative NEGATIVE.
