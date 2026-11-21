# L900 frequency-weighted Xi interpolation — audit coverage

TARGET: Audit L900's frequency-weighted normalized Xi-defect bound, checking the unit-circle coefficient estimate, uniform squared-height removal, real normalizer variation and the constant K on the full closed height square.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the prior ready 2026-11-08-frequency-weighted-xi-defect-interpolation.md assessment and its exact-target searches; step115's scoped local terminology search found no earlier matching frequency-weighted normalized two-height lemma. No new mathematical hypothesis or source claim is introduced by this audit target.
SOURCE_EVIDENCE: Existing L320 (4)/(6); NIST DLMF v1.2.8, 1.9.30/31 and 1.10.1, inspected in the prior comparison; audited L899 (5)/(6)/(9) for logarithmic sinhc variation and finite Q; L898 (2) and its zero-height identity for actual-Xi normalization. Exact primary URLs and applicability are recorded below and in the canonical L900 proof.
COMPARISON: L900 specializes the already assessed uniform product envelope and Cauchy/Taylor tools; the proposed audit checks that specialization, not a new growth theorem, sign mechanism or extension of the assessed domain.
GAP: Independently check the coefficient bounds, termwise differentiated series through t=0, both real quotient terms and all constants; the lemma is written but has not received this separate audit. Numerical K, reference margins, relative small-value control and all-degree signs remain outside scope.
REASON: The separate literature-only approval step116 confirms adequate coverage for this exact audit; proceed to the bounded proof replay without another source-approval turn. This approves scope, not correctness of L900.
LITERATURE_REASON: The supervisor explicitly required a separate approval turn for step115's newly written continuation; existing adequate coverage is reused, with only the primary Cauchy/Taylor hypotheses rechecked.
SCOPE: Only L900 for actual Phi and Xi, real x and 0<=v,y<=1/2, with power 5, rate pi/2 and factor |y^2-v^2|; no new lemma, parameter domain, numerical constant or sign premise is proposed.

## Reused sources and exact audit scope

The ready [source comparison](2026-11-08-frequency-weighted-xi-defect-interpolation.md)
covers this same mathematical inequality and its full closed height
square. Its imported analytic tools are Cauchy's formulas in
[NIST DLMF 1.9.30–31](https://dlmf.nist.gov/1.9#iii) and analytic
Taylor expansion in [1.10.1](https://dlmf.nist.gov/1.10.E1), version
1.2.8 (15 September 2026). No new external retrieval was performed
or is required for the audit. The entire function H_x, the unit
circle and the interior Taylor disk meet those source hypotheses.

[L900](../../lemmas/L900-frequency-weighted-normalized-xi-defect-interpolation.md)
now contains the complete specialization. Inspect L320 (4)/(6),
L898's actual-Xi defect/zero-height identity, and L899's scalar
logarithmic bound and finite-Q argument only as needed to replay it.
The prior source comparison contains the primary growth-source
qualifications; an inaccessible alternate Rademacher source is not
an essential dependency. The L899 audit is recorded canonically in
that lemma, and its Sprungk theorem need not be reapplied to L900.

The audit should verify these existing proof steps, without enlarging
the target: R=1 gives product power 9/2 and preserves the exponential
rate for every real x; Cauchy's coefficient formula bounds the even
series; differentiation is uniform on the closed t-interval; the
identity C_y=F_x(y²) includes zero; the real exponential mean value
bound is integrable with Q; and both quotient terms yield the stated
K. It must not replace this by pointwise removability or divide by
a complex normalizer. No independent audit is claimed in this file.

The earlier full-L1 result L899 remains the unweighted comparison.
L898's fixed cross-endpoint stop and L312's qualified ordering failure
are not negated by an absolute interpolation estimate. A separate
signed-margin mechanism is still missing. Mathlib coverage of the
full result and supporting analytic tools remains not checked.

Continue if the exact inequality survives the audit. If a constant,
endpoint or hypothesis fails, repair that issue within the assessed
scope or record the failure; do not silently weaken the target or
promote the error estimate into a sign theorem. This is an ordinary
proof replay, not a creative attempt or candidate-RH review.

## Separate scope approval (2026-11-08, step116)

Reused the prior comparison's exact-target searches and inspected
source evidence, including its duplicate and failure comparisons;
no novelty search or broader theorem claim is added. Read L900 to
locate the proposed audit obligations, L320 (4)/(6) and the intervening
product-envelope argument, L898's normalization and defect identity,
and L899 (5)/(6)/(9) with its recorded step113 audit. These are
coverage reads, not an independent replay of L900's inequalities.

Reopened the primary [Cauchy statement](https://dlmf.nist.gov/1.9#iii),
equations 1.9.30–31 and their hypothesis paragraph, and
[Taylor's theorem](https://dlmf.nist.gov/1.10#i), equation 1.10.1
and the radius-of-convergence sentence. The retrieved Cauchy page
identifies version 1.2.8, release 2026-09-15. Cauchy's formulas
require interior analyticity, continuity through the contour and an
interior evaluation point; Taylor's theorem assumes analyticity on
the open disk. L900 explicitly uses an entire product and a fixed
unit circle, so the proposed audit is within this source scope.
The sources do not assert the normalized inequality or its constant.

All essential coverage is available. The next research step must
independently replay L900 (3)–(9), including its differentiated series
on the closed squared-height interval, the zero-height identity,
the integrable real-normalizer comparison, both quotient terms and
the final frequency conversion. This turn does not certify any of
those conclusions or change the lemma. No numerical K, independent
signed margin, complex normalizer nonvanishing, relative small-value
control or all-degree positivity is supplied or assumed. The failed
fixed cross-endpoint and oscillatory-ordering routes remain stopped
in their stated scopes; neither is a reason to reject this absolute
estimate audit. Mathlib coverage remains not checked.

Decision: retain SPECIALIZE and the unchanged TARGET. This is a
scope approval with no new mathematical evidence, honestly recorded
as STALLED rather than a mathematical advance. Proceed directly to
the approved audit; do not schedule another approval of this same
unchanged assessment. No source blocker requires a different target.
