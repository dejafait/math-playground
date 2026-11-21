# Source scope for a separate audit of the finite primitive comparison

TARGET: Audit C759f's two-sine normalized-primitive comparison, checking the relative-kernel cancellation, H1 tail bound, both poles, all prime powers, interval generator and continuum quartic certificate; accept the finite-slice result or identify a concrete error.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step815 reused the exact-statement/stronger-result and local-failure search in review812/step813 and compared assessment813 with the complete C759f claim; inspected Python Decimal primary API passages for interval arithmetic. No duplicate mathematical search or new sign calculation.
SOURCE_EVIDENCE: Reuse inspected Suzuki2606.09096v2 Theorem1.1/(1.8)/Section2.4/(2.7)/Lemma3.1/Section3.2 and v3 Sections8.2/8.4/8.5, plus DLMF5.9.13 with real part1/4; exact URLs and inspected passage details remain in assessment813 and review812. C759a/d/e and L741 provide local form, cap and regularization inputs.
COMPARISON: Existing coverage suffices for the fixed-slice audit, including C759f's stronger all-nonzero-vector conclusion on the same two modes. Known form/primitive identities and Decimal semantics support verification; no source certifies the relative matrix, tail or quartic sign. Existing fixed-modulus tail numbers cannot be copied.
GAP: Source scope is approved in step815; conceptual and complete arithmetic verification of C759f remains wholly pending. No certificate replay, analytic verification or mathematical acceptance is claimed in this literature turn.
REASON: Reused mathematical coverage and inspected software-contract evidence cover the exact saved audit target. Proceed to one conceptual audit, classified REPRODUCTION; preserve the finite-slice calculation and do not enlarge modes, window or cap.
SCOPE: Only C759f and scripts/spectral-triples/two-sine-primitive-814.py/.json, at the unchanged C759a form and first-two-sine domain; subsequent audit classification REPRODUCTION if approved.

The calculation's main potential failure points are normalization and
scalar cancellation in the relative form, absolute convergence at zero,
polarized translation identity and complete tail, correlation/pole factors,
and the continuum sign rather than a floating grid. Check the exact
projective endpoint c1=0 as well as every real finite ratio. Preserve the
uncertified diagnostics as selection evidence only. The software trust
assumption is Python integer/Decimal/libmpdec correctness.

The required audit must inspect the complete load-bearing generator and
certificate evidence, with independent arithmetic where it is useful;
a preview, positive Ritz sample or seven boolean checks alone is not
verification. A pass verifies only the finite-slice result. It does not
pay the infinite odd complement, parity infima, signs/simplicity, other
windows, or Xi realization. No creative infinite-domain target has yet
been justified by a concrete signed domination mechanism.

## Completed separate source-scope approval — step815

The main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is independent verification of C759f, whose plausible
use is a finite variational parity-comparison input. Accept only after the
complete analytic and arithmetic checks; a concrete error reopens the slice.
A pass ends this fixed test and leaves the full odd domain and Xi transfer open.

Read assessment813 and the full review812/step813 source comparison, then
C759f's complete statement/proof to identify required coverage, C759a's
form/domain hypotheses, C759e's hypotheses and domain passage, history814,
and the metric-warning passage located in assessment548. This was source
scope comparison, not verification of those mathematical arguments. The
previous modulus/fixed-shift stops concern different maps. No new duplicate
search is needed at unchanged hypotheses; no cross-notebook input is used.

The precise mathematical sources and qualifications remain those recorded
above and in review812: Suzuki v2 Theorem1.1, Section2.4/(2.7), Lemma3.1
and Section3.2; v3 Sections8.2/8.4/8.5 for the inverse derivative metric;
DLMF5.9.13 for positive real argument part. The phase discrepancy is a
local audit obligation, not permission to import an energy ordering. No
new external realization or parity theorem is required. All-direction
homogeneous certification on the same slice is within scope; it is not an
infinite-domain claim. The optional Bombieri access failure remains nonessential.

New primary software evidence: [Python Decimal documentation](https://docs.python.org/3/library/decimal.html),
served as Python3.15.2 on 2026-11-13, sections Decimal objects, Context objects,
and Rounding modes. Inspected exp/ln (correct rounding, HALF_EVEN), sqrt
(full precision), next_minus/next_plus (adjacent representables), copy_negate
(context-independent), and FLOOR/CEILING (directed rounding). Also inspected
the power warning: C two-argument power is only almost always correctly
rounded. These contracts support an audit, not automatic certification.
Check the actual interpreter/library version, contexts, exponent range,
nonfinite values and each operation used. Do not substitute generic power
for an inspected rounding contract. Software correctness remains a trust assumption.

No generator or certificate was executed or verified. The next audit must
read the full relevant generator and complete load-bearing certificate
values, independently check the cancellation, H1 remainder, both poles,
all prime powers and projective endpoint, and assess the continuum
square-completion certificate. Booleans and entry previews alone are
insufficient. Mathlib full matching coverage remains unchecked; no formal
verification claim follows from API documentation or structural validation.

LITERATURE_REASON: The invocation-start REVIEW_REQUIRED assessment required separate scope approval; the numerical generator also cites a primary Decimal contract not detailed in the supplied assessment. This turn supplies that narrow evidence and reuses the unchanged mathematical coverage.
