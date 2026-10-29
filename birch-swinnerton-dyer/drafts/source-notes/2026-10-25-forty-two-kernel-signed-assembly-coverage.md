# Step 483 — signed 42-kernel assembly source coverage

2026-10-25. Literature only. No coefficient or kernel was recomputed,
no signed sum or radius was calculated, and no proof audit was executed.

## Gap, intermediate target and test

The main unresolved claim remains rational rank equals analytic order
for every E/Q of analytic order at least two. The exact intermediate
target is the TARGET in the matching signed-assembly assessment.
Its downstream use is a fixed-curve derivative enclosure under L116;
it cannot supply the missing uniform rank comparison or refined BSD.
Continue to calculation only with the same normalized newform, common
midpoint and valid retained intervals. The calculation must report the
actual radius and test zero exclusion, or stop at its first unmet input
premise. An interval containing zero fails this nonvanishing test without
refuting BSD or proving that the derivative vanishes.

## Primary statements and applicability

Reuse the ready analytic comparison in
`drafts/source-notes/2026-10-25-forty-two-kernel-contract-coverage.md`
and the audit comparison in
`drafts/source-notes/2026-10-25-l116-audit-coverage.md`.
Read the complete L116 contract and its separate audit. Its exact curve,
conductor 389, Fricke eigenvalue -1, lower vanishing, full Euler factors,
all-n coefficient majorant and unnormalized derivative are unchanged.
The reviewed analytic composition requires no new estimate or integrator.

Reopened J. E. Cremona, *Algorithms for Modular Elliptic Curves*,
corrected second edition (1997), Chapter 2, Section 2.6,
equations (2.6.1)--(2.6.2), printed p.25, including coprime
multiplicativity; Section 2.8, equation (2.8.3), printed p.29;
and Section 2.13, Proposition 2.13.1 and preceding proof,
printed pp.42--43 ([author chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf)).
The Euler rules normalize a_1=1 and distinguish primes dividing N.
The retained indices are below 389, so their prime factors are good;
the existing coefficient audit is within that source case. The derivative
statement requires order at least r and Fricke eigenvalue (-1)^(r-1).
At r=2, L101/L116 retain those conditions, including lower vanishing
in the completed-to-uncompleted transition. These named results are
imported, not reproved; the new task is their finite artifact application.

Reuse Wuthrich, arXiv:1608.06423v2, Section 3.1, Lemma 4/proof,
printed pp.6--7, and Johansson, arXiv:1802.07942v1, Section 2,
printed p.2, as inspected in the two coverage notes above. The former's
proof supplies the elliptic-newform coefficient majorant, not this
derivative certificate. The latter distinguishes whole-set containment
and analyticity tests from requested tolerances and coarse/failure
outputs. No FLINT backend is used by the proposed exact summation.
L102's audited Taylor theorem and L103's audited parameter construction
remain the containment inputs; their adequate DLMF coverage is reused
from the first-kernel and subsequent fixed-kernel assessments.

