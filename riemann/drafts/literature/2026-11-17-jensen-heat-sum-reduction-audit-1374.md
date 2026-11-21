# C019k specialization audit: continuation1374

TARGET: Audit C019k's uniform heat-sum reduction against Polymath v2 Theorem1.3/(5)-(24), checking the gamma normalization, all three errors, cutoff equality cases and one band-uniform onset.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment1373's exact-target search and source comparison, plus assessment1372's recorded overlaps and signed-block failures; the audit concerns the same specialization and unchanged hypotheses. No fresh discovery search or originality inference is needed.
SOURCE_EVIDENCE: https://arxiv.org/html/1904.12438v2 (1)/(4)-(24), Proposition6.2/(49)-(58), Corollaries6.4-6.5/(68)-(74) and Proposition6.6 inspected; https://dlmf.nist.gov/5.11.E3 with (5.11.4) and its fixed-sector hypothesis inspected. C019j's full proof and L018/L021 conventions were read in step1374.
COMPARISON: The known theorem supplies a pointwise effective two-sum formula even at small positive time; C019k supplies the coupled-scale conversion with existential absolute constants. Its proof needs verification of specialization, not a new Riemann-Siegel theorem or signed-moment estimate.
GAP: Independently replay C019k's normalization and inequalities with the actual floor and exact t(Y); no signed margin or Jensen count is included in the audit target.
REASON: Separate literature approval completed in step1375; the unchanged audit target is ready for research. Approval establishes source coverage, not correctness of C019k.
SCOPE: Exactly C019k's actual xi and C019j band, integer d tending to infinity, t=Y^2/(2d), principal source branches and gamma-only m(Y); no RH, nonvanishing, effective onset, moment or root-count assertion.

The completed research step is a reproduction/specialization of named
known estimates, recorded in C019k. The audit must check (4)--(8) for
uniform constants, the source multiplier in (9)--(10), the nonzero gamma
ratio in (11)--(12), both finite-sum errors in (13)--(14), and the full
uncorrected remainder in (15)--(16). At a_src=k the source floor gives
N=k and p=1; its endpoint case must remain included. Check that the
finite list of thresholds really admits one d_0 on the closed band.
Do not extend a fixed-positive-time asymptotic to the moving-time regime.

Continue with the reduction if these checks retain (3). If a factor,
source hypothesis or uniform bound fails, preserve the failed claim and
repair only what is justified; do not infer failure of RH. The audit
does not approve any new signed-moment mechanism. Such a mechanism still
needs a concrete bounded test and essential source comparison before a
creative research attempt. Matching Mathlib coverage remains unchecked.

## Separate source approval1375 — 17 November 2026

Reused assessments1372/1373 for discovery, duplicates and stops1345/1355/559.
Read C019k to delimit the audit; did not replay its estimates.
LITERATURE_REASON: Required separate approval of the newly nominated audit;
no additional discovery search or target extension.

Reopened the primary v2 text (4 August 2019), (1), (5)--(24),
Proposition6.2/(49)--(58), Proposition6.3's hypotheses, and
Corollaries6.4--6.5/(68)--(74). The effective domain includes y=0
and arbitrarily small positive t. The actual floor and the closed
[-1,1] bound for C_0 impose no integral-cutoff exclusion.
The uncorrected remainder remains essential. Proposition6.6(iv)--(vi)
and its passage to (24) were inspected as the error-source map.
These citations cover the audit's source inputs; they do not themselves
certify the coupled-scale bound.

Reopened DLMF5.11(i), (5.11.3)--(5.11.4): the stated sector is
|ph z|<=pi-delta and g_0=1. Applying this with C019k's gamma
argument, checking conjugation, and obtaining a common onset remain
mathematical audit obligations. No new proof or calculation is recorded.

Decision: retain SPECIALIZE and the exact TARGET. Source access is
adequate; proceed directly to that audit. No matching Mathlib theorem
was checked. This approval adds no mathematical result or new signed
mechanism; creative work remains blocked by an unpaid quantitative
signed-margin test.
