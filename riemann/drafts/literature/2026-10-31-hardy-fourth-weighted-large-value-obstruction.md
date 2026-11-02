# Actual-Hardy fourth-weighted large values: completed source comparison

TARGET: Assess unconditional fourth-moment-weighted Hardy large-value bounds at |Z|>(log H)^2/256 as an obstruction test for L583's exceptional fourth-energy hypothesis.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched weighted fourth-moment tails, unconditional critical-line large deviations and the log-squared cutoff; inspected Heap--Soundararajan Corollaries 1--2, Arguin--Bailey Theorem 1 and its critical-line limitation, and Arguin--Creighton Theorem 1.1 with Section 2.2. Reused Curran/Fazzari coverage and narrow Hardy-route failures.
SOURCE_EVIDENCE: Arguin--Creighton arXiv:2603.01711v1 (2 March 2026), Theorem 1.1 p.2, notation p.4, Lemma 2.1 and Section 2.2/Proposition 2.2 pp.6--8, https://arxiv.org/pdf/2603.01711v1; Heap--Soundararajan arXiv:2007.13154v1, Corollaries 1--2 p.2, https://arxiv.org/pdf/2007.13154; Arguin--Bailey arXiv:2403.19803v2, Theorem 1 and following discussion, https://arxiv.org/html/2403.19803v2. Source proofs remain unaudited.
COMPARISON: The first source states an unconditional critical-line Gaussian lower tail for V asymptotic to alpha log log T, including fixed alpha=2, on [0,T]. Older fractional-moment and shifted-line results do not cover the exact question. Weighted fourth energy, dyadic transfer and L583's phase-set comparison still require a separate mathematical application.
GAP: No R_4(H) or actual exceptional-energy bound is proved here. Residual obligations are quantitative Gaussian specialization, cumulative-to-dyadic transfer with the moving cutoff, and comparison with L582's specified periodic g and L583's E_pair.
REASON: Newly inspected primary coverage permits a bounded application test with explicit manuscript qualifications. No tail calculation, reproof, maximal-set inclusion or new lemma was derived in this literature-only step. The continuation is nominated separately for approval.
LITERATURE_REASON: Startup REVIEW_REQUIRED target lacked unconditional scalar lower-tail coverage; prior conditional support and upper-moment assessments did not cover it.
SCOPE: Actual Hardy Z, real sufficiently large heights or an unbounded sequence sufficient to exclude an eventual-ray budget; ell=log H, cutoff ell^2/256, unchanged L582 unit bridge and P=H ell+1, L583's exact fourth budget. No RH or weighted CLT. The manuscript theorem is an unaudited import.

## Gap and bounded decision

The main gap remains actual-Xi all-degree positivity at unbounded heights.
The intermediate target tests the viability of L583's additional fourth-energy
assumption. An obstruction would redirect that sufficient support route,
leaving its conditional proof intact. It would not refute RH, all support
constructions, positive clipping or Xi transfer.

Retain the nominated quantity and discriminating threshold:

    R_4(H)=H^(-1) integral_H^(2H)
           |Z(t)|^4 1_{|Z(t)|>(log H)^2/256} dt;
    target: R_4(H) is not O((log H)^3).

Continue only with exact cutoffs, intervals and normalizations; otherwise
preserve the failed comparison and redirect. This review does not assert
the target or perform the proposed mathematical comparison.

## Primary theorem evidence

