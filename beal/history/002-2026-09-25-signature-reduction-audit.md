# 2026-09-25 — Exact exponent reduction and qualified global exclusions

STEP_ID: beal-2026-09-25-002-signature-reduction

The prior local-solubility work and all existing changes were preserved. This step tested the checkpoint's global reduction route rather than repeating the stopped unrestricted-congruence approach. The source formulation was rechecked on Mauldin's primary page; the nominated AMS endpoint still failed retrieval.

[L002](../lemmas/L002-prime-four-signature-reduction.md) proves reduction to exponents in {4} union {odd primes}, preserving positivity and prime support for every divisor choice. [C002a](../lemmas/C002a-darmon-merel-signature-exclusions.md) then excludes equal exponents, all placements of (p,p,3) and (p,p,4) for odd primes p >= 5, and the ordered signature (4,4,3). The cube clause is unconditional after the separately checked full-modularity theorem; precise sources are in [standard inputs](../foundations/02-standard-results.md).

The mathematical review checked all sign conversions, primitive/nontrivial source hypotheses, base-one cases, and the n = 3 and n = 4 boundaries. The identity 1^3+2^3=3^2 blocks an unqualified extension of the square clause to exponent three; (-a)^4=a^4 blocks the proposed sign conversion for (4,3,4). These checks and the pre-proof reasoning are in [the audit draft](../drafts/2026-09-25-signature-reduction-audit.md). No bounded numerical search was used as evidence of global nonexistence.

The achieved threshold is an exact reduction with exclusions of infinite families, not emptiness of the residual set. Infinitely many mixed signatures remain. The effect on the main gap is a rigorous narrowing of its scope, not a complete candidate. Outcome: ADVANCE; exploration turns outstanding: 0/3. The reason for changing mechanism within the global route is that direct applications of the audited clauses are exhausted, while factorization of a^3+b^3 offers additional integer constraints on the remaining family with a third prime exponent at least five.

The DAG adds only the reduction as a mathematical input to the corollary. L001 is a contrast and route constraint, not an input to the new proofs. `python3 ../scripts/docs/check_structure.py --problem beal` passed with three nodes and one edge; local links, file coverage, acyclicity, and overview lengths passed. `git diff --check -- .` also passed. These are storage checks, separate from the informal mathematical review above. Mathlib coverage remains not checked.
