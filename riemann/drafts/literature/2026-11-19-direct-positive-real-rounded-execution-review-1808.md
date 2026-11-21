# Rounded intermediate arithmetic: nomination1808, source review1809

TARGET: Review whether rounding C033z's intermediate rational values can preserve both2^-10 arithmetic allowances and the10^6 operation cap for C033w's eight positive-real scalars, using the1808 exact-execution evidence.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1809 searched rational rounding/operation counts, arbitrary-precision ball arithmetic and stronger correctly-rounded conversion contracts; checked the direct-positive-real assessments/histories and relevant C033y/z/u/w/x ranges. No inspected source supplies this evaluator's finite cap. Queries, inspected cases and limitations: drafts/literature/2026-11-19-direct-positive-real-rounded-source-notes-1809.md.
SOURCE_EVIDENCE: Johansson1611.02831v1 Sections3.1.1-3.2/4/5-5.1,pp5-8, https://arxiv.org/pdf/1611.02831v1; Arb2.23.0 arf.h semantics/conversions, https://arblib.org/arf.html and arb.h introduction/division/dot-products, https://arblib.org/arb.html; MPFR4.2.2 Sections4.4/4.6/5.2, https://www.mpfr.org/mpfr-4.2.2/mpfr.html . Reuse analytic source evidence1799/1804/1805 without refreshing it.
COMPARISON: Inspected sources cover rounding semantics and enclosure propagation, including denominator separation, but their bit/limb routines and timing comparisons are not C033z's rational-operation ledger. The989767 count assumes exact intermediates. Execution1808's saved prefix diagnoses a practical bottleneck, not a mathematical lower bound. Neither a precision request nor a library call certifies the unchanged cap.
GAP: A costed implementation of selected rounding using only rational arithmetic/comparisons, its accumulated error and its propagation through C033z remain unproved. No all-eight enclosure, chosen precision, completed cost or bit-cost bound is supplied. Generic source access is adequate; instance-specific mathematics is the remaining task.
REASON: Known enclosure principles cover the ingredients, so import those principles rather than reprove them; derive only an explicitly costed local specialization in a later research turn. Review1809 performs no derivation or implementation. A narrower Ihat-only nomination is saved separately for next-turn approval; neither black-box rounding nor scalar execution is approved here.
SCOPE: Source comparison for the unchanged eight scalars, both2^-10 allowances, radius<2^-8 and cap10^6. A subsequent specialization must pay conversion, comparisons, error tracking and propagation in the original rational-operation model; no free floor, integer division, limb access, fused arithmetic or transcendental callback.

## Completed source review1809

The [source comparison](2026-11-19-direct-positive-real-rounded-source-notes-1809.md)
records the inspected primary cases and the distinction between a valid
enclosure and a certified finite cost. SPECIALIZE is an ingredient-scope
decision, not an existence theorem for a successful rounded evaluator.
The next independently testable subtarget is only the Ihat accumulation;
the other exact constructors and unfinished execution remain preserved.
No theorem has been added to the canonical argument in this literature turn.

## Original nomination1808, retained as history

This is a new continuation nomination, not an additional literature turn
completed1808. The completed task was implementation/REPRODUCTION under
the pre-existing SPECIALIZE1806 assessment. No rounded evaluator has been
derived, implemented or approved in this step.

The next review should retrieve exact primary arithmetic hypotheses and
relevant error-propagation cases before deciding IMPORT, SPECIALIZE or
EXPLORE. Determine whether the operation model even permits the proposed
rounding implementation within the unchanged cap. Do not silently grant
floor, approximate transcendental calls or bit operations as unit-cost
rational operations. A negative comparison is a valid result; no new lemma
or mathematical script belongs in that literature-only step.

Essential inputs: C033y/z/u/w, C032s/q/w and C032j law conventions;
execution summaries `scripts/smoothed-law/direct_positive_real_execution_1808.json`
and `scripts/smoothed-law/direct_positive_real_execution_remaining_1808.json`.
Preserve all exact1808 data, earlier1800-1806 certificates, C033x/1781/1782
stops and unfinished C033v. The exact route remains mathematically open;
this is a practical execution reassessment, not a global stop.

Retain the actual divisor/conjugation/multiplicity, excluded ordinate0,
strict strip/gamma>14, counting, real zeros through100 and one in(14,15),
reciprocal-square tail, heat positivity and separate fixed-j errors, both
fixed-v1 qualifications, zero drift/killing and Gaussian half-variance.
Source-wide and zero-data correctness and full matching Mathlib coverage
remain unverified. Neither this finite computation nor a later successful
rounding contract would pay conditioning, exact interpolation weights,
TV, the full observation interval, signed height, cancellation, realization
or L030-L032/C032a actual-Xi positivity.

The central creative blocker1796 is unchanged: this finite scalar mechanism
supplies no independent signed-height input or representation. This task is
an arithmetic-source comparison, not a creative main-gap mechanism.
