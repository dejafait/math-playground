# 2026-09-25 — Qualified repeated-cube exclusion

STEP_ID: beal-2026-09-25-004-freitas-theorem-audit

Preserved the existing work and completed the checkpoint's single source-and-application audit. The relevance test and saved reasoning are in [the draft](../drafts/2026-09-25-freitas-theorem-audit.md). The precise numbered theorem, published source, and qualifications are in [the foundation](../foundations/03-freitas-repeated-cube-theorem.md).

[L004](../lemmas/L004-freitas-repeated-cube-exclusions.md) proves the application to every placement of (3,3,p) for prime p >= 17 congruent to 2 modulo 3, with the original-exponent divisibility consequence and emptiness of both complete systems in L003. The key scope correction relative to the abstract is the lower bound. This imports an established result; it does not claim literature novelty or an elementary factor exclusion.

The result removes a genuine part of the residual set and meets zero solutions on that exact range. Complementary repeated-cube primes, the smaller boundary cases, and other mixed families remain missing from the assembled argument. Outcome: ADVANCE; exploration turns used: 0/3. No complete candidate appears. The overview and checkpoint now reflect this narrower gap.

The reason for the subsequent Kraus source direction is that a proved divisibility restriction at the complementary primes could remove one of L003's branches there. The original hypotheses and normalization must be checked; a theorem quoted in Freitas's introduction has not been silently added as another result. The earlier failed congruence-only and single-factor mechanisms remain inactive.

The informal review checked the finite-field equivalence, every sign rearrangement, nonzero coordinates and gcd preservation, the exponent-divisor range, the direction of L003's converse, and the p=5,11 and p=19 hypothesis boundaries. L004 uses L002 for the divisibility transfer and L003 for the factor-system consequence. C002a and the failed approaches are comparisons, not mathematical inputs to L004; their existing DAG rows are preserved. Mathlib coverage remains not checked.

The primary target page at UNT was retrieved again; the nominated AMS page again returned HTTP 403. No target change was found. No numerical search was needed for this cited-theorem application.

`python3 ../scripts/docs/check_structure.py --problem beal` passed with five nodes and three edges, valid local links, complete lemma coverage, an acyclic graph, and compact overviews. `git diff --check -- .` passed. These storage checks are separate from the source-hypothesis and mathematical-input review above.
