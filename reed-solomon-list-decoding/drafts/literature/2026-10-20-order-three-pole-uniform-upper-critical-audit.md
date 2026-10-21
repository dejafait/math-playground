# Critical-audit coverage for L100

TARGET: Critically audit L100's uniform upper certificate, including character extension, all exceptional powers, sieve normalization and the exact threshold comparison.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the uniform-fiber and phase-sensitive assessments; compared L100, history/369-370 and ATTEMPTS/083, then narrowly reopened the same two versioned primary sources for theorem hypotheses and proof cases. No new discovery search was needed.
SOURCE_EVIDENCE: Rechecked Li-Wan 1806.00152v3 Section 4 setup, Lemma 4.1 and complete proof (4.1); Li-Wan 1507.06329v1 Section 2 setup, Theorem 2.1, Corollary 2.2 and cycle generating identity in Lemma 2.6 proof. Versions and applicability are recorded below.
COMPARISON: L100 specializes known tools to K=H times (E,+)^2 and obtains a cap strictly below the ambient threshold; it is a local reproduction, with no novelty claim or arbitrary-center safety theorem.
GAP: Source coverage is adequate for the independent audit; the complete Fourier group, extension/twist normalization, every character-power case, exceptional cancellation, factorial and strict endpoint still require that mathematical audit.
REASON: This separate coverage review resolves the proposed audit scope without rederiving the specialization; the completed construction remains intact and no audit verdict is claimed.
SCOPE: Exactly L100 with Q=65537, n=1024, 67-subsets, modulus X^3, constant-H residue subgroup, L099's entire-list interpretation for all m>=1 and T=Q^28/2^128. No other poles, new estimates or arbitrary-center claim.

The main gap remains arbitrary-center 67/68 safety, not the validity of
this particular family as a witness. The intermediate review target is
L100's entire uniform bound, with plausible downstream use of retaining
or correcting the family exclusion before routing elsewhere.

Essential inputs: C012a's field and generator, L099's audited entire-list
dictionary, L100's full proof, foundations/01–02 and the prior
[uniform-upper assessment](2026-10-20-order-three-pole-uniform-fiber-upper.md).
The construction evidence is in
`scripts/coefficient-fibers/order-three-pole-uniform-upper-results.json`
and `scripts/coefficient-fibers/order-three-pole-uniform-upper-verification.json`.
These paths are notebook-relative. The two arithmetic scripts do not
replace a symbolic proof audit. No essential source is unread for the
scoped audit. Reuse these inspected tools without another discovery search.

An approved audit should reconstruct the unit decomposition and all
characters, check the factor 1/64 and x=0 branch in every complete sum,
verify nontriviality for all j=1,...,67, isolate all ten exceptional
constant-character orders, and independently derive the unordered sieve
normalization and coefficient. Check the full exact U and T comparison,
including c outside H, empty fibers and ambient-extension/tuple scope.
Continue the family exclusion only if every essential step passes;
otherwise identify and repair or retract precisely the failing claim.
Do not infer arbitrary-center safety, a sharp boundary or novelty.

Mathlib coverage is not checked, as recorded in L100; that is not
evidence of absence. No cross-notebook input is proposed. This review supplies SPECIALIZE coverage for a later critical audit;
it does not perform that audit or certify L100.


COVERED_TARGET: Critically audit L100's uniform upper certificate, including character extension, all exceptional powers, sieve normalization and the exact threshold comparison.
LITERATURE_REASON: The new independent-audit scope required a separate comparison; only its already inspected character and sieve hypotheses were reopened, with no new bound or broader search.

## Completed source comparison — 2026-10-20

Li and Wan, *Distance Distribution in Reed-Solomon Codes*,
[arXiv:1806.00152v3](https://arxiv.org/html/1806.00152v3#S4),
2019-07-30, Section 4 Lemma 4.1, printed pp. 9–10: the setup allows
any positive-degree monic modulus and extends a unit-group character by
zero on nonunits. The first bound requires nontriviality; squarefreeness
and triviality on field units are not hypotheses of that bound. The
proof covers the vanishing high-degree coefficients and the
L-polynomial reciprocal-root estimate. The separate cumulative bound
has an extra trivial-on-field-units hypothesis and is not needed here.
This covers the source theorem used by L100, rather than its restricted
subgroup sum. The later audit must check each twist and power before
applying it with modulus X^3 and monic degree one. No Weil-bound reproof
or stronger character theorem is authorized or needed.

Li and Wan, *Counting polynomial subset sums*,
[arXiv:1507.06329v1](https://arxiv.org/html/1507.06329v1#S2),
2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5, permit arbitrary
finite domains and complex weights; conjugacy grouping requires a
symmetric domain and weight. The sign counts all cycles, including
fixed points. The general cycle exponential identity appears in the
Lemma 2.6 proof (printed pp. 6–7); its subsequent special coefficient
inequality is not the input being imported. These statements cover the
weighted sieve tool, not a prepackaged multiplicative-residue fiber
bound. Its ordered-to-unordered factor and L100's precise coefficient
remain audit obligations. Import these identities without reproof.

The strongest applicable known inputs are consequently the same tools
already assessed for construction. No source states the complete local
proper-subgroup cap or its RS interpretation. SPECIALIZE, rather than
IMPORT, preserves that distinction. Reading L100 here only identifies
claims and the independence plan; no new symbolic derivation, arithmetic
certificate check or critical-review verdict was performed.

## Duplicate/failure comparison and bounded continuation

History/370 records construction and its two arithmetic reconstructions,
not an independent proof audit. History/369 parks a different
phase-sensitive lower proposal; ATTEMPTS/083 parks averaging alone.
Neither failure bars verifying L100's upper certificate. The prior
assessment already distinguishes the stopped residual-energy routes;
they are not reopened. No new quantitative target is proposed.

Next turn may perform one coherent proof audit, including a bounded
independent checker if useful. Reconstruct the character enumeration,
all 64 twists, every power 1 through 67 and all ten exceptional orders;
check the subgroup denominator and factorial independently of the
constructor. Inspect the complete decisive values in both existing
certificates and compare the manuscript and threshold by exact
arithmetic. Recheck L099's imported scope only as needed for the
all-m consequence, preserving foundations/01–02's ABF qualification.
Do not treat small-field examples or rerun success as symbolic proof.
A concrete failing assertion requires a precise correction or withdrawal;
new character estimates or other families require separate assessment.

This completed coverage review is EXPLORATION / LITERATURE /
REPRODUCTION, not a new mathematical advance. The newly ready audit
receives separate supervisor approval next turn. The continuation test
above remains unchanged. No lemma, script, DAG edge or assembled
argument was changed. Mathematical exploration usage remains 0/3;
independent arbitrary-center 67/68 safety, the exact boundary and ABF
comparison remain open. No essential source blocker remains for this audit.