Newly inspected official Python 3.15.1 documentation:
[fractions.Fraction](https://docs.python.org/3/library/fractions.html)
and [numbers.Rational](https://docs.python.org/3/library/numbers.html#numbers.Rational).
Integer numerator/denominator construction represents their rational
ratio; Fraction implements rational arithmetic and positive-denominator
normalized export. Float construction preserves the float's value,
which may differ from the intended rational. The approved implementation
must therefore use stored integers and integer denominators throughout,
with no float parsing or limit_denominator approximation. Compare an
independent summation traversal using exact integer/rational arithmetic;
documentation alone does not certify an implementation or its output.

## Existing evidence, duplicates and historical qualifications

Read L031's derivative-facing extraction and separate step-410 audit,
and their ready assessment
`drafts/literature/2026-10-23-finite-derivative-coefficient-audit.md`.
The exact export is `scripts/finite-derivative-coefficients/certificate.json`,
SHA256 `9ad5f8b621dab84edeb97b891f5d4ed9cfe6d11c43b1b7b7f8e2b7147780363f`.
Its indexed export covers 1..128. The same-model, conductor, original
certificate binding and untwisted a_1=1 normalization are the relevant
subset; neither twist values, periods nor optimality are new premises.
Step 410 already audits all coefficient slots and the export. Later
application must read the complete relevant export and verify the exact
selected binding, not accept this note or a PASS preview as its values.

Read the hypotheses/conclusions and artifact references of L103--L114,
L103's parameter proof, and the relevant completed L106 audit passages.
The retained evidence is step-404 for n=1, step-412 for n=2, then
step-417, 424, 431, 435, 440, 449, 453, 457, 461 and 468 for successive
four-index blocks from 3..6 through 39..42. The artifact is kernel.json
in the first two directories and n-<index>/kernel.json in each block.
The common parameter is step-404/parameter.json; later whole-parameter
copies/identities must agree with it. There is no parameter rescaling.
Each canonical statement claims containment and a separate completed
audit. In particular L106's step-446 audit explicitly closes its pending
audit: earlier pending wording in later-produced summaries is historical,
not evidence that n=7..10 remain unaudited.

Inspector previews located schemas only. Complete small kernel records
for n=1,3,39 and the coefficient normalization were read to identify the
interface, not to validate all 42 values or their containment. kernel.json
uses integer final_grid endpoints divided by grid_denominator; midpoint
and radius are rational pairs. parameter.json records c_grid, midpoint
and delta alongside elementary witnesses. Guessed final.json paths were
absent; the subsequent scoped filename search found kernel.json. No
certificate premise was declared failed from those navigation errors.

Reuse completed signed replay/containment conclusions, with their exact
scope, rather than rerun 42 full integrations in an assembly turn.
Historical n=1/n=2 finalization, coefficient post-write timing, stopped
426/429/444 and later document-transition qualifications remain in the
canonical proofs. Current input bindings and preservation must still be
checked; a fresh application cannot certify historical timing or silently
repair source provenance. No historical resource claim supplies a
containment premise. ATTEMPTS/052--054 park further production, not this
different finite test, and remain unchanged.

Targeted searches of the 2026-10-21/24/25 assessments, ATTEMPTS/052--054
and histories 408/410/446/470/480/482 found conditional composition,
coefficient extraction and kernel audits, not a completed signed assembly.
Reuse step 479's broader derivative discovery. New queries were
`"389" "second derivative" "rigorous" L-function` and
`"elliptic" "L-series" "derivative" "exact" "interval"`.
Results included numerical Sage/PARI interfaces and Magma's heuristic
analytic-rank description; search snippets are not theorem evidence.
The primary PARI manual fetch timed out and is an unread optional lead,
not an essential source blocker: no PARI call or value is an input.
No search failure establishes novelty; this is known-method reproduction.

## Ready calculation boundary

SPECIALIZE. There is no essential unread theorem for this exact target.
Apply L116 unchanged using L031's audited export and the audited retained
kernel conclusions. A later bounded calculation must inspect complete
relevant endpoint/parameter/coefficient records, match canonical values
and existing audit/source bindings, preserve inputs before/after, and
record every selected artifact and qualification. This does not authorize
new production, changed quadrature, tighter bounds, source adapters or
repair of a failed binding. An unexpectedly unvalidated containment input
is the first unmet premise; stop rather than undertake a new audit here.

Compute only L116's signed rational center and its stated radius using
the actual nonnegative widths, with eta=0 only after exact arithmetic
comparison. Keep both original analytic remainders, full-sum parameter
transfer and L115's block allowance; do not inherit the old 2^-40
total-radius guarantee. Independently compare reverse-order summation
and direct interval endpoint arithmetic. Persist a complete certificate
and report the exact center, each allowance, total radius, resulting
endpoints and strict zero test, or the first precise failed premise.
Use one inclusive 180-second/134217728-new-byte cap including setup and
reporting, without retries or integration replay. A later separate
critical audit is required for a successful assembled certificate.
Full matching Mathlib coverage remains unchecked; no complete candidate
for the notebook's exact target is present.
