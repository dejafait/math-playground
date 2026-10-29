# Step 525 — source scope for the separate L126 audit

2026-10-27. Literature-only comparison for the exact TARGET in
`drafts/literature/2026-10-27-l126-critical-audit.md`.
This note approves coverage, not any equality in L126. No new
mathematics, proof audit verdict or scalar calculation is supplied.

## Reuse, duplicates and recorded failures

Reused the step-523 construction assessment and its source note,
including its exact queries, general-prime-power comparison and
Gonzalez--Rotger square-free limitation. Read L126 in full to identify
its claims, the L123/L124 hypotheses and relevant projection/descent
passages, and their step-515/520 audit records. ATTEMPTS/060 preserves
the selected-branch/full-Hecke-fiber obstruction; L125 remains
unaudited motivation, not an input. No exact raw replacement theorem
was identified in the sources inspected; this is no novelty claim.
No broad search or cross-notebook input was needed.

## Primary theorem scope actually checked

**Voight**, *Quaternion Algebras*, GTM 288 (Springer, 2021),
Chapter 30, pp.541--567,
<https://doi.org/10.1007/978-3-030-56694-4_30>.
Retrieved the publisher HTML on 2026-10-27 and read §§30.5.1--30.5.3,
the complete proof of Proposition 30.5.3, (30.6.2), and the statements
and complete proofs of Lemmas 30.6.3/30.6.9. The local base is a
complete DVR with finite residue field; embeddings are optimal algebra
embeddings of a quadratic order in a separable quadratic algebra.
Maximal split orders use 30.5.3(a); the division maximal-order case
uses 30.5.3(b). The latter proof explicitly identifies the full
normalizer with the division algebra's units. General positive
Eichler exponent uses 30.6.3 and 30.6.9(a),(b), with the unit
discriminant condition retained. No odd-characteristic hypothesis
appears in those cited cases; 30.6.9(c) has an additional lifting
condition and is not licensed by dropping that condition.
The proof text supplies the division normalizer assertion even where
the displayed embedding-count formula is rendered as an image.

**Fornea**, *Plectic Heegner classes*, arXiv:2603.28327v2,
13 April 2026, <https://arxiv.org/html/2603.28327v2>.
Retrieved the versioned HTML on 2026-10-27. Read the conductor/residual
hypotheses and (2), local level definitions in §2 and §2.2,
§2.0.1/(7), (22)--(23), Proposition 3.8 with its proof and Corollary
3.9, (34)--(35), Corollary 4.15 with proof and (63), Proposition
4.18 with full proof, Theorem 4.22 with full proof including (65)--(66),
and §4.4/(67)--(68) with the proof of Corollary 4.24. The earlier
vanishing, flatness and finite-descent coverage is reused from the
audited L123/L124 inputs, not independently re-audited here.

## Coverage map and remaining audit obligations

| L126 claim to audit | Available source scope; what remains local |
| --- | --- |
| Tame embedding comparison and (2) | Voight covers maximal orders and general split Eichler exponents. Match (2) of Fornea to the maximal CM order, verify both split orientations at exponent two and all good tame cases, then check centralizers, almost-everywhere choices and the fixed original n. |
| Full tame level, discarded coordinates | Fornea's §2 definitions distinguish the full Eichler unit group from the deep p subgroup. Check actual unit membership at every discarded inert place; no extra orientation subgroup or omitted rational coordinate may be assumed. |
| Raw (5)--(7) | Corollary 3.9 specifies the original finite cells and normalized maps; (34)--(35) specify the p domain/action. §2.0.1/(7) supplies continuous integration for separated complete modules. The eigenvector/determinant cancellation, rational-cell signs, compact torus action and pushforward identification remain to verify. No raw equality follows merely by invoking Proposition 4.18. |
| Full quotient and (8) | §4.4 explicitly compares the truncated and full torus quotients under the inert/coprime hypotheses. Equations (67)--(68) specify a representative sum. Check L126's original list and each multiplicity, stabilizer and representative change before reindexing. |
| Projected domain and descent | (63) has an invariant domain, and Theorem 4.22/Corollary 4.24 concern the specialized construction. Conditional on a valid raw equality, inspect its transfer using the existing L123/L124 domain, injective restriction and rational descent; do not apply projection to cells or identify distinct Galois lifts. |
| Degree-one geometry | The source's actual level definitions are available. Verify normalization and inverse at every level. No compatibility with a Hecke eigensummand or scalar eigenvalue is supplied by a degree statement. |

The key scope boundary is visible in the source proofs: Proposition
4.18 uses Lemma 4.7 and Theorem 4.13 after kernel changes; Theorem
4.22 removes local constant terms using Theorem 4.13. These are not
statements of invariance of raw measures or of L126's full raw moment.
The source supplies the framework for checking L126's stronger claim,
not the claim itself. Its elementary specialization must therefore be
checked rather than replaced by a citation or a reproof of Fornea.

## Decision and bounded test

SPECIALIZE for the unchanged audit target. No essential source remains
blocked. Accept L126 only after every case of (2), (5)--(8), both
projection domains and the finite-extension descent pass. On the first
unsupported equality, preserve the preceding valid partial result
and record the exact failed hypothesis; do not assume a scalar or
repair the gap with a full Hecke fiber. This is a conceptual audit,
not a new central-mechanism attempt or candidate-solution review.

An accepted identity would make degree-one tame geometry available
for the later scalar question. The residual R, rational Kummer
membership, nonvanishing, the second finite local condition, suitable
auxiliary choices and the arbitrary rank/order gap remain unresolved.
Mathlib coverage is not checked. There is no mathematical advance
beyond the sources in this coverage-only turn; its outcome is STALLED
in the mathematical sense, with a ready, actionable next audit.
