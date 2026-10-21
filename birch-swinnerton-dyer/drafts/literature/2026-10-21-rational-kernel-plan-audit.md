# Capped rational-kernel proof audit — coverage pending

TARGET: Critically audit L102's capped rational Taylor kernel enclosure proof, including uniform radius, constant and coefficient rounding, full-product integration, and finite replay-cost bounds.
CHECKED: 2026-10-21
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Prior proof-target source/duplicate coverage is available in drafts/literature/2026-10-21-rational-kernel-plan.md and drafts/source-notes/2026-10-21-rational-kernel-source-review.md; exact audit-target reuse/comparison has not yet been separately approved.
SOURCE_EVIDENCE: Previously inspected DLMF v1.2.8 equations 1.4.35--37, 1.4.26/28/29, 4.2.19, 4.6.1/4, 4.7.3/7/8/10, 4.8.2 and 1.2.11; L031 endpoint arithmetic and audited L101 finite-error contract. No additional source was read for this newly proposed audit.
COMPARISON: L102 derives a particular coefficient/error construction and loose arithmetic cost from standard theorems; a later independent audit must compare every case with their hypotheses and check that its complete caps and uniform claims follow. The prior plan assessment authorized the proof attempt, not its completed critical review.
GAP: Separate coverage approval and independent critical audit of the newly written proof remain; no implementation, evaluated parameter, kernel or derivative certificate exists.
REASON: Newly derived bounds are not approved as audited mathematics in the deriving turn; preserve the completed proof attempt while routing this new exact audit target to a separate literature-only approval step.
LITERATURE_REASON: The new target concerns L102's just-written uniform rounding/cost specialization and its independent audit; approve reuse at this exact scope before proof_audit, without repeating unchanged analytic-tail browsing.

The next approval should reuse adequate inspected sources and read only
needed canonical proof passages. Essential numerical inputs are L031's
exact endpoint rules and L101's finite-kernel definition/contract.
The downstream analytic premises remain L030, L031's independent
coefficient/sign and elementary parameter rules, audited L099 and
foundations/02 through L101. Exclude L035/L100, published basis/Sha
premises, the unavailable library and the unread optional Taylor-model
paper from the proof's inputs.

The discriminating audit is containment and radius under exactly 1016
panels of length 1/8, degree <=256, scalar series <=256 terms, <=16
squarings and grid 2^-256. Check both scalar remainder/enlargement
errors, all coefficient recurrences, convolution signs/full slots,
analytic integration and summed radius <2^-183<=2^-50. Also distinguish
endpoint operation count from arbitrary-input bit complexity and any
unproved practical resource claim. Failure retains the actual failed
bound and parks these caps; no enlargement or implementation occurs
in that audit. Success only validates a numerical plan, not actual
kernels, L'' nonvanishing or BSD. Mathlib remains not checked.
