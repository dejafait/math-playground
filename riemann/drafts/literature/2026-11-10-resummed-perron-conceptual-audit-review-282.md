# Actual moving-band Perron germs: conceptual-audit scope

TARGET: Audit L994's actual G_1/G_2 Perron-Cauchy representation, including degree normalization, all four jump signs, the exact continuum term and the locally uniform height limit.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the bounded exact/stronger-result searches and duplicate/failure comparison in review279, with unchanged primary-source approval in review280; this audit stays wholly within that construction's hypotheses and techniques.
SOURCE_EVIDENCE: Montgomery-Vaughan MNT I section5.1 Theorems5.1-5.2/Corollary5.3 pp137-140 https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/09.0_pp_137_167_Dirichlet_series_II.pdf ; DLMF https://dlmf.nist.gov/18.12.E13 and https://dlmf.nist.gov/18.14.E8 ; their inspected contracts are in review279 and approved review280. L985 and L989 provide the exact kernel and global normalization.
COMPARISON: The existing ready source scope covers the same Laguerre extraction, complex-coefficient truncated Perron formula and degree/height domination now specialized in L994; audit the specialization rather than reprove the general theorems.
GAP: Independently verify that L994's logarithmic kernel and explicit remainder recover the actual moving-band coefficients, with every jump and compensator and no unproved uniform separation or absolute infinite-height convergence.
REASON: The common-line and two-limit passage are load-bearing analytic claims; a conceptual audit is needed before the proposed signed interface can support a new central mechanism. Separate source approval completed in step283; it does not certify the proof.
SCOPE: Exactly L994 on |z|<1/(4*exp(2)), actual Lambda with all powers, n>=2, r=1,2, |w|=1/4, Re(s)=1 and symmetric height limits. No spectral deformation, infinite-zero representation, singularity persistence, sign estimate or RH transfer.

## Reused coverage and audit contract

This is a new continuation record, not an extension of mathematical
source coverage or a second completed task in step282. The full prior
comparison is in [review279](2026-11-10-moving-band-degree-germ-review-279.md),
and its direct primary-source approval is in
[review280](2026-11-10-resummed-perron-cauchy-construction-review-280.md).
No further search or unread theorem is claimed. The old centered-Vaughan
stop244 and unfinished inverse working271 retain their scope.

Inputs to inspect are L994 in full, L985's exact K_m identification,
L989's global bound and endpoint convention, and the cited Perron
contract. L990/C990a/L993 are downstream context, not premises of L994.
There is no cross-notebook input. Full matching Mathlib coverage remains
unchecked and unknown.

Check the degree factors w^(-m)/(m-1), including n=2 for r=1,2;
the common absolute-convergence line for both Dirichlet series; the
branch and removable-value conventions for S_1,S_2; the signs of every
full-prefix conversion; and the -r*S_r(z) term in C_r. Reconstruct the
finite-degree/finite-height identity before assessing either limit.
In particular verify that excluding q=x from the near error is compatible
with the retained half jump and the complete source remainder, that
the same constants work for every w on the circle, and that the bound
in L994(13) makes the degree tail uniform in height. A pointwise Perron
formula or a numerical contour sample cannot replace that argument.

Accept only if the actual coefficient identity and every interchange
survive the audit. Repair a real mathematical error if possible within
this same source scope; otherwise isolate the failed claim and preserve
the original construction. Do not infer impossibility of the interface
from failure of one bound. No new signed or singularity theorem is
authorized by this assessment. Any such target needs REVIEW_REQUIRED
coverage before a mathematical attempt.

Main gap and plausible use: L030-L032/C032a positivity and L966/L968
signed forcing remain open. A reliable actual interface could permit
a later bounded test of zero-term survival against analytic remainders;
actual outputs, both complements, inversion/interval transport and
L984(H) remain independent gaps. Creative work is currently blocked
by this unaudited interface and unassessed continuation/cancellation
hypotheses. It is not replaced by labeling this audit creative.

Recommended purpose after separate approval: proof_audit/conceptual_audit,
deep_research/xhigh. The critical issue is logical control of the two
limits, not arithmetic replay or candidate-solution review. The present
SPECIALIZE recommendation reuses already approved construction scope;
it does not constitute that independent approval or a correctness verdict.


## Separate source approval — step283, 10 November 2026

LITERATURE_REASON: The supervisor requires separate approval of this newly
prepared continuation. Reuse the ready comparison; check only the essential
primary contracts for the unchanged audit target, without another discovery search.

Reused review279's searches, duplicate comparison and stop244/working271
qualifications, and review280's approved construction scope. Read L994 fully
for scope, L985 through its exact kernel identification, L989 through its
global bound and endpoint convention, and step282's history. This is source
comparison, not an independent verification of those proofs.

Primary verification used the author-hosted Montgomery–Vaughan chapter,
2007 book, section5.1, printed pp138–140, Theorems5.1–5.2 and Corollary5.3
[primary PDF](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/09.0_pp_137_167_Dirichlet_series_II.pdf#page=2).
The first theorem uses c>max(0,sigma_c) and symmetric height limits.
The quantitative theorem uses c>max(0,sigma_a), x>0; its remainder
retains two strict near ranges. Read its far-range contours, both near
cases and the semicircular indentation at zero, plus the corollary proof.
The equality endpoint has half weight; it is excluded from the near sum
but retains the quantitative theorem's residual error. The proof estimates
scalar inversion errors before summing against absolute coefficient values;
no positivity or reality of coefficients is required. Thus complex
coefficients are within scope. These source facts permit auditing a common
c=1 specialization; they do not certify L994's family-uniform estimates.

Rechecked [DLMF18.12.13](https://dlmf.nist.gov/18.12.E13) and
[DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), live retrieval on the checked
date, using the version1.2.8 provenance already recorded in L989.
The generating function holds for coefficient variable modulus below one;
the inequality covers real nonnegative argument, alpha>=0 and nonnegative
integral degree. Alpha=2 is covered. Neither statement supplies moving-band
resummation or a uniform Perron-height passage. Reuse their proofs and
L985/L989's existing specialization; no general reproof is justified.

DECISION remains SPECIALIZE, now approved for exactly TARGET and SCOPE.
All essential source coverage for this audit is ready. No new theorem,
calculation, source obstruction or changed mathematical route was found.
The outcome is STALLED: this required approval repeats the adequate prior
coverage and must not be counted as an advance. L994 remains unaudited.
Full matching Mathlib coverage remains unchecked and unknown.

The next mathematical invocation must independently reconstruct L994's
finite-degree/finite-height identity and test every normalization, four
jump signs, continuum term, common-line estimate and height-uniform tail.
Accept only if the complete coefficient identity and limit survive; repair
within the approved scope or isolate a precise failure otherwise. Preserve
step282's construction and unfinished work. This review authorizes no
zero-singularity, spectral deformation or cancellation theorem. Those
uncovered targets require REVIEW_REQUIRED coverage. Creative priority is
blocked by the essential interface audit and unassessed remainder analyticity;
no routine source approval is relabeled creative. Actual signed positivity,
outputs, both complements, transport and L984(H) remain unpaid.
