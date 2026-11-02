# L643 weighted-annulus application — approved source coverage

TARGET: Critically audit L643's W_T=O(N^(2-1/80)) estimate, checking E_N conjugation invariance, Poisson edge leakage, exact-product growth and multiplicity-counted density summation against L018, L467 and L641.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged exact-W_T scope of drafts/literature/2026-11-01-vertical-pick-density-weighted-annulus.md; its primary source comparison and local failure searches cover all tools in L643. No new external search or source approval for a different mathematical mechanism is claimed.
SOURCE_EVIDENCE: Baluyot 2017 thesis Theorem 1.2.1 p.16 https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=183460&itemId=33320 ; Bellotti--Wong 2412.15470v2 Theorem 1.1 https://arxiv.org/pdf/2412.15470v2 ; Baranov--Zarouf v1 Section 1.1 https://arxiv.org/html/1310.1182v1 ; Baranov--Jaming--Kellay--Speckbacher v2 Section 3.1 https://arxiv.org/pdf/2304.02385v2 ; Camara et al. Section 4 https://link.springer.com/article/10.1007/s13324-020-00364-5 ; Poisson Theorem 10.3.1 https://complexanalysis.org/web/sec_poisson-integral-formula.html . Primary statements reopened 2026-11-01; previously inspected essential density cases reused, not independently re-audited.
COMPARISON: The sources provide uniform near-line density and standard finite rational, conjugation and Poisson tools; none of the inspected theorems supplies L643's assembled weighted mean. The audit stays within the previously covered hypotheses and techniques and must check the new quantitative specialization, not reprove a general source theorem.
GAP: L643 is locally proved but independently unaudited; check the half-plane antilinear action on E_N, both kernel diagonals, the monotone distinct-grid error, the entire Poisson edge integral, and the strict-threshold band sum with all occurrences. L641's unrelated arguments and the source manuscripts remain outside this audit.
REASON: A critical check of the newly assembled application is warranted before attempting simultaneous height selection. Separate literature approval is completed below; this does not approve L643's mathematical correctness.
SCOPE: Exactly L643's fixed H_N/E_N/F_N/W_T and its proof, with L018's zero correspondence/reflection, L467's total-count consequence, and only L641's finite kernel, spectral concentration and leakage inputs. No new zero-density theorem, actual-zero sign assertion, or favorable-height application is authorized by this assessment.

## Why the previous coverage is sufficient for the nominated audit

The prior assessment's SCOPE explicitly covers the fixed E_N, all
actual Xi zero occurrences with |Im(zeta)|<1/2, N=floor(log T),
finite rational kernels, model conjugation, contour/Poisson estimates
and finite spectral theory. Its covered target required exactly the
product-growth comparison, shrinking-displacement concentration and
weighted summation now written in L643. Auditing that application
does not change the weight, pole grid, density hypotheses or source
versions. The exact audit action above has now received the separate literature
coverage review recorded below; the prior assessment is preserved.

The canonical mathematical proof is
[L643](../../lemmas/L643-vertical-pick-density-weighted-annulus.md).
The reused [source comparison](2026-11-01-vertical-pick-density-weighted-annulus.md)
contains the queries, primary read ranges, strict-count convention,
uniformity and manuscript qualifications. There is no need for a
general weighted Maples--Rodgers theorem or an additional source search
unless the audit identifies an essential changed hypothesis.

The check must retain the numerical margins rho=21/20<11/10=2theta,
theta=11/20<4/7, delta_N=(log N)/(4N), core exponent 141/80 and
outer exponent 159/80. In particular it must not replace the
Poisson edge term by bare boundary leakage or double the product
exponent by discarding E_N's claimed conjugation invariance.

Check y=0 separately; the strict beta>sigma threshold is lowered by
1/N in the outer bands; the ordinate range is enlarged to (0,3T)
only after padding the X annulus. All zero orders and both signs of
horizontal displacement remain in the estimate. No actual-Xi signed
trace, spectral sign or RH conclusion is a premise or output here.

Continuation test: retain the saving only if every step, including
finite-space input specialization, is valid with constants independent
of the growing N and the band index. Repair a demonstrable error with
its actual quantitative effect, or withdraw the saving if a gap
cannot be closed within this scope. Do not infer failure of the signed
trace from failure of a majorant proof.

This is a conceptual proof audit, not a creative mechanism. A new
central signed-cancellation idea has not been supplied. The immediate
justified task is to scrutinize this advance before using it in the
still-open simultaneous count/trace selection. Full matching Mathlib
coverage remains unchecked, not absent.


## Separate coverage approval and URL repair — 1 November 2026

This literature-only recovery step supplies direct source URLs in
SOURCE_EVIDENCE and approves reuse for the exact TARGET. DECISION
remains SPECIALIZE. No mathematical proof audit has been performed.
The prior nomination and its numerical checks remain audit obligations.

Reopened the six primary URLs above. Read Baluyot's printed p.16
Theorem 1.2.1 and p.17's explicit unconditional qualification: fixed
0<theta<4/7, uniform sigma>=1/2, large height, theta-dependent constant.
The single-log density statement matches the nominated input; no
effective onset or new source theorem is asserted. Reuse the prior
assessment's inspected Sections 3.2/3.6 essential near-line cases and
multiplicity conventions rather than repeating manuscript extraction.

Reopened Bellotti--Wong v2 p.1 Theorem 1.1 (T>=e) and the beginning
of Baranov--Zarouf v1 Section 1.1. Read the upper-half-plane kernel
and diagonal in Baranov et al. v2 Section 3.1 (3.1)--(3.2). Their
Lebesgue norm differs from L641's dx/(2pi); normalization remains an
audit obligation. Read Camara et al., *Conjugations in L^2 and their
invariants*, Section 4's model-space preservation statement preceding
Proposition 4.1. This is a disk statement; it alone does not establish
L643's half-plane eigenspace invariance.

Read Poisson Theorem 10.3.1 and its proof: bounded piecewise continuous
real boundary data produce a harmonic extension with the stated
continuity-point boundary values. This statement alone does not prove
uniqueness for an arbitrary unbounded harmonic function, nor the
assembled complex rational or edge estimate. L643's decay/uniqueness,
conjugation, finite-product and band-sum applications still require
the exact saved audit. No new uniqueness theorem is imported here.

The existing assessment's duplicate/failure comparison is reused
unchanged: restricted L485 does not license arbitrary weighted sampling,
and deterministic boundary-transfer failures remain recorded. No new
search is needed for an unchanged target. Full matching Mathlib coverage
remains unchecked. No lemma, mathematical script, DAG or PROOF edit.

LITERATURE_REASON: Supervisor recovery requires direct primary URLs in this ready audit assessment and separate approval of reused coverage; this is the bounded repair, not further discovery on a ready mathematical target.

Outcome: STALLED as mathematical evidence; source accessibility and
metadata repair do not establish the weighted saving or reset a failed
mathematical route. Coverage is ready for the exact conceptual audit
next turn without another approval-only step.
