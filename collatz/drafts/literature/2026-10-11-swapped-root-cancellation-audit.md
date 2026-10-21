# Swapped-root cancellation: critical-audit source coverage

TARGET: Critically audit L058's prime-five cancellation proof and complete exact certificate.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the six targeted queries and inspected primary coverage in 2026-10-11-swapped-root-five-adic-cancellation.md; searched the exact swapped-root drafts and histories 158–159, read L058 in full, L055's complete allocation, L056's coordinate/composition section, L057's prior audit scope and Attempt 028. No new external discovery was necessary for this unchanged order and modulus.
SOURCE_EVIDENCE: Reused inspected Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 and printed induction cases, pp. 228–229, and Mathlib PadicVal.Basic at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953: padicValRat.defn, padicValInt_dvd_iff and Rat.num_or_den_zero_padicVal with their complete proofs.
COMPARISON: Known formal affine composition and prime valuation cancellation cover all general inputs; the fixed allocation's exact residue table and two implementations need independent verification, not a new general theorem or a reproof of coding.
GAP: Essential source coverage is sufficient; independent verification of L058's nonzero hypotheses, complete table, exact certificate and limited stop implication remains outstanding.
REASON: This separate literature-only comparison approves the previously uncovered critical-audit scope while reusing ready sources; no mathematical audit or new arithmetic result is performed.
SCOPE: Only L058's unshifted root in L057's intact swap (0,6), fixed K=397573379 and N=630138897, moduli 5 and 25, complete certificate and prime-five cancellation implication; no larger modulus, other order/factor or realization test.
LITERATURE_REASON: The saved continuation required separate audit coverage approval; its essential affine and valuation hypotheses are compared here without repeating the ready discovery search.

## Relevance and bounded decision

The main gap is universal eventual descent. The intermediate target is
exactly TARGET. Its downstream use is a trustworthy decision about the
prime-five diagnostic for this one order, before selecting any materially
different arithmetic target. This cannot close the universal gap.

Continue with one separate RESEARCH/REPRODUCTION proof audit because the
sources cover the needed hypotheses. Accept the stop only if every relevant
certificate value and written contribution is independently verified with
nonzero numerator and denominator. Suspend or repair an unsupported claim;
do not enlarge the prime-power or permutation search. Attempt 028 remains
recorded pending that verification. A sound cancellation verdict abandons
prime-five exclusion of this order, not the overall research problem.

## Precise imported inputs and scope comparison

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
equations (2)–(4) and Lemma 2 supply the formal integer numerator,
chronological concatenation and unique fixed root for a nonempty binary
word with nonzero denominator. The inspected printed induction treats
one letter and an appended zero; the appended-one case is stated analogous.
Reuse that inspected proof scope. No rational-parity conclusion is needed.
Here 0 means E, 1 means O, length is N and odd count is K. Last maps act
on the left. Formal real affine identities do not require an actual integer
itinerary. Lemma 9's rotation/gcd comparison, already inspected in the
permutation assessment, does not decide this swapped numerator's valuation.

[Mathlib PadicVal.Basic, pinned source](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean)
supplies the general valuation/divisibility and reduced-fraction machinery.
The reused assessment inspected the full statements and relevant proofs:
`padicValRat.defn` identifies rational valuation with the integer numerator
and denominator multiplicity difference under the prime and nonzero
hypotheses; `padicValInt_dvd_iff` retains the zero alternative in testing
prime-power divisibility; `Rat.num_or_den_zero_padicVal` uses reduced-pair
coprimality. Their zero conventions must not replace a nonzero proof.
Prime 5 is the applicable prime. These are supporting results, not a
formal verification of this allocation. Full matching Mathlib coverage
is unchecked, and no Lean build is claimed.

The audit scope adds independent verification of existing evidence rather
than changing the mathematical assumptions assessed in the ready calculation
review. Reuse is therefore adequate. No source theorem is cited as proving
the exact residues or cancellation verdict for this particular allocation.
The needed specialization is finite exact verification; no new general
lemma or reproof is justified. No essential source is blocked. Unread
search leads listed in the reused assessment remain unused; failed searches
supply no novelty claim.

## Local overlap and essential audit obligations

Essential inputs are L055, L056, L057 and the claim being audited, L058.
L055 supplies all 25 triples, their totals and positive Delta. L056 supplies
the positive integral offsets in the unshifted coordinate. L057 fixes
order 6,1,2,3,4,5,0,7,...,24 with tail 166504412 attached to index 24.
Its separate audit settles the earlier modulo-five stop only. L058 claims
a decisive comparison at exponent 2; this source review does not certify it.
History 159 and Attempt 028 record that calculation and pending audit,
not an already completed independent verification. L056's literal-order
exclusion and Attempt 027's uniform-modulo-five stop remain intact.

The later audit must read complete relevant evidence in
`scripts/postspell-word-count/swapped-root-five-adic-cancellation-certificate.json`
and inspect the implementation
`scripts/postspell-word-count/test_swapped_root_five_adic_cancellation.py`.
It must independently check the full allocation and exact prefix/suffix
counts, every contribution modulo 25, chronological composition from O/E,
compressed-offset integrality and division by the unit 11, denominator
powers, agreement modulo 5, and the nonzero hypotheses before applying
valuation cancellation. Inspect all load-bearing values and failures;
previews, stored success flags or two implementations from the original
attempt are insufficient as the independent audit. Comparison with the
written table is required. The original cap 8 does not authorize an audit
search past the claimed decisive exponent 2.

Accept only the scope stated in L058: absence of prime 5 in the reduced
pair for this root. Integrality, other factors/orders/allocations, permuted
real guards, integer/parity/primitive realization, universal entry,
unrestricted cycles, divergence and eventual descent remain unresolved.
Published qualifications persist. No two-word closure converse is extended
to this 25-word formal allocation.

This step changes source readiness only. It writes no lemma or mathematical
script, performs no residue calculation and spends no mathematical
exploration budget. Independent critical audit is the sole next action.
