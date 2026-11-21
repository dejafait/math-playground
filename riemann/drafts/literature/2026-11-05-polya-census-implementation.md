# Bounded actual Pólya event census — specialization nomination

TARGET: Implement one bounded interval census of L814's nondegenerate events on 0<x<=40, certifying full theta-series and integral tails and all excluded cells, and saving every unresolved origin, edge, multiple-root or common-zero interval.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step578's completed source comparison in 2026-11-05-polya-certified-event-census.md; no fresh discovery search is needed for this unchanged family and bounded method. Newly written continuation awaits separate approval before execution.
SOURCE_EVIDENCE: Hickey–Ju–van Emden2001 author manuscript Section4.8 Theorems9–10/proofs PDF pp10–11 https://fab.cba.mit.edu/classes/S62.12/docs/Hickey_interval.pdf ; Johansson1802.07942v1 Sections2/2.1 pp2–4,3.2 p6 https://arxiv.org/pdf/1802.07942 ; Arb2.23 contracts https://arblib.org/arb_calc.html and https://arblib.org/acb_calc.html ; optional DLMF8.2.2 https://dlmf.nist.gov/8.2#E2 ; reuse L814's exact Q and local fold inputs.
COMPARISON: The cited inclusion, finite quadrature and bounded-subdivision methods cover analytic functions with rigorous evaluators and explicit unresolved output. They supply no actual census or automatic theta/integral tails. Specialize existing L016/L019/L020/L814 majorants and tests without reproving general algorithms.
GAP: Explicit constants, evaluator and coverage certificate remain unconstructed. No guarantee of resolving multiple roots, common zeros or exact edge equality is assumed. Signed compensation, unbounded x, infinity and mixed positivity remain open.
REASON: Nominate concrete standard work after completed coverage; separate approval is the gate for a newly written continuation, not a reason to repeat discovery or revive the parked global-reference access loop.
SCOPE: One bounded implementation/calculation for actual F,G, with all step578 certificate obligations; no new reference, global theorem, parameter sweep or creative-sign claim. Full Mathlib match unchecked.

Use only L016/L019/L020/L021 and audited L814 as local mathematical
inputs, plus the cited methods. No cross-notebook input or assumed
all-real reference. Keep exact c,Q,B,F,G,D,W conventions. Save partial
reasoning before expensive work.

Prove/document explicit real-path theta-series and improper-integral
error bounds for orders0,1,2, normalization and any extra derivatives
actually used. Retain full omitted tails. Integrate finite theta sums
under validated quadrature and add proved real-path errors afterward;
do not assert a complex infinite-series enclosure without justification.
Enclose interval x uniformly. Record backend/version and outward rounding;
requested tolerances alone do not establish achieved accuracy.

Use a bounded partition, explicit caps and the cited strict interval
Newton inclusion or sign-change/derivative tests. Distinguish exclusion
by W from event exclusion by same-sign F,G. Save a complete domain cover,
including all shared endpoints, isolated-root tests and unresolved cells.
Close a positive-width origin interval and edge40 or explicitly mark them
unresolved. Multiple/common zeros need independent resolution or retention.
An interval containing zero is not a certificate of equality.

Classify events only with a certified W root, F G<0 and W' excluding
zero over its box; enclose tau and orientation using L814. Save full
arithmetic, tails, input provenance, coverage checks and failures on disk;
print only conclusions, actual/required inequalities and artifact paths.
Publish any used new bounds canonically. Partial coverage is not absence.

Continue only if a certified event/sign or substantial exclusion gives
a discriminating result. At fixed caps preserve all undecided relevant
regions and stop this attempt; repetition requires a materially refined
or independent test. No outcome alone supplies RH or all-degree positivity.
After separate approval, route implementation to standard/high. This is
REPRODUCTION of known certification, not creative work. Any claimed
census/evaluator needs a later audit before reliance.
