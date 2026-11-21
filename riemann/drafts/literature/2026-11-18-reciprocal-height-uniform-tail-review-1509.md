# Reciprocal-height degree-uniform tail target1509

TARGET: Establish or refute constants C,A_0>0, independent of d, such that |integral_(|y|>A d) f_d(y)dy|<=C d/A for every integer d>=3 and real A>=A_0, with f_d(y)=log|P_d(y-b_1)|-d log|y|.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1510 searched uniform Jensen convergence/coefficient bounds, Appell exterior asymptotics and logarithmic tails; compared C028a-d and reused source-notes1500/1507 and the named reference-budget stops. Queries and retrieval limits: 2026-11-18-reciprocal-height-uniform-tail-source-notes-1510.md. No exhaustive novelty claim.
SOURCE_EVIDENCE: Craven--Csordas, Pacific J.Math.136(2) (1989), Lemma2.2 pp244-245/(2.13)-(2.21), https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf ; O'Sullivan arXiv:2007.13582v2 Section3.1 Theorem3.1 proof sketch and Section3.2 Lemma3.4/(3.3)-(3.4), https://arxiv.org/html/2007.13582v2#S3.SS2 ; Boyer--Goh arXiv:0809.1266v1 Section3 Theorem1/proof/Corollary1 p4, https://arxiv.org/pdf/0809.1266v1 , is a hypothesis-limited comparison, not an input.
COMPARISON: Arbitrary-entire Jensen approximation and classical Cauchy coefficient control cover a local analytic method without RH; the product formula covers the proposed centering method. No inspected theorem states this exact degree-uniform signed-tail bound. Appell compact asymptotics do not provide unbounded-tail domination under the actual hypotheses.
GAP: Verify the centered coefficient specialization, obtain a degree-uniform small exterior logarithm with integrable decay, and prove the C d/A bound for every d>=3 and A>=A_0. These quantitative applications remain unproved; C028d's fixed-d root bounds cannot be substituted silently.
REASON: Approve only a known-method specialization for the original target, isolating the exterior from the independent RH-equivalent central cancellation. No general Jensen or Poisson-Jensen reproof and no new central-height mechanism is justified by this coverage.
SCOPE: C028a's unchanged actual entire F and monic P_d, C028b's reciprocal scale, C028d's centered coefficient definitions, all integers d>=3 and real A>=A_0; constants may depend on the fixed family but not on d or A. No root reality, global logarithm or degree-limit integration is assumed.

At nomination1509 this was an uncovered continuation. No derivation or
source search for it was performed during the finite specialization1509.
Separate literature review1510 now supplies source approval for the same
target, not its mathematical proof. C028d awaits an independent audit;
this source approval does not certify that proof or strengthen it.

Use the unchanged actual polynomial, normalization and positive coefficients
from C028a, C028b's reciprocal scale and multiplicity convention, and
C028d's centered function, absolute integrability and exact fixed-degree
tail. C028a and C028c's norm-budget stops are contrasts, not inputs.
Do not infer uniform constants from C028d's K_d, assume root reality,
or pass a degree limit through an integral without a proved estimate.

The intended bounded mathematical test, after coverage is ready, is the
single displayed C d/A bound for actual coefficients, with explicit
constants or a rigorous actual-family obstruction. A proof with arbitrary
d-dependent constants does not pass. A counterexample for a different
polynomial family alone would not refute this actual-family statement.
Review1510 found applicable methods rather than an exact imported bound.
Retain the correct degree range and prove any required cutoff hypotheses.

Even a successful bound only controls the outer signed contribution.
The central signed-log estimate needed for H_d=o(d), and hence the main
RH-equivalent gap in C028b, remains an independent unresolved problem.
The separate review1510 completes the original source gate. The next
turn may attempt exactly this target under this SPECIALIZE assessment;
the old finite-degree assessment1507 alone would not authorize it.
Full matching Mathlib availability is unknown.

## Approval1510: remaining applicability checks

Read primary statements and essential proof cases as qualified in
[source-notes1510](2026-11-18-reciprocal-height-uniform-tail-source-notes-1510.md).
The arbitrary-entire approximation theorem is usable without LP or
hyperbolicity. Some older PDF displays are OCR-obscured; no exact
convergence rate from them is needed or imported. O'Sullivan supplies
a legible compact limit and formal product identities. Only their
actual normalization, centering and quantitative local-log application
need checking. A direct coefficient estimate is justified for that
difference; do not reprove the general approximation theorem.

C028d already supplies c_(d,0)=1 and c_(d,1)=0. A subsequent proof
must justify any identification with coefficients of e^(-b_1 u)F(u),
then obtain estimates uniform in d before integrating. Compact
convergence alone is not an integrable tail bound. Handle all smaller
degrees if the proof initially yields only an eventual estimate.
The exterior target need not use C028d's unaudited full-line identity.
That identity and the central payment remain separately qualified.

Continue only upon explicit uniform constants or a rigorous actual-family
obstruction. A stronger absolute-tail estimate is an admissible method,
not a result of this review. Preserve both reference-budget stops.
This ordinary specialization is not creative research or progress beyond
the sources checked. The absent central cancellation mechanism blocks
a justified creative nomination here; the approved outer-tail test
should be completed before further source searches on this unchanged
target. A changed target still needs its own separate source review.
