# Numerical signed-exponential truncation preflight1778

TARGET: Derive numerical uniform endpoint and full-tail bounds for C033j's Q_sigma from C032s(10)-(12), and test whether convolution orders at most128 and power-of-two cutoffs within [2^-256,2^256] give combined omitted-part error at most2^-20 for C033r's paired observable at n=1, delta=1/16, including lambda and signed-width TV<=2.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed comparison1778 for the parent direct-enclosure target; exact searches, local overlap, failure checks and unused leads are in drafts/literature/2026-11-19-paired-direct-enclosure-source-notes-1778.md. No claim of originality or full matching numerical algorithm.
SOURCE_EVIDENCE: Finite signed exponential and TV norm coverage: Cekanavicius-Vellaisamy2018 Section1 after(1), https://www.vmsta.org/journal/VMSTA/article/114/read; actual heat/counting input: Sra fixed2610.00584v1 Section2.1/(2.1)-(2.3), Lemma2.1 complete proof and PropositionB.1 proof, https://hexagonmath.org/pdf/2610.00584v1; existing quantitative specialization C032s(8)-(12), and C033m(3)-(5); Gaussian identity coverage reused from notes1740/1764.
COMPARISON: C032s's existing two-sided absolute inequalities are numerical, although its concluded difference/sign statement uses only widths1,2. They may be used to attempt uniform absolute width bounds without differentiating asymptotic remainders. The signed-exponential norm framework alone does not give the requested numerical budget. This is local application development, not a new general exponential or heat theorem.
GAP: Obtain explicit all-width constants and both cutoff errors, control the normalization scalar and omitted convolution orders for both R_sigma and lambda, and pay the signed-width cap in one combined absolute allowance. Prove or fail the displayed budget; no bound is established by this assessment.
REASON: Concrete numerical input inequalities and known signed-series tools are available before invocation; only their bounded application is approved. This newly written ready continuation requires separate next-turn approval. Stop on an unnamed constant or a failed displayed budget; do not launch literal high-dimensional enumeration or a full separator search.
SCOPE: W=[1,2], X=[0,infinity), exact Q_sigma=(ell_sigma-ell_1)dt, normalized R_sigma and C033i's lambda/P; fixed base Gaver n=1, delta=1/16 only. Spatial cuts bound omitted measure parts, not merely the observed sum variable. Keep the zero atoms and all signed coefficients. Compact quadrature errors, numerical function values, B/L/J parameter selection, full runtime and actual-Xi positivity are outside this preflight.

The main gap is actual-Xi all-degree positivity. A numerical omitted-part
certificate would pay one concrete missing input for a later direct
observable enclosure. It is useful even while compact evaluation and
the genuine separating choice of delta,n remain unresolved. The fixed
n=1 test is not claimed to have a positive separator gap.

Use the complete inspected evidence in
[source-notes1778](2026-11-19-paired-direct-enclosure-source-notes-1778.md).
The cited C032s inequalities are already proved canonical inputs; their
extension to the continuum and their integrated error costs are the
mathematical task, not conclusions of this review. No positivity of
Q_sigma, R_sigma or signed eta, undamped moments, global inverse or
numerical heat-asymptotic constant may be assumed. No reproof of the
source counting theorem, Gaussian identity or measure-exponential
framework is needed. Explain every new specialization explicitly.

The budget128 and cutoff range are a finite preflight discriminator,
not a universal lower bound or a claim that compact evaluation is
feasible. Preserve failed bounds if it does not pass; a larger-budget
retry needs a materially sharper input or a refined mechanism. If it
passes, nominate the separately uncovered compact-evaluation problem
with REVIEW_REQUIRED rather than silently implementing an evaluator.
Existing stop1571, stop1576, closure1768 and unfinished C033k remain.

Retain actual divisor, conjugation/multiplicity, excluded ordinate zero,
strict strip, gamma>14, explicit counting, through100 real-zero input,
retained real zero, reciprocal-square tail, heat positivity, separately
controlled fixed-j errors through j=2, Gaussian half-variance and both
fixed-v1 qualifications. Numerical-data and source-wide correctness
are not independently certified. Full matching Mathlib coverage remains
unchecked/unknown. This is routine quantitative specialization and
calculation, not a creative central-gap mechanism or an RH candidate.
