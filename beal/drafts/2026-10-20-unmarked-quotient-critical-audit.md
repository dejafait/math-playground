# Unmarked quotient: independent critical audit

Approved target: critically audit L107's invariant quotient, genus 38 and
normalized square-class −3 lifting criterion, including every boundary
fiber. Reuse the supplied SPECIALIZE assessment
`drafts/literature/2026-10-20-unmarked-quotient-critical-audit.md`.

Main gap: elimination of both L095 integer systems and global factor
compatibility. The intermediate target is reliable quotient geometry and
reversible lifting, potentially usable by a later rational-point method.
Pass only after checking the full invariant scheme, constants, smooth
proper model, every boundary inertia orbit and normalized residue algebra,
and independently replaying every load-bearing finite record.

The full L106 and L107 proofs, L106 audit code/note, quotient producer and
construction assessment have been read. No defect is apparent in the
invariant free-module calculation or the odd-inertia boundary argument.
At a curve-point DVR the residue characteristic is zero; this is not a
dyadic number-ring calculation. The unit-root algebra must be identified
with the full integral closure, not merely shown to have the right
fraction field. Full finite replay and the final local normalization
audit remain pending at this checkpoint.

ATTEMPTS/045's backend park and ATTEMPTS/046-minus-three-joint-factor-at-seven.md's
exact witness are preserved; neither concerns correctness of this quotient.
No sibling notebook or new external source is needed for this unchanged
approved scope. No rational-point classification or new target is being
attempted in this step.

## Completed audit

The full mathematical review is canonical in L107's independent-audit
section. The invariant scheme, geometric domain/constants, smooth proper
quotient, all branch cycles and boundary freeness pass without correction.
The curve-point local ring calculation identifies the entire integral
closure and both possible rational residue algebras, so the normalized
square-class test retains every boundary point.

The independent `scripts/global-fiber-genus/audit_quotient.py` uses
multinomial coefficients, monic long division and quadratic-algebra
multiplication, then verifies every original quotient record and both
complete ordered lifts over every quotient cycle. Its report
`scripts/global-fiber-genus/quotient-audit-certificate.json` has 9,581
passing checks and no failures. L106's full certificate replay also
passes its 6,822 checks. Degree 495, genus 38, relative indices one and
the 990/1000 label bound are confirmed. The optional SymPy import was
unavailable; the completed audit uses only the Python standard library.

Completed classification: RESEARCH / EXPLORATION / REPRODUCTION;
actual task proof_audit. No new mathematical input or error repair is
claimed, so this is not ADVANCE. Mathematical exploration usage is one
since step 366. PROOF.md and DAG.md are unchanged because the argument
and its mathematical inputs did not change. L107's canonical audit
supersedes the overview's historical pending-audit wording.

The proposed next scope is exact arithmetic of rational boundary fibers
and their normalized lifting classes. This could supply boundary data
for a later rational-point method, but is not derived here. Its new
assessment is REVIEW_REQUIRED and needs separate source comparison.
Both L095 power/gcd/positivity systems, remaining global factors,
minus-eleven and the general Beal gap remain unresolved.
