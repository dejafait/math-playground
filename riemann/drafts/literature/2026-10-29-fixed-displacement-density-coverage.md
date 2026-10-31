# Fixed-displacement pair mass — completed source comparison

TARGET: Assess whether unconditional zero-density estimates and the ordinary fourth moment control L471's fixed-displacement sector d_j>=1/16 by B_{>=1/16}(T)=o(T(log T)^3).
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded Ingham/fixed-sigma density, weighted zero-neighborhood/fourth-moment and Xi/Laguerre/negative-part searches; narrow L471/L467, moment, selected-energy and complementary-mass comparisons; no inspected theorem states the exact restricted pair-mass conclusion. Queries and source scope are in drafts/2026-10-29-fixed-displacement-source-review-notes.md; no novelty claim.
SOURCE_EVIDENCE: Directly inspected Chourasiya--Simonic arXiv:2507.15184v1 (21 July 2025), Introduction p. 1, Corollary 1/(3) and Table 1 p. 2, proof pp. 4--5, Section 4 (32) and concluding proof p. 14; Guth--Maynard arXiv:2405.20552v1 Theorem 1.2 and (1.2)--(1.4). Reused Bui--Hall v1 Theorem 3/Section 7 coverage and Bellotti--Wong v2/L467's audited closed-shell specialization with their source-audit qualifications.
COMPARISON: Accessible unconditional multiplicity-counted density covers the fixed positive cutoff and padded cumulative heights; reviewed ordinary fourth moments and closed shells cover continuous energy and overlap. These are separate known inputs, not a citation for the exact B-sector estimate. Aggregate-window L2 estimation differs from L471's failed separate-pair summation and L475's growing-disk norm.
GAP: No aggregate-kernel norm, resulting height exponent, little-o sector bound or canonical import has been proved in this literature-only step; these are the bounded specialization obligations in the new continuation assessment.
REASON: Essential source coverage is available for a different, independently testable aggregation mechanism after duplicate audit stalls. Preserve all prior stops; approve only one later fixed-sector test, subject to separate approval of its new assessment.
SCOPE: Actual Xi; L471's B(T), P_T, J_j(T), one-copy quotients F_j and full multiplicities; restrict the original nonnegative summands to d_j>=1/16 without changing their weights. No RH, simplicity, spacing, external half-plane premise or shrinking displacement cutoff.
LITERATURE_REASON: The proposed use of an unconditional off-line zero-density theorem with a fixed positive displacement cutoff is outside the assessed ordinary-moment and scale-adapted source scopes.

## Original nomination, preserved for scope

Define B_{>=1/16}(T) only by restricting L471's existing B(T) sum
to pairs with d_j>=1/16. Retain every multiplicity and the clipped
windows. No estimate follows from this definition. The target is a
partial sector of the sufficient pair-mass majorant for N(T), not a
necessary condition or a claim that a nonreal pair forces negativity.

The main gap remains initial signs at unbounded heights and global
mixed positivity. A fixed-sector saving could remove one expressly
uncontrolled part of L471's majorant. Displacements below 1/16,
including the microscopic and intermediate ranges, the full saving,
individual heights and higher signs would remain unresolved.

Review exact statements and stronger known results first. Retrieve
an unconditional zero-density theorem at real part 1/2+1/16 with
its multiplicity convention, parameter range, powers and logarithmic
losses. Match positive-height conjugate Xi pairs to the zeta zeros
actually counted, including the clipped-window padding beyond
[T,2T]. Reuse the existing fourth-moment assessment where adequate;
do not assume a short-interval, zero-conditioned or discrete moment
from a global moment statement. Check local zero-count coverage if
aggregation needs an overlap bound. Search the active notebook for
this exact fixed-cutoff implementation and recorded failures before
approving a calculation. Model memory is only a discovery lead.

Continue only if accessible primary hypotheses and explicit bounds
support a concrete aggregation test that could attain the displayed
little-o threshold without an unproved selected-amplitude estimate.
If the available density/moment combination only gives full scale,
assumes RH or requires inaccessible essential proof coverage, record
the precise mismatch and park this implementation. Do not revive the
stopped displacement-free summation or the growing-disk envelope by
renaming it. This is a source-review nomination, not an application
of any density theorem or a new mathematical result.

The likely eventual application would be an established-tool
specialization, not a creative route merely because this sector was
uncovered locally. A central creative attempt still needs a justified
arithmetic cancellation mechanism for the remaining microscopic mass.
Full matching and supporting Mathlib coverage remain unchecked.

## Completed comparison and decision, 29 October 2026

The source review now supplies the missing density coverage. See
[the source notes](../2026-10-29-fixed-displacement-source-review-notes.md)
for the exact cited theorem, what was read, reuse provenance, unused
leads and limits. The original nomination above records the review
questions, not an outstanding instruction to repeat the search.

Three mechanisms were compared: repeat the C464c audit (already
completed, no changed claim); repeat the scale-adapted disk norm
(L475's exponential-cost stop persists); or aggregate the fixed-sector
real windows using a density count, local overlap and the ordinary
fourth moment. Select the third. It changes the controlled sector and
the order of aggregation, without assuming a zero-conditioned moment.
The retained small-displacement and signed-kernel gaps remain open.

The source statements support testing the third mechanism; no bound
for its aggregate kernel or its final scale is established here. A
known theorem does not state this exact pair sum, so use SPECIALIZE
rather than IMPORT for the subsequent application. Reproving a density
or moment theorem is unnecessary. Full manuscripts and their finite
computations have not been independently audited locally.

The single mathematical continuation is nominated in
`drafts/literature/2026-10-29-fixed-sector-aggregate-kernel-test.md`.
It must receive separate approval before invocation. This completed
step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: new source
coverage, no mathematical saving or discovery beyond the sources.
