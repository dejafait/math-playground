# Regular-background stopped-density audit — scope952

TARGET: Audit C466r's class-uniform stopped-density bound, including the fixed-time variational law, finite-lifetime stopping, measurability and the measurable-set modulus.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-target discovery and local duplicate/failure comparison in review950 at step951 and its approved attempt assessment951; this audit keeps precisely those H, metric, time and stopping hypotheses. No fresh search or novelty claim is made.
SOURCE_EVIDENCE: TNV JHEP10(2017)100 arXiv1706.03822v2 AppendixB(B.1)–(B.5) p22 and Section2.2(2.19)–(2.21), footnotes1–2 p6 https://arxiv.org/pdf/1706.03822v2; source scope and non-applicable global/changed-metric conclusions are recorded in review950. Standard named inputs are smooth ODE existence/continuation/dependence and the differential Gronwall inequality.
COMPARISON: TNV supplies nonsingular fixed-time variational machinery, not the arbitrary-H bound. C466r adds the inequality |S''|-|S'|^2<=M_2+M_1^2 and a stopped measurable envelope. C466q is the H=0 comparison, not a premise of that estimate.
GAP: Independently verify C466r's claimed specialization and its boundary and class-uniform quantifiers; global signed integration, tangential coupling, endpoints, all-order signs and Xi transfer are outside this audit and remain open.
REASON: Separate literature approval completed at step953: source coverage is sufficient for the exact conceptual audit, with TARGET and SCOPE unchanged. This approves audit invocation, not C466r's correctness or the earlier attempt retroactively; the next turn is mathematical audit, with no further literature approval needed on this unchanged scope.
SCOPE: C466r only, with 0<a<R<infinity, H holomorphic on D_R, finite H(0), uniform |H'|<=M_1 and |H''|<=M_2, unit flat raw flow, initial ir, fixed physical time, first zero hit/escape and zero-extension density. No new mechanism or strengthened global conclusion is preapproved.

## Reused coverage and exact audit

The full primary-source comparison, precise versions, inspected
cases, queries, unread leads and failures remain in
[review950 completed at step951](2026-11-14-regular-background-weighted-flow-950.md).
The original mathematical target was approved in
[assessment951](2026-11-14-regular-background-weighted-flow-attempt-951.md).
No new essential source or changed hypothesis has been introduced
by this audit target. No broader literature survey is requested.

Read the complete canonical C466r proof. Check the conjugation on J
and the fixed-time initial derivative i; then check the full-density
squared-norm estimate, the cross term in |S'|^2, and the uniform
completion of the square. Confirm that Gronwall does not hide a
zero cutoff and that the claimed initial weight bound follows on
the straight segment inside D_R.

Independently check that a finite maximal punctured-disk lifetime
has a zero or boundary limit under the stated derivative bound,
and that the open smooth-flow domain gives Borel stopped densities.
The stipulated zero extension must be used only as a definition;
no trace regularity, through-zero Jacobian, distributional equation
at a stopping boundary or conserved integral may be silently added.

Finally verify all quantifiers in the measurable-set modulus and
the supremum over H sharing the data. The decisive test is a valid
bound for every measurable E and every finite fixed T_0, including
moving hitting/escape boundaries, or a precise flaw/counterexample
to a claimed step. It is not enough to check H=0 or origin mass.
C466q may be used as the exact control but is not a direct
mathematical input of C466r's proof. Essential result under audit:
C466r. No cross-notebook input is involved.

This is conceptual verification of a local analytic estimate, not
a creative central-sign attempt. The signed-contour connection to
actual-Xi determinant positivity has not been supplied. Preserve
stops927/932/941/947/948 and all independent global gaps regardless
of the audit outcome. Full matching Mathlib coverage remains not
checked, rather than established absent.

## Separate approval953 — 14 November 2026

Reused review950 and assessment951, including their exact-target searches,
reference comparisons and recorded stops. Read C466r's hypotheses,
conclusion and source-convention passage only to compare scope; its full
proof has not been independently audited in this literature-only step.

Reinspected TNV v2 Appendix B (B.1)–(B.5), printed p22, and
Section 2.2 (2.19)–(2.21) with footnotes 1–2, printed p6, using
the [PDF](https://arxiv.org/pdf/1706.03822v2) and
[HTML Appendix B](https://arxiv.org/html/1706.03822v2#A2).
HTML numbers the Appendix equations (69)–(73); (73) matches PDF
(B.5). The real initial variation and conjugated Jacobian are explicit.
The zero example omits nonsingular terms; its bounded-weight discussion
does not prove the arbitrary-H estimate. Section 3's different metric
remains outside scope. These observations confirm existing coverage,
not a new theorem or new obstruction. Standard smooth ODE and Gronwall
inputs remain named inputs; no global thimble result is imported.

SPECIALIZE is retained: audit only the claimed extra estimate and its
stopping/measurability justification. C466q remains comparison, not an
input. No new lemma, bound, script, proof audit or Mathlib search was
performed. Full matching Mathlib coverage remains unchecked. Outcome
STALLED records confirmation of an existing assessment rather than
mathematical progress; the completed separate gate approval makes the
same exact audit actionable next turn. No essential source blocker or
changed mathematical target was found. No further approval loop is
nominated.
