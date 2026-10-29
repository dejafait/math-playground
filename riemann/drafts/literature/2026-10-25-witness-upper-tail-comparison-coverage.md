# Witness/upper-tail range comparison — source-scope approval

TARGET: Determine whether L463's upper-tail positivity can shorten L461's finite negative-witness range, retaining exact thresholds, integer rounding and existential onsets.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact logarithmic-order and initial-sign searches in the completed initial-sign comparison, the L461 construction assessment and the L463 import assessment. Searched those specific assessments and the L463 application-audit history for shortening, combined ranges, intersection and rounding; the combined consequence is nominated but not established there. No claim of exhaustive novelty search.
SOURCE_EVIDENCE: Reused inspected bramble_trace v4 Theorem 1b (4b), definitions (1)–(2), Sections 4.2–4.5 (18a)–(18n), and Titchmarsh second edition Theorem 14.2, pp. 336–337, with its changed-domain comparison; read L461's full conclusion and L463's full statement/application audit. Primary proof-case coverage is retained in the linked prior assessments, not newly audited here.
COMPARISON: The inspected source supplies the upper tail; L461 supplies the separately proved witness cutoff. Neither reused assessment records their exact combined integer range. Only elementary application and range comparison remain within this target; no fresh analytic estimate is required.
GAP: Establish or refute a useful shortening in a later mathematical step, distinguishing eventual heights from all heights, fixing parameters before height varies, and preserving the two logarithms and every rounding operation. No combined consequence is proved in this review.
REASON: Existing essential source coverage is adequate for this bounded specialization. The pending gate can be approved without another external search or reproof; approval itself supplies no new mathematical evidence.
SCOPE: Actual Xi with L018's normalization; precisely L461 and L463 as written, arbitrary central multiplicities and both signs of real centers; fixed c>3/16 and fixed c_0>3/8; existential constants/onsets only. Authorizes range comparison and its necessary elementary applicability argument, not a new sign mechanism, effective bound, endpoint or source audit.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED for the exact combined range question. This separate approval reuses adequate component assessments and their inspected primary proof cases; it does not refresh already ready analytic coverage.

## Main gap, intermediate target and test

Initial signs at unbounded heights remain the immediate gap; global
mixed positivity and bounded-height overlap are independent gaps. The
intermediate target is exactly TARGET above. A shortening could reduce
the sign workload for excluding a hypothetical nonreal zero. It need
not resolve the other gaps to be useful.

Continue to one mathematical range comparison if both inputs have the
same coefficients and their recorded hypotheses suffice. That condition
is met at the statement/coverage level: both use the actual analytic
product H_a(y), and their normalization and central-zero issues already
have application audits. Determine the exact remaining integer set and
whether any admissible fixed choices make it strictly smaller at large
heights. If they do not, record redundancy or an obstruction. Abandon
any stronger inference requiring the boundary coefficients, a uniform
parameter limit, missing initial signs, or an effective height overlap.
These are proposed tests, not established range consequences.

## Reused primary coverage and exact scope

bramble_trace, *Generalized Laguerre positivity at growing orders*,
[rStation paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
displayed v4, 24 October 2026, 07:18 UTC, Theorem 1b, equation (4b),
assumes 1/2<=sigma_0<1 and zero-freeness on Re(s)>sigma_0. For each
fixed c_0>sigma_0-1/2 it gives one eventual onset, independent of order,
for strict positivity at all integers 2n>=c_0 log(t/(2pi)). There is no
upper cutoff. The [initial-sign assessment](2026-10-25-initial-laguerre-sign-coverage.md)
records the primary definitions and essential shifted-saddle and
all-order overlap proof cases actually read. The
[import assessment](2026-10-25-logarithmic-upper-tail-import-coverage.md)
and canonical L463 retain negative centers and central zeros. Reuse
those readings; neither a fresh source-version claim nor a full
manuscript audit is made in this turn.

L461 states that every hypothetical nonreal zero a+ib forces some
negative D_n with 1<=n<=ceil(c log(2+|a|)+B_c), for each fixed c>3/16,
with B_c>0 independent of a and of displacement/multiplicity. Its
[construction assessment](2026-10-24-fixed-half-plane-witness-cutoff-coverage.md)
records Titchmarsh, *The Theory of the Riemann Zeta-function*, second
edition (1986), Theorem 14.2 and proof, pp. 336–337, especially
(14.2.5)–(14.2.6), and the relevant complex Stirling coverage. The
printed theorem assumes RH; the changed-domain application is proved
and separately audited in L461, not imported by substituting 7/8 into
Titchmarsh's statement. No part of that analytic proof needs reproof
for the proposed elementary comparison.

Both inputs retain OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re s > 7/8*, September 30, 2026, Theorem 1.1, commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a. The strict half-plane permits
the pole and excludes neither boundary line. Its manuscript/import
closure and bramble_trace's analytic proof remain locally unaudited.
The [external register](../../foundations/2026-10-quasi-riemann-input.md)
and [overlap assessment](2026-10-21-openai-quasi-rh-overlap.md) were
consulted; no stronger external premise is introduced.

## Duplication, failures and permitted next work

The initial-sign comparison already distinguishes the two occurrences
of 3/16 and says that the source does not fill the initial segment.
That warning is retained; it is not an exact combined-range theorem.
The scoped searches found no established shortening in these records.
This is a local duplication check, not evidence of mathematical novelty.

Reuse its recorded L251/L257/L354 masking and count/gap obstructions:
they block generic sufficiency of finite signs or coarse counts, not
this comparison of inputs about actual Xi. L462's fixed-anchor and
L322's exterior-anchor stops remain intact. No countermodel, anchor
calculation or discarded sign mechanism is reopened. C460b's distinct
quantitative margin is not replaced by a sign-only comparison.

The next research step must retain the exact thresholds above, include
integer-boundary cases and the independently existential constants,
and state its bounded-height remainder. Do not infer uniformity as c
or c_0 approaches its strict lower boundary. Essential mathematical
inputs are L461 and L463, with L018's convention; the retained external
premise is an unresolved trust qualification, not a new local theorem.
SPECIALIZE authorizes REPRODUCTION for this elementary application;
no originality claim or new source theorem is intended. A separate
canonical result is warranted only if the mathematical comparison
actually produces a useful statement. Full matching Mathlib coverage
is unchecked; absence is not asserted.

This literature-only approval changes no argument, lemma, DAG or
mathematical script. The target text is unchanged and its existing
pending assessment is now ready for the next mathematical invocation.
