# Endpoint-null nonvanishing: second-order coefficient discrepancy

TARGET: Resolve the M=2 Laguerre B_0 normalization discrepancy in the endpoint-null nonvanishing attempt against primary formulas, keeping eventual definition unproved until the coefficient and remainder are justified.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step262 compared exact DLMF18.15.20/factor2 queries and Frenzen-Wong1988/PDF leads, then inspected GST1609.00829v1 and1709.09656v1; scoped reviews258/259 and step261 contain no prior normalization resolution. Earlier filter overlap/stops are reused; no novelty inference.
SOURCE_EVIDENCE: Inspected GST1609.00829v1 section2.1.3 equations20-34 https://arxiv.org/html/1609.00829v1#S2.SS1.SSS3 and GST1709.09656v1 sections3.3-3.3.1 equations77-98 https://arxiv.org/html/1709.09656v1#S3.SS3; DLMF18.15.17-20,10.17.1-3/iii,18.9.1/Table18.9.1 and errata; Temme1990 section2.1/equation2.1. Original Frenzen-Wong full text remains unread behind access routes; alternate primary formula/uniformity coverage is accessible. Full dictionary/qualifications: 2026-11-10-laguerre-normalization-source-notes-262.md.
COMPARISON: GST uses v=N/2 and C=-D for DLMF's printed D=B_0, so its first correction is2D/(N*sqrt(xi)), whereas DLMF18.15.19 prints D/(N*sqrt(xi)); leading prefactors/arguments agree. Use the GST uniform expansion directly, not a silently corrected DLMF theorem or a numerical fit. No official erratum or original-paper error is asserted.
GAP: Source normalization comparison is complete for a restricted later specialization; endpoint gamma values, the additive O(n^-2) specialization and exact-degeneracy exclusion remain unproved. Original Frenzen-Wong error proof and full matching Mathlib coverage remain unchecked; neither is substituted by numerical evidence.
REASON: New inspected formulas change the second-order source choice and identify a factor2 incompatibility between published presentations. A later mathematical turn can specialize the accessible GST uniform contract; this literature-only step proves no nonvanishing result and changes no lemma or mathematical script.
LITERATURE_REASON: Step261's finite discrepancy changed the precision required beyond the reused first-order assessment; primary coefficient and remainder normalization was essential unread coverage.
SCOPE: The same fixed three-degree filter, n integer, common interval [n,2n], and tau=10^13; inspect only coefficient normalization and remainder for p_n=L_n^2 at u=n,2n, alpha=2, nu=4n+6. No filter/quartet sweep or new signed arithmetic target.

## Original evidence to inspect (nomination preserved)

The canonical partial result is L990: exact endpoint constraints,
controlled signed rate1/2 on an infinite defined subsequence, a
uniform upper bound on all defined indices, and the exact necessary
condition for degeneracy. Cofinite definition remains open. This
nomination does not revoke or critically audit its first-order proof.

Unfinished second-order reasoning is in
`drafts/2026-11-10-endpoint-null-filter-working-261.md`. The finite
diagnostic and reproduction script are
`scripts/endpoint-null-filter/phase-check-261.json` and `.py`.
It has 90-digit Decimal arithmetic without interval enclosures and
is not a rigorous asymptotic certificate. All ten rows were inspected;
selected last-row values can be read with
`python3 ../scripts/loop/inspect_json.py scripts/endpoint-null-filter/phase-check-261.json --pointer /rows/9 --full`.

The literal proposed upper-endpoint first phase coefficient is
about -0.468660337. The finite recurrence extraction at n1024 is
about -0.541033689, and the n^2 residual there is about -73.1905,
versus36.6356 at n512. This warrants checking the source-to-formula
normalization; it does not prove a DLMF error or invalidate a
uniform O assertion. A formal alternative multiplying the B_0
contribution by2 is recorded only as an unverified lead, not as
an authorized replacement theorem.

First retrieve the primary formulas with their precise normalizations,
fixed-parameter hypotheses and the relevant remainder construction.
Compare the exact p_n recurrence, the prefactor, nu, xi, the Bessel
first sine coefficient and the B_0 multiplier before larger passages.
Inspect an erratum or independent primary formula if needed. Do not
substitute a fit for an analytic proof, assume a source typo, or
derive/approve the subsequent nonvanishing proof during this review.

## Continuation and stopping test

Approve a later specialization only if the coefficient and the
uniform remainder on a compact bulk interval are justified by the
inspected source(s), with every changed factor explicit. If the
discrepancy remains inaccessible, retain SOURCE_BLOCKED and park
the second-order branch; the established first-order partial remains.
A demonstrated mistake in the local substitution should be recorded
plainly. No exact-degeneracy exclusion is established by this review.

L985's finite connection and L990's reduction are essential local
inputs. L987 is the synthetic benchmark, L988/L989 motivate endpoint
removal, and steps233/235/244 remain scoped contrasts. Eventual
definition is unproved; actual-zero realization, other-zero control,
the original B_n/criterion transfer and both complements remain
independent gaps. No cross-notebook result is used. Full matching
Mathlib coverage remains unchecked. A later audit of L990 remains
distinct from this coefficient source check.

## Completed comparison — step262

The [source record](2026-11-10-laguerre-normalization-source-notes-262.md)
contains the exact parameter/prefactor dictionary, the conflicting
first corrections and access qualifications. The accessible GST2017
uniform contract, corroborated by GST2016's explicit alpha formula,
replaces reliance on the literal DLMF correction for this branch.
Do not combine a changed coefficient with DLMF's remainder assertion.
No new endpoint phase coefficient, integer-norm limit or nonvanishing
claim is established here. The original diagnostic stays unmodified.

This is an informative source-negative outcome: it changes which
published formula the attempted proof may use. It is not progress
beyond the inspected literature, an audit of L990, or an RH candidate.
The [separate continuation assessment](2026-11-10-endpoint-null-cofinite-definition-review-262.md)
nominates a bounded REPRODUCTION specialization for separate approval.
