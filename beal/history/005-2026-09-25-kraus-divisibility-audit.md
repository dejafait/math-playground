# 2026-09-25 — Kraus's restriction removes one cube branch

STEP_ID: beal-2026-09-25-005-kraus-divisibility-audit

Preserved the existing work and completed one source-and-application step. The relevance test, saved reasoning, and source-access assessment are in [the draft](../drafts/2026-09-25-kraus-divisibility-audit.md). Kraus's original full text was not retrieved. Instead, the precise published Proposition 7 of Bennett–Chen–Dahmen–Yazdani and corroborating Theorem 1 of Freitas support the prime-p >= 17 input; the exact citations and limitations are in [the foundation](../foundations/04-kraus-divisibility-restriction.md).

[L005](../lemmas/L005-kraus-ramified-branch-restriction.md) eliminates L003's complete system I throughout that prime range, without a condition on p modulo 3. It also restricts system II to odd u,v, v congruent to 1 modulo 12, and the stated difference valuations. The proof handles the implicit parity normalization symmetrically and continues to allow 3 dividing u. This imports an established global restriction, without claiming that the elementary factorization itself selects a branch.

The intermediate threshold is met: zero solutions in branch I. At complementary primes, emptiness of the constrained system II still separates this family from a full exclusion. The small-exponent and other mixed-signature gaps remain. Outcome: ADVANCE; exploration turns used: 0/3. No complete candidate appears.

The reason for the subsequent direction is to test local feasibility after imposing the new global restrictions. Attempt 001 only treats unrestricted local solutions, so its witnesses do not decide this more constrained question. Compatible lifts satisfying the new valuations would be informative negative evidence against an obstruction at the exceptional primes; a failed lift would require a proof of obstruction. The single-factor shortcut remains stopped.

Mathematical review checked the source range and normalization, the direction of L003's converse, the modulo-4 calculation and combination modulo 12, the nonzero valuation arguments, and the unchanged allowance for 3 dividing u. L005's only direct local lemma input is L003; L004 and the stopped attempts are comparisons. Existing DAG rows were retained. Mathlib coverage is not checked. No numerical search was needed for this cited input and its elementary consequences.

`python3 ../scripts/docs/check_structure.py --problem beal` passed with six nodes and four edges, valid local links, complete lemma coverage, an acyclic graph, and compact overviews. `git diff --check -- .` passed. These storage checks do not certify the cited theorems or replace the mathematical review above.
