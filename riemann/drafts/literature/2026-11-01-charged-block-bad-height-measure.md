# Charged-block exceptional heights: completed source comparison

TARGET: Assess whether unconditional zero-density bounds imply meas{t in [T,2T]: K_t>0}=o(T) for C464c's charged degree, retaining arbitrarily small displacements.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact near-critical-line Selberg density, horizontal first moment, zero-neighborhood union and exceptional-set searches; checked C464c/L464/L018 and reused negative-middle, fixed-displacement and L486 all-mesoscopic-stop comparisons. Queries and inspected passages are recorded below.
SOURCE_EVIDENCE: Simonic arXiv:1910.08274v2 Theorem 1 pp. 1–2, Section 4.2 pp. 29–30 and complete Section 4.5 pp. 33–34, especially (74); Dobner arXiv:2101.01747v2 Section 4 Lemmas 5–8 and complete proofs; Baluyot et al. arXiv:2306.04799v1 Introduction/Theorems 1–3 only.
COMPARISON: The first source covers uniform microscopic density and an integrated O(T) bound; the second controls a weighted contribution above a positive threshold, not K_t>0. No inspected theorem supplies the exact o(T) union measure. Fixed-displacement density and conditional microscopic improvements do not fill that difference.
GAP: A count-to-union applicability proof and a sharp nonimplication test remain mathematical tasks; no union bound or lower bound for actual Xi has been proved here. All-height signs and exceptional-center control remain open.
REASON: Essential source coverage is now available, but it supports no direct import of the desired sublinear conclusion. Park implementation aimed at proving o(T) from these estimates alone; nominate one separate abstract density-saturation test with its own assessment.
SCOPE: Actual Xi and exact C464c K_t, all multiplicities, 0<d<1/2 without a cutoff, clipped [T,2T], strict charge |gamma-t|<d. No RH, simplicity or density conjecture. SPECIALIZE authorizes only later hypothesis matching of the inspected count inputs, not an asserted saving or new density theorem.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target newly retains all microscopic displacements; earlier fixed-cutoff coverage did not inspect the essential uniformity and exceptional-set hypotheses.

## Completed comparison and decision

The main gap is actual-Xi all-degree signs at unbounded heights. The
intermediate target is the exact TARGET. Its plausible use is to localize
centers needing further sign analysis; it could never alone imply RH.
The source-level continuation test fails for direct import: the inspected
results do not state the required o(T) geometric conclusion. This is an
informative source mismatch, not a proof that the desired estimate is
false or that every possible use of density information fails.

C464c's hypotheses and factor allocation were read, along with L464's
normalization/count hypotheses and L018's full zero correspondence.
C464c assigns 2m per conjugate pair with |gamma-t|<d; repeated pairs,
strict charge endpoints and arbitrarily small d are retained. Under L018,
each such pair corresponds to one right-off-line zeta zero with the same
m. Distinct blocks may share an ordinate; no spacing is assumed. The
existing coefficient proof and its completed audit are not repeated.

## Primary source statements and essential cases

