# Finite target-Radau reproduction — nominated scope, step412

TARGET: Justify and run the certified eight-step Gauss/left-Radau test for C997s's exact continuum inverse form and proposed F_n at n=64,128 with lambda_n=exp(-n/16).
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step412's completed review411, including targeted repeated-eigenvalue/normalization and rigorous-integration searches and local duplicate/failure checks. The exact two-degree object and fixed parameters are unchanged; no all-n rate is covered or claimed novel.
SOURCE_EVIDENCE: Li-Sra-Jegelka PMLR48 (2016), Section3/Theorem2 and Theorems6/8, https://proceedings.mlr.press/v48/lig16.pdf; supplement A.1-A.2/Lemmas11/15/Theorem21 proof/Lemmas23/25/26/Theorem27/AppendixC through Corollary31, https://proceedings.mlr.press/v48/lig16-supp.pdf; arXiv:1512.01904v2 Algorithm5/Section5.4, https://arxiv.org/html/1512.01904v2#S5.SS4; Johansson arXiv:1802.07942v1 Sections2/2.1, https://arxiv.org/pdf/1802.07942v1; Clason arXiv:2001.00617v2 Lemma6.3/Theorem6.5, https://arxiv.org/pdf/2001.00617v2#page=62. Full inspected cases and original complex-cap references remain in reviews411/410/369.
COMPARISON: Known exact-arithmetic bounds need local cyclic-subspace and complex-normalization justification and rigorous continuum/arithmetic specialization. Published pseudocode and AppendixC are not direct coverage of those differences. The future task is a bounded reproduction, not a creative mechanism or generic-rate reproof.
GAP: No matrix, target inverse form, F sign or E bound is established. Research must prove the local applicability and original-cap conversion, then enclose the exact finite values; eight steps may be useless or interval arithmetic may fail.
REASON: The defining quadrature and rigorous integration contracts support one concrete finite test after separate supervisor approval; step412 has not derived or applied any new specialization. Further unchanged generic literature review is unnecessary.
SCOPE: Exact review410 G,h,d,F and C997c/C997s complete kernel; n=64,128 only, original complex cap, all grid columns, ordinary Lebesgue I=[7/4,9/4], prescribed target/grid and lambda; at most eight Lanczos steps per degree; fixed 2048-bit-equivalent run, entry widths<=2^-256, endpoint arithmetic widths<=2^-64 and propagated F endpoint arithmetic widths<=2^-60, with all quadrature width retained.

The complete source comparison and acceptance/abandonment contract are in
[review411](2026-11-11-target-radau-finite-enclosure-review-411.md),
completed section step412. This newly saved scope receives the supervisor's
separate approval on the next turn. It does not authorize mathematics
during the completed literature-only step.

Essential inputs: C997c, C997s; proposed objects and reused Clason coverage
in review410; complex cap coverage in review369. C999d and stop410 are
error-scope comparisons only; stop341 concerns a different operator.
No stopped sampled generator is reopened. No cross-notebook input.

Write the local applicability proof before using a numerical sign:
Hermitian realification and normalization, active cyclic compression
under the finite-dimensional spectral theorem, zero target and exact
termination, PSD/exact regularization and a strict positive left endpoint,
complete product integration with zero-exponent cases and outward
enclosures, and original-cap/L2-to-sup conversion. Import known general
theorems by citation rather than reprove them. Use normalized Jacobi
inverse entries and restore squared norm once; do not transcribe the
inconsistent printed scalar recurrence. Eight Lanczos matrix-vector
steps allow the prescribed Radau augmentation, not a ninth Lanczos step.

Require a positive certified lower F endpoint at both degrees. Park on
a nonpositive lower endpoint, excessive gap, failed arithmetic budget,
uncertain breakdown or an unenclosed denominator; save the exact failure.
No iteration, parameter, precision or degree sweep. Failure is inconclusive
about the true E_n or F_n sign. Any positive result is finite only.

Save full proof and citations with Hypotheses, Conclusion, Proof, Mathlib
in a canonical lemma/corollary file if a result is actually established;
otherwise preserve unfinished reasoning or failure in drafts/ATTEMPTS.
Save full arithmetic certificates under scripts/ in that later research
turn; print only meaningful bounds, failures and paths. Do not relabel
this reproduction as new mathematics. Matching Mathlib coverage unchecked.

Unbounded target-mass rate, C997a(8), selected/both-sign transfer,
reconstruction, complements/regulators, L993 arithmetic output, L984(H),
L966/L968 forcing and actual-Xi positivity remain unpaid. A finite sign
can help decide whether a new analytic mass target merits assessment;
it cannot close those independent gaps. No RH candidate.

## Direct-source repair and scope approval — step413, 11 November 2026

The supervisor reported missing direct source URLs in this ready assessment.
This repair puts the primary URLs in SOURCE_EVIDENCE itself, retaining the
exact TARGET, SPECIALIZE decision and bounded reproduction scope. The PMLR
paper, its supplement and Johansson v1 were opened successfully through the
web tool on this date. Targeted source reads rechecked Theorem2 (PDF p4),
Theorems6/8 (pp4–5), supplement Lemma15 and its complete proof (p4),
AppendixC/Corollary29 (pp9–10), and Johansson's analytic callback contract
(p2). Earlier complete proof-case coverage in review411 is reused; no new
search or general-rate comparison is needed. The arXiv normalization
cross-check, Clason and cap coverage are reused from the recorded reviews,
not represented as freshly reread here.

This is a process repair, not new mathematical evidence: STALLED,
LITERATURE, NOVELTY_UNCHECKED, actual task type metadata. The accessible
sources support the existing SPECIALIZE assessment for the exact saved
Next action. No changed mathematical target or newly derived specialization
is approved in this turn. No essential source blocker remains in this
recorded scope; the local applicability proof and numerical success remain
work to be done. The next invocation should perform the bounded reproduction
subject to the supervisor gate, rather than repeat this URL repair.

The source bounds do not guarantee the prescribed eight-step width or sign.
The active-support qualification, complex normalization, exact product
integration, cap conversion and all previous stop evidence remain as above.
No lemma, mathematical script, PROOF or DAG was changed. Mathlib coverage
remains unchecked. No advance toward RH or beyond the checked sources is
claimed.
