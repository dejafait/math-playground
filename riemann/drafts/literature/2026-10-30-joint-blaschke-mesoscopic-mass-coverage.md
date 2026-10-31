# Joint local zero extraction: uncovered mesoscopic mass nomination

TARGET: Review whether simultaneous local Blaschke extraction of neighboring Xi zeros can prove B_{epsilon<d log T<100 log log T}(T)=o(T(log T)^3) for every fixed 0<epsilon<1, with sparse neighborhoods retained.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches for zeta Blaschke suppression, sparse local counts, Fujii/Selberg moments and unconditional mesoscopic zero statistics; inspected primary passages and local L471/L474/L475/C483a plus the recorded aggregate stop. See drafts/2026-10-30-joint-blaschke-source-review-working.md. No adequate weighted sparse-neighborhood theorem was identified; no novelty claim.
SOURCE_EVIDENCE: Broughan II (2017), Theorem 3.3 proof (1),(4), pp. 26--27, https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48; Bettin arXiv:1111.0925v1 Theorem 1 p. 2, https://arxiv.org/pdf/1111.0925v1#page=2; Maples--Rodgers arXiv:1404.3080v2 Theorem 1.2 pp. 1--2, Theorem 2.4/Proposition 2.5 p. 5, (8) p. 6 and Section 4 pp. 8--12, https://arxiv.org/html/1404.3080v2. Read the full finite/central-zero cases and local-density bootstrap, including (18)--(23). Reuse Titchmarsh 7.2(A) and gamma coverage from the existing scale assessment.
COMPARISON: Joint extraction of all selected pair factors already occurs in L474/L475. Additional zeros are a real change, but Broughan supplies no local occupancy or weighted exception estimate. Maples--Rodgers counts multiplicities unconditionally; its mesoscopic CLT requires n(T) tending to infinity, counts ordinates rather than disk membership and does not weight by the pair quotient or disk norm. Proposition 2.5 is a concrete distinct local-density lead, with apparent normalization issues requiring a restricted audit before use.
GAP: No inspected input controls the full weighted sparse-neighborhood contribution or the fixed-displacement-scale annuli. No whole-sector little-o estimate or actual-Xi compensation follows from this review. Park the proposed joint-suppression implementation; separately audit the indicator local-density statement before any kernel application.
REASON: New comparison identifies substantive overlap with the stopped scheme and an essential count-versus-weight mismatch, so it changes the route without refuting the mass target. The source statement supplies a narrower independently testable continuation; apparent printed rescaling and weight-generality issues justify that audit, not an unverified import.
LITERATURE_REASON: The nominated target changes selected-pair extraction to all neighboring zeros at growing microscopic radii and requires sparse weighted exceptions; existing microscopic and scale-envelope coverage does not assess that change.
SCOPE: Actual Xi, every real T sufficiently large, every fixed 0<epsilon<1, full pair multiplicities and clipped windows. No RH, zero simplicity, local spacing lower bound, favorable cluster occupancy, external fixed-half-plane result, actual-prime-phase independence or Haar-to-height transfer is assumed.

## Exact proposed target and relevance

Using the definitions in L471 and L474, the proposed B is

    sum_(j in P_T, epsilon<d_j log T<100 log log T) m_j d_j^3
      integral_(J_j(T)) (1-v^2)
         |F_j(gamma_j+d_j v)/A(gamma_j+d_j v)|^2 dv.

Here F_j removes exactly one conjugate pair, even when that pair
has multiplicity m_j. The next review must check this normalization
against C483a's large-displacement mass before claiming sector
assembly. The main gap remains actual-Xi all-degree mixed positivity.
This intermediate target could control the sector between the known
small- and large-displacement estimates in L471's negative-mass
majorant. Even a full little-o negative-mass estimate would leave
pointwise signs, higher signs and RH unresolved.

The changed idea is to estimate a removed pair while retaining the
suppression from all other zeros in its local analytic disk, rather
than applying the same single-pair global supremum envelope on a
larger disk. That is a proposed mechanism, not an established bound.
It needs an honest alternative for disks without sufficiently useful
neighboring zeros. Empty/sparse neighborhoods cannot be presumed rare
from a global zero-count asymptotic alone.