Aleksander Simonic, *Explicit zero density estimate for the Riemann
zeta-function near the critical line*,
[arXiv:1910.08274v2](https://arxiv.org/pdf/1910.08274v2#page=2),
29 November 2019, Theorem 1, pp. 1–2: for H>=3.0610046*10^10 and
1/2<=sigma<=0.831,

    N(sigma,2H)-N(sigma,H)
      <=10395.2 H^(1-(sigma-1/2)/4) log H
        +1.104 log^2 H+0.173 log H log log H+0.51 log H.

Here N counts beta>sigma, 0<gamma<=H. Section 4.2's Littlewood formula
counts zero orders, so the estimate retains multiplicities. Complete
Section 4.5, pp. 33–34, was inspected: it extends to boundary ordinates
by continuity and handles the microscopic ranges by total counts.
In particular (74) already bounds the integrated density by a leading
O(H) term at sigma=1/2, with no vanishing factor. This is an inspected
source inequality, not a newly derived measure bound. The full moment
proof, constants and computation are not independently audited.

Alexander Dobner, *Large deviations of the argument of the Riemann
zeta function*, [arXiv:2101.01747v2, Section 4](https://arxiv.org/html/2101.01747v2#S4),
25 March 2024; published Mathematika 70 (2024), DOI
[10.1112/mtk.12251](https://doi.org/10.1112/mtk.12251).
Lemmas 5–8 and their proofs were read. Lemma 8 bounds
meas{|Z_lambda(t)|>V} by

    O(T exp(10 lambda-d' sqrt(V log T/lambda))),
    log log T<=lambda<=log T/2, 2<=V<=log T/lambda,

for large T and an absolute d'>0. Z_lambda is a signed smoothed
zero contribution, not a block-presence indicator. Its proof separates
local crowding and far zeros, then imposes a positive displacement
threshold. No implication from K_t>0 to this event is supplied.
The proof's displayed local denominator uses min where max appears
intended; no correction or independent proof audit is claimed here,
and the mismatch of observables does not rely on that step.

Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh,
*An unconditional Montgomery theorem for pair correlation of zeros
of the Riemann zeta function*,
[arXiv:2306.04799v1, pp. 1–2](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7377443/7377443.pdf#page=2),
7 June 2023, Theorems 1–3 and the intervening remarks were read.
Theorem 3 assumes N(sigma,T)=o(T^(2(1-sigma))) uniformly in its
specified microscopic range starting at 1/2+1/(2 log T), up to
25/32+eta. It is conditional; the introduction also identifies a
Selberg density improvement as a conjecture. Neither supplies an
unconditional missing factor. Theorem 1's full pair-correlation proof
was not read or imported; its unconditional label must not be transferred
to Theorem 3's hypothesis. The repository file is the v1 preprint,
not a claim to have inspected the published 2024 revision.

## Applicability obligations and limits

The exact union application is deferred. It must check the L018
one-right-zero-per-pair convention, multiplicities, repeated ordinates,
strict displacement cuts and finite clipping at T and 2T. An interval
of charge can meet the slab from outside, so a padded height range is
required. The source's strict beta>sigma convention must be respected;
positive sigma margin or integration avoids silently asserting equality
coverage. Theorem 1 must not be used above sigma=0.831; a later attempt
may use monotonicity at an allowed fixed sigma for that sector. The
source's dyadic and cumulative versions must not be conflated.

The source already treats d of order 1/log T using total counts. There
is no source justification for silently improving O(T) to o(T), discarding
that band, taking V down to zero in Dobner's lemma, or assuming a positive
lower bound for the smoothed contribution when a charged block exists.
No claim of optimality follows from an upper bound failing the target.
A separate abstract model test is needed to decide the logical strength
of the count assumptions alone. Its result would concern those
assumptions, not realizable zeta zeros.

## Reuse, duplicates, search record and unread leads

The negative-middle assessment dated 26 October covers the coefficient
mechanism. The fixed-displacement assessment dated 29 October covers
d>=1/16 with multiplicity; its Guth–Maynard/Ingham comparisons are reused.
Neither is an all-displacement union theorem. The preserved L486 stop in
ATTEMPTS/2026-10-30-local-density-all-mesoscopic-certificate.md concerns
a weighted energy certificate with a surviving displacement loss;
it is supporting comparison evidence, not a theorem about this union.
L611's sign stop and the completed C464c audit remain unchanged.

Queries included `Selberg zero density estimate uniform sigma 1/2 T log T`,
`zeta zeros sum beta minus 1/2 Selberg O T`, `zeros union Selberg critical
line measure`, `Selberg zero density bad set measure`, and Dobner's exact
title/Lemma 8. Local searches combined K_t, bad-height, height-union and
density/multiset terminology in this notebook's assessments and failures.
No inspected exact matching union theorem or duplicate of the nominated
abstract saturation test was found; no novelty is inferred.

Original Selberg (1946) Theorem 1 was located bibliographically but not
retrieved. Its result is not imported from a search snippet: Simonic's
inspected primary theorem supplies independent usable coverage. The
Conrey–Ghosh–Gonek PDF link returned 404; it is unused. The Dobner author
repository returned 403, resolved by the accessible arXiv v2. These are
not persistent essential source blockers. Improvements of the exponential
slope reported in introductions are unread leads, not imported results.
Full matching or supporting Mathlib coverage is not checked.

Outcome: NEGATIVE / LITERATURE / NOVELTY_UNCHECKED. New source comparison
parks direct density-only implementation of the desired saving; it does
not disprove the estimate. No lemma, mathematical script, DAG or PROOF
change, new measure estimate or countermodel was produced.

## Original nomination retained as historical scope

## Relevance, bounded test and remaining inputs

The main gap remains actual-Xi all-degree signs at unbounded heights.
The intermediate source question is the displayed sublinear-measure
threshold. If available, such control could combine with the known
window/nonnegative-block criterion to localize the heights still requiring
sign analysis. This is only a plausible downstream use; that criterion's
normalization, central factors and exceptional centers must retain their
own hypotheses. An almost-all-height conclusion would not resolve RH.

Start with the exact K_t definition in C464c and its underlying L464/L018
zero convention. Reuse the source and failure comparisons named above.
Retrieve primary zero-density statements and their essential proof cases
only as needed to determine sigma-uniformity near 1/2, height padding,
multiplicity conventions and logarithmic losses. Any fixed-positive-sigma
theorem must be distinguished from coverage uniform at microscopic
displacement. Selberg-type density bounds are an unread search lead,
not an available input. No source citation has been manufactured from
memory, and no claim of novelty or theorem absence is made.

Continue only if inspected bounds support a concrete test of the exact
o(T) measure threshold, or an exact source already supplies it. If the
best covered conclusion leaves an O(T) or larger loss, record that
limitation without claiming an actual lower bound on the bad set. Park
this density-only implementation rather than returning to a fixed-cutoff
estimate or relabeling an energy calculation. A later mathematical test
requires IMPORT, SPECIALIZE or EXPLORE coverage saved in advance.

## Mechanism comparison and routing

Reciprocal double-zero sign development remains stopped: L611's audit
does not control its coefficient. Another C464c proof audit would repeat
the recorded completed audit and its duplicate-replay failure. Select the
different height-union/density question above, which targets where
offending blocks can occur, not their coefficient-tail algebra or the
weighted quotient mass in L486. The latter's microscopic logarithmic-loss
stop remains relevant comparison evidence, not a theorem about this set.

This nomination is not approved mathematics. No measure identity, bound,
lemma or calculation was derived. A genuinely creative all-height
mechanism is not yet justified: independent control at exceptional centers
and the missing cutoff coefficient sign remain absent. Do not label a
standard density specialization creative to satisfy scheduling preference.
Full matching or supporting Mathlib coverage for this target is not checked.