**Arguin--Creighton.** Louis-Pierre Arguin and Nathan Creighton,
*Lower bounds for the large deviations and moments of the Riemann zeta
function on the critical line*, [v1](https://arxiv.org/pdf/2603.01711v1),
Theorem 1.1, p.2: for fixed alpha>0, V~alpha log log T and sufficiently
large T, with positive K_alpha,

    T^(-1) meas{t in [0,T]: log|zeta(1/2+it)|>V}
      >= K_alpha integral_V^infinity
           exp(-y^2/(log log T))/sqrt(log log T) dy.

No RH premise; alpha=2 is included. Section 1.4 confirms [0,T].
Read Section 2.2's alpha>=1 case: good-event mollifier comparison,
conditional Paley--Zygmund step, all three restricted-moment estimates
of Proposition 2.2 and the final threshold choice; also Section 3.1's
upper/lower indicator cases. This is coverage, not an independent audit
of Section 3 or its arithmetic references. Equation (2.19) displays a
squared denominator, inconsistent with (1.7) and the following unnumbered
formula; PDF text and HTML agree on this discrepancy. Do not import
(2.19) as written or claim its repair. Only the stated Theorem 1.1 is
proposed as input. No effective onset or direct dyadic conclusion.

**Older unconditional inputs.** Winston Heap and K. Soundararajan,
*Lower bounds for moments of zeta and L-functions revisited*,
[v1](https://arxiv.org/pdf/2007.13154), Corollaries 1--2, p.2.
Corollary 1 gives two-sided dyadic moment bounds of order
T(log T)^(k^2) for (log T)^(-1/2)<=k<=2. Corollary 2 controls
unweighted large-value measures only in the range

    sqrt(log log T) log log log T <= V
      <= 2 log log T-2 sqrt(log log T) log log log T,

with an error in the exponential. The upper endpoint does not include
V=2 log log T-log 256 on an eventual ray. Full statements were inspected;
no new consequence from their moment bounds was derived.

Louis-Pierre Arguin and Emma Bailey,
*Lower Bounds for the Large Deviations of Selberg's Central Limit
Theorem*, [v2](https://arxiv.org/html/2403.19803v2), Theorem 1 and
following discussion: the deviation statement is at
sigma=1/2+delta/log T, with delta sufficiently large depending on alpha.
The authors explicitly do not extend that method to delta=0. Its
critical-line moment corollary is not the required tail statement.

**Reused inputs.** Curran v1 Theorem 1/Proposition 1 and the Hardy
conversion are retained from the completed scalar-saturation assessment:
upper joint moments of Z,Z', not the missing lower tail. Reuse Fazzari
v1 Theorem 1/Proposition 2.1 from the joint-Hardy assessment: the weighted
CLT retains RH even in known twisted-moment cases. No conditional CLT,
log-normal heuristic, random-phase law or typical-value CLT is substituted.

## Searches, duplicates and continuation boundary

Queries included `Fazzari weighted central limit theorem zeta fourth
moment unconditional log zeta`; `zeta fourth moment weighted large
values log T squared lower bound`; `zeta unconditional large values
measure log zeta 2 log log log lower bound`; and the exact titles of
the three inspected primary papers. Abstracts and third-party copies
served only as leads. The primary arXiv record for Arguin--Creighton
lists v1, submitted 2 March 2026, 26 pages. Primary PDF and HTML were
opened. PDF screenshot retrieval failed; primary text was available,
so access is not an essential blocker. No other lead is an input.

Narrow local comparison covered L583's exact hypotheses, L582's
specified segment/bridge and period, scalar-saturation and spatial-
truncation assessments, and the joint-Hardy substitution stop. No
matching Arguin--Creighton application was found in these route files;
this is not an exhaustive novelty claim. Earlier scalar-cutoff bridge
and joint-law stops retain their different hypotheses and evidence.
No cross-notebook input. Matching Mathlib coverage is unchecked;
absence is not asserted.

The [continuation scope](2026-10-31-hardy-fourth-tail-application-scope.md)
nominates only the residual application, pending separate approval.
It must respect the cumulative interval, strict threshold, eventual-ray
quantifiers and period normalization. The source proof and displayed
discrepancy remain qualifications, not a newly verified local theorem.
No justified central creative sign mechanism emerges: this is an
established-theorem specialization at a conditional support interface.
No lemmas/, scripts/, DAG or PROOF edits were made.
