# Exact trial trace — nomination for a separate conceptual audit

TARGET: Audit L762's periodic midpoint and all-N trace bound, including the finite-Fourier denominator, every seam/cutoff jump, mean and conditional tail.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact fixed-lambda endpoint/jump assessment 2026-11-04-ccm-boundary-trace-specialization.md and its parent 2026-11-04-ccm-projected-boundary-trace.md, including their duplicate/failure comparison; step376 added only the approved specialization, not a new source search.
SOURCE_EVIDENCE: Lebl section4.3.2/Theorem4.3.1 https://www.jirka.org/diffyqs/html/moreonfourier_section.html ; Batenkov2015 section2/Proposition6 pp2330–2331 https://dimabatenkov.info/pdf/batenkov_complete.pdf ; DLMF24.8.2–3 https://dlmf.nist.gov/24.8 ; Osipov–Rokhlin1301.1707v1 Theorem1/(27), Theorem3/(38), Remark6 https://arxiv.org/html/1301.1707v1#S3.SS1 . The latter exact statements were reopened in step376; other coverage is reused.
COMPARISON: The source methods already cover the same fixed trial's periodic midpoint and jump subtraction. The proposed audit checks the new explicit specialization, not a new convergence theorem or a stronger source claim; the qualitative CCM boundary-domain theorem still cannot replace the jump accounting.
GAP: The written L762 specialization has no separate critical audit. Its exact-mode denominator estimate, twelve periodic jumps, two integrations, mean, row normalization and conditional tail constants must be scrutinized. No lower bound for the limiting midpoint is supplied.
REASON: Separate source approval completed in step377 using the existing same-scope coverage and reopened primary statements. SPECIALIZE permits the exact conceptual audit as REPRODUCTION; no mathematical verification is claimed.
SCOPE: Only the exact trial and signs of L761, lambda=sqrt(13), L760's boundary row extended to integer N>=1, and the formulas/constants of L762. No ground comparison, new pointwise approximation, lambda family, denominator nonvanishing or Xi sign assertion.

Essential local mathematical inputs are L761's exact mode realization,
chi_n<726 and positive integral bounds, plus L760's row convention;
the basis is already explicit in L761. C761a is a preserved contrast,
not an input used to prove the trace. L759 is upstream through those
inputs; its finite Weil matrix is not a premise of the trace calculation.

The audit should test the whole claimed estimate for all integer N>=1,
not sample N. Specifically it must check that entire angular modes
justify the ODE energy integration and differentiated integral formula;
the finite-Fourier eigenvalues are bounded below rather than merely
nonzero; the r=13 isolated value contributes to neither inward trace;
the r=1 seam and all eleven interior cutoff jumps, including first
derivatives, are retained; mean and sqrt(L) factors survive; and the
sawtooth tail uses symmetric/conditional convergence with the correct
signs and geometric constant. Check the elementary arithmetic yielding
34000000/N. A correction belongs in the canonical proof with all
previous evidence preserved.

Continue if these steps establish exactly L762's stated midpoint and
bound, or repair a specific defect without expanding the target. Stop
the asserted estimate if a load-bearing gap cannot be repaired within
these hypotheses. Even a successful audit does not establish M!=0,
ground convergence, a lambda limit or positivity. The deliberately loose
bound cannot repair C761a's failed1/10 discriminator. Mathlib remains
unchecked. This nomination claims no new literature or mathematical
advance and no independent verification.

## Separate source approval — step377, 2026-11-04

The TARGET and SCOPE remain unchanged. This turn approves source adequacy,
not L762. The existing endpoint/jump comparison and its duplicate/failure
search were reused. L762 was read only to map its claimed inputs and
obligations to that coverage; no estimates were checked or derived.

Primary passages reopened for this approval:

- [Osipov–Rokhlin v1, section3.1, (26)–(27), Theorem1, Theorem3/(38), Remark6](https://arxiv.org/html/1301.1707v1#S3.SS1): c is positive and real, the eigenfunctions have unit L2 norm, and the finite-Fourier eigenvalues are nonzero. The continuous angular ODE solutions coincide up to scalar with these modes. Remark6 extends both the modes and ODE to complex arguments. The root assertions are unnecessary here. These are regularity and identity inputs, not the numerical lower bound for the eigenvalue claimed in L762. That bound and its use of L761 remain audit obligations.
- [Lebl, section4.3.2, definition and complete Theorem4.3.1](https://www.jirka.org/diffyqs/html/moreonfourier_section.html): a finite smooth partition with finite one-sided data and piecewise-continuous derivative gives periodic midpoint convergence, including the discontinuous case. The theorem uses half-period notation; its application must match the notebook's full period. It gives no effective rate.
- [Batenkov (2015), section2, (2.1), Proposition6/(2.2), p2331](https://dimabatenkov.info/pdf/batenkov_complete.pdf): the jump model includes periodic-endpoint jumps and nonzero-frequency coefficients. Neither the zero coefficient nor an effective bound for this trial is supplied by that identity. Reuse the parent assessment's explicit-polynomial qualification rather than its surrounding degree wording. The previously read 2012 integration-by-parts proof is reused, not freshly reopened.
- [DLMF24.8.2–3](https://dlmf.nist.gov/24.8): the first Bernoulli formula excludes endpoints; symmetric midpoint evaluation needs the convergence theorem. This check used the live formula page, without verifying its release metadata.

The exact trial therefore remains a standard-method specialization requiring
an independent audit. The mean, row normalization, all twelve periodic
value/derivative jumps, two piecewise integrations, conditional tail and
explicit constants must be checked in the mathematical turn. Geometric
summation and summation by parts are elementary steps written in L762,
not an uninspected external theorem being imported. No additional source
is essential before that audit. Mathlib coverage remains unchecked.

The preserved fixed-cell stop is
[the C761a observable miss](../../ATTEMPTS/2026-11-04-ccm-fixed-boundary-observable-miss.md).
It neither verifies nor refutes this all-N trace claim. Prior 96-mode
failure and 112-mode success remain recorded; no recalculation is done.
There is no new duplicate search or novelty claim. Repeating the adequate
source decision is honestly STALLED under the shared outcome rule,
although this separate approval removes the procedural gate for the
saved mathematical audit. No lemma, script, DAG or argument is changed.
