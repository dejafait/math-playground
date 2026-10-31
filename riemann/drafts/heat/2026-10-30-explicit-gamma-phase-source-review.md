# Explicit gamma phase/count coverage review

2026-10-30. Literature only. No phase inequality, contour margin,
zero count, new lemma or mathematical script is established here.

Main gap: actual-Xi all-degree positivity; on the current heat-flow
route, finite positive-time collision exclusion remains missing.
Intermediate target: explicit phase/modulus inputs for a numerical
real/simple tail on 1/25<=t<=11/50. A successful tail could make the
remaining collision domain numerical, without excluding its collisions
or controlling t down to zero. Continue the full counting application
only with explicit strict margins and complete exhaustion; otherwise
isolate one independently testable component.

## Primary source inspected

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences 6 (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2).
Read definitions (5)–(11),(16), Theorem 1.5(i)–(ii) and (26), exact
derivative formulas (42)–(43), Proposition 6.6(i) and its proof
(75)–(76), Proposition 9.1(i) and its proof, and Lemma 9.2 and its
proof (100)–(101). Read both essential counting cases following
(102)–(104): the small-circle argument and nearest-center exhaustion.
These locations specify the inspected version; saddle proofs were
not audited. Earlier source evidence and the distinction between
Theorem 1.3's explicit range and Section 9's enlarged range remain in
[the residual source review](2026-10-30-explicit-positive-time-tail-source-review.md).

The source supplies a fixed holomorphic logarithm in (7), an explicit
alpha in (9), and the exact logarithmic derivative in (100). Formula
(43) requires Im(s)>3. The proof's (75)–(76) bound alpha' and alpha
at s=sigma+ix/2; its application has 0<=sigma<=1 and x>=200.
They retain numerical constants. In contrast, Lemma 9.2's local
variation and phase errors are O(log X/X), with no numerical
constant or onset. Theorem 1.5 and Proposition 9.1 retain unnamed
thresholds. Thus the explicit formulas are suitable inputs for a
separate quantitative specialization, rather than a numerical tail
already available by citation. Full matching Mathlib coverage unchecked.

## Comparison with the needed counting cases

L490 provides an additive normalized residual <153/10^6 on the closed
upper strip and prescribed height range. It supplies no relative
estimate at cancellation. The source's modulus bound in Proposition
6.6(i) is numerical, but a one-sided modulus bound is insufficient
to certify the local winding number near a cancellation of 1+gamma.

The small-circle case needs a numerical holomorphic local comparison,
including its nonvanishing normalization and a strictly larger boundary
modulus than its total error. The source's coarse display (104) alone
does not supply this; L488's audited qualitative proof retains the
common holomorphic factor of (102). The nearest-center case separately
needs quantitative center spacing, phase restriction, and localization
of EVERY zero in the strip into a counted disk. A count of selected
disks alone leaves exhaustion unproved. Both steps need time-uniform
constants and a padded spatial edge. None of these numerical margins
is established in this review.

The reflected lower half needs a justified normalization/error
comparison by conjugation, not an unstated extension of Theorem 1.3.
The source's real/simple theorem uses a global strip input, already
retained in L488. Its adjusted constants for |y|<=10 are unnecessary
for the proposed next component and are not numerical inputs here.
Floor-dependent f_t is not the holomorphic comparison function.

## Bounded continuation, not a completed inequality

Select a gamma-log linearization test, defined precisely in
[its assessment](../literature/2026-10-30-explicit-gamma-log-linearization.md).
It uses only the explicit logarithm and derivative formulas above,
on disks with |z-X|<=1 and X>=4*pi*exp(10000)+2. The source's
asymptotic lemma explains the intended linear model but does not
prove the proposed error 1/100. That numerical tolerance is a TEST
PARAMETER. Success could feed a later strict contour comparison with
L490. Failure must retain the failing term/domain and trigger a
reassessment before any counting claim. No count, exhaustion or
edge-transfer theorem is approved with this component.

## Searches, reuse and route limits

Queries included `Polymath 1904.12438 gamma phase explicit Proposition
6.6 Lemma 9.2 real simple zeros`; `"1904.12438" "phase" "explicit"`;
`"M_t" "gamma" "Polymath" "logarithmic"`; `"Polymath" "gamma"
"Lemma 9.2"`; `"1904.12438" "linearization"`; and explicit
heat-flow real/simple-cutoff searches. Results did not supply another
matching inspected theorem. Search snippets, unrelated zeta-zero
verification and secondary research portfolios are not theorem inputs;
no novelty or global absence is inferred.

Narrow local comparison used L490's hypotheses/imports, L488's phase,
circle and exhaustion proof ranges, the residual assessment, and
ATTEMPTS/2026-10-30-direct-numerical-tail-extraction.md and
ATTEMPTS/2026-10-30-tail-approval-loop-recovery.md. No matching numerical
gamma-log certificate was found in those checked paths. The new target
asks for explicit constants, so it neither repeats the existential-tail
audit nor resumes direct extraction of unspecified constants. Existing
generic shape/energy obstructions remain in force. No new theta-specific
input justifies a creative collision-exclusion mechanism in this step.
