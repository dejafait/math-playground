# 2026-09-25 — Chen–Siksek's finite exponent range

One focused source audit found that Chen–Siksek's Theorem 2 covers n=7,11,13 and every integer 3 <= n <= 10^9. [L010](../lemmas/L010-chen-siksek-exponent-range-exclusions.md) applies it to all placements, exponent-divisor extensions, and both complete factor systems. The [foundation](../foundations/07-chen-siksek-exponent-range.md) preserves the exact source version and computational qualifications; the published theorem is imported through the identified author manuscript, without an independent rerun.

Outcome: ADVANCE; exploration turns used 0/3. This reaches zero solutions with unrestricted bases in the stated range. The assembled repeated-cube gap is now confined to primes p > 10^9 with p congruent to 1 modulo 3, still in constrained system II. Other mixed signatures remain, and no complete Beal candidate appeared. The [draft assessment](../drafts/2026-09-25-chen-siksek-range-audit.md) records the relevance test and scope review.

The application review checked the ambient nontrivial primitive scope, signs, base-one cases, even exponents, the composite-exponent divisor step, and the exact converse of L003. The DAG adds only L002 and L003 as inputs to L010. Existing identifiers, inactive branches, and work in other notebooks are preserved. Mathlib coverage remains not checked.

`python3 ../scripts/docs/check_structure.py --problem beal` passed with 11 nodes, 11 unique edges, an acyclic graph, complete file coverage, valid local links, and compact overviews. `git diff --check -- .` also passed. No numerical solution search or unrelated computation was needed; structural validation does not certify the mathematical citation or proof.

The reason for the next direction is the separate infinite-family theorem in the same source, which may exclude some complementary large-prime classes; a density statement alone cannot close the residual gap. The sole current action is in PROGRESS.md.