## Source gate, duplicate check and bounded test

Before a mathematical attempt, retrieve primary hypotheses and
relevant proof cases for quantitative finite Blaschke division with
retained zero factors, applicable local zero counts and the precise
moment estimates needed on the proposed disks. Read the full relevant
L474/L475 arguments and recorded aggregate failure to decide whether
this change actually avoids the exponential envelope. The existing
source scopes do not license changing microscopic shifts to growing
ones. Broughan's cited primary preview is
https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48
and Bettin's is https://arxiv.org/pdf/1111.0925v1#page=2;
these are reuse leads here, not newly inspected passages.

Continue only if the comparison identifies a concrete joint-zero
inequality and a justified way to retain sparse neighborhoods at the
required scale. Stop this implementation if the available inputs
reduce to L475's envelope or require RH-equivalent local zero control.
Preserve any informative obstruction. No numerical evidence or
unspecified favorable zero statistics can pass this test.

If coverage supports a genuinely new mechanism, the later mathematical
attempt should be proof_attempt / creative / deep_research / max.
The precise escalation would be the mesoscopic contribution above:
test whether simultaneous extraction supplies the missing saving while
retaining sparse configurations, multiplicities and clipped endpoints.
For now the exact Next action is literature_comparison / standard /
high. Mathlib matching and all target-specific source coverage remain
unchecked. This assessment creates no new mathematical result.

## Completed comparison, 30 October 2026

The nomination above remains a record of the proposed mechanism, not an
approved mathematical continuation. The source review is complete for this
bounded search. No theorem matching the whole weighted sum was found.
This does not establish that the target is false or novel.

The exact L471 one-pair quotient, full multiplicities and clipping agree
in L474 and C483a. Their small and large sectors leave the strict open
mesoscopic interval in TARGET. L474 bounds its small sector by a uniform
constant times epsilon^3 T(log T)^3; it does not dispose of the fixed
positive annuli above epsilon. L475 already retains all selected factors
before one-pair division, including other copies of repeated zeros. Its
single-simple-pair example tests only a local analytic tool. Its exponential
envelope remains the preserved stop; the aggregate recovery stop is
procedural and supplies no mathematical ban.

Broughan permits additional finite zero lists, including real and central
zeros. It does not assert useful additional zeros in every actual-Xi disk.
An ordinate count alone is not a count in that disk: horizontal zeta
displacements must also be controlled. A continuous unweighted exceptional
measure alone is not a bound on the pair-quotient-weighted mass. These
missing comparisons cannot be silently replaced by generic occupancy,
simplicity, spacing, RH or a favorable correlation.

Maples--Rodgers gives genuinely relevant unconditional local counts. Its
Theorem 1.2 includes multiplicities, but requires a scale n(T) tending to
infinity and a fixed compactly supported bounded-variation test function
with divergent Fourier variance. It supplies no fixed-scale conclusion
or quotient norm. Proposition 2.5 offers a separate L2 local off-line
count route that can retain all sparse configurations through integration.
It has no zeta-amplitude factor, so any later application still needs its
own kernel and moment comparison. No such calculation is done here.

The source's (8) defines a displacement normalized by log T; its final
indicator substitution after (23) and its Cauchy-kernel domination need
reconciliation with that definition. Also (19) passes from cumulative
tails to general piecewise-continuous weights without an explicit
restriction adequate for our use. These are questions for a restricted
critical audit, not a claim that Proposition 2.5 is false or has already
been repaired. The full general-weight lemma is not imported.

The next independently testable target is recorded in
`2026-10-30-maples-rodgers-indicator-audit-coverage.md` for separate
approval. It audits only k=2 and c=1/4, using the source's count-only
inputs with their import qualifications. It neither approves the full
joint-suppression mechanism nor asserts a new creative bound. Source
normalization and weighted sparse coverage are the current blockers to
a justified creative attempt. Mathlib matching remains unchecked.
