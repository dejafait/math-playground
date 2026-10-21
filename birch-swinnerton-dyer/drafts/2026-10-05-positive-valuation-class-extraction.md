# Positive-valuation extraction working record

STEP_ID: BSD-2026-10-05-048-positive-valuation-class-extraction

Approved target: Specialize Sakamoto's Poitou-Tate comparison and rank-zero class relations under L023's hypotheses for m > 2h to test classical membership of its two prime-deletion classes and the span-index bound p^(3h).

Prior assessment: drafts/literature/2026-10-05-positive-valuation-prime-deletion-extraction.md (SPECIALIZE), supplied before invocation; its COVERED_TARGET matches the approved target.

Main gap: rank E(Q) versus complex order at order at least two. Intermediate target: actual classical extraction at finite depth, retaining the finite quotient F. Plausible downstream use: bounded-index Selmer generators before a separately justified passage to characteristic zero. Rational Kummer membership, compatible depths/primes and complex-order comparison remain independent gaps.

Test: retain only if both actual components are classical and their span quotient has length at most 3h, including h=0 and positive h, with no cancellation of p^h or freeness assumption on the full Selmer module.

Read L021/L023 in full, L015's class relations, L016/L017's hypotheses and obstruction statements, ATTEMPTS/021 and L023's completed critical-audit record. Existing changes are preserved. The earlier error models lack L023's working-depth localization surjection.

Unfinished reasoning saved before primary verification: write M for classical, K for strict at N and B for relaxed at N. The strict/classical Poitou-Tate sequence, with classical self-dual, should show B=M because M -> R_m^2 is onto. Each prime-deletion component belongs to B, and at the other prime is transverse, hence zero once classical. Definition 2.18's last relation with d=N/ell_i and an extra q should identify its own finite-singular coordinate as -delta_m(N), with all G factors retained. Then image of their span in R_m^2 is p^h R_m^2. The quotient fits between a quotient of K (length h) and (R_m/p^h)^2 (length 2h). Verify exact dual structures, tensor contraction and the source relation before recording a result. No extraction verdict or new lemma is asserted in this saved reasoning.

## Completed attempt

Canonical L024 now contains the full conditional extraction proof.
Poitou-Tate yields B=M using the granted localization surjection without
requiring K=0. The actual class relations give diagonal scalar -delta
with valuation h and zero cross localizations. The span quotient has
length 3h-length(K intersect C), hence at most 3h. Both boundary cases
are checked in that proof; no mathematical script was needed. This is
a reproduction/specialization of known mechanisms, with no claim of
originality or rational membership. Its separate critical-audit coverage
checkpoint is REVIEW_REQUIRED; the next turn must approve that new
continuation before conducting its audit.
